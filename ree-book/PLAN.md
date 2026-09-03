# ree-book: build plan and status

Working notes for building the REE separations book. Written to be picked up
cold — if you are resuming this after a gap, read this file first.

**Where things stand: Phases 0–5 are done and committed. Phase 6 is in progress.**

| Phase | What | Status |
|---|---|---|
| 0 | Scaffold the MyST project, prove the toolchain | ✅ `6286a05` |
| 1 | Merge, dedupe, and verify the bibliography | ✅ `0edb8aa`, `d9a9221` |
| 2 | Convert all sources to MyST Markdown | ✅ `cc2e1df` |
| 3 | Restructure into chapters | ✅ |
| 4 | Convert citations to `[@key]` | ✅ `cc2e1df`, `0abdc70`, `821d1a2` |
| 5 | Index and glossary | ✅ `91d098f` |
| 6 | **Final build and verification** | 🔄 in progress |

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

# Phase 4 — Citations ✅

All four inherited citation styles are gone from `src/`. `grep -r 'cite:'`,
a numeric-marker grep, and a hyperlink-citation grep all return nothing. The
book builds 26 pages with **643 cite nodes and no unresolved citation**, and
every key used in the text exists in `references.bib`.

| Style | Where | Done in |
|---|---|---|
| org-ref `cite:key` | leaching, chemistry-fundamentals, coacervates, high-throughput | `cc2e1df` (`tools/convert_citations.py`) |
| org-cite `[cite:@a; @b]` | microfluidic-colorimetric | `cc2e1df` |
| numeric `[1]`, `[1-3]` | ch. 7, ch. 9 | `0abdc70` (`tools/convert_numeric_citations.py`) |
| inline Markdown hyperlinks | ch. 1, 4, 7, 9–17 | `821d1a2` (`tools/convert_link_citations.py`) |

`references.bib` went 406 → **500 entries** across the phase: 27 DOIs recovered
from the numeric reference lists, 19 hand-written grey-literature entries, 21
recovered from hyperlink URLs, and the rest from the org-ref conversions.

## What the audits found

The two hand-written citation styles were both unreliable in the same way, and
neither failure is visible from a build log. **A resolving DOI proves nothing;
only a title cross-check does.** Both converters now hard-fail rather than
write a chapter when a resolved title disagrees with the recorded one.

**Numeric citations** (`numeric-citation-audit.md`) — of 112 markers:

- 9 carried a DOI that resolves cleanly to a *completely unrelated paper*.
  Recovered by CrossRef title search.
- 9 described papers that **do not exist**. Each was re-sourced to work that
  supports the sentence, or the claim was cut. This removed a fabricated
  figure (TiCl₄ production "exceeding 280 million metric tonnes annually") and
  a misidentified company (REEtec → REEgen, a Cornell spinout).
- 22 were grey literature — USGS commodity summaries, agency reports,
  reference works — which get real bib entries rather than being dropped.

**Hyperlink citations** — of 153 links:

- 113 resolved to a DOI and became citations. `tools/link_dois.py` does the
  recovery: DOIs in the path, Nature article ids, RSC codes, Elsevier PIIs via
  the CrossRef `alternative-id` filter, MDPI via ISSN + volume/issue/page,
  Hindawi, Research Square, and PMC/PubMed via NCBI esummary.
- 3 pointed at a real paper on an unrelated subject — the same failure as the
  wrong DOIs above, arriving through a different channel. Corrected in
  `MANUAL_URL` with replacements found by CrossRef search.
- 4 were repository/aggregator URLs (ResearchGate, an institutional
  repository, a publisher platform, SciELO) hosting a real paper with no
  exposed DOI; matched to the published record by title search.
- **36 stay hyperlinks on purpose.** Vendor pages, national-lab reports, news
  articles, software documentation — sources with no DOI because they are not
  papers. Citing them would imply a peer-reviewed record that does not exist.

`feng2025microfluidic` was upgraded from its SSRN preprint DOI to the published
*Sep. Purif. Technol.* record its link pointed at.

## Carried into Phase 6

