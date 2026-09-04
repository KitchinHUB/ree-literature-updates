# Rare Earth Element Separations

An organized introduction to rare earth element separation science, written for
a graduate student or new researcher who knows chemistry and chemical
engineering but has not worked on rare earths. It began as a folder of a dozen
literature reviews written at different times for different purposes; this is
that folder, reorganized so it can be read in order. Twenty-one chapters run
from why the separation is hard at all, through leaching and solvent extraction,
to coacervates, microfluidics, membranes, and the methods used to tell whether
any of it worked.

## Reading it locally

The book is built with [MyST](https://mystmd.org), not Sphinx:

```
cd ree-book
npx -y mystmd start
```

Then open <http://localhost:3000>. Use `npx -y mystmd build --html` for a static
site in `_build/html`.

If a `jupyter-book` binary is already on your PATH, do not use it. That is
Jupyter Book v1, which is Sphinx-based and will fail on this source. Jupyter
Book 2 is mystmd, and `npx -y mystmd` gets it without installing anything
globally.

## The bibliography

Every citation resolves to an entry in `references.bib`, and every entry there
has been checked against an external source — a DOI resolved in CrossRef or
DataCite, a URL fetched live, or an ISBN looked up. Entries that failed are not
deleted silently; they sit in `references-rejected.bib` with the reason, and
`verification-report.md` records each verdict.

This matters because the book was assembled with substantial AI assistance, and
language models fabricate citations. They did here, and the checking caught
them. Be clear about what the check establishes: that a cited paper exists, and
that its authorship, venue, and title match its DOI. It does not establish that
the paper says what this book says it says. No automated check can. Before you
cite anything from here in your own work, read the primary source.
`src/00-prologue.md` sets out the full pipeline and its limits.

## Reporting an error

Open a GitHub issue using the **Book content** template
(`.github/ISSUE_TEMPLATE/book-content.yml` at the repository root). You do not
need to write the replacement text and you do not need repository access. Say
what is wrong, which chapter and section it is in, and what it should say
instead. Issues are worked by Claude and reviewed by a group member before
anything lands, so specificity saves a round trip.

## License

Creative Commons Attribution 4.0 International (CC BY 4.0). The full text is in
`LICENSE`. You may share and adapt this material, including commercially, so
long as you give credit.

John Kitchin, Carnegie Mellon University.
