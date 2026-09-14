#!/usr/bin/env python3
"""
Rare Earth Literature Monitor

Searches OpenAlex for recent publications that mention rare earth elements,
screens each candidate for relevance to REE separation with an LLM (the
`claude` CLI), and writes a categorized markdown report.

Pipeline:
    1. OpenAlex title/abstract search for REE terms, every page of results
    2. Drop duplicates (version DOIs, repository copies) and future-dated works
    3. Keyword prefilter: the title or abstract must name an REE
    4. LLM relevance pass: score 0-3, assign a category; keep scores >= 2

Usage:
    python literature_monitor.py                    # Last 7 days
    python literature_monitor.py --days 30          # Last 30 days
    python literature_monitor.py --output report.md # Custom output file
    python literature_monitor.py --slack            # Send notification to Slack
    python literature_monitor.py --data-out run.json    # Save works for later
    python literature_monitor.py --slack-from run.json  # Notify from saved works
    python literature_monitor.py --no-llm           # Skip the relevance pass

Environment Variables:
    OPENALEX_API_KEY   - Raises the OpenAlex rate limits (optional)
    CLAUDE_BIN         - Path to the claude CLI (default: found on PATH)
    SLACK_WEBHOOK_URL  - Incoming webhook URL for simple notifications
    SLACK_BOT_TOKEN    - Bot token for file uploads (optional)
    SLACK_CHANNEL      - Channel ID for file uploads (optional)
"""

import argparse
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
import urllib.error
import urllib.parse
import urllib.request

# OpenAlex title/abstract searches. Together these cast a wide net: anything
# that names a rare earth is a candidate, and the LLM pass decides what is
# relevant. Searching titles and abstracts (not fulltext) keeps out papers
# that mention a rare earth once in passing.
SEARCH_QUERIES = [
    '"rare earth" OR "rare earths" OR "rare-earth" OR lanthanide OR lanthanoid'
    ' OR lanmodulin OR "f-element"',
    "lanthanum OR cerium OR praseodymium OR neodymium OR promethium OR samarium"
    " OR europium OR gadolinium OR terbium OR dysprosium OR holmium OR erbium"
    " OR thulium OR ytterbium OR lutetium OR scandium OR yttrium",
    'NdFeB OR "Nd-Fe-B" OR Nd2Fe14B OR monazite OR bastnasite OR bastnäsite'
    ' OR xenotime OR "ion-adsorption"',
]

# GitHub repository for report hosting
GITHUB_REPO_URL = "https://github.com/KitchinHUB/ree-literature-updates"

_ELEMENT_NAMES = (
    "lanthanum|cerium|praseodymium|neodymium|promethium|samarium|europium|"
    "gadolinium|terbium|dysprosium|holmium|erbium|thulium|ytterbium|lutetium|"
    "scandium|yttrium"
)

# A candidate must name a rare earth in its title, abstract, or keywords. All
# matches are whole words: plain substrings let "three" pass as "ree " and
# "1859 CE" pass as cerium.
REE_MENTION_PATTERNS = [
    re.compile(
        r"\b(rare[- ]earths?|lanthanides?|lanthanoids?|actinides?|lanmodulin|"
        r"f-elements?|f-block|4f|" + _ELEMENT_NAMES + r"|"
        r"ndfeb|nd-fe-b|nd2fe14b|monazite|bastn[aä]site|xenotime|ion-adsorption)\b",
        re.IGNORECASE,
    ),
    # Case-sensitive, so "REE" is not "Ree" or "three".
    re.compile(r"\bREEs?\b"),
    # Element symbols that are rarely ordinary words, as whole words: "Nd doping",
    # "Ce(III)", "Dy2Co3Ge5". Case-sensitive, so "CE" (the era) does not count.
    re.compile(r"(?<![A-Za-z])(Ce|Nd|Pm|Sm|Gd|Tb|Dy|Tm|Yb|Lu)(?![a-z])"),
    # Symbols that double as words in other languages ("La", "Eu") or English
    # ("Pr", "Er", "Y") count only in a chemical context: a stoichiometry digit,
    # a charge or oxidation state, a dopant suffix, or a slash pair like "Nd/Pr".
    re.compile(
        r"(?<![A-Za-z])(La|Eu|Pr|Ho|Er|Sc|Y)"
        r"(?=\s?\d|[³⁺]|\s?\((?:II|III|IV)\)|[2-4]\+|-(?:doped|based|containing)|/[A-Z])"
    ),
    re.compile(r"(?<=[/-])(La|Eu|Pr|Ho|Er|Sc|Y)(?![a-z])"),
]

# The LLM relevance pass. Papers scoring at or above the threshold go in the
# report; the rest are listed, collapsed, at the end so the screening can be
# audited.
LLM_MODEL = "sonnet"
RELEVANCE_THRESHOLD = 2
LLM_BATCH_SIZE = 25
LLM_WORKERS = 4
LLM_TIMEOUT = 600      # seconds per batch
LLM_ATTEMPTS = 3
LLM_ABSTRACT_CHARS = 1500

CATEGORIES = [
    "Separation Technologies",
    "Extractants & Materials",
    "Recycling & Urban Mining",
    "Environmental & Sustainability",
    "Supply Chain & Policy",
    "Other",
]

