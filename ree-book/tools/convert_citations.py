"""Convert the inherited org-mode citations in `src/` to MyST citations.

The chapters arrive carrying two org styles -- org-ref (`cite:key`,
`citep:key1,key2`) and org-cite (`[cite:@key; @key2]`) -- whose keys are the
ones the source documents used, not the ones `references.bib` now uses.  This
rewrites both styles to MyST (`[@key]`, `[@key1; @key2]`) and renames the keys
through `citation-key-map.json` in the same pass, because doing them separately
would leave the book in a state where neither form resolves.

A citation standing in for its authors -- at the start of a sentence and
followed by a verb, as in "cite:augustine2024advancing developed a platform" --
becomes a narrative citation (`@key`) rather than a parenthetical one, so the
sentence still reads as a sentence.  Everything else is parenthetical.

Nothing is guessed: a key missing from the map, or mapping to an entry absent
from the bibliography, is a hard error.

Usage:
    python tools/convert_citations.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

ORG_CITE = re.compile(r"\[cite:((?:\s*@[A-Za-z0-9_-]+\s*;?)+)\]")
ORG_REF = re.compile(r"\bcite[a-z]*:([A-Za-z0-9_][A-Za-z0-9_,-]*)")
# A citation used as the subject of its sentence: sentence-initial, one key,
# followed by a lowercase word.
NARRATIVE = re.compile(
    r"(?:(?<=^)|(?<=\.\s))cite[a-z]*:([A-Za-z0-9_][A-Za-z0-9_-]*)(?=\s+[a-z])", re.M
)


def bib_keys(path: pathlib.Path) -> set[str]:
    return set(re.findall(r"^@\w+\{([^,]+),", path.read_text(), re.M))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--src", default="src")
    ap.add_argument("--map", default="citation-key-map.json")
    ap.add_argument("--bib", default="references.bib")
    args = ap.parse_args()

    key_map = json.loads((ROOT / args.map).read_text())
    known = bib_keys(ROOT / args.bib)
    missing_target = {v for v in key_map.values() if v not in known}
    if missing_target:
        sys.exit(f"key map points at entries not in the bibliography: {sorted(missing_target)}")

    problems: list[str] = []

    def rename(key: str, where: str) -> str:
        if key in key_map:
            return key_map[key]
        if key in known:
            return key
        problems.append(f"{where}: unmapped citation key `{key}`")
        return key

    totals = {"org-cite": 0, "parenthetical": 0, "narrative": 0}
    changed = []

    for path in sorted((ROOT / args.src).glob("*.md")):
        text = original = path.read_text()
        where = path.name

        def do_org_cite(m: re.Match) -> str:
            keys = [rename(k, where) for k in re.findall(r"@([A-Za-z0-9_-]+)", m.group(1))]
            totals["org-cite"] += 1
            return "[" + "; ".join(f"@{k}" for k in keys) + "]"

        def do_narrative(m: re.Match) -> str:
            totals["narrative"] += 1
            return "@" + rename(m.group(1), where)

        def do_parenthetical(m: re.Match) -> str:
            keys = [rename(k, where) for k in m.group(1).split(",") if k]
            if not keys:
                return m.group(0)
            totals["parenthetical"] += 1
            return "[" + "; ".join(f"@{k}" for k in keys) + "]"

        text = ORG_CITE.sub(do_org_cite, text)
        text = NARRATIVE.sub(do_narrative, text)
        text = ORG_REF.sub(do_parenthetical, text)

        if text != original and not args.dry_run:
            path.write_text(text)
        if text != original:
            changed.append(path.name)

    if problems:
        for p in problems:
            print(p, file=sys.stderr)
        sys.exit(f"{len(problems)} unmapped keys; nothing is guessed at, so stopping")

    verb = "would convert" if args.dry_run else "converted"
    print(
        f"{verb} {totals['org-cite']} org-cite, {totals['parenthetical']} parenthetical "
        f"and {totals['narrative']} narrative citations in {len(changed)} files"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
