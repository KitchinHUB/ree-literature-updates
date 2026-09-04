---
title: Microfluidic Separations
---

(microfluidic-separations)=
# Microfluidic Separations

Shrinking a {index}`solvent extraction` contactor to the width of a human hair changes
the physics of what happens inside it. Surface-to-volume ratio is fixed by the
channel width rather than by agitation — a 50-100 µm channel presents 400-800 cm²
of interface per cm³ of fluid — volumetric mass transfer coefficients rise by one
to two orders of magnitude, and contact time becomes something that can be set to
a fraction of a second rather than estimated over twenty minutes. The measured
consequence is extraction in seconds where conventional
{index}`mixer-settlers <mixer-settler>` need tens of minutes.

The more interesting consequence is that it opens a separation mechanism that
bulk processing cannot use. Conventional solvent extraction runs to equilibrium,
so it can only exploit *thermodynamic* differences between lanthanides — and
those differences are small, which is the whole problem
([](#why-rare-earths-are-hard-to-separate)). A microfluidic contactor can be
stopped short of equilibrium at a precisely controlled point, which means it can
exploit *kinetic* differences instead. Where two lanthanides approach
equilibrium at different rates, a contact time can be chosen at which they are
maximally separated even though their equilibrium {index}`distribution ratios <distribution ratio>` are nearly
identical.

Set against this is the scale problem, and it is severe. {index}`Microfluidics <microfluidics>` does not
scale up, it numbers up: throughput comes from running more channels, not bigger
ones. The best pilot demonstration in the literature is a three-stage
counter-current chip train numbered up 100-fold without loss of extraction
efficiency — a laboratory device multiplied by a hundred, against the
50,000–100,000 tonnes of concentrate a year an industrial separation plant
handles. Closing that gap requires several further orders of magnitude of
parallelization. That is the honest headline of this chapter: the science is demonstrated and the
engineering economics are not.

Three of the internal reviews this book was assembled from
([](#appendix-a-source-provenance)) covered microfluidics, and where they
disagree on a number the disagreement is noted below rather than averaged.

:::{warning} Citation reliability in this chapter
One of those three carried an explicit unresolved
warning from its author that references without a URL might be fabricated. Its
citations went through the verification pipeline described in the prologue, and
the ones that failed were deleted — but the base rate of trouble in this
material was higher than elsewhere in the book. Check the primary source before
relying on any specific number here.
:::

## Why Microfluidics Changes the Problem

Microfluidic technology represents a transformative approach to REE separation, offering precise control, enhanced mass transfer, and significant process intensification. This section provides a comprehensive overview of microfluidic approaches for rare earth separation.

### Fundamentals and Advantages
Microfluidic liquid-phase extraction miniaturizes traditional liquid-liquid extraction within microchannels (typically tens of µm cross-section), offering several key advantages [@song2025mine]:

**Core Benefits:**

- **High surface-to-volume ratio**: Dramatically increases mass transfer rates
- **Precise flow control**: Sub-second contact time resolution
- **Low reagent consumption**: Minimizes chemical waste
- **Rapid testing**: Enables high-throughput reagent screening
- **Process intensification**: 2-3× higher extraction rates than conventional methods

**Performance Metrics:**

| Parameter | Microfluidic | Conventional Mixer-Settler |
| ----------- | ------------- | --------------------------- |
| Extraction time | 3-60 seconds | 10-25 minutes |
| Extraction rate | 2-3× higher | Baseline |
| Contact time control | Sub-second | Minutes |
| Reagent consumption | Minimal | High |

The two extraction times in that first row are the same rate law evaluated with
two mass transfer coefficients, and [](#fig-09-kinetics) draws it. The second
panel is the part that has no conventional counterpart: a contact time short
enough to stop the extraction before equilibrium is a contact time at which two
lanthanides that share an equilibrium can still be told apart.

## Extraction Architectures

Microfluidic extractors run in the laminar regime (Reynolds number \<2300), and
within it the same two phases can be arranged in the same channel in several
ways [@kolar2016microfluidic; @fernandezmaza2024high; @zhang2019mechanistic;
@zhang2019enabling]. Four arrangements account for most of the REE work, and
they are drawn in [](#fig-09-flow-regimes). They differ in one thing that
matters for extraction: how much liquid-liquid interface the same two phases
present inside the same channel. Each is therefore suited to a different kinetic
regime.

### Co-Laminar (Parallel) Flow

Both phases move as continuous side-by-side streams separated by a single
stable interface across which mass transfer proceeds by diffusion. Reported
linear velocities are modest --- Dessimoz and co-workers worked between zero and
50 mm/s for parallel flow in a 269 µm channel, and found slug flow unstable above
about 20 mm/s, the parallel pattern taking over beyond that
[@dessimoz2008liquid]. Holding the interface in place limits the configuration to
relatively low phase ratios, roughly 5:1 to 1:5. It suits fast-kinetics
extractions: in the Y-Y microchip work on a leached mixed-REO concentrate, the
two phases were contacted for up to 15 seconds with sub-second resolution, and
measured extraction rates ran roughly double those of the corresponding bulk
contact --- which the authors attribute to the higher interfacial area per unit
volume [@kolar2016microfluidic]. The reference measurement of the underlying rate
constants is the plug-based microfluidic study of @nichols2011mechanistic, which
determined interfacial mass transfer rate constants for every lanthanide except
promethium, plus yttrium, under TALSPEAK conditions with rapid mixing and a known
interfacial area --- the two things bulk kinetic methods cannot deliver together.

### Slug (Segmented) Flow

Slug flow creates alternating aqueous and organic segments, which makes slug
length---and with it the specific surface area---a variable the operator sets
[@dessimoz2008liquid]. Internal circulation within each segment adds convective
mixing to diffusion, and reported mass transfer efficiencies are 86.9-94.8%,
enough for small-to-medium scale duties. The regime's practical difficulty is
not contacting but disengagement, and that is where the recent hardware work
sits: an additively manufactured micro-separator whose micro-post array sets up
a capillary pressure gradient on the non-wetting organic phase achieves
continuous, membrane-free, density-independent phase separation of both slug
flow and dispersed droplet flow, with near-complete separation at flow rates up
to 15 mL/min and equilibrium extraction reached within 0.25 s in the upstream
micromixer [@touma2024intensification]. That work is on an isobutanol-water
system rather than on rare earths, but the separator is the component a
numbered-up REE train would need. The same problem is why the Priest group's
early microfluidic circuit was built to carry extraction, stripping and phase
disengagement together rather than contacting alone --- on high-value platinum
chloride solutions, in that case, rather than on rare earths
[@kriel2015microfluidic].

Reactor geometries in this family include serpentine microreactors, rotating
microchannel extractors and 3D reticulated hollow-strut SiC foam microreactors,
the last reaching **98.7% extraction efficiency** for {index}`praseodymium` and
97.0% for {index}`cerium` [@zhang2022solvent].

### Droplet (Micro-Droplet) Flow

Breaking one phase into discrete drops in the other replaces the flat interface
with the surface of every drop, and the shear that forms the drops drives
internal vortexes inside them, which homogenize the concentration field within
each drop; a grooved microchannel that retains drops on this principle also lets
the working phase ratio inside the channel fall well below the injected phase
ratio, which is what raises the extraction efficiency
[@zhou2019controlled]. No enhancement factor against a conventional contactor is
quoted for the droplet regime in the sources cited here; the only such
comparison in this chapter's literature is Dessimoz's, in the performance table
below. Reported mass transfer efficiencies, 92.9-97.4%, are the highest of the
four regimes, and it is the regime reported for high-selectivity separation of
trace REEs.

The REE case reported in most detail is a flow-focusing droplet microreactor
run on a binary Dy-La system, with the aqueous REE solution dispersed as
monodisperse droplets in a continuous organic phase of Cyanex 572 in Shellsol
D70 [@fernandezmaza2024high]. Residence times of 3-60 seconds produced droplets
presenting 49.2-61.4 cm²/cm³ of interfacial area; at pH 1, 90% of the
{index}`dysprosium` was extracted and the two elements were separated almost
completely, at a reported {index}`separation factor <separation factor>` of
**279**.

Two variants extend the regime to dilute feeds. Hollow droplets introduce a gas
phase (gas-in-oil-in-water) so that a thin organic shell contacts a large
aqueous volume: working at a phase ratio of 200:1 with P507, this configuration
concentrates neodymium from a dilute waste water into a product of the order of
grams per litre in a single pass [@chen2017fast]; the paper is paywalled with no
released abstract, so no numeric enrichment factor is quoted here.
Snowman-shaped magnetic
Janus nanoparticles added as emulsifiers disperse the extractant uniformly, hold
their emulsification performance over three or more cycles, and allow rapid
magnetic demulsification in under 3 minutes---a route to enriching
low-concentration REE streams [@chen2022efficient].

### Pore-Throat Microchannels

A sequential pore-throat geometry---a serial converging-diverging
channel---creates capillary barriers that retain dispersed droplets and so lower
the apparent aqueous-to-organic volume ratio where mass transfer actually
happens [@ge2024enhanced]. A double pore-throat channel reaches extraction
equilibrium within 30 seconds at phase ratios of 50-250, and a quadruple one
reaches 77% extraction efficiency at an extreme 500:1 phase ratio, concentrating
100 mg/L aqueous feeds into organic solutions of up to 6 g/L.

:::{figure} ../figures/09-flow-regimes.svg
:name: fig-09-flow-regimes
:width: 100%

The four regimes, in the order listed above, with this section's own numbers
beside each. The drawing is schematic — nothing is to scale, and the channel is
deliberately identical in all four so that the only thing changing is what the
two phases do inside it. The coloured line is the liquid-liquid interface, and
following it down the figure is the argument for why the regime matters: one
flat plane in co-laminar flow, the caps of a slug train, then the perimeter of
every drop in a dispersion, which is the order the reported mass transfer
efficiencies follow. What separates the first three is increasing flow rate and
shear; the sources cited for the regime maps [@dessimoz2010quantitative;
@kashid2007hydrodynamics] locate those boundaries, but this chapter quotes no
capillary number or transition velocity, so no threshold is drawn. Pore-throat
is set apart because it is a change of channel geometry rather than of flow
rate. Drawn by `tools/figures/fig_flow_regimes.py`.
:::

## Separation Mechanisms and Extractants

The dominant separation mechanism employs cation exchange extraction using organophosphorus extractants [@xie2014critical]. The fundamental reaction---RE³⁺(aq) + 3(HA)₂(org) → RE(A₂H)₃(org) + 3H⁺(aq)---involves each REE ion extracted in a complex with six extractant molecules arranged as dimers [@jensen2002comparison].

**Table 1: Common Extractants for REE Separation**

| **Extractant** | **Target REEs** | **Key Application** |
|----|----|----|
| D2EHPA | All lanthanides | Most versatile, established |
| Cyanex 572 | Heavy REEs (Er, Tm, Yb, Lu) | 3× faster extraction for Lu, Yb |
| HEHEHP/P507 | Light REEs (La, Ce, Pr, Nd) | Lower acid stripping requirement |
| TODGA | f-element separations | Tridentate ligand, high Ln affinity |

Synergistic extraction systems combining multiple extractants produce non-linear enhancement effects: {index}`TODGA` + {index}`TBP <TBP (tributyl phosphate)>` in the {index}`ionic liquid <ionic liquids>` \[C4mim\]\[Tf2N\] raises extraction and intra-lanthanide selectivity together [@turanov2020solvent]. Studies of DMDOHEMA + {index}`HDEHP` systems reveal that synergy effects are quadratic in mole fraction, attributed to in-plane mixing entropy at bent extractant film interfaces [@elmaangar2020microfluidic]. A related but distinct route makes the ionic liquid itself the extractant: trioctylmethylammonium dioctyl diglycolamate, \[A336\]\[DGA\], dissolved in the fluorine-free ionic liquid diluent \[A336\]\[NO₃\], extracts neodymium and the other lanthanides from nitric acid media more strongly than the molecular acid its anion was prepared from [@rout2014solvent].

Beyond solvent extraction, electrophoretic methods, particularly capillary zone electrophoresis with HIBA buffers, achieve complete separation of **14 lanthanides in under 6 minutes**---though primarily at analytical scale [@yelkenci2017separation]. Electrodialysis with EDTA chelation exploits differential chelation between heavy REEs (preferentially forming chelates) and light REEs (remaining as free cations) to achieve a **Dy/Nd separation factor of 125** with 93% Dy purity [@ding2023separation].

## The Adjacent Lanthanide Challenge

Separating adjacent lanthanides differing by only 0.01-0.02 Å in ionic radius represents the field's hardest problem [@nash1993basic]. For the industrially critical **Nd/Pr separation**, optimized D2EHPA systems at pH 5 in hydrochloric acid achieve separation factors of only 2.72---requiring many stages for high purity [@safarzadeh2018insights]. pH emerges as the dominant variable affecting Nd/Pr selectivity.

The **Dy/Nd separation** critical for permanent magnet recycling has seen dramatic advances through non-conventional approaches. {index}`Lanmodulin <lanmodulin>` protein variants (Hans-LanM R100K) achieve **\>98% purity and \>99% yield in a single stage**---a result unachievable with conventional solvent extraction [@mattocks2023enhanced]. {index}`MOF <metal-organic framework (MOF)>` nanotraps (NCU-1) with carboxyl groups and triazole nitrogen atoms demonstrate **separation factors of 273 for Nd/Er and 796 for Pr/Lu** in single-step separations [@hu2024rationally]. Flow-focusing droplet microreactors reach a Dy/La separation factor of 279 [@fernandezmaza2024high], but Dy and La sit at opposite ends of the series; none of the microfluidic studies cited in this chapter reports a separation factor for an adjacent lanthanide pair.

Microfluidic intensification exploits kinetic rather than equilibrium differences [@zhang2019mechanistic]. For lanthanide pairs with distinguished kinetics (Eu³⁺/La³⁺), extraction proceeds to different degrees before equilibrium is reached. For pairs with similar kinetics (Eu³⁺/Sm³⁺), Damköhler number manipulation via flow rate, concentration, and temperature enables separation through precise control of non-equilibrium conditions---impossible in conventional batch systems [@zhang2019enabling].

## Process Intensification: The Numbers

Quantitative comparisons between microfluidic and conventional solvent extraction
are worth making carefully, because the intensification factor depends on which
channel and which conventional contactor are being compared. The flow-regime
definitions that underlie these measurements are given by
[@dessimoz2010quantitative; @kashid2007hydrodynamics].

**Table 2: Performance Comparison**

| **Parameter** | **Microfluidic** | **Conventional** | **Enhancement** |
|----|----|----|----|
| Mass transfer coefficient (kLa) | 0.2-0.5 s⁻¹, measured for both slug and parallel flow in 269-400 µm rectangular glass channels [@dessimoz2008liquid] | 10⁻³-10⁻² s⁻¹ | **20-500×** |
| Extraction time | 3-60 s residence time [@fernandezmaza2024high] | 10-25 minutes | **10-500×** |
| Surface-to-volume ratio | \~800 cm²/cm³ at 50 µm; \~400 at 100 µm; \~57 at a 0.7 mm capillary | set by drop size and holdup, not quoted on a common basis | geometric, not intrinsic |
| Phase ratio capability | 200:1 demonstrated [@chen2017fast] | Typically \<50:1 | **\~4×** |

*Basis of each row.* Every enhancement figure above is the ratio of the two
columns at their extremes, computed here rather than quoted: 0.2/10⁻² = 20 and
0.5/10⁻³ = 500 for kLa, 600 s/60 s = 10 and 1500 s/3 s = 500 for extraction
time. Three caveats travel with them. The kLa band is not a property of slug flow
in particular: Dessimoz's headline result is that slug and parallel flow give the
*same* volumetric coefficient, the flow pattern changing what the coefficient
depends on rather than how large it is. The conventional kLa is an
order-of-magnitude figure carrying no stated agitation condition, and a
vigorously stirred contactor sits at or above the top of that range, so 500× is
an upper bound rather than a typical value --- Dessimoz's own comparison table
gives ~(1.75-6.3)×10⁻³ s⁻¹ for a spray column but ~0.05-0.3 s⁻¹ for impinging
streams, and the paper claims only "more than one order of magnitude" of
enhancement over conventional contactors. And surface-to-volume is not an
intrinsic property of "microfluidics" at all: for a square channel of side *d* it is simply 4/*d*, so
it must be quoted against a channel size. At the tens-of-µm scale described above
that is several hundred cm²/cm³; at a 0.7 mm capillary, which is what much of the
slug-flow literature actually uses, it is about 57 cm²/cm³ — an order of
magnitude lower, from the same technology. The flow-focusing droplet reactor
that supplies the 279 separation factor quoted above reports 49.2-61.4 cm²/cm³
[@fernandezmaza2024high], which is the capillary end of that range rather than
the tens-of-µm end. No interfacial area for a stirred
dispersion is reported on a comparable basis in the sources cited here, so no
ratio is given for that row.

:::{figure} ../figures/09-kinetics.svg
:name: fig-09-kinetics
:width: 100%

Approach to equilibrium against contact time. **(a)** The first-order model
$E/E_{eq} = 1 - \exp(-k_L a\,t)$, evaluated with the two volumetric mass
transfer coefficients of the table above: 0.2–0.5 s⁻¹, measured for both slug
and parallel flow in 269–400 µm rectangular glass channels
[@dessimoz2008liquid], and the 10⁻³–10⁻² s⁻¹ order-of-magnitude figure quoted
for a conventional contactor.
Neither band is data: the curves are the rate law and the bands are the reported
spread in $k_L a$. The two vertical strips are operating times quoted elsewhere
in the chapter — 3–60 s residence time in a flow-focusing droplet reactor
[@fernandezmaza2024high], 10–25 min in a mixer-settler — and the model
reproduces both without adjustment, reaching 95% of equilibrium at 6–15 s and at
5–50 min respectively. **(b)** Why stopping short can separate what equilibrium
cannot. Two lanthanides with the same equilibrium but different rates are
furthest apart at $t^* = \ln(k_f/k_s)/(k_f - k_s)$ and indistinguishable once
both have finished. The threefold rate ratio drawn here is illustrative: the
chapter names Eu³⁺/La³⁺ as a kinetically distinguished pair but reports no rate
ratio for it, so none is claimed. Drawn by `tools/figures/fig_kinetics.py`.
:::

The table carries no generic separation-factor row, because no generic figure is
supportable: selectivity is a property of an element pair and a chemistry, not of
a contactor. The separation factors reported in this chapter are quoted per pair
and per system instead — 279 for Dy/La in a flow-focusing droplet reactor
[@fernandezmaza2024high], 2.72 for Nd/Pr with D2EHPA at pH 5
[@safarzadeh2018insights] — and none of the microfluidic studies cited here
measured the same pair in a conventional contactor for comparison.

Heavy REE extraction from a leached mixed rare earth oxide concentrate using Cyanex 572 in a Y-Y microchip runs at roughly double the bulk rate, and **3× faster** for Lu and Yb specifically; the phases were contacted for up to 15 seconds, against the minutes to hours of a bulk contact, and selectivity for the heavy fraction was good at pH 0.7 [@kolar2016microfluidic].

## Electrophoretic Microfluidic Separation
Electrophoretic techniques offer exceptional resolution for lanthanide separation on microfluidic platforms:

**{index}`Isotachophoresis <isotachophoresis>` (ITP) on Chip:** ITP can separate up to **14 lanthanides** from a homogeneous sample into elementally pure bands [@pesavento2021versatile]:

- Fused-silica microfluidic device joined to a fused-silica capillary
- Complexing agents: acetate and α-hydroxyisobutyric acid (HIBA)
- Eight lanthanides concentrated within \~6 minutes
- Chip-to-ICP-MS interface enables elemental analysis

**Capillary Zone Electrophoresis (CZE):** Complete separation of all 14 lanthanide ions achieved [@yelkenci2017separation]:

- Buffer: 4.5 mM 2-hydroxyisobutyric acid + 1 mM acetic acid (pH 4.5)
- Separation time: **\<6 minutes**
- Capacitively coupled contactless conductivity detection (C4D), which detects
  the non-UV-active lanthanide ions without a UV-active ligand or a
  visualization agent

**Ligand-Assisted Enhancement:** Iminodiacetic acid (IDA) greatly enhances light/heavy lanthanide separation:

- Tridentate coordination with light lanthanides
- Bidentate coordination with heavy lanthanides
- Significantly improved selectivity

## Scale-Up by Numbering-Up

The most significant pilot-scale achievement comes from the University of South Australia, where Yang and co-workers demonstrated **three-stage {index}`counter-current <countercurrent cascade>` microfluidic solvent extraction numbered up 100-fold without losing extraction efficiency** [@yang2022pilot]. The numbering-up was achieved by building multi-layer glass chips and operating three of them in counter-current or parallel configuration. The paper is behind a paywall with no open copy and no released abstract, so the throughput it reached is not quoted here; the description above is as its authors summarize it in their own later review [@yang2024industry].

Scale-up follows numbering-up rather than geometric scale-up, preserving the microfluidic advantages of enhanced mass transfer [@hessel2013process]. The choice is between *internal* numbering-up, which puts parallel channels inside one device and is the hardware-efficient option, and *external* numbering-up, which replicates whole systems including their pumps and is simpler to implement but multiplies the ancillary equipment. The South Australian chips were run on high-value metals --- platinum as well as rare earths --- rather than on a single model system [@yang2022pilot; @yang2024industry].

However, a substantial gap remains between current demonstrations and industrial requirements. Industrial REE separation typically processes 50,000-100,000 tonnes of concentrates annually, while the published microfluidic demonstrations are laboratory devices numbered up by a factor of a hundred. Even on the most favourable reading the gap is several orders of magnitude of further parallelization, and it is wider still than any such ratio suggests, because one side of it is measured as solid concentrate and the other as dilute liquor.

### Mini-Channel Counter-Current Extractors
For intermediate scale, mini-channel extractors (4-6 mm diameter) bridge the gap between microfluidics and conventional equipment [@he2024intensifying]:

**Design Parameters:**

- Channel length \>250 mm provides \>1 extraction stage
- Guidance for novel extractor design
- Improved REE extraction efficiency

**Novel Continuous Countercurrent Micro-Extractor:** Hydrodynamic characteristics studied for continuous operation, addressing the challenges of:

- Large input/output volumes
- Time delays
- Nonlinear, multivariable behavior

## Reported REE Microfluidic Systems

### Synergic Extraction with XRF Detection

El Maangar et al. (2020) demonstrated a microfluidic technique coupled with X-ray fluorescence for investigating synergic liquid-liquid extraction of rare earth elements [@elmaangar2020microfluidic]:

- Studied combinations of solvating and ionic extractants
- Quantified Gibbs free energies of transfer for five REEs
- Analyzed effects of temperature and surface charge density
- First automated microfluidic tool with online XRF for studying LLE processes

### Cyanex 572 for REE Extraction

Kolar et al. (2016) investigated microfluidic solvent extraction of REEs from a leached mixed rare earth oxide mineral concentrate using Cyanex 572 [@kolar2016microfluidic]:

- Extraction rates typically double that observed in conventional bulk extractions
- Lu and Yb showed three-times faster extraction
- Higher surface-to-volume ratio accounts for faster extraction kinetics

### Lanthanide Extraction Kinetics

Nichols et al. (2011) developed a plug-based microfluidic system to determine absolute interfacial mass transfer rate constants for all lanthanides under TALSPEAK process conditions [@nichols2011mechanistic]:

- Conditions of rapid mixing and controlled interfacial area
- Quantified extraction kinetics for nuclear reprocessing applications
- Enabled mechanistic understanding of extraction chemistries

### Spectroscopic Monitoring

Nelson et al. (2018) demonstrated micro-Raman technology to interrogate two-phase extraction on microfluidic devices [@nelson2018micro]:

- Microfluidic devices provide ideal environments for studying solvent extraction
- Plug flow enables examination of reaction kinetics and interfacial transfer
- Non-invasive spectroscopic monitoring of extraction progress

(detection-colorimetry-fluorescence-and-spectroscopy)=
## Detection: Colorimetry, Fluorescence, and Spectroscopy

### Colorimetric Sensors for Heavy Metals

Idros and Chu (2018) developed a triple-indicator-based multidimensional colorimetric sensing platform [@idros2018triple]:

- Low-cost paper-based microfluidic analytical device (μPAD)
- Detection of mercury, lead, chromium, nickel, copper, and iron ions
- RGB color space analysis using digital imaging
- Portable and disposable monitoring capability

### Fluorescent and Colorimetric Sensors

Kim et al. (2012) provided a comprehensive Chemical Society Reviews article on fluorescent and colorimetric sensors for lead, cadmium, and mercury ions [@kim2012fluorescent]:

- Systematic coverage of sensor mechanisms
- Design principles for selective detection
- Applications in environmental monitoring

### Paper-Based Analytical Devices

Chauhan and Toley (2021) developed barrier-free microfluidic paper analytical devices for multiplex colorimetric detection [@chauhan2021barrier]:

- Stack of paper membranes with different wicking rates
- No need for wax patterning or barriers
- Simultaneous multi-analyte detection capability

### Smartphone-Based Detection

Lopez-Ruiz et al. (2014) demonstrated smartphone-based simultaneous pH and nitrite colorimetric determination [@lopezruiz2014smartphone]:

- Seven sensing areas with immobilized reagents
- Smartphone flash as controlled light source
- HSV color space analysis for quantification
- Customized algorithm for multidetection

## Computer Vision and Machine Learning

### Deep Neural Networks for Droplet Analysis

Hadikhani et al. (2019) presented a non-intrusive method for measuring fluidic properties by optically monitoring droplet flow [@hadikhani2019learning]:

- Neural networks extract information from droplet images
- Published in Scientific Reports
- Demonstrated measurement of flow properties without contact

### Enhanced Image Analysis with Deep Learning

Gelado et al. (2023) investigated deep learning methods for accurate droplet detection and measurement [@gelado2023enhancing]:

- Compared Segment Anything Model (SAM) with Circular Hough Transform
- SAM provides superior detection accuracy
- Reduced droplet diameter measurement error
- Image restoration of low-resolution images

## Device Fabrication and Solvent-Resistant Materials

Standard PDMS devices face solvent compatibility challenges. Several solutions have been developed:

### Perfluoropolyether (PFPE) "Liquid Teflon"

Rolland et al. (2004) reported the first fabrication of solvent-compatible microfluidic devices using photocurable PFPE materials [@rolland2004solvent]:

- Highly fluorinated functionalized perfluoropolyethers
- Remarkable chemical resistance to organic solvents
- Overcomes PDMS swelling limitations

### Hybrid Coatings for PDMS

Kim et al. (2009) developed solvent-resistant PDMS microfluidic devices with hybrid inorganic/organic polymer coatings [@kim2009solvent]:

- HR4 coating provides chemical resistance
- Simple coating procedure
- Compatible with virtually any solvent

## Feedstock Integration

Microfluidic systems have been validated with diverse REE-containing feedstocks beyond synthetic solutions. Processing of **mixed rare earth oxide ore leachates** using Y-Y microchip configurations with Cyanex 572 achieved 2-3× higher extraction rates with contact times of only 15 seconds [@kolar2016microfluidic]. Particulate-laden feeds are the standing difficulty for closed microchannels, whose dimensions are comparable to the particles in a mineral stream, and open-channel designs are the response: an open-microfluidic geometry that creates a dynamic fluidic obstacle outside the channel excludes particles while letting soluble ions enter freely for analysis [@yang2024industry].

**{index}`NdFeB` permanent magnet recycling** represents a high-value near-term application, and the pretreatment matters as much as the contactor. Roasting magnet scrap in air above 500 °C converts the neodymium not to Nd₂O₃ but to the refractory ternary NdFeO₃, which then takes more than a day to dissolve; roasting instead under argon with 5 wt% carbon as an iron reductant avoids that phase, segregates metallic iron from the rare earth phase, and leaves a residue that dissolves completely in the ionic liquid \[Hbet\]\[Tf₂N\] in twenty minutes, at a rare-earth-to-iron ratio some fifty times the ratio in the scrap [@orefice2019selective]. That kind of leachate --- concentrated, low in iron, already in a single phase --- is what a microfluidic contactor downstream would want.

**{index}`Coal fly ash <coal fly ash>`** is a plausible feed on grade alone. Taggart and co-workers measured more than a hundred U.S. ashes and found total REE --- lanthanides plus yttrium and scandium --- averaging 591 mg/kg in ashes from Appalachian coals, against 403 mg/kg for Illinois basin and 337 mg/kg for Powder River basin ashes, with the critical fraction (Nd, Eu, Tb, Dy, Y, Er) at 34-38 % of the total, well above the under-15 % typical of conventional ores [@taggart2016trends]. A microfluidic contactor would sit downstream of a leach, on the pregnant liquor; no such coupling has been demonstrated at the time of writing. Complete "ash-to-oxide" processes achieve enrichment factors exceeding 400× relative to raw fly ash. {index}`Flash Joule heating <flash Joule heating>` ultrafast activation (\~3000°C, \~1 second) increases REE extractability approximately 2× from secondary wastes including coal ash, bauxite residue, and electronic waste at remarkably low energy consumption of 600 kWh/ton (\~\$12/ton) [@deng2022rare].

### Scandium Recovery from Red Mud
A specific application demonstrating microfluidic strategy for rapid Sc extraction from {index}`red mud` (bauxite residue) shows the technology's applicability to industrial waste streams [@feng2025microfluidic].

## Industrial Status and Key Players

**True commercial-scale microfluidic REE separation plants do not yet exist.** The technology remains at research-to-pilot stages. Several companies are commercialising *related* intensified separations, and the figures below come from company announcements rather than from the peer-reviewed literature; treat them as claims, not measurements.

- **IBC Advanced Technologies** offers the most mature related technology, SuperLig® Molecular Recognition Technology (MRT™), a ligand-on-support column chemistry that the company reports separates individual REEs, including adjacent pairs, from spent NdFeB magnets at high recovery and purity.

- **Phoenix Tailings** (Boston) extracts REEs from mine tailings by a route it describes as free of the acids and radioactive waste of conventional processing, and is scaling from tens to hundreds of tonnes per year.

- **REEgen**, a Cornell spinout, uses {index}`bioleaching` with *Gluconobacter oxydans* — the organism behind the biolixiviant work in [](#biological-and-biomimetic-separations) — rather than microfluidic contactors as such.

### Leading Research Groups
**Tsinghua University's State Key Laboratory of Chemical Engineering** leads global research, with Prof. Jianhong Xu's group pioneering hollow droplet extraction and Janus nanoparticle-stabilized systems [@chen2022efficient]. Prof. Yundong Wang's team focuses on continuous REE recovery from wastewater

## The Mine-on-a-Chip Vision

The concept of "mine-on-a-chip" envisions leveraging microfluidics for critical materials recovery [@song2025mine]:

**Opportunities:**

- Materials characterization at microscale
- Reagent screening and optimization
- Process development with minimal material
- Analytical sample preparation
- Rapid separation method development

**Challenges Addressed:**

- Natural REE co-occurrence
- Association with major cations (Ca, Al, Fe)
- Co-existence with radionuclides
- Physicochemical similarity across lanthanide series

## Comparison of Microfluidic Configurations
| Configuration | Mass Transfer | Phase Ratio | Scale | Best Application |
|----|----|----|----|----|
| Co-laminar | Moderate | 1:5 to 5:1 | Lab-Pilot | Bulk waste extraction |
| Slug flow | High (86-95%) | Moderate | Small-Medium | High-efficiency transfer |
| Micro-droplet | Highest (93-97%) | High | Small-Medium | Trace REE separation |
| Pore-throat | High | 50-500:1 | Lab | Ultra-high phase ratio |
| Electrophoretic | Excellent resolution | N/A | Analytical | 14-element separation |

(limitations-and-outlook)=
## Limitations and Outlook

**Challenges:**

- Maintaining stable interfaces at high phase ratios
- Fouling and clogging with real feedstocks
- Integration with upstream/downstream processes
- Cost of precision fabrication at scale

**Future Developments:**

- Machine learning for flow optimization
- 3D-printed microfluidic devices for rapid prototyping
- Integration with online analytics (ICP-MS, etc.)
- Hybrid systems combining multiple flow regimes
- Automated multi-stage counter-current operation

Microfluidic rare earth separation has progressed from fundamental kinetic studies to pilot-scale demonstrations numbered up a hundredfold without loss of extraction efficiency. The technology delivers genuine intensification---volumetric mass transfer coefficients 20-500× those assumed for a conventional contactor, extraction rates 2-3× faster [@kolar2016microfluidic], and, in specific pairs, separation factors far above a single conventional stage (279 for Dy/La in a flow-focusing droplet reactor [@fernandezmaza2024high])---by exploiting kinetic differences between lanthanides under precisely controlled non-equilibrium conditions.

Three key developments will determine commercial trajectory: (1) successful scale-up to industrially relevant throughputs through massive parallelization while maintaining microfluidic advantages; (2) integration of robust on-chip analytics for real-time process control; and (3) demonstration of long-term operational stability with real industrial feedstocks [@wang2017microflow]. Biological separation approaches using lanmodulin proteins achieving \>98% purity in single stages suggest hybrid bio-microfluidic systems may ultimately prove more transformative than incremental improvements to solvent extraction chemistry [@mattocks2023enhanced].

The most promising near-term applications target high-value, low-volume separations---particularly adjacent heavy REE pairs critical for permanent magnets where conventional SX requires dozens of stages. Phoenix Tailings, RETi, and IBC Advanced Technologies are positioning related technologies for commercial deployment, though true microfluidic processing at scale remains 5-10 years away. The fundamental science is proven; the engineering and economics of massive parallelization will determine whether microfluidics transforms REE processing or remains a powerful laboratory tool.

(microfluidic-research-opportunities)=
## Research Opportunities

Based on this literature review, several promising research directions emerge:

### Real-Time Colorimetric Monitoring of REE Extraction
**Concept**: Develop microfluidic devices with integrated colorimetric indicator zones for real-time monitoring of rare earth element extraction efficiency.

**Precedent**:

- Micro-Raman monitoring demonstrated for two-phase extraction [@nelson2018micro]
- Smartphone colorimetric detection established [@lopezruiz2014smartphone]
- REE extraction kinetics characterized via microfluidics [@nichols2011mechanistic]

### Machine Learning-Optimized Extraction Screening
**Concept**: Combine high-throughput droplet generation with computer vision analysis for automated extraction optimization.

**Precedent**:

- Deep learning for droplet detection demonstrated [@hadikhani2019learning; @gelado2023enhancing]
- Droplet-based extraction fundamentals established [@mary2008microfluidic]

### Smartphone-Based Field Detection
**Concept**: Portable microfluidic extraction kit with smartphone colorimetric readout for field applications.

**Precedent**:

- Smartphone platforms demonstrated for multi-analyte detection [@lopezruiz2014smartphone]
- Paper-based colorimetric devices for heavy metals [@idros2018triple; @chauhan2021barrier]
