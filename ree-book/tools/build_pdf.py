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
   the first table-of-contents entry, treating it as the document rather than
   as a chapter of it. That page is the website's title page, whose whole job
   -- title, one-paragraph summary, table of contents -- the book class already
   does with \\maketitle and \\tableofcontents, so in print it is dropped on
   purpose and nothing is spliced back. If the toc order ever changes, check
   this: the page that lands first is the page that silently disappears.

9. Chapters that should not be numbered are. The prologue, preface, glossary,
   index and appendices all take chapter numbers, which pushes every real
   chapter two ahead of the source file it came from. Fixed by setting those
   as `\\chapter*` with their own table-of-contents entries.

Also applied here rather than by MyST: the DRAFT watermark, to match the
website; a numbered bibliography in citation order, with the DOIs hyperlinked;
and `backref` so each bibliography entry says where it was cited.

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
% Tables taller than a page; see paginate_tables().
\usepackage{longtable}
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

% unsrtnat writes \doi{...} for every entry that has one. Left to its own
% fallback that prints as dead text; doi.sty makes it a link, and handles the
% underscores that appear in Springer chapter DOIs.
\usepackage{doi}

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


SUPERSCRIPT_DOT = re.compile(r"\\textsuperscript\{\.\}")


def fix_superscript_plus(text, report):
    r"""Put back the plus sign MyST turns into a period.

    MyST's own unicode-to-LaTeX table maps U+207A SUPERSCRIPT PLUS SIGN to
    `\textsuperscript{.}`, so every ion in the book prints as `La3.` instead
    of `La3+`. It is a straight typo in the table -- the *subscript* plus
    U+208A maps correctly, and the superscript *minus* does too -- but it
    fires 409 times here, on nearly every charged species the book names.

    The substitution happens inside MyST, upstream of the newunicodechar
    fallbacks in the preamble, so those never see the character and cannot
    fix it. It has to be repaired in the emitted TeX.

    Rewriting every `\textsuperscript{.}` is safe because nothing else
    produces one: a superscript period is not a thing this book writes, and
    the source contains no raised-dot character that could become one. The
    count is asserted against the source so that a future MyST release which
    fixes the typo makes this function report zero rather than silently
    corrupting something else.
    """
    text, n = SUPERSCRIPT_DOT.subn(r"\\textsuperscript{+}", text)
    report[0] += n
    return text

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


# A `tabular` cannot break across a page. MyST emits every table as one, so a
# table taller than the text block runs off the bottom of the page and the rest
# of it is simply not printed -- silently, with no LaTeX error. The book has one
# table where that happens badly (the technology comparison in ch. 4, which is
# 23,000 characters of prose in six columns) and three more close enough to the
# limit to be at risk on a reflow. Those are converted to `longtable`, which
# paginates and repeats the header row on each page.
#
# The thresholds are deliberately loose. Short tables are left as they are,
# because a `longtable` is never allowed to float and a small table set inline
# leaves worse page breaks than one LaTeX is free to move.
LONGTABLE_MIN_CHARS = 2500
LONGTABLE_MIN_ROWS = 20


def _balanced(text, start):
    """Index just past the `}` matching the `{` at `start`."""
    depth = 0
    i = start
    while i < len(text):
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError("unbalanced brace")


