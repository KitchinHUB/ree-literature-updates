"""Verify every bibliography entry describes a real, findable source.

Three verification routes, in order of strength:

1. DOI present -> resolve against the CrossRef works API. A resolving DOI is
   proof the paper exists, and the returned metadata is authoritative, so it
   also repairs the 29 placeholder `{{Journal}} Authors` fields and the 211
   entries carrying no author at all.
2. No DOI but a URL -> check the URL responds. Web sources (standards pages,
   vendor documentation, software) are legitimate references that will never
   have a DOI; a live URL is the right evidence for them.
3. Neither -> unverifiable. These are the likely-fabricated entries.

Entries failing all three are written to a separate file rather than deleted in
place, so the removal is reviewable before it is applied.

Usage:
    python tools/verify_bib.py [--bib references.bib] [--apply]
"""

from __future__ import annotations

import argparse
import difflib
import json
import pathlib
import random
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

import bibtexparser

MAILTO = "jkitchin@andrew.cmu.edu"
UA = f"ree-book/1.0 (https://github.com/KitchinHUB; mailto:{MAILTO})"
MAX_ATTEMPTS = 4
RETRYABLE_STATUS = {429, 500, 502, 503, 504}

PLACEHOLDER_AUTHOR = re.compile(
    r"^\{?\{?\s*[\w\s.&'-]+?\s+Authors\s*\}?\}?$", re.IGNORECASE
)


def norm_title(raw: str) -> str:
    t = (raw or "").lower()
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"[{}\\$]", " ", t)
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def norm_doi(raw: str) -> str:
    d = (raw or "").strip().lower()
    d = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", d)
    return re.sub(r"^doi:\s*", "", d).strip().rstrip(".")


def _get(url: str, timeout: int = 30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code not in RETRYABLE_STATUS:
                return e.code, b""
            reason = e.code
        except Exception as e:  # noqa: BLE001 - network errors are all retryable here
            reason = str(e)
        if attempt == MAX_ATTEMPTS:
            return None, b""
        time.sleep(min(2 ** (attempt - 1), 30) + random.uniform(0, 0.4))
    return None, b""


def crossref_by_doi(doi: str) -> dict | None:
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}?mailto={MAILTO}"
    status, body = _get(url)
    if status != 200 or not body:
        return None
    try:
        return json.loads(body).get("message")
    except json.JSONDecodeError:
        return None


def url_alive(url: str) -> bool:
    if not url.lower().startswith(("http://", "https://")):
        return False
    status, _ = _get(url, timeout=20)
    return status is not None and 200 <= status < 400


