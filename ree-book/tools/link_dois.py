"""Recover a DOI from a publisher URL.

The broad review documents cite by hyperlink -- `([Nature Communications](url))`
-- with the label naming a journal rather than a paper.  The URL is the only
identifier, so a citation can only be made out of one if the URL yields a DOI.

Five publishers between them account for nearly every recoverable link, and each
encodes the DOI differently: Elsevier hides it behind a PII, Nature and RSC put
it in the path under a different prefix, MDPI numbers by volume/issue/page, and
everyone else writes it out.  Anything else -- a vendor page, a news story, a
laboratory press release -- has no DOI and is left as a hyperlink.
"""

from __future__ import annotations

import json
import pathlib
import re
import time
import urllib.parse
import urllib.request

UA = (
    "ree-book/1.0 (https://github.com/KitchinHUB/ree-literature-updates; "
    "mailto:jkitchin@andrew.cmu.edu)"
)
CACHE = pathlib.Path(__file__).resolve().parent.parent / ".link-dois.json"

DOI_IN_URL = re.compile(r"(10\.\d{4,9}/[^\s?#]+)")
NATURE = re.compile(r"nature\.com/articles/([a-z0-9-]+)")
RSC = re.compile(r"pubs\.rsc\.org/en/content/article\w+/\d{4}/\w+/([a-z0-9]+)", re.I)
PII = re.compile(r"sciencedirect\.com/science/article/(?:abs/)?pii/([A-Z0-9]+)")
MDPI = re.compile(r"mdpi\.com/(\d{4}-\d{3}[\dxX])/(\d+)/(\d+)/(\d+)")
HINDAWI = re.compile(r"hindawi\.com/journals/\w+/(\d{4})/(\d+)")
RESEARCHSQUARE = re.compile(r"researchsquare\.com/article/(rs-\d+)/(v\d+)")
PMC = re.compile(r"ncbi\.nlm\.nih\.gov/articles/(PMC\d+)")
PUBMED = re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)")
# ".../full", ".../abstract", ".../meta" are viewer suffixes, not part of the DOI
DOI_TAIL = re.compile(r"/(?:full|abstract|meta|unauth|pdf|html)$", re.I)


def _get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as f:
        return json.load(f)


def _cache() -> dict:
    return json.loads(CACHE.read_text()) if CACHE.exists() else {}


def _save(cache: dict) -> None:
    CACHE.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n")


def doi_for(url: str, cache: dict | None = None) -> str:
    """DOI for a publisher URL, or "" when the URL does not name an article."""
    own = cache is None
    cache = _cache() if own else cache
    if url in cache:
        return cache[url]

    doi = ""
    if m := DOI_IN_URL.search(url):
        doi = DOI_TAIL.sub("", m.group(1).rstrip(".)"))
    elif m := NATURE.search(url):
        doi = f"10.1038/{m.group(1)}"
    elif m := RSC.search(url):
        doi = f"10.1039/{m.group(1).lower()}"
    elif m := PII.search(url):
        # Elsevier's PII is indexed by CrossRef as an alternative id.
        js = _get(
            "https://api.crossref.org/works?rows=2&filter=alternative-id:"
            + m.group(1)
        )
        items = js["message"]["items"]
        doi = items[0]["DOI"] if len(items) == 1 else ""
        time.sleep(0.5)
    elif m := MDPI.search(url):
        issn, vol, issue, page = m.groups()
        js = _get(
            f"https://api.crossref.org/works?rows=20&filter=issn:{issn}"
            f"&query.bibliographic={urllib.parse.quote(f'{vol} {issue} {page}')}"
        )
        for it in js["message"]["items"]:
            if (
                str(it.get("volume")) == vol
                and str(it.get("issue")) == issue
                and str(it.get("page")) == page
            ):
                doi = it["DOI"]
                break
        time.sleep(0.5)
    elif m := HINDAWI.search(url):
        doi = f"10.1155/{m.group(1)}/{m.group(2)}"
    elif m := RESEARCHSQUARE.search(url):
        doi = f"10.21203/rs.3.{m.group(1)}/{m.group(2)}"
    elif m := (PMC.search(url) or PUBMED.search(url)):
        # NCBI's summary endpoint carries the DOI in articleids.
        ident = m.group(1)
        db = "pmc" if ident.startswith("PMC") else "pubmed"
        js = _get(
            f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            f"?db={db}&retmode=json&id={ident.removeprefix('PMC')}"
        )
        for rec in js.get("result", {}).values():
            if not isinstance(rec, dict):
                continue
            for aid in rec.get("articleids", []):
                if aid.get("idtype") == "doi":
                    doi = aid["value"]
        time.sleep(0.4)

    cache[url] = doi
    if own:
        _save(cache)
    return doi
