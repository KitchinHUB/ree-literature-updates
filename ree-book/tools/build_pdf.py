#!/usr/bin/env python3
r"""Build a single downloadable PDF of the whole book.

`mystmd build --pdf` does not work on this project unaided. It emits TeX that
LaTeX cannot compile, and it emits TeX that compiles into a bad book. This
script runs the MyST TeX export, patches what MyST gets wrong, and drives
LuaLaTeX itself.

What MyST gets wrong, and what is done about it:

1. Glossary entries are not escaped. `\\newglossaryentry{...}{description={...}}`
   is written with the description verbatim, so a `%` in a definition comments
   out the closing brace and the run dies with a runaway argument. `_` and `^`
   in a definition are text-mode math errors for the same reason. Fixed by
   escaping the specials inside each entry.

2. Every heading is too deep. Parts come out as `\\section`, chapters as
   `\\subsection`, and the book class's `\\part` and `\\chapter` go unused -- so
   the book has no chapter breaks, no chapter numbers, and a flat table of
   contents. Fixed by promoting the headings in each file by the amount that
   puts that file's own title on `\\chapter`.

3. Cross-references between chapters become `\\href{/src/<slug>}`, a
   site-relative URL that means nothing in a PDF. Fixed by labelling each
   chapter file with its slug and rewriting those links to `\\hyperref`, so they
   work as internal links in the PDF.

4. Math commands are emitted in text mode. `\\rightarrow` outside math is an
   error; the preamble makes the ones the book actually uses mode-agnostic.

5. Glossary entries are defined but never `\\gls`-referenced, and the glossaries
   package prints only referenced entries -- so the Glossary chapter comes out
   empty. Worse, a term containing a subscript digit breaks `\\csname` outright.
   Fixed by dropping the glossaries package: the entries are lifted out of the
   preamble and set as a plain description list under the Glossary chapter.

6. pdfLaTeX cannot set the book's characters. It uses 68 distinct non-ASCII
   characters, including box-drawing for the ASCII-art diagrams and subscript
   digits in formulae. LuaLaTeX with fontspec sets them, with newunicodechar
   fallbacks for the ones Latin Modern lacks.

7. Figures are rasterized, or not resolved at all. Every figure in the book is
   an SVG; MyST converts it with whatever converter is on the machine, and on a
   machine with none it writes the .svg path into `\\includegraphics`, which
   LaTeX cannot read. Fixed by rendering each SVG to PDF with rsvg-convert.

8. The first page of the book is dropped. MyST's project-wide TeX export omits
   the first table-of-contents entry, which here is the prologue disclosing how
   the book was written -- the one page that must not go missing. Fixed by
   exporting it on its own and splicing it back in.

9. Chapters that should not be numbered are. The prologue, preface, glossary,
   index and appendices all take chapter numbers, which pushes every real
   chapter two ahead of the source file it came from. Fixed by setting those
   as `\\chapter*` with their own table-of-contents entries.

Also applied here rather than by MyST: the DRAFT watermark, to match the
website, and `backref` so each bibliography entry says where it was cited.

The book's own rendered bibliography page (src/92-references.md) is left out of
the PDF. It exists to give the website a citable, linkable index of the 554
sources with the chapters that cite each one; in print, natbib plus backref
does that job, and including both would add some eighty redundant pages.

Usage: python tools/build_pdf.py [--skip-myst]
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXDIR = ROOT / "_build" / "tex"
STEM = "rare-earth-separations"
OUTDIR = ROOT / "exports"

# MyST writes the whole book too deep for the `book` class, and not by a fixed
# amount: a page nested under a part gets its title as \subsection, a
# top-level page gets \section, and the part titles themselves are \section
# too. So the shift is computed per file from the page's own title, which is
# always its first heading and always wants to be \chapter.
LEVELS = ["part", "chapter", "section", "subsection", "subsubsection",
          "paragraph", "subparagraph"]
HEADING_RE = re.compile(
    r"\\(" + "|".join(sorted(LEVELS, key=len, reverse=True)) + r")(\*?\{)")

# Characters Latin Modern does not carry, or that read better as real LaTeX.
UNICODE_FALLBACKS = {
    "\u2080": r"\textsubscript{0}", "\u2081": r"\textsubscript{1}",
    "\u2082": r"\textsubscript{2}", "\u2083": r"\textsubscript{3}",
    "\u2084": r"\textsubscript{4}", "\u2085": r"\textsubscript{5}",
    "\u2086": r"\textsubscript{6}", "\u2087": r"\textsubscript{7}",
    "\u2088": r"\textsubscript{8}", "\u2089": r"\textsubscript{9}",
    "\u2090": r"\textsubscript{a}", "\u2091": r"\textsubscript{e}",
    "\u2093": r"\textsubscript{x}", "\u2098": r"\textsubscript{m}",
    "\u207a": r"\textsuperscript{+}", "\u207b": r"\textsuperscript{-}",
    "\u2070": r"\textsuperscript{0}", "\u00b9": r"\textsuperscript{1}",
    "\u00b2": r"\textsuperscript{2}", "\u00b3": r"\textsuperscript{3}",
    "\u2074": r"\textsuperscript{4}", "\u2075": r"\textsuperscript{5}",
    "\u2076": r"\textsuperscript{6}", "\u2077": r"\textsuperscript{7}",
    "\u2078": r"\textsuperscript{8}", "\u2079": r"\textsuperscript{9}",
    "\u21cc": r"\ensuremath{\rightleftharpoons}",
    "\u2192": r"\ensuremath{\rightarrow}",
    "\u2190": r"\ensuremath{\leftarrow}",
    "\u2193": r"\ensuremath{\downarrow}",
    "\u2191": r"\ensuremath{\uparrow}",
    "\u226b": r"\ensuremath{\gg}", "\u226a": r"\ensuremath{\ll}",
    "\u2273": r"\ensuremath{\gtrsim}", "\u2272": r"\ensuremath{\lesssim}",
    "\u2264": r"\ensuremath{\leq}", "\u2265": r"\ensuremath{\geq}",
    "\u2248": r"\ensuremath{\approx}", "\u2260": r"\ensuremath{\neq}",
    "\u00b1": r"\ensuremath{\pm}", "\u00d7": r"\ensuremath{\times}",
    "\u25bc": r"\ensuremath{\blacktriangledown}",
    "\u2032": r"\ensuremath{'}", "\u2033": r"\ensuremath{''}",
    "\u00b5": r"\textmu{}", "\u03bc": r"\textmu{}",
    "\u03b1": r"\ensuremath{\alpha}", "\u03b2": r"\ensuremath{\beta}",
    "\u03b3": r"\ensuremath{\gamma}", "\u03b4": r"\ensuremath{\delta}",
    "\u03b5": r"\ensuremath{\epsilon}", "\u03b7": r"\ensuremath{\eta}",
    "\u03bb": r"\ensuremath{\lambda}", "\u03bd": r"\ensuremath{\nu}",
    "\u03c1": r"\ensuremath{\rho}", "\u03c3": r"\ensuremath{\sigma}",
    "\u03c4": r"\ensuremath{\tau}", "\u03c6": r"\ensuremath{\phi}",
    "\u03c9": r"\ensuremath{\omega}", "\u0394": r"\ensuremath{\Delta}",
    "\u03a9": r"\ensuremath{\Omega}", "\u03a3": r"\ensuremath{\Sigma}",
    "\u2012": "--", "\u2010": "-",
}

# Math commands MyST emits in text mode. Making them mode-agnostic is cheaper
# and safer than trying to find every site and wrap it.
ENSUREMATH_COMMANDS = [
    "rightarrow", "leftarrow", "leftrightarrow", "uparrow", "downarrow",
    "rightleftharpoons", "to", "gg", "ll", "geq", "leq", "approx", "neq",
    "pm", "times", "cdot", "alpha", "beta", "gamma", "delta", "Delta",
    "lambda", "mu", "sigma", "circ", "infty",
]

PREAMBLE = r"""
%%%%%%%%%%%%%%%%%%%%  patched by tools/build_pdf.py  %%%%%%%%%%%%%%%%%%%%
\usepackage{fontspec}
\usepackage{newunicodechar}
% DejaVu Sans Mono carries the box-drawing characters the ASCII-art process
% diagrams are made of; Latin Modern Mono does not.
\setmonofont{DejaVu Sans Mono}[Scale=MatchLowercase]

