"""Merge the REE review bibliographies into one deduplicated, re-keyed file.

Merges five topic .bib files from ree-literature-review/. nnl.bib is
deliberately excluded: it is a general materials-science library with zero DOI
overlap with these five, and 147 of its entries carry no verifiable identifier.

Deduplication is two-pass because a DOI-only pass misses real duplicates:
17 cross-file title duplicates have no DOI on at least one side, and 10
cross-file DOI duplicates carry *different* citation keys, so merging by key
would silently keep both.

Usage:
    python tools/merge_bib.py [--review-dir DIR] [--out FILE] [--report FILE]
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
import unicodedata
from collections import defaultdict

import bibtexparser

# Source files, in precedence order. Earlier files win ties only when metadata
# completeness is equal; completeness is the primary criterion.
SOURCES = [
    "colorimetric-microfluidic-separation.bib",  # cleanest: 17/17 keys resolve
    "coacervate.bib",
    "high-throughput-ree-refs.bib",
    "carbochlorination/carbohalogenation_references.bib",
    "rare_earth_separation_references.bib",  # largest but weakest metadata
]

# Fabricated author placeholders found in the carbochlorination bib, e.g.
# author = {{PNAS Authors}}. The recorded authorship is known-wrong.
PLACEHOLDER_AUTHOR = re.compile(
    r"^\{?\{?\s*[\w\s.&'-]+?\s+Authors\s*\}?\}?$", re.IGNORECASE
)

STOPWORDS = {
    "a", "an", "the", "of", "for", "and", "on", "in", "to", "from", "with",
    "by", "at", "as", "via", "into", "using", "toward", "towards", "new",
    "novel", "recent", "study", "studies", "review",
}


def norm_doi(raw: str) -> str:
    """Normalize a DOI for comparison: strip resolver prefixes and case."""
    d = (raw or "").strip().lower()
    d = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", d)
    d = re.sub(r"^doi:\s*", "", d)
    return d.strip().rstrip(".")


def norm_title(raw: str) -> str:
    """Aggressively normalize a title so formatting differences collapse."""
    t = (raw or "").lower()
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"<[^>]+>", " ", t)          # strip <sub>/<sup> markup
    t = re.sub(r"[{}\\$]", " ", t)          # strip TeX braces and math
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def first_author_surname(entry: dict) -> str:
    """Best-effort surname of the first author, '' when unusable."""
    author = (entry.get("author") or "").strip()
    if not author or PLACEHOLDER_AUTHOR.match(author):
        return ""
    first = re.split(r"\s+and\s+", author)[0].strip().strip("{}")
    if "," in first:                        # "Surname, Given"
        surname = first.split(",")[0]
    else:                                   # "Given Surname"
        surname = first.split()[-1] if first.split() else ""
    surname = unicodedata.normalize("NFKD", surname)
    surname = "".join(c for c in surname if not unicodedata.combining(c))
    return re.sub(r"[^a-zA-Z]", "", surname).lower()


def title_word(entry: dict) -> str:
    """First meaningful title word, for the key suffix."""
    for w in norm_title(entry.get("title", "")).split():
        if w not in STOPWORDS and len(w) > 2 and not w.isdigit():
            return w
    return "untitled"


def completeness(entry: dict) -> tuple:
    """Rank records so the richest duplicate survives a merge."""
    has_real_author = bool(first_author_surname(entry))
    return (
        bool(norm_doi(entry.get("doi", ""))),
        has_real_author,
        bool(entry.get("url", "").strip()),
        bool(entry.get("journal", "").strip()),
        bool(entry.get("year", "").strip()),
        sum(1 for v in entry.values() if str(v).strip()),
    )


def merge_pair(keep: dict, drop: dict) -> dict:
    """Fill empty fields on the surviving record from the discarded one."""
    for k, v in drop.items():
        if k in ("ID", "ENTRYTYPE"):
            continue
        if str(v).strip() and not str(keep.get(k, "")).strip():
            keep[k] = v
    keep.setdefault("_merged_from", "")
    merged = [x for x in keep["_merged_from"].split(";") if x]
    merged.append(f"{drop['_source']}:{drop['ID']}")
    keep["_merged_from"] = ";".join(merged)
    return keep


def load_all(review_dir: pathlib.Path) -> list[dict]:
    entries = []
    for rel in SOURCES:
        path = review_dir / rel
        if not path.exists():
            sys.exit(f"missing source bibliography: {path}")
        parser = bibtexparser.bparser.BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = False
        db = bibtexparser.loads(path.read_text(errors="replace"), parser=parser)
        for e in db.entries:
            e["_source"] = pathlib.Path(rel).name
            entries.append(e)
    return entries


def dedupe(entries: list[dict]) -> tuple[list[dict], list[str]]:
    """Two-pass dedup: exact DOI, then title+year for entries lacking a DOI."""
    log: list[str] = []

    # Pass 1 - exact normalized DOI.
    by_doi: dict[str, dict] = {}
    no_doi: list[dict] = []
    for e in entries:
        doi = norm_doi(e.get("doi", ""))
        if not doi:
            no_doi.append(e)
            continue
        if doi in by_doi:
            a, b = by_doi[doi], e
            keep, drop = (a, b) if completeness(a) >= completeness(b) else (b, a)
            by_doi[doi] = merge_pair(keep, drop)
            log.append(
                f"DOI  {doi}: kept {keep['_source']}:{keep['ID']}, "
                f"dropped {drop['_source']}:{drop['ID']}"
            )
        else:
            by_doi[doi] = e

    # Pass 2 - title+year, covering no-DOI entries and their DOI-bearing twins.
    survivors = list(by_doi.values())
    by_title: dict[tuple, dict] = {}
    for e in survivors:
        key = (norm_title(e.get("title", "")), (e.get("year") or "").strip())
        if key[0]:
            by_title.setdefault(key, e)

    kept_no_doi: list[dict] = []
    for e in no_doi:
        t, y = norm_title(e.get("title", "")), (e.get("year") or "").strip()
        if not t:
            kept_no_doi.append(e)
            continue
        twin = by_title.get((t, y)) or by_title.get((t, ""))
        if twin is not None:
            merge_pair(twin, e)
            log.append(
                f"TITLE '{t[:60]}': folded {e['_source']}:{e['ID']} "
                f"into {twin['_source']}:{twin['ID']}"
            )
            continue
        dup = next(
            (o for o in kept_no_doi
             if norm_title(o.get("title", "")) == t
             and (o.get("year") or "").strip() == y),
            None,
        )
        if dup is not None:
            keep, drop = (dup, e) if completeness(dup) >= completeness(e) else (e, dup)
            if keep is e:
                kept_no_doi[kept_no_doi.index(dup)] = e
            merge_pair(keep, drop)
            log.append(
                f"TITLE '{t[:60]}': merged two no-DOI records "
                f"({keep['_source']}:{keep['ID']} kept)"
            )
        else:
            kept_no_doi.append(e)
            by_title.setdefault((t, y), e)

    return survivors + kept_no_doi, log


def rekey(entries: list[dict]) -> list[str]:
    """Assign lastnameYEARword keys from actual metadata, not existing keys."""
    warnings: list[str] = []
    used: dict[str, int] = defaultdict(int)
    for e in entries:
        surname = first_author_surname(e)
        if not surname:
            surname = "anon"
            warnings.append(
                f"no usable author: {e['_source']}:{e['ID']} "
                f"({(e.get('title') or '')[:70]})"
            )
        year = re.sub(r"[^0-9]", "", e.get("year", "")) or "nodate"
        base = f"{surname}{year}{title_word(e)}"
        used[base] += 1
        e["_old_id"] = e["ID"]
        e["ID"] = base if used[base] == 1 else f"{base}{chr(ord('a') + used[base] - 2)}"
    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--review-dir",
        default="../../ree-literature-review",
        help="directory holding the source .bib files",
    )
    ap.add_argument("--out", default="references.bib")
    ap.add_argument("--report", default="bibliography-audit.md")
    args = ap.parse_args()

    review_dir = pathlib.Path(args.review_dir).resolve()
    entries = load_all(review_dir)
    print(f"loaded {len(entries)} entries from {len(SOURCES)} files")

    merged, log = dedupe(entries)
    print(f"after dedup: {len(merged)} entries ({len(entries) - len(merged)} removed)")

    warnings = rekey(merged)
    merged.sort(key=lambda e: e["ID"])

    placeholder = [
        e for e in merged if PLACEHOLDER_AUTHOR.match((e.get("author") or "").strip())
    ]
    unverifiable = [
        e for e in merged
        if not any(str(e.get(k, "")).strip() for k in ("doi", "url", "isbn"))
    ]
    missing_doi = [e for e in merged if not norm_doi(e.get("doi", ""))]

    db = bibtexparser.bibdatabase.BibDatabase()
    db.entries = [
        {k: v for k, v in e.items() if not k.startswith("_")} for e in merged
    ]
    writer = bibtexparser.bwriter.BibTexWriter()
    writer.indent = "  "
    writer.order_entries_by = ("ID",)
    pathlib.Path(args.out).write_text(bibtexparser.dumps(db, writer))

    report = [
        "# Bibliography audit",
        "",
        f"- Source files merged: {len(SOURCES)} (`nnl.bib` excluded: disjoint, "
        "general materials science, 147 unverifiable entries)",
        f"- Entries loaded: **{len(entries)}**",
        f"- Entries after dedup: **{len(merged)}** "
        f"({len(entries) - len(merged)} duplicates removed)",
        f"- Missing a DOI: **{len(missing_doi)}**",
        f"- No DOI, URL, or ISBN — unverifiable as recorded: **{len(unverifiable)}**",
        f"- Placeholder `{{Journal}} Authors` fields: **{len(placeholder)}**",
        "",
        "## Duplicates removed",
        "",
        *(f"- {line}" for line in log),
        "",
        "## Entries with no usable author",
        "",
        *(f"- {w}" for w in warnings),
        "",
        "## Unverifiable as recorded (no DOI/URL/ISBN)",
        "",
        *(
            f"- `{e['ID']}` ({e['_source']}) — {(e.get('title') or '')[:90]}"
            for e in unverifiable
        ),
        "",
        "## Placeholder author fields (authorship known-wrong)",
        "",
        *(
            f"- `{e['ID']}` — author = {{{e.get('author', '')}}} — "
            f"{(e.get('title') or '')[:70]}"
            for e in placeholder
        ),
        "",
    ]
    pathlib.Path(args.report).write_text("\n".join(report))

    print(f"missing DOI: {len(missing_doi)}")
    print(f"unverifiable (no doi/url/isbn): {len(unverifiable)}")
    print(f"placeholder authors: {len(placeholder)}")
    print(f"wrote {args.out} and {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