def format_authors(msg: dict) -> str:
    names = []
    for a in msg.get("author") or []:
        family, given = a.get("family"), a.get("given")
        if family and given:
            names.append(f"{family}, {given}")
        elif family:
            names.append(family)
        elif a.get("name"):
            names.append(a["name"])
    return " and ".join(names)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bib", default="references.bib")
    ap.add_argument("--rejects", default="references-rejected.bib")
    ap.add_argument("--report", default="verification-report.md")
    ap.add_argument("--delay", type=float, default=0.35)
    ap.add_argument("--title-threshold", type=float, default=0.75,
                    help="warn when the CrossRef title diverges this much")
    ap.add_argument("--apply", action="store_true",
                    help="write the pruned bibliography (default: dry run)")
    args = ap.parse_args()

    path = pathlib.Path(args.bib)
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    db = bibtexparser.loads(path.read_text(), parser=parser)
    total = len(db.entries)
    print(f"verifying {total} entries")

    verified, rejected = [], []
    repaired_authors, mismatched_titles = [], []

    for i, e in enumerate(db.entries, 1):
        doi = norm_doi(e.get("doi", ""))
        if doi:
            msg = crossref_by_doi(doi)
            time.sleep(args.delay)
            if msg is None:
                rejected.append((e, f"DOI {doi} does not resolve in CrossRef"))
                continue

            # CrossRef metadata is authoritative; repair broken authorship.
            authors = format_authors(msg)
            old = (e.get("author") or "").strip()
            if authors and (not old or PLACEHOLDER_AUTHOR.match(old)):
                e["author"] = authors
                repaired_authors.append((e["ID"], old or "(empty)", authors[:60]))
            for field, val in (
                ("journal", (msg.get("container-title") or [""])[0]),
                ("year", str(((msg.get("issued") or {}).get("date-parts")
                              or [[None]])[0][0] or "")),
                ("volume", msg.get("volume", "")),
                ("publisher", msg.get("publisher", "")),
            ):
                if val and not (e.get(field) or "").strip():
                    e[field] = val

            cr_title = (msg.get("title") or [""])[0]
            if cr_title:
                sim = difflib.SequenceMatcher(
                    None, norm_title(e.get("title", "")), norm_title(cr_title)
                ).ratio()
                if sim < args.title_threshold:
                    mismatched_titles.append((e["ID"], sim, e.get("title", "")[:60],
                                              cr_title[:60]))
            e["_verified"] = "crossref-doi"
            verified.append(e)
            print(f"  [{i}/{total}] {e['ID']}: ok")
            continue

        url = (e.get("url") or "").strip().strip("{}")
        if url:
            ok = url_alive(url)
            time.sleep(args.delay)
            if ok:
                e["_verified"] = "url-live"
                verified.append(e)
                print(f"  [{i}/{total}] {e['ID']}: ok (url)")
            else:
                rejected.append((e, f"no DOI; URL does not respond: {url[:70]}"))
            continue

        rejected.append((e, "no DOI, no URL — unverifiable as recorded"))

    print(f"\nverified {len(verified)} / {total}; rejected {len(rejected)}")

    if args.apply:
        out = bibtexparser.bibdatabase.BibDatabase()
        out.entries = [{k: v for k, v in e.items() if not k.startswith("_")}
                       for e in verified]
        w = bibtexparser.bwriter.BibTexWriter()
        w.indent = "  "
        w.order_entries_by = ("ID",)
        path.write_text(bibtexparser.dumps(out, w))

        # Append rather than overwrite: this script is re-run after repairs,
        # and a later pass rejecting fewer entries must not erase the record of
        # what earlier passes removed.
        rej_path = pathlib.Path(args.rejects)
        existing = []
        if rej_path.exists():
            rp = bibtexparser.bparser.BibTexParser(common_strings=True)
            rp.ignore_nonstandard_types = False
            rp.expect_multiple_parse = True
            existing = bibtexparser.loads(rej_path.read_text(), parser=rp).entries
        seen = {e["ID"] for e in existing}
        rej = bibtexparser.bibdatabase.BibDatabase()
        rej.entries = existing + [
            {k: v for k, v in e.items() if not k.startswith("_")}
            for e, _ in rejected if e["ID"] not in seen
        ]
        rej_path.write_text(bibtexparser.dumps(rej, w))
        print(f"wrote {path} and {args.rejects}")
    else:
        print("dry run; re-run with --apply to prune")

    report = [
        "# Citation verification report",
        "",
        f"- Entries checked: **{total}**",
        f"- Verified: **{len(verified)}** "
        f"({sum(1 for e in verified if e.get('_verified') == 'crossref-doi')} "
        f"by resolving DOI, "
        f"{sum(1 for e in verified if e.get('_verified') == 'url-live')} "
        "by live URL)",
        f"- Rejected: **{len(rejected)}**",
        f"- Author fields repaired from CrossRef: **{len(repaired_authors)}**",
        f"- Titles diverging from CrossRef: **{len(mismatched_titles)}**",
        "",
        "## Rejected — removed from the bibliography",
        "",
        "Any claim resting solely on one of these must be removed or rewritten.",
        "",
        *(f"- `{e['ID']}` — {why} — {(e.get('title') or '')[:75]}"
          for e, why in rejected),
        "",
        "## Titles that disagree with CrossRef (check these by hand)",
        "",
        *(f"- `{i}` (similarity {s:.2f})\n  - bib: {a}\n  - crossref: {b}"
          for i, s, a, b in mismatched_titles),
        "",
        "## Author fields repaired",
        "",
        *(f"- `{i}`: {old} -> {new}" for i, old, new in repaired_authors),
        "",
    ]
    pathlib.Path(args.report).write_text("\n".join(report))
    print(f"wrote {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
