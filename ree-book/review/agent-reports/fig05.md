# fig05 — one drawn flowsheet for ch. 5 (FIXPLAN G29(i))

## What was drawn

`tools/figures/fig_flowsheet.py` → `figures/05-flowsheet.svg`, wired into
`src/05-hydrometallurgical-leaching.md` as `fig-leaching-flowsheet` and referred
to from three places in the prose (the Processing Overview, the Complete Process
Flowsheets section, and the Energy and Carbon section).

The figure is a six-column grid — beneficiation, cracking, leaching, Th removal
and medium conversion, purification, separation feed — crossed by five lanes
grouped into three feedstock bands:

| Band | Lane | Route |
|---|---|---|
| bastnäsite ore | 1 | Mountain Pass: HCl pre-leach → oxidative roast → HCl leach |
| bastnäsite ore | 2 | Bayan Obo: concentrated H₂SO₄ bake → water leach |
| monazite sand | 3 | Indian: conc. H₂SO₄ digestion → water leach → Th removal |
| monazite sand | 4 | caustic: 60-70 wt% NaOH → water leach → acid dissolution |
| ion-adsorption clay | 5 | ion exchange → P507 concentration |

All five converge on one impurity-removal box and one feed specification.

Colour is used for one thing only: the medium a stream is in — ink for solids
(ore, concentrate, calcine, hydroxide cake), `ACCENT` for a sulfate liquor,
`AQUEOUS` for a chloride one. That makes the chapter's own argument visible:
three of the four mineral routes leach into sulfate and each has to go back
through a solid (precipitate, filter, redissolve in HCl) to reach a chloride
feed; only the Mountain Pass route runs unbroken across the conversion column.

## Where each element came from

Everything is from ch. 5 itself, and every citation attached to it in the new
prose already exists in `references.bib`. **No new bibliography entry was
needed; `review/bib-additions/fig05.bib` was not created.**

- Flotation, ≈60 % REO concentrate, tailings — "Beneficiation Summary" and
  "Mountain Pass (USA) beneficiation" [@kim2025rare; @jordens2013processing].
- Gravity/HIMS/electrostatic, ilmenite and zircon co-products — the Indian
  practice list and the old monazite ASCII flowsheet
  [@gupta2004extractive; @jha2016hydrometallurgical].
- HCl pre-leach of carbonate gangue, oxidative roast in air at ≈600 °C,
  Ce(III)→Ce(IV), cerium concentrate in the residue — "Mountain Pass (USA):
  oxidative roast, then HCl" [@gupta2004extractive; @castor2006rare].
- Conc. H₂SO₄ bake at 400-600 °C, HF and SiF₄ off-gas, water leach of
  REE₂(SO₄)₃, precipitation as double sulfate or hydroxide then redissolution in
  HCl — "Bayan Obo (China)" [@kim2025rare].
- 93-98 wt% H₂SO₄ at 200-250 °C; REE and Th sulfates with H₃PO₄ in the liquor;
  primary-amine Th removal from the sulfate liquor; REE(OH)₃ at pH 8 then
  redissolution in HCl; Th concentrate to licensed storage — "Sulfuric Acid
  Digestion", "Thorium Management" and "Industrial Practice"
  [@jha2016hydrometallurgical; @amaral2010thorium].
- 60-70 wt% NaOH at 140-150 °C and atmospheric pressure; Na₃PO₄ dissolving out
  and recovered for fertiliser; hydroxide cake redissolved in dilute HCl;
  Th(OH)₄ dropped at pH 4-5 — "Sodium Hydroxide Digestion" and "Method 2"
  [@borai2016modified; @shahreldin2018selective].
- (NH₄)₂SO₄ or MgSO₄ at ambient temperature and pH 4-6, in situ through wells or
  heaped, 20-100 days, PLS at 200-1000 mg/L, P507 concentrating 10-50× and
  stripped with HCl, residual NH₄⁺ to groundwater — "Ion-Adsorption Clay
  Leaching" and "Heap Leaching Process" [@shi2022column; @han2024efficient;
  @xiao2015recovery; @chi2008weathered].
- pH 3.5-4.5 for Fe(OH)₃, pH 4.5-5.5 for Al(OH)₃, Ca as gypsum, PO₄³⁻ as
  Ca₃(PO₄)₂ — "Leach Solution Purification" [@jha2016hydrometallurgical].
- Feed spec (0.5-2.0 M REE, Fe < 100 ppm, Al < 500 ppm, Ca < 1000 ppm,
  Th < 10 ppm, PO₄³⁻ < 500 ppm, < 100 NTU) — "Purified Solution Specification"
  table [@jha2016hydrometallurgical].

## Disagreements found, and what I did about them