Both resolved in Phase 6; see below.

- ~~**184 of 500 bib entries are orphans**~~ — 185, now listed in
  `orphan-references.md` rather than pruned blind.
- ~~**`src/92-references.md` renders empty.**~~ — generated by
  `tools/render_bibliography.py`.

---

# Phase 5 — Index and glossary ✅

Done in `91d098f`.

**Glossary: 4 → 51 terms.** The four seed terms (distribution ratio, separation
factor, lixiviant, pH swing) were kept verbatim. Each new term is written for
the sense it carries *in REE separation*, not its general chemistry sense —
"stripping" means recovering the metal from the loaded organic, not gas
stripping. Glossary terms index themselves; no `{index}` role is needed on them.

**Index: 0 → 85 entries, 245 locators.** `tools/tag_index.py` tags a fixed list
of terms (extractants, minerals and feedstocks, unit operations, emerging
techniques, metrics, elements, named deposits and operations) across chapters
01–19. It is idempotent: a second run tags nothing.

What the tagger has to get right, learned by getting it wrong:

- **MyST index entries are case- and number-sensitive.** `{index}`Monazite`` and
  `{index}`monazite`` become two headwords, and so do "mixer-settler" and
  "mixer-settlers". Anything but an exact match against the canonical entry goes
  through the `` {index}`surface <entry>` `` display form, and every term string
  is aligned to its glossary spelling.
- **Never tag inside a quoted span.** An early run put `{index}` roles inside the
  quoted *titles* of the deliberately-fabricated references in the prologue,
  which reads as an endorsement of them. Quoted spans, inline code, math, links,
  existing roles, and citation brackets are all protected; the preface, prologue,
  glossary, index, references, and both appendices are skipped entirely.

# Phase 6 — Final verification 🔄

| Check | Result |
|---|---|
| `npx mystmd build --html` clean against all diagnostic markers | ✅ 26 pages, no `⛔`/`❌`/`⚠️`/error/warning |
| Every `[@key]` in `src/` exists in `references.bib` | ✅ scripted — `render_bibliography.py` hard-fails otherwise |
| Orphan bib entries reported, not pruned | ✅ `orphan-references.md`, 185 entries |
| TOC resolves, index populates, no dead cross-references | ✅ audited in the built AST |
| `grep -riE "bakery square\|SOW\|staffing" src/` | ✅ only the provenance appendix, describing what was excluded |
| `python tools/verify_bib.py` → 0 rejections | ✅ **500 / 500 verified** |

The click-through was done against `_build/site/**/*.json` rather than by eye,
which is both stricter and repeatable: **873 cite nodes, 0 unresolved; 323
cross-reference nodes, 0 dead; 32 TOC entries** (6 parts + 26 pages, none
orphaned); the index page renders 296 locator links; `92-references.md` renders
315 list items where it used to render nothing.

## What Phase 6 fixed

**`src/92-references.md` rendered empty.** MyST puts a reference list at the
foot of each page that cites, so there is no whole-book list to render. Rather
than replace the page with a signpost, `tools/render_bibliography.py` generates
it from `references.bib` and the citations actually present in `src/` — and
records *which chapters cite each work*, so the page doubles as a citation
index. Cited entries only; listing the uncited remainder would misrepresent
what the book rests on. `--check` gates it in CI; `--orphans` writes the
uncited list.

The same run writes `src/references-cited.bib` — the 315 cited entries copied
*verbatim* out of `references.bib`, not re-serialized, so nothing is lost in a
round trip. Both it and the full 500-entry file are declared in the page's
`downloads:` frontmatter and linked inline with `{download}`, so a reader can
pull either straight into Zotero. MyST content-hashes the served filename but
restores the original name on save.

**`verify_bib.py` rejected 12 real sources.** Three separate causes:

- 5 were bot-blocks, not dead links — Britannica ×4, IEA, IAEA answered 403 to
  a script. A server that answers about a specific URL and refuses to serve it
  is evidence the resource exists, which is all the check is asking, so 401,
  403, and 406 now count as alive.
