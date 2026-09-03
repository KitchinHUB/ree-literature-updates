"""Convert the ree-literature-review sources to MyST Markdown (Phase 2).

Output lands in converted/ rather than src/ on purpose. Several chapters are
splits or merges of these files -- the 17k-word markdown review feeds eight
chapters, three documents merge into the microfluidics chapter, two into the
halogenation chapter -- so restructuring is Phase 3's job. This step is purely
mechanical: get every source into one format, losslessly, and stop.

Carbochlorination prose is taken from the generated .docx rather than the
python-docx scripts that built them. The scripts hold the text as string
literals interleaved with document-building calls; the .docx is the same prose
already assembled in reading order.

Usage:
    python tools/convert_sources.py [--review-dir DIR] [--out-dir converted]
"""

from __future__ import annotations

import argparse
import pathlib
import re
import shutil
import subprocess
import sys

# (source path relative to review dir, output stem, note for the manifest)
SOURCES = [
    # Straight 1:1 chapter sources
    ("leaching/ree-ore-leaching-review.org", "leaching",
     "Ch. 5 Hydrometallurgical Leaching"),
    ("clay-ion-exchange/readme.org", "clay-ion-exchange",
     "Ch. 6 Ion-Adsorption Clays"),
    ("coacervate-ree-separations-review.org", "coacervates",
     "Ch. 8 Coacervates"),
    ("molecular-crystallization-separation.org", "crystallization",
     "Ch. 10 Selective Crystallization"),
    ("thermodynamic-cycle-to-kex.org", "thermodynamic-cycle",
     "Ch. 13 Thermodynamics (strip the SOW section in Phase 3)"),
    # Split or merged in Phase 3
    ("ree-chemistry-fundamentals-review.org", "chemistry-fundamentals",
     "Ch. 2 + Ch. 3 (split at section 2)"),
    ("high-throughput-ree-separations-review.org", "high-throughput",
     "Ch. 14, sections 1-5 only; 6-7 are lab planning, drop"),
    ("Microfluidic_REE_Separation_Report.org", "microfluidic-report",
     "Ch. 9 merge source (industrial/pilot framing)"),
    ("colorimetric-microfluidic-separation.org", "microfluidic-colorimetric",
     "Ch. 9 merge source (detection + computer vision)"),
    ("rare_earth_separation_literature_review.md", "broad-review",
     "Ch. 1, 4, 11, 12, 15, 16, 17, 18, 19 (split by section)"),
    # .docx-only sources
    ("carbochlorination/Carbochlorination_Rare_Earth_Processing_Report.docx",
     "carbochlorination-report", "Ch. 7 merge source"),
    ("carbochlorination/Carbohalogenation_Comprehensive_Review.docx",
     "carbohalogenation-review", "Ch. 7 merge source"),
    ("leaching/Bastnasite_Dissolution_to_Acidic_Phosphate_Extraction_Framework.docx",
     "bastnasite-framework", "Ch. 5 sidebar or Ch. 13 (short, 568 words)"),
]

# Pandoc emits explicit anchors when its auto-slug would differ from the
# heading text. MyST generates its own slugs, and the literal attribute renders
# as text, so drop them.
HEADING_ANCHOR = re.compile(r"^(#{1,6} .+?)\s*\{#[^}]*\}\s*$", re.M)
# Org export keywords and org-ref/citar local variables that survive conversion.
ORG_KEYWORD = re.compile(r"^#\+[A-Za-z_]+:.*$", re.M)
LOCAL_VARS = re.compile(
    r"^\s*(#\s*)?Local Variables:.*?^\s*(#\s*)?End:\s*$", re.M | re.S
)
# Pandoc escapes brackets it does not recognise as syntax, so numeric citations
# arrive as "\[1-3\]" and org-cite groups as "[cite:@a; @b\]". Phase 4 has to
# find these, so restore the plain brackets here rather than making every later
# pattern account for backslashes.
ESCAPED_NUM_CITE = re.compile(r"\\\[(\d+(?:\s*[-,]\s*\d+)*)\\?\]")
ESCAPED_CITE_CLOSE = re.compile(r"(\[cite:[^\]]*?)\\\]")
# MyST reads $...$ as inline math, so an unescaped currency figure silently
# swallows everything up to the next dollar sign -- which wrecks the cost
# tables in the leaching and techno-economics chapters. Escape a dollar only
# when it introduces a number or a rate ($1,430, $/ton), leaving genuine math
# delimiters (coacervates.md defines a separation factor in LaTeX) alone.
CURRENCY = re.compile(r"(?<!\\)\$(?=[0-9/])")
# Pandoc leaves an empty citeproc bibliography container behind; Phase 4 adds
# the real bibliography.
EMPTY_REFS_DIV = re.compile(r"^:::+ \{#refs\}\s*\n:::+\s*$", re.M)
# Org directives pandoc cannot map (#+PRINT_BIBLIOGRAPHY: and friends) come
# through as raw ```{=org} blocks. MyST reads "{=org}" as a directive name and
# errors out. They are empty here, and org-only markup would not render in
# MyST anyway, so drop them -- warning if one ever carries content.
RAW_FORMAT_BLOCK = re.compile(r"^```\{=\w+\}\n(.*?)^```\s*$", re.M | re.S)


