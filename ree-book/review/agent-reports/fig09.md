# Agent fig09 — G29, two figures for ch. 9 (microfluidic separations)

Files created: `tools/figures/fig_kinetics.py`, `tools/figures/fig_flow_regimes.py`,
`figures/09-kinetics.svg`, `figures/09-flow-regimes.svg`, this report.
File edited: `src/09-microfluidic-separations.md` (two figure directives plus two
short prose hooks). Nothing else touched; no new bibliography entries were
needed, so `review/bib-additions/fig09.bib` was not created.

Both figures were proofed visually via `FIG_PROOF=/tmp/figproof` and iterated:
`09-kinetics` through two passes (an annotation leader that crossed a curve, a
two-line panel title that would not align), `09-flow-regimes` through three (the
footer ran off the right edge, the margin note collided with it, drops drew as
ellipses because the axes aspect is not 1, and patch-level `alpha` was washing
out the interface edge colour along with the fill). Final proofs are clean: no
overlap, nothing outside the axes, legible at print width.

## Figure 1 — `09-kinetics.svg`, approach to equilibrium (`fig-09-kinetics`)

Placed in **Process Intensification: The Numbers**, immediately after the
"Basis of each row" paragraph, so it sits under Table 2 whose numbers it uses.
Referred to from **Why Microfluidics Changes the Problem** as well, right after
the Performance Metrics table.

Panel (a) is the first-order model `E/E_eq = 1 - exp(-kLa·t)`. Not data — the
caption and the module docstring both say so, and the bands are the reported
spread in kLa, not experimental scatter.

| number | source |
|---|---|
| kLa 0.19–0.41 s⁻¹, microfluidic | ch. 9 Table 2, cited to `@dessimoz2008liquid` (slug flow, 269–400 µm rectangular glass channels) |
| kLa 10⁻³–10⁻² s⁻¹, conventional | ch. 9 Table 2, uncited order-of-magnitude column; drawn as a band and labelled "order of magnitude, no agitation stated", matching the caveat the chapter's own basis note gives |
| 3–60 s residence-time window | ch. 9 Table 2 and §Adjacent Lanthanide Challenge, cited to `@fernandezmaza2024high` |
| 10–25 min mixer-settler window | ch. 9 Table 2 and the Performance Metrics table |
| 95%-of-equilibrium times, 7–16 s and 5–50 min | computed here from the model as 3/kLa; stated in the caption as a consequence of the curve, not as a measurement |

The point worth keeping: the two kLa ranges independently reproduce the two
contact times the chapter quotes from unrelated sources, which is a consistency
check the reader can do by eye. The chapter's other kinetic figures are
consistent with the same band — "10–15 s" for heavy REE (`@kriel2015microfluidic`),
"equilibrium within 30 s" for pore-throat, 15 s in the Y-Y microchip
(`@kolar2016microfluidic`) — but I did not clutter the axis with them.

Panel (b) is the chapter's kinetic-separation mechanism: two lanthanides with a
shared equilibrium and different rates, so the gap opens before equilibrium and
closes at it. The fast rate is the top of the measured microfluidic range; the
**3× rate ratio is illustrative and is labelled as such in both the caption and
the docstring.** The chapter names Eu³⁺/La³⁺ as a kinetically distinguished pair
but reports no rate ratio for it, so no ratio is claimed. The maximum is
analytic (`t* = ln(k_f/k_s)/(k_f - k_s)` = 4 s), which is why it can be printed.

## Figure 2 — `09-flow-regimes.svg`, the four regimes (`fig-09-flow-regimes`)

Placed in **Flow Regimes and Configurations**, immediately after the four bullet
blocks it draws, and referred to from that section's opening sentence. Schematic,
stated as such in the caption; nothing is to scale.

The four panels are in the chapter's order — co-laminar, slug, micro-droplet,
pore-throat — each labelled with that section's own numbers: phase ratio 5:1 to
1:5 (co-laminar); 86.9–94.8% mass transfer efficiency (slug); 92.9–97.4%
(micro-droplet); phase ratio 50–250:1, 77% at 500:1, equilibrium within 30 s
(pore-throat). The internal-circulation arrow in the slug panel and the
"capillary barriers retain droplets" reading of the pore-throat panel are the
chapter's own descriptions of those regimes.

