# Agent report: `p30-misc` — P30 (ch. 19 seams + indented-equation conversion)

**Files edited:** `src/19-research-directions.md`, `src/02-ore-to-feed-solution.md`,
`src/04-technology-landscape.md`, `src/10-selective-crystallization.md`,
`src/15-characterization.md`, `src/17-environment-tea-lca.md`, and this file.

**Not touched:** `references.bib`, `myst.yml`, `review/FIXPLAN.md`, and every file
owned by another worker. No new bibliography entries were needed, so
`review/bib-additions/p30-misc.bib` was **not** created. Build not run; nothing
staged or committed. P30 left unchecked in FIXPLAN — it is a multi-agent item and
I covered only my slice.

---

## 1. The ch. 19 seams

**Could the source reviews be named? Yes — but not cited.** They are not published
literature. Both passages descend from the group's own internal literature
reviews: per [](#appendix-a-source-provenance), ch. 19 was assembled from
`broad-review.md` §9 (1233–1259) and §15 (2716–2732) plus `high-throughput.md`
349–357. I checked `converted/broad-review.md` directly: §9.1–9.3 is the horizon
list, verbatim in structure, and it carries **no citation of any kind** for its
timelines. There is no published roadmap behind them and no `[@key]` that could
honestly be attached. So the fix names the document class and points at the
provenance appendix rather than inventing a citation.

**Seam 1 (was `19:18`).** Was: *"the timelines below are the source reviews'
estimates, and review-article timelines are systematically optimistic."*
Now:

> Second, the timelines below are not drawn from any published roadmap. They are
> the judgments of the group's own internal literature reviews, the documents
> this book was assembled from ([](#appendix-a-source-provenance)), and estimates
> made that way run optimistic. Treat them as an ordering, not as dates.

The hedge survives and is strengthened: the reader is now told *whose* estimate
it is, that no published source stands behind it, and where to go to see the
document. "Review-article timelines are systematically optimistic" was itself an
unsourced empirical generalization, so it is now phrased as the book's own
caution about this class of estimate rather than as a finding.

**Seam 2 (was `19:129-130`).** Was: *"The source reviews group the work as
follows. These are the reviews' judgments, retained here for orientation."*
Now:

> The grouping below is taken from the concluding section of the group's broad
> internal review of the field ([](#appendix-a-source-provenance)), which offered
> no citation for it. It is that document's judgment of what should come first,
> retained here for orientation, and it should be read as one group's ordering
> rather than as a schedule anyone has committed to.

Singular, not plural: the horizon list comes from the broad review alone. The
high-throughput review's contribution is the separate "Gaps in Automation and
Computation" section, which already stands on its own without a phantom
reference.

**Other instances of the register in ch. 19:** none. I grepped the whole file for
"source review", "this document", "this report", "the source documents", "the
review". Line 18 and line 129 were the only two. (Live instances remain in chs. 6,
7, 9, 12 and in `00-prologue.md` / `93-appendix-provenance.md` — the last two are
legitimate, since those files are *about* the source documents.)

**One extra fix in ch. 19:** the opportunities table wrote `K_ex` as bare text.
Changed to `$K_\mathrm{ex}$` to match the book convention already used in chs. 3
and 13.

---

## 2. Indented blocks

Nine indented blocks across the six files. Detector now returns clean on all six.

| File | → display math | → fenced | → prose | Notes |
|---|---|---|---|---|
| `02-ore-to-feed-solution.md` | 3 | 0 | 0 | HCl, HNO₃, and clay ion-exchange reactions |
| `04-technology-landscape.md` | 0 | 1 | 0 | ASCII displacement-chromatography band diagram |
| `10-selective-crystallization.md` | 3 | 0 | 0 | oxalate stoichiometry; Ce³⁺/Ce⁴⁺ pair split into two blocks |
| `15-characterization.md` | 2 | 0 | 0 | definitions of $D$ and $\beta$ |
| `17-environment-tea-lca.md` | 0 | 0 | 1 | cradle-to-gate boundary chain |
| `19-research-directions.md` | 0 | 0 | 0 | none present |

Judgment calls worth recording:

- **Ch. 4's band diagram is a picture, not an equation.** Box-drawing characters,
  aligned columns, an annotated arrow. Wrapped in a ` ```text ` fence and the
  common four-space indent stripped so the internal alignment is preserved
  relative to the fence rather than to the paragraph.
- **Ch. 17's boundary chain could not be fenced.** It contains a live MyST role,
  `` {index}`Precipitation <precipitation>` ``. A code fence would print the role
  literally and drop the index entry. It is a one-line process chain, so it was
  de-indented into an ordinary paragraph — the role survives, the arrows read
  fine as prose.
- **Ch. 10's cerium block held two coupled reactions.** Written as two
  consecutive `$$` blocks rather than one `aligned` environment, deliberately: I
  cannot run the build to confirm the environment renders, and two plain display
  blocks are certain to.
- **`E° = 1.74 V` in ch. 10 was left at its source value.** It is high for the
  Ce⁴⁺/Ce³⁺ couple outside perchlorate media (the value is strongly
  medium-dependent), but the number is a content question, not a markup one, and
  is outside P30's scope. Flagging it for whoever owns ch. 10 chemistry.

Notation follows the book's existing convention: `\mathrm{}` for species and
subscript labels, matching `07:80,93` and `13:47`. No mhchem/`\ce{}` — nothing
in the book uses it and it is not configured in `myst.yml`.

---

## 3. Preserved

`(label)=` anchor counts unchanged in all six files. `fig-precipitation-ph` and
both of its cross-references (`10:98`, `10:217`) intact — the caption sits
between the two equation conversions and was not touched. No cross-reference
target was moved or removed.

## 4. Added by coordinator mid-task: the gadolinium boundary (ch. 4 only)

`04:55` "### Separation Groups" presented a three-group split (Gd in the middle)
as an unmarked definition, conflicting with the glossary's two-group convention
(Gd heavy) that ch. 10's precipitation figure now draws.

Fixed on the ch. 4 side only. The section is unsourced in the chapter, so no
citation was invented; it is now framed as what it is — a commercial convention,
not a chemical boundary, and one operators do not draw identically. A paragraph
after the list states plainly that Gd is where the conventions disagree, that
this book uses both, and which is which: three-group industrial split → Gd
middle; two-group light/heavy split (glossary, `fig-precipitation-ph`) → light
runs La–Eu and Gd counts heavy. Neither is declared correct.

**Anchor added:** `(separation-groups)=` immediately above the heading, as
requested, so the glossary's `[](#separation-groups)` no longer depends on an
auto-slug. Heading text also left unchanged, so both routes resolve.

The pointer back to the glossary is written `[](#glossary)` plus the term in
italics, **not** `{term}`heavy rare earth elements (HREE)``. Reason: `{term}` is
currently used nowhere outside `90-glossary.md` itself, so cross-file `{term}`
resolution is unproven in this build and I cannot run the build to check.
`[](#glossary)` is certain. If a later pass confirms cross-file `{term}` works,
that line can be upgraded.

## 5. Left unfixed

- No claim was added anywhere, so no DOI verification was needed and no bib file
  was written.
- P30's other sub-items in my files (Unicode sub/superscripts, cross-chapter
  number reconciliation, duplication) were out of scope for this assignment and
  are untouched.
