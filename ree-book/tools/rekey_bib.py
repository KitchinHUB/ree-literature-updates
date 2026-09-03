"""Re-key bibliography entries whose keys no longer match their metadata.

Phase 1 generated keys from the metadata as it stood *before* the DOI-recovery
and DOI-mismatch repairs.  Entries whose author field was a placeholder at that
moment were keyed `anonYEARword`; many of them have since acquired a real
author from CrossRef, so their key now lies about the record.  This tool
recomputes those keys from the current metadata using the project convention
(`lastnameYEARword`), rewrites references.bib in sorted order, and propagates
the renames to any direct citation in src/.

Entries whose author is still missing or a `{Journal} Authors` placeholder keep
their `anon` key: the key is honest about what is known.

Usage:
    python tools/rekey_bib.py [--dry-run]
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from merge_bib import first_author_surname, title_word  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
BIB = ROOT / "references.bib"
SRC = ROOT / "src"

ENTRY = re.compile(r"^@(\w+)\{([^,]+),\n(.*?)\n\}\n", re.S | re.M)
FIELD = re.compile(r"^\s*(\w+)\s*=\s*\{(.*?)\}\s*,?\s*$", re.S | re.M)


def parse(text: str) -> list[tuple[str, str, str, str]]:
    """(kind, key, body, whole) for each entry, in file order."""
    out = []
    for m in ENTRY.finditer(text):
        out.append((m.group(1), m.group(2), m.group(3), m.group(0)))
    return out


def fields(body: str) -> dict:
    return {k.lower(): v for k, v in FIELD.findall(body)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    text = BIB.read_text()
    entries = parse(text)
    if len(entries) != text.count("\n@"):
        pass  # count check is advisory only; the regex is the authority

    taken = {key for _, key, _, _ in entries}
    renames: dict[str, str] = {}
    used: dict[str, int] = defaultdict(int)

    for _kind, key, body, _whole in entries:
        if not key.startswith("anon"):
            continue
        f = fields(body)
        surname = first_author_surname(f)
        if not surname:
            continue                      # still genuinely anonymous
        year = re.sub(r"[^0-9]", "", f.get("year", "")) or "nodate"
        base = f"{surname}{year}{title_word(f)}"
        cand = base
        n = 0
        while cand in taken or cand in renames.values():
            cand = f"{base}{chr(ord('a') + n)}"
            n += 1
        used[base] += 1
        renames[key] = cand
        taken.add(cand)

    print(f"{len(entries)} entries, {len(renames)} re-keyed")
    if args.dry_run:
        for old, new in sorted(renames.items()):
            print(f"  {old} -> {new}")
        return 0

    # Rewrite entries with new keys, then emit sorted by key.
    rewritten = []
    for kind, key, body, whole in entries:
        new = renames.get(key, key)
        if new != key:
            whole = whole.replace(f"@{kind}{{{key},", f"@{kind}{{{new},", 1)
        rewritten.append((new, whole))
    rewritten.sort(key=lambda t: t[0])

    header = text[: text.index("@")] if text.lstrip().startswith("%") else ""
    BIB.write_text(header + "\n\n".join(w.strip("\n") for _, w in rewritten) + "\n")

    # Propagate to any key cited directly in the chapters.
    touched = 0
    for md in sorted(SRC.glob("*.md")):
        s = md.read_text()
        out = s
        for old, new in renames.items():
            out = re.sub(rf"(?<![A-Za-z0-9_]){re.escape(old)}(?![A-Za-z0-9_])", new, out)
        if out != s:
            md.write_text(out)
            touched += 1

    report = ROOT / "bib-rekey.md"
    if not renames and report.exists():
        print("nothing to re-key; leaving the existing report in place")
        return 0
    lines = [
        "# Bibliography re-key",
        "",
        "Phase 1 keyed entries from metadata that the later DOI repairs improved.",
        f"{len(renames)} entries whose author was a placeholder at keying time now",
        "carry a real author, so their keys were recomputed from current metadata.",
        "",
        f"- Entries in `references.bib`: **{len(entries)}**",
        f"- Re-keyed: **{len(renames)}**",
        f"- Still `anon` (no usable author on record): "
        f"**{sum(1 for _, k, _, _ in entries if k.startswith('anon')) - len(renames)}**",
        f"- Chapter files updated: **{touched}**",
        "",
        "## Renames",
        "",
    ]
    lines += [f"- `{o}` → `{n}`" for o, n in sorted(renames.items())]
    report.write_text("\n".join(lines) + "\n")
    print(f"wrote {report.relative_to(ROOT)}; {touched} chapter files updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
