---
title: Critical Minerals from Pennsylvania Produced Water
---

(produced-water-critical-minerals)=
# Critical Minerals from Pennsylvania Produced Water

Every Marcellus Shale gas well in Pennsylvania produces water as well as gas.
The water comes back up the same hole, at a rate that falls steeply over the
first two years and then continues for the life of the well, and it is not
fresh: it is a brine carrying more than 100,000 mg/L of total dissolved solids
[@mackey2024estimates]. It is already pumped, already piped, already collected
at central facilities, and already treated to some degree before it is
reinjected somewhere else. Whatever is dissolved in it has, in a sense, already
been mined. The only cost left is the cost of taking it out of the water.

That is the argument for treating produced water as a critical mineral
feedstock, and it is a good one. This chapter is about what is actually in the
water, what could plausibly be recovered from it, and what stands in the way.

It has to open with a correction, because this is a book about rare earths and
the honest answer for rare earths is discouraging. The critical mineral in
Pennsylvania produced water is {index}`lithium`, not the lanthanides. The
national accounting in @smith2024critical puts the total rare earth content of
all US oil and gas produced water at **1 metric tonne per year** — the standard
deviation on that estimate is 2 tonnes — against a US apparent consumption of
9,300 t, or **0.01 %** of demand. For lithium the same study's arithmetic gives
**300 %**. The two numbers differ by four and a half orders of magnitude, and
no improvement in separation chemistry closes that gap, because the gap is in
the feed.

So this chapter is mostly about lithium, and the reason it belongs in a rare
earth book is not that produced water is a rare earth resource. It is that the
central separation problem in produced water — telling {index}`lithium` from
{index}`magnesium` — is the same *kind* of problem as telling neodymium from
praseodymium, and the same instincts apply. The lithium case is the easier
version of the problem the rest of this book is about, it has a real feedstock
and real money behind it, and watching what does and does not work there is
informative about what to expect from the harder version.

(what-pennsylvania-produces)=
## What Pennsylvania Actually Produces

The best-characterised account of the Pennsylvania resource is
@mackey2024estimates, from the National Energy Technology Laboratory and the
University of Pittsburgh. Its data are Pennsylvania Department of Environmental
Protection compliance reports from 2012 to 2023 — 595 reports covering 515
wells, extracted by OCR — filtered to exclude analyses with a charge imbalance
worse than ±10 % and to keep only genuine brines above 35,000 mg/L TDS. Well
production volumes came from decline-curve analysis on six of the top ten
operators, covering 42 % of the wells that reported produced water volumes in
2022; of 4,798 wells initially evaluated, 2,561 survived the filters and 1,228
gave usable curve fits at r² ≥ 0.5.

The headline result is a Monte Carlo estimate over 25,000 realisations:

| Quantity | Northeast PA | Southwest PA |
|---|---|---|
| Li, median (IQR) | 205 mg/L (139-267), n = 422 | 127 mg/L (112-140), n = 137 |
| Mg, median | 1,000 mg/L, n = 421 | 2,300 mg/L, n = 137 |
| Mg/Li mass ratio, median (IQR) | 5.39 (2.66-7.26) | 17.8 (14.3-20.7) |
| 10-year cumulative produced water per well, median | 2.43 × 10⁷ L, n = 506 | 4.68 × 10⁷ L, n = 722 |
| 10-year Li yield per well (95 % CI) | 1.96 mt (1.86-2.07) | 2.90 mt (2.80-2.99) |

Statewide, the mean annual produced water volume over 2018-2022 was
8.76 × 10⁹ L (± 5.54 × 10⁸), the statewide lithium median was 174 mg/L, and the
maximum likelihood estimate for annual lithium mass yield is **1,160 mt/yr
(95 % CI 1,140-1,180)**. Set against an estimated 3,000 mt of annual US lithium
consumption, that is 38-40 % of domestic demand — with the explicit assumption,
which the authors state, of 100 % lithium recovery. Their robustness claim is
that even two standard deviations low, the figure exceeds 30 %.

