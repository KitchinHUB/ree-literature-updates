"""Recover missing DOIs for merged bibliography entries via the CrossRef API.

CrossRef is used rather than OpenAlex because OpenAlex meters a daily credit
quota (1000 credits, 10 per query) that is easy to exhaust; CrossRef's polite
pool only asks for a mailto.

A match is accepted only when the normalized title similarity clears
--threshold and the year agrees (when both sides state one). Everything else is
left alone and reported, so a wrong DOI is never silently written into the
bibliography.

Usage:
    python tools/recover_dois.py [--bib references.bib] [--apply]
"""

from __future__ import annotations

import argparse
import difflib
import json
import pathlib
import random
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

import bibtexparser

MAILTO = "jkitchin@andrew.cmu.edu"
MAX_ATTEMPTS = 4
RETRY_MAX_DELAY = 30.0
RETRYABLE_STATUS = {429, 500, 502, 503, 504}


def norm_title(raw: str) -> str:
    t = (raw or "").lower()
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"[{}\\$]", " ", t)
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def query_crossref(title: str, rows: int = 5) -> list[dict]:
    """Search CrossRef by bibliographic title, retrying transient failures."""
    params = {
        "query.bibliographic": title,
        "rows": str(rows),
        "select": "DOI,title,issued,container-title,author",
        "mailto": MAILTO,
    }
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": f"ree-book/1.0 ({MAILTO})"})

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode()).get("message", {}).get("items", [])
        except urllib.error.HTTPError as e:
            if e.code not in RETRYABLE_STATUS:
                return []
            reason = f"HTTP {e.code}"
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            reason = str(e)
        if attempt == MAX_ATTEMPTS:
            print(f"    give up after {MAX_ATTEMPTS}: {reason}", file=sys.stderr)
            return []
        delay = min(2 ** (attempt - 1), RETRY_MAX_DELAY) + random.uniform(0, 0.4)
        time.sleep(delay)
    return []


def best_match(entry: dict, items: list[dict], threshold: float) -> tuple:
    """Return (doi, score, why) for the best acceptable candidate, else (None, ...)."""
    want_title = norm_title(entry.get("title", ""))
    want_year = re.sub(r"[^0-9]", "", entry.get("year", ""))[:4]
    best = (None, 0.0, "no candidates")

    for it in items:
        cand_title = norm_title((it.get("title") or [""])[0])
        if not cand_title:
            continue
        score = difflib.SequenceMatcher(None, want_title, cand_title).ratio()
        if score <= best[1]:
            continue
        parts = (it.get("issued") or {}).get("date-parts") or [[None]]
        cand_year = str(parts[0][0]) if parts and parts[0] and parts[0][0] else ""
        if want_year and cand_year and abs(int(want_year) - int(cand_year)) > 1:
            best = (None, score, f"year mismatch {want_year} vs {cand_year}")
            continue
        if score >= threshold:
            best = (it.get("DOI"), score, "ok")
        else:
            best = (None, score, f"below threshold ({score:.2f})")
    return best


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bib", default="references.bib")
    ap.add_argument("--report", default="doi-recovery.md")
    ap.add_argument("--threshold", type=float, default=0.90)
    ap.add_argument("--delay", type=float, default=0.4, help="seconds between queries")
    ap.add_argument("--apply", action="store_true",
                    help="write recovered DOIs into the bib (default: dry run)")
    args = ap.parse_args()

    path = pathlib.Path(args.bib)
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    db = bibtexparser.loads(path.read_text(), parser=parser)

    targets = [e for e in db.entries if not (e.get("doi") or "").strip()]
    print(f"{len(targets)} entries missing a DOI")

    found, failed = [], []
    for i, e in enumerate(targets, 1):
        title = (e.get("title") or "").strip("{} ")
        if not title:
            failed.append((e, "no title to search on"))
            continue
        doi, score, why = best_match(e, query_crossref(title), args.threshold)
        if doi:
            found.append((e, doi, score))
            e["doi"] = doi
            print(f"  [{i}/{len(targets)}] {e['ID']}: {doi} ({score:.2f})")
        else:
            failed.append((e, why))
        time.sleep(args.delay)

    print(f"\nrecovered {len(found)} / {len(targets)}")

    if args.apply:
        writer = bibtexparser.bwriter.BibTexWriter()
        writer.indent = "  "
        writer.order_entries_by = ("ID",)
        path.write_text(bibtexparser.dumps(db, writer))
        print(f"wrote {path}")
    else:
        print("dry run; re-run with --apply to write")

    report = [
        "# DOI recovery via CrossRef",
        "",
        f"- Entries missing a DOI: **{len(targets)}**",
        f"- Recovered: **{len(found)}** (title similarity >= {args.threshold}, "
        "year agreeing within 1)",
        f"- Still missing: **{len(failed)}**",
        "",
        "## Recovered",
        "",
        *(f"- `{e['ID']}` -> {doi} (similarity {s:.2f}) — "
          f"{(e.get('title') or '')[:80]}" for e, doi, s in found),
        "",
        "## Not recovered",
        "",
        *(f"- `{e['ID']}` — {why} — {(e.get('title') or '')[:80]}"
          for e, why in failed),
        "",
    ]
    pathlib.Path(args.report).write_text("\n".join(report))
    print(f"wrote {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
