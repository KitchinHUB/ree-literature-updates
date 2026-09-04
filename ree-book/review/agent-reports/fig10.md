# fig10 — G29(g): precipitation pH across the series, ch. 10

Files touched: `tools/figures/fig_precipitation.py` (new),
`src/10-selective-crystallization.md`. `figures/10-precipitation-ph.svg` is the
generated output. No bib additions were needed, so
`review/bib-additions/fig10.bib` was not created. `references.bib`,
`style.py`, `PLAN.md` and `FIXPLAN.md` untouched. Not built, not committed.

## What is drawn

One panel, x = La…Lu with Y, y = pH at which the hydroxide precipitates.

- **Two group bands, flat**: light REE 6.8–7.5 across La–Eu (blue), heavy REE
  7.0–8.0 across Gd–Lu (orange). Flat, not curved, because the chapter gives
  group ranges and no per-element numbers. This is the honest answer to "be
  honest about which elements you actually have values for": there is not one
  element for which a precipitation pH is reported, so no element carries a
  point, and no curve is drawn through the two groups.
- **Y** as a single capped bar at 6.5–7.5, in ink, placed between Ho and Er.
- **Cerium as a discontinuity**: an accent-coloured box at pH 3–5 under Ce with
  an arrow down from the light-REE band. Roughly a three pH unit drop, against
  the 0.35 units that separate the two group midpoints. This is the chapter's
  thesis (oxidation state is a threshold, radius is a gradient) and it is the
  only thing in the figure that is not a band.
- **Inset**: the three ranges laid on the shared pH axis, with 7.0–7.5 shaded
  because all three contain it, and a hatched ±0.2 pH control bar for scale.
  Same rhetorical move as `fig_logd_vs_ph.py`'s inset: the gap the industry
  would need is smaller than the resolution it has.
- Dashed line at pH 9.5 with the chapter's statement that above it every REE
  hydroxide is similarly insoluble — the top bound of the usable window.

## Where every number comes from

All from `src/10-selective-crystallization.md`, no external source:

| Number | Source in the chapter |
|---|---|
| light REE 6.8–7.5, heavy REE 7.0–8.0, Y 6.5–7.5 | "Industrial pH Thresholds" table |
| Fe 2.5–3.5, Th 3.5–4.5, Al 4.0–5.0, U 4.0–5.5 (quoted in the annotation as "2.5–5.5") | same table |
| Ce(IV) at pH 3–5, 80–95 % Ce removal, other REE losses < 5 % | "Performance Data (H₂O₂ Method)" table |
| E° = 1.74 V for Ce³⁺/Ce⁴⁺ | the cerium half-reaction block |
| ±0.2 pH control precision | "Key Process Considerations" |
| pH 9.5 ceiling | "Solubility Trends" bullet |
| Cerium taken after Fe/Al/Th/U | "Typical Industrial Precipitation Sequence" table, stages 1–4 |

Two things in the figure are *not* from ch. 10 and are marked as such:

- **The La–Eu / Gd–Lu boundary** is the book's own convention, from
  `src/90-glossary.md` ("This book puts Gd with the heavies throughout"). Ch. 10
  says only "Light REEs" and "Heavy REEs". Note that `src/04-technology-
  landscape.md` uses a *three*-group split (La–Nd / Sm–Gd / Tb–Lu+Y), which is a
  pre-existing inconsistency in the book, not something this figure introduces;
  I followed the glossary because the glossary declares itself normative.
- **Y between Ho and Er** is by six-coordinate ionic radius, Y³⁺ 0.900 Å against
  Ho³⁺ 0.901 and Er³⁺ 0.890, from `@shannon1976revised`, already in
  `references.bib` and already cited in ch. 1 for the contraction. The chapter
  itself only says Y "behaves as HREE". The caption states this.

## Computed versus qualitative

- **Nothing is a computed solubility curve, and no Ksp is used.** The chapter
  supplies no solubility products for the series; the only solubility numbers it
  gives are saturation indices for *lanthanum alone* (La-oxalate 5.76/5.48 and
  La-hydroxide −3.81/−1.99 at pH 7 and 8). Following the brief, I did not go
  find a Ksp set and present it as quantitative. The figure plots precipitation
  pH, which the chapter does tabulate, and says so on the panel and in the
  caption.
- **The only arithmetic** is 7.15 and 7.5 as the two band midpoints, their
  difference 0.35, and 0.35/14 ≈ 0.03 pH per neighbour. The 0.03 is labelled on
  the panel as "implied and never measured" — it is an inference from the group
  ranges, not a reported quantity, and the panel says so rather than drawing a
  sloped line that would make it look measured.
- **The band edges are hard** because the chapter's ranges are hard; in reality
  they are soft and concentration-dependent. The figure does not claim
  otherwise but does not annotate this either.

## What I could not verify or chose not to draw

- **Oxalate and double sulfate.** The brief allowed following the salt the
  chapter uses. The chapter gives a *direction* for both (LREEs less soluble,
  precipitate first) and no per-element or even per-group numbers, so there was
  nothing to place on a pH or solubility axis. Drawing a second qualitative
  series for them would have been decoration. They are left out of the figure
  entirely rather than sketched.
- **Eu(II).** The glossary names Eu(II) alongside Ce(IV) as an accessible
  non-trivalent state, and ch. 7 discusses EuCl₂/YbCl₂ under reducing
  conditions, but ch. 10 covers no europium reduction-precipitation route and
  gives no numbers for one. Only the cerium discontinuity is drawn. If a later
  pass adds a europium redux section to ch. 10, a second discontinuity at Eu
  would be the natural extension.
- **The "over 99 % REE precipitation at pH 6.5" claim** in the chapter's
  hydroxide section sits below the 6.8–7.5 band from its own table. I did not
  reconcile the two and did not draw the 6.5 figure; worth an editorial look.
- The two source URLs behind the hydroxide section (OLI Systems, OSTI) are bare
  links in the chapter, not `references.bib` entries. Every number I used from
  that section is printed in the chapter's own tables, so nothing in the figure
  depends on fetching them.

## Proofing

Rendered with `FIG_PROOF=/tmp/figproof python3 tools/figures/fig_precipitation.py`
and inspected as a PNG over four passes. Fixed on the way: the group-shift
annotation colliding with the pH 9.5 label; the cerium annotation running under
the inset; the "±0.2 pH control" label reading as if it belonged to the yttrium
bar; the "heavy REE" label crowding the Y bar. Final state has no overlap and
nothing outside the axes.
