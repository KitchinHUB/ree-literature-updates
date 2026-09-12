"""Merge the tagging pass's TSV batches into `facet-tags.json`.

The topic facet and the element facet for works with no full text are assigned
by reading titles, not by regex -- see the header of `build_facets.py` for why.
That reading is done in batches of ~95 and lands as TSV, one work per line:

    <citation key>\t<topic,topic>\t[<El> <El> ...]

The third column is optional and is only wanted where `build_facets.py` has no
full text to count element mentions in; where it does, the regex opinion is
better than a guess from a title and this file should stay out of its way.

Merging is additive: a key already in `facet-tags.json` is overwritten by a
later batch, so a correction is made by re-running one batch, not by editing
JSON by hand. Unknown topic ids and unknown element symbols are hard errors --
a typo in a tag is silent everywhere else, because a facet nothing matches
looks exactly like a facet nothing was tagged with.

Usage:
    python tools/merge_facet_tags.py <batch.tsv> [<batch.tsv> ...]
"""

from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import bibtexparser                                        # noqa: E402
import facet_vocab as V                                    # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "facet-tags.json"

TOPICS = {t[0] for t in V.TOPICS}
SYMBOLS = {e[0] for e in V.ELEMENTS}


def main(paths: list[str]) -> int:
    with open(ROOT / "references.bib", encoding="utf-8") as fh:
        known = {e["ID"] for e in bibtexparser.load(fh).entries}

    tags = json.loads(OUT.read_text()) if OUT.exists() else {}
    errors, added, updated = [], 0, 0

    for p in paths:
        for lineno, line in enumerate(pathlib.Path(p).read_text().splitlines(), 1):
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.split("\t")
            key = parts[0].strip()
            where = f"{pathlib.Path(p).name}:{lineno}"

            if key not in known:
                errors.append(f"{where}: '{key}' is not in references.bib")
                continue

            topics = [t.strip() for t in parts[1].split(",") if t.strip()] if len(parts) > 1 else []
            bad = [t for t in topics if t not in TOPICS]
            if bad:
                errors.append(f"{where}: unknown topic {bad} (have: {sorted(TOPICS)})")
                continue

            rec = {"topic": topics}
            if len(parts) > 2 and parts[2].strip():
                els = parts[2].split()
                bad = [e for e in els if e not in SYMBOLS]
                if bad:
                    errors.append(f"{where}: unknown element {bad}")
                    continue
                rec["element"] = els

            if key in tags:
                updated += 1
            else:
                added += 1
            tags[key] = rec

    if errors:
        for e in errors:
            print(f"  ! {e}", file=sys.stderr)
        print(f"\n{len(errors)} errors; nothing written", file=sys.stderr)
        return 1

    OUT.write_text(json.dumps(tags, indent=1, sort_keys=True) + "\n")
    with_el = sum(1 for v in tags.values() if v.get("element"))
    print(f"{added} added, {updated} updated -> {OUT.name}")
    print(f"  {len(tags)} of {len(known)} works tagged ({with_el} with explicit elements)")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
