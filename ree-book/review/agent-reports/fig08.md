# fig08 — coacervate phase diagram (FIXPLAN G29d)

**Script:** `tools/figures/fig_coacervate.py`
**Output:** `figures/08-coacervate-phase-diagram.svg`
**Wired into:** `src/08-coacervates.md`, in *Complex Coacervation* right after the
sentence about phase-diagram topology, and referred to again from
*Process Considerations*. Anchor `fig-coacervate-phase-diagram`, referenced as
`[](#fig-coacervate-phase-diagram)` in two places.

## What is drawn

Two panels.

**(a) The phase window.** Salt concentration on the vertical axis, total polymer
concentration on the horizontal, which is the standard framing for complex
coacervation and the one that matches what the chapter says. A two-phase dome
closing at a critical salt concentration; a low-salt strip below the dome
labelled as the kinetically-trapped-precipitate regime; a horizontal tie line
at one operating ionic strength with its two ends marked — dilute supernatant
(blue) and dense coacervate (purple); an arrow along the tie line saying the
metal follows the dense phase; and a vertical green arrow from the coacervate
end straight up and out of the dome, labelled "add salt, heat past the cloud
point, or drop pH → REE released". That vertical arrow is the operating idea:
one variable both forms the coacervate and breaks it.

**(b) The loop.** Four stations — mix polymers into the leach liquor; coacervate
forms and takes the REE; settle and discard the supernatant; strip by leaving
the dome — with a green return leg for the desalted polymer. Two of the arrows
are cross-labelled to the corresponding move in panel (a). Under it, in plain
text, the claim the loop rests on (every stream is water, so it replaces the
kerosene diluent and not the extractant chemistry) and, in muted type, the two
costs the chapter itself names (lower metal loading than an organic extractant,
and polymer recovery).

## Measured versus schematic

**Nothing in this figure is a measurement.** Neither axis carries tick values,
the panel title says "(schematic)", and the caption says so in the first two
sentences. This was the stated risk for this figure and it is handled by
removing every quantitative affordance rather than by a disclaimer alone.

From the chapter / its cited sources (topology only):

- A two-phase region at intermediate ionic strength, bounded above by a
  single-phase region where screening suppresses coacervation and below by a
  very-low-salt regime of kinetically trapped precipitates — this is `08:64`
  verbatim, citing `@sing2020progress`; the salt-driven complex/coacervate
  continuum is `@spruijt2014polyelectrolyte`.
- Tie lines horizontal (the two coexisting phases share an ionic strength) —
  standard for this coordinate choice, implied by "phase-separates into a
  polymer-rich coacervate phase and a polymer-dilute supernatant" (`08:53`).
- Metal partitions into the dense polymer-rich phase — the chapter's
  *Mechanism of Ion Uptake* section (`08:79-87`).
- Salt, temperature past a cloud point, and pH each move the system out of the
  two-phase region — the chapter's *Stimuli-Responsive Coacervates* section
  (`@love2020reversible`, `@favrerguillon2004cloud`, `@kumar2023comprehensive`).
- The four-step loop in panel (b) is the chapter's own list in *Integration with
  Hydrometallurgical Processes* (`08:380-385`), and the advantages/challenges
  text under it is its *Comparison with Organic Solvent Extraction* list.

Drawn for illustration, with no source behind it:

- The shape of the binodal (an asymmetric mean-field dome, dilute branch
  hugging the axis; exponents 0.55 and 0.62 chosen to look right).
- Where the critical point sits, where the precipitate boundary sits, where the
  operating tie line sits on the dome, and how far apart the two coexisting
  compositions are.

## Bibliography

No additions needed. Every source the figure leans on — `sing2020progress`,
`spruijt2014polyelectrolyte`, `love2020reversible`, `favrerguillon2004cloud`,
`kumar2023comprehensive` — is already in `references.bib` and already cited by
this chapter. `review/bib-additions/fig08.bib` was not created.

## Could not verify

- No measured binodal for a *rare-earth-relevant* coacervate or ABS appears
  anywhere in the chapter, so there is no way to check the drawn dome against
  data. This is why the figure is explicitly schematic rather than a redraw of
  a published phase diagram. If a real binodal is wanted later, the natural
  candidate is a PEG–salt ABS tie-line diagram, but that would need a source the
  chapter does not currently cite.
- The chapter never gives a coacervate/supernatant partition coefficient for any
  REE, so the tie line carries a direction ("REE follows the dense phase") and
  no magnitude.
- The chapter does not say *which* stimulus is preferred in practice, so panel
  (a) lists all three the chapter names rather than committing to one.

## Other notes

- Added an explicit `(process-considerations)=` anchor above the
  *Process Considerations* heading in `src/08-coacervates.md` so the caption's
  cross-reference resolves without relying on implicit heading anchors.
- Proofed via `FIG_PROOF=/tmp/figproof`; three layout iterations were needed
  (overlapping top labels in panel (a), overflowing note text in panel (b), and
  a white label box that was punching a hole in the binodal). Final proof is
  clean: nothing overlaps, nothing falls outside the axes.
- Files touched: `tools/figures/fig_coacervate.py` (new),
  `figures/08-coacervate-phase-diagram.svg` (generated), `src/08-coacervates.md`,
  this report. Nothing else. No build, no commit.
