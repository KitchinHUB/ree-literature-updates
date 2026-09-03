# ree-book: build plan and status

Working notes for building the REE separations book. Written to be picked up
cold — if you are resuming this after a gap, read this file first.

**Where things stand: Phases 0–3 are done and committed. Phase 4 is next.**

| Phase | What | Status |
|---|---|---|
| 0 | Scaffold the MyST project, prove the toolchain | ✅ `6286a05` |
| 1 | Merge, dedupe, and verify the bibliography | ✅ `0edb8aa`, `d9a9221` |
| 2 | Convert all sources to MyST Markdown | ✅ `cc2e1df` |
| 3 | Restructure into chapters | ✅ |
| 4 | **Convert citations to `[@key]`** | ⬜ next |
| 5 | Index and glossary | ⬜ |
| 6 | Final build and verification | ⬜ |

## Decisions already made

Do not relitigate these; they were settled deliberately.

| Question | Decision | Why |
|---|---|---|
| Location | `ree-literature-updates/ree-book/` | user's choice |
| Source format | One-time pandoc conversion; `src/*.md` is canonical | originals in `ree-literature-review/` are now historical |
| Toolchain | Jupyter Book 2 / MyST | already installed; native TOC + index + BibTeX. mdBook was the original idea but needs a Rust build, a third-party plugin for BibTeX, and has no back-of-book index |
| Citations | Verify all; **delete** what cannot be verified | see Phase 1 results |
| Scope | Reorganize existing prose only | no new synthesis chapters |
| Monitor integration | Not for now | the 33 weekly reports stay separate |

## How to work on it

```bash
cd ree-book
npx mystmd build --html       # build
npx mystmd start              # live preview
```

**Use `mystmd`, not `jupyter-book`.** The `jupyter-book` on PATH is v1
(Sphinx-based) and does not understand this project; it fails on `--html`.
`mystmd` is not installed globally, so `npx` fetches it.

Use the venv Python for the `tools/` scripts:
`/Users/jkitchin/Dropbox/uv/.venv/bin/python`.

**Checking the build:** grep the output for `⛔`, `❌`, `⚠️`, `error`, *and* `warn`.
MyST reports some failures as `⛔️ Unexpected node …` with no word "error" in
them — grepping only for "error" hid a broken glossary for two phases.

---

# Phase 3 — Restructure into chapters ✅

All nineteen chapters, both appendices, and the preface are written. The build
is clean: `npx mystmd build --html` produces 26 pages with zero unresolved
cross-references and zero diagnostic markers other than the ten Phase 4
citation warnings listed below.

**Where the content came from is now recorded in the book itself**, in
`src/93-appendix-provenance.md`: a per-chapter table of source files and line
ranges, the material deliberately dropped, and the structural decisions. That
appendix, not this file, is the provenance record. What follows is only what a
future editor needs that does not belong in the book.

## Deviations from the original Phase 3 plan

- `broad-review.md` §2.3 (Precipitation) went to **Ch. 10**, not Ch. 4, and
  Ch. 10 was retitled *Precipitation and Selective Crystallization*. §2.3 is
  400 lines of precipitation chemistry; it belongs next to crystallization,
  not in a landscape overview.
- `bastnasite-framework.md` went to **Ch. 13**, not Ch. 5. It is a
  thermodynamic argument, and it reads as a natural extension of the
  extraction thermodynamic cycle. Ch. 5 carries a pointer.
- The full flash-Joule-heating-with-chlorination treatment is in **Ch. 7**,
  because the chemistry is chlorination. Ch. 12 keeps a pointer plus the
  performance numbers for comparison against the other emerging technologies.
- Per-chapter "Research opportunities" sections **stayed in their chapters**.
  Ch. 19 synthesizes and cross-references them instead of absorbing them —
  judging an opportunity needs the surrounding technical context.
- **Section numbers were stripped from every heading** so MyST owns numbering.
  The sources numbered their own sections and keeping both produced headings
  like "3.2.1" inside chapter 12.
- The one-shot extraction script stayed in the scratchpad rather than going
  into `tools/`. It is not re-runnable against the current `src/`, which is
  hand-edited; re-running it would clobber the editing. Appendix A carries the
  provenance instead.

## Things fixed along the way

- **`convert_sources.py` used the wrong pandoc reader for `.md`.** The broad
  review writes "Key challenges include:" directly above its bullets with no
  blank line, so pandoc's markdown reader treated every such list as lazy
  paragraph continuation and `--wrap=none` joined it onto one line. Fixed with
  `markdown+lists_without_preceding_blankline`. `converted/broad-review.md`
  went from 1,903 to 2,936 lines and 370 table rows started parsing.
  **All line numbers in the pre-Phase-3 version of this plan are stale.**
