---
title: Membranes, MOFs, and Emerging Approaches
---

(membranes-mofs-and-emerging-approaches)=
# Membranes, MOFs, and Emerging Approaches

This chapter is a survey of the approaches that do not yet have chapters of
their own: membranes, {index}`metal-organic frameworks <metal-organic framework (MOF)>`, supramolecular hosts, flash
Joule heating, {index}`diglycolamide` ligands, and supercritical CO₂. They have little in
common as chemistry. What they share is a position on the development curve —
most sit between TRL 3 and TRL 7, with laboratory results that are genuinely
striking and scale-up records that are thin or absent.

Read them with that asymmetry in mind. MOF nanotraps reporting separation
factors of 270–800 are doing something conventional extractants cannot
approach; they are also being measured on synthetic feeds at milligram scale.
The gap between those two statements is where most of the remaining work lies,
and the chapters that follow on process economics
([](#environment-techno-economics-and-life-cycle)) and industrial status
([](#the-industrial-landscape)) are the place to calibrate expectations.

{index}`Microfluidic <microfluidics>` separation belongs to the same family of
emerging approaches, but it has grown enough to warrant its own chapter and is
treated there rather than here — [](#microfluidic-separations).

(membrane-separation-technologies)=
## Membrane Separation Technologies

Two quite different things travel under the word "membrane" in this literature,
and the chapter is unreadable if they are not kept apart.

The first is the **liquid membrane**, in which a thin barrier is impregnated
with, or holds in place, an organic phase containing exactly the extractants of
[](#solvent-extraction-fundamentals). Here the membrane does no chemistry at
all. It is a piece of geometry: it holds the organic phase still so that the
aqueous feed sits on one face and the aqueous strip liquor on the other, which
means extraction and stripping proceed at the same time across a single unit
instead of in two banks of contactors [@kaczorowska2023latest]. The selectivity
is the carrier's selectivity, no better and no worse.

The second is the **pressure-driven filtration membrane** — nanofiltration (NF,
pores below about 2 nm) and ultrafiltration (UF, 2–50 nm) — where separation
comes from size and from charge, and the mechanism has nothing to do with
coordination chemistry. Microfiltration is too open to reject a hydrated REE³⁺
ion at all, and appears in these flowsheets only as pretreatment
[@bashiri2022rare]. Solid-phase variants — {index}`polymer inclusion membranes <polymer inclusion membranes>` (PIMs),
which hold the carrier and a plasticiser inside a polymer network, and molecular
or ion-imprinted membranes — sit between the two families, trading transport
rate for a membrane that does not bleed [@kaczorowska2023latest;
@kujawa2023membrane].

Both families are widely reviewed as green alternatives to hydrometallurgy,
because both cut the organic inventory and the wastewater volumes that
[](#hydrometallurgical-leaching) is full of [@bashiri2022rare; @chen2018overview].
Neither has displaced a mixer-settler cascade. The reasons are specific, they
are known, and they are set out at the end of this section rather than left
implicit.

(liquid-membranes-the-cascade-folded-into-one-barrier)=
### Liquid Membranes: The Cascade Folded into One Barrier

The carrier chemistry is the chemistry of chapter 3. The workhorse carriers are
the same acidic organophosphorus extractants — {index}`D2EHPA` and PC88A
(equivalently EHEHPA or P507) — operating by the same cation-exchange
equilibrium, three extractant dimers per REE³⁺, with the same steep dependence
of the distribution ratio on pH ([](#solvent-extraction-fundamentals)). Anything
chapter 3 says about extractant loading, third-phase formation, or the
competition from Fe(III) applies here unchanged.

What the membrane adds is that all three steps happen at once. Ions are
extracted into the immobilised organic phase at the feed face, diffuse across
it, and are stripped into the receiving phase at the far face, in one
simultaneous three-stage process [@kaczorowska2023latest]. In the hollow-fibre
form ({index}`HFSLM <supported liquid membrane (SLM)>`) the feed is pumped through the lumen of a bundle of
microporous fibres while the strip solution flows on the shell side; the organic
phase is held in the fibre-wall pores by capillary forces. This gives a far
higher interfacial area per unit volume than a flat sheet, and faster transport
[@kaczorowska2023latest].

The consequence worth stating plainly is that the driving force is not the REE
concentration difference. Transport is driven by the proton gradient between the
acidic strip liquor and the less acidic feed, and by the relative affinity of
each cation for the carrier [@middleton2023separation]. Because the gradient
that does the work is a pH gradient, the metal can be pumped *up* its own
concentration gradient: the strip liquor can end up more concentrated in REE
than the feed it came from. That is the property no equilibrium contactor has,
and it is why these systems keep being proposed for dilute feeds — ion-adsorption
clay liquors ([](#ion-adsorption-clays)), acid mine drainage, ash leachates —
where a mixer-settler would need enormous phase volumes to do anything useful.

#### What Has Actually Been Demonstrated

The largest reported REE liquid-membrane operation is a pilot at KTH using a
hollow-fibre module with **8 m² of mass-transfer area**, 10 vol% D2EHPA in
kerosene as the membrane phase and 3 M HCl as the strip, on synthetic feeds of
1–22 mM total REE at pH 1.5–3.2 based on an apatite-concentrate recovery process
[@alemrajabi2022separation]. Three configurations were compared: conventional
HFSLM, hollow-fibre renewal liquid membrane (HFRLM, in which organic is also
dispersed in the strip and continuously re-wets the support), and emulsion
pertraction (EPT). The liquid membrane was more selective toward the heavy
lanthanides at lower pH and higher REE loading. HFRLM gave the higher transport
rate; plain HFSLM gave the higher selectivity between individual rare earths.
This is the only result in this chapter that has been carried to a scale where
engineering problems are visible, and what it made visible was a failure mode —
see below.

For magnet recycling, dysprosium has been recovered from the nitric-acid leach
liquor of hard-disk-drive NdFeB scrap at **better than 97% purity and about 94%
recovery**, using 0.5 M EHEHPA in a hollow-fibre contactor operated in
non-dispersive mode, at a 1:1 phase ratio and 100 mL/min [@yadav2018ndfeb]. The
distinction matters: this is non-dispersive solvent extraction across a
membrane contactor, where the organic phase flows and the membrane merely pins
the interface, not a true supported liquid membrane with a static impregnated
carrier. It has the mass-transfer advantages of the membrane geometry without
the carrier-retention problem, and it is the configuration closest to industrial
practice.

Bench-scale work fills in the shape of the technology. D2EHPA HFSLMs recover Nd,
Pr and Dy simultaneously from waste-magnet leach liquor, transporting them in
the order Nd > Pr > Dy — which is an ordering, not a separation
[@kaczorowska2023latest]. And the most-quoted single-element result is worth
reading in full: HFSLM transport of Nd(III) reaching **99.80% extraction** but
only **78.58% stripping** into the receiving phase [@mohdee2023applicability].
The second number is the one that governs a process, and the gap between the two
is metal sitting in the membrane rather than in the product.

### Nanofiltration and Ultrafiltration

NF and UF reject a rare earth for being trivalent and hydrated, not for being a
rare earth. Rejection therefore comes from Donnan exclusion at a charged
membrane surface, from dielectric exclusion, and from size — and can be raised
sharply by binding the metal into a bulkier or oppositely charged complex before
it reaches the membrane [@feng2026selective; @bashiri2022rare].

The numbers are good and they are all group numbers:

| System | Conditions | Result | Source |
|--------|-----------|--------|--------|
| NF-300, Nd(III) | with SDS / with EDTA in feed | rejection rises from 86.7% to **99.5%** / **99.4%** | [@murthy2011application] |
| Desal G10, Gd(III) | 4 bar, pH 1–3, ±0.3 mM DTPA | **<10%** without DTPA; **5–95%** with it, tracking complex formation | [@sorin2005rejection] |
| NF270, acid mine drainage | H₂SO₄, pH 1.5–3.0 | high rejection of Ca, Al, Zn and the REEs while the acid permeates | [@lopez2018application] |
| UP020 UF (20 kDa), micellar-enhanced | pH 3.5, 3 bar, 8 mM SDS | **97%** REE rejection on synthetic leachate, **71%** on the real one | [@kosemutlu2020separation] |
| 30 kDa UF, polymer-enhanced | pH 8–9, 30 mg/L polyacrylic acid | **>90%** REE retention | [@duan2015removal] |
| Ceramic UF (1 kDa), micellar-enhanced | 30 mg/L Y, 2 mg/L Zn, WEEE effluent | **~99%** removal — of Y *and* of Zn | [@innocenzi2018treatment] |

Read the last two rows together with the third. The Gd result says the rejection
is a property of the complex, not of the element: the same membrane rejects the
same ion anywhere between 5% and 95% depending only on how much DTPA is in the
feed. The WEEE result says the process does not distinguish a rare earth from a
base metal. And the UP020 result says what happens when a method tuned on
synthetic solution meets a real leachate: 97% becomes 71%.

Flux and pressure are modest by desalination standards and have been mapped
properly only once for a real REE feed. For coal fly ash leachate, NF rejection
of six critical REEs and permeate flux were mapped over 12–24 bar and pH 1.5–3.5
by response-surface methodology and fed into a cost model; the economic optimum
was the *low*-pressure corner, 12 bar and pH 3.5, because the extra flux bought
at 24 bar did not pay for the energy [@kosemutlu2018application]. Acid stability
is the other design constraint: NF270 exposed to 1 M H₂SO₄ for four weeks
changes measurably in surface chemistry and morphology, which is the relevant
time scale when the feed is a sulphuric leach liquor [@lopez2018application].

No nanofiltration or ultrafiltration membrane has separated adjacent
lanthanides. Poor adjacent-REE selectivity heads the list of open problems in
the most recent review of the field, alongside fouling, loss of performance at
high salinity, chemical instability, and the gap between model and real feeds
[@feng2026selective]. NF/UF belongs in an REE flowsheet as a concentration and
impurity-rejection step ahead of a separation, not as the separation.

### Electrodialysis
Recent research has explored electrodialysis for REE separation, using adjacent anion exchange membranes with chelating agents like EDTA. Mathematical models based on the Nernst-Planck equation have been developed to optimize Dy separation from Pr/Nd mixtures [@ding2024mathematical].

### Why Membranes Have Not Displaced the Cascade

Supported liquid membranes have been proposed as a replacement for
countercurrent solvent extraction for forty years, and the review literature has
repeated the promise for most of that time. The reasons they have not arrived
are not mysterious. The most recent review of REE liquid membranes states the
verdict in one line: the technology has not been implemented industrially mainly
because of membrane instability, difficulty of scale-up, and the short lifetime
of the membrane module [@kaczorowska2023latest]. Each of those has a mechanism.

**Carrier loss.** The immobilised organic phase is not immobilised. D2EHPA and
PC88A have an aqueous solubility of roughly 5–10 ppm
([](#solvent-extraction-fundamentals)), and both the feed and the strip stream
are aqueous phases in continuous contact with the membrane. In a mixer-settler
that solubility is a rounding error, because the plant holds cubic metres of
organic and recycles it; the makeup is a fraction of a percent per cycle. In a
supported liquid membrane the entire carrier inventory is the few millilitres
held in the pores of the support, so the same ppm-level solubility empties the
membrane. Add the other mechanisms catalogued in the standard review of SLM
instability — emulsification of the organic phase at the pore mouths, pressure
differences pushing liquid out of the pores, progressive wetting of the support
by the aqueous phase — and the result is a barrier whose composition changes
while it runs [@kemperman1996stability].

**Lifetime.** The pilot makes this concrete rather than theoretical. In the 8 m²
module, the HFSLM configuration's performance *decayed rapidly with time*, while
the renewal-membrane and emulsion-pertraction configurations, which continuously
resupply organic to the support, stayed comparatively stable
[@alemrajabi2022separation]. A second, chemically specific failure appeared in
the same work: above an organic loading of about 46% for Nd, 38% for Y, 46% for
Dy and 65% for Er, the loaded organic phase forms a gel — the third-phase
problem of [](#solvent-extraction-fundamentals), except that in a cascade the
third phase is drained from a settler, while in a membrane it plugs the pores it
formed in. The practical lifetime under load is measured in hours and days.
Mixer-settler circuits run for years.

**Real leachates.** The feeds in [](#hydrometallurgical-leaching) are not the
synthetic solutions these systems are optimised on. The clearest measurement of
what that costs is for Nd and Er transport across a D2EHPA membrane from
solutions matching coal-ash and acid-mine-drainage leachates: the permeability
of both metals is most sensitive to Fe(III), and the threshold Fe(III)
concentration that degrades REE permeability is **more than a hundred times
lower** than the concentration of Al(III) or Fe(II) needed to do the same
damage [@middleton2023separation]. It is worth being precise about the mechanism,
because "fouling" is the usual and wrong shorthand: in that study excess Fe(III)
produced *no* observable fouling layer. The iron simply outcompetes the rare
earths for the carrier, exactly as it does in a mixer-settler
([](#solvent-extraction-fundamentals)) — only here there is no way to bleed and
regenerate the loaded organic. Genuine fouling by particulates and organics is a
separate and well-documented problem for the pressure-driven membranes
[@feng2026selective], and any real leachate needs microfiltration in front of
them [@kosemutlu2018application].

**And the selectivity was never the point.** Even a perfectly stable supported
liquid membrane inherits the separation factor of its carrier — β ≈ 2–4 for
adjacent light lanthanide pairs with D2EHPA ([](#solvent-extraction-fundamentals)).
The membrane collapses extraction and stripping into one unit; it does not
collapse the *stage count*, which is set by thermodynamics and remains in the
tens to hundreds. A high-purity separation therefore still needs a cascade — now
a cascade of modules, each one a barrier whose carrier is draining into the
process streams. That is the argument in one sentence: liquid membranes solve
the contactor problem, which was never the expensive part, and leave the stage
problem, which is.

Where the technology is genuinely competitive is the case the cascade handles
badly: a single group separation from a dilute, dirty feed, run against the
concentration gradient. The Dy-from-magnet-scrap result above is that case, and
so are the ash and mine-drainage applications. That is a real and useful niche.
It is not a replacement for the cascade, and the chapter should not be read as
promising one.

(metal-organic-framework-mof-nanotraps)=
## Metal-Organic Framework (MOF) Nanotraps
A breakthrough approach using rationally designed MOF structures has demonstrated remarkable selectivity [@hu2024rationally].

### Key Innovation

- NCU-1: A two-fold interpenetrated MOF with dense uncoordinated carboxyl groups and triazole N atoms
- Creates "nanotraps" highly responsive to rare-earth ionic radius variations

### Performance

- **Pr/Lu {index}`separation factor`: 796**
- **Nd/Er separation factor: 273**
- Achieves high separation in a **single step**

## Supramolecular Chemistry Approaches
Supramolecular strategies amplify small property differences across the lanthanide series to achieve selective separation [@oconnelldanes2022selective].

### Triamidoarene Platform
- Selective {index}`precipitation` of light REE nitratometalates as supramolecular capsules
- Works under acidic, biphasic conditions
- Near-quantitative recovery of Nd/Pr directly from magnet scrap without pH adjustment
- Receptor can be recycled for further use

### M₄L₄ Tetrahedral Cages
Self-assembled metal-organic cages exhibit high-precision metal ion self-sorting, enabling selective assembly across the lanthanide series [@li2018supramolecular].

## Brief Overview of Bioseparation
Bioseparation technologies offer high selectivity with minimal environmental impact, and are treated in full in [](#biological-and-biomimetic-separations). In outline:

- **{index}`Lanmodulin <lanmodulin>` proteins**: about 10⁸-fold selectivity for lanthanides
  *over calcium* — a group separation, not an intra-series one. The protein binds
  every lanthanide from La to Lu at nearly the same picomolar affinity, so its
  discrimination *between* rare earths is weak; the two numbers differ by seven
  orders of magnitude and must not be quoted interchangeably. Engineered dimeric
  variants do fractionate the series, but the affinity ratios usually cited for
  them are for La against Dy — opposite ends of the series — not for an adjacent
  pair. [](#biological-and-biomimetic-separations) gives both numbers and the
  demonstrated single-stage purities.
- **Lanthanide binding peptides**: Interfacial separation at air-water interfaces
- **Biosurfactants**: Rhamnolipid complexation with REEs
- **Microbial {index}`biosorption`**: Bacteria, yeast, and algae for REE recovery
- **Phytomining**: Hyperaccumulator ferns for sustainable extraction

## Flash Joule Heating with Chlorination (FJH-Cl₂)
A 2025 result combines {index}`flash Joule heating` with {index}`chlorination` to recover rare earths from **waste magnets**, exploiting the differences in free energy of formation and boiling point among the metal chlorides [@xu2025sustainable]. The chemistry is chlorination, so the full treatment sits in [](#flash-joule-heating-with-chlorination); the reported performance is repeated here for comparison against the other technologies in this chapter.

Two of the figures below are laboratory measurements and the rest are not. The
purity and yield were measured on the demonstration; the reductions in energy,
emissions, cost, water and acid are outputs of a life-cycle assessment and
techno-economic analysis comparing a modelled FJH-Cl₂ process against
conventional routes, not plant data [@xu2025sustainable]. The "100%
elimination of water and acid" applies to the chlorination step itself, and does
not carry the downstream separation of the mixed chloride product, which still
has to happen somewhere.

**Reported performance vs. traditional hydrometallurgy:**

*Measured on the demonstration:*

- REE purity: **\>90%**
- REE yield: **\>90%** in a single step

*Modelled (LCA/TEA), against a conventional route:*

- Energy consumption reduction: **87%**
- Greenhouse gas emission reduction: **84%**
- Operating cost reduction: **54%**
- Water and acid use: **100% elimination** — for the chlorination step alone

## Water-Based Recycling (2025)
Researchers at IOCB Prague developed a novel aqueous recycling method ([Metal Tech News](https://www.metaltechnews.com/story/2025/07/09/tech-bytes/water-based-rare-earth-recycling-emerges/2367.html)):

- Uses only water and a specially designed chelating molecule
- Bypasses hazardous acids, organic solvents, and high-temperature treatments
- Achieves separation factors comparable to industrial {index}`solvent extraction`
- Selectively binds {index}`neodymium`, causing precipitation while {index}`dysprosium` remains dissolved

## DGA Ligand Technology
Developed by Oak Ridge National Laboratory and Idaho National Laboratory ([ORNL](https://www.ornl.gov/news/game-changing-rare-earth-elements-separation-technology-licensed-marshallton)):

- Diglycolamide (DGA) extractants offer improved selectivity
- Reduces chemical consumption and waste production
- Fewer separation stages required, reducing capital costs
- Licensed to Marshallton for commercialization

## CSEREOX Method
Chemical Separation of Rare-Earth Element Oxalates (CSEREOX):

- Exploits different solubilities when REEs react with oxalate and organic base
- LREEs precipitate first due to lower solubility
- Operates at neutral pH
- More environmentally friendly than acidic processes

## Supercritical Fluid Extraction (SFE)
Supercritical fluid extraction using carbon dioxide (sc-CO₂) offers an environmentally benign alternative to conventional hydrometallurgical processes, eliminating organic solvents and aqueous acid waste streams while achieving high extraction efficiencies.

### Fundamentals and Principles
Supercritical CO₂ (critical point: 31.1°C, 7.38 MPa) is an attractive solvent for REE extraction due to its unique properties [@lin1994supercritical]:

**Requirements for Metal Dissolution in sc-CO₂:**

1.  **Charge neutralization**: Metal ions must be rendered electrically neutral
2.  **Coordinative saturation**: Metal must be coordinatively satisfied
3.  **Lipophilicity**: Resulting metal-ligand complex must be nonpolar

Direct extraction of charged REE³⁺ ions by sc-CO₂ is inefficient because CO₂ is a weak Lewis base. Therefore, chelating agents are dissolved in the supercritical phase to form CO₂-soluble metal complexes.

**Process Parameters:**

| Parameter | Typical Range | Optimal Conditions |
| ----------- | -------------- | ------------------- |
| Temperature | 40-100°C | 60-65°C |
| Pressure | 10-40 MPa | 20-34 MPa |
| Extraction time | 30-180 min | 90-120 min |
| CO₂ density | 0.4-0.9 g/mL | Tunable |

### Chelating Agents and Extractant Systems
Several extractant systems have been developed for REE extraction in sc-CO₂ ([OSTI 1995](https://www.osti.gov/biblio/7243167)):

**{index}`TBP <TBP (tributyl phosphate)>`-HNO₃ Adduct System:** The tributyl phosphate-nitric acid system is the most extensively studied ([INL 2017](https://inldigitallibrary.inl.gov/sites/sti/sti/Sort_7228.pdf)):

- Nitrate anions bond with Ln³⁺ to form nitrate salts
- TBP molecules substitute coordinated water
- Forms CO₂-soluble Ln(NO₃)₃·nTBP complexes
- Optimal H⁺ concentration: \~4 mol/L
- Fastest extraction kinetics among tested systems

**Fluorinated β-Diketones:**

- Hexafluoroacetylacetone (HFA, pKa = 4.4)
- Thenoyltrifluoroacetone (TTA)
- 2,2-dimethyl-6,6,7,7,8,8,8-heptafluoro-3,5-octanedione (FOD)
- Exhibit strong synergistic effect with TBP
- Quantitative extraction (92-98%) from solid matrices at 60°C, 150 atm

**Synergistic TBP-β-Diketone Systems:**

| Extractant Combination | Conditions | REE Recovery |
| ---------------------- | ------------ | -------------- |
| TBP + TTA (2.7:3.2 mol%) | 65°C, 20 MPa | 88% Am, 69% Pu |
| TBP + HFA (5.3:6.8 mol%) | 95°C, 26 MPa | 95% Am, 83% Pu |
| TBP-HNO₃ (4M H⁺) | 65°C, 34 MPa | \>99% REE |

**Fluorinated Organophosphates:** Recent advances in fluorinated tributyl phosphate derivatives (TFPs) show enhanced CO₂ solubility [@deng2024maximized]:

- TFPC4 solubility: 8.82 mmol/mol CO₂
- Compared to CMPO: 5.41 mmol/mol CO₂
- Compared to DIDPA: 2.49 mmol/mol CO₂

**Crown Ethers and Calixarenes:**

- DC18C6 (dicyclohexano-18-crown-6) for Cs/Sr separation
- Calixarene-crown ethers for selective Cs extraction
- Research ongoing for REE applications

### Ore Processing Applications
**{index}`Bastnäsite <bastnäsite>` Extraction:** Pretreatment is essential for efficient REE dissolution [@sinclair2017rare]:

*Roasted Bastnäsite (500°C calcination):*

| Element | 60 min | 90 min | 120 min |
| --------- | -------- | -------- | --------- |
| La | 48% | 62% | 72% |
| Ce | 78% | 89% | 96% |
| Pr | 68% | 80% | 88% |
| Nd | 72% | 83% | 90% |

*NaOH-Digested Bastnäsite (caustic cracking):*

| Element | 60 min | 90 min | 120 min |
| --------- | -------- | -------- | --------- |
| La | 81% | 93% | 97% |
| Ce | 94% | 100% | 100% |
| Pr | 91% | 99% | 100% |
| Nd | 93% | 101% | 101% |

The NaOH digestion route achieves near-complete extraction in shorter times due to:

- Conversion of fluorocarbonates to hydroxides
- Enhanced REE accessibility to chelating agents
- Removal of CO₂ and fluorine barriers

**Zircon-Rich Ore Processing:** Canadian ore concentrate containing REEs in zircon matrix [@li2024optimization]:

- NaOH cracking pretreatment essential
- Near-complete REE extraction achieved
- Superior selectivity over gangue elements vs. acid leaching

### Secondary Source Processing
**Coal Ash Extraction:** Coal ash contains 270-1480 ppm REEs and represents a significant secondary resource ([U. Alaska Fairbanks 2024](https://scholarworks.alaska.edu/handle/11122/15693)):

- Anthracite, bituminous, sub-bituminous ash all amenable
- Concentration factor increased to 3.23 ± 0.30 vs. acid leaching
- Enhanced selectivity of REEs over impurities

**Coal Byproducts (2025):** Research on coal-related materials demonstrates feasibility [@veerla2025investigation]:

- Chelation mechanism with synthesized organic solvents
- TBP + HNO₃ extractants in sc-CO₂
- Green alternative to traditional methods

**Fluorescent Lamp Phosphors:** Waste fluorescent lamp luminescent materials ([ResearchGate 2011](https://www.researchgate.net/publication/223476971)):

- Y and Eu extraction \>99% after 120 min
- 15 MPa, 333 K (60°C)
- TBP·(HNO₃)x·(H₂O)y complexes

**Acid Mine Drainage:** AMD from anthracite coal regions [@song2021extraction]:

- Coagulation + complexation approach
- Selective REE extraction demonstrated
- Wastewater remediation co-benefit

### Selectivity and Separation Factors
**Lanthanide Size Effects:** Higher extraction rates are observed for heavier REEs due to smaller ionic radii:

- Nd extraction 30-100% faster than La
- This trend enables some inherent fractionation
- Heavy REEs preferentially extracted

**Selectivity Over Impurities:**

| Matrix | REE Selectivity | Concentration Factor |
| -------- | ---------------- | --------------------- |
| Coal fly ash | Superior to acid leaching | 3.23× |
| Bastnäsite | Excellent over Fe, Ca, Al | \>10× |
| AMD precipitates | Good vs. base metals | Variable |

**Individual REE Separation:** Achieving high separation factors between individual lanthanides remains challenging due to their chemical similarity. Current approaches:

- Multi-stage extraction with optimized conditions
- Temperature/pressure gradient fractionation
- Sequential extraction with different chelating agents

### Green Chemistry Approaches
**Citric Acid-Based Extraction:** Sandia National Laboratory developed an ultra-green approach ([Sandia 2024](https://ip.sandia.gov/opportunity/green-extraction-of-rare-earth-elements-from-coal-waste/)):

- Uses only water, sc-CO₂, and food-grade citric acid
- Thermodynamic and DFT modeling guided development
- 42% extraction efficiency achieved
- Preferential extraction of critical REEs
- No hazardous reagents required

**Environmental Benefits of SFE:**

| Aspect | SFE | Conventional Hydromet |
| -------- | ----- | ---------------------- |
| Organic solvent use | None | High |
| Aqueous acid waste | Minimal | Large volumes |
| CO₂ recyclability | \>95% | N/A |
| Process footprint | Compact | Large |
| Temperature | Moderate (40-100°C) | Variable |

### Process Engineering and Scale-Up
**Reactor Configurations:**

- Batch extraction vessels (lab to pilot scale)
- Semi-continuous with CO₂ recirculation
- {index}`Counter-current <countercurrent cascade>` multi-stage extraction

**A design study, not a plant.** The largest number attached to this route is a
technoeconomic analysis of a hypothetical 4,000 L reactor facility in Ontario
[@azimi2025technoeconomic]. Nothing in the table below was measured: the reactor
volume is a design choice, the costs are modelled from it, and the recovery and
purity are the targets the model assumes in order to price the product. They are
useful as a statement of what the route would have to achieve to be worth
building, and they are not evidence that it does.

| Parameter      | Value               | What it is          |
|----------------|---------------------|---------------------|
| Reactor volume | 4000 L              | design basis        |
| CAPEX          | \$13.7-14.6 million | modelled            |
| Year 1 OPEX    | \~\$3 million       | modelled            |
| REE recovery   | \>95%               | assumed target      |
| Purity         | Battery-grade       | assumed target      |

Every supercritical-CO₂ result cited in this chapter is bench-scale, and none of
the sources reports the vessel size it was obtained in. The gap between that and
a 4,000 L reactor is the whole of the scale-up problem, and it is unmeasured.

**Scale-Up Considerations:**

- High-pressure vessel design and safety
- CO₂ compression and recycling systems
- Heat integration for efficiency
- Extractant recovery and regeneration
- Integration with pretreatment operations

### Advantages and Limitations
**Advantages:**

- Eliminates aqueous acid waste streams
- No organic solvent consumption or emissions
- Tunable solvent power via pressure/temperature
- Compact process footprint
- CO₂ is non-toxic, non-flammable, and recyclable
- Lower environmental impact than hydrometallurgy
- High selectivity over gangue elements

**Limitations:**

- High capital cost for pressure equipment
- Limited individual REE separation capability
- Requires solid pretreatment (roasting or caustic cracking)
- Extractant costs for fluorinated ligands
- Scale-up challenges for very large throughputs
- Current technology readiness level: pilot scale

### Comparison with Conventional Methods
| Parameter             | SFE     | Solvent Extraction | Ion Exchange |
|-----------------------|---------|--------------------|--------------|
| REE recovery          | \>95%   | \>99%              | \>99%        |
| Individual separation | Limited | Excellent          | Excellent    |
| Capital cost          | High    | Medium             | Medium-High  |
| Operating cost        | Medium  | Medium             | High         |
| Environmental impact  | Low     | High               | Medium       |
| Waste generation      | Minimal | Large volumes      | Moderate     |
| Technology maturity   | Pilot   | Commercial         | Commercial   |