LLM_SYSTEM_PROMPT = """\
You screen new scientific publications for a weekly literature update on rare
earth element (REE) separation. The readers are a research group working on how
REEs are extracted, separated, refined, and recycled, and on the supply chain
around them. Judge each paper only from the metadata given. Be strict: a paper
that uses a rare earth as a dopant, phosphor, magnet, catalyst, or alloy
component, without being about obtaining or separating it, is not relevant."""

LLM_INSTRUCTIONS = """\
Score every paper below for relevance, using this scale:

3 - Directly about REE separation, extraction, leaching, refining, metal
    production, or recycling, or about designing extractants, ligands, or
    sorbents for REEs.
2 - Substantively about REEs in a way that informs separations or supply:
    lanthanide coordination and selectivity chemistry, actinide-lanthanide
    separation, REE ore processing or beneficiation, lanthanide biochemistry
    relevant to biorecovery, REE supply chains, policy, mining, or the
    environmental impact of REE mining and processing.
1 - REEs appear only as a component or application (doped materials,
    phosphors, magnet physics, catalysts, alloys, medical imaging), or the
    paper is about critical minerals generally with no REE focus.
0 - Not about rare earths at all.

Assign each paper one category:
- Separation Technologies: solvent extraction, ion exchange, chromatography,
  membranes, electrochemical or molten-salt processes, precipitation, leaching.
- Extractants & Materials: extractants, ligands, sorbents, and the selectivity
  chemistry behind them, including computational screening.
- Recycling & Urban Mining: recovery from magnets, e-waste, industrial wastes,
  tailings, and other secondary sources.
- Environmental & Sustainability: environmental impact, toxicity, and life
  cycle of REE mining, processing, and use.
- Supply Chain & Policy: markets, geopolitics, policy, mining projects.
- Other: anything else, including every paper scored 0 or 1.

Give a one-sentence reason (at most 25 words) that says what the paper does
and why that earns its score. Return exactly one entry per paper id.

Papers (JSON lines):
"""

LLM_SCHEMA = {
    "type": "object",
    "properties": {
        "papers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "score": {"type": "integer", "enum": [0, 1, 2, 3]},
                    "category": {"type": "string", "enum": CATEGORIES},
                    "reason": {"type": "string"},
                },
                "required": ["id", "score", "category", "reason"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["papers"],
    "additionalProperties": False,
}


# Retry policy for the OpenAlex API. It returns 503 during maintenance and
# 429 when the polite-pool rate limit is hit; both clear on their own, so a
# failed topic should not silently produce a thin report.
class OpenAlexUnavailable(Exception):
    """Raised when a topic query cannot be completed, even after retries."""


class OpenAlexQuotaExhausted(OpenAlexUnavailable):
    """Raised when the daily credit quota is spent; retrying is pointless."""


MAX_ATTEMPTS = 5
# Results per page is capped at 200 by OpenAlex. A week is two or three pages
# per query; the page cap only guards against a runaway --days value.
PER_PAGE = 200
MAX_PAGES_PER_QUERY = 25
RETRY_BASE_DELAY = 2.0   # seconds; doubles each attempt
RETRY_MAX_DELAY = 60.0   # cap on an exponential backoff step
RETRYABLE_STATUS = {429, 500, 502, 503, 504}

# Client-side throttling. Firing the topic queries back to back trips
# OpenAlex's short-window limit, so space requests out, and widen the spacing
# whenever the server pushes back with a 429.
MIN_REQUEST_INTERVAL = 1.5    # seconds between requests
MAX_REQUEST_INTERVAL = 15.0   # ceiling for the widened spacing
# A 429 whose Retry-After is at most this long is a short-window throttle and
# is waited out. Anything longer means the daily quota is gone.
MAX_RATE_LIMIT_WAIT = 600.0
# Queries that fail on the first pass get one more try after this cooldown.
FAILED_QUERY_COOLDOWN = 90.0


class _Throttle:
    """Keeps a minimum interval between OpenAlex requests."""

    def __init__(self, interval: float):
        self.interval = interval
        self._last = 0.0
        self.quota_exhausted = False

    def wait(self):
        remaining = self._last + self.interval - time.monotonic()
        if remaining > 0:
            time.sleep(remaining)
        self._last = time.monotonic()

    def back_off(self):
        self.interval = min(self.interval * 2, MAX_REQUEST_INTERVAL)


_throttle = _Throttle(MIN_REQUEST_INTERVAL)


def _parse_seconds(value: Optional[str]) -> Optional[float]:
    try:
        return float(value) if value is not None else None
    except ValueError:
        return None  # Retry-After can be an HTTP date


def query_openalex(
    query: str,
    from_date: str,
    to_date: str,
    cursor: str = "*",
    per_page: int = PER_PAGE,
) -> dict:
    """
    Fetch one page of OpenAlex works whose title or abstract matches the query.

    Args:
        query: Boolean search string (quoted phrases, OR)
        from_date: ISO date string (YYYY-MM-DD), start of the window
        to_date: ISO date string, end of the window. Always bounded: publishers
            post works dated weeks or months ahead, and those belong to the
            week they are dated in.
        cursor: Pagination cursor ("*" for the first page)
        per_page: Results per page

    Returns:
        API response as dict
    """
    base_url = "https://api.openalex.org/works"

    params = {
        "filter": (
            f"from_publication_date:{from_date},to_publication_date:{to_date},"
            f"title_and_abstract.search:{query}"
        ),
        "per-page": str(per_page),
        "cursor": cursor,
        "mailto": "jkitchin@andrew.cmu.edu",  # Polite pool
    }
    # A key raises the limits well above the anonymous pool. Cron has no login
    # environment, so weekly_update.sh loads it from .env.
    api_key = os.environ.get("OPENALEX_API_KEY")
    if api_key:
        params["api_key"] = api_key

    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "LiteratureMonitor/1.0"})

    if _throttle.quota_exhausted:
        raise OpenAlexQuotaExhausted("daily quota exhausted earlier in this run")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        retry_after = None
        _throttle.wait()
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                remaining = _parse_seconds(response.headers.get("X-RateLimit-Remaining"))
                if remaining is not None and remaining <= 0:
                    # This request got through, but the next one will not.
                    _throttle.quota_exhausted = True
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as e:
            if e.code not in RETRYABLE_STATUS:
                # 4xx client errors will not fix themselves; fail fast.
                raise OpenAlexUnavailable(f"HTTP {e.code}") from e
            headers = e.headers or {}
            retry_after = _parse_seconds(headers.get("Retry-After"))
            reason = f"HTTP {e.code}"
            if e.code == 429:
                _throttle.back_off()
                remaining = _parse_seconds(headers.get("X-RateLimit-Remaining"))
                # Only a long wait, or the server saying no credits remain,
                # means the daily quota is spent. A short Retry-After is a
                # burst throttle and is worth waiting out.
                if (retry_after is not None and retry_after > MAX_RATE_LIMIT_WAIT) or (
                    remaining is not None and remaining <= 0
                ):
                    _throttle.quota_exhausted = True
                    reset = _parse_seconds(headers.get("X-RateLimit-Reset")) or retry_after
                    when = f", resets in {reset / 3600:.1f}h" if reset else ""
                    raise OpenAlexQuotaExhausted(f"daily quota exhausted{when}") from e
                reason = "rate limited"
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            reason = str(e)

        if attempt == MAX_ATTEMPTS:
            raise OpenAlexUnavailable(
                f"{reason} after {MAX_ATTEMPTS} attempts"
            )

        # Honor Retry-After in full when sent (it is bounded above); otherwise
        # exponential backoff. Jitter either way.
        if retry_after is not None:
            delay = retry_after
        else:
            delay = min(RETRY_BASE_DELAY * (2 ** (attempt - 1)), RETRY_MAX_DELAY)
        delay += random.uniform(0, 1.0)

        print(
            f"    {reason}, retrying in {delay:.1f}s "
            f"(attempt {attempt}/{MAX_ATTEMPTS})"
        )
        time.sleep(delay)

    # Unreachable: the final attempt always returns or raises above.
    raise OpenAlexUnavailable("exhausted retries")


