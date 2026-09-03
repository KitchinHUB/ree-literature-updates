"""Map the citation keys used in `src/` back onto the verified bibliography.

Phase 1 regenerated every citation key from real author/year/title metadata,
so the keys inherited from the source documents (`cite:xie2014critical`) do not
match `references.bib`.  This rebuilds the old -> new mapping the same way the
merge did: by identity of the underlying paper, not by string similarity of the
keys, which would happily map one paper onto another.

Matching is DOI first, then normalized title with a year check.  A key that
matches nothing is reported, never guessed at.  A key whose paper was rejected
in Phase 1 is reported separately, because the claim resting on it has to be
rewritten rather than re-pointed.

Usage:
    python tools/map_citation_keys.py [--review-dir DIR] [--out FILE]
"""

from __future__ import annotations

import argparse
import difflib
import json
import pathlib
import re
import sys

import bibtexparser

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from merge_bib import SOURCES, norm_doi, norm_title  # noqa: E402

# Both org-ref styles that survive in src/: `cite:key`, `citep:key,key2`, and
# the org-cite bracket form `[cite:@key; @key2]`.
ORG_REF = re.compile(r"\bcite[a-z]*:([A-Za-z0-9_][A-Za-z0-9_,-]*)")
ORG_CITE = re.compile(r"\[cite:((?:\s*@[A-Za-z0-9_-]+\s*;?)+)\]")

TITLE_MATCH_THRESHOLD = 0.90

# The Crucible wiki bibliography stores weak `@misc` records whose DOI sits in
# the url field and whose title is prefixed "Surname YEAR - ".  Both are
# recoverable, so those entries can be matched like any other.
URL_DOI = re.compile(r"(?:doi\.org/|doi:)\s*(10\.\d{4,9}/\S+)", re.I)
TITLE_PREFIX = re.compile(r"^[A-Z][A-Za-z'\u2019-]+\s+\d{4}\s*[-\u2013\u2014]\s*")


def entry_doi(entry: dict) -> str:
    """Normalized DOI, falling back to one embedded in the url field."""
    doi = norm_doi(entry.get("doi", ""))
    if doi:
        return doi
    m = URL_DOI.search(entry.get("url", "") or "")
    return norm_doi(m.group(1)) if m else ""


def entry_title(entry: dict) -> str:
    """Normalized title with a 'Surname YEAR - ' citation prefix removed."""
    return norm_title(TITLE_PREFIX.sub("", (entry.get("title") or "").strip()))


# Keys the clay source cites that appear in no .bib file at all: they were
# written against the hand-typed reference list at the end of the source
# document.  Each was identified from that list and the DOI confirmed against
# CrossRef, so the mapping is evidence-based rather than guessed -- but it
# cannot be derived mechanically, which is why it lives here.
MANUAL = {
    "pan2024": "pan2024insights",   # MgSO4 selective leaching, 10.1016/j.jre.2024.04.025
    "shi2022": "shi2022column",     # low-ammonium column leaching, 10.1016/j.jmrt.2022.05.199
    "he2025": "he2025stepwise",     # HMTA aluminum inhibition, 10.1007/s11356-025-36598-8
    # The coacervate source recorded this title truncated ("...Driven by
    # Asymmetry", dropping "of Charge Density"), which holds the title match
    # just under threshold. Same paper: Macromolecules 55, 10.1021/acs.macromol.2c01205.
    "chen2023multiphase": "chen2022multiphase",
}


def load_bib(path: pathlib.Path) -> list[dict]:
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    db = bibtexparser.loads(path.read_text(errors="replace"), parser=parser)
    return db.entries


def keys_used(src_dir: pathlib.Path) -> dict[str, list[str]]:
    """Every citation key appearing in src/, with the files it appears in."""
    used: dict[str, list[str]] = {}
    for p in sorted(src_dir.glob("*.md")):
        text = p.read_text()
        found = set()
        for m in ORG_CITE.finditer(text):
            found.update(re.findall(r"@([A-Za-z0-9_-]+)", m.group(1)))
        # Strip the bracket form before scanning for the bare form, or
        # `[cite:@a]` would also register as the org-ref key "@a".
        for m in ORG_REF.finditer(ORG_CITE.sub("", text)):
            found.update(k for k in m.group(1).split(",") if k)
        for k in found:
            used.setdefault(k, []).append(p.name)
    return used


def index_entries(entries: list[dict]) -> tuple[dict, dict]:
    """Index a bibliography by normalized DOI and by normalized title."""
    by_doi, by_title = {}, {}
    for e in entries:
        doi = entry_doi(e)
        if doi:
            by_doi.setdefault(doi, e)
        title = entry_title(e)
        if title:
            by_title.setdefault(title, e)
    return by_doi, by_title