The interfacial-area argument is made geometrically rather than numerically: the
channel is identical in all four panels and the liquid–liquid interface is drawn
in one colour throughout, so it visibly goes from a single flat plane to slug
caps to the perimeter of every drop — the same order as the reported
efficiencies. I did not put a specific-area number on any panel. The chapter's
only S/V figures (4/d: ~800 cm²/cm³ at 50 µm, ~400 at 100 µm, ~57 at 0.7 mm) are
*wall* surface-to-volume against channel size, not the interfacial area of a
dispersion, and none of the cited sources gives interfacial area per volume for
the droplet or slug regimes. Manufacturing a ladder of areas would have meant
inventing drop sizes and holdups.

**Transition labels — a limitation, not an omission.** The chapter gives only
the envelope (laminar, Re < 2300) and cites `@dessimoz2010quantitative` and
`@kashid2007hydrodynamics` for the regime maps without quoting a capillary
number or a transition velocity. So the figure marks the *direction* of the
first three transitions ("increasing flow rate and shear") and no threshold, and
the caption says explicitly that the chapter quotes none. Pore-throat is set
apart in the margin as a change of channel geometry rather than flow rate; the
first three would otherwise misread as points on a single flow-rate axis, which
would be wrong.

## The 279 conflict — where each key is used

Not fixed (a different work item), and the number 279 appears in neither figure.
Current state of the chapter:

- **`@zhang2019mechanistic`** heads `### Droplet-Based Microfluidic Systems`
  (now line 142: "Droplet microfluidics has emerged as a powerful platform for
  REE separation [@zhang2019mechanistic]:"), and the bullet list underneath it —
  flow-focusing droplet microreactors, Dy/La binary, residence times 3–60 s,
  90% Dy at pH 1, **"Separation factor: 279"** (line 149) — carries no other
  citation, so the whole block reads as attributed to that key.
- **`@fernandezmaza2024high`** carries the same result in three other places:
  line 182 (§The Adjacent Lanthanide Challenge, "90% Dy extraction with
  separation factor of 279 for Dy/La at pH 1 in 3-60 seconds residence time"),
  line 199 (Table 2 extraction-time row, "3-60 s residence time"), line 243
  (§Process Intensification, "279 for Dy/La in a flow-focusing droplet
  reactor"), and line 476 (the conclusions).

So it is not only the separation factor that is double-attributed: the *entire*
flow-focusing Dy/La result, including the 3–60 s residence time, appears under
both keys. That matters for this figure, because my kinetics caption cites
`@fernandezmaza2024high` for the 3–60 s window — following Table 2 and the three
other sites, which are the majority and the ones the ch0609 reviewer worked on.
**If the conflict resolves the other way (the flow-focusing work is actually
`@zhang2019mechanistic`), the citation in the `fig-09-kinetics` caption has to
move with it.** The figure script itself needs no change; only the caption key.

Line numbers above are post-edit, i.e. after my two figure directives were
inserted.

## Not verified

- The primary Dessimoz kLa range. The ch0609 agent could not read the paper
  (Elsevier 403) and noted that secondary summaries give "approximately
  0.2–0.5 s⁻¹" against the chapter's printed 0.19–0.41. I drew the chapter's
  printed numbers. If they are later corrected to 0.2–0.5, the two constants at
  the top of `fig_kinetics.py` are the only edit, and the 95% times in the
  caption (7–16 s) become 6–15 s.
- The conventional 10⁻³–10⁻² s⁻¹ column remains uncited in the chapter. The
  figure draws it as a band and labels it as an order of magnitude with no
  agitation condition, which is the most the source supports.
- The mass transfer efficiencies (86.9–94.8%, 92.9–97.4%) are the chapter's own,
  taken from the `@kolar2016microfluidic`-cited flow-regime section. I did not
  chase them to the primary source, and the chapter does not say what fraction
  they are efficiencies *of* (of equilibrium, presumably) or over what contact
  time — so they are printed as labels beside the panels, not plotted.
