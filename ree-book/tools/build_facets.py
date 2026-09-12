"""Build `static/search/facets.json`: the bibliography, faceted for the search page.

The search page filters 758 works by element, extractant, technique, feedstock
and topic. Nothing in `references.bib` supports that directly -- only 126
entries carry an abstract and only 325 carry keywords, and matching element
names against the bibliography alone finds a specific element in 122 entries,
which would make a periodic table that is empty for most of the periodic table.

So evidence is drawn from three places, in descending order of trust:

1. **Title and keywords.** Author-chosen and about the work as a whole. One
   mention is enough to tag.
2. **Abstract.** Same, where it exists.
3. **Full text**, from the 578 key-named PDFs cached by
   `extract_fulltext_cache.py`. This is where most of the signal lives and all
   of the noise: every paper in the field mentions neodymium somewhere. A
   mention here counts only above the thresholds below.

`element` and `topic` come from `facet-tags.json` instead -- a committed,
hand-checkable file written by the tagging pass. Regex can tell you a paper
says "neodymium"; it cannot tell you whether the paper is *about* neodymium,
and it certainly cannot tell a mechanistic study from a flowsheet design. The
regex element counts are still computed and are used to flag disagreements
with `--audit`, which is how the tag file gets checked.

Thresholds (calibrated on this corpus -- see `--calibrate`):

  MIN_HITS       4   absolute floor for a full-text mention to count at all
  DOMINANCE   0.15   and, for elements, at least this share of the most-
                     mentioned element in the same work

The dominance rule is what separates a paper about the Nd/Dy pair (Nd 50,
Dy 40, La 3 -> Nd and Dy) from a survey that name-checks all seventeen.

Usage:
    python tools/build_facets.py [--audit] [--calibrate] [--check]
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import bibtexparser                                        # noqa: E402
import facet_vocab as V                                    # noqa: E402
import render_bibliography as RB                           # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
BIB = ROOT / "references.bib"
CACHE = ROOT / "fulltexts" / ".text-cache"
TAGS = ROOT / "facet-tags.json"
OUT = ROOT / "static" / "search" / "facets.json"

MIN_HITS = 4
DOMINANCE = 0.15

# LaTeX escapes survive bibtexparser and would be rendered literally.
TEX = [(r"\{\\\"([aouAOU])\}", r"\1"), (r"\{\\'([a-zA-Z])\}", r"\1"),
       (r"\{\\`([a-zA-Z])\}", r"\1"), (r"\{\\~([a-zA-Z])\}", r"\1"),
       (r"\{\\v ?([a-zA-Z])\}", r"\1"), (r"\{\\ss\}", "ss"),
       (r"[{}]", ""), (r"\\&", "&"), (r"\s+", " ")]


def clean(s: str) -> str:
    for pat, rep in TEX:
        s = re.sub(pat, rep, s)
    return s.strip()


def short_authors(raw: str) -> str:
    """`Zhang, Wei and Li, Bo` -> `Zhang & Li`; three or more -> `Zhang et al.`"""
    if not raw:
        return ""
    names = [clean(a).strip() for a in re.split(r"\s+and\s+", raw)]
    surnames = [n.split(",")[0].strip() if "," in n else n.split()[-1] for n in names if n]
    if not surnames:
        return ""
    if len(surnames) == 1:
        return surnames[0]
    if len(surnames) == 2:
        return f"{surnames[0]} & {surnames[1]}"
    return f"{surnames[0]} et al."


def compile_group(terms):
    return [(lab, re.compile(rx, 0 if cased else re.I)) for lab, rx, cased in terms]


def element_regexes():
    out = {}
    for sym, name, _z, _g in V.ELEMENTS:
        out[sym] = [re.compile(rx, 0 if cased else re.I)
                    for rx, cased in V.element_patterns(sym, name)]
    return out


def count(patterns, text: str) -> int:
    return sum(len(p.findall(text)) for p in patterns)


def load_entries():
    with open(BIB, encoding="utf-8") as fh:
        db = bibtexparser.load(fh)
    return db.entries


def evidence(entry) -> tuple[str, str]:
    """(strong, weak) text: title+keywords, and abstract+full text."""
    strong = " ".join(clean(entry.get(f, "")) for f in ("title", "keywords"))
    weak = clean(entry.get("abstract", ""))
    cached = CACHE / f"{entry['ID']}.txt"
    if cached.exists():
        weak += "\n" + cached.read_text(encoding="utf-8", errors="replace")
    return strong, weak


def facets_for(entry, groups, elems):
    """-> (facet dict from regex, element hit counts)."""
    strong, weak = evidence(entry)
    out = {}
    for gid, _label, terms in groups:
        hits = []
        for lab, pat in terms:
            if pat.search(strong) or count([pat], weak) >= MIN_HITS:
                hits.append(lab)
        out[gid] = hits

    ecounts = {}
    for sym, pats in elems.items():
        s = count(pats, strong)
        w = count(pats, weak)
        ecounts[sym] = (s, w)
    return out, ecounts


def elements_from_counts(ecounts) -> list[str]:
    """The regex opinion on which elements a work is about."""
    top = max((w for _s, w in ecounts.values()), default=0)
    out = []
    for sym, (s, w) in ecounts.items():
        if s:                                    # named in title or keywords
            out.append(sym)
        elif w >= MIN_HITS and w >= DOMINANCE * top:
            out.append(sym)
    return out


def chapter_urls() -> dict[str, str]:
    """MyST label -> the page's built URL path.

    `cited_by` reports the `(label)=` anchor, which is written for prose
    cross-references and is not the URL. With `folders: true` MyST serves a
    chapter at `/src/<stem minus its ordering prefix>`, so the filename is
    what a link has to be built from. A label with no file is dropped rather
    than guessed at: a link to nowhere is worse than no link.
    """
    out = {}
    for path in sorted((ROOT / "src").glob("*.md")):
        m = RB.LABEL.search(path.read_text())
        if m:
            out[m.group(1)] = "/src/" + re.sub(r"^\d+-", "", path.stem)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true",
                    help="report where facet-tags.json and the regex disagree")
    ap.add_argument("--calibrate", action="store_true",
                    help="print the hit distributions the thresholds sit in")
    ap.add_argument("--check", action="store_true", help="write nothing")
    args = ap.parse_args()

    entries = load_entries()
    groups = [(gid, lab, compile_group(terms)) for gid, lab, terms in V.GROUPS]
    elems = element_regexes()
    cited = RB.cited_by({e["ID"] for e in entries})
    curls = chapter_urls()
    tags = json.loads(TAGS.read_text()) if TAGS.exists() else {}

    records, regex_elems = [], {}
    for e in entries:
        key = e["ID"]
        f, ecounts = facets_for(e, groups, elems)
        regex_elems[key] = elements_from_counts(ecounts)

        t = tags.get(key, {})
        f["element"] = t.get("element", regex_elems[key])
        f["topic"] = t.get("topic", [])

        records.append({
            "key": key,
            "title": clean(e.get("title", "")),
            "authors": short_authors(e.get("author", "")),
            "year": e.get("year", ""),
            "venue": clean(e.get("journal") or e.get("booktitle") or
                           e.get("publisher") or e.get("institution", "")),
            "doi": e.get("doi", ""),
            "url": e.get("url", ""),
            "cited": [[curls[lab], title] for lab, title in cited.get(key, [])
                      if lab in curls],
            "f": {k: v for k, v in f.items() if v},
            "ft": (CACHE / f"{key}.txt").exists(),
        })

    if args.calibrate:
        return calibrate(records, entries, groups, elems)
    if args.audit:
        return audit(records, regex_elems, tags)

    records.sort(key=lambda r: (r["authors"].lower() or r["title"].lower(), r["year"]))
    payload = {
        "groups": ([("element", "Element", [])] +
                   [(g, l, [t[0] for t in terms]) for g, l, terms in V.GROUPS] +
                   [("topic", "Topic", [t[0] for t in V.TOPICS])]),
        "elements": [[s, n, z, g] for s, n, z, g in V.ELEMENTS],
        "topics": [list(t) for t in V.TOPICS],
        "records": records,
    }
    if args.check:
        print(f"{len(records)} records, {sum(1 for r in records if r['ft'])} with full text")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, separators=(",", ":"), ensure_ascii=False))
    size = OUT.stat().st_size / 1024

    tagged = sum(1 for r in records if r["f"].get("element"))
    topiced = sum(1 for r in records if r["f"].get("topic"))
    print(f"{len(records)} records -> {OUT.relative_to(ROOT)} ({size:.0f} KB)")
    print(f"  full text available : {sum(1 for r in records if r['ft'])}")
    print(f"  with an element tag : {tagged}")
    print(f"  with a topic tag    : {topiced}")
    for gid, label, _ in V.GROUPS:
        n = sum(1 for r in records if r["f"].get(gid))
        print(f"  {label:22s}: {n}")
    return 0


def calibrate(records, entries, groups, elems) -> int:
    """Show where the thresholds fall, so they can be argued with."""
    by = collections.Counter()
    for e in entries:
        _s, weak = evidence(e)
        if not weak.strip():
            continue
        for sym, pats in elems.items():
            c = count(pats, weak)
            if c:
                by[c // 5 * 5] += 1
    print("full-text element mention counts, bucketed by 5:")
    for bucket in sorted(by):
        bar = "#" * min(60, by[bucket] // 10)
        mark = "  <- MIN_HITS" if bucket == 0 else ""
        print(f"  {bucket:4d}+ {by[bucket]:5d} {bar}{mark}")
    n = sum(len(r["f"].get("element", [])) for r in records)
    print(f"\nelements per record, mean {n / max(1, len(records)):.2f}")
    return 0


def audit(records, regex_elems, tags) -> int:
    """Where the tag file and the regex disagree about elements."""
    if not tags:
        print("no facet-tags.json yet; nothing to audit")
        return 0
    bad = 0
    for r in records:
        key = r["key"]
        if key not in tags:
            continue
        tagged = set(tags[key].get("element", []))
        found = set(regex_elems[key])
        # Only full-text-backed disagreements are interesting; a work with no
        # PDF gives the regex nothing to go on.
        if not r["ft"]:
            continue
        missed = found - tagged
        extra = tagged - found
        if len(missed) > 2 or len(extra) > 2:
            bad += 1
            print(f"{key}: tags={sorted(tagged)} regex={sorted(found)}")
            print(f"    {r['title'][:90]}")
    print(f"\n{bad} records disagree by more than two elements "
          f"({len(tags)} tagged, {len(records)} total)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