- 6 were hand-guessed publisher landing-page URLs that 404. Real URLs were
  found for the DOE and CSIRO reports; the three books were re-identified by
  ISBN or DOI and their invented URLs deleted. `verify_bib.py` gained a fourth
  verification route through OpenLibrary for entries carrying only an ISBN.
  An ISBN names the *book*, so for a chapter the comparison is against
  `booktitle`, not `title` — otherwise every chapter reports a false mismatch.
- 1 was a transient failure on a 202.

`habashi1997handbook` carried an ISBN with a wrong check digit
(`978-3-527-28792-3`; correct is `…-5`), which is why OpenLibrary could not
find it.

**Five entries had placeholder authors and meaningless keys.** They were
`{ACS Sustainable Chemistry \& Engineering Authors}` and friends — the journal
name where the author list should be, which had then produced keys like
`authors2024extraction`. CrossRef confirmed all five titles (sim 0.99–1.00) and
supplied the real author lists; all five were re-keyed from the real first
author and the citations in `src/` updated. `mining2025advancements` also had
the *wrong journal* recorded — the placeholder said "Mining, Metallurgy &
Exploration", CrossRef says *International Journal of Coal Preparation and
Utilization* — which is exactly how the bad key was generated.

**Encoding cleanup.** 8 journal names carried `&amp;` HTML entities straight
from CrossRef container titles, and 5 author fields used BibTeX accent macros
(`{\"O}nal` rendered as `"Onal` and sorted to the top of the bibliography).
Entities became `\&`, the file's existing convention; accent macros were
decoded to Unicode. The book is UTF-8 MyST throughout and has no use for TeX
escapes.

## Remaining

- Click through the rendered site in a browser for typography and layout — the
  AST audit proves the links resolve, not that the page reads well.
- Decide what to do with the 185 orphans in `orphan-references.md`. Several are
  candidates for the thinner chapters; the rest can go.

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
| `add_refs.py` | Adds a DOI to `references.bib` from CrossRef | same bar as Phase 1 |
| `convert_citations.py` | org-ref/org-cite → `[@key]` | Phase 4 |
| `convert_numeric_citations.py` | numeric markers → `[@key]` | hard-fails on a title mismatch |
| `link_dois.py` | URL → DOI, cached in `.link-dois.json` | 8 publisher URL shapes |
| `convert_link_citations.py` | hyperlink citations → `[@key]` | leaves non-papers as links |
| `tag_index.py` | Adds `{index}` roles across chapters | idempotent; skips quoted spans |
| `render_bibliography.py` | Generates `src/92-references.md` and `src/references-cited.bib` | `--check` to gate, `--orphans` to list |

Audit trail, all committed: `bibliography-audit.md`, `doi-recovery.md`,
`verification-report.md`, `doi-mismatch-repair.md`, `numeric-citation-audit.md`,
`references-rejected.bib`, `orphan-references.md`, `converted/MANIFEST.md`.

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
- **Hand-written reference lists contain papers that do not exist.** Nine of
  the 112 numeric references in ch. 7 and ch. 9 described no real paper, and
  three hyperlink URLs pointed at an unrelated one. Neither shows up in a
  build log. Every converter must cross-check the resolved title against the
  recorded one and refuse to write the chapter when they disagree.
- **A placeholder author field silently poisons the citation key.** Five
  entries carried the *journal name* as the author (`{… Authors}`), which
  `merge_bib.py` turned into keys like `authors2024extraction` and
  `mining2025advancements`. The keys look plausible enough to survive review.
  Grep for `author = {[^}]*Authors}` after any merge.
- **A 403 is not a dead link.** Britannica, the IEA, and the IAEA all refuse
  scripted requests. Treating that as a broken URL nearly deleted six real
  sources.
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
- ~~Two Research Square preprint DOIs~~ — resolved. `rs-5243250` was already
  upgraded to its published record (`he2025stepwise`,
  10.1007/s11356-025-36598-8); `rs-2525701` (`alizadeh2023deep`) still has no
  published version, confirmed by CrossRef `relation` and title search.

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
