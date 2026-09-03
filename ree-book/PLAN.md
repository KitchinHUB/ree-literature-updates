# ree-book: build plan and status

Working notes for building the REE separations book. Written to be picked up
cold — if you are resuming this after a gap, read this file first.

**Where things stand: Phases 0–2 are done and committed. Phase 3 is next.**

| Phase | What | Status |
|---|---|---|
| 0 | Scaffold the MyST project, prove the toolchain | ✅ `6286a05` |
| 1 | Merge, dedupe, and verify the bibliography | ✅ `0edb8aa`, `d9a9221` |
| 2 | Convert all sources to MyST Markdown | ✅ `cc2e1df` |
| 3 | **Restructure into chapters** | ⬜ next |
| 4 | Convert citations to `[@key]` | ⬜ |
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
jupyter-book build --html     # build
jupyter-book start            # live preview
```

Use the venv Python: `/Users/jkitchin/Dropbox/uv/.venv/bin/python`.

**Checking the build:** grep the output for `⛔`, `❌`, `⚠️`, `error`, *and* `warn`.
MyST reports some failures as `⛔️ Unexpected node …` with no word "error" in
them — grepping only for "error" hid a broken glossary for two phases.

---

# Phase 3 — Restructure into chapters (next)

The first phase needing editorial judgment rather than mechanics. Move content
from `converted/` into the `src/` stubs. `converted/MANIFEST.md` maps every
file to its destination.

Five sources map 1:1 and are mostly lift-and-drop: `leaching.md` → Ch. 5,
`clay-ion-exchange.md` → Ch. 6, `coacervates.md` → Ch. 8,
`crystallization.md` → Ch. 10, `thermodynamic-cycle.md` → Ch. 13.

The rest need real work:

### 3a. Split `broad-review.md` (17,610 words, 1,903 lines) across 8 chapters

Its `##` sections map as follows (line numbers as of `cc2e1df`):

| Section | Line | Destination |
|---|---|---|
| 1. Introduction and Background | 9 | Ch. 1 Why separation is hard |
| 2. Conventional Separation Technologies | 25 | Ch. 4 Technology landscape |
| 3. Emerging Separation Technologies | 305 | Ch. 12 Membranes/MOFs — **but §3.9 microfluidics goes to Ch. 9** |
| 4. Electrochemical and Pyrometallurgical | 544 | Ch. 7 (merge with carbochlorination) |
| 5. Recycling and Urban Mining | 672 | Ch. 16 |
| 6. Environmental and Sustainability | 692 | Ch. 17 |
| 7. Industrial Developments | 720 | Ch. 18 |
| 8. Comparison of Technologies | 735 | Ch. 4 Technology landscape |
| 9. Future Directions | 751 | Ch. 19 Research directions |
| 10. Biological Separation Technologies | 779 | Ch. 11 (large — 313 lines) |
| 11. Characterization Methods | 1092 | Ch. 15 |
| 12. Techno-Economic Analysis | 1407 | Ch. 17 |
| 13. Life Cycle Assessment | 1515 | Ch. 17 |
| 14. Computational Approaches | 1612 | Ch. 14 (merge with high-throughput) |
| 15. Conclusions | 1714 | fold into Ch. 19 |
| 16. Microcalorimetry for LLE Thermodynamics | 1723 | Ch. 13 (pairs with the thermodynamic cycle) |

Its `## References` (line 1865) is a hand-written list of 16 links, not a
bibliography — drop it, Phase 4 handles citations.

### 3b. Merge the three microfluidic sources into Ch. 9

`microfluidic-report.md` (3,045 w), `microfluidic-colorimetric.md` (1,311 w),
and `broad-review.md` §3.9. All three repeat the same co-laminar / droplet /
slug taxonomy and the same performance numbers (100–1000× mass transfer,
2–3× faster extraction). Keep each one's distinct contribution:

- report → industrial status, pilot scale, key players, feedstock integration
- colorimetric → colorimetric/fluorescence detection, computer vision
- broad-review §3.9 → fundamentals

⚠️ `Microfluidic_REE_Separation_Report.org` carried its own warning:
*"If there is not a url, the reference may be hallucinated."* Its 53 numeric
citations went through Phase 1 verification, but this chapter deserves a closer
read than the others.

### 3c. Merge the two carbochlorination sources into Ch. 7

`carbochlorination-report.md` (7,418 w) and `carbohalogenation-review.md`
(4,882 w) overlap on fundamentals. Merge and dedupe; keep the Ti/Zr/Al/Mg/Nb-Ta
industrial-precedent material, which is a genuinely distinctive angle. Add
`broad-review.md` §4.

Drop from the report: its manual "Table of Contents" section (MyST generates
one) and the "Prepared by Claude Code" byline (the prologue covers provenance).

### 3d. Split `chemistry-fundamentals.md` into Ch. 2 and Ch. 3

Ch. 2 "From ore to feed solution" = its §1 (line 13–113).
Ch. 3 "Solvent extraction fundamentals" = its §2–6 (line 114–866). This is the
core teaching chapter for new researchers.
Its §7 (high-throughput, line 867) → Ch. 14.

### 3e. Cut project-internal material

- `high-throughput.md`: keep §1–5 (lines 1–256), **drop §6–7** (lines 257–404)
  — "Bakery Square Lab" equipment and staffing plans, CMU/METALLIC
  recommendations. Internal memo, not a book chapter.
- `thermodynamic-cycle.md`: strip the "Success Metrics from Your SOW" section.
- Verify afterward: `grep -riE "bakery square|SOW|staffing" src/` returns nothing.

### 3f. Short pieces

`bastnasite-framework.md` (550 w) is a compact thermodynamic framework, not a
review. Best as a sidebar in Ch. 5 or an aside in Ch. 13 — reader's call.

### 3g. Fill the back matter

Appendix A (provenance): table mapping each chapter to its original file in
`ree-literature-review/`. Appendix B (further reading): the 6 un-synthesized
PDFs in `papers/` and `microfluidic-ree-papers/`, with DOIs.

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