- **38 pipe tables were collapsed onto single lines** across seven chapters,
  from sources that wrote a table inside a paragraph. Rebuilt into real tables
  by splitting on the `\| \|` row boundaries.
- **`convert_sources.py` only unescaped the closing bracket of an org-cite.**
  `ESCAPED_CITE_OPEN` now handles the opening bracket too.
- Memo voice is gone: `grep -riE "bakery square|SOW|staffing"` returns nothing,
  and the only surviving "your" is a compound adjective.

## Cross-references: use explicit labels

MyST does **not** register an implicit target for a page's H1 when the H1 text
matches the frontmatter `title` — the heading is consumed as the page title and
`[](#chapter-slug)` silently fails with "No target for internal reference".
Every file in `src/` therefore carries an explicit `(slug)=` label above its
H1, and every section that is referenced from another file carries one too.
**Add a label when you add a cross-reference target**; do not rely on implicit
heading IDs, which also break the moment a heading is reworded.

---

# Phase 4 — Citations

Four incompatible styles must all become MyST `[@key]` against the verified
`references.bib` (406 entries).

| Style | Where | Count |
|---|---|---|
| org-ref `cite:key` | leaching, chemistry-fundamentals, coacervates, high-throughput | 83 / 70 / 73 / 23 |
| org-cite `[cite:@a; @b]` | microfluidic-colorimetric | 38 |
| numeric `[1]`, `[1-3]` | carbochlorination-report, carbohalogenation-review, microfluidic-report | 166 / 51 / 49 |
| inline Markdown hyperlinks | broad-review | 172 |

Two hard cases:

- **Numeric citations** need their hand-written reference lists parsed first,
  then each number mapped to a bib key. The lists are at the end of each file.
- **`broad-review.md` cites nothing from any `.bib`** — 172 inline hyperlinks
  and no citation keys, despite a 257-entry bib file having sat next to it.
  Match hyperlinks back to bib entries by DOI/URL. Whatever resolves to
  nothing becomes a verification candidate.

**The keys changed in Phase 1.** Every citation key was regenerated from actual
author/year/title metadata, so `cite:xie2014critical` in a converted file will
*not* match `references.bib` directly. `bibliography-audit.md` records the old
→ new mapping; use it, don't guess.

## What the Phase 3 build already tells you

Auditing `src/` against `references.bib` after Phase 3: **50 `cite:` keys are
used in the text but do not exist in the bibliography.** Only three of those
(`chen2023multiphase`, `huang2006development`, `rydberg2004solvent`) are in
`references-rejected.bib`; the other 47 are Phase 1 re-keying casualties and
should map cleanly via `bibliography-audit.md`. Get the list with:

```bash
grep -rhoE "cite:[a-zA-Z0-9]+" src/*.md | sed 's/cite://' | sort -u > /tmp/used
grep -oE "^@[a-z]+\{[^,]+," references.bib | sed -E 's/^@[a-z]+\{//; s/,$//' | sort -u > /tmp/have
comm -23 /tmp/used /tmp/have
```

The build also reports ten `Could not link citation with label "X"` warnings,
all in `src/09-microfluidic-separations.md`. These are org-cite `[cite:@key]`
spans that MyST already parses as citations — they only need the key remapped,
so they are the easiest ten to do first and a good check that the mapping
works.

Two references were added to `references.bib` during Phase 3 for Appendix B
(`chen2024continuous`, `maurice2021first`), both with DOIs read out of the PDFs
themselves and confirmed against CrossRef. The bibliography now has 408
entries.

**67 citations were deleted** (`references-rejected.bib`). Any claim resting
solely on one of those must be removed or rewritten, not left unsupported.

---

# Phase 5 — Index and glossary

Tag terms with the `{index}` role across chapters: extractants (D2EHPA, PC88A,
TBP, Cyanex, diglycolamide), minerals (bastnasite, monazite, xenotime,
ion-adsorption clay), techniques, and elements. `src/91-index.md` already has
`{show-index}` and works. Extend `src/90-glossary.md` beyond its 4 seed terms.

# Phase 6 — Final verification

1. `jupyter-book build --html` clean against **all** diagnostic markers.
2. Every `[@key]` in `src/` exists in `references.bib`; report orphan bib
   entries. Script this.
3. Click through `jupyter-book start`: TOC resolves, index populates, no dead
   cross-references.
4. `grep -riE "bakery square|SOW|staffing" src/` → nothing.
5. Re-run `python tools/verify_bib.py` — expect 0 rejections.