def best_title_match(title: str, year: str, by_title: dict):
    """Closest title above threshold, with the year agreeing within one."""
    if not title:
        return None, 0.0
    best, score = None, 0.0
    for cand_title, cand in by_title.items():
        s = difflib.SequenceMatcher(None, title, cand_title).ratio()
        if s > score:
            best, score = cand, s
    if best is None or score < TITLE_MATCH_THRESHOLD:
        return None, score
    try:
        if year and best.get("year") and abs(int(year) - int(best["year"])) > 1:
            return None, score
    except ValueError:
        pass
    return best, score


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--review-dir", default="../../ree-literature-review")
    ap.add_argument(
        "--extra-originals",
        action="append",
        default=["../../.crucible/references.bib"],
        help="additional bibliographies whose keys the chapters may cite; "
             "the Crucible wiki bib is included by default because the clay "
             "chapter was written against it",
    )
    ap.add_argument("--src", default="src")
    ap.add_argument("--bib", default="references.bib")
    ap.add_argument("--rejected", default="references-rejected.bib")
    ap.add_argument("--out", default="citation-key-map.json")
    ap.add_argument("--report", default="citation-key-map.md")
    args = ap.parse_args()

    review_dir = pathlib.Path(args.review_dir).resolve()
    used = keys_used(pathlib.Path(args.src))
    print(f"{len(used)} distinct citation keys used in {args.src}/")

    verified = load_bib(pathlib.Path(args.bib))
    verified_keys = {e["ID"] for e in verified}
    v_doi, v_title = index_entries(verified)

    rejected = load_bib(pathlib.Path(args.rejected))
    r_doi, r_title = index_entries(rejected)

    # The original records, keyed as the source documents cite them.
    originals: dict[str, dict] = {}
    for rel in SOURCES:
        path = review_dir / rel
        if not path.exists():
            sys.exit(f"missing source bibliography: {path}")
        for e in load_bib(path):
            originals.setdefault(e["ID"], e)
    for rel in args.extra_originals:
        path = (pathlib.Path(rel) if pathlib.Path(rel).is_absolute()
                else pathlib.Path(args.src).parent / rel).resolve()
        if not path.exists():
            print(f"note: extra originals not found, skipping: {path}")
            continue
        for e in load_bib(path):
            originals.setdefault(e["ID"], e)

    mapping, resolved, unknown, dead, ambiguous = {}, [], [], [], []
    for key in sorted(used):
        if key in verified_keys:
            resolved.append((key, key, "already current"))
            mapping[key] = key
            continue
        if key in MANUAL and MANUAL[key] in verified_keys:
            mapping[key] = MANUAL[key]
            resolved.append((key, MANUAL[key], "hand-identified"))
            continue
        src = originals.get(key)
        if src is None:
            unknown.append((key, used[key]))
            continue
        doi = entry_doi(src)
        hit = v_doi.get(doi) if doi else None
        how = "DOI"
        if hit is None:
            hit, score = best_title_match(
                entry_title(src), (src.get("year") or "").strip(), v_title
            )
            how = f"title {score:.2f}"
        if hit is not None:
            mapping[key] = hit["ID"]
            resolved.append((key, hit["ID"], how))
            continue
        # Not in the verified bibliography -- was it one of the 67 rejected?
        rej = r_doi.get(doi) if doi else None
        if rej is None:
            rej, _ = best_title_match(
                entry_title(src), (src.get("year") or "").strip(), r_title
            )
        if rej is not None:
            dead.append((key, used[key], src.get("title", "").strip()))
        else:
            ambiguous.append((key, used[key], src.get("title", "").strip()))

    pathlib.Path(args.out).write_text(json.dumps(mapping, indent=2, sort_keys=True) + "\n")

    lines = [
        "# Citation key map",
        "",
        "Generated by `tools/map_citation_keys.py`. Maps the citation keys",
        "inherited from the source documents onto the verified bibliography,",
        "matching on DOI first and normalized title second. Regenerate rather",
        "than editing by hand.",
        "",
        f"- Distinct keys used in `src/`: **{len(used)}**",
        f"- Resolved to a verified entry: **{len(resolved)}**",
        f"- Cite a paper deleted in Phase 1: **{len(dead)}**",
        f"- In a source bibliography but matched nothing: **{len(ambiguous)}**",
        f"- Not in any source bibliography: **{len(unknown)}**",
        "",
        "## Resolved",
        "",
        "| Old key | New key | Matched on |",
        "|---|---|---|",
    ]
    lines += [f"| `{a}` | `{b}` | {c} |" for a, b, c in resolved]

    if dead:
        lines += [
            "",
            "## Cites a rejected reference",
            "",
            "These keys name papers that failed Phase 1 verification and were",
            "moved to `references-rejected.bib`. The claim resting on each has",
            "to be rewritten or removed -- do not re-point it at a neighbour.",
            "",
            "| Key | Files | Recorded title |",
            "|---|---|---|",
        ]
        lines += [f"| `{k}` | {', '.join(f)} | {t} |" for k, f, t in dead]

    if ambiguous:
        lines += [
            "",
            "## In a source bibliography, matched nothing",
            "",
            "| Key | Files | Recorded title |",
            "|---|---|---|",
        ]
        lines += [f"| `{k}` | {', '.join(f)} | {t} |" for k, f, t in ambiguous]

    if unknown:
        lines += [
            "",
            "## Not in any source bibliography",
            "",
            "The source document cited a key that never existed in the `.bib`",
            "it sat next to. Treat these as unsupported claims.",
            "",
            "| Key | Files |",
            "|---|---|",
        ]
        lines += [f"| `{k}` | {', '.join(f)} |" for k, f in unknown]

    pathlib.Path(args.report).write_text("\n".join(lines) + "\n")
    print(f"resolved {len(resolved)}, rejected {len(dead)}, "
          f"unmatched {len(ambiguous)}, unknown {len(unknown)}")
    print(f"wrote {args.out} and {args.report}")


if __name__ == "__main__":
    main()
