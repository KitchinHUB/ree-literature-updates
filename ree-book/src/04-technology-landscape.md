---
title: The Landscape of Separation Technologies
---

(the-landscape-of-separation-technologies)=
# The Landscape of Separation Technologies

Part I closes with a map. This chapter sketches the two technologies that
actually run at industrial scale today — {index}`solvent extraction` and {index}`ion exchange` —
and then places every approach in this book on a single comparison, so that the
detailed chapters that follow can be read against a common frame.

Ion exchange deserves particular attention here because it has no chapter of
its own. It is the only route that routinely delivers the ≥99.9999% purities
required for optical and electronic applications, and it does so by displacement
{index}`chromatography` rather than by staging. Its limitation is throughput, which is
why it survives industrially as a polishing step downstream of solvent
extraction rather than as a replacement for it.

The comparison at the end of the chapter is worth reading carefully, and worth
reading sceptically. {index}`Separation factors <separation factor>` quoted for laboratory systems are
measured under conditions chosen to show them at their best; the TRL column is
the honest one. Only the incumbent routes — solvent extraction, ion exchange,
ore leaching, and bulk precipitation — are at TRL 9, and each TRL below is
justified from a demonstrated scale rather than from a claimed one.

## Solvent Extraction (Liquid-Liquid Extraction)
Solvent extraction is the dominant industrial method for REE separation, chosen because high-purity rare earths can be produced in large quantities continuously and economically [@xie2014critical].

### Principle of Operation
Solvent extraction operates on mass transfer between two immiscible phases:

1.  An aqueous solution containing REE ions is mixed with an organic phase containing extractant molecules
2.  REEs selectively transfer to the organic phase, forming complexes with extractant molecules
3.  The phases separate (like oil and vinegar), allowing recovery of concentrated REEs

### Commercial Extractants
Key industrial extractants include:

- **{index}`D2EHPA`** (Di-2-ethylhexyl phosphoric acid)
- **{index}`PC88A`/HEHEHP** (2-ethylhexyl phosphonic acid mono-2-ethylhexyl ester) - industrial standard
- **Versatic 10** (neodecanoic acid)
- **{index}`TBP <TBP (tributyl phosphate)>`** (Tributyl phosphate)
- **{index}`Aliquat 336`** (quaternary ammonium salt)
- **Cyanex® 572** - emerging alternative marketed as reducing acid consumption
  relative to PC88A; the quoted reduction is a vendor figure and has not been
  independently reproduced in the literature surveyed here

### Industrial Scale
- Up to **hundreds of stages** of {index}`mixer-settlers <mixer-settler>` may be required
- Typical purities: **99.9-99.99%** on individual oxides, routinely, from a
  cascade with enough stages; the limit is stage count and reflux, not chemistry
- For optical/phosphor-grade materials (5-6 nines purity), ion exchange post-processing is required

(separation-groups)=
### Separation Groups
A commercial plant rarely splits the whole series in one cascade. The common
industrial practice is a first cut into three groups, each then separated
internally. The grouping below is that convention; it is a commercial habit
rather than a chemical boundary, and operators do not draw it identically:

- **Light REEs (LREEs)**: La, Ce, Pr, Nd
- **Medium REEs (MREEs)**: Sm, Eu, Gd
- **Heavy REEs (HREEs)**: Tb, Dy, Ho, Er, Tm, Yb, Lu, Y