% Let math symbols survive being emitted in text mode.
%%ENSUREMATH%%

% Characters the text font does not carry.
%%NEWUNICODECHAR%%

% Long unbroken strings (DOIs, URLs, chemical formulae) must not overflow.
% (url itself is already loaded by MyST's own import block.)
\setlength{\emergencystretch}{3em}
\sloppy

% Match the website: the book is a draft and every page should say so.
\usepackage{draftwatermark}
\SetWatermarkText{DRAFT}
\SetWatermarkScale{1}
\SetWatermarkLightness{0.92}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""


def run(cmd, **kw):
    print("$", " ".join(str(c) for c in cmd))
    return subprocess.run(cmd, **kw)


TEXT_ESCAPES = {
    "\\": r"\textbackslash{}",
    "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
    "_": r"\textunderscore{}",
    "^": r"\textasciicircum{}",
    "~": r"\textasciitilde{}",
}

GLOSSARY_ENTRY = re.compile(
    r"\\newglossaryentry\{[^}]*\}\{name=(.*?),description=\{(.*?)\}\}\n",
    re.DOTALL)


def escape_text(s):
    for ch, rep in TEXT_ESCAPES.items():
        s = s.replace(ch, rep)
    return s


def extract_glossary(text):
    r"""Pull the glossary out of the preamble and hand back a plain list.

    MyST emits each definition as `\newglossaryentry` and writes nothing
    escaped, so a `%` in a definition comments out the closing brace and the
    run dies with a runaway argument. That is only the first problem. The
    entry *key* is the term itself, so keys carry subscript digits and
    slashes that blow up when the glossaries package expands them inside
    `\csname`. And since nothing in the book ever writes `\gls`, glossaries
    would print an empty list anyway without a separate `makeglossaries` pass.

    Three problems, one answer: nothing here needs the package. The entries
    are already in the order the book wants, so they are lifted out and set
    as an ordinary description list in the Glossary chapter.
    """
    entries = [(escape_text(n.strip()), escape_text(d.strip()))
               for n, d in GLOSSARY_ENTRY.findall(text)]
    text = GLOSSARY_ENTRY.sub("", text)
    for line in ["\\usepackage{glossaries}\n", "\\makeglossaries\n",
                 "\\printglossaries\n"]:
        text = text.replace(line, "")
    return text, entries


def render_glossary(entries):
    body = "\n".join(
        f"\\item[{name}] {desc}" for name, desc in entries)
    return ("\n\\begin{description}[style=nextline, leftmargin=0pt,"
            " font=\\normalfont\\bfseries]\n" + body +
            "\n\\end{description}\n")


VERBATIM = re.compile(r"\\begin\{verbatim\}.*?\\end\{verbatim\}", re.DOTALL)


def restore_verbatim(text):
    r"""Put the symbols back in the code blocks MyST rewrote.

    Inside a verbatim block MyST converts some unicode to LaTeX and leaves the
    rest alone -- an arrow in an ASCII-art flow diagram comes out as the
    literal text `\rightarrow{}` while the box-drawing around it survives. In
    verbatim nothing is interpreted, so the command is simply printed. The
    characters go back.
    """
    restore = {}
    for char, latex in UNICODE_FALLBACKS.items():
        m = re.fullmatch(r"\\ensuremath\{\\([a-zA-Z]+)\}", latex)
        if m:
            restore[m.group(1)] = char
    names = sorted(restore, key=len, reverse=True)
    pattern = re.compile(r"\\(" + "|".join(names) + r")(\{\}| )?")

    return VERBATIM.sub(
        lambda block: pattern.sub(
            lambda m: restore[m.group(1)], block.group(0)),
        text)


def split_runon_commands(text, report):
    """Separate a math command MyST ran into the following word.

    MyST converts a unicode symbol to its LaTeX command without a following
    space or brace, so `Pro->Ala` becomes `\\rightarrowAla` -- one undefined
    control sequence rather than an arrow and a word. Splitting is only safe
    when the remainder cannot itself be part of a real command name, so this
    fires only where the text resumes with a capital: it fixes
    `\\rightarrowAla` and `\\DeltaG` and leaves booktabs' `\\toprule` alone.

    A `{}` also goes in where a space follows, since TeX would otherwise eat
    it and set `Aqueous -> Organic` closed up.
    """
    names = sorted(ENSUREMATH_COMMANDS, key=len, reverse=True)
    pattern = re.compile(r"\\(" + "|".join(names) + r")(?=[A-Z]| )")

    def fix(m):
        report.add(m.group(0))
        return "\\" + m.group(1) + "{}"

    return pattern.sub(fix, text)


LENGTH = re.compile(r"^-?[0-9.]+\s*(pt|ex|em|cm|mm|in|bp|sp|baselineskip)\b")


def protect_bracket_after_newline(text):
    r"""Stop a row that begins with `[` from being eaten as `\\`'s optional arg.

    A table row starting with a bracketed name -- the ionic liquid
    `[A336][NO3]`, say -- follows the previous row's `\\`, and LaTeX reads
    `\\[A336]` as a row break with a length argument. A `{}` between them
    settles it. Genuine `\\[2ex]` spacing is left alone.
    """
    def fix(m):
        return m.group(0) if LENGTH.match(m.group(2)) else m.group(1) + "{}["

    return re.sub(r"(\\\\\s*)\[([^]]*)", fix, text)


PART_LINE = re.compile(r"\\part\{(.*?)\}")


def tidy_parts(text):
    r"""Leave the parts unnumbered, named exactly as the book names them.

    The book names its own parts -- "Part I --- Orientation" -- so letting
    LaTeX number them as well gives "II Part I --- Orientation", off by one
    because the front matter counts as a part too. Unnumbering them keeps the
    printed names identical to the website's, with no second numbering to
    disagree with. \\cleardoublepage first, so the manual contents entry
    records the part page rather than the one before it.
    """
    return PART_LINE.sub(
        lambda m: ("\\cleardoublepage\n\\phantomsection\n"
                   "\\addcontentsline{toc}{part}{" + m.group(1) + "}\n"
                   "\\part*{" + m.group(1) + "}"),
        text)


def promote_headings(text, shift=None):
    """Raise every heading so the page title lands on \\chapter."""
    if shift is None:
        first = HEADING_RE.search(text)
        if not first:
            return text
        shift = LEVELS.index(first.group(1)) - LEVELS.index("chapter")
    if shift <= 0:
        return text

    def fix(m):
        level = LEVELS[max(0, LEVELS.index(m.group(1)) - shift)]
        return "\\" + level + m.group(2)

    return HEADING_RE.sub(fix, text)


PROLOGUE_SRC = "src/00-prologue.md"
PROLOGUE_TEX = Path("_build") / "exports" / "index_tex" / "index.tex"


def recover_prologue(root):
    r"""Export the one page the project-wide TeX export silently drops.

    MyST leaves the first entry in the table of contents out of a
    project-wide TeX export -- it is the site's root page, and the exporter
    treats it as the document rather than as a chapter of it. Here that page
    is the prologue, which is the AI-assistance disclosure and the account of
    the fabricated citations that were found and removed. It is the last page
    that may go missing from a distributable copy of this book.

    Exporting it on its own gives a standalone document; its body is lifted
    out and returned as a chapter.
    """
    r = run(["npx", "-y", "mystmd", "build", PROLOGUE_SRC, "--tex"], cwd=root)
    tex = root / PROLOGUE_TEX
    if r.returncode != 0 or not tex.exists():
        sys.exit(f"could not export {PROLOGUE_SRC}")
    body = tex.read_text()
    body = body[body.index("\\begin{document}") + len("\\begin{document}"):]
    body = body[:body.index("\\end{document}")]
    for junk in ["\\maketitle", "\\begin{center}\\logo\\end{center}"]:
        body = body.replace(junk, "")
    return body.strip() + "\n"


# The book numbers its own chapters, and its numbering starts at "Why Rare
# Earths Are Hard to Separate". Everything outside that run is unnumbered, so
# the PDF's chapter numbers agree with the numbers the book uses everywhere
# else.
UNNUMBERED = {
    "prologue", "preface", "glossary", "index",
    "appendix-provenance", "appendix-further-reading",
}

FIRST_CHAPTER = re.compile(r"\\chapter\{(.*?)\}")


def unnumber_chapter(text):
    """Turn a page's own title into an unnumbered chapter, still in the ToC."""
    def fix(m):
        title = m.group(1)
        return ("\\chapter*{" + title + "}\n"
                "\\addcontentsline{toc}{chapter}{" + title + "}\n"
                "\\markboth{" + title + "}{" + title + "}")

    return FIRST_CHAPTER.sub(fix, text, count=1)


def slug_of(path):
    """rare-earth-separations-src.coacervates.tex -> coacervates"""
    return path.name[len(STEM) + len("-src."):-len(".tex")]


INCLUDEGRAPHICS = re.compile(r"(\\includegraphics(?:\[[^\]]*\])?)\{files/([^}]+)\}")


def vectorize_figures(text, converted):
    r"""Point \includegraphics at a PDF rendered from the figure's SVG source.

    Every figure in this book is an SVG. MyST rasterizes those with whatever
    converter happens to be installed, and when it finds none it writes the
    .svg path straight into \includegraphics, which LaTeX cannot read at all
    -- that is what breaks the build on a bare CI runner. Rendering the SVG
    to PDF with rsvg-convert instead depends on one small package, gives the
    same result on every machine, and puts a vector figure in a vector
    document rather than a screen-resolution raster of one.
    """
    def fix(m):
        svg = (TEXDIR / "files" / m.group(2)).with_suffix(".svg")
        if not svg.exists():
            return m.group(0)
        pdf = svg.with_suffix(".pdf")
        if not pdf.exists():
            r = subprocess.run(["rsvg-convert", "-f", "pdf",
                                "-o", str(pdf), str(svg)])
            if r.returncode != 0 or not pdf.exists():
                return m.group(0)
        converted.add(svg.name)
        return f"{m.group(1)}{{files/{pdf.name}}}"

    return INCLUDEGRAPHICS.sub(fix, text)


def report_log(log):
    """Say what the final LaTeX pass was unhappy about, if anything."""
    text = log.read_text(errors="replace")
    pages = re.search(r"Output written on .*?\((\d+) pages", text)
    errors = re.findall(r"^! .*", text, re.M)
    undefined = set(re.findall(r"Citation `([^']+)' on page", text))
    missing = set(re.findall(r"Missing character: There is no (.+?) in font",
                             text))
    print(f"pages: {pages.group(1) if pages else '?'}   "
          f"overfull boxes: {len(re.findall(r'Overfull .hbox', text))}")
    for name, items in [("LaTeX errors", errors),
                        ("undefined citations", sorted(undefined)),
                        ("missing glyphs", sorted(missing))]:
        if items:
            print(f"{name}: {len(items)}")
            for item in items[:10]:
                print("   ", item)


def main():
    if "--skip-myst" not in sys.argv:
        if TEXDIR.exists():
            shutil.rmtree(TEXDIR)
        r = run(["npx", "-y", "mystmd", "build", "--tex"], cwd=ROOT)
        if r.returncode != 0:
            sys.exit("MyST TeX export failed")

    main_tex = TEXDIR / f"{STEM}.tex"
    if not main_tex.exists():
        sys.exit(f"expected {main_tex}")

    (TEXDIR / f"{STEM}-src.prologue.tex").write_text(recover_prologue(ROOT))

    chapter_files = sorted(TEXDIR.glob(f"{STEM}-src.*.tex"))
    slugs = {slug_of(p) for p in chapter_files}
    runons = set()
    figures = set()
    if not shutil.which("rsvg-convert"):
        print("warning: rsvg-convert not found; figures may not typeset "
              "(install librsvg)")

    # --- chapter files -------------------------------------------------
    for path in chapter_files:
        slug = slug_of(path)
        text = path.read_text()
        text = split_runon_commands(text, runons)
        text = restore_verbatim(text)
        text = protect_bracket_after_newline(text)
        text = vectorize_figures(text, figures)
        text = promote_headings(text)
        if slug in UNNUMBERED:
            text = unnumber_chapter(text)
        # Give the chapter a target its cross-references can point at.
        text = f"\\label{{{slug}}}\n" + text
        # /src/<slug> is a website path; in a PDF it has to be an internal jump.
        def to_hyperref(m):
            target = m.group(1)
            return (f"\\hyperref[{target}]{{" if target in slugs
                    else f"\\href{{https://kitchinhub.github.io/"
                         f"ree-literature-updates/src/{target}}}{{")
        text = re.sub(r"\\href\{/src/([a-z0-9-]+)\}\{", to_hyperref, text)
        path.write_text(text)

    # --- main file -----------------------------------------------------
    text = main_tex.read_text()
    text, glossary_entries = extract_glossary(text)
    text = split_runon_commands(text, runons)
    # In the main file the only headings are the book's part titles.
    text = promote_headings(text, shift=LEVELS.index("section"))
    text = tidy_parts(text)

    ensure = "\n".join(
        rf"\let\orig{c}\{c}\renewcommand{{\{c}}}{{\ensuremath{{\orig{c}}}}}"
        for c in ENSUREMATH_COMMANDS)
    nuc = "\n".join(rf"\newunicodechar{{{k}}}{{{v}}}"
                    for k, v in UNICODE_FALLBACKS.items())
    preamble = (PREAMBLE.replace("%%ENSUREMATH%%", ensure)
                        .replace("%%NEWUNICODECHAR%%", nuc))

    # pdfLaTeX-only font machinery, replaced by fontspec.
    for line in [r"\usepackage[T1]{fontenc}",
                 r"\usepackage[utf8]{inputenc}"]:
        text = text.replace(line + "\n", "")

    # Bibliography backreferences, so each entry says where it was cited.
    text = text.replace(r"\usepackage{hyperref}",
                        "\\usepackage[backref=page]{hyperref}")

    prologue_include = f"\\include{{{STEM}-src.prologue}}\n"
    preface_include = f"\\include{{{STEM}-src.preface}}\n"
    assert text.count(preface_include) == 1, "preface include moved"
    text = text.replace(preface_include, prologue_include + "\n" + preface_include)

    anchor = "\\makeindex\n"
    assert text.count(anchor) == 1, "preamble anchor moved"
    text = text.replace(anchor, anchor + preamble)

    # The rendered bibliography page is a website artifact; natbib plus
    # backref does its job in print. See the module docstring.
    text = text.replace(f"\\include{{{STEM}-src.references}}\n", "")

    # natbib sets the bibliography as \chapter*, which leaves it out of the
    # table of contents -- in a 300-page book that is the one entry a reader
    # is most likely to go looking for.
    text = text.replace(
        "\\bibliography{main.bib}",
        "\\cleardoublepage\n"
        "\\addcontentsline{toc}{chapter}{Bibliography}\n"
        "\\bibliography{main.bib}")

    main_tex.write_text(text)

    print(f"figures: {len(figures)} rendered from SVG")

    gloss = TEXDIR / f"{STEM}-src.glossary.tex"
    if gloss.exists() and glossary_entries:
        gloss.write_text(gloss.read_text().rstrip("\n") + "\n"
                         + render_glossary(glossary_entries))
    print(f"glossary: {len(glossary_entries)} entries")

    if runons:
        print("split run-on commands: " + ", ".join(sorted(runons)))

    # --- compile -------------------------------------------------------
    # Compile outside the source tree. This one lives in a Dropbox folder,
    # and a file-sync daemon rewriting .aux files under latexmk makes the
    # build fail at random -- once with a conflicted copy of the .aux left
    # in the directory. A scratch directory is not synced by anything.
    work = Path(tempfile.mkdtemp(prefix="ree-pdf-"))
    shutil.copytree(TEXDIR, work, dirs_exist_ok=True)

    # No -halt-on-error: a book needs several passes, and the first one is
    # expected to be full of unresolved references. Errors are read back out
    # of the log afterwards instead.
    r = run(["latexmk", "-lualatex", "-interaction=nonstopmode",
             f"{STEM}.tex"], cwd=work)
    built = work / f"{STEM}.pdf"
    log = work / f"{STEM}.log"
    if log.exists():
        shutil.copy(log, TEXDIR / f"{STEM}.log")
    if r.returncode != 0 or not built.exists():
        sys.exit(f"LaTeX failed; see {TEXDIR / (STEM + '.log')}")

    report_log(log)

    OUTDIR.mkdir(exist_ok=True)
    shutil.copy(built, OUTDIR / f"{STEM}.pdf")
    shutil.rmtree(work, ignore_errors=True)
    print(f"\nwrote {OUTDIR / (STEM + '.pdf')}")


if __name__ == "__main__":
    main()