def search_openalex_all_queries(
    from_date: str, to_date: str
) -> tuple[list[dict], list[str]]:
    """
    Run every search query, following pagination to the last page.

    Returns:
        Tuple of (works deduplicated by OpenAlex id, queries that failed)
    """
    all_works = {}

    def fetch_all_pages(query: str) -> None:
        cursor = "*"
        for page in range(1, MAX_PAGES_PER_QUERY + 1):
            result = query_openalex(query, from_date, to_date, cursor=cursor)
            for work in result.get("results", []):
                work_id = work.get("id", "")
                if work_id and work_id not in all_works:
                    all_works[work_id] = work
            cursor = (result.get("meta") or {}).get("next_cursor")
            if not cursor or not result.get("results"):
                return
        count = (result.get("meta") or {}).get("count", "?")
        print(
            f"    Warning: stopped after {MAX_PAGES_PER_QUERY} pages "
            f"({count} matches); narrow the date window to see them all"
        )

    def search(queries: list[str]) -> list[str]:
        failed = []
        for query in queries:
            print(f"  Searching OpenAlex: {query[:70]}...")
            before = len(all_works)
            try:
                fetch_all_pages(query)
            except OpenAlexUnavailable as e:
                # A partly fetched query is still a failed one: its remaining
                # pages are missing. Works already fetched are kept, and the
                # retry skips over them.
                print(f"    FAILED: {e}")
                failed.append(query)
                continue
            print(f"    {len(all_works) - before} new works")
        return failed

    failed_queries = search(SEARCH_QUERIES)

    # Transient throttling and outages usually clear within a minute or two,
    # so give failed queries a second pass before counting them as lost.
    if failed_queries and not _throttle.quota_exhausted:
        print(
            f"\n  {len(failed_queries)} query(ies) failed; retrying after "
            f"{FAILED_QUERY_COOLDOWN:.0f}s cooldown"
        )
        time.sleep(FAILED_QUERY_COOLDOWN)
        failed_queries = search(failed_queries)

    return list(all_works.values()), failed_queries


