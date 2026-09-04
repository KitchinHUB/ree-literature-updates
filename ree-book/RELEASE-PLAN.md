---
title: "Plan: first draft release"
---

# Plan: first draft release

Written 2026-09-04, on top of commit `8d956d0`. This is the plan to take the
book from "builds cleanly, reads unevenly" to a first draft that can be put in
front of readers under its own name.

The bar for a **first draft release** is deliberately not the bar for a finished
book. It is this:

1. Nothing the book says about itself is false.
2. Every number in the prose is either sourced, or its absence is stated.
3. No chapter reads as converted slides.
4. It is licensed, described, pushed, and reachable at a URL.

Items 1 and 4 are a day's work. Item 2 and item 3 are the same work, and they
are the bulk of what remains.

## Where things stand

Measured at `8d956d0`, not estimated.

- 117,727 words across 28 files in `src/`.
- 619 entries in `references.bib`; 462 cited, 157 uncited; 90 in
  `references-rejected.bib`.
- 9 SVG figures, all used through `{figure}` directives.
- Full `mystmd build --html` is clean: 0 unresolved citations, 0 unresolved
  cross-references, 0 math errors, 0 unlabelled containers.
- No TODO, FIXME, or placeholder markers anywhere in `src/`.
- 52 commits ahead of `origin/main`. Nothing has ever been pushed.

The machinery is ready. The prose is not, in nine chapters out of twenty-one.

## Phase A — the four blockers

These are small, and one of them is the most damaging error the book could
carry, because the book's central claim about itself is that its bibliography
was checked.

### A1. The bibliography count the book states is wrong

`src/93-appendix-provenance.md:167` says:

> It now holds 558 entries, all 558 verified — 510 by resolving a DOI in
> CrossRef, one by resolving a DOI in DataCite, 44 by fetching a live URL, and
> three books by ISBN. Ninety entries sit in `references-rejected.bib`.

`references.bib` holds **619**. The 90 rejected is still correct; every other
number in that sentence is stale. `verification-report.md` is stale for the same
reason — it reports 562 checked.

**Do:** re-run the checker over all 619 entries, regenerate
`verification-report.md` from the actual result, and rewrite that sentence from
the new numbers. Do not hand-patch the count — the breakdown by verification
method has to come from the re-run, or the same thing happens again.

**Do also:** add a line to the provenance appendix saying when the count was
last regenerated, so a future reader can tell staleness from error.

**Never:** `verify_bib.py --apply`. It rewrites `references.bib` through
bibtexparser and destroys the house formatting and ordering. Read-only runs
only.

### A2. `iaea2011radiation` is present but reported removed

`verification-report.md` lists it as rejected and removed.
`references.bib:2979` still has it. It is **uncited**, so no claim in the book
rests on it — this is a bookkeeping inconsistency, not a false statement in the
text.

**Do:** move it to `references-rejected.bib` with the rejection reason, or, if
it turns out to be verifiable after all, keep it and correct the report. Either
way the two files must agree.

### A3. No license, no README, no `license` field

There is no `LICENSE` and no `README.md` in `ree-book/`, and `myst.yml` has no
`license` key. A public book with no license is not usable by the people it is
written for.

**Do:**
- `LICENSE` — CC BY 4.0 for the prose is the conventional choice for a work
  like this. This is the one decision in Phase A that is not mine to make.
- `license:` in `myst.yml` under `project:`, matching.
- `README.md` — what the book is, who it is for, how to build it
  (`npx -y mystmd start`), how to report an error (the issue template already
  exists at `.github/ISSUE_TEMPLATE/book-content.yml`), and how the bibliography
  is verified.

### A4. Nothing is pushed and nothing is deployed

52 commits sit locally. There is no `.github/workflows/` directory at all.

**Do:** add a GitHub Pages deploy workflow for `mystmd build --html`, push the
52 commits, confirm the build passes in CI and the site is reachable. Then add
the published URL to the README and to `myst.yml`.

**Note:** the repo is `KitchinHUB/ree-literature-updates`, and `ree-book/` is a
subdirectory of it. The workflow has to set its working directory accordingly,
and the Pages deploy will publish the book at a path, not at the repo root.

