"""Repair entries whose recorded DOI resolves to a different paper.

verify_bib.py flags entries where the bibliography title and the title CrossRef
returns for the recorded DOI disagree. Every such entry in this corpus inherited
its DOI from a source .bib file, and the CrossRef titles are unrelated papers --
so the DOI is wrong, not the title.

The naive repair (adopt the CrossRef title) is destructive: it would silently
replace each reference with whatever unrelated paper the bad DOI points at.
Instead, search CrossRef by the recorded *title* to find the DOI that title
actually belongs to:

  - confident match  -> replace the wrong DOI, entry rescued
  - borderline match -> leave alone, report for a human
  - no match         -> the title describes nothing findable; reject the entry

Usage:
    python tools/fix_doi_mismatches.py [--apply]
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
UA = f"ree-book/1.0 (https://github.com/KitchinHUB; mailto:{MAILTO})"
MAX_ATTEMPTS = 4
RETRYABLE_STATUS = {429, 500, 502, 503, 504}
# Supplementary-material component DOIs, e.g. 10.1021/acsomega.1c02982.s001
COMPONENT_DOI = re.compile(r"\.s\d{3}$", re.IGNORECASE)


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


def _get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code not in RETRYABLE_STATUS:
                return None
        except Exception:  # noqa: BLE001
            pass
        if attempt == MAX_ATTEMPTS:
            return None
        time.sleep(min(2 ** (attempt - 1), 30) + random.uniform(0, 0.4))
    return None


def search_by_title(title: str, rows: int = 10) -> list[dict]:
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode({
        "query.bibliographic": title,
        "rows": str(rows),
        "select": "DOI,title,issued,container-title,author",
        "mailto": MAILTO,
    })
    data = _get_json(url)
    return (data or {}).get("message", {}).get("items", [])


def crossref_title(doi: str) -> str:
    data = _get_json(
        f"https://api.crossref.org/works/{urllib.parse.quote(doi)}?mailto={MAILTO}"
    )
    if not data:
        return ""
    return ((data.get("message") or {}).get("title") or [""])[0]


def format_authors(item: dict) -> str:
    names = []
    for a in item.get("author") or []:
        family, given = a.get("family"), a.get("given")
        if family and given:
            names.append(f"{family}, {given}")
        elif family:
            names.append(family)
    return " and ".join(names)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bib", default="references.bib")
    ap.add_argument("--rejects", default="references-rejected.bib")
    ap.add_argument("--report", default="doi-mismatch-repair.md")
    ap.add_argument("--verification", default="verification-report.md")
    ap.add_argument("--accept", type=float, default=0.90)
    ap.add_argument("--borderline", type=float, default=0.75)
    ap.add_argument("--delay", type=float, default=0.4)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    flagged = set(re.findall(
        r"^- `([^`]+)` \(similarity", pathlib.Path(args.verification).read_text(), re.M
    ))
    if not flagged:
        sys.exit("no flagged entries found in the verification report")

    path = pathlib.Path(args.bib)
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    db = bibtexparser.loads(path.read_text(), parser=parser)

    fixed, borderline, unfindable = [], [], []
    for e in db.entries:
        if e["ID"] not in flagged:
            continue
        bib_title = (e.get("title") or "").strip("{} ")
        old_doi = norm_doi(e.get("doi", ""))

        best_item, best_score = None, 0.0
        for it in search_by_title(bib_title):
            cand = norm_title((it.get("title") or [""])[0])
            if not cand:
                continue
            # CrossRef registers supplementary files as component DOIs ending
            # .s001 etc. They carry the article's title but resolve to the SI
            # rather than the paper, so never adopt one as a citation.
            if COMPONENT_DOI.search(it.get("DOI") or ""):
                continue
            score = difflib.SequenceMatcher(None, norm_title(bib_title), cand).ratio()
            if score > best_score:
                best_item, best_score = it, score
        time.sleep(args.delay)

        if best_item and best_score >= args.accept:
            new_doi = (best_item.get("DOI") or "").lower()
            e["doi"] = new_doi
            if not (e.get("author") or "").strip():
                authors = format_authors(best_item)
                if authors:
                    e["author"] = authors
            journal = (best_item.get("container-title") or [""])[0]
            if journal and not (e.get("journal") or "").strip():
                e["journal"] = journal
            fixed.append((e["ID"], old_doi, new_doi, best_score, bib_title))
            print(f"  FIXED {e['ID']}: {old_doi} -> {new_doi} ({best_score:.2f})")
        elif best_item and best_score >= args.borderline:
            borderline.append((e["ID"], old_doi, best_item.get("DOI"),
                               best_score, bib_title,
                               (best_item.get("title") or [""])[0]))
            print(f"  BORDERLINE {e['ID']} ({best_score:.2f}) - left alone")
        else:
            unfindable.append((e["ID"], old_doi, best_score, bib_title))
            print(f"  UNFINDABLE {e['ID']} (best {best_score:.2f}) - reject")

    reject_ids = {i for i, *_ in unfindable}
    kept = [e for e in db.entries if e["ID"] not in reject_ids]
    dropped = [e for e in db.entries if e["ID"] in reject_ids]

    print(f"\nfixed {len(fixed)}, borderline {len(borderline)}, "
          f"rejected {len(unfindable)}")

    if args.apply:
        w = bibtexparser.bwriter.BibTexWriter()
        w.indent = "  "
        w.order_entries_by = ("ID",)
        out = bibtexparser.bibdatabase.BibDatabase()
        out.entries = kept
        path.write_text(bibtexparser.dumps(out, w))

        rej_path = pathlib.Path(args.rejects)
        prev = bibtexparser.loads(rej_path.read_text(), parser=parser).entries \
            if rej_path.exists() else []
        rej = bibtexparser.bibdatabase.BibDatabase()
        rej.entries = prev + dropped
        rej_path.write_text(bibtexparser.dumps(rej, w))
        print(f"wrote {path} ({len(kept)} entries) and {rej_path}")
    else:
        print("dry run; re-run with --apply")

    report = [
        "# DOI mismatch repair",
        "",
        "Entries whose recorded DOI resolved to a different paper. In every case",
        "the DOI came from a source `.bib` file, not from automated recovery.",
        "Repaired by searching CrossRef for the recorded *title* and adopting the",
        "DOI that title actually belongs to -- never by adopting the wrong DOI's",
        "title, which would have replaced the reference with an unrelated paper.",
        "",
        f"- Flagged: **{len(flagged)}**",
        f"- DOI corrected: **{len(fixed)}**",
        f"- Borderline, left for manual review: **{len(borderline)}**",
        f"- Not findable in CrossRef, rejected: **{len(unfindable)}**",
        "",
        "## DOIs corrected",
        "",
        *(f"- `{i}` ({s:.2f}): `{old}` -> `{new}`\n  - {t[:90]}"
          for i, old, new, s, t in fixed),
        "",
        "## Borderline - needs a human",
        "",
        *(f"- `{i}` (best {s:.2f}), current DOI `{old}`, candidate `{new}`\n"
          f"  - bib:      {t[:85]}\n  - candidate: {ct[:85]}"
          for i, old, new, s, t, ct in borderline),
        "",
        "## Rejected - no CrossRef record for this title",
        "",
        "These titles match no paper CrossRef knows about, and their recorded",
        "DOIs belong to unrelated work. Treated as fabricated.",
        "",
        *(f"- `{i}` (best match {s:.2f}), bad DOI `{old}`\n  - {t[:90]}"
          for i, old, s, t in unfindable),
        "",
    ]
    pathlib.Path(args.report).write_text("\n".join(report))
    print(f"wrote {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
