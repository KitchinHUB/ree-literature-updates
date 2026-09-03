"""Add references to `references.bib` from DOIs, using CrossRef as the source.

Everything in the bibliography has to clear the same bar: the DOI resolves, and
the metadata recorded is the metadata CrossRef returns rather than whatever a
source document happened to write down.  This applies that bar to references
that arrive later than Phase 1 -- a citation from a knowledge base, a paper
added in response to an issue -- so they do not become a second, softer tier.

Keys follow the project convention (`lastnameYEARword`) computed from the
CrossRef metadata, not from the key the source used.

Usage:
    python tools/add_refs.py DOI [DOI ...]
    python tools/add_refs.py --file pairs.txt   # "anykey DOI" per line, key ignored
    python tools/add_refs.py --dry-run 10.1234/abcd
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

import bibtexparser

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from merge_bib import norm_doi, norm_title, title_word  # noqa: E402

UA = "ree-book/1.0 (https://github.com/KitchinHUB/ree-literature-updates; mailto:jkitchin@andrew.cmu.edu)"

TYPE_MAP = {
    "journal-article": "article",
    "proceedings-article": "inproceedings",
    "book": "book",
    "reference-book": "book",
    "monograph": "book",
    "edited-book": "book",
    "book-chapter": "inbook",
    "posted-content": "misc",
    "report": "techreport",
    "dataset": "misc",
}


def crossref(doi: str) -> dict:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as fh:
        import json
        return json.load(fh)["message"]


def strip_markup(s: str) -> str:
    """CrossRef titles carry <i>/<sub> markup and hard line breaks."""
    s = re.sub(r"<[^>]+>", "", s or "")
    return re.sub(r"\s+", " ", s).strip()


def surname(author: dict) -> str:
    return author.get("family") or author.get("name") or ""


def key_for(msg: dict) -> str:
    au = msg.get("author") or []
    last = surname(au[0]) if au else ""
    last = re.sub(r"[^a-zA-Z]", "", last).lower() or "anon"
    year = str((msg.get("issued", {}).get("date-parts") or [[None]])[0][0] or "0000")
    word = title_word({"title": strip_markup((msg.get("title") or [""])[0])})
    return f"{last}{year}{word}"


def entry_for(msg: dict) -> dict:
    au = msg.get("author") or []
    authors = " and ".join(
        f"{a['family']}, {a['given']}" if a.get("family") and a.get("given")
        else surname(a)
        for a in au
        if surname(a)
    )
    year = (msg.get("issued", {}).get("date-parts") or [[None]])[0][0]
    e = {
        "ENTRYTYPE": TYPE_MAP.get(msg.get("type", ""), "article"),
        "ID": key_for(msg),
        "title": strip_markup((msg.get("title") or [""])[0]),
        "doi": msg.get("DOI", ""),
        "url": "https://doi.org/" + msg.get("DOI", ""),
    }
    if authors:
        e["author"] = authors
    if year:
        e["year"] = str(year)
    for field, src in (("journal", "container-title"), ("publisher", "publisher")):
        v = msg.get(src)
        v = v[0] if isinstance(v, list) and v else v
        if v:
            e[field] = strip_markup(v) if field == "journal" else v
    if msg.get("volume"):
        e["volume"] = msg["volume"]
    if msg.get("issue"):
        e["number"] = msg["issue"]
    if msg.get("page"):
        e["pages"] = msg["page"].replace("-", "--")
    return e


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("dois", nargs="*")
    ap.add_argument("--file", help="file with one DOI per line; a leading key is ignored")
    ap.add_argument("--bib", default="references.bib")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    dois = list(args.dois)
    if args.file:
        for line in pathlib.Path(args.file).read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            dois.append(line.split()[-1])
    if not dois:
        ap.error("no DOIs given")

    bib_path = pathlib.Path(args.bib)
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    db = bibtexparser.loads(bib_path.read_text(), parser=parser)
    have_doi = {norm_doi(e.get("doi", "")) for e in db.entries if e.get("doi")}
    have_title = {norm_title(e.get("title", "")) for e in db.entries}
    have_key = {e["ID"] for e in db.entries}

    added = []
    for doi in dois:
        d = norm_doi(doi)
        if d in have_doi:
            print(f"skip (DOI already present): {d}")
            continue
        try:
            msg = crossref(d)
        except Exception as exc:                      # noqa: BLE001
            print(f"FAIL {d}: {exc}")
            continue
        if norm_doi(msg.get("DOI", "")) != d:
            print(f"FAIL {d}: CrossRef returned {msg.get('DOI')}")
            continue
        e = entry_for(msg)
        if norm_title(e["title"]) in have_title:
            print(f"skip (title already present): {e['title'][:60]}")
            continue
        base = e["ID"]
        n = 0
        while e["ID"] in have_key:
            n += 1
            e["ID"] = base + chr(ord("a") + n - 1)
        have_key.add(e["ID"])
        have_doi.add(d)
        have_title.add(norm_title(e["title"]))
        added.append(e)
        print(f"add {e['ID']:<28} {d:<38} {e['title'][:55]}")
        time.sleep(0.2)

    if not added or args.dry_run:
        print(f"{len(added)} would be added" if args.dry_run else "nothing to add")
        return

    db.entries = sorted(db.entries + added, key=lambda e: e["ID"].lower())
    writer = bibtexparser.bwriter.BibTexWriter()
    writer.indent = "  "
    writer.order_entries_by = ("ID",)
    bib_path.write_text(bibtexparser.dumps(db, writer))
    print(f"added {len(added)} entries to {bib_path} ({len(db.entries)} total)")


if __name__ == "__main__":
    main()