def have_pandoc() -> str:
    exe = shutil.which("pandoc")
    if not exe:
        sys.exit("pandoc not found on PATH")
    return exe


def convert(src: pathlib.Path, dest: pathlib.Path, media_dir: pathlib.Path) -> None:
    fmt = {".org": "org", ".docx": "docx", ".md": "markdown"}[src.suffix.lower()]
    cmd = [
        "pandoc", "-f", fmt, "-t", "commonmark_x",
        "--wrap=none", "--markdown-headings=atx",
        f"--extract-media={media_dir}",
        str(src), "-o", str(dest),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        sys.exit(f"pandoc failed on {src}:\n{res.stderr}")
    if res.stderr.strip():
        for line in res.stderr.strip().splitlines()[:3]:
            print(f"      pandoc: {line}")


def postprocess(path: pathlib.Path) -> dict:
    text = path.read_text()
    before = len(text)
    text = LOCAL_VARS.sub("", text)
    text = ORG_KEYWORD.sub("", text)
    text = HEADING_ANCHOR.sub(r"\1", text)
    text = ESCAPED_NUM_CITE.sub(r"[\1]", text)
    text = ESCAPED_CITE_CLOSE.sub(r"\1]", text)
    text = EMPTY_REFS_DIV.sub("", text)
    for body in RAW_FORMAT_BLOCK.findall(text):
        if body.strip():
            print(f"      WARNING: dropping non-empty raw block: {body[:60]!r}")
    text = RAW_FORMAT_BLOCK.sub("", text)
    text = CURRENCY.sub(r"\\$", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    path.write_text(text.strip() + "\n")
    return {
        "chars": len(text),
        "removed": before - len(text),
        "headings": len(re.findall(r"^#{1,6} ", text, re.M)),
        "tables": len(re.findall(r"^\|", text, re.M)),
        # org-ref/org-cite citations left as plain text for Phase 4 to convert
        "org_cites": len(re.findall(r"cite:[&@]?[\w:.@-]+", text)),
        "num_cites": len(re.findall(r"\[\d+(?:\s*[-,]\s*\d+)*\]", text)),
        "words": len(text.split()),
        "currency_escaped": len(re.findall(r"\\\$", text)),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--review-dir", default="../../ree-literature-review")
    ap.add_argument("--out-dir", default="converted")
    args = ap.parse_args()

    have_pandoc()
    review = pathlib.Path(args.review_dir).resolve()
    out = pathlib.Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    media = out / "media"

    rows, total_words = [], 0
    for rel, stem, note in SOURCES:
        src = review / rel
        if not src.exists():
            print(f"  MISSING {rel}")
            rows.append((stem, rel, note, None))
            continue
        dest = out / f"{stem}.md"
        print(f"  {rel}")
        convert(src, dest, media)
        stats = postprocess(dest)
        total_words += stats["words"]
        print(f"      -> {dest.name}: {stats['words']:,} words, "
              f"{stats['headings']} headings, {stats['tables']} table rows, "
              f"{stats['org_cites']} org cites, {stats['num_cites']} numeric cites")
        rows.append((stem, rel, note, stats))

    manifest = [
        "# Phase 2 conversion manifest",
        "",
        "Mechanical pandoc conversion of the ree-literature-review sources to",
        "MyST Markdown. Nothing here is restructured yet -- Phase 3 splits and",
        "merges these into `src/`. Citations are still in their original four",
        "styles; Phase 4 converts them to `[@key]`.",
        "",
        f"Total: **{total_words:,} words** across {len(rows)} files.",
        "",
        "| Converted file | Source | Words | Headings | org `cite:` | `[n]` cites | Destination |",
        "|---|---|---|---|---|---|---|",
    ]
    for stem, rel, note, st in rows:
        if st is None:
            manifest.append(f"| — | `{rel}` | MISSING | | | | {note} |")
        else:
            manifest.append(
                f"| `{stem}.md` | `{rel}` | {st['words']:,} | {st['headings']} | "
                f"{st['org_cites']} | {st['num_cites']} | {note} |"
            )
    manifest += [
        "",
        "## Excluded from the book",
        "",
        "- `notes.org` — mostly tungsten alloys, HEAs, crack detection; off-topic.",
        "- `litdb-ree-findings.org` — a database search log, not prose.",
        "- `ideas.org` — brainstorming; the stimuli-responsive nanoparticle idea",
        "  may seed Ch. 19 Research Directions.",
        "- `nnl.bib` — disjoint general materials-science library (see Phase 1).",
        "- `papers/`, `microfluidic-ree-papers/` — PDFs with no written prose;",
        "  they become Appendix B further reading.",
        "",
    ]
    (out / "MANIFEST.md").write_text("\n".join(manifest))
    print(f"\ntotal {total_words:,} words -> {out}/")
    print(f"wrote {out}/MANIFEST.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
