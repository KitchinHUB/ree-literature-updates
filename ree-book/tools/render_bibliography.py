"""Generate `src/92-references.md`: a consolidated, cross-referenced bibliography.

MyST renders a reference list at the foot of every page that cites something,
so there is no whole-book list to render and a hand-written bibliography page
stays empty. This builds one, and makes it worth more than a flat list by
recording *where each work is cited* -- so the page doubles as a citation
index: pick a paper, see which chapters draw on it.

Only cited entries are listed. `references.bib` was merged from five source
bibliographies and covers more ground than the book does; listing the
uncited remainder would misrepresent what the book actually rests on.

The page is generated, not edited. Re-run after adding citations.

A companion `src/references-cited.bib` is written alongside the page: the same
entries, verbatim, as a file a reader can download and import into Zotero.
Entries are copied byte-for-byte out of `references.bib` rather than
re-serialized, so nothing is lost in a round trip.

The uncited remainder is not silently dropped: `--orphans` writes
`orphan-references.md`, so the entries that survived verification but that no
chapter draws on stay visible and can be pruned deliberately.

Usage:
    python tools/render_bibliography.py [--check] [--orphans]
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

import bibtexparser

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = SRC / "92-references.md"
ORPHANS = ROOT / "orphan-references.md"
CITED_BIB = SRC / "references-cited.bib"

CITE_GROUP = re.compile(r"\[([^\]\[]*@[^\]\[]*)\]")
KEY = re.compile(r"@([A-Za-z0-9_:.\-]+)")
# A narrative citation -- `@smith2020thing showed` -- renders as a citation
# just as `[@smith2020thing]` does, and the book uses both forms. Scanning
# only the bracketed one silently dropped real works from this page.
NARRATIVE = re.compile(r"(?<![\w/\-.])@([A-Za-z][A-Za-z0-9_:.\-]*)")
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)
LABEL = re.compile(r"^\(([a-z0-9-]+)\)=\s*$", re.M)


def cited_by(known: set[str] | None = None) -> dict[str, list[tuple[str, str]]]:
    """key -> [(chapter label, chapter title)], in reading order.

    `known` is the set of keys in `references.bib`. Bracketed citations are
    taken as written, so a typo in one is still reported as a missing key.
    A narrative citation is accepted only when it names a real entry: an
    `@` in prose is not always a citation.
    """
    out: dict[str, list[tuple[str, str]]] = {}
    for path in sorted(SRC.glob("*.md")):
        if path.name == OUT.name:
            continue
        text = path.read_text()
        m = LABEL.search(text)
        t = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", text, re.M)
        if not m or not t:
            continue
        where = (m.group(1), t.group(1))

        def record(key: str) -> None:
            seen = out.setdefault(key, [])
            if where not in seen:
                seen.append(where)

        body = CODE.sub(" ", text)
        for g in CITE_GROUP.finditer(body):
            for key in KEY.findall(g.group(1)):
                record(key)
        # Narrative keys live outside the bracketed groups; blank those out
        # first rather than counting the same citation twice.
        for raw in NARRATIVE.findall(CITE_GROUP.sub(" ", body)):
            key = raw.rstrip(".-:")
            if known is None or key in known:
                record(key)
    return out


def escape(s: str) -> str:
    """Strip BibTeX braces and escape what MyST would otherwise interpret."""
    s = re.sub(r"[{}]", "", s or "")
    s = re.sub(r"\s+", " ", s).strip()
    return s.replace("\\", "").replace("$", r"\$").replace("*", r"\*")


def author_list(raw: str) -> str:
    names = [escape(a) for a in re.split(r"\s+and\s+", raw or "") if a.strip()]
    if not names:
        return ""
    if len(names) > 8:
        return names[0] + " and others"
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + " and " + names[-1]


def sort_key(e: dict) -> tuple:
    a = escape(e.get("author", "")).lower()
    return (a or "zzz", e.get("year", ""), escape(e.get("title", "")).lower())


def render(e: dict, where: list[tuple[str, str]]) -> str:
    bits = []
    authors = author_list(e.get("author", ""))
    if authors:
        bits.append(authors)
    year = escape(e.get("year", ""))
    bits.append(f"({year})." if year else "(n.d.).")
    bits.append(f"*{escape(e.get('title', 'Untitled'))}*.")

    venue = escape(e.get("journal") or e.get("booktitle") or "")
    if venue:
        vol = escape(e.get("volume", ""))
        pages = escape(e.get("pages", "")).replace("--", "–")
        venue += f", {vol}" if vol else ""
        venue += f", {pages}" if pages else ""
        bits.append(venue + ".")
    elif e.get("institution"):
        bits.append(escape(e["institution"]) + ".")
    elif e.get("publisher"):
        bits.append(escape(e["publisher"]) + ".")

    doi = escape(e.get("doi", ""))
    if doi:
        bits.append(f"[{doi}](https://doi.org/{doi}).")
    elif e.get("url"):
        bits.append(f"[link]({e['url'].strip()}).")
    elif e.get("isbn"):
        bits.append(f"ISBN {escape(e['isbn'])}.")

    cited = ", ".join(f"[](#{label})" for label, _ in where)
    return "- " + " ".join(bits) + f" Cited in {cited}."


def write_cited_bib(raw: str, keys: set[str]) -> None:
    """Copy the cited entries verbatim into a downloadable .bib."""
    blocks, keep, depth, buf = [], False, 0, []
    for line in raw.splitlines(keepends=True):
        if depth == 0 and line.lstrip().startswith("@"):
            key = re.match(r"\s*@\w+\s*\{\s*([^,\s]+)", line)
            keep = bool(key) and key.group(1) in keys
            buf = []
        if keep:
            buf.append(line)
        depth += line.count("{") - line.count("}")
        if depth <= 0 and buf and line.strip().startswith("}"):
            blocks.append("".join(buf))
            keep, buf, depth = False, [], 0
    header = (
        "% Works cited in \"Rare Earth Element Separations\".\n"
        f"% {len(blocks)} entries, each verified against CrossRef, a live URL,\n"
        "% or an ISBN. Generated by tools/render_bibliography.py -- do not edit.\n\n"
    )
    CITED_BIB.write_text(header + "\n".join(blocks))
    print(f"wrote {CITED_BIB.relative_to(ROOT)} with {len(blocks)} entries")


def write_orphans(orphans: list[dict]) -> None:
    """Record the verified-but-uncited entries so nothing is pruned blind."""
    lines = [
        "# Orphan references",
        "",
        f"{len(orphans)} entries in `references.bib` that survived verification",
        "but that no chapter cites. `references.bib` was merged from five source",
        "bibliographies covering more ground than the book does, so orphans are",
        "expected. They are listed rather than deleted: each is a real, verified",
        "source, and several are candidates for chapters that are still thin.",
        "",
        "Generated by `python tools/render_bibliography.py --orphans`.",
        "",
        "| key | year | first author | title | venue |",
        "| --- | ---- | ------------ | ----- | ----- |",
    ]
    def cell(s: str) -> str:
        return escape(s).replace("|", r"\|")
    for e in sorted(orphans, key=sort_key):
        first = re.split(r"\s+and\s+", e.get("author", "") or "")[0]
        venue = e.get("journal") or e.get("booktitle") or e.get("publisher") or ""
        lines.append(f"| `{e['ID']}` | {cell(e.get('year',''))} | {cell(first)} "
                     f"| {cell(e.get('title',''))} | {cell(venue)} |")
    ORPHANS.write_text("\n".join(lines) + "\n")
    print(f"wrote {ORPHANS.relative_to(ROOT)} with {len(orphans)} uncited entries")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="fail if the page is out of date instead of writing it")
    ap.add_argument("--orphans", action="store_true",
                    help="also write orphan-references.md, the uncited entries")
    args = ap.parse_args()

    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    raw = (ROOT / "references.bib").read_text()
    db = bibtexparser.loads(raw, parser=parser)
    entries = {e["ID"]: e for e in db.entries}

    where = cited_by(set(entries))
    missing = sorted(k for k in where if k not in entries)
    if missing:
        print("cited but not in references.bib:", ", ".join(missing), file=sys.stderr)
        return 1

    cited = sorted((entries[k] for k in where), key=sort_key)
    lines = [
        "---",
        "title: Bibliography",
        "downloads:",
        "  - file: references-cited.bib",
        f"    title: references-cited.bib — the {len(cited)} works cited",
        "  - file: ../references.bib",
        f"    title: references.bib — the full {len(entries)}-entry working bibliography",
        "---",
        "",
        "(bibliography)=",
        "# Bibliography",
        "",
        f"The {len(cited)} sources cited in this book, with the chapters that cite",
        "each one. Every entry was verified against CrossRef, a live URL, or an",
        "ISBN; see `bibliography-audit.md` and `verification-report.md` for what",
        "was removed during verification and why.",
        "",
        "Each chapter also carries its own reference list at the foot of the page.",
        "",
        "**Import these into Zotero, Mendeley, or BibTeX:** download",
        "{download}`references-cited.bib <references-cited.bib>` for the "
        f"{len(cited)} works below, or",
        "{download}`references.bib <../references.bib>` for the full "
        f"{len(entries)}-entry working bibliography, which covers more ground",
        "than the book does. In Zotero: *File → Import…*, then pick the file.",
        "",
        "```{note}",
        "This page is generated by `tools/render_bibliography.py`. Edit the",
        "bibliography, not this file.",
        "```",
        "",
    ]
    lines += [render(e, where[e["ID"]]) for e in cited]
    page = "\n".join(lines) + "\n"

    if args.check:
        if OUT.exists() and OUT.read_text() == page:
            print(f"up to date ({len(cited)} entries)")
            return 0
        print("92-references.md is out of date; re-run without --check",
              file=sys.stderr)
        return 1

    OUT.write_text(page)
    write_cited_bib(raw, set(where))
    print(f"wrote {OUT.relative_to(ROOT)} with {len(cited)} cited entries "
          f"({len(entries) - len(cited)} uncited entries omitted)")

    if args.orphans:
        write_orphans([e for k, e in entries.items() if k not in where])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