def extract_work_info(work: dict) -> dict:
    """Extract relevant information from an OpenAlex work."""
    # Get authors (first 5; author_count says whether there are more)
    authors = []
    # Some repository records list a placeholder author named "et al.".
    authorships = [
        a for a in (work.get("authorships") or [])
        if ((a.get("author") or {}).get("display_name") or "").strip().lower()
        not in {"et al.", "et al", "others"}
    ]
    for authorship in authorships[:5]:
        author = authorship.get("author") or {}
        name = author.get("display_name") or "Unknown"
        authors.append(name)

    # Get primary source/journal
    source = (work.get("primary_location") or {}).get("source") or {}
    journal = source.get("display_name") or "Unknown Source"

    # Get DOI
    doi = work.get("doi") or ""
    if doi and not doi.startswith("http"):
        doi = f"https://doi.org/{doi}"

    # Get abstract
    abstract = ""
    if work.get("abstract_inverted_index"):
        # Reconstruct abstract from inverted index
        inv_index = work["abstract_inverted_index"]
        words = [""] * (max(max(positions) for positions in inv_index.values()) + 1)
        for word, positions in inv_index.items():
            for pos in positions:
                words[pos] = word
        abstract = " ".join(words)

    # Keywords are OpenAlex's current tagging. The legacy concepts field it
    # replaced produced tags like "Mercury (programming language)".
    keywords = [
        k.get("display_name") or "" for k in (work.get("keywords") or [])[:5]
    ] or [
        t.get("display_name") or "" for t in (work.get("topics") or [])[:3]
    ]

    # Use `or` rather than get() defaults: OpenAlex returns these keys with
    # explicit null values, which a default would not catch.
    work_id = work.get("id") or ""

    return {
        "id": work_id,
        "title": work.get("title") or "Untitled",
        "authors": authors,
        "author_count": len(authorships),
        "publication_date": work.get("publication_date") or "",
        "journal": journal,
        "doi": doi,
        "url": work_id.replace("https://openalex.org/", "https://openalex.org/works/"),
        "abstract": abstract,
        "keywords": keywords,
        "cited_by_count": work.get("cited_by_count") or 0,
        "type": work.get("type") or "unknown",
        "open_access": (work.get("open_access") or {}).get("is_oa", False),
    }


def deduplicate_works(works: list[dict]) -> list[dict]:
    """
    Collapse records of the same work under different OpenAlex ids.

    Repositories mint a DOI per version (figshare ".v1", Zenodo concept and
    version DOIs), and OpenAlex indexes each. Records match on normalized
    title; short generic titles ("Editorial", "Preface") also need the same
    first-author surname. Author names are not compared for long titles
    because copies spell them differently ("PhD Antonio Pereira" and
    "Antonio Pereira, PhD"). The kept record prefers a publisher DOI over a
    repository one, then an unversioned DOI, then one with an abstract.
    """
    def key(work: dict) -> tuple[str, str]:
        title = re.sub(r"[^\w]+", "", work["title"].lower())
        if len(title) >= 40:
            return title, ""
        first = work["authors"][0].split()[-1].lower() if work["authors"] else ""
        return title, first

    def quality(work: dict) -> tuple[bool, bool, bool, bool]:
        doi = work["doi"]
        return (
            bool(doi) and not re.search(r"10\.(5281/zenodo|6084/m9\.figshare)", doi),
            bool(doi) and not re.search(r"\.v\d+$", doi),
            bool(work["abstract"]),
            bool(doi),
        )

    best: dict[tuple[str, str], dict] = {}
    for work in works:
        k = key(work)
        if k not in best or quality(work) > quality(best[k]):
            best[k] = work
    return list(best.values())


def mentions_ree(work: dict) -> bool:
    """True if the title, abstract, or keywords name a rare earth element."""
    text = " ".join(
        [work.get("title") or "", work.get("abstract") or ""]
        + (work.get("keywords") or [])
    )
    return any(pattern.search(text) for pattern in REE_MENTION_PATTERNS)


class LLMScreeningError(Exception):
    """Raised when the relevance pass cannot score every candidate."""


def _find_claude() -> str:
    claude = os.environ.get("CLAUDE_BIN") or shutil.which("claude")
    if not claude:
        # Cron's PATH does not include the default install location.
        fallback = Path.home() / ".local" / "bin" / "claude"
        if fallback.exists():
            claude = str(fallback)
    if not claude:
        raise LLMScreeningError(
            "claude CLI not found; set CLAUDE_BIN or pass --no-llm"
        )
    return claude


def _screen_batch(claude: str, batch: list[tuple[int, dict]], model: str) -> dict:
    """Score one batch; returns {id: {score, category, reason}}."""
    lines = []
    for paper_id, work in batch:
        abstract = work["abstract"]
        if len(abstract) > LLM_ABSTRACT_CHARS:
            abstract = abstract[:LLM_ABSTRACT_CHARS] + "..."
        lines.append(json.dumps({
            "id": paper_id,
            "title": work["title"],
            "venue": work["journal"],
            "type": work["type"],
            "keywords": work["keywords"],
            "abstract": abstract or "(no abstract)",
        }, ensure_ascii=False))
    prompt = LLM_INSTRUCTIONS + "\n".join(lines)

    cmd = [
        claude, "-p",
        "--model", model,
        "--output-format", "json",
        "--json-schema", json.dumps(LLM_SCHEMA),
        "--system-prompt", LLM_SYSTEM_PROMPT,
        # A pure judgment call: no tools, MCP servers, hooks, or saved session.
        "--tools", "",
        "--strict-mcp-config",
        "--setting-sources", "",
        "--no-session-persistence",
    ]
    expected = {paper_id for paper_id, _ in batch}
    error = "no attempts made"

    for attempt in range(1, LLM_ATTEMPTS + 1):
        try:
            # Run outside the project so no CLAUDE.md is picked up.
            with tempfile.TemporaryDirectory() as cwd:
                proc = subprocess.run(
                    cmd, input=prompt, capture_output=True, text=True,
                    timeout=LLM_TIMEOUT, cwd=cwd,
                )
            response = json.loads(proc.stdout)
            if response.get("is_error"):
                raise LLMScreeningError(response.get("result") or "claude reported an error")
            papers = (response.get("structured_output") or {}).get("papers") or []
            scored = {p["id"]: p for p in papers if p.get("id") in expected}
            missing = expected - scored.keys()
            if missing:
                raise LLMScreeningError(f"no score for {len(missing)} paper(s)")
            return scored
        except (subprocess.TimeoutExpired, json.JSONDecodeError, LLMScreeningError) as e:
            error = str(e) or type(e).__name__
            print(f"    LLM batch failed ({error}), attempt {attempt}/{LLM_ATTEMPTS}")
            if attempt < LLM_ATTEMPTS:
                time.sleep(RETRY_BASE_DELAY * 2 ** attempt)

    raise LLMScreeningError(error)


