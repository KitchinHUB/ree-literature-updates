"""Extract plain text from the key-named PDFs in `fulltexts/all/` into a cache.

The facet tagger needs to know what a paper is *about*, and `references.bib`
does not carry enough to tell it: only 126 of 758 entries have an abstract and
only 325 have keywords, so matching element names against the bibliography
alone finds a specific element in just 122 entries. Most of the signal is in
the PDFs, 578 of which are named for their citation key and so need no lookup
table (see `fulltexts/README.md` for why the rest are not).

Text is written to `fulltexts/.text-cache/<key>.txt`, gitignored alongside the
PDFs it comes from -- publisher PDFs are not redistributable and neither is
their text. Only the derived counts in `facets.json` are ever committed.

The first two pages and the last page are skipped by default. Front matter is
mastheads, author affiliations and copyright boilerplate, and the last page is
usually references -- a reference list names every element and extractant the
field has ever used, which is exactly the noise the threshold in
`build_facets.py` exists to suppress. Dropping them at the source is cheaper
than filtering them later.

Caching is by (path, size, mtime), so a re-run after adding PDFs only reads the
new ones.

Usage:
    python tools/extract_fulltext_cache.py [--force] [--limit N]
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDFS = ROOT / "fulltexts" / "all"
CACHE = ROOT / "fulltexts" / ".text-cache"
STAMP = CACHE / ".stamp.json"

# The convention from fulltexts/README.md: `<author><year><word>.pdf`. Files
# named by the publisher (`1-s2.0-S0304386X23000294-main.pdf`) carry no key and
# are skipped -- fulltext_inventory.py resolves those by scanning for a DOI,
# which is the slow path this deliberately avoids.
KEY = re.compile(r"^[a-z]+\d{4}[a-z0-9]+$")

SKIP_HEAD = 2   # mastheads, affiliations, copyright
SKIP_TAIL = 1   # reference lists


def extract(path: pathlib.Path) -> str:
    import fitz

    with fitz.open(path) as doc:
        n = doc.page_count
        lo = SKIP_HEAD if n > SKIP_HEAD + SKIP_TAIL + 1 else 0
        hi = n - SKIP_TAIL if n > SKIP_HEAD + SKIP_TAIL + 1 else n
        parts = []
        for i in range(lo, hi):
            try:
                parts.append(doc.load_page(i).get_text("text"))
            except Exception as exc:              # a damaged page, not a damaged file
                print(f"  ! {path.name} page {i}: {exc}", file=sys.stderr)
    text = "\n".join(parts)
    # Hyphenation across a line break splits "neodym-\nium" into two tokens that
    # match nothing. Ligatures do the same to "fluoride".
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    return text.replace("ﬁ", "fi").replace("ﬂ", "fl")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-extract everything")
    ap.add_argument("--limit", type=int, help="stop after N PDFs, for a smoke test")
    args = ap.parse_args()

    if not PDFS.is_dir():
        sys.exit(f"no {PDFS}; nothing to extract")

    CACHE.mkdir(parents=True, exist_ok=True)
    stamp = {} if args.force else json.loads(STAMP.read_text()) if STAMP.exists() else {}

    todo = []
    for p in sorted(PDFS.glob("*.pdf")):
        key = p.stem
        if not KEY.match(key):
            continue
        st = p.stat()
        sig = [st.st_size, int(st.st_mtime)]
        if stamp.get(key) == sig and (CACHE / f"{key}.txt").exists():
            continue
        todo.append((key, p, sig))

    if args.limit:
        todo = todo[: args.limit]

    print(f"{len(todo)} PDFs to extract ({len(stamp)} already cached)")
    ok = fail = 0
    for i, (key, path, sig) in enumerate(todo, 1):
        try:
            text = extract(path)
        except Exception as exc:
            print(f"  ! {path.name}: {exc}", file=sys.stderr)
            fail += 1
            continue
        (CACHE / f"{key}.txt").write_text(text, encoding="utf-8")
        stamp[key] = sig
        ok += 1
        if i % 50 == 0:
            print(f"  {i}/{len(todo)}")
            STAMP.write_text(json.dumps(stamp))

    STAMP.write_text(json.dumps(stamp))
    total = len(list(CACHE.glob("*.txt")))
    print(f"extracted {ok}, failed {fail}; cache holds {total} texts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