Three qualifications travel with that number and all three come from the paper
itself.

The first is that the water is not free. Roughly **95 % of Marcellus produced
water is already reused** in ongoing hydraulic fracturing, and any volume
diverted to lithium extraction would have to be made up with fresh water.
Lithium extraction is a more complex operation than the minimal solids removal
the water currently gets, and @mackey2024estimates say plainly that it "may
increase the environmental footprint of water operations due to added
transportation and solid wastes generated from PW treatment." The stream is not
a waste stream looking for a use; it is an input to an existing process.

The second is that the resource is a flow, not a stock, and the flow decays. A
typical Marcellus well loses **80 % of its water production within its first two
years**. Sustaining 1,160 mt/yr therefore requires continuously drilling new
wells to replace older ones. The lithium is not sitting in a reservoir waiting;
it arrives as a by-product of a drilling programme, and it stops when the
drilling does.

The third is the one that makes this a separations problem, and it deserves
its own section.

(the-magnesium-lithium-problem)=
## The Magnesium-Lithium Problem

Look again at the two Pennsylvania columns. Southwest wells produce about twice
the water and yield about 33 % more lithium per well over ten years — but only
26-38 % more once the lower lithium concentration is accounted for. And their
Mg/Li ratio is 17.8 against the northeast's 5.39.

That ratio is the whole game. @mackey2024estimates note that extraction from
brines with Mg/Li above 6 is less efficient and more expensive than from
low-ratio brines, and that northeastern Pennsylvania's ratio is comparable to
salar brines such as the Atacama — which are the feedstocks that evaporative and
distillation-based lithium recovery was built around. Two corners of one state,
producing from the same formation, present the separation engineer with feeds
that differ threefold in the ratio of the thing you want to the thing you must
reject.