def screen_with_llm(works: list[dict], model: str = LLM_MODEL) -> None:
    """
    Score every work for relevance with the claude CLI, in parallel batches.

    Sets "relevance", "category", and "relevance_reason" on each work in place.
    Raises LLMScreeningError if any batch cannot be scored: an unscreened
    report is the thing this step exists to prevent.
    """
    claude = _find_claude()
    indexed = list(enumerate(works))
    batches = [
        indexed[i:i + LLM_BATCH_SIZE] for i in range(0, len(indexed), LLM_BATCH_SIZE)
    ]
    print(
        f"  Screening {len(works)} candidates with {model} "
        f"({len(batches)} batches)..."
    )

    with ThreadPoolExecutor(max_workers=LLM_WORKERS) as pool:
        results = list(pool.map(lambda b: _screen_batch(claude, b, model), batches))

    for scored in results:
        for paper_id, verdict in scored.items():
            work = works[paper_id]
            work["relevance"] = verdict["score"]
            work["category"] = verdict["category"] if verdict["score"] >= RELEVANCE_THRESHOLD else "Other"
            work["relevance_reason"] = verdict["reason"]


def _category_keyword_fallback(work: dict) -> str:
    """Category for unscreened (--no-llm) runs, from title and abstract."""
    text = f"{work['title']} {work['abstract']}".lower()
    rules = [
        ("Recycling & Urban Mining", r"\b(recycl\w*|urban mining|e-waste|end-of-life)"),
        ("Extractants & Materials", r"\b(extractants?|ionic liquids?|eutectic|ligands?|sorbents?|adsorbents?)\b"),
        ("Separation Technologies", r"\b(separat\w*|solvent extraction|ion exchange|chromatograph\w*|leach\w*|membranes?)"),
        ("Supply Chain & Policy", r"\b(supply chains?|polic\w+|geopolitic\w*|export)"),
        ("Environmental & Sustainability", r"\b(environmental|sustainab\w+|toxic\w*|pollution|life cycle)"),
    ]
    for category, pattern in rules:
        if re.search(pattern, text):
            return category
    return "Other"


def categorize_works(works: list[dict]) -> dict[str, list[dict]]:
    """
    Group works by category, most relevant then newest first within each.

    Uses the category from the LLM pass when present.
    """
    categories = {name: [] for name in CATEGORIES}
    for work in works:
        category = work.get("category") or _category_keyword_fallback(work)
        categories.get(category, categories["Other"]).append(work)

    for cat_works in categories.values():
        cat_works.sort(key=lambda w: w["publication_date"], reverse=True)
        cat_works.sort(key=lambda w: w.get("relevance", 0), reverse=True)

    # Remove empty categories
    return {k: v for k, v in categories.items() if v}


# =============================================================================
# Slack Integration
# =============================================================================

def send_slack_webhook(
    webhook_url: str,
    message: str,
    blocks: list = None,
    attachments: list = None
) -> bool:
    """
    Send a message to Slack via incoming webhook.

    Args:
        webhook_url: Slack incoming webhook URL
        message: Fallback text message
        blocks: Optional Block Kit blocks for rich formatting
        attachments: Optional attachments

    Returns:
        True if successful, False otherwise
    """
    payload = {"text": message}

    if blocks:
        payload["blocks"] = blocks
    if attachments:
        payload["attachments"] = attachments

    data = json.dumps(payload).encode("utf-8")

    try:
        req = urllib.request.Request(
            webhook_url,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.status == 200
    except Exception as e:
        print(f"Warning: Slack webhook failed: {e}")
        return False


def upload_slack_file(
    token: str,
    channel: str,
    file_path: Path,
    title: str = None,
    initial_comment: str = None
) -> bool:
    """
    Upload a file to Slack using the Bot API.

    Args:
        token: Slack Bot OAuth token
        channel: Channel ID to upload to
        file_path: Path to file to upload
        title: Optional title for the file
        initial_comment: Optional message to accompany the file

    Returns:
        True if successful, False otherwise
    """
    url = "https://slack.com/api/files.upload"

    # Read file content
    with open(file_path, "rb") as f:
        file_content = f.read()

    # Build multipart form data manually (avoiding external dependencies)
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"

    body_parts = []

    # Add channel
    body_parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="channels"\r\n\r\n{channel}')

    # Add title if provided
    if title:
        body_parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="title"\r\n\r\n{title}')

    # Add initial comment if provided
    if initial_comment:
        body_parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="initial_comment"\r\n\r\n{initial_comment}')

    # Add filename
    filename = file_path.name
    body_parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="filename"\r\n\r\n{filename}')

    body = "\r\n".join(body_parts).encode("utf-8")
    body += f'\r\n--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{filename}"\r\nContent-Type: text/markdown\r\n\r\n'.encode("utf-8")
    body += file_content
    body += f"\r\n--{boundary}--\r\n".encode("utf-8")

    try:
        req = urllib.request.Request(
            url,
            data=body,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": f"multipart/form-data; boundary={boundary}",
            },
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode())
            return result.get("ok", False)
    except Exception as e:
        print(f"Warning: Slack file upload failed: {e}")
        return False


