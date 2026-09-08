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
a fraction of a second rather than estimated over twenty minutes. What that
buys is real and smaller than the arithmetic suggests, and
[](#process-intensification-the-numbers) sets the enhancement factors against
the only two head-to-head comparisons this chapter's literature contains: on a
real rare earth leachate a chip ran about twice the rate of a stirred beaker,
and in a nuclear-reprocessing surrogate it ran four times *slower* than a
stirred cell.

The more interesting consequence is that it opens a separation mechanism that
bulk processing cannot use. Conventional solvent extraction runs to equilibrium,
so it can only exploit *thermodynamic* differences between lanthanides — and
those differences are small, which is the whole problem
([](#why-rare-earths-are-hard-to-separate)). A microfluidic contactor can be
stopped short of equilibrium at a precisely controlled point, which means it can
exploit *kinetic* differences instead. Where two lanthanides approach
equilibrium at different rates, a contact time can be chosen at which they are
maximally separated even though their equilibrium {index}`distribution ratios <distribution ratio>` are nearly
identical. The argument is sound and it has been demonstrated. The sizes
involved are the disappointment: the interfacial rate constants measured for
*adjacent* lanthanide pairs in P507 differ by factors of 1.25 to 2.4, which is
the same order as the equilibrium separation factors the mechanism was meant to
improve on ([](#the-adjacent-lanthanide-challenge)). Rate ratios are large only
between elements that are already easy to separate.

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

One of the three carried an explicit warning from its author that references
without a URL might be fabricated. That warning was taken seriously: the
chapter has since been rebuilt against the primary literature, and every
quantitative claim below was read out of the paper it is attributed to rather
than inherited from the review. Numbers that could not be found in their
sources have been corrected or deleted, and the two claims resting on a paper
no copy of which could be obtained say so where they appear.

## Why Microfluidics Changes the Problem

### Fundamentals and Advantages

Microfluidic liquid-liquid extraction is the same chemistry as a mixer-settler
run in a channel tens of micrometres across, and everything that follows from
that is geometric [@song2025mine]. Shrinking the channel raises the interfacial
area per unit volume, which raises the volumetric mass transfer coefficient,
which shortens the time to equilibrium from minutes to seconds. It also makes
the residence time a controlled quantity rather than an emergent one: flow rate
and channel length set contact time directly, to sub-second resolution. And
because the whole device holds microlitres, screening a reagent costs almost
nothing in material, which is the argument [](#the-mine-on-a-chip-vision) is
built on.

Two consequences deserve to be separated, because they are usually run together.
The first is intensification: the same separation, faster and in a smaller
volume. The numbers behind that claim are collected and their basis given in
[](#process-intensification-the-numbers), where the enhancement factors are
computed from measured coefficients rather than quoted. The second has no
conventional counterpart at all. A contact time short enough to stop the
extraction before equilibrium is a contact time at which two lanthanides that
share an equilibrium can still be told apart, and [](#fig-09-kinetics) draws
exactly that: two approaches to the same endpoint, distinguishable only while
they are still on the way. Kinetic selectivity is available to a chip and not to
a mixer-settler, and it is the more interesting of the two claims. It is also
not confined to microfluidics: [](#kinetics-and-mass-transfer) collects what has
actually been demonstrated on rate differences between rare earths, and is
candid about how little of it is on the pairs that matter.

(extraction-architectures)=
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
volume [@kolar2016microfluidic]. It is not, however, the weakest of the four
regimes in practice. The one study that ran all three flow regimes in a single
apparatus on a single chemistry --- scandium from a red mud acid leachate into
1 vol% P204 --- got 94.1-96.4% in co-laminar flow, which straddles what the
same apparatus achieved as slugs and as droplets [@feng2025microfluidic]. What
co-laminar flow does have over the others is that the metal it does extract
comes out concentrated: its enrichment factor was 0.99 against 0.59 for slugs
and 0.142 for droplets, because a fine dispersion dilutes what it collects.
The reference measurement of the underlying rate
constants is the plug-based microfluidic study of @nichols2011mechanistic, which
determined interfacial mass transfer rate constants for every lanthanide except
promethium, plus yttrium, under TALSPEAK conditions with rapid mixing and a known
interfacial area --- the two things bulk kinetic methods cannot deliver together.

### Slug (Segmented) Flow

Slug flow creates alternating aqueous and organic segments, which makes slug
length---and with it the specific surface area---a variable the operator sets
[@dessimoz2008liquid]. Internal circulation within each segment adds convective
mixing to diffusion. The extraction efficiencies of 86.9-94.8% that circulate
for this regime are one paper's numbers for one system --- scandium from red
mud leachate into 1 vol% P204, at three feed flow rates
[@feng2025microfluidic] --- and should be read as such rather than as a
property of slug flow. In the same apparatus a conventional shake-and-stand
contact of the same liquors, fifteen minutes of shaking plus five of settling,
reached 74.6%. The regime's practical difficulty is
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
microchannel extractors and 3D reticulated hollow-strut SiC foam microreactors.
The last of these is the most useful result in the chapter, because it ran an
*adjacent* pair. Zhang and co-workers extracted Ce³⁺ and Pr³⁺, each at
0.55 g/L, with saponified P507 in sulfonated kerosene through a foam of
0.5 mm strut diameter and 4 mm cell size, and reached **98.7% extraction
efficiency** for {index}`praseodymium` and 97.0% for {index}`cerium` at a
combined 4 mL/min; at 36 mL/min, far above what most microchannel reactors
sustain, they still got 92.2% and 86.9%, with $K_La$ of 0.198 and 0.161 s⁻¹
and a pressure drop of 2.8 kPa/m [@zhang2022solvent]. The separation factor is
the part that matters, and it is discussed in
[](#the-adjacent-lanthanide-challenge): the chip matched the shaken
equilibrium value at low throughput and lost ground as throughput rose.

### Droplet (Micro-Droplet) Flow

Breaking one phase into discrete drops in the other replaces the flat interface
with the surface of every drop, and the shear that forms the drops drives
internal vortexes inside them, which homogenize the concentration field within
each drop; a grooved microchannel that retains drops on this principle also lets
the working phase ratio inside the channel fall well below the injected phase
ratio, which is what raises the extraction efficiency
[@zhou2019controlled]. No enhancement factor against a conventional contactor is
quoted for the droplet regime in the sources cited here; the head-to-head
comparisons that do exist are collected in
[](#process-intensification-the-numbers). The extraction efficiencies quoted
for this regime, 92.9-97.4%, come from the same scandium study as the slug
figures above and are its highest of the three regimes
[@feng2025microfluidic] --- but only just, and at the cost of an enrichment
factor seven times lower than co-laminar flow gave on the same feed.

The REE case reported in most detail is a flow-focusing droplet microreactor
run on a binary Dy-La system, with the aqueous REE solution dispersed as
monodisperse droplets in a continuous organic phase of Cyanex 572 in Shellsol
D70 [@fernandezmaza2024high]. Residence times of 3-60 seconds produced droplets
presenting 49.2-61.4 cm²/cm³ of interfacial area; at pH 1, 90% of the
{index}`dysprosium` was extracted in 30 s and the two elements were separated
almost completely: at a 20 s residence time about 80% of the dysprosium
crossed over against under 3% of the lanthanum, a reported
{index}`separation factor <separation factor>` of **175.9**. Two of that
paper's control calculations are worth more than the headline. Replacing the
spiral channel with a straight one of the same dimensions moved 80% of the
dysprosium in 30 s rather than 16.5 s, and freezing the internal circulation
altogether --- a motionless droplet, transport by diffusion alone --- pushed
the same duty out to 90 s. Most of what the droplet regime buys is the
stirring inside the drop, not the area around it.

Two variants extend the regime to dilute feeds. Hollow droplets introduce a gas
phase (gas-in-oil-in-water) so that a thin organic shell contacts a large
aqueous volume. Working at a phase ratio of 200 with P507 on neodymium,
@chen2017fast report enrichment factors of 200-450 from feeds of 30-90 ppm at
extraction efficiencies above 90%, with europium and erbium run as medium and
heavy cases. The gas core is what makes it work: it raises $k_L a$ by five to
fifty times over the same droplet without it, and equilibrium is reached
within 0.3 m of outlet channel. Snowman-shaped magnetic
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
following it down the figure is the geometric argument for why the regime
matters: one flat plane in co-laminar flow, the caps of a slug train, then the
perimeter of every drop in a dispersion. The efficiencies do *not* follow that
order --- the three bands overlap, and co-laminar flow sits between the other
two --- which is why the panels carry the enrichment factor as well. That one
does follow it, downward and steeply, because a finer dispersion dilutes what
it collects. All nine figures are @feng2025microfluidic's, on one metal and one
extractant; they are put on the drawing to show the shape of the trade, not to
rank the regimes for any other chemistry. What separates the first three is
increasing flow rate and shear; the sources cited for the regime maps
[@dessimoz2008liquid; @kashid2007hydrodynamics] locate those boundaries, but
this chapter quotes no capillary number or transition velocity, so no threshold
is drawn. Pore-throat
is set apart because it is a change of channel geometry rather than of flow
rate. Drawn by `tools/figures/fig_flow_regimes.py`.
:::

## Separation Mechanisms and Extractants

The dominant separation mechanism employs cation exchange extraction using organophosphorus extractants [@xie2014critical]. The fundamental reaction---RE³⁺(aq) + 3(HA)₂(org) → RE(A₂H)₃(org) + 3H⁺(aq)---involves each REE ion extracted in a complex with six extractant molecules arranged as dimers [@jensen2002comparison].

:::{table} Extractants appearing in the microfluidic literature covered by this chapter
:name: tbl-microfluidic-extractants

| Extractant | Where it is used in microfluidic work | Note |
|----|----|----|
| D2EHPA | All lanthanides | The established acidic organophosphorus reference case ([](#solvent-extraction-fundamentals)) |
| Cyanex 572 | Heavy rare earths | The extractant in the Kolar mixed-oxide-leachate chip work [@kolar2016microfluidic] |
| HEHEHP/P507 | Light rare earths | Strips at lower acidity than D2EHPA |
| TODGA | f-element separations | Tridentate diglycolamide, high lanthanide affinity [@ansari2011chemistry] |

:::

The column headings matter: this is a list of what has been run on a chip, not
a ranking of extractants, and the rate enhancements reported for these systems
belong to the contactor rather than to the extractant — the same chemistry in a
mixer-settler does not go faster.

Synergistic extraction systems combining multiple extractants produce non-linear enhancement effects: {index}`TODGA` + {index}`TBP <TBP (tributyl phosphate)>` in the {index}`ionic liquid <ionic liquids>` \[C4mim\]\[Tf2N\] raises extraction and intra-lanthanide selectivity together, to separation factors of 1622 for Lu/La, 45 for Lu/Sm and 4.8 for Lu/Tb [@turanov2020solvent] — a batch separatory-funnel result rather than a chip one, quoted here for the chemistry and not as a microfluidic demonstration. Studies of DMDOHEMA + {index}`HDEHP` systems reveal that synergy effects are quadratic in mole fraction, attributed to in-plane mixing entropy at bent extractant film interfaces [@elmaangar2020microfluidic]. A related but distinct route makes the ionic liquid itself the extractant: trioctylmethylammonium dioctyl diglycolamate, \[A336\]\[DGA\], dissolved in the fluorine-free ionic liquid diluent \[A336\]\[NO₃\], extracts neodymium and the other lanthanides from nitric acid media more strongly than the molecular acid its anion was prepared from [@rout2014solvent].

Beyond solvent extraction, electrophoretic methods, particularly capillary zone electrophoresis with HIBA buffers, achieve complete separation of **14 lanthanide ions — the series less promethium, which has no stable isotope — in 6 minutes**, with detection limits of 2.77-8.26 nmol/L, though primarily at analytical scale [@yelkenci2017separation]. Electrodialysis with EDTA chelation works on the same principle of differential complexation — the heavy rare earth takes the ligand and migrates as an anion, the light ones stay behind as free cations — but it is a membrane cell rather than a chip, and it is treated with the other electrically driven separations in [](#electrodialysis).

(the-adjacent-lanthanide-challenge)=
## The Adjacent Lanthanide Challenge

Separating adjacent lanthanides differing by only 0.01-0.02 Å in ionic radius represents the field's hardest problem [@nash1993basic]. For the industrially critical **Nd/Pr separation**, optimized D2EHPA systems at pH 5 in hydrochloric acid achieve separation factors of only 2.72---requiring many stages for high purity [@safarzadeh2018insights]. pH emerges as the dominant variable affecting Nd/Pr selectivity.

The **Dy/Nd separation** critical for permanent magnet recycling has seen dramatic advances through non-conventional approaches. {index}`Lanmodulin <lanmodulin>` protein variants (Hans-LanM R100K) achieve **\>98% purity and \>99% yield in a single stage**---a result unachievable with conventional solvent extraction [@mattocks2023enhanced]. {index}`MOF <metal-organic framework (MOF)>` nanotraps (NCU-1) with carboxyl groups and triazole nitrogen atoms demonstrate **separation factors of 273 for Nd/Er and 796 for Pr/Lu** in single-step separations [@hu2024rationally]. Flow-focusing droplet microreactors reach a Dy/La separation factor of 175.9 [@fernandezmaza2024high], but Dy and La sit at opposite ends of the series, and a separation factor of that size between them is what any acidic organophosphorus extractant gives in a beaker.

The microfluidic literature does contain one adjacent pair measured properly,
and it is the most informative result in this chapter. The hollow-strut SiC
foam reactor of the previous section was run on Ce³⁺/Pr³⁺ with saponified
P507. Before putting the liquors through the chip, the authors shook the same
two phases in a flask for two hours and measured the equilibrium separation
factor: 2.28. In the chip at a combined 4 mL/min they got 2.27 --- the
equilibrium value, reproduced. As they pushed the flow rate up to 36 mL/min the
separation factor fell steadily to 1.79 [@zhang2022solvent]. Stopping short of
equilibrium made the separation *worse*, not better, over the whole range they
could reach.

That is not an argument that kinetic selectivity is a mirage; it is an argument
that it points in a direction which depends on the pair, and that the direction
is knowable in advance. The mechanism was worked out numerically by Hao Zhang
and co-workers in two papers. The controlling quantity is the
{index}`Damköhler number` --- the ratio of the maximum extraction reaction rate
to the rate at which the reactants reach the interface --- computed separately
for the two elements. At low flow the droplet interior is transport-limited for
both ($Da \gg 1$), the interface is depleted of whichever ion reacts faster,
and the depletion is itself a separation. Raising the flow rate stirs the drop
harder, replenishes the interface, drives both $Da$ values down, and pushes the
concentration ratio at the interface back toward one, which is the equilibrium
answer. **Separation improves with flow rate only when the two elements'
$Da$ values diverge as it rises.** For Eu³⁺/La³⁺, whose rate constants differ
by a factor of eighteen, they do: at 10 mm/s $Da$ is about 10² for La³⁺ and
2.72 for Eu³⁺, La³⁺ remains transport-limited while Eu³⁺ has become jointly
limited by its own reaction kinetics, and the enhancement factors part company
(2.4 against 1.6) [@zhang2019mechanistic]. For Eu³⁺/Sm³⁺, whose kinetics are
sluggish and nearly identical, they do not, and the modelled separation factor
declines as flow rises [@zhang2019enabling] --- the same direction the SiC foam
measured for Ce/Pr.

The numbers that decide this are worth setting down plainly, because they are
the answer to the question the chapter opened with. Interfacial mass transfer
rate constants in P507, in mm/s [@zhang2019enabling]:

:::{table} Interfacial mass transfer rate constants in P507, and the kinetic ratio each pair offers
:name: tbl-kinetic-ratios

| Pair | Rate constants (mm/s) | Kinetic ratio | Adjacent? |
|----|----|----|----|
| Eu³⁺/La³⁺ | 1.2 × 10⁻² / 2.1 × 10⁻¹ | 18 | no --- eight places apart |
| Nd³⁺/Pr³⁺ | 3.7 × 10⁻² / 9.0 × 10⁻² | 2.4 | yes |
| Pr³⁺/Ce³⁺ | 9.0 × 10⁻² / 1.6 × 10⁻¹ | 1.8 | yes |
| Ce³⁺/La³⁺ | 1.6 × 10⁻¹ / 2.1 × 10⁻¹ | 1.3 | yes |
| Eu³⁺/Sm³⁺ | 1.2 × 10⁻² / 1.5 × 10⁻² | 1.25 | yes |

:::

The kinetic ratios for adjacent pairs run from 1.25 to 2.4. The equilibrium
separation factors for the same pairs in the same chemistry run from about 1.5
to 2.7 ([](#why-rare-earths-are-hard-to-separate); 2.72 for Nd/Pr with D2EHPA
above). They are the same size. The lanthanide contraction that makes the
thermodynamics nearly degenerate makes the kinetics nearly degenerate too, and
for the pairs industry actually has to split, a chip stopped short of
equilibrium is not solving a different problem from a mixer-settler run to
equilibrium --- it is solving the same problem with the same margin, faster.
Experiments on Ce³⁺/La³⁺, Pr³⁺/Ce³⁺ and Nd³⁺/Pr³⁺ in microchannels all report
that raising the flow rate *weakens* the separation, consistent with the
mechanism above [@zhang2019enabling].

Where that leaves the idea is stated in [](#kinetics-and-mass-transfer), which
collects what has been demonstrated on rate differences between rare earths
across every technology, not only on chips. The honest reading of the
microfluidic evidence is that non-equilibrium operation is a real and
controllable lever, that its levers are known --- lower flow rate, more
concentrated extractant, higher feed pH, and a temperature optimum, all of them
acting through the divergence between two Damköhler numbers
[@zhang2019enabling] --- and that on adjacent pairs it has so far bought
nothing that equilibrium did not already offer.

(process-intensification-the-numbers)=
## Process Intensification: The Numbers

Quantitative comparisons between microfluidic and conventional solvent extraction
are worth making carefully, because the intensification factor depends on which
channel and which conventional contactor are being compared. The flow-regime
definitions that underlie these measurements are given by
[@dessimoz2008liquid; @kashid2007hydrodynamics].


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
that supplies the 175.9 separation factor quoted above reports 49.2-61.4 cm²/cm³
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
spread in $k_L a$. The rate law itself is an idealization, and one of the
sources says so — @mary2008microfluidic measured $\sqrt{t}$ growth rather
than an exponential approach, and reported that the assumption of a uniform
concentration inside the droplet, which is what makes the first-order form
exact, "is not tenable". The two vertical strips are operating times quoted elsewhere
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
and per system instead — 175.9 for Dy/La in a flow-focusing droplet reactor
[@fernandezmaza2024high], 2.72 for Nd/Pr with D2EHPA at pH 5
[@safarzadeh2018insights], 2.27 for Ce/Pr in a SiC foam microchannel against
2.28 for the same chemistry shaken to equilibrium in a flask
[@zhang2022solvent] — and only the last of those was measured against its own
conventional control.

(what-the-two-real-comparisons-say)=
### What the Two Real Comparisons Say

Enhancement factors computed from two columns of an order-of-magnitude table
are worth exactly what the weaker column is worth. Two studies in this
chapter's literature did the harder thing and ran the same chemistry both
ways, and they should be read before the table above is used for anything.

The first is the Y-Y microchip work on a leached mixed rare earth oxide
concentrate with Cyanex 572, and it is the only real-feed lanthanide
comparison there is [@kolar2016microfluidic]. After ten seconds of contact the
chip had reached 66% of equilibrium and the beaker 31%. Fitted first-order
rate constants came out roughly double the bulk values, and about triple for
{index}`lutetium` and {index}`ytterbium`. The authors then did the thing that
makes the result useful: they measured why. Interfacial area per unit volume in
the chip was 13-15 mm⁻¹, set by stream geometry alone; in the stirred beaker at
800 rpm the mean drop was 0.8-0.9 mm, giving about 7 mm⁻¹. Twice the area,
twice the rate --- which accounts for every element except Lu and Yb, and
leaves nothing for microfluidics as such to explain. The gain is real, it is
geometric, and it is a factor of two, not a factor of five hundred.

The second is a micro-Raman study of a T-junction chip against a stirred Lewis
cell, on nitric acid into 30 vol% TBP in n-dodecane --- a PUREX surrogate with
no lanthanide in it, which limits what it can be asked to say
[@nelson2018micro]. What it says is nevertheless uncomfortable. The chip gave
forward and reverse mass transfer coefficients of 1.0(±0.1) × 10⁻³ and
6.4(±0.5) × 10⁻³ mm/s; the conventional Lewis cell gave 4.75(±0.14) × 10⁻³ and
2.56(±0.03) × 10⁻² mm/s. The macroscopic stirred cell was about four times
faster, because the chip was diffusion-limited at the flow rates used. A
microchannel does not intensify anything by being small; it intensifies by
being *stirred* relative to its own diffusion length, and a chip run too gently
loses to a beaker run hard.

Three further observations belong with these. @feng2025microfluidic's
conventional control --- fifteen minutes of shaking plus five of settling ---
reached 74.6% against the chip's 86.9-97.4%, an improvement of 26-29 percentage
points, and the chip took 5.6-10 minutes to process 1 mL, so the time saved was
minutes rather than orders of magnitude. @wang2017microflow's review states the
optimistic end of the range, two to three orders of magnitude in mass transfer
rate over common extractors, and makes the claim that matters more for design:
extraction efficiencies in miniaturized extractors tend to exceed 90%, so such
an extractor can be treated as one theoretical stage. And
@mary2008microfluidic, who measured transfer into and out of octanol-borne
water droplets directly, found that the transferred mass grows as $\sqrt{t}$
after a short transient and that the completion time falls as $Pe^{-2/3}$ ---
not the first-order exponential that [](#fig-09-kinetics) draws. That figure is
a rate law fitted to reported coefficients, not a measurement, and its shape is
wrong in the one system where the shape was checked.

## Electrophoretic Microfluidic Separation

Electrophoresis is not a contactor and does not belong in the intensification
argument, but it is where the sharpest lanthanide separations on a chip have
been achieved, and it is worth the space for that reason alone.

The cleanest demonstration is an
{index}`isotachophoresis <isotachophoresis>` device from PNNL: a fused-silica
chip with a 70 µm × 70 µm serpentine channel 33.3 cm long, joined at a 90°
junction to a 25 cm fused-silica capillary of 50 µm bore, with under 7 nL of
void volume at the joint [@pesavento2021versatile]. The leading electrolyte is
10 mM ammonium acetate with 7.0 mM α-hydroxyisobutyric acid and 1.0% w/v PVP at
pH 4.5; the trailing electrolyte drops the acetate to 10 mM acetic acid at
pH 3.0. Samples are loaded at 2.0 kV for 60 s and separated at 7.0 kV. Mixtures
of two, seven and all fourteen non-radioactive lanthanides were run at
0.10 mg/mL each, with the effluent fed to a quadrupole ICP-MS through a
commercial chip-to-ICP interface. Two numbers characterize it: resolution
between adjacent zones was 0.42 ± 0.08 on the chip itself and 0.53 ± 0.04
further along the capillary, because isotachophoretic zones self-sharpen as
they migrate, and the average error on zone composition was 5.7%. It is a
genuine chip-to-ICP-MS separation of the full series, and the claim sometimes
attached to it --- eight lanthanides concentrated in about six minutes --- is
that paper's description of earlier work by others, not its own result.

Capillary zone electrophoresis reaches the same endpoint by a simpler route.
With 4.5 mM α-hydroxyisobutyric acid and 1 mM acetic acid at pH 4.5 and
capacitively coupled contactless conductivity detection, all fourteen
lanthanide ions separate in six minutes [@yelkenci2017separation]. Detection
limits are 2.77-8.26 nmol/L and quantitation limits 9.29-27.5 nmol/L, improved
further by sample stacking. C4D is what makes this practical for lanthanides
specifically: the ions are not UV-active, and conductivity detection reads them
without a chromophoric ligand or a visualization agent.

Both rest on the same chemistry, which is worth naming because it recurs
elsewhere in this book. HIBA is a weak, fast-exchanging complexant whose
stability constants rise monotonically across the series, so it converts a 1%
difference in ionic radius into a difference in the fraction of each element
that is complexed at any instant, and therefore into a difference in effective
charge and mobility. Iminodiacetic acid works the same way with a sharper
light/heavy discrimination, coordinating tridentate to the light lanthanides
and bidentate to the heavy ones.

The reason this is a footnote to the chapter rather than its centre is
throughput. These are nanolitre injections read by an instrument that costs
more than the separation it is feeding. Nothing in the electrophoretic
literature scales, and nobody claims it does; what it offers rare earth
processing is analysis, not production. Electrodialysis with EDTA chelation
works on the same principle of differential complexation --- the heavy rare
earth takes the ligand and migrates as an anion while the light ones stay
behind as free cations --- but it is a membrane cell rather than a chip, and it
is treated with the other electrically driven separations in
[](#electrodialysis).


## Scale-Up by Numbering-Up

The most significant pilot-scale achievement comes from the University of South Australia, where Yang and co-workers demonstrated **three-stage {index}`counter-current <countercurrent cascade>` microfluidic solvent extraction numbered up 100-fold without losing extraction efficiency** [@yang2022pilot]. The numbering-up was achieved by building multi-layer glass chips and operating three of them in counter-current or parallel configuration. The paper is behind a paywall with no open copy and no released abstract, so the throughput it reached is not quoted here; the description above is as its authors summarize it in their own later review [@yang2024industry].

Scale-up follows numbering-up rather than geometric scale-up, preserving the microfluidic advantages of enhanced mass transfer [@hessel2013process]. The choice is between *internal* numbering-up, which puts parallel channels inside one device and is the hardware-efficient option, and *external* numbering-up, which replicates whole systems including their pumps and is simpler to implement but multiplies the ancillary equipment. The South Australian chips were run on high-value metals --- platinum as well as rare earths --- rather than on a single model system [@yang2022pilot; @yang2024industry].

However, a substantial gap remains between current demonstrations and industrial requirements. Industrial REE separation typically processes 50,000-100,000 tonnes of concentrates annually, while the published microfluidic demonstrations are laboratory devices numbered up by a factor of a hundred. Even on the most favourable reading the gap is several orders of magnitude of further parallelization, and it is wider still than any such ratio suggests, because one side of it is measured as solid concentrate and the other as dilute liquor.

### Mini-Channel Counter-Current Extractors

Between a chip and a mixer-settler sits the mini-channel: a 4-6 mm bore, large
enough to carry a real flow, small enough that the flow stays ordered.
Continuous counter-current operation at this scale has been characterized
hydrodynamically rather than only demonstrated [@he2024intensifying], which is
what a scale-up calculation needs. No copy of that paper could be obtained, and
so none of its design results are quoted here: how many theoretical stages a
mini-channel contactor delivers per unit length, and the length at which it
stops being a contactor and starts being a cascade element, are numbers this
chapter cannot source.

The problems a continuous contactor at this scale must solve are the ones every
continuous contactor has --- the volumes going in and out are large relative to
the holdup, a change at the inlet reaches the outlet only after a delay, and the
behaviour is nonlinear in several variables at once --- and they are why
[](#process-control-and-automation) treats control as a design problem rather
than an afterthought.

### What Actually Limits Numbering-Up

The bottleneck is not the extraction. Extraction in a microchannel is fast, and
the head-to-head comparisons in
[](#what-the-two-real-comparisons-say) show it is fast by a factor of about two
rather than a factor of hundreds. What is hard is getting the two phases apart
again, once per channel, without a settler.

The clearest measurement of that ceiling comes from a membrane-free separator
built by binder jetting: an array of micro-posts that splits the phases by
wetting rather than by density, which means it works on either phase order and
on both slug and dispersed droplet flow [@touma2024intensification]. Extraction
reached equilibrium in 0.25 s. Separation was essentially complete up to
15 mL/min --- at interfacial tensions of 48.9 and 10.9 mN/m and aqueous-to-organic
ratios of 1:1 and 2:1 --- and broke down at 20 mL/min, where the dispersed phase
began to carry through. The working fluids were isobutanol and cyclohexane, not
a metal system, so the numbers are a hydrodynamic ceiling rather than a
process result. Taken at face value they say that a hundred numbered-up
channels of this kind would pass something under 1.5 L/min of combined phases,
and that pushing each channel a third harder loses the separation entirely.

The milli-fluidic route trades interfacial area for throughput and gets further.
As Yang and Priest describe it, a cobalt extraction run in coiled tubing with an
inline phase separator was projected to a pilot capacity of about 53 m³ per year
[@yang2024industry] --- roughly 0.1 L/min, in the same range as the micro-post
separator, but reached with plumbing rather than with a chip. That is the honest
current scale of the field: litres per minute, not tonnes per day.

## Reported REE Microfluidic Systems

Two of the studies most often cited in this area have already done their work in
this chapter. Kolar and co-workers' Cyanex 572 extraction from a real mixed-oxide
leachate and Nelson and co-workers' micro-Raman kinetics are the two head-to-head
comparisons against conventional contacting, and they are discussed in
[](#what-the-two-real-comparisons-say); Feng and co-workers' three-regime
comparison runs through [](#extraction-architectures). Two others are worth
naming, and both come with the same caveat.

El Maangar and co-workers coupled a microfluidic contactor to online X-ray
fluorescence --- by their account the first automated microfluidic tool with XRF
detection for liquid-liquid extraction --- and used it to study synergic
extraction of rare earths by combinations of solvating and ionic extractants,
reporting Gibbs free energies of transfer for five elements together with the
effects of temperature and interfacial charge density
[@elmaangar2020microfluidic]. No copy of the paper could be obtained. The
description here is from its abstract, and no quantity from it is quoted
anywhere in this chapter.

Nichols and co-workers built a plug-based system to measure absolute interfacial
mass transfer rate constants for the whole lanthanide series under
{index}`TALSPEAK` conditions, with rapid mixing and a known interfacial area
[@nichols2011mechanistic]. That is the same measurement Zhang and co-workers
later made for P507, and it is the measurement that decides whether kinetic
selectivity is worth anything for a given extractant. No copy of this paper could
be obtained either, so its rate constants are not tabulated in
[](#the-adjacent-lanthanide-challenge); the constants there are P507's alone.

(detection-colorimetry-fluorescence-and-spectroscopy)=
## Detection: Colorimetry, Fluorescence, and Spectroscopy

A chip that separates faster than it can be measured is not much use, and the
attraction of a colorimetric readout is that a camera is cheaper than an ICP-MS
by three orders of magnitude. The literature on that readout is real and
substantial. It is also, without exception among the work cited here, about
something other than lanthanides --- which is precisely why
[](#microfluidic-research-opportunities) lists a lanthanide-selective
colorimetric readout as an opportunity rather than a tool.

The most quantitative of these is Idros and Chu's triple-indicator paper device,
which reads six metal ions from the RGB values of a photograph
[@idros2018triple]. Its detection limits are worth setting against the
concentrations that actually matter, because for four of the six it clears them
and for two it does not:

:::{table} Detection limits of a three-indicator µPAD against the corresponding safe-limit concentrations [@idros2018triple]
:name: tbl-upad-lod

| Ion | Detection limit | Safe limit | Usable? |
|----|----|----|----|
| Cu²⁺ | 15 µM | 20.46 µM (1300 µg/L) | yes |
| Fe³⁺ | 3.58 µM | 5.37 µM (300 µg/L) | yes |
| Ni²⁺ | 0.5 µM | 1.19 µM (70 µg/L) | yes |
| Cr²⁺ | 0.8 µM | 1.92 µM (100 µg/L) | yes |
| Hg²⁺ | 0.1 µM | 10 nM (2 µg/L) | no --- an order of magnitude too high |
| Pb²⁺ | 0.3 µM | 48.26 nM (10 µg/L) | no --- about six times too high |

:::

The two it misses are the two that matter most for toxicity, and the paper says
so. It is a fair picture of where cheap colorimetry sits: adequate for
process-stream concentrations, not for regulatory ones.

Two developments make such devices more practical. Chauhan and Toley removed the
wax barriers that normally define channels on paper, stacking two membranes of
different wicking rates so that the fast one distributes sample and the slow one
holds reagent; the result puts 20 dried reagent spots on an 8 cm × 2 cm strip and
rehydrates them uniformly in as few as 30 s, improving the detection limit of the
same colorimetric assays by more than 3.5× over a conventional wax-patterned
device [@chauhan2021barrier]. Their analytes are salivary --- thiocyanate,
protein, glucose, nitrite --- not metals; what carries over is the geometry, not
the chemistry. López-Ruiz and co-workers took the camera seriously as an
instrument, using a phone's own flash as the light source over seven sensing
areas and working in HSV rather than RGB, and reached a resolution of 0.04 pH
units with an accuracy of 0.09 and a mean squared error of 0.167, alongside
0.51% resolution at 4.0 mg/L of nitrite with a detection limit of 0.52 mg/L
[@lopezruiz2014smartphone]. That is the performance ceiling of a phone camera
used carefully, and it is respectable.

The design principles behind selective fluorescent and colorimetric probes for
lead, cadmium and mercury have been reviewed at length [@kim2012fluorescent]. It
has since been read, and it confirms what the citation was hedged against:
across the whole review neither lanthanides nor rare earths are mentioned once.
Their f-f transitions are weak and shielded, so they need either a sensitizing
ligand or an entirely different readout, and none of this probe chemistry
transfers.

## Computer Vision and Machine Learning

Two things a camera can do on a microfluidic device: measure the fluid, and
measure the drops.

Hadikhani and co-workers did the first. They trained a deep network on images of
droplets alone --- no probe in the channel, no calibration against a second
instrument --- and recovered the composition of a water-isopropanol mixture to
0.5% and the flow rate to a resolution of 0.05 mL/h [@hadikhani2019learning]. The
underlying idea is that droplet shape and spacing encode viscosity, surface
tension and flow rate, so an image is already a measurement; the authors note it
should extend to those properties directly. It is not an extraction system, and
no lanthanide appears in it, but for a numbered-up device where a hundred
channels cannot each carry a sensor, a camera watching all of them at once is the
only instrument that scales.

Gelado and co-workers did the second, and their result is a caution about
resolution. Detecting and sizing droplets in a 390 × 190 µm channel is easy at
full resolution and gets hard quickly as the image degrades. Compared on
identically downsampled images, the classical Circular Hough Transform and a
Segment Anything Model pipeline diverge sharply: at a 4× reduction the Hough
transform scored a Dice coefficient of 0.49 ± 0.30 with a diameter error of
115.25 ± 89.63 µm, while SAM followed by the same transform scored 0.94 ± 0.10
with an error of 18.10 ± 56.20 µm [@gelado2023enhancing]. Super-resolution
before detection helped, with a multi-scale residual network outperforming both
SRCNN and bicubic interpolation, and DnCNN denoising held up to a noise standard
deviation of 4. The practical reading is that a segmentation model buys roughly a
factor of two in usable magnification, which is what decides whether one camera
can watch a whole numbered-up array or needs one per channel.

## Device Fabrication and Solvent-Resistant Materials

{index}`PDMS` is the default material of academic microfluidics and the wrong
material for this chapter's chemistry. It swells in exactly the solvents rare
earth extraction runs on --- aliphatic kerosene diluents, and the aromatics and
chlorinated solvents used to dissolve extractants --- and a swollen channel is a
channel of unknown dimension.

Two responses exist, and they are not equivalent. Rolland and co-workers
replaced the material outright, photocuring a perfluoropolyether network from a
PFPE diol of Mn 3800 end-capped with isocyanatoethyl methacrylate and cured
under 365 nm light with 1 wt% photoinitiator [@rolland2004solvent]. The
uncured resin is thinner than Sylgard 184 --- 0.36 against 3.74 Pa·s --- so it
moulds features as faithfully. The number that matters is the swelling: after
94 hours in dichloromethane a PDMS network had swelled to 109% of its weight,
while the PFPE network took up under 3%. That is not an improvement in
degree; it is a material that does not swell.

Kim and co-workers took the other route and coated the PDMS, curing a hybrid
inorganic-organic layer (HR4) onto the channel walls [@kim2009solvent]. Measured
as weight uptake after 12 hours, the reduction is large and uneven:

:::{table} Swelling of PDMS after 12 h, uncoated and with the HR4 hybrid coating, as weight uptake in percent (±3%) [@kim2009solvent]
:name: tbl-pdms-swelling

| Solvent | PDMS | HR4-coated PDMS |
|----|----|----|
| Trichloroethylene | 173.67 | 27.55 |
| Chloroform | 127.52 | 33.10 |
| Toluene | 114.96 | 9.76 |
| Hexane | 112.07 | 14.65 |
| Heptane | 101.33 | 37.61 |
| Tetrahydrofuran | 95.91 | 22.30 |
| Acetone | 13.53 | 7.40 |

:::

A four- to twelve-fold reduction is enough to make a device survive a run it
would otherwise fail, and it is not the same as not swelling: heptane still
takes up 37.61% and chloroform 33.10%. The aliphatic entries are the relevant
ones here, since kerosene diluents such as ShellSol D70 and sulfonated kerosene
are aliphatic, and they are also the two the coating handles least well.

This is why the rare earth studies in this chapter are not built in PDMS. The
devices that carried real extractant chemistry were glass, PTFE and PEEK
capillary, or --- in the SiC foam work --- ceramic. PDMS remains the right
material for the aqueous-phase detection devices in the preceding section, and
the wrong one for the contactor.


## Feedstock Integration

Microfluidic systems have been validated with diverse REE-containing feedstocks beyond synthetic solutions. Processing of **mixed rare earth oxide ore leachates** using Y-Y microchip configurations with Cyanex 572 achieved 2-3× higher extraction rates with contact times of only 15 seconds [@kolar2016microfluidic]. Particulate-laden feeds are the standing difficulty for closed microchannels, whose dimensions are comparable to the particles in a mineral stream, and open-channel designs are the response: an open-microfluidic geometry that creates a dynamic fluidic obstacle outside the channel excludes particles while letting soluble ions enter freely for analysis [@yang2024industry].

**{index}`NdFeB` permanent magnet recycling** represents a high-value near-term application, and the pretreatment matters as much as the contactor. Roasting magnet scrap in air above 500 °C converts the neodymium not to Nd₂O₃ but to the refractory ternary NdFeO₃, which then takes more than a day to dissolve; roasting instead under argon with 5 wt% carbon as an iron reductant avoids that phase, segregates metallic iron from the rare earth phase, and leaves a residue that dissolves completely in the ionic liquid \[Hbet\]\[Tf₂N\] in twenty minutes, at a rare-earth-to-iron ratio some fifty times the ratio in the scrap [@orefice2019selective]. That kind of leachate --- concentrated, low in iron, already in a single phase --- is what a microfluidic contactor downstream would want.

**{index}`Coal fly ash <coal fly ash>`** is a plausible feed on grade alone. Taggart and co-workers measured more than a hundred U.S. ashes and found total REE --- lanthanides plus yttrium and scandium --- averaging 591 mg/kg in ashes from Appalachian coals, against 403 mg/kg for Illinois basin and 337 mg/kg for Powder River basin ashes, with the critical fraction (Nd, Eu, Tb, Dy, Y, Er) at 34-38 % of the total, well above the under-15 % typical of conventional ores [@taggart2016trends]. A microfluidic contactor would sit downstream of a leach, on the pregnant liquor; no such coupling has been demonstrated at the time of writing. Complete "ash-to-oxide" processes achieve enrichment factors exceeding 400× relative to raw fly ash. {index}`Flash Joule heating <flash Joule heating>` ultrafast activation (\~3000°C, \~1 second) increases REE extractability approximately 2× from secondary wastes including coal ash, bauxite residue, and electronic waste at remarkably low energy consumption of 600 kWh/ton (\~\$12/ton) [@deng2022rare].

### Scandium Recovery from Red Mud

The one feedstock in this chapter that has actually been run through a chip is
{index}`red mud`. Feng and co-workers extracted Sc³⁺ from a bauxite-residue
leachate with 1 vol% P204, comparing all three flow regimes on the same
apparatus [@feng2025microfluidic]. The comparison against conventional practice
is the useful part: a 15-minute shake followed by a 5-minute stand recovered
74.6% of the scandium, while every microfluidic regime cleared 86.9% and the best
conditions reached 97.4%, at residence times under a minute. Processing one
millilitre took 5.6 to 10 minutes depending on the regime --- a reminder that
short residence time and high throughput are different things, and that this is
still a laboratory device.

Scandium is the right first target for a chip, and not because it is easy. It is
present at low concentration in a large, awkward, alkaline waste stream that
exists in hundreds of millions of tonnes; the value per tonne of feed is low and
the value per kilogram of product is high, which is the combination that makes a
small, fast, cheap contactor worth building.

(industrial-status-and-key-players)=
## Industrial Status and Key Players

**True commercial-scale microfluidic REE separation plants do not yet exist.** The technology remains at research-to-pilot stages. Several companies are commercialising *related* intensified separations, and the figures below come from company announcements rather than from the peer-reviewed literature; treat them as claims, not measurements.

- **IBC Advanced Technologies** offers the most mature related technology, SuperLig® Molecular Recognition Technology (MRT™), a ligand-on-support column chemistry that the company reports separates individual REEs, including adjacent pairs, from spent NdFeB magnets at high recovery and purity.

- **Phoenix Tailings** (Boston) extracts REEs from mine tailings by a route it describes as free of the acids and radioactive waste of conventional processing, and is scaling from tens to hundreds of tonnes per year.

- **REEgen**, a Cornell spinout, uses {index}`bioleaching` with *Gluconobacter oxydans* — the organism behind the biolixiviant work in [](#biological-and-biomimetic-separations) — rather than microfluidic contactors as such.

### Leading Research Groups

Much of the droplet-microfluidics work cited in this chapter comes out of the
State Key Laboratory of Chemical Engineering at Tsinghua University, where
Jianhong Xu's group developed the hollow-droplet and Janus
nanoparticle-stabilised systems discussed above [@chen2022efficient], and
Yundong Wang's group has worked on continuous rare earth recovery from
wastewater. This is an observation about where the cited papers originate, not
a ranking of laboratories.

(the-mine-on-a-chip-vision)=
## The Mine-on-a-Chip Vision

"Mine-on-a-chip" is a perspective piece rather than a process, and it is worth
reading as an argument about where microfluidics is most likely to pay
[@song2025mine]. Its case rests on three properties of the format — small sample
and reagent consumption, parallel processing, and testing that is fast and
cheap — and it points them not only at separation but at everything around it:
characterizing a material, screening reagents, developing a chemical analysis,
and defining a resource in the first place. That framing is a useful corrective
to the rest of this chapter. The intensification numbers above are about a
contactor, but the strongest near-term argument for a chip may be that it lets a
hundred conditions be tried on a gram of feed rather than that it separates
better than a mixer-settler.

## Choosing Among the Configurations

The four contactor architectures in [](#extraction-architectures) trade the same
three things against each other, and the earlier sections give the reasoning for
each in its own terms rather than as a scorecard. Co-laminar flow has the
simplest device and the cleanest phase separation, and the slowest mass transfer,
because nothing stirs. Slug flow adds internal circulation within each segment
and gets a large gain for a small change in hardware. Droplet flow goes further
still and buys the highest interfacial area per volume, at the cost of having to
break the emulsion afterwards. Pore-throat channels exist to reach phase ratios
no other format can hold. Electrophoretic separation is not a contactor at all
and belongs in the analytical column of the ledger.

No table of efficiencies by configuration is given here. The per-architecture
extraction percentages and phase-ratio ranges that circulate for this comparison
could not be traced to sources that state them, and they would be misleading
even if they could: the numbers reported in the studies cited above are each
tied to a particular extractant, feed and residence time, and moving one of
those moves the efficiency more than changing the architecture does.

(limitations-and-outlook)=
## Limitations and Outlook

Four things stand between the results in this chapter and a process. Interfaces
that are stable in a clean laboratory system are hard to keep stable at the high
phase ratios that make the format attractive. Real feedstocks foul and clog
channels whose whole advantage is that they are small. A chip has to be
integrated with a leach upstream and a stripping and precipitation train
downstream, and the intensification is only worth what the slowest neighbouring
unit allows. And precision fabrication is cheap per device and expensive per
tonne of throughput, which is the arithmetic that numbering-up has to beat.

The directions being pursued follow from those four. Machine learning is being
used to optimize flow conditions, and computer vision to read the droplets
directly, both treated above. 3D printing shortens the prototype cycle.
Coupling a chip to online ICP-MS closes the loop between running a condition and
knowing what it did. Hybrid devices combine flow regimes, using one architecture
for contacting and another for separation. Automated multi-stage
counter-current operation is the one that matters most, because it is what turns
a single-stage demonstration into something a cascade calculation applies to,
and it is the least demonstrated of the five.

The honest summary is narrower than the enthusiastic one, and more useful. A
microfluidic contactor really does transfer mass faster than a conventional one:
volumetric coefficients of 0.2-0.5 s⁻¹ have been measured in 269-400 µm channels
[@dessimoz2008liquid], against the 10⁻³-10⁻² s⁻¹ a mixer-settler is usually
credited with. But the only two studies that ran both sides of that comparison
themselves put the gain at about a factor of two in favour of the chip
[@kolar2016microfluidic] and about a factor of four *against* it
[@nelson2018micro], and the reason is that the denominator in the arithmetic
above is a textbook figure rather than a measurement of a vigorously stirred
vessel. Residence times of seconds instead of tens of minutes are real and are
not in dispute. Two orders of magnitude of intensification are not.

The kinetic-selectivity argument needs the same discipline. Large separation
factors have been reported in flow --- 175.9 for Dy/La in a flow-focusing droplet
reactor at 20 s and pH 1 [@fernandezmaza2024high] --- but Dy and La sit nine
places apart, and any acidic organophosphorus extractant separates them well in a
beaker. The single measurement in this literature on an *adjacent* pair points
the other way: a chip matched the shaken-equilibrium β for Ce/Pr at low
throughput and lost selectivity as throughput rose, from 2.27 to 1.79
[@zhang2022solvent]. Kinetic control is a real lever, and
[](#the-adjacent-lanthanide-challenge) sets out the condition under which it
helps --- the two Damköhler numbers must diverge as flow rises, which for most
adjacent pairs they do not.

What would change the picture is not a faster contactor. It is (1) a phase
separator that holds at more than the ~15 mL/min per unit where the best
membrane-free design fails [@touma2024intensification], since that, not the
extraction, is what numbering-up is limited by; (2) on-chip analytics good
enough to close a control loop, which exists in pieces and has not been
assembled; and (3) any demonstration at all of stable long-term operation on a
real industrial feed [@wang2017microflow]. The near-term value is in high-value,
low-volume duties --- magnet recycling streams above all --- and in using chips as
instruments rather than as plant: a device that measures interfacial rate
constants in seconds is worth having whether or not it ever separates a tonne.

It is also worth keeping the competition in view. The best single-stage result
on a Dy/Nd mixture in this book comes not from a chip but from an engineered
protein column, at \>98% purity and \>99% yield [@mattocks2023enhanced], and that
is a light/heavy split rather than an adjacent pair
([](#biological-and-biomimetic-separations)). Phoenix Tailings and IBC Advanced
Technologies are commercialising intensified separations that are not
microfluidic. The fundamental science of microfluidic extraction is sound;
whether it becomes plant or stays a laboratory instrument will be settled by
phase separation and by economics, not by mass transfer.

(microfluidic-research-opportunities)=
## Research Opportunities

Based on this literature review, several promising research directions emerge:

### Real-Time Colorimetric Monitoring of REE Extraction
**Concept**: Develop microfluidic devices with integrated colorimetric indicator zones for real-time monitoring of rare earth element extraction efficiency.

The pieces exist separately. Micro-Raman monitoring of a two-phase extraction
has been demonstrated [@nelson2018micro], smartphone colorimetric detection is
established [@lopezruiz2014smartphone], and rare earth extraction kinetics have
been characterized in a microfluidic device [@nichols2011mechanistic]. Nobody
has put the three together.

### Machine Learning-Optimized Extraction Screening
**Concept**: Combine high-throughput droplet generation with computer vision analysis for automated extraction optimization.

Deep learning for droplet detection is demonstrated
[@hadikhani2019learning; @gelado2023enhancing] and droplet-based extraction is
well founded [@mary2008microfluidic]; what is missing is a loop that closes
between them, where the vision output changes the next condition tried.

### Smartphone-Based Field Detection
**Concept**: Portable microfluidic extraction kit with smartphone colorimetric readout for field applications.

Smartphone platforms handle multi-analyte detection [@lopezruiz2014smartphone]
and paper-based colorimetric devices work for heavy metals
[@idros2018triple; @chauhan2021barrier]. Neither has been demonstrated on a
rare earth, where the analytical problem is discriminating between elements that
a colorimetric reagent sees as identical.