The brief asked me to flag rather than silently resolve. Six items.

1. **A fourth ASCII flowsheet.** The chapter had *four*, not three: besides the
   three in "Complete Process Flowsheets", the "Processing Overview" section
   (old lines 64-80) carried a generic `Mining → … → Product` chain. The drawn
   figure subsumes it completely, so I replaced it with prose plus a forward
   reference to the figure, and dropped the "This chapter covers steps 2-5"
   phrasing that depended on that block's numbering. **Flagging in case the
   orchestrator's P30 sweep expected that block to survive** — it is the only
   deletion beyond the three I was asked to make.

2. **Bayan Obo is drawn although it was not one of the three ASCII flowsheets.**
   The chapter sets it out in prose immediately after Mountain Pass explicitly so
   the two can be compared, and it is the acid-bake-versus-chloride branch the
   brief asked me to follow. Drawing it is what makes the sulfate/chloride
   colour argument legible. It is the one piece of content in the figure that no
   ASCII drawing contained.

3. **Ore grade feeding flotation — genuine three-way conflict, left unlabelled.**
   "Raw ore: 5-15% REO" (Beneficiation Summary), "Feed: 7-9% REO bastnasite ore"
   (Mountain Pass), and "Grade: 60-75% REO (from 10-30% feed)" (Bastnasite
   Flotation) cannot all describe the same stream, and the waste-generation
   section then computes ore tonnages from the 10-30 % figure. No ore grade
   appears in the figure. **Worth a P30 line.**

4. **Bastnäsite leach acid strength — conflict, left unlabelled.** The HCl
   section gives 4-8 M HCl, 60-90 °C, 1-3 h; the summary table gives
   "2-6M, 60-90°C, 2-4h" for the same step; the sulfuric section gives 2-6 M
   H₂SO₄, 60-95 °C, 1-4 h. Only the temperature is common to all, so the HCl
   leach box carries "60-90 °C" and no molarity or time.

5. **Ion-adsorption lixiviant strength — conflict, left unlabelled.** 2-3 %
   (NH₄)₂SO₄ in the old in-situ flowsheet, 2-5 wt% in the process conditions and
   again in the summary table, and the column-leaching subsection reports that
   *lower* concentrations give *higher* recovery (0.2 % → 93 %, 1.0 % → 85 %),
   which contradicts the framing of 2-5 % as a working range. The leach box
   names the salts and the pH but no concentration.

6. **Leach residence times — pervasive conflict, none drawn.** For steps the
   chapter treats as the same operation it gives 1-2 h, 1-3 h, 1-4 h, 2-4 h,
   2-6 h, 2-8 h, 4-8 h and 6-12 h in different places. No time appears anywhere
   in the figure.

Smaller items I noticed but did not act on, since they are P30's territory:
ThO₂ in monazite is "0-12%" in the mineral list and "0.1-12 wt%" twice
elsewhere; the SX feed section gives pH 0.5-2.0 while the specification table
gives free acid 0.1-1.0 M for the same liquor (I printed neither); and the
monazite concentrate is "55% REO" in the old flowsheet against "50-70%" in the
mineral list (I printed neither).

## Where the three ASCII flowsheets disagreed with the prose

They did not, materially — the prose paragraphs that followed each of them had
already been corrected (the Mountain Pass one explicitly rebuts the "leach with
H₂SO₄ then evaporate it" story, and the monazite one explains the hydroxide
route to chloride). The ASCII drawings were consistent with those corrections.
Their real defect was that they were three separate pictures of the same
skeleton, so the reader had to hold three linear chains in mind to see that the
routes differ only at the cracking step. That is the gap the single figure
closes.

Two things the ASCII drawings carried that the figure deliberately does not:
they ran on past solvent extraction to "Individual REE oxides" and, for the
clays, to calcined REE oxide. The chapter's stated scope ends at the purified
feed, so the figure ends there and the prose says so.

## Verification

Proofed visually via `FIG_PROOF=/tmp/figproof python3
tools/figures/fig_flowsheet.py` and inspection of the PNG, plus a programmatic
extent check (every `Text` against the axes limits, against its containing box,
and against every other text and box). Final state: nothing outside the axes,
nothing spilling a box, no text–box collisions, and the only text–text bbox
contacts are adjacent lines within the same multi-line annotation.

Figure is 10.9 × 7.25 in; body text is 6 pt, which is the practical floor for a
six-column, five-lane flowsheet. It is intended to be read at full page width.

I did not run `mystmd build` and did not commit, as instructed. Files touched:
`tools/figures/fig_flowsheet.py` (new), `figures/05-flowsheet.svg` (generated),
`src/05-hydrometallurgical-leaching.md`, `review/agent-reports/fig05.md`.