**Care:** the git root is `ree-literature-updates`, and its parent
`nnl-rare-earth` is a separate, near-entirely-untracked repo. Stage only
`ree-book/` paths.

## Phase B — the nine chapters that still read as slides

This is the real work. Eleven chapters have already had it done to them —
ch15, ch16, ch18, ch20, ch21, ch04, ch07, ch09, ch13, ch14, ch19 all sit at
72–100 % prose with almost no scaffolding. Nine have not.

Prose share of body lines, and count of `**Advantages**:` / `**Challenges**:` /
`**Preparation**:`-style scaffolding markers:

| Chapter | Words | Prose | Scaffold |
|---|---|---|---|
| 02 From Ore to Feed Solution | 687 | **39 %** | 11 |
| 10 Selective crystallization | 3,342 | 53 % | 8 |
| 08 Coacervates | 5,229 | 56 % | 0 |
| 03 Solvent extraction fundamentals | 7,287 | **57 %** | **16** |
| 06 Ion-adsorption clays | 2,684 | 60 % | 0 |
| 05 Hydrometallurgical leaching | 9,303 | 64 % | 19 |
| 17 Characterization | 4,387 | 69 % | 13 |
| 11 Biological / biomimetic | 6,743 | 71 % | 15 |
| 12 Membranes, MOFs | 4,428 | 72 % | 3 |

The roughly 219 paragraph-blocks that carry a bare number with no citation are
the *same* defect, clustered in exactly these bullet stacks — ch05 has 44, ch03
has 40, ch07 has 35 (ch13's 26 are mostly legitimate textbook constants like
RT = 2.478 kJ/mol). The representative case is ch05:

```
- Recovery: 60-80% REE
- Grade improvement: 2-5x enrichment
```

Real numbers. No source. That is the thing a hostile reader will find first,
and it is the thing that reads as machine-generated.

### The rule for every chapter in this phase

For each bare number: trace it to a source and cite it, or delete it and say
plainly what is not known. Never leave it standing unsourced, and never invent a
citation that merely resolves — the cited work has to actually contain the
number. This is the same standard the rest of the book was held to and it is not
negotiable for a public release.

### Order, and why

1. **ch02 (687 words, 39 % prose)** — first. It is the third page of Part I, it
   is the shortest chapter in the book by a wide margin, and at 687 words it is
   not a chapter yet, it is an outline. A reader who opens the book and reaches
   page three finds this. Needs to roughly triple in length: the chloride,
   nitrate, and sulfate routes each written as an argument about why a
   downstream circuit wants that anion, not as three bullet lists.
2. **ch03 (7,287 words, 16 scaffold markers)** — second, and the largest single
   job. It calls itself "the core teaching chapter of the book" and it has the
   most scaffolding of any chapter. Sixteen sections to convert. It also has 40
   unsourced-number blocks.
3. **ch05 (9,303 words, 19 markers, 44 unsourced numbers)** — third. Longest of
   the nine and the worst offender on bare numbers.
4. **ch10 and ch17** — fourth. Both are heavily scaffolded (8 and 13 markers)
   and both are essentially catalogues, which is the format that most tempts
   bullet lists. ch17 in particular is eleven analytical techniques in a row.
5. **ch06, ch08, ch11, ch12** — last. ch06 and ch08 have zero scaffold markers,
   so their low prose share is bullets rather than headed blocks; ch11 has 15
   markers but is otherwise in reasonable shape; ch12 has only 3.

### How to do it, per chapter

Work one chapter per commit, so each is reviewable:

1. Read the chapter in full.
2. List every bare number and every scaffolded block.
3. For the numbers: check the existing bibliography first — with 157 uncited
   entries, some of what is needed is already verified and sitting there. Only
   go outside for what is genuinely missing, and verify anything new against
   CrossRef / OpenAlex / OSTI before it goes in.
4. Rewrite the scaffolded sections as prose that makes the argument the bullets
   only gestured at.
5. Delete what cannot be sourced, and say so where the absence matters.
6. Rebuild, check the two layers (log grep, then the JSON walk for unresolved
   cites / crossrefs / math errors / unlabelled containers), commit.