def create_slack_summary(
    works: list[dict],
    categorized: dict[str, list[dict]],
    from_date: str,
    to_date: str,
    report_path: Path = None
) -> tuple[str, list]:
    """
    Create a Slack message summarizing the literature update.

    Returns:
        tuple: (fallback_text, blocks)
    """
    total = len(works)

    # Fallback text
    fallback = f"📚 Rare Earth Literature Update: {total} new publications ({from_date} to {to_date})"

    # Block Kit formatting for rich message
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📚 Rare Earth Literature Update",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{total} new publications* found from {from_date} to {to_date}"
            }
        },
        {"type": "divider"}
    ]

    # Category breakdown
    if categorized:
        category_lines = []
        for category, cat_works in categorized.items():
            emoji = {
                "Separation Technologies": "🔬",
                "Extractants & Materials": "🧪",
                "Recycling & Urban Mining": "♻️",
                "Environmental & Sustainability": "🌱",
                "Supply Chain & Policy": "📊",
                "Other": "📄"
            }.get(category, "📄")
            category_lines.append(f"{emoji} *{category}*: {len(cat_works)}")

        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\n".join(category_lines)
            }
        })

    # Highlight top papers: most relevant, then most recent
    if works:
        blocks.append({"type": "divider"})
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*📌 Highlights:*"
            }
        })

        highlights = sorted(works, key=lambda x: x["publication_date"], reverse=True)
        highlights = sorted(highlights, key=lambda x: x.get("relevance", 0), reverse=True)[:3]

        for work in highlights:
            title = work["title"][:100] + "..." if len(work["title"]) > 100 else work["title"]
            authors = ", ".join(work["authors"][:2])
            if work.get("author_count", len(work["authors"])) > 2:
                authors += " et al."

            text = f"• *{title}*\n  _{authors}_ ({work['journal']})"
            if work["doi"]:
                text += f"\n  <{work['doi']}|View paper>"

            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text
                }
            })

    # Add report link/note if available
    if report_path:
        github_link = f"{GITHUB_REPO_URL}/blob/main/{report_path}"
        blocks.append({"type": "divider"})
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"📎 <{github_link}|View full report on GitHub>"
            }
        })

    return fallback, blocks


def notify_slack(
    works: list[dict],
    categorized: dict[str, list[dict]],
    from_date: str,
    to_date: str,
    report_path: Path,
    upload_file: bool = False
) -> bool:
    """
    Send Slack notification about the literature update.

    Uses SLACK_WEBHOOK_URL for simple notifications.
    Uses SLACK_BOT_TOKEN + SLACK_CHANNEL for file uploads.

    Args:
        works: List of processed works
        categorized: Works organized by category
        from_date: Start date of search period
        to_date: End date of search period
        report_path: Path to the generated report
        upload_file: Whether to upload the full report file

    Returns:
        True if notification sent successfully
    """
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    bot_token = os.environ.get("SLACK_BOT_TOKEN")
    channel = os.environ.get("SLACK_CHANNEL")

    if not webhook_url and not bot_token:
        print("Warning: No Slack credentials configured")
        print("Set SLACK_WEBHOOK_URL or SLACK_BOT_TOKEN environment variable")
        return False

    # Create summary message
    fallback, blocks = create_slack_summary(
        works, categorized, from_date, to_date, report_path
    )

    success = False

    # Send webhook notification
    if webhook_url:
        print("Sending Slack notification...")
        success = send_slack_webhook(webhook_url, fallback, blocks)
        if success:
            print("✓ Slack notification sent")

    # Upload file if configured and requested
    if upload_file and bot_token and channel:
        print("Uploading report to Slack...")
        title = f"Literature Update {to_date}"
        comment = f"📚 Rare Earth Literature Update: {len(works)} publications"
        file_success = upload_slack_file(bot_token, channel, report_path, title, comment)
        if file_success:
            print("✓ Report uploaded to Slack")
        success = success or file_success

    return success


def format_citation(work: dict) -> str:
    """Format a work as a citation string."""
    authors_str = ", ".join(work["authors"][:3])
    if work.get("author_count", len(work["authors"])) > 3:
        authors_str += " et al."

    year = work["publication_date"][:4] if work["publication_date"] else "n.d."

    citation = f"{authors_str} ({year}). {work['title']}. *{work['journal']}*."

    if work["doi"]:
        citation += f" [{work['doi']}]({work['doi']})"

    return citation


# OpenAlex work types that are journal-style articles; everything else
# (preprints, datasets, theses, repository deposits) is written as @misc.
ARTICLE_TYPES = {"article", "review", "letter", "editorial", "erratum"}


