# fig03 — figures for ch. 3 (FIXPLAN G29 b, c)

## What was done

**Task A — `figures/03-logd-vs-ph.svg` wired in.** The script
`tools/figures/fig_logd_vs_ph.py` was not touched. The figure is placed in
*Selectivity Between REEs*, immediately after the derivation of
`β = 10^(3 × Δ pH₁/₂)`, because that is the one place where the +3 slope and the
meaning of β = 1.5 meet. Two prose repairs around it:

- The paragraph that introduces the figure now runs the chapter's own
  arithmetic at the value the chapter actually uses:
  `Δ pH₁/₂ = (log 1.5)/3 = 0.06` pH units. The chapter previously stopped at
  "a gap of 0.1 is β = 2; 0.2 is β = 4" and never evaluated it at 1.5, which is
  the number the figure is drawn for.
- A forward reference was added in *pH Dependence (The "pH Swing")*, after the
  slope-3 table, so the +3 slope section points at the drawing: the two lines
  are parallel, which is where the steepness stops being an unmixed blessing.
- One word changed for disambiguation: "which is the figure
  [](#why-rare-earths-are-hard-to-separate) uses" → "which is the **value** …",
  since there is now a real figure directly above that sentence.

The caption states that the lines are the mass-action expression evaluated, not
fitted data, that the constants only place `D = 1` in the middle of the panel,
that the slope triangle is to scale, and that the inset is at true scale rather
than exaggerated.

**Task B — `tools/figures/fig_cascade.py` → `figures/03-cascade.svg`, new.**
Two stacked panels sharing one horizontal extent so the stage axis of the lower
panel lies under the cascade of the upper one.

- *Upper (schematic):* extraction section, scrub section, feed entering at the
  boundary, strip section, the raffinate and product streams at the two ends,
  and the scrub liquor drawn as a split of the cascade's own strip product
  (labelled "the reflux"). Two curved arrows carry the sections' jobs: the
  more-extractable element pulled into the organic in the extraction section,
  the co-extracted less-extractable element displaced back off the extractant
  and returned toward the feed in the scrub section. That return is why the
  scrub section exists and why a cascade can be pure at both ends.
- *Lower (profile):* the chapter's Fenske bound drawn rather than evaluated.
  At total reflux each stage multiplies the heavy:light ratio by β, so on a
  logit (log-ratio) axis the profile is a straight line of slope log β and the
  stage count is read off as a length. Both of the chapter's cases are drawn:
  β = 1.5 → 45 stages, β = 3.0 → 17.

The ASCII drawing was deleted and the sentence introducing it re-pointed at the
figure. A sentence was added at the end of the Fenske section pointing at the
lower panel, since that is where its numbers come from.

## Where every number comes from

| Number | Source |
|---|---|
| slope +3, `log D = log Kₑₓ + 3 log[(HL)₂] + 3 pH` | ch. 3, *pH Dependence* and *Selectivity Between REEs*; already cited to `@tanaka2021revaluating`, `@li2020hydration`, `@iloeje2019gibbs` |
| β = 1.5 for an adjacent pair | ch. 3 opening and *Typical separation windows* |
| Δ pH₁/₂ = (log 1.5)/3 = 0.06 | computed in the script from the two lines above |
| x_P = 0.9999, x_R = 0.0001 | ch. 3, *How Many Stages for Separation? A Fenske Bound* |
| N_min = 45 (β = 1.5), 17 (β = 3.0) | Fenske evaluated in the script: 45.43 and 16.77, matching the chapter's 45 and 17 |
| feed at stage 24 | computed, not asserted: `1 + ln((1−x_R)/x_R)/ln β` = 23.7 for an equimolar binary feed, so the profile first crosses 50/50 at stage 24 |
| "two to three times N_min", 90-95% stage efficiency, ten-component feed | ch. 3, same section; kept in the caption/prose, not on the figure |
| La to the raffinate, Pr + Nd to the strip product | ch. 3, *Industrial Example*, Step 4 |
| strip section = strong acid, extractant regenerated | ch. 3, *Stripping Stage* and Step 4 (4 M HCl, 50 °C) |

No new sources were needed, so `review/bib-additions/fig03.bib` was not created.
Nothing on either figure is presented as measured data.

## Things worth flagging

1. **The ASCII art had its flow arrows backwards.** It drew
   `aqueous →→→` / `organic ←←←` while placing the raffinate at the left end and
   the loaded organic at the right. Those cannot both be true: the raffinate is
   the aqueous leaving the cascade, so the aqueous must run right to left, and
   the organic left to right (entering fresh at the raffinate end, leaving
   loaded at the scrub end). The chapter's *prose* is correct and unambiguous
   on this ("between the feed point and the loaded-organic outlet, an aqueous
   stream washes the loaded organic on its way out … returning it toward the
   feed"), so the figure follows the prose and the ASCII directions are gone.
2. **The task brief said the scrub "returns co-extracted light neighbours to the
   organic stream".** That is the wrong direction and I did not draw it: the
   scrub displaces the light neighbour *off* the extractant *into* the aqueous,
   which then flows back through the feed point into the extraction section.
   The chapter says exactly this, and the figure follows the chapter.
3. **The chapter's stated N_min = 45 is a rounding of 45.43.** The drawn profile
   therefore reaches 0.99982 at stage 45 rather than exactly 0.9999 — visible as
   the last marker sitting a hair below the 99.99% rule. Keeping the chapter's
   number seemed better than silently using 46.
4. **The chapter says the feed enters "somewhere in the middle" but never fixes
   the stage.** I derived it (stage 24 of 45) rather than choosing it, and both
   panels use the same value, so the section labels read "stages 1-23" and
   "stages 24-45". This is exact only for an equimolar binary feed at total
   reflux, which the caption says.
5. **Not verified:** whether real fractional-extraction circuits place the feed
   near the middle in practice. Xu Guangxian's theory
   (`@xu1985theory`, cited in the chapter) fixes the feed stage from β, the feed
   composition and the two purity specs; the figure's placement is the
   total-reflux binary result, and is labelled as such rather than as plant
   practice.
6. Both figures were proofed visually at `FIG_PROOF=/tmp/figproof` and iterated
   (six passes on the cascade) until nothing overlapped and no label fell
   outside its axes. `mystmd build` was not run, per the brief; the figure
   directives were copied verbatim from the verified form in ch. 13.