**Note on what is *not* a defect:** ch20 sources through inline markdown links
to SEC 10-Ks, company releases, and USGS rather than through bib keys. That was
a deliberate choice and it is the right one for that material. Do not "fix" it.

## Phase B-bis — the six chapters the survey got wrong

Done 2026-09-04, after Phase B closed. The table above put ch04, ch07, ch09,
ch13, ch14 and ch19 in the "already fine" group on the strength of their overall
prose share. That measure was misleading: a chapter can be 80 % prose and still
carry a self-contained bullet catalogue in the middle of it, and all six did.
The catalogues were the same defect Phase B targeted, and in two cases they were
worse than anything Phase B found, because they were performance tables with no
source at all.

What was removed, and why:

- **ch04** — an ion-exchange catalogue with `**Advantages:**` /
  `**Disadvantages:**` blocks, a resin-type applications table, and an
  ion-imprinted-polymer performance table (`Selectivity coefficient 10-100×`,
  `Adsorption capacity 20-100 mg/g`, `Reusability >10 cycles`,
  `Equilibrium time 30-120 minutes`) with nothing behind any of the four rows.
  Rewritten as prose. The IIP numbers now given are the measured ones from
  @zhao2025ultra — 58.6 mg/g, Tm/La separation factor 161, 95 % of capacity over
  ten cycles, 12.6 mg/g in 1 M HCl — with the chapter's own "a separation factor
  without an element pair is not a number" convention applied to the 161. The
  µPIB section now carries @croft2024online's actual experiment (60 wt% D2EHPA
  in PVC, La/Gd, then Nd and Dy from a magnet digest) instead of a feature list.
  Note this chapter hosts the book's single comparison table and states that
  convention, which made the unsourced table in it the worst instance in the
  book.
- **ch07** — the SC-CVT section's performance bullets and both
  "Carbochlorination Feasibility" tables. The feasibility tables graded all
  fourteen lanthanides `Excellent` / `Good` / `Theoretical` against no source,
  including entries that were not feasibility statements at all. The SC-CVT
  numbers all traced to one closed-access 2002 paper whose full text could not
  be reached through CrossRef, OpenAlex, Europe PMC, OSTI or the publisher; the
  process description stays, attributed, and the section now says in the body
  which numbers were withdrawn and where to check them.
- **ch09** — an unsourced configuration-comparison table (`86-95 %`, `93-97 %`,
  `50-500:1`) that duplicated, less carefully, the sourced intensification table
  earlier in the same chapter; plus the mine-on-a-chip, limitations and
  research-opportunity bullet stacks.
- **ch13** — tutorial-slide residue in the thermodynamic cycle
  (`This term allows you to screen different solvents!`) and a bare
  `**References:**` list of three keys.
- **ch14** — the melt-amidation platform specification and the DFT
  applications list.
- **ch19** — `**Critical Success Factors:**` / `**Risk Factors:**` generic
  bullets, the four ore-specific impact lists, and a `Key Limitations` block
  cited to a ResearchGate link rather than a bibliography entry. The
  uncertainty ranges quoted there (`GWP estimates vary by 5×`,
  `Water footprint estimates vary by 8×`) had no source and are gone; the
  chapter now says why no aggregate range is quoted.

Route worth recording: **OpenAlex returns abstracts for Elsevier papers that
CrossRef, Semantic Scholar and Europe PMC all report as having none.** It is
what made the ch04 rewrite possible, after the other three had failed on all
four keys. It is not universal — it returned nothing for the three older
metallurgy papers in ch07 — but it should be tried before a claim is written off
as unverifiable.

## Phase C — final pass

1. Full clean build; both verification layers green.
2. Read the rendered site in a browser, chapter by chapter. This is PLAN.md's
   own last outstanding item and it has never been done. Figures, tables, math,
   cross-reference targets, the bibliography page, the `.bib` download.
3. ~~Decide what to do with the 157 uncited entries.~~ **Resolved.** The
   rendered bibliography lists only the 538 works actually cited, and
   `src/92-references.md` offers both `references-cited.bib` (538 entries) and
   the full `references.bib` (637) as downloads. Nothing is silently dropped
   and nothing uncited is presented as though it supported the text.
