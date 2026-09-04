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

### Conventional Ion Exchange Resins
**Advantages:**

- Capable of refining all REEs
- Adaptable to various raw material compositions
- Can achieve 5N-6N purities (99.999-99.9999%)

**Disadvantages:**

- Low throughput
- Prolonged batch processes (up to a month)
- High operational costs
- Low concentrations of REEs in solutions

**Resin Types:**

| Resin Type | Functional Group | Application |
|----|----|----|
| Strong acid cation | Sulfonic acid (-SO₃H) | General REE separation |
| Weak acid cation | Carboxylic acid (-COOH) | pH-selective extraction |
| Chelating | Iminodiacetic acid, aminophosphonic | High selectivity |
| Anion exchange | Quaternary ammonium | REE-anionic complex capture |

### Magnetic Ion Exchange Adsorbents
Magnetic adsorbents combine polymer ion-exchange functionality with magnetic particles for easy recovery, representing an emerging approach for REE separation [@molinacaldern2022advances].

**Design Approaches:**

| Approach | Description | Advantages |
|----|----|----|
| Impregnated beads | Magnetite (Fe₃O₄) grown or embedded in polymer beads | Simple fabrication |
| Core-shell | Magnetic core with polymer shell | High magnetic response |
| Composite | Magnetic particles dispersed in polymer matrix | Tunable properties |

**Functional Groups:**

- Sulfonic acid groups for general cation exchange
- Chelating groups (iminodiacetic acid, EDTA-type) for selectivity
- Phosphonic acid groups for enhanced REE binding

**Operational Benefits:**

- Magnetic collection after use eliminates filtration/centrifugation
- Rapid solid-liquid separation
- Reusable through desorption and regeneration
- Demonstrated for heavy metal removal (Cu²⁺, Pb²⁺) with translation to REE recovery

### Polymer Inclusion Beads (µPIBs)
Micro {index}`polymer inclusion beads <polymer inclusion membranes>` represent a recent advance for online separation of critical rare-earth elements from end-of-life permanent magnets [@croft2024online].

**Features:**

- Functionalized polymer phase for selective REE binding
- Magnetic responsiveness for easy recovery
- Designed specifically for magnet recycling applications
- Online separation capability

**Target Applications:**

- {index}`NdFeB` permanent magnet recycling
- Recovery of Nd, Pr, Dy from e-waste
- Separation of critical REEs from non-critical elements

### Ion-Imprinted Polymers (IIPs)
{index}`Ion-imprinted polymers <ion-imprinted polymer>` create binding cavities complementary in size and coordination to target REE ions, enabling high selectivity [@zhao2025ultra].

**Imprinting Process:**

1.  Template REE ion complexed with functional monomers
2.  Cross-linking polymerization around template
3.  Template removal creates selective cavities
4.  Rebinding occurs with high specificity

**Multi-Ion Imprinted Polymers (MIIPs):** Recent developments enable simultaneous imprinting for multiple REEs:

- Cavities for both light and heavy REEs
- Group selectivity (LREE vs. HREE)
- Higher capacity than single-ion IIPs

**Performance Characteristics:**

| Parameter               | Typical Value             |
|-------------------------|---------------------------|
| Selectivity coefficient | 10-100× vs. non-imprinted |
| Adsorption capacity     | 20-100 mg/g               |
| Reusability             | \>10 cycles               |
| Equilibrium time        | 30-120 minutes            |

### Advanced Chelating Resins
Modern chelating resins offer improved selectivity through tailored functional groups:

**Aminophosphonic Acid Resins:**

- Strong affinity for trivalent REEs
- pH-dependent selectivity
- Effective for HREE enrichment

**Diglycolamic Acid Resins:**

- Selective for middle and heavy REEs
- Applied in spent nuclear fuel processing
- High radiation stability

**Bis-picolinic Acid Resins:**