def format_bibtex(work: dict, key: str) -> str:
    """Format a work as a BibTeX entry."""
    authors = list(work["authors"])
    if work.get("author_count", len(authors)) > len(authors):
        authors.append("others")
    year = work["publication_date"][:4] if work["publication_date"] else ""

    # Clean title for BibTeX
    title = work["title"].replace("{", "").replace("}", "")

    if work["type"] in ARTICLE_TYPES:
        entry_type, venue_field = "article", "journal"
    else:
        entry_type, venue_field = "misc", "howpublished"

    fields = [
        ("author", " and ".join(authors)),
        ("title", f"{{{title}}}"),
        (venue_field, work["journal"]),
        ("year", year),
        ("doi", work["doi"].replace("https://doi.org/", "")),
        ("url", work["url"]),
    ]
    body = "".join(f"  {name} = {{{value}}},\n" for name, value in fields if value)
    return f"@{entry_type}{{{key},\n{body}}}\n"


def generate_report(
    works: list[dict],
    from_date: str,
    to_date: str,
    output_path: Path,
    candidate_count: Optional[int] = None,
    screened_out: Optional[list[dict]] = None,
    model: Optional[str] = None,
) -> str:
    """
    Generate a markdown report of the literature search results.

    Args:
        works: Works to report
        from_date, to_date: Reporting window
        output_path: Where to write the report
        candidate_count: Works that went into the LLM pass
        screened_out: Candidates the LLM pass rejected, listed for auditing
        model: The LLM that screened the candidates; None for an unscreened run
    """
    categorized = categorize_works(works)
    screened_out = screened_out or []

    if model:
        method = (
            f"Candidates come from OpenAlex title and abstract searches for rare earth\n"
            f"terms. An LLM ({model}) scored each of the {candidate_count} candidates for\n"
            f"relevance to REE separation on a 0-3 scale; papers scoring\n"
            f"{RELEVANCE_THRESHOLD} or higher are listed here, most relevant first. The\n"
            f"{len(screened_out)} it set aside are listed at the end."
        )
    else:
        method = (
            "Candidates come from OpenAlex title and abstract searches for rare earth\n"
            "terms. **This run skipped the LLM relevance pass**, so every paper that\n"
            "names a rare earth is listed and categories come from keywords."
        )

    report = f"""# Rare Earth Separation Literature Update

**Report Period:** {from_date} to {to_date}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Total Publications Found:** {len(works)}

---

## Executive Summary

{method}

### Publications by Category

| Category | Count |
|----------|-------|
"""

    for category, cat_works in categorized.items():
        report += f"| {category} | {len(cat_works)} |\n"

    report += "\n---\n\n"

    # Detailed sections for each category
    for category, cat_works in categorized.items():
        report += f"## {category}\n\n"

        for i, work in enumerate(cat_works, 1):
            oa_badge = "🔓" if work["open_access"] else "🔒"

            report += f"### {i}. {work['title']}\n\n"
            report += f"**Authors:** {', '.join(work['authors'])}\n\n"
            report += f"**Published:** {work['publication_date']} | "
            report += f"**Journal:** {work['journal']} | "
            report += f"**Citations:** {work['cited_by_count']} | "
            report += f"**Access:** {oa_badge}\n\n"

            if work["doi"]:
                report += f"**DOI:** [{work['doi']}]({work['doi']})\n\n"

            if work.get("relevance_reason"):
                report += (
                    f"**Relevance ({work['relevance']}/3):** "
                    f"{work['relevance_reason']}\n\n"
                )

            if work["abstract"]:
                abstract = work["abstract"]
                if len(abstract) > 500:
                    abstract = abstract[:500] + "..."
                report += f"**Abstract:** {abstract}\n\n"

            if work["keywords"]:
                report += f"**Keywords:** {', '.join(work['keywords'])}\n\n"

            report += "---\n\n"

    # The bibliography follows the order of the sections above.
    ordered = [work for cat_works in categorized.values() for work in cat_works]

    report += "## Full Bibliography\n\n"

    for i, work in enumerate(ordered, 1):
        report += f"{i}. {format_citation(work)}\n\n"

    if screened_out:
        report += (
            f"## Screened Out\n\n<details>\n<summary>{len(screened_out)} candidates "
            f"scored below {RELEVANCE_THRESHOLD}</summary>\n\n"
        )
        for work in sorted(screened_out, key=lambda w: -w["relevance"]):
            link = work["doi"] or work["url"]
            report += (
                f"- ({work['relevance']}) [{work['title']}]({link}): "
                f"{work['relevance_reason']}\n"
            )
        report += "\n</details>\n\n"

    # BibTeX section
    report += "\n## BibTeX Entries\n\n```bibtex\n"

    for i, work in enumerate(ordered, 1):
        # Create a key from first author's last name and year
        first_author = work["authors"][0] if work["authors"] else "Unknown"
        last_name = first_author.split()[-1].lower()
        year = work["publication_date"][:4] if work["publication_date"] else "0000"
        key = f"{last_name}{year}_{i}"

        report += format_bibtex(work, key)

    report += "```\n"

    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report)

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Monitor rare earth separation literature"
    )
    parser.add_argument(
        "--days", type=int, default=7,
        help="Number of days to look back (default: 7)"
    )
    parser.add_argument(
        "--output", type=str, default=None,
        help="Output file path (default: reports/YYYY-MM-DD_literature_update.md)"
    )
    parser.add_argument(
        "--to-date", type=str, default=None,
        help="End of the reporting window, YYYY-MM-DD (default: today). "
             "Use with --days or --from-date to backfill a past week."
    )
    parser.add_argument(
        "--from-date", type=str, default=None,
        help="Start of the reporting window, YYYY-MM-DD (overrides --days)"
    )
    parser.add_argument(
        "--llm-model", type=str, default=LLM_MODEL,
        help=f"Model for the relevance pass (default: {LLM_MODEL})"
    )
    parser.add_argument(
        "--no-llm", action="store_true",
        help="Skip the LLM relevance pass and list every candidate"
    )
    parser.add_argument(
        "--slack", action="store_true",
        help="Send notification to Slack (requires SLACK_WEBHOOK_URL env var)"
    )
    parser.add_argument(
        "--slack-upload", action="store_true",
        help="Upload full report to Slack (requires SLACK_BOT_TOKEN and SLACK_CHANNEL)"
    )
    parser.add_argument(
        "--data-out", type=str, default=None,
        help="Also write the run's works as JSON, for a later --slack-from"
    )
    parser.add_argument(
        "--slack-from", type=str, default=None,
        help="Notify Slack from a saved --data-out file instead of searching again"
    )

    args = parser.parse_args()

    # Replaying a saved run: the search already happened, so reuse its results
    # rather than querying OpenAlex a second time. A second search returns a
    # different set of works, so the Slack summary would not match the report
    # that was committed.
    if args.slack_from:
        data = json.loads(Path(args.slack_from).read_text())
        works = data["works"]
        ok = notify_slack(
            works,
            categorize_works(works),
            data["from_date"],
            data["to_date"],
            Path(data["report_path"]),
            upload_file=args.slack_upload,
        )
        return 0 if ok else 1

    # Calculate date range
    if args.to_date:
        to_date = datetime.strptime(args.to_date, "%Y-%m-%d")
    else:
        to_date = datetime.now()

    if args.from_date:
        from_date = datetime.strptime(args.from_date, "%Y-%m-%d")
    else:
        from_date = to_date - timedelta(days=args.days)

    if from_date > to_date:
        parser.error("--from-date must not be after --to-date")

    from_date_str = from_date.strftime("%Y-%m-%d")
    to_date_str = to_date.strftime("%Y-%m-%d")

    print(f"Searching for publications from {from_date_str} to {to_date_str}")
    print(f"Running {len(SEARCH_QUERIES)} queries...")

    # Search OpenAlex
    works, failed_queries = search_openalex_all_queries(from_date_str, to_date_str)

    # Each query covers a whole family of terms, so losing any one of them
    # leaves a hole that looks like a quiet week, and the weekly cron would
    # commit and push it. Refuse to write the report instead.
    if failed_queries:
        print(
            f"Error: {len(failed_queries)}/{len(SEARCH_QUERIES)} queries failed. "
            f"Refusing to write an incomplete report.",
            file=sys.stderr,
        )
        return 1

    print(f"\nFound {len(works)} unique publications")

    # Extract info from works
    processed_works = [extract_work_info(w) for w in works]

    # Filter out works without titles, and any dated past the window
    processed_works = [
        w for w in processed_works
        if w["title"] != "Untitled" and w["publication_date"] <= to_date_str
    ]
    processed_works = deduplicate_works(processed_works)
    print(f"After removing duplicates: {len(processed_works)} publications")

    candidates = [w for w in processed_works if mentions_ree(w)]
    print(
        f"Naming a rare earth in title or abstract: {len(candidates)} "
        f"(dropped {len(processed_works) - len(candidates)})"
    )

    screened_out = []
    model = None
    if args.no_llm:
        processed_works = candidates
    else:
        model = args.llm_model
        try:
            screen_with_llm(candidates, model=model)
        except LLMScreeningError as e:
            print(
                f"Error: LLM relevance pass failed: {e}. Refusing to write an "
                f"unscreened report (use --no-llm to skip the pass).",
                file=sys.stderr,
            )
            return 1
        processed_works = [w for w in candidates if w["relevance"] >= RELEVANCE_THRESHOLD]
        screened_out = [w for w in candidates if w["relevance"] < RELEVANCE_THRESHOLD]
        print(
            f"After LLM relevance pass: {len(processed_works)} publications "
            f"({len(screened_out)} set aside)"
        )

    # Categorize for reporting and Slack
    categorized = categorize_works(processed_works)

    # Generate output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path("reports") / f"{to_date_str}_literature_update.md"

    # Generate report
    report = generate_report(
        processed_works, from_date_str, to_date_str, output_path,
        candidate_count=len(candidates), screened_out=screened_out, model=model,
    )

    print(f"\nReport saved to: {output_path}")
    print(f"Total publications: {len(processed_works)}")

    # Save the run so a later step can notify Slack from these exact works
    if args.data_out:
        data_path = Path(args.data_out)
        data_path.parent.mkdir(parents=True, exist_ok=True)
        data_path.write_text(json.dumps({
            "from_date": from_date_str,
            "to_date": to_date_str,
            "report_path": str(output_path),
            "works": processed_works,
            "screened_out": screened_out,
        }, indent=2))
        print(f"Run data saved to: {data_path}")

    # Send Slack notification if requested
    if args.slack or args.slack_upload:
        if not notify_slack(
            processed_works,
            categorized,
            from_date_str,
            to_date_str,
            output_path,
            upload_file=args.slack_upload
        ):
            print("Error: Slack notification failed", file=sys.stderr)
            return 1

    return processed_works


if __name__ == "__main__":
    # main() returns 1 on an aborted run and the list of works on a good one;
    # only an int is an exit status.
    result = main()
    sys.exit(result if isinstance(result, int) else 0)