4. Refresh `PLAN.md`. Its "Open items" still claims "No figures exist in any
   source document," which stopped being true when the nine figures were added.
5. Re-read `src/00-preface.md` against the finished book and confirm every claim
   it makes about the book is still true.

## What this is not

This plan does not cover: expanding ch06 or ch12 into full treatments of fields
that are genuinely thin in the literature; the book-reviews section that was
raised and then set aside; or any new chapters. Those are second-draft
questions.

## Sequencing

Phase A is about a day and is independent of everything else — it can be done
first and pushed, which also gets the book a URL to point at while Phase B runs.

Phase B is the schedule driver. Nine chapters, one commit each, with ch03 and
ch05 being much larger than the rest.

Phase C needs Phase B finished.

## Phase C findings — the correctness pass

The correctness pass ran ten automated scans over `src/`. Three of them found a
class of problem that every earlier pass had missed, and they are recorded here
because the same blind spots will recur in any future draft.

### The blockquote-scaffold blind spot

Earlier passes searched for draft scaffolding as `**Bold label:**`. That pattern
misses `> Label:` entirely. A scan for `^> [A-Z][^*]{2,60}:\s*` found 17 more,
all concentrated in ch07, together with 10 chemical equations formatted as
blockquotes rather than as the `$` display math the rest of the book uses.
**Search for a construct, not for one spelling of it.**

### Line wrapping as a proxy for "reviewed"

Rewritten prose in this book is hard-wrapped at about 78 characters. Untouched
first-draft prose is one long line per paragraph. Unwrapped lines *that also
lack a citation* located the genuinely unreviewed regions — ch07's industrial
precedents and most of ch19 — and separated them from chapters that were merely
never re-wrapped. This is the cheapest reliable signal available.

### Vendor marketing presented as fact

The most reputationally dangerous class, and the one an unfriendly reader would
find first. ch19 cited a vendor's own product page for ">99% recovery and >99%
purity", an investor-promotion aggregator for a named public company's CAPEX and
OPEX, and a paywalled consultancy with no published methodology for break-even
economics. ch09 had already handled the *same company* correctly, with an
explicit instruction to treat its figures as claims rather than measurements —
so the book contradicted itself on the identical question. All three ch19
sources are gone.

### The book disagreeing with itself

ch19 asserted that deep eutectic solvents offer "lower toxicity and cost" while
ch11 states that amino-acid-based DESs are up to 10⁵ times *more* toxic than
conventional choline-chloride ones — citing `li2022high`, which is in this
book's own bibliography. A claim can be individually plausible, correctly
formatted, and flatly refuted forty pages away. ch19 now defers to ch11.

Four smaller internal contradictions were found and fixed the same way: an
LnCl₃ boiling point given as 1,500 °C in prose against ≳1,550 °C in the
chapter's own sourced table (twice); an acid-leaching temperature of 150-200 °C
against ch05's sourced 200 °C-and-above; a magnesium carbochlorination window of
500-675 °C against the chapter text's 425-600 °C; and a rare earth conversion
quoted as ">93-97%" and "better than 93 %" where the cited sources give 91-93 %.
ch18 summarized three cited phosphor dissolution figures (89.4, 93.1, 94.6 %) as
"90-95 %"; corrected to 89-95 %. ch09 credited a threefold rate enhancement to
the extractant Cyanex 572 when its own source attributes it to the microfluidic
contactor.

**The general lesson.** Every one of these was internal. None needed a library,
a subscription, or a domain expert — only a check of the book against itself.
Do that check before reaching for external verification, because it is both
cheaper and higher-yield.

### What remains open

- `needs-journal-access.md` lists the ten claims that rest on abstracts rather
  than on the passage containing the number, plus the one deliberate gap
  (ch05 states no overall recovery figure, because no source consulted supports
  one). That file is the standing to-do list; it is the only correctness
  category this project could not close on its own.
- A human still has to read the rendered site. No automated check substitutes
  for it, and it is still the last outstanding item.
- GitHub Pages is not enabled on the repository. Enabling it is a settings
  change only the owner can authorize: Settings → Pages → Source "GitHub
  Actions".