- Exceptionally high selectivity for Am/Cm over lanthanides
- Used in minor actinide separations

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
| **Hydrometallurgical leaching** — [](#hydrometallurgical-leaching) | Not reported. The chapter's only quantified split is Al/REE at aluminium removal: 94.4 % of the aluminium out for 8.2 % of the rare earths lost, at pH 4.5 and 60 °C [@wang2020removal] | Real ores: bastnäsite concentrate 60-65 % REO at Mountain Pass and 61 % at Bayan Obo, from a 7-9 % REO flotation feed; monazite concentrate 44-60 % REO carrying typically 5-6 wt % ThO₂; ion-adsorption clay ore at a few tenths of a percent REO, never above 1 % [@iaea2011radiation] | Monazite: 98 % H₂SO₄ at 200-220 °C, or 60-70 % NaOH at 140-160 °C for 3-9 h [@iaea2011radiation]. Bastnäsite acid molarity and leach temperature, and the pH windows for iron removal: **not reported** — the chapter deleted the values it carried as untraceable | Commercial for every ore type in the chapter, including the Indian monazite circuit [@jha2016hydrometallurgical] | 9 [^trl-leach] |
| **Ion-adsorption clays** — [](#ion-adsorption-clays) | Not expressed as β. The mechanism itself is the limitation: ion exchange, which does most of the leaching, "cannot cause evident REE fractionation"; only surface complexation fractionates, enriching HREE over LREE [@wu2023rare] | Real regolith ore, a few tenths of a percent REO and not above 1 % [@iaea2011radiation], REE in the ion-exchangeable phase | (NH₄)₂SO₄ or MgSO₄. A thermodynamic screening across 0.05-0.6 M and 25-80 °C finds the ammonium salt degrades with dose and does so element-specifically — La³⁺ maximally stable only to 0.25 M, Nd³⁺ only to 0.05 M [@mohamadsobri2025enhancing]. Plant lixiviant strength, temperature and liquor pH: **not reported** | Leaching: commercial in-situ, \>90 % of global HREE supply [@zhou2020genesis]. Clay as a separation medium: not demonstrated | 9 leaching / 2-3 as a separation step [^trl-iac] |
| **Pyrometallurgy and halogenation** — [](#pyrometallurgical-and-halogenation-routes) | Not reported for any lanthanide pair. The best quantified split is a La+Ce group cut, ~80 % chloride purity, by selective condensation in stepwise carbochlorination-chemical vapour transport [@huang2002rare] | Real: bastnäsite ~70 wt % REO, monazite 55-65 % REO, xenotime 52-62 % REO, NdFeB scrap | Carbochlorination 600-900 °C (optimum 700 °C, 60 min, 12 wt % C, Cl₂); anhydrous, no pH | Pilot-to-commercial in China (Baotou); pilot elsewhere | 7-8 China / 6-7 elsewhere [^trl-pyro] |
| **Coacervates and aqueous biphasic systems** — [](#coacervates-and-aqueous-biphasic-systems) | **Not reported** for any lanthanide pair by a coacervate or cloud-point system. The Gd/La figure this row previously carried could not be confirmed against its source and was withdrawn from [](#coacervates-and-aqueous-biphasic-systems). The best verified adjacent-pair figures in that chapter are protein-based: Nd/Dy 8.12 ± 0.40 for Hans-LanM and 12.7 ± 1.3 for its R100K variant [@mattocks2023enhanced] | Synthetic, composition not reported. One real feed: NdFeB magnet leachate, for Fe/REE rejection (Fe \>99 % extracted, REE \<10 %) [@liu2022one] | Not reported. Isolated values: PNIPAM LCST ~32 °C; Sc-selective phosphonate at pH 0.78 | Bench. The chapter lists pilot demonstration on real feedstock as an unmet need | 3-4 [^trl-coac] |
| **Microfluidic separations** — [](#microfluidic-separations) | 279, Dy/La, flow-focusing droplet microreactor at 90 % Dy extraction [@fernandezmaza2024high]; 125, Dy/Nd, by electrodialysis with EDTA [@ding2023separation]. Adjacent-pair reality check: 2.72, Nd/Pr, with D2EHPA [@safarzadeh2018insights] | Both. Dy/La binary is synthetic; real feeds include leached mixed-REO concentrate with Cyanex 572 [@kolar2016microfluidic] and NdFeB leachate [@yadav2018ndfeb] | pH 1 (Dy/La) to pH 5 (D2EHPA); residence 3-60 s; REE feed concentration and temperature not reported | Pilot: three-stage countercurrent, numbered up 100-fold with no loss of extraction efficiency; throughput not published [@yang2022pilot]; 8 m² HFSLM module [@alemrajabi2022separation] | 4-5 [^trl-micro] |
| **Precipitation and selective crystallization** — [](#precipitation-and-selective-crystallization) | 26.9 ± 3.1, La/Lu, by solvothermal selective crystallization with H₂PDA [@yin2025selective]. Best-documented Ce(IV)/RE(III) split is 99.8 % of the cerium precipitated as Ce(OH)₄ with under 1.5 % co-precipitation of the others, by permanganate on a NiMH battery leachate [@salehi2025tailored] | Both. Real: bastnäsite calcine, acid mine drainage, NiMH leachate, electrolytic slag. Designed ligands: synthetic only | Oxalate 1.5 mol per mol REE by stoichiometry; raising the temperature *decreases* oxalate recovery, so no warm operating window is given [@nawab2022parametric]. Staged hydroxide: Fe³⁺ over pH 2.0-3.5, Al³⁺ over 3.5-4.5, rare earths as hydroxide over 7.0-10.0 [@zhang2018rare; @li2025iron]. Oxalate pH control tolerance: **not reported** | Commercial for bulk precipitation and Ce removal (Molycorp calcine route); proof-of-concept for the designed ligands | 9 conventional / 2-3 designed ligands [^trl-precip] |
| **Biological and biomimetic** — [](#biological-and-biomimetic-separations) | **No pairwise β is reported.** Lanmodulin's intrinsic Ln³⁺/Ln³⁺ preference is only about fivefold across the whole La-Lu series [@mattocks2023enhanced]; the famous 10⁸ figure is Ln³⁺/Ca²⁺ [@cotruvo2018lanmodulin], not Ln/Ln. Best separation performance: \>98 % purity and \>99 % yield on a Dy/Nd mixture in a single column stage with the Hans-LanM R100K variant [@mattocks2023enhanced]. The original immobilized-LanM column reaches 99.9 % purity on both halves of a 50:50 Dy/Nd feed, but recovers only \~76 % of each element [@dong2021bridging] | Real and characterised: a Powder River Basin coal fly ash leachate at 0.043 mol % REE — \~150 µM total REE against millimolar Na, Mg, Al, Ca and Sr — taken to 88.2 mol % purity in a single column run [@dong2021bridging]; e-waste as sole REE source for engineered *M. extorquens* [@good2024scalable] | Adsorption pH 3, desorption pH \<1.7 (binding halved at pH 2.2, insignificant at ≤1.7); protein stable to pH 2.5 and 95 °C; synthetic feeds 0.2 mM Nd, fly ash leachate \~150 µM total REE; temperature not reported | Bench. Columns of 0.80-1.0 mL bed volume at 0.5 mL/min, largest run 29.1 bed volumes of leachate through 0.94 mL of resin, ten adsorption/desorption cycles without capacity loss [@dong2021bridging]; largest biological figure is a 10 L culture [@good2024scalable]. No continuous or scaled-up operation is reported | 3-4 [^trl-bio] |
| **Membranes, MOFs and emerging** — [](#membranes-mofs-and-emerging-approaches) | **796, Pr/Lu**, and 273, Nd/Er, in a single step on the MOF nanotrap NCU-1 [@hu2024rationally] — the highest β in this book. The same experiment gave 67 for Nd/Dy, which is the pair a magnet recycler faces, and is the number to carry forward. Membranes: no rejection, flux or selectivity value is reported. scCO₂: explicitly cannot separate individual lanthanides | MOFs: synthetic binary solutions, milligram scale, plus one real tailings water at 0.09-0.92 ppm REE. scCO₂: real — roasted and caustic-digested bastnäsite; coal fly ash at 591 mg/kg for Appalachian, 403 for Illinois basin coals [@taggart2016trends] | NCU-1: 1:1 binary lanthanide nitrate solution in water at pH 4.5, where *K*d peaks; it falls away by pH 6, so an acidic leach liquor must be neutralised first [@hu2024rationally]. scCO₂: 34 MPa and 65 °C with TBP-HNO₃ adducts at 2-6 M H⁺ [@sinclair2017rare] | Lab. The 4,000 L reactor is a techno-economic design study [@azimi2025technoeconomic], not a built facility | 2-3 MOFs / 4-5 scCO₂ [^trl-mof] |

*TRL = Technology Readiness Level (1-9 scale). β = separation factor.*

[^trl-sx]: Full commercial deployment: solvent extraction produces essentially
    all separated rare earth oxide sold today, at plant scale, continuously.

[^trl-ix]: Commercial, but as a polishing step rather than a bulk route.
    Pilot-plant separations were demonstrated in 1947 [@spedding1947separation]
    and the method has been in industrial use for high-purity oxides since.

[^trl-leach]: Commercial for every ore type in the chapter, the Indian
    monazite circuit included. Bioleaching within the same chapter is
    explicitly "laboratory and pilot scale, not yet industrial implementation".

[^trl-iac]: Two different technologies share the chapter. In-situ ammonium- or
    magnesium-sulfate leaching is commercial and dominant. Using the clay itself
    as a chromatographic separation medium has no engineered demonstration at
    all — the chapter's own proof of concept is the orebody, and it lists
    measured separation factors on clay as an open research question — so it
    sits at concept stage.

[^trl-pyro]: Carbochlorination is described as practiced at pilot-to-commercial
    scale at Baotou, which supports 7-8 in China; outside China the chapter
    reports pilot demonstration only, hence 6-7. Ch. 7 states both numbers in
    different places. **Flash Joule heating with chlorination** is a special
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
    the same 4-5. Nanofiltration and ultrafiltration for REE separation carry no
    reported rejection or flux in this book and cannot be assigned a TRL at all.

[^trl-precip]: Oxalate and carbonate precipitation and oxidative cerium removal
    are unit operations inside commercial flowsheets. The reverse-size-selective
    ligands in the second half of the chapter are, in the chapter's own words,
    at proof-of-concept scale.

[^trl-bio]: Bench columns and a 10 L culture. Ch. 11's own summary table
    assigns "pilot" and even "industrial" scalability to several entries, but no
    demonstration in the chapter supports those labels, and the chapter
    elsewhere states that commercial breakthroughs have been limited.

[^trl-mof]: The MOF nanotrap result is a single study on synthetic feed at
    milligram scale with no capacity, kinetic, cycling or real-feed data — a
    striking laboratory measurement, not a process. Supercritical CO₂ extraction
    has repeated bench-scale batch demonstrations on real solids, which supports
    4-5; the 4,000 L facility exists only as a techno-economic analysis.
