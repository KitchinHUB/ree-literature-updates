"""Tag index terms across the chapters with the MyST `{index}` role.

`src/91-index.md` renders `{show-index}`, which collects every `{index}` role
in the book plus every `{glossary}` term. The glossary populates itself; this
adds the terms a reader would look up that are not glossary entries -- named
extractants, ore minerals, individual elements, named technologies -- and adds
chapter locators to the glossary terms that do appear in prose.

Only the **first occurrence in each chapter** is tagged. An index entry
pointing at every mention of "solvent extraction" in a book about solvent
extraction is an index nobody can use; one locator per chapter is what a reader
actually wants.

Tagging is skipped inside anything where a role would be wrong or would not
parse: frontmatter, fenced code, inline code, math, link and citation
brackets, directive options, table rows, and headings. Headings are excluded
because MyST uses heading text to build cross-reference targets.

Where a term is also a glossary entry, the index entry string must match the
glossary term *exactly*. MyST files "mixer-settler" and "mixer-settlers" as two
separate headwords, which splits one concept's locators across two places in
the index.

The script is idempotent -- a term already carrying an `{index}` role in a
chapter counts as tagged -- so it can be re-run after chapters are edited.

Usage:
    python tools/tag_index.py [--dry-run]
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
# The title page, preface and prologue are about how the book was made, not
# about the chemistry. A reader looking up "microfluidics" wants chapter 9,
# not the preface's roadmap sentence.
SKIP_FILES = {"00-title.md", "00-preface.md", "00-prologue.md",
              "90-glossary.md", "91-index.md", "92-references.md",
              "93-appendix-provenance.md", "94-appendix-further-reading.md"}

# (index entry, regex for the surface form in prose).
#
# The entry is what appears in the index; the regex is what is matched in the
# text. Where they differ -- "bastnäsite" written without the umlaut,
# "microfluidic" used adjectivally -- the role is written in its
# `display <entry>` form so the prose is left alone and the index stays
# canonical. Case-insensitive except where the term is an acronym or a trade
# name, where a case-insensitive match would fire on ordinary words.
TERMS: list[tuple[str, str, bool]] = [
    # extractants and solvents
    ("D2EHPA", r"D2EHPA", True),
    ("PC88A", r"PC88A", True),
    ("Cyanex 272", r"Cyanex\s*272", True),
    ("TBP (tributyl phosphate)", r"\bTBP\b", True),
    ("TODGA", r"TODGA", True),
    ("diglycolamide", r"diglycolamides?", False),
    ("HDEHP", r"HDEHP", True),
    ("EHEHPA", r"EHEHPA", True),
    ("Aliquat 336", r"Aliquat\s*336", True),
    ("ionic liquids", r"ionic liquids?", False),
    ("deep eutectic solvent", r"deep eutectic solvents?", False),
    # ore minerals and feedstocks
    ("bastnäsite", r"bastn[äa]site", False),
    ("monazite", r"monazite", False),
    ("xenotime", r"xenotime", False),
    ("ion-adsorption clay", r"ion[- ]adsorption (?:clays?|ores?|deposits?)", False),
    ("coal fly ash", r"coal fly ash", False),
    ("red mud", r"red mud", False),
    ("NdFeB", r"NdFeB", True),
    # unit operations and technologies
    ("solvent extraction", r"solvent extraction", False),
    # Anchored: without \b this matched inside "cation exchange" and
    # "anion exchange", splitting the word and inventing a false locator.
    ("ion exchange", r"\bion[- ]exchange", False),
    ("supported liquid membrane (SLM)", r"supported liquid membranes?", False),
    ("chromatography", r"chromatograph(?:y|ic)", False),
    ("molten salt electrolysis", r"molten[- ]salt electrolysis", False),
    ("carbochlorination", r"carbochlorination", False),
    ("chlorination", r"(?<!carbo)chlorination", False),
    ("flash Joule heating", r"flash Joule heating", False),
    ("bioleaching", r"bioleaching", False),
    ("biosorption", r"biosorption", False),
    ("metal-organic framework (MOF)", r"metal[-–]organic frameworks?", False),
    ("metal-organic framework (MOF)", r"\bMOFs?\b", True),
    ("ion-imprinted polymer", r"ion[- ]imprinted polymers?", False),
    ("polymer inclusion membranes", r"polymer inclusion (?:membranes?|beads?)", False),
    ("microfluidics", r"microfluidics?", False),
    ("isotachophoresis", r"isotachophoresis", False),
    ("selective crystallization", r"(?:selective|fractional) crystalli[sz]ation", False),
    ("precipitation", r"precipitation", False),
    ("mixer-settler", r"mixer[- ]settlers?", False),
    ("countercurrent cascade", r"counter[- ]?current", False),
    ("solvent extraction", r"liquid[-–]liquid extraction", False),
    # biology
    ("lanmodulin", r"lanmodulin", False),
    ("lanthanide binding tags", r"lanthanide[- ]binding tags?", False),
    # concepts
    ("separation factor", r"separation factors?", False),
    ("distribution ratio", r"distribution ratios?", False),
    ("lanthanide contraction", r"lanthanide contraction", False),
    ("life cycle assessment", r"life[- ]cycle assessment", False),
    ("techno-economic analysis (TEA)", r"techno[- ]economic", False),
    # elements
    ("neodymium", r"neodymium", False),
    ("dysprosium", r"dysprosium", False),
    ("praseodymium", r"praseodymium", False),
    ("terbium", r"terbium", False),
    ("scandium", r"scandium", False),
    ("yttrium", r"yttrium", False),
    ("cerium", r"cerium", False),
    ("europium", r"europium", False),
    ("samarium", r"samarium", False),
    ("lanthanum", r"lanthanum", False),
    ("thorium", r"thorium", False),
    # deposits and operations a reader would look up by name
    ("Mountain Pass", r"Mountain Pass", True),
    ("Bayan Obo", r"Bayan Obo", True),
    ("Lynas", r"Lynas", True),
    ("MP Materials", r"MP Materials", True),
    ("Nechalacho", r"Nechalacho", True),
]

# Spans a role must never be inserted into.
PROTECTED = re.compile(
    r"`[^`]*`"                      # inline code
    r"|\$[^$\n]*\$"                 # inline math
    r"|\[[^\]\n]*\]\([^)\n]*\)"     # links
    r"|\[[^\]\n]*@[^\]\n]*\]"       # citations
    r"|\{[a-z-]+\}`[^`]*`"          # existing roles
    r"|<[^>\n]*>"                   # autolinks and raw html
    r"|\"[^\"\n]*\""                 # quoted spans: paper titles, quotations
    r"|\u201c[^\u201d\n]*\u201d"
)


def taggable_spans(line: str):
    """Yield (start, end) of the parts of a line a role may be inserted into."""
    pos = 0
    for m in PROTECTED.finditer(line):
        if m.start() > pos:
            yield pos, m.start()
        pos = m.end()
    if pos < len(line):
        yield pos, len(line)


def skip_line(line: str) -> bool:
    s = line.lstrip()
    return (not s
            or s.startswith("#")            # headings own cross-reference targets
            or s.startswith("|")            # table rows
            or s.startswith(":::")
            or s.startswith("```")
            or s.startswith(":")            # directive options, definition lists
            or s.startswith("("))           # (label)= targets


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    patterns = [(entry, re.compile(rx if cased else rx, 0 if cased else re.I))
                for entry, rx, cased in TERMS]
    total = 0

    for path in sorted(SRC.glob("*.md")):
        if path.name in SKIP_FILES:
            continue
        lines = path.read_text().splitlines(keepends=True)

        # Frontmatter and fenced code are line-ranges, not line properties.
        in_fence = False
        body_start = 0
        if lines and lines[0].strip() == "---":
            for i, ln in enumerate(lines[1:], 1):
                if ln.strip() == "---":
                    body_start = i + 1
                    break

        done: set[str] = set()
        # A term already tagged by an earlier run counts as done.
        text = "".join(lines)
        for entry, _ in patterns:
            if "{index}`" + entry + "`" in text or f"<{entry}>`" in text:
                done.add(entry)

        tagged_here = 0
        for i in range(body_start, len(lines)):
            line = lines[i]
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence or skip_line(line):
                continue

            for entry, rx in patterns:
                if entry in done:
                    continue
                hit = None
                for lo, hi in taggable_spans(line):
                    m = rx.search(line, lo, hi)
                    if m:
                        hit = m
                        break
                if not hit:
                    continue
                surface = hit.group(0)
                # Anything but an exact match -- including a sentence-initial
                # capital -- goes through the `display <entry>` form. MyST
                # treats "Monazite" and "monazite" as separate index entries.
                role = (f"{{index}}`{surface}`" if surface == entry
                        else f"{{index}}`{surface} <{entry}>`")
                line = line[:hit.start()] + role + line[hit.end():]
                lines[i] = line
                done.add(entry)
                tagged_here += 1

        total += tagged_here
        if tagged_here and not args.dry_run:
            path.write_text("".join(lines))
        print(f"  {path.name}: {tagged_here}")

    print(f"tagged {total} index terms")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