def _longtable(cols, body, caption, label, ncols):
    r"""Rebuild one tabular body as a longtable.

    The header is whatever sits between `\toprule` and the first `\hline`,
    which is how MyST always writes it; it is repeated on every page after the
    first, under a "continued" line so a reader who turns the page knows what
    they are looking at. The caption goes inside the environment because
    `longtable` is not a float and has nowhere else to put one.
    """
    head, sep, rest = body.partition("\\hline\n")
    if not sep:                       # no header row: nothing to repeat
        head, rest = "", body
    head = head.replace("\\toprule\n", "")
    rest = rest.replace("\\bottomrule\n", "")

    cap = ""
    if caption:
        cap = f"\\caption{{{caption}}}"
        if label:
            cap += f"\\label{{{label}}}"
        cap += "\\\\\n"

    repeat = (f"\\multicolumn{{{ncols}}}{{@{{}}l}}"
              f"{{\\footnotesize\\itshape continued from the previous page}}\\\\\n")

    out = [f"\\begin{{longtable}}{{{cols}}}"]
    if cap:
        out.append(cap.rstrip("\n"))
    out.append("\\toprule")
    if head:
        out.append(head.rstrip("\n"))
        out.append("\\hline")
    out.append("\\endfirsthead")
    out.append(repeat.rstrip("\n"))
    out.append("\\toprule")
    if head:
        out.append(head.rstrip("\n"))
        out.append("\\hline")
    out.append("\\endhead")
    out.append("\\bottomrule")
    out.append("\\endfoot")
    out.append(rest.rstrip("\n"))
    out.append("\\end{longtable}")
    return "\n".join(out) + "\n"


def paginate_tables(text, report):
    r"""Turn the tables that are too tall to fit a page into longtables.

    Two shapes have to be recognised, because MyST writes a captioned table and
    an uncaptioned one differently: a captioned one is wrapped in a `table`
    float carrying `\caption` and `\label`, an uncaptioned one is a bare
    `tabular` between a `\bigskip\noindent` and a `\bigskip`. Both become a
    `longtable`; in the captioned case the caption and label move inside it,
    since a longtable is not a float.
    """
    out = []
    pos = 0
    while True:
        i = text.find("\\begin{tabular}{", pos)
        if i < 0:
            break
        j = text.find("\\end{tabular}", i)
        if j < 0:
            break
        j += len("\\end{tabular}")
        chunk = text[i:j]
        rows = chunk.count("\\\\")
        if len(chunk) < LONGTABLE_MIN_CHARS and rows < LONGTABLE_MIN_ROWS:
            out.append(text[pos:j])
            pos = j
            continue

        colstart = i + len("\\begin{tabular}")
        colend = _balanced(text, colstart)
        cols = text[colstart + 1:colend - 1]
        ncols = cols.count("p{") or cols.count("l") or 1
        body = text[colend:j - len("\\end{tabular}")].lstrip("\n")

        # Absorb the float wrapper, if there is one, and take its caption.
        start, end = i, j
        caption = label = None
        pre = text.rfind("\\begin{table}", pos, i)
        if pre >= 0 and "\\end{table}" not in text[pre:i]:
            start = pre
            header = text[pre:i]
            m = re.search(r"\\caption(?:\[[^\]]*\])?\{", header)
            if m:
                k = m.end() - 1
                caption = header[k + 1:_balanced(header, k) - 1]
            m = re.search(r"\\label\{", header)
            if m:
                k = m.end() - 1
                label = header[k + 1:_balanced(header, k) - 1]
            close = text.find("\\end{table}", j)
            if close >= 0:
                end = close + len("\\end{table}")

        out.append(text[pos:start])
        out.append(_longtable(cols, body, caption, label, ncols))
        report[0] += 1
        pos = end
    out.append(text[pos:])
    return "".join(out)


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


DOI_FIELD = re.compile(r"(doi\s*=\s*\{)([^}]*)(\})", re.I)
URL_FIELD = re.compile(r"[ \t]*url\s*=\s*\{([^}]*)\},?\n", re.I)


