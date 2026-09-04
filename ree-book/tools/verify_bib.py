"""Verify every bibliography entry describes a real, findable source.

Three verification routes, in order of strength:

1. DOI present -> resolve against the CrossRef works API. A resolving DOI is
   proof the paper exists, and the returned metadata is authoritative, so it
   also repairs the 29 placeholder `{{Journal}} Authors` fields and the 211
   entries carrying no author at all. A DOI CrossRef does not know is then
   tried against DataCite: software and dataset records -- the DOE/OSTI ones
   in particular -- are minted there, and a DOI that resolves in DataCite is
   the same evidence as one that resolves in CrossRef. Only the registry
   differs, and rejecting an entry for being in the wrong one would be a
   verdict on the registry rather than on the source.
2. No DOI but a URL -> check the URL responds. Web sources (standards pages,
   vendor documentation, software) are legitimate references that will never
   have a DOI; a live URL is the right evidence for them.
3. No DOI and no URL, but an ISBN -> look the ISBN up in OpenLibrary. Books
   and book chapters are legitimate references that predate DOIs, and a
   publisher landing page guessed from the title is not evidence -- five such
   URLs were written by hand and all of them 404'd.
4. None of the above -> unverifiable. These are the likely-fabricated entries.

A URL that answers with 401, 403, or 406 counts as alive. Britannica, the IEA,
and the IAEA refuse scripted requests outright; the server answering about that
exact URL is evidence the page exists, and treating a refusal as a dead link
rejected five real sources. A URL that does not answer at all is a third case:
it is kept and listed as unchecked, because a server that never replied has
said nothing about whether the page is there.

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

# Verdicts reached by hand that a machine re-run would otherwise erase. The
# report is regenerated from scratch every run, so a correction made in the
# file itself does not survive; it has to live here.
STANDING_NOTES = """An earlier run rejected `iaea2011radiation` on the grounds that its URL
was gone. That verdict was wrong, and it was reached against a stale
`iaea.org` catalogue URL rather than the URL the entry actually carries.
The URL in `references.bib`,
<https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1512_web.pdf>,
was re-checked by hand on 2026-09-04: it returns HTTP 200 and 2.75 MB of
PDF whose title page reads *Radiation Protection and NORM Residue
Management in the Production of Rare Earths from Thorium Containing
Minerals*, Safety Reports Series No. 68, © IAEA 2011, STI/PUB/1512,
ISBN 978-92-0-115710-2. Every field in the entry matches the document.
The entry stays in `references.bib`."""

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


def _get(url: str, timeout: int = 30, method: str = "GET"):
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method=method)
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


def title_candidates(msg: dict) -> list[str]:
    """Both readings of a CrossRef title: with and without its subtitle.

    CrossRef files a book's subtitle in a field of its own, and a bibliography
    may reasonably record either the bare title or both parts joined. Matching
    against one reading alone reported three entries as diverging when none of
    them did, in both directions.
    """
    title = (msg.get("title") or [""])[0]
    out = [title]
    sub = msg.get("subtitle") or []
    sub = sub[0] if sub else ""
    if sub and norm_title(sub) not in norm_title(title):
        out.append(f"{title}: {sub}")
    return [t for t in out if t]


def datacite_by_doi(doi: str) -> dict | None:
    """Resolve a DOI that CrossRef does not know against DataCite."""
    url = f"https://api.datacite.org/dois/{urllib.parse.quote(doi)}"
    status, body = _get(url)
    if status != 200 or not body:
        return None
    try:
        return json.loads(body)["data"]["attributes"]
    except (json.JSONDecodeError, KeyError):
        return None


def crossref_by_doi(doi: str) -> dict | None:
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}?mailto={MAILTO}"
    status, body = _get(url)
    if status != 200 or not body:
        return None
    try:
        return json.loads(body).get("message")
    except json.JSONDecodeError:
        return None


# The server answered about this exact URL and refused to serve it to a script.
# That is evidence the resource exists, which is all this check is asking.
ACCESS_REFUSED = {401, 403, 406}


def url_alive(url: str) -> str:
    """"alive", "dead", or "unreachable".

    The third verdict matters. A server that answers 404 has told us the page
    is gone; a server that never answers has told us nothing, and treating the
    two the same rejected a live USGS yearbook chapter whose only fault was
    that the agency rate-limits a long sequential run. This is the same rule
    the ISBN route already follows.
    """
    if not url.lower().startswith(("http://", "https://")):
        return "dead"
    # HEAD first: several of these URLs are multi-megabyte agency PDFs, and
    # downloading one whole to prove it exists is its own way of timing out.
    status, _ = _get(url, timeout=20, method="HEAD")
    if status is None or status in (405, 501):
        status, _ = _get(url, timeout=45)
    if status is None:
        return "unreachable"
    if 200 <= status < 400 or status in ACCESS_REFUSED:
        return "alive"
    return "dead"


def isbn_title(isbn: str) -> tuple[str, str | None]:
    """Resolve an ISBN to a title.

    Returns one of ("found", title), ("absent", None) or ("unreachable", None).
    The three are not interchangeable: a registry that cannot be reached is
    silence, not a verdict, and rejecting an entry on it would delete a real
    book because a host was down or firewalled. Only "absent" — a registry that
    answered and did not have the ISBN — is evidence against an entry.

    Two registries are tried, because either can be blocked where this runs.
    """
    digits = re.sub(r"[^0-9Xx]", "", isbn)
    reached = False

    key = "ISBN:" + digits
    url = ("https://openlibrary.org/api/books?format=json&jscmd=data"
           f"&bibkeys={urllib.parse.quote(key)}")
    status, body = _get(url, timeout=20)
    if status == 200 and body:
        reached = True
        try:
            rec = json.loads(body).get(key)
        except json.JSONDecodeError:
            rec = None
        if rec and rec.get("title"):
            return "found", rec["title"]

    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{digits}"
    status, body = _get(url, timeout=20)
    if status == 200 and body:
        reached = True
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            data = {}
        items = data.get("items") or []
        if items:
            title = (items[0].get("volumeInfo") or {}).get("title")
            if title:
                return "found", title

    return ("absent" if reached else "unreachable"), None


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
    repaired_authors, mismatched_titles, unreachable = [], [], []

    for i, e in enumerate(db.entries, 1):
        doi = norm_doi(e.get("doi", ""))
        if doi:
            msg = crossref_by_doi(doi)
            time.sleep(args.delay)
            if msg is None:
                dc = datacite_by_doi(doi)
                time.sleep(args.delay)
                if dc is None:
                    rejected.append(
                        (e, f"DOI {doi} resolves in neither CrossRef nor DataCite"))
                    continue
                # DataCite's schema is not CrossRef's, and its records here are
                # software and datasets rather than articles, so no field is
                # repaired from it. Existence is all this route claims.
                titles = dc.get("titles") or [{}]
                dc_title = (titles[0] or {}).get("title", "")
                if dc_title:
                    sim = difflib.SequenceMatcher(
                        None, norm_title(e.get("title", "")), norm_title(dc_title)
                    ).ratio()
                    if sim < args.title_threshold:
                        mismatched_titles.append((e["ID"], sim, e.get("title", "")[:60],
                                                  dc_title[:60]))
                e["_verified"] = "datacite-doi"
                verified.append(e)
                print(f"  [{i}/{total}] {e['ID']}: ok (datacite)")
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

            cands = title_candidates(msg)
            if cands:
                sim, cr_title = max(
                    (difflib.SequenceMatcher(
                        None, norm_title(e.get("title", "")), norm_title(c)
                    ).ratio(), c)
                    for c in cands
                )
                if sim < args.title_threshold:
                    mismatched_titles.append((e["ID"], sim, e.get("title", "")[:60],
                                              cr_title[:60]))
            e["_verified"] = "crossref-doi"
            verified.append(e)
            print(f"  [{i}/{total}] {e['ID']}: ok")
            continue

        url = (e.get("url") or "").strip().strip("{}")
        if url:
            verdict = url_alive(url)
            time.sleep(args.delay)
            if verdict == "alive":
                e["_verified"] = "url-live"
                verified.append(e)
                print(f"  [{i}/{total}] {e['ID']}: ok (url)")
            elif verdict == "unreachable":
                e["_verified"] = "url-unreachable"
                verified.append(e)
                unreachable.append((e["ID"], url[:70], e.get("title", "")[:60]))
                print(f"  [{i}/{total}] {e['ID']}: kept (URL did not answer)")
            else:
                rejected.append((e, f"no DOI; URL is gone: {url[:70]}"))
            continue

        isbn = (e.get("isbn") or "").strip().strip("{}")
        if isbn:
            verdict, title = isbn_title(isbn)
            time.sleep(args.delay)
            if verdict == "unreachable":
                # No registry answered. Keep the entry and say so; silence from
                # a lookup service is not evidence about the book.
                e["_verified"] = "isbn-unreachable"
                verified.append(e)
                unreachable.append((e["ID"], f"ISBN {isbn}", e.get("title", "")[:60]))
                print(f"  [{i}/{total}] {e['ID']}: kept (ISBN registry unreachable)")
                continue
            if verdict == "found":
                # An ISBN names the book. For a chapter, that is `booktitle`;
                # comparing it to the chapter title reports a false mismatch.
                recorded = e.get("booktitle") or e.get("title", "")
                sim = difflib.SequenceMatcher(
                    None, norm_title(recorded), norm_title(title)
                ).ratio()
                if sim < args.title_threshold:
                    mismatched_titles.append((e["ID"], sim, e.get("title", "")[:60],
                                              title[:60]))
                e["_verified"] = "isbn"
                verified.append(e)
                print(f"  [{i}/{total}] {e['ID']}: ok (isbn)")
            else:
                rejected.append((e, f"no DOI, no URL; ISBN not found: {isbn}"))
            continue

        rejected.append((e, "no DOI, no URL, no ISBN — unverifiable as recorded"))

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
        f"Generated by `python tools/verify_bib.py` on "
        f"{time.strftime('%Y-%m-%d')}. Re-run it whenever `references.bib` "
        f"changes; the counts below are only as current as that run.",
        "",
        f"- Entries checked: **{total}**",
        # Count every route, or the three numbers will not add up to the
        # total and a reader will rightly distrust the rest of the report.
        f"- Verified: **{len(verified)}** "
        f"({sum(1 for e in verified if e.get('_verified') == 'crossref-doi')} "
        f"by resolving a CrossRef DOI, "
        f"{sum(1 for e in verified if e.get('_verified') == 'datacite-doi')} "
        f"by resolving a DataCite DOI, "
        f"{sum(1 for e in verified if e.get('_verified') == 'url-live')} "
        f"by live URL, "
        f"{sum(1 for e in verified if e.get('_verified') == 'isbn')} "
        f"by ISBN, "
        f"{sum(1 for e in verified if e.get('_verified') in ('isbn-unreachable', 'url-unreachable'))} "
        "kept unchecked because nothing answered)",
        f"- Rejected: **{len(rejected)}**",
        f"- Author fields repaired from CrossRef: **{len(repaired_authors)}**",
        f"- Titles diverging from CrossRef: **{len(mismatched_titles)}**",
        "",
        "## Rejected — removed from the bibliography",
        "",
        "Any claim resting solely on one of these must be removed or rewritten.",
        "",
        *([f"- `{e['ID']}` — {why} — {(e.get('title') or '')[:75]}"
           for e, why in rejected]
          or ["Nothing was rejected in this run."]),
        "",
        STANDING_NOTES,
        "",
        "## Kept, but not machine-checked",
        "",
        "Nothing answered about these — an ISBN registry that could not be",
        "reached, or a URL whose server never replied. That is silence, not a",
        "verdict: the entries are kept and the identifier is printed here so it",
        "can be checked by hand.",
        "",
        *(f"- `{i}` — {ident} — {t}" for i, ident, t in unreachable),
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