A reader who has come this far will recognise the shape of this. It is the
argument of [](#why-rare-earths-are-hard-to-separate) transposed to a different
pair of ions: the difficulty of a separation is not set by the target's
properties but by how nearly the interferent shares them, and by how much of the
interferent there is. Where the lithium case differs — and differs in its
favour — is that Li⁺ and Mg²⁺ do not share a charge. Adjacent lanthanides are
both trivalent and differ by about one percent in ionic radius, which leaves a
designer almost nothing to grip. Li⁺ and Mg²⁺ differ in charge, in hydration
enthalpy, and in hydrated size. On paper this should be easy.

In practice it is not, and the reason is instructive. The hydrated diameters are
close enough that a membrane with an ordinary pore size distribution cannot
resolve them. @peng2024extreme give the numbers. A conventional polyamide
nanofiltration membrane made by interfacial polymerisation of piperazine with
trimesoyl chloride has a pore size range of 2.0-14.0 Å; two commercial
membranes, NF270 and DK, come in at 1.6-12.6 Å and 3.0-9.5 Å. The hydrated
diameter of Mg²⁺ is 8.6 Å. Every one of those membranes has a substantial
population of pores wider than the ion it is supposed to exclude, and the
reported Li⁺/Mg²⁺ selectivity of pressure-driven nanofiltration is
correspondingly poor — "usually less than 20," in the paper's own summary of the
field.

@peng2024extreme narrow the distribution rather than shift it. Running the
interfacial polymerisation in the presence of an oil-soluble surfactant that
forms a monolayer at the oil/water interface — they call it OSARIP — produces a
membrane whose pores span 3.2-8.0 Å, entirely below the Mg²⁺ hydrated diameter.
On a simulated brine of 2,000 ppm total salt at a Mg/Li mass ratio of 20:1, the
membrane rejects 99.82 % of the Mg²⁺ while showing a *negative* rejection of
−48.35 % for Li⁺ — lithium is enriched in the permeate — for a Li⁺/Mg²⁺
selectivity of **828**. The same membrane chemistry made by conventional
interfacial polymerisation gives 92.56 % and −19.25 %, a selectivity of 16.
Pushing the Mg/Li ratio from 10:1 to 60:1 raises selectivity from 548 to 4,147,
because the more magnesium there is the more of it gets stopped.

This is a genuinely large number, one to two orders of magnitude above other
pressure-driven membranes and above the reported framework materials — and it is
the strongest available demonstration that a size-sieving membrane can be sharp
enough to separate ions that a bulk process cannot. It is also, for the
Pennsylvania application, measured on the wrong feed. Raising the total salt
concentration from 2,000 to 5,000 ppm at a fixed 20:1 ratio drops the
selectivity from 828 to **185** — a factor of 4.5 for a 2.5-fold increase in
salinity. Marcellus produced water is above 100,000 mg/L TDS, twenty times the
saltiest solution in that experiment, and the feed is a real brine with
calcium, barium, strontium and iron in it rather than a binary mixture of MgCl₂
and LiCl. Nothing in the paper licenses an extrapolation across that gap, and
the paper does not attempt one.

@smith2024critical make the general form of this criticism, and it is worth
quoting the shape of it: promising laboratory performance for direct lithium
extraction, including good lithium-to-magnesium separation, is largely obtained
on synthetic feeds, and "most are not tested with real brines that contain
multivalent ions that could impact overall performance indicators." The book's
recurring finding about rare earth separations — that headline selectivities are
measured on the easy pairs and in the easy media — has an exact analogue here.

### The adsorbent route, and the gap between theory and capacity

Membranes are one of two candidate mechanisms; the other is a selective solid.
The leading material is layered H₂TiO₃, the protonated form of Li₂TiO₃, which
takes up lithium by Li⁺--H⁺ exchange and rejects magnesium on size. Its appeal
over the λ-MnO₂ ion sieve is a stable titanium framework and a higher theoretical
capacity, **about 128 mg Li per gram** [@marthi2021lithium]. What is actually
achieved is a good deal less: the literature maximum under optimal conditions is
**below 50 mg/g**, and @marthi2021lithium measure **about 40 mg/g** on their own
material. A factor of three between the theoretical and the delivered capacity is
the kind of gap that decides whether a process is economic, and it had not been
explained.

Their explanation is mechanistic and it revises the accepted picture. Lithium
uptake had been understood as a straight ion exchange involving no bond breaking.
FTIR and Raman spectra instead show that Li⁺--H⁺ exchange **does** break surface
O--H bonds in the HTi₂ layers and form O--Li bonds, and that the hydroxyls which
participate are the isolated surface ones rather than the hydrogen-bonded
hydroxyls in the interlayer spacings. If only a subset of the available hydroxyl
sites is chemically accessible, the theoretical capacity was never the right
target, and the shortfall is structural rather than a matter of optimisation.

The practical reading for Pennsylvania is that adsorbent capacity is a second
constraint stacked on top of the selectivity constraint discussed above, and this
result narrows rather than widens the design space. It also, usefully, points at
what to change: the accessible capacity is set by the surface hydroxyl
population, which is a synthesis variable.

### What a concentrated lithium stream looks like

It is worth setting the produced water numbers against a lithium stream that is
*not* dilute, because the contrast is the whole argument. @kumari2021recovery
treat the effluent left after cobalt, copper, nickel and graphite have been
recovered from spent lithium-ion battery black mass: about **8 m³ of effluent per
tonne** of black cathode material, carrying **5--10 g/L manganese and 1--3 g/L
lithium**. At those concentrations the recovery step is precipitation with
saturated alkali — 30 minutes settling at about pH 12 gives roughly **90 %** of
the lithium as a salt — and no selective membrane or ion sieve is needed at all.

Marcellus produced water carries lithium at a median in the tens of milligrams
per litre ([](#what-pennsylvania-produces)). The battery-recycling effluent is
one to three grams per litre: **one to two orders of magnitude more
concentrated**, in a smaller volume, already inside a plant, and with a single
major competing cation rather than a brine full of them. Nothing about the
chemistry of lithium recovery is hard in that setting. What makes Pennsylvania
produced water hard is not the element and not the separation principle; it is
the concentration and the matrix, which is the same conclusion this chapter
reaches from every other direction.

(where-the-rare-earths-are-not)=
## Where the Rare Earths Are Not

The national inventory in @smith2024critical is the place to see why rare earths
are not the story. The study filtered the USGS National Produced Waters
Geochemical Database — about 115,000 samples — for five high-priority critical
minerals (cobalt, lithium, magnesium, manganese, nickel) and combined average
concentrations with 2017 produced water volumes by formation. Marcellus averages
came out at 76 mg/L Li (n = 232), 940 mg/L Mg, 5.0 mg/L Mn, 1.5 mg/L Co and
0.73 mg/L Ni, at an average TDS of 120,000 ± 80,000 mg/L. Lithium, nickel and
cobalt averages were highest in the Marcellus of any formation examined.

Set against 2022 US apparent consumption, the totals from all formations
combined look like this:

| Element | Total in produced water (2017), t/yr | US consumption 2022, t | Ratio |
|---|---|---|---|
| Mg | 900,000 ± 900,000 | 50,000 | 1,810 % |
| Li | 9,000 ± 30,000 | 3,000 | 300 % |
| Mn | 9,000 ± 20,000 | 890,000 | 1 % |
| Co | 9 ± 16 | 7,800 | 0.12 % |
| Ni | 20 ± 20 | 220,000 | 0.01 % |
| REE | 1 ± 2 | 9,300 | 0.01 % |

The standard deviations are as large as the estimates in several rows, and the
authors say so; these are order-of-magnitude statements, not resource estimates.
But an order of magnitude is all that is needed here. Cobalt, nickel, manganese
and the rare earths are present, and are present in quantities that could not
matter to US supply even at complete recovery. @smith2024critical put it
directly: recovery of manganese, cobalt and nickel from produced water would
have negligible impact on import reliance, though it might offset the cost of
treating the water, and "preliminary estimates suggest the total recovery of
REEs from PW will not have an impact on U.S. demand."

The measurements behind the rare earth row are thin, and the thinness is itself
worth recording. The USGS database contains no rare earth concentrations at all.
The figures come from a separate survey, reported through
@smith2024critical's Table 3, which found total rare earths (excluding Sc and Y)
of **1,100 ± 900 ng/L in Marcellus produced water — from two samples**, against
2,000 ± 2,000 ng/L in the Bakken from fifteen. A microgram per litre, with a
relative standard deviation near one, from a sample of two. That is not a
resource estimate; it is a detection.

Measuring it better is hard for a reason this book has met before. Rare earths
in a near-neutral high-TDS brine sit at nanogram-per-litre levels in a matrix
that interferes with the analysis: barium is abundant in Marcellus brines, and
barium oxide and hydroxide ions interfere with rare earth masses in ICP-MS. The
same paper notes that standardised methods and reference materials for highly
saline produced water do not really exist. Before anyone can say whether rare
earths in produced water are worth recovering, someone has to be able to measure
them reliably, and that capability is not yet routine.

What *is* well characterised is the rare earth content of the rock, and it is a
useful control. @noack2015rare analysed eleven Marcellus outcrop samples from
New York, Pennsylvania and West Virginia and six depth intervals from a core in
Greene County, Pennsylvania, taken between 7,780 and 7,920 ft. Individual rare
earths varied over three orders of magnitude, with 95 % of measurements between
0.324 and 75.2 ppm; most samples fell within the normal range for black shales.
Abundance tracked the clay fraction — samples with a major illite phase carried
about 98 ppm more total rare earths (95 % CI 39-158) — while the degree of
fractionation tracked the carbonate fraction, samples with major calcite being
roughly 400 % more fractionated but carrying 6-120 ppm less. The authors are
explicit that "little is known of the REE occurrence in the Marcellus Shale or
its produced waters," that structurally bound rare earths in clays may not be
released at all, and that produced water profiles therefore need not resemble
the bulk rock. Both halves of that statement matter: the shale is an ordinary
black shale by rare earth content, and the fraction of it that reaches the water
is unmeasured.

(why-the-marcellus-is-lithium-rich)=
## Why the Water Is Lithium-Rich

The lithium is a different story, and the reason it is a different story is
worth understanding, because it is the same host-phase argument that decides
whether phosphogypsum can be leached ([](#phosphogypsum)).

Marcellus produced water is enriched in lithium relative to other formations of
comparable salinity [@mackey2024estimates]. The formation was deposited
contemporaneously with Middle Devonian volcanism, and the interlayered volcanic
ash beds are the proposed source: lithium partitioned into pore fluids during
diagenesis. That the salinity itself is a basin-wide inheritance rather than a
local artefact is supported by @chapman2012geochemical, who measured strontium
isotope ratios in Marcellus produced waters across roughly 375 km of
Pennsylvania and found a narrow band — εSr relative to seawater of +13.8 to
+41.6 — distinct from Upper Devonian Venango-group brines and from western
Pennsylvania acid mine drainage. One source of dissolved solids, consistently,
across the play.

Where the lithium sits in the rock, however, sets a hard ceiling on how much of
it the water can ever carry. @phan2018role report that structurally bound
lithium — lithium inside clay minerals — accounts for **75-91 wt % of the total
lithium in the Marcellus Shale**, with less than 3 % extractable from exchange
sites and carbonate cement, and up to 20 % released by oxidation of sulfides and
organic matter. The lithium in the produced water is overwhelmingly the small,
accessible fraction. The large fraction is locked in a silicate lattice that
water at reservoir conditions does not dissolve on the timescale of a well.

That framing makes @donmoyer2023effect the interesting experiment. Working with
Marcellus core and synthetic fracturing fluid at formation temperature, they
compared three oxidative breakers used in the Appalachian Basin — ammonium
persulfate, sodium bromate, sodium hypochlorite — and found that the more
strongly oxidising fluids released substantially more of the critical elements:
total critical element concentrations were **439 % and 408 % higher** in the
sodium bromate and sodium hypochlorite effluents than in the ammonium persulfate
effluent. The elements detected were Li, Be, Al, Ti, V, Cr, Mn, Co, Cu, As, Mo,
Ag, Cd, Sb, Tl, U and Zn. The mechanism they propose is oxidative dissolution of
pyrite and degradation of organic matter, which is consistent with @phan2018role's
finding that oxidation is the route by which the non-exchangeable fraction moves.

It is a screening study on core samples, and the authors say so — they call for
further work before oxidative breakers could be used at field scale to enhance
critical mineral release. But it makes the shape of the opportunity clear, and
it makes the shape of the problem clear at the same time. The list of elements
that came out under oxidising conditions includes arsenic, cadmium, thallium,
lead and uranium alongside the lithium. You do not get to mobilise one without
the others.

(radium-and-what-else-comes-up)=
## Radium, and What Else Comes Up

This is the point at which Pennsylvania produced water stops resembling the
other unconventional feedstocks in [](#recycling-and-urban-mining) and becomes a
category of its own. Coal ash and phosphogypsum raise radiological questions
that depend on the source rock. Appalachian Basin brines raise them
unconditionally.

@blondes2020utica analysed sixteen Utica Shale Play wells in Ohio and
Pennsylvania and found total dissolved solids of 214-283 g/L, a chemistry
consistent enough over time and space to plan disposal around, an annual salt
output equivalent to **3.4 % of US halite production** — and **radium activities
580 times the EPA maximum contaminant level**, in brines already supersaturated
with respect to barite. Radium follows barium, barium is abundant, and barite is
the scale that forms.

@warner2013impacts show what that means downstream. At a brine treatment
facility in western Pennsylvania taking Marcellus produced water, barium and
radium were **reduced by more than 90 %** in the treated effluent — the treatment
worked — and yet ²²⁶Ra in the stream sediments at the discharge point measured
**544-8,759 Bq/kg**, roughly **200 times** the 22-44 Bq/kg of upstream and
background sediments, and above radioactive waste disposal thresholds. A
90 %-efficient removal step operating continuously on a stream with 580 times the
contaminant limit still concentrates radium in the receiving environment to a
level that would not be accepted in a waste facility.

The lesson generalises to any recovery process. @smith2024critical make the
point in the context of critical mineral extraction: naturally occurring
radioactive material in produced water can become concentrated in treatment
processes, and any process design has to say where the radium ends up. A lithium
extraction plant on Marcellus brine is also, whether or not it means to be, a
radium concentration plant, and the solid residue is the product that decides
whether the process is permittable. This is not a footnote to the flowsheet; for
this feedstock it is close to being the flowsheet's central constraint.

(what-treating-the-water-costs)=
## What Treating the Water Costs

There is one published techno-economic analysis close enough to be worth
reading, with its scope stated honestly. @wenzlick2020techno, also from NETL,
costed two centralised produced water treatment facility designs. The scope
caveats are real: the brines are from **Texas and Louisiana, not Pennsylvania**,
and the products are ten-pound brine and fresh water, **not critical minerals**.
The lithium content of their feed is 4 mg/L, against 127-205 mg/L in
Pennsylvania. It is not the Pennsylvania case. What it is, is a costed account
of the water handling that any Pennsylvania critical mineral scheme would have
to sit on top of.

Both designs remove oil, grease and suspended solids, reduce divalent ion
concentrations, and concentrate the brine to near NaCl saturation with
mechanical vapour recompression. The baseline design removes divalents by
chemical precipitation; the advanced design uses nanofiltration to separate
divalent from monovalent ions and reverse osmosis to pre-concentrate the brine
before the evaporator. Three findings carry over.

Chemical precipitation is cost-effective for low-hardness brines and
**cost-prohibitive at high hardness** — and Marcellus brine is very hard. Second,
the evaporator dominates: mechanical vapour recompression is the largest cost in
every case, with levelized costs more than twice those of the reverse osmosis
membranes, so the advanced design wins partly by shrinking the evaporator rather
than by any cleverness of its own. Third, nanofiltration is the promising
alternative to precipitation — with the condition the authors attach to it, that
it will improve the process greatly "if NF membranes are shown to be as
effective at high salinities."

That condition and @peng2024extreme's salinity result are the same open question
approached from two directions, and neither paper closes it. A membrane
engineer has demonstrated the selectivity at 2,000 ppm and watched it fall by a
factor of 4.5 by 5,000 ppm; a process engineer has costed a plant whose
economics turn on that membrane working at 100,000 ppm and above. As a
calibration point, @wenzlick2020techno cost their equipment against the
thermodynamic floor rather than against a competitor, and mechanical vapour
recompression comes in at **\$2.2 ± 0.3 per kWh of the theoretical minimum
separation work** — against \$0.9 ± 0.3 for reverse osmosis and \$1.4 ± 0.5
for nanofiltration, in 2017 dollars. The energy penalty behind that number is
larger still: a commercial-scale MVR unit on 50 g/L produced water draws about
40 kWh per m³ of distillate where the theoretical minimum for that salinity and
recovery is 2 kWh/m³, a second-law efficiency of 5 %. Treating this water is
not cheap even when nothing is being recovered from it.

(the-comparison-case)=
## The Comparison Case: Smackover

Pennsylvania is not the only oilfield brine being assessed this way, and the
comparison is useful because the more favourable case has the same structure.

@knierim2024evaluation applied a random forest model to lithium concentrations
in Smackover Formation brines in southern Arkansas, training on 544 brine
samples across the Gulf Coast in which lithium ranged from 0.08 to 1,700 mg/L.
The model reached an r² of 0.93 with a root mean square error of 36 mg/L,
underpredicting the high concentrations above 400 mg/L as tree-based models
generally do. Combined with reservoir thickness and porosity, the prediction
maps give **5.1 to 19 million tonnes of lithium** in the Reynolds oolite unit —
27 to 100 Mt of lithium carbonate equivalent — which is **35 to 136 % of the
current US lithium resource estimate** of 14 Mt.

Three things about that assessment are worth carrying back to Pennsylvania.

The Smackover is genuinely richer: predicted concentrations run to over
400 mg/L against Pennsylvania's 205 mg/L median in its best region, and southern
Arkansas already hosts a commercial brine industry producing bromine, so the
water is being lifted for other reasons. Second, the annual flow is a vanishing
fraction of the stock. On the basis of brine actually extracted in 2022,
approximately **5,000 t of lithium reached the surface — less than 0.1 % of the
resource** — as a waste stream of the oil, gas and bromine industries. A resource
number in the millions of tonnes and a production number in the thousands are
answering different questions, and only the second one is about supply this
decade.

And third: @knierim2024evaluation close by observing that those 5,000 t would
cover estimated US consumption for 2022 **assuming 100 % extraction efficiency**
— the identical assumption to @mackey2024estimates' 38-40 %. Two independent
assessments of two different basins arrive at the same framing, and it is a
framing that assigns all of the remaining difficulty to a separation step that
neither paper evaluates. That step is what the rest of this book is about, and
its history in the rare earth case suggests that "assuming 100 % recovery" is
where most of the cost lives.

(what-this-chapter-does-not-establish)=
## What This Chapter Does Not Establish

Several things that a reader might reasonably expect to find here are absent,
and the absences are deliberate.

There is no costed process for recovering lithium from Pennsylvania produced
water, because none has been published. @wenzlick2020techno costs water
treatment on other basins' brines; @mackey2024estimates and
@knierim2024evaluation size resources and stop at the plant gate;
@duchanois2023prospects survey which metals are worth pursuing from wastewater
and brine in general. The specific question — what does a tonne of lithium
carbonate from a Marcellus well cost — has no published answer, and the interval
between a resource estimate and a cost is exactly where most unconventional
feedstocks fail.

There is no rare earth recovery scheme for this water either, and on the
evidence assembled here there should not be. One tonne per year nationally, at
0.01 % of consumption, measured to a standard deviation twice the estimate, in a
matrix that defeats routine analysis, is not a resource. The correct research
question for rare earths in produced water is analytical before it is
preparative: establish reliable measurement in high-TDS brine, then revisit.
[](#brines-and-produced-water) treats what the recovery chemistry would have to
look like if the concentrations were ever shown to justify it, and
@noack2015rare's caution about release mechanisms is the right place to start.

There is no radiological assessment of a hypothetical extraction plant's solid
residues, because the published radium work
[@warner2013impacts; @blondes2020utica] measures brines and receiving
environments rather than process streams. That gap is the most consequential of
the three. The lithium arithmetic in this chapter is encouraging enough that the
binding constraint is unlikely to be whether lithium can be recovered; it is
likely to be what the plant does with the radium, and nobody has published that
number.

What can be said, and is worth saying plainly: Pennsylvania produced water is a
real lithium resource of national scale, an unremarkable rare earth resource of
no consequence, and a radium problem regardless of which of those you pursue.
The separation chemistry it needs is the Li⁺/Mg²⁺ problem, which is the same
problem as the one this book is about with one of the difficulties removed — and
the current best answer to it has been demonstrated at one twentieth of the
salinity of the feed. The arithmetic in
[](#environment-techno-economics-and-life-cycle) is where to take that next.