def tidy_bib(bib):
    r"""Prepare the bibliography database for print.

    Two changes, both to the copy under _build, not to references.bib.

    Escape the specials in DOI fields. Seven of the book's DOIs are Springer
    chapter DOIs ending in _<n>. A raw underscore reaches \doi as a subscript
    token and the run dies with "Missing $ inserted" -- but only when hyperref
    is loaded with backref, which is how this book loads it. doi.sty accepts
    \_ and \#, so escaping them costs nothing: the printed DOI and the link it
    points at both come out right.

    Then drop url fields that only restate the entry's own DOI. Just over half
    of them do, and unsrtnat prints both, so each of those entries carried the
    same string twice on consecutive lines. Publisher URLs that go somewhere
    else -- a Nature page, a PDF on an agency site -- are kept.
    """
    def escape(m):
        doi = m.group(2).replace(r"\_", "_").replace(r"\#", "#")
        return m.group(1) + doi.replace("_", r"\_").replace("#", r"\#") + m.group(3)

    out, dropped = [], 0
    for entry in re.split(r"\n(?=@)", bib):
        doi = DOI_FIELD.search(entry)
        if doi:
            bare = doi.group(2).replace(r"\_", "_").rstrip("/").lower()
            url = URL_FIELD.search(entry)
            if (url and "doi.org" in url.group(1)
                    and url.group(1).rstrip("/").lower().endswith(bare)):
                entry = entry[:url.start()] + entry[url.end():]
                dropped += 1
        out.append(DOI_FIELD.sub(escape, entry))

    print(f"bibliography: dropped {dropped} url fields that restated the DOI")
    return "\n".join(out)


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

    bib = TEXDIR / "main.bib"
    bib.write_text(tidy_bib(bib.read_text()))

    chapter_files = sorted(TEXDIR.glob(f"{STEM}-src.*.tex"))
    slugs = {slug_of(p) for p in chapter_files}
    runons = set()
    plusfix = [0]
    longtables = [0]
    figures = set()
    if not shutil.which("rsvg-convert"):
        print("warning: rsvg-convert not found; figures may not typeset "
              "(install librsvg)")

    # --- chapter files -------------------------------------------------
    for path in chapter_files:
        slug = slug_of(path)
        text = path.read_text()
        text = split_runon_commands(text, runons)
        text = fix_superscript_plus(text, plusfix)
        text = paginate_tables(text, longtables)
        text = restore_verbatim(text)
        text = protect_bracket_after_newline(text)
        # MyST writes a narrative citation -- "@binnemans2013recycling is the
        # paper that defined the field", rendered on the site as "Binnemans et
        # al. (2013)" -- as a bare \cite, which a numbered style sets as "[524]
        # is the paper that defined the field". \citet keeps the author names
        # in the sentence where the sentence was built around them.
        text = text.replace(r"\cite{", r"\citet{")
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
    # Before the glossary is lifted out: 8 of the charges live in entries.
    text = fix_superscript_plus(text, plusfix)
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

    # A numbered bibliography, ordered by first citation. sort&compress turns
    # the long runs of citations this book carries into [4-9] rather than
    # nine separate numbers.
    for old_pkg, new_pkg in [
            (r"\usepackage{natbib}",
             r"\usepackage[numbers,sort&compress]{natbib}"),
            (r"\bibliographystyle{abbrvnat}", r"\bibliographystyle{unsrtnat}")]:
        assert text.count(old_pkg) == 1, f"missing {old_pkg}"
        text = text.replace(old_pkg, new_pkg)

    # MyST drops the first toc entry (see item 8): that is the title page, and
    # the prologue immediately after it must survive.
    prologue_include = f"\\include{{{STEM}-src.prologue}}\n"
    assert text.count(prologue_include) == 1, (
        "the prologue is not in the TeX export -- has the toc order changed?")

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
    print(f"long tables: {longtables[0]} paginated")

    # A charge reaches the PDF by one of two routes: MyST mangles it to
    # \textsuperscript{.} and the repair above catches it, or MyST passes the
    # character through untouched and the preamble's newunicodechar sets it.
    # Both are correct; what would be silent breakage is a third outcome, so
    # the two are counted and reconciled against the source.
    expected = sum(p.read_text(encoding="utf-8").count("\u207a")
                   for p in sorted((ROOT / "src").glob("*.md")))
    survived = sum(p.read_text(encoding="utf-8").count("\u207a")
                   for p in sorted(TEXDIR.glob("*.tex")))
    print(f"superscript plus: {plusfix[0]} repaired + {survived} passed through "
          f"= {plusfix[0] + survived} (source has {expected})")
    if plusfix[0] + survived < expected:
        print("   WARNING: charges went missing between source and TeX")

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