Gadolinium is where the conventions disagree, and it is worth flagging because
this book uses both. In the three-group industrial split above, Gd sits in the
middle group. Where the book speaks of two groups — the light/heavy division
used in the glossary and in [](#fig-precipitation-ph) — the light group runs La
through Eu and Gd is counted with the heavies. Neither placement is more
correct than the other; see the [](#glossary) entry for *heavy rare earth
elements (HREE)*.

## Ion Exchange
Ion exchange was the predominant method before the 1960s and remains important for ultra-high purity applications [@elouardi2023progress].

(displacement-chromatography)=
### Displacement Chromatography
Ion exchange separates rare earths by a mechanism with no counterpart in solvent
extraction, and since it has no chapter of its own, it is worth setting out here.

The bed is a strong-acid cation resin, loaded to capacity with the mixed rare
earths as a single narrow band. A chelating eluent — {index}`EDTA`, or HEDTA or
DTPA where a weaker or a stronger complex is wanted — is then pumped through
[@james1968displacement]. It does not *elute* the band in the chromatographic
sense of carrying solutes at different velocities through excess resin; it
*displaces* it, pushing a saturated band down a bed that is otherwise full. Ahead
of the rare earths sits a band of a **retaining ion**, usually Cu²⁺ or Zn²⁺, whose
EDTA complex is less stable than any lanthanide's [@powell1956basic]. Eluent that
runs ahead of the front is intercepted by the retaining ion and handed back, so
the front cannot smear: it stays a step.

Within the band the elements sort themselves by the stability of their EDTA
complexes, which rises monotonically with atomic number. The heavier lanthanide
spends more of its time in solution as the complex, travels faster, and
accumulates at the front; the lighter one is left behind. Because the band is
saturated, an element that diffuses forward into its neighbour's zone meets resin
already fully loaded with a heavier element that outcompetes it and pushes it
back. The zones therefore **self-sharpen** into adjacent bands of nearly pure
single elements, each one abutting the next with a boundary a few centimetres
wide, and each can be cut out of the effluent as it emerges
[@spedding1947separation; @belova2024chromatographic]. This is why the method
reaches purities a cascade struggles with: the separation is not the ratio of two
distribution coefficients repeated across dozens of stages, it is a
thermodynamically self-correcting front.

```text
EDTA eluent in                              direction of travel  →
     │
     ▼
┌────────────┬──────┬──────┬──────┬──────┬──────┬───────────┬────────┐
│  eluent    │  La  │  Ce  │  Pr  │  Nd  │  Sm  │ retaining │ resin  │
│  front     │      │      │      │      │      │ ion, Cu²⁺ │ ahead  │
└────────────┴──────┴──────┴──────┴──────┴──────┴───────────┴────────┘
  rear of band   ←── weakest EDTA complex to strongest ──→   band front
                     (each zone one element, self-sharpening)
```

What limits the method is not resolution, which is excellent, but throughput.
The band occupies the whole bed, so the quantity separated per cycle is set by
the resin inventory rather than by a flow rate; a cycle takes days to weeks;
the product leaves at the eluent's concentration, so it is dilute and must be
precipitated and redissolved; and both the eluent and the retaining ion have to
be recovered and recycled. Capital and cycle time per kilogram are therefore
poor against a mixer-settler train that runs continuously
[@elouardi2023progress]. That economics confines displacement chromatography to
work where purity is worth more than tonnage — scandium and lutetium, 5N-6N
oxides for optical and electronic use, and, historically, the Manhattan-era and
early Ames Laboratory separations that first produced weighable quantities of the
individual lanthanides in pure form [@spedding1947separation].

**Extraction chromatography** is a related but distinct arrangement, and it makes
the throughput point unusually concrete. Instead of an ion-exchange resin and a
chelating eluent, a reverse-phase column is functionalized by physically adsorbing
a solvent-extraction reagent onto its C18 chains, so that the separation chemistry
is the extractant's and the staging is the column's. @sanku2021extraction
impregnated a 150 mm × 4.6 mm Kromasil C18 column with HDEHP to a ligand density
of 0.64 mmol/g, and eluted a six-element mixture — La, Ce, Pr, Nd, Y, Dy from
synthetic apatite leach solutions — with a combined isocratic and gradient nitric
acid programme at 40 °C. It resolved all six into individual fractions in a single
pass, including, in their description, an almost perfect separation of Nd from Pr,
the pair that costs a solvent extraction plant tens of stages.

The load was **50 µL of a 1,000 mg/L solution: 50 micrograms of total rare
earth**. The authors are explicit that this is "just exceeding the analytical
range" and that limited productivity is the method's main drawback. That
juxtaposition — a separation a cascade would need forty-five stages to achieve,
performed in one pass on fifty micrograms — is the cleanest statement in this
chapter of why resolution and throughput are separate axes, and why a technology
can be excellent on one and disqualified on the other. Scaling it is not a matter
of running the column longer; it requires operating in the overloaded regime,
where resolution degrades, and the paper names that as the necessary next
experiment rather than claiming it.

### The Resins Themselves

The chemistry underneath is the same acid-base and coordination chemistry that
solvent extraction uses, immobilized on a bead. A strong-acid sulfonic resin
exchanges cations without discriminating much among them; it separates the
lanthanides only when an eluent does the discriminating, which is the
displacement scheme above. A weak-acid carboxylic resin is ionized only above
its pKa, so loading and stripping are set by pH rather than by an added
complexant. A chelating resin carries the ligand itself — iminodiacetic,
aminophosphonic, {index}`diglycolamide` — and brings the selectivity of the
corresponding extractant onto a solid. An anion exchanger works from the other
side, holding rare earths only in media concentrated enough to form anionic
sulfate or chloride complexes.

The chelating family is where most of the recent work sits, and its ligands are
borrowed rather than invented. The diglycolamides were developed for
partitioning minor actinides from lanthanides in spent fuel reprocessing
[@ansari2011chemistry]; the same molecules now appear supported on beads.
@croft2024polymer puts the case for the class plainly, and it is worth
repeating here: the advantage is using the *same* extractants as commercial
solvent extraction, with far less of them. What none of this changes is the
throughput arithmetic of the section above. Ion exchange is reviewed as a route
for secondary resources — recycled magnets, mine and metallurgical waste
streams — on the strength of its selectivity and the simplicity of running it,
not of its capacity [@elouardi2023progress].

### Solid Phases Under Development

Three directions are worth naming. The honest summary of all three is that they
are laboratory results.

**Magnetic adsorbents.** Superparamagnetic nanoparticles functionalized as rare
earth ion adsorbents — magnetic nanohydrometallurgy — replace filtration with a
magnet [@molinacaldern2022advances]. The attraction is mechanical rather than
chemical. The binding chemistry is the resin chemistry above; what changes is
that recovering a sub-micron particle from a slurry stops being the step that
decides whether the material can be used at all.

**Polymer inclusion beads.** @croft2024online packed micro
{index}`polymer inclusion beads <polymer inclusion membranes>` — 60 wt%
D2EHPA in 40 wt% PVC — into a column, the first time these beads had been run
in that format. The column separated La³⁺ from Gd³⁺, then took a digest of
end-of-life {index}`NdFeB` permanent magnets in 2 M sulfuric acid containing
Fe³⁺, Co²⁺ and Ni²⁺, diluted it to 0.03 M acid, reduced the iron to Fe²⁺ with
ascorbic acid, and recovered Nd³⁺ and Dy³⁺ by selective back-extraction into
0.3 M and 2 M sulfuric acid respectively. Thermogravimetry after six cycles
showed negligible loss of D2EHPA from the beads. The extractant is the ordinary
industrial one; what the bead contributes is holding a small quantity of it in a
form that can be packed, run and reused.

**Ion-imprinted polymers.** Polymerize around a template ion, then remove it,
and the cavity left behind matches that ion in size and coordination.
{index}`Ion-imprinted polymers <ion-imprinted polymer>` are the sharpest
statement of the idea that selectivity can be built into a solid rather than
tuned by solution chemistry. The strongest recent result is a
thulium-imprinted polymer bridged by alkyne linkages, reported with a maximum
capacity of 58.6 mg/g, a Tm³⁺/La³⁺ separation factor of 161, retention of 95%
of capacity over ten adsorption-desorption cycles, and 12.6 mg/g still
available in 1 M HCl [@zhao2025ultra]. That separation factor needs the
convention this chapter states below applied to it: Tm and La sit at opposite
ends of the series, so 161 is a whole-series number and not an adjacent-pair
one, and it comes from a single laboratory report on a synthetic acidic
wastewater with a cavity imprinted for one element. Read it as what an
imprinted cavity can do, not as what a process does. Comparable figures for
imprinted polymers as a class are not given here: no source consulted reports
them for the class, and the class is young and heterogeneous enough that an
average across it would not mean much.

(technology-comparison)=
## Comparison of Separation Technologies

This is the book's single comparison table; where another chapter needs one, it
points here. Four conventions govern it, and they are what make it usable.

**A separation factor without an element pair is not a number.** β = 796 for
Pr/Lu and β = 1.5 for Nd/Pr describe problems that differ by six elements of
lanthanide contraction; quoting either as "the separation factor" of a technology
is the most common way a comparison misleads. Every β below carries its pair.

**"Not reported" is an entry.** Several chapters describe real technologies that
have never been characterised on an adjacent lanthanide pair — they report
recovery, or purity, or discrimination against iron. Where that is so, the cell
says so rather than borrowing a number from somewhere else.

**TRL is assigned from demonstrated scale**, not from promise, and each is
justified in the notes. A licensing announcement, a techno-economic study of a
plant that does not exist, and a vendor datasheet are not demonstrations.

**Conditions are the chapter's own.** Where a chapter gives no feed
concentration, temperature or pH — which is more often than it should be — the
cell says "not reported", and that absence is itself a finding.

| Approach | Best reported β (element pair) | Feed | Conditions | Demonstrated scale | TRL |
|----|----|----|----|----|----|
| **Solvent extraction** — [](#solvent-extraction-fundamentals) | ~1.5-2 per stage for adjacent pairs, wider for pairs several atomic numbers apart — see [](#solvent-extraction-fundamentals) on why published β values are often not comparable. Which is why up to hundreds of mixer-settler stages are assembled to make the separation [@xie2014critical] | Real: purified chloride or nitrate liquor from any ore route | 0.3-1.5 M REE; 20-40 °C; pH 2.5-4.0 extraction, \<1 stripping | Commercial; tens of thousands of t/y REO worldwide | 9 [^trl-sx] |
| **Ion exchange (displacement)** — [](#displacement-chromatography) | Not expressed as β; adjacent zones separate on EDTA complex stability [@powell1956basic] | Real: mixed REE loaded on cation resin | Chelating eluent (EDTA/HEDTA/DTPA), ambient, Cu²⁺ or Zn²⁺ retaining ion | Commercial polishing step; pilot plants since 1947 [@spedding1947separation] | 9 [^trl-ix] |
| **Hydrometallurgical leaching** — [](#hydrometallurgical-leaching) | Not reported. The chapter's only quantified split is Al/REE at aluminium removal: 94.4 % of the aluminium out for 8.2 % of the rare earths lost, at pH 4.5 and 60 °C [@wang2020removal] | Real ores: bastnäsite concentrate 60-65 % REO at Mountain Pass and 61 % at Bayan Obo, from a 7-9 % REO flotation feed; monazite typically 40-70 % REO, with a by-country table spanning 35 to 74 %, carrying typically 5-6 wt % ThO₂; ion-adsorption clay ore at a few tenths of a percent REO, never above 1 % [@iaea2011radiation] | Monazite: 98 % H₂SO₄ at 200-220 °C, or 60-70 % NaOH at 140-160 °C for 3-9 h [@iaea2011radiation]. Bastnäsite acid molarity and leach temperature, and the pH windows for iron removal: **not reported** — the chapter deleted the values it carried as untraceable | Commercial for every ore type in the chapter, including the Indian monazite circuit [@jha2016hydrometallurgical] | 9 [^trl-leach] |
| **Ion-adsorption clays** — [](#ion-adsorption-clays) | Not expressed as β. The mechanism itself is the limitation: ion exchange, which does most of the leaching, "cannot cause evident REE fractionation"; only surface complexation fractionates, enriching HREE over LREE [@wu2023rare] | Real regolith ore, a few tenths of a percent REO and not above 1 % [@iaea2011radiation], REE in the ion-exchangeable phase | (NH₄)₂SO₄ or MgSO₄. A thermodynamic screening across 0.05-0.6 M and 25-80 °C finds the ammonium salt degrades with dose and does so element-specifically — La³⁺ maximally stable only to 0.25 M, Nd³⁺ only to 0.05 M [@mohamadsobri2025enhancing]. Plant lixiviant strength, temperature and liquor pH: **not reported** | Leaching: commercial in-situ, \>90 % of global HREE supply [@zhou2020genesis]. Electrokinetic mining, which replaces hydraulic flow with an applied field, is reported at 95 % REE recovery on a 5,000 t ore body with a 95 % reduction in ammonia emissions [@wang2025industrial] — one laboratory, unreplicated ([](#electrokinetic-mining)). Clay as a separation medium: not demonstrated | 9 conventional leaching / 6-7 electrokinetic leaching / 2-3 as a separation step [^trl-iac] |
| **Pyrometallurgy and halogenation** — [](#pyrometallurgical-and-halogenation-routes) | Adjacent-pair separation factors **are** reported, and they are small: 0.89-1.16 La:Ce, 1.01-1.59 Pr:Ce and 1.23-1.32 Pr:Nd on a reduced condensation gradient, rising to 2.01-2.28 Ce:La, 1.30-1.33 Ce:Pr and 0.96-1.08 Nd:Pr on a wavy one, by selective condensation in stepwise carbochlorination-chemical vapour transport [@huang2002rare]. **The best of them is about 2.3, and several fall below 1** — one stage of solvent extraction, obtained at 1000 °C in chlorine. Earlier drafts of this row claimed a ~80 % chloride purity for a La+Ce group cut; no purity figure of any kind appears in the source, and it has been withdrawn | Real: mineral concentrates, tabulated at 70-74 wt % REO for bastnäsite, 35-71 % for monazite and 52-67 % for xenotime [@jha2016hydrometallurgical], plus NdFeB scrap | Anhydrous throughout, no pH. One-step carbochlorination of bastnäsite, 700 °C, 60 min, 12 % reductant, 10 L/min Cl₂ [@xue2025onestep]. SC-CVT on mixed bastnäsite-monazite is a different and colder sequence: 500 °C for 2 h under Cl₂ + SiCl₄ at Ln:C = 1:3 for extraction, 800 °C for 0.5 h with AlCl₃ added for thorium removal, then 1000 °C for 6 h under Cl₂ + AlCl₃ for the separation itself [@huang2002rare] | Pilot-to-commercial in China (Baotou); pilot elsewhere | 7-8 China / 6-7 elsewhere [^trl-pyro] |
| **Coacervates and aqueous biphasic systems** — [](#coacervates-and-aqueous-biphasic-systems) | **Not reported** for any lanthanide pair by a coacervate or an aqueous biphasic system. Cloud-point extraction does report one: Gd/La 32.4 ± 0.6 in a single contact, with D = 2067 for Gd against 63.8 for La, at a 14-fold molar excess of 8-hydroxyquinoline in 1 wt % Triton X-114, pH 5.5, 60 °C [@favrerguillon2004cloud] — a pair four f electrons apart, on a synthetic 0.36 mM solution. The best verified adjacent-pair figures in that chapter are protein-based: Nd/Dy 8.12 ± 0.40 for Hans-LanM and 12.7 ± 1.3 for its R100K variant [@mattocks2023enhanced] | Synthetic, composition not reported. One real feed: NdFeB magnet leachate, for Fe/REE rejection (Fe \>99 % extracted, REE \<10 %) [@liu2022one] | Cloud point: 1 wt % Triton X-114, pH 5.5, 60 °C for 1 h, 8-HQ:Ln = 14, 45 mL micellar phase to 1.2 mL surfactant-rich [@favrerguillon2004cloud]. Otherwise not reported. Isolated values: PNIPAM LCST ~32 °C; Sc-selective phosphonate at pH 0.78 | Bench. The chapter lists pilot demonstration on real feedstock as an unmet need | 3-4 [^trl-coac] |
| **Microfluidic separations** — [](#microfluidic-separations) | 279, Dy/La, flow-focusing droplet microreactor at 90 % Dy extraction [@fernandezmaza2024high]. Adjacent-pair reality check: 2.72, Nd/Pr, with D2EHPA [@safarzadeh2018insights] | Both. Dy/La binary is synthetic; real feeds include leached mixed-REO concentrate with Cyanex 572 [@kolar2016microfluidic] and NdFeB leachate [@yadav2018ndfeb] | pH 1 (Dy/La) to pH 5 (D2EHPA); residence 3-60 s; REE feed concentration and temperature not reported | Pilot: three-stage countercurrent, numbered up 100-fold with no loss of extraction efficiency; throughput not published [@yang2022pilot]; 8 m² HFSLM module [@alemrajabi2022separation] | 4-5 [^trl-micro] |
| **Precipitation and selective crystallization** — [](#precipitation-and-selective-crystallization) | 26.9 ± 3.1, La/Lu, by solvothermal selective crystallization with H₂PDA [@yin2025selective]. Best-documented Ce(IV)/RE(III) split is 99.8 % of the cerium precipitated as Ce(OH)₄ with under 1.5 % co-precipitation of the others, by permanganate on a NiMH battery leachate [@salehi2025tailored] | Both. Real: bastnäsite calcine, acid mine drainage, NiMH leachate, electrolytic slag. Designed ligands: synthetic only | Oxalate 1.5 mol per mol REE by stoichiometry; raising the temperature *decreases* oxalate recovery, so no warm operating window is given [@nawab2022parametric]. Staged hydroxide: Fe³⁺ over pH 2.0-3.5, Al³⁺ over 3.5-4.5, rare earths as hydroxide over 7.0-10.0 [@zhang2018rare; @li2025iron]. Oxalate pH control tolerance: **not reported** | Commercial for bulk precipitation and Ce removal (Molycorp calcine route); proof-of-concept for the designed ligands | 9 conventional / 2-3 designed ligands [^trl-precip] |
| **Biological and biomimetic** — [](#biological-and-biomimetic-separations) | **No pairwise β is reported.** Lanmodulin's intrinsic Ln³⁺/Ln³⁺ preference is only about fivefold across the whole La-Lu series [@mattocks2023enhanced]; the famous 10⁸ figure is Ln³⁺/Ca²⁺ [@cotruvo2018lanmodulin], not Ln/Ln. Best separation performance: \>98 % purity and \>99 % yield on a Dy/Nd mixture in a single column stage with the Hans-LanM R100K variant [@mattocks2023enhanced]. The original immobilized-LanM column reaches 99.9 % purity on both halves of a 50:50 Dy/Nd feed, but recovers only \~76 % of each element [@dong2021bridging] | Real and characterised: a Powder River Basin coal fly ash leachate at 0.043 mol % REE — \~150 µM total REE against millimolar Na, Mg, Al, Ca and Sr — taken to 88.2 mol % purity in a single column run [@dong2021bridging]; e-waste as sole REE source for engineered *M. extorquens* [@good2024scalable] | Adsorption pH 3, desorption pH \<1.7 (binding halved at pH 2.2, insignificant at ≤1.7); protein stable to pH 2.5 and 95 °C; synthetic feeds 0.2 mM Nd, fly ash leachate \~150 µM total REE; temperature not reported | Bench. Columns of 0.80-1.0 mL bed volume at 0.5 mL/min, largest run 29.1 bed volumes of leachate through 0.94 mL of resin, ten adsorption/desorption cycles without capacity loss [@dong2021bridging]; largest biological figure is a 10 L culture [@good2024scalable]. No continuous or scaled-up operation is reported | 3-4 [^trl-bio] |
| **Electrochemical separations** — [](#electrochemical-separations) | **No equilibrium β is reported for any lanthanide pair.** The one quantified separation is 125 by EDTA-assisted electrodialysis [@ding2023separation], and it needs two qualifications that earlier drafts of this table got wrong: it is Dy over Pr **and** Nd combined, not Dy/Nd, and it is a ratio of fractional transfers after a 180-minute batch — 62 at 10 V, 125 at 12 V, 88 at 14 V — not a distribution-ratio β comparable with the rest of this column. It delivers 93 % Dy purity at 77 % Dy yield, and the selectivity is the EDTA's, not the electrode's: the same paper finds Pr/Nd inseparable even by cascading, and states that electrodialysis without chelation cannot separate rare earths at all. Electrosorption discriminates rare earths from base metals, not lanthanides from each other: 23.66 mg/g La in 25 min from a La/Fe/Ca/Na solution on N-doped carbon [@zhao2022selectively]. The best-quantified electrochemical split in the chapter is an impurity removal, 8.4 mg Th per g of carbon [@aziman2021rapid] | Synthetic for every separation result — the electrodialysis feed is Pr, Nd and Dy sulfates in deionized water at 0.001 mol/L each (141, 144, 163 mg/L), chosen to resemble an ion-adsorption clay leachate [@ding2023separation]. Real feed appears only at the two ends of the flowsheet: a 5,000 t ore body under electrokinetic mining [@wang2025industrial], and the oxide or halide entering a metal cell | Electrosorption and electrodialysis: dilute aqueous, ambient. Electrodialysis: 10-14 V across a four-compartment cell, 100 cm² membrane area, 500 mL per compartment, pH 3-4, EDTA/Dy 1:1, 150-180 min; \~45 GJ per tonne of REE separated against 15.6-22.7 GJ/t quoted for solvent extraction, at a space-time yield of 0.002 kg L⁻¹ h⁻¹ [@ding2023separation]. Electrosorption current density and energy per kg of product: **not reported**. Molten salt electrolysis conditions are in [](#molten-salt-electrolysis) | Commercial at both ends — all rare earth metal is made in an electrolytic cell, and EKM is demonstrated on 5,000 t of ore [@wang2025industrial]. Between lanthanides: bench, synthetic solutions | 9 electrowinning / 6-7 EKM / 2-3 as a lanthanide separation [^trl-electro] |
| **Membranes, MOFs and emerging** — [](#membranes-mofs-and-emerging-approaches) | **796, Pr/Lu**, and 273, Nd/Er, in a single step on the MOF nanotrap NCU-1 [@hu2024rationally] — the highest β in this book. The same experiment gave 67 for Nd/Dy, which is the pair a magnet recycler faces, and is the number to carry forward. **Artificial ion channels** on a pillar[5]arene scaffold report transport selectivities of ~140 Tb/La, 72 Tb/Yb and 58 Tb/Nd [@behera2025supramolecular] — the largest membrane numbers in this book, from one paper, measured across a lipid bilayer rather than a process membrane. The same paper's nearest pair, Tb/Eu, gives **3**, and no adjacent pair is measured at all. **COFs**: 15.34 Eu/Yb, 14.70 Eu/Tm, 10.78 Eu/La [@xiao2022highly] — middle-versus-end pairs, not adjacent ones. **Nanofiltration and ultrafiltration** reject rare earths as a *group* and well — Nd rejection rises from 86.7 % to 99.5 % when the feed is complexed [@murthy2011application] — and have never separated adjacent lanthanides [@feng2026selective]. **MXenes**: no lanthanide pair; 892.8 mg/g Eu(III) at pH 2.0 and 99.1 % Eu removal by a supported membrane at pH 5.0 [@bao2025mxene]. scCO₂: explicitly cannot separate individual lanthanides | MOFs: synthetic binary solutions, milligram scale, plus one real tailings water at 0.09-0.92 ppm REE. Artificial channels and COFs: synthetic only. MXenes: synthetic, then a real rare earth processing wastewater and a magnet-manufacturing sludge [@bao2025mxene]. NF/UF: real acid mine drainage, coal fly ash leachate and WEEE effluent, and one synthetic-to-real comparison in which 97 % REE rejection became 71 % [@kosemutlu2020separation]. scCO₂: real — roasted and caustic-digested bastnäsite; coal fly ash at 591 mg/kg for Appalachian, 403 for Illinois basin coals [@taggart2016trends] | NCU-1: 1:1 binary lanthanide nitrate solution in water at pH 4.5, where *K*d peaks; it falls away by pH 6, so an acidic leach liquor must be neutralised first [@hu2024rationally]. NF/UF: 4-24 bar, pH 1.5-3.5, with the economic optimum at the low-pressure corner [@kosemutlu2018application]. MXene: pH 2.0 batch, pH 5.0 membrane [@bao2025mxene]. Artificial channels: transport across a bilayer; flux at practical driving force **not reported**. scCO₂: 34 MPa and 65 °C with TBP-HNO₃ adducts at 2-6 M H⁺ [@sinclair2017rare] | Lab for everything that separates lanthanides. The 4,000 L reactor is a techno-economic design study [@azimi2025technoeconomic], not a built facility. NF/UF modules are commercial hardware operated on REE feeds at bench and small-pilot scale, as a concentration step | 2-3 MOFs, COFs, MXenes and channels / 4-5 NF-UF as a concentration step / 4-5 scCO₂ [^trl-mof] |

*TRL = Technology Readiness Level (1-9 scale). β = separation factor.*

[^trl-sx]: Full commercial deployment: solvent extraction produces essentially
    all separated rare earth oxide sold today, at plant scale, continuously.

[^trl-ix]: Commercial, but as a polishing step rather than a bulk route.
    Pilot-plant separations were demonstrated in 1947 [@spedding1947separation]
    and the method has been in industrial use for high-purity oxides since.

[^trl-leach]: Commercial for every ore type in the chapter, the Indian
    monazite circuit included. Bioleaching within the same chapter is
    explicitly "laboratory and pilot scale, not yet industrial implementation".

[^trl-iac]: Three different technologies share the chapter. In-situ ammonium- or
    magnesium-sulfate leaching is commercial and dominant. Electrokinetic mining
    is a leaching technology, not a separation: it is reported at field and
    industrial scale by one group [@wang2022electrokinetic; @wang2025industrial],
    with a comparative technoeconomic analysis but no independent replication,
    which supports 6-7 and not 9 — see also [^trl-electro]. Using the clay itself
    as a chromatographic separation medium has no engineered demonstration at
    all — the chapter's own proof of concept is the orebody, and it lists
    measured separation factors on clay as an open research question — so it
    sits at concept stage. The impurity rejection electrokinetic mining does
    achieve is rare earths against aluminium, iron and calcium, which does not
    change that assessment.

[^trl-pyro]: Carbochlorination is described as practiced at pilot-to-commercial
    scale at Baotou, which supports 7-8 in China; outside China the chapter
    reports pilot demonstration only, hence 6-7. Ch. 7 states both numbers in
    different places. That 7-8 should be read narrowly. It is carbochlorination
    of *bastnäsite* concentrate that is industrial; [@huang2002rare] states that
    the Baotou mixed bastnäsite-monazite concentrate is treated by
    high-temperature sulfuric acid roasting followed by solvent extraction, and
    that Goldschmidt carbochlorination "has not been applied industrially" for
    that feed. The separation half of the row — SC-CVT — is bench work in a
    1500 mm tube furnace and would rate 3 on its own. **Flash Joule heating with chlorination** is a special
    case: it is a feed-activation and leaching step rather than a separation,
    ch. 7 assigns it TRL 5-6 on a "pilot" designation, but the only support
    offered is a licensing agreement and production *planned* for 2026. On
    demonstrated scale it is bench work, TRL 4-5, until a pilot run is
    documented.

[^trl-coac]: Laboratory proof of concept only. The chapter states that pilot
    demonstration with real feedstock remains a research need, and gives no
    feed composition, throughput or cycle data for any system.

[^trl-micro]: Continuous multi-stage operation on real leachate has been
    demonstrated, which is more than most of Part III can claim, but the
    demonstrated scale is several orders of magnitude below plant scale and the
    chapter states that commercial-scale microfluidic REE plants do not exist. **Supported
    liquid membranes** are the strongest membrane result in the book — an 8 m²
    hollow-fibre module and \>97 % Dy purity from NdFeB leachate — and belong at
    the same 4-5. Nanofiltration and ultrafiltration are assessed with the other
    membranes in [^trl-mof].

[^trl-precip]: Oxalate and carbonate precipitation and oxidative cerium removal
    are unit operations inside commercial flowsheets. The reverse-size-selective
    ligands in the second half of the chapter are, in the chapter's own words,
    at proof-of-concept scale.

[^trl-bio]: Bench columns and a 10 L culture. Ch. 11's own summary table
    assigns "pilot" and even "industrial" scalability to several entries, but no
    demonstration in the chapter supports those labels, and the chapter
    elsewhere states that commercial breakthroughs have been limited.

[^trl-electro]: Three technologies at three readiness levels share one row.
    Molten salt electrolysis is the commercial route to rare earth metal and sits
    at 9. Electrokinetic mining is reported at 5,000 t of ore with a comparative
    technoeconomic analysis [@wang2025industrial], which is a pilot-to-commercial
    demonstration, but from a single laboratory and unreplicated, hence 6-7 rather
    than higher. As a separation *between* lanthanides the chapter has bench work
    on synthetic solutions and nothing else. The single quantified result, the
    electrodialysis separation factor of 125, is a batch transfer ratio on a
    synthetic three-element feed at bench scale, and its authors conclude that a
    standalone electrodialysis process offers no clear technical or economic
    advantage over solvent extraction — so 2-3, on the same basis as the MOF
    entry below.

[^trl-mof]: The MOF nanotrap result is a single study on synthetic feed at
    milligram scale with no capacity, kinetic, cycling or real-feed data — a
    striking laboratory measurement, not a process. The artificial-channel
    result is one paper measuring transport across a bilayer, with no flux, no
    module and no lifetime, and sits at the same 2-3; so do the COF and MXene
    results, which are adsorption studies rather than processes even where they
    use real feed. Nanofiltration and ultrafiltration are the exception in the
    row: the hardware is mature and commercial in other industries, and the REE
    work is bench-to-small-pilot on real leachates, which supports 4-5 *as a
    concentration and impurity-rejection step*. As a separation between
    lanthanides NF/UF cannot be assigned a TRL, because no such separation has
    been demonstrated. Supercritical CO₂ extraction has repeated bench-scale
    batch demonstrations on real solids, which supports 4-5; the 4,000 L
    facility exists only as a techno-economic analysis.