---

# Tooling

All in `tools/`, all re-runnable. Run from `ree-book/`.

| Script | Does | Note |
|---|---|---|
| `merge_bib.py` | Merges 5 source bibs, dedupes, re-keys | `nnl.bib` excluded on purpose |
| `recover_dois.py` | Fills missing DOIs from CrossRef | `--apply` to write |
| `verify_bib.py` | Verifies every entry; repairs authors | `--apply` to prune |
| `fix_doi_mismatches.py` | Fixes DOIs that resolve to the wrong paper | reads `verification-report.md` |
| `convert_sources.py` | pandoc → MyST for all 13 sources | rewrites `converted/` |

Audit trail, all committed: `bibliography-audit.md`, `doi-recovery.md`,
`verification-report.md`, `doi-mismatch-repair.md`, `references-rejected.bib`,
`converted/MANIFEST.md`.

## Gotchas learned the hard way

- **Grep the build for `⛔` and `⚠️`, not just "error."** A broken glossary
  survived two phases because of this.
- **MyST parses `$` as math.** Currency in cost tables must stay escaped.
  `convert_sources.py` handles it; do not undo the escaping.
- **A resolving DOI is not a correct DOI.** 37 entries had DOIs that resolved
  cleanly to entirely unrelated papers — right journal and year, invented
  article number. Only a title-vs-DOI cross-check catches this.
- **Never adopt a wrong DOI's title.** It looks like a fix and silently swaps
  one reference for another.
- **`verify_bib.py` used to overwrite `references-rejected.bib`.** Fixed to
  append. If you write another tool that touches it, append.
- **`[](#slug)` to a chapter H1 fails silently** unless the file carries an
  explicit `(slug)=` label. MyST consumes an H1 that matches the frontmatter
  `title` as the page title, leaving no heading target. The build says "No
  target for internal reference" — another reason to grep for `⚠️`.
- **`jupyter-book` on PATH is v1 and cannot build this project.** Use
  `npx mystmd`.
- Re-running `convert_sources.py` wipes `converted/` — fine while that is
  staging, but not after Phase 3 edits land in `src/`.

## Open items

- **No figures exist in any source document.** The book will ship text-only
  unless diagrams are commissioned. Worth doing for Ch. 3 (pH swing, contactor
  cascades) and Ch. 5 (flowsheets).
- **Crucible knowledge base** — `clay-ion-exchange/readme.org` cites
  `.crucible/wiki/concepts/*.org`. Not yet surveyed; may hold more material.
- `Microfluidic_REE_Separation_Report.docx` and
  `microfluidic_extraction_presentation.pptx` look redundant with the `.org`
  siblings. Confirm before ignoring.
- Two Research Square preprint DOIs in `references.bib`
  (`10.21203/rs.3.rs-2525701/v1`, `10.21203/rs.3.rs-5243250/v1`) — check
  whether published versions now exist.

---

# Parked: unrelated work in this repo

Not part of the book. Recorded so it is not lost.

### Literature monitor query refinement

Analyzed in depth, **not implemented**. Decisions already made: the relevance
filter should **require an REE term AND a process term**, and the 21 search
topics should be **consolidated**.

Findings from analyzing all 33 reports (952 entries):

- `sort=publication_date:desc` in `scripts/literature_monitor.py` overrides
  OpenAlex relevance ranking, so each query returns the 15 most *recent*
  matches in an already-narrow window rather than the 15 best. Biggest lever.
- `search=` also searches fulltext; `title_and_abstract.search` would tighten it.
- Bare two-letter element symbols in `RELEVANCE_TERMS` match foreign-language
  stopwords. `" la "` alone admitted 22 papers, including French ecology and
  literary-criticism articles.
- **45.1%** of all entries land in category "Other". Including the abstract in
  categorization would rescue ~42% of them; rule order is also backwards, so
  99 separation papers are filed elsewhere.
- `config.yaml` is **never read** by the script despite the README instructing
  you to edit it to change topics.

### Three backfilled weekly reports

`reports/2026-05-18`, `2026-07-20`, `2026-08-31` are generated but
**uncommitted and unverified** — 05-18 and 07-20 ran under code where a failed
topic silently returned empty, so they may be incomplete. Regenerate and
compare before committing.

Still missing entirely: `2026-07-27`, `2026-08-03`, `2026-08-10`.

⚠️ OpenAlex meters **1000 credits/day, 10 per query**; a full 21-topic run
costs 210. Five reports will not fit in one day. `weekly_update.sh` also runs
the monitor twice (the `--slack` call re-queries everything), doubling weekly
usage — worth fixing.
