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

They do not, however, share a weight of evidence, and the chapter is written to
reflect that. Membranes are a field: forty years of work, several hundred
papers, and a proper review literature to argue with [@chen2018overview;
@bashiri2022rare; @feng2026selective]. The porous-material work has one review
that covers it as a class [@oztug2024overview]. Everything after that — the MOF
nanotraps, the supramolecular receptors, the aqueous macrocycles, flash Joule
heating — is a handful of groups and, in several cases, a single paper. Where a
result in this chapter rests on one measurement by one laboratory and has not
been reproduced by anyone else, the text says so, and the reader should weigh it
accordingly.

Read the numbers with the same asymmetry in mind. A MOF nanotrap reporting a
separation factor of 796 is doing something no conventional extractant can
approach; it is also reporting it for a pair of elements at opposite ends of the
series, on a two-component synthetic solution, at milligram scale. The gap
between those two statements is where most of the remaining work lies, and the
chapters that follow on process economics
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

A third geometry drives the ions with a field instead of a pressure or a
concentration difference. In the configuration studied for rare earths, the feed
is complexed with EDTA and passed between two adjacent anion-exchange membranes,
so that the anionic Ln-EDTA complexes migrate and the uncomplexed cations do
not; the selectivity is the selectivity of the EDTA complexation, and the
membranes only sort by charge. @ding2024mathematical built and validated an
extended Nernst-Planck model of this cell for the separation of Dy from Pr and
Nd, and the useful part of the result is the shape of the trade-off rather than
a separation number. Raising the applied voltage above 8 V speeds the separation
and costs disproportionately more energy; dropping the rinse-solution
concentration below 0.05 mol/L improves energy efficiency but depletes the rinse
before the separation finishes; and the required rinse concentration scales
linearly with feed concentration, so a more concentrated feed is cheaper per
kilogram separated. The authors also identify the flaw in their own cell:
independent migration of sulphate carries current without carrying rare earths,
which caps the current efficiency, and they recommend alternating cation and
anion exchange membranes instead. That is modelling work on a laboratory cell,
not a demonstrated separation, and no throughput or product purity is reported.

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

The MOF result is the most striking number in this book and the one that most
needs its conditions attached to it, so this section states them all.

@hu2024rationally report a zinc carboxylate framework, NCU-1, built so that
two-fold interpenetration of the network leaves a dense population of small
cavities about 3.2 Å across, lined with uncoordinated carboxyl groups and
triazole nitrogens. The design argument is a size argument: the cavity is
matched to the larger, light lanthanide ions, and the multiple donor atoms
around it hold a well-fitting ion strongly enough that a poorly fitting one is
displaced. First-principles calculations put the binding order at Al³⁺ < Dy³⁺ <
Pr³⁺, which is the order the experiments show. This is not the same physics as
solvent extraction, where selectivity comes from the free-energy difference
between two complexes in solution ([](#solvent-extraction-fundamentals)); it is
closer to the size-matched crystallisation of
[](#precipitation-and-selective-crystallization), executed inside a rigid pore.

The separation factors were measured on binary mixtures. NCU-1 powder was
dispersed in an aqueous solution of two lanthanide nitrates in a 1:1 molar
ratio, at pH 4.5, and the two elements were counted in the supernatant
afterwards. Six such pairs were run. The headline pair, Pr/Lu, gave a
{index}`separation factor` of 796 and Nd/Er gave 273, but the same experiment gave
73 for Eu/Lu and 67 for Nd/Dy [@hu2024rationally]. That last number is the one to keep. Pr
and Lu sit at opposite ends of the lanthanide series; Nd and Dy are the pair a
magnet recycler actually has to separate, and there the framework delivers
roughly 67 rather than roughly 800. Sixty-seven is still an extraordinary
figure — more than an order of magnitude above the β ≈ 2–4 that D2EHPA achieves
on adjacent pairs ([](#solvent-extraction-fundamentals)) — and it is the figure
that should be quoted when the technology is compared against a cascade.

The uptake numbers need the same care. The capacities usually cited for NCU-1 —
420 mg/g for Pr, falling monotonically through 310 for Nd, 221 for Eu, 140 for
Gd, 126 for Dy, 97 for Er to 66 mg/g for Lu — are Langmuir *q*ₘ values fitted to
single-element isotherms at pH 4.5 [@hu2024rationally]. A Langmuir *q*ₘ is the
asymptote of a fitted curve, not a loading anyone measured; it is the right
quantity for comparing sorbents against each other and the wrong one for sizing
a column. What the pH dependence adds is a harder constraint: the distribution
coefficient rises from pH 2 to a maximum at 4.5 and falls again by pH 6, so the
entire useful window sits in mildly acidic water. A sulphuric or hydrochloric
leach liquor from [](#hydrometallurgical-leaching) arrives at pH below 1 and
would have to be neutralised before it could be fed to this material at all —
which is a unit operation, a reagent bill, and a precipitation risk that none of
the reported experiments include.

On a real feed the framework was tested against mine tailings water from
Ganzhou, Jiangxi. That water is near-neutral and dilute: total rare earths at
0.09–0.92 ppm against 8.15 ppm of aluminium, roughly ten times more of the
interferent than of the target [@hu2024rationally]. NCU-1 captured the rare
earths selectively from it, with a breakthrough bed volume of 150 for Pr against
80 for Dy — that is, the light element both loads more and elutes later, which
is the separation working in column form. The distribution coefficient for rare
earths runs three to four orders of magnitude above that for the alkali and
alkaline-earth ions, so the group separation from ordinary water chemistry is
not in doubt.

The cycling claim is the one most likely to be over-read. What is reported is
four sorption/desorption cycles, with the loaded rare earths stripped by dilute
nitric acid at pH 3 and the crystallinity confirmed by powder XRD after the
fourth [@hu2024rationally]. Four cycles on a clean strip is evidence that the
framework is not destroyed by its own regeneration; it is not evidence of
lifetime in service, and the paper does not claim it is. A sorbent in a real
circuit is cycled thousands of times against a liquor carrying iron, aluminium,
silica and organics, and the failure modes that matter — irreversible fouling,
slow hydrolysis of the linker, attrition of the crystallites — do not appear in
four cycles.

Everything above is one paper from one group. The class it belongs to has a
review [@oztug2024overview], and the NCU-1 paper's own introduction places the
result against the earlier and much weaker MOF sorbents — hydroxyl-decorated
frameworks giving separation factors below 2, Zn-BTC on nanoporous graphene at
about 30 for Nd/Dy [@hu2024rationally] — so the improvement over the previous
state of the art is not in doubt. What is missing is that no independent
laboratory has reproduced the 796, and the scale is milligrams of powder in a
vial. Treat it as the best current
evidence that a designed pore can out-select a designed ligand, and not yet as a
measured property of a material anyone can buy.

## Supramolecular Encapsulation and Precipitation

A second line of work amplifies the small size differences across the series by
building a receptor that encapsulates a rare earth complex and then, crucially,
makes the encapsulated product insoluble. Separation by precipitation has a
practical attraction the solvent-extraction cascade lacks: the product leaves
the system as a solid, so there is no organic inventory to lose and no phase
disengagement to design for.

@oconnelldanes2022selective introduced the platform — a pre-organised
triamidoarene that, under acidic biphasic conditions, selectively precipitates
light rare earth *nitratometalates*, [Ln(NO₃)₆]³⁻, as supramolecular capsules
held together by intra- and intermolecular hydrogen bonds. The point of the
design is that the receptor recognises the anionic nitrate complex rather than
the bare cation, which is why it tolerates an acidic feed: no pH adjustment is
needed to make the target species, because nitric acid makes it already.

The application came two years later. @oconnelldanes2024simple report
single-step, near-quantitative recovery of Nd and Pr directly from the acidic
leach solution of magnet scrap, with no pH adjustment and no pretreatment; the
rare earth nitrate is then stripped from the host-guest precipitate with plain
water and the receptor recycled. The same receptor takes La-Nd near
quantitatively from lateritic rare earth ore with, in the authors' words, no
uptake of any non-f-element. Two things follow from that phrasing and are worth
stating rather than glossing. First, this is a group separation — light rare
earths out, everything else left behind — and not an intra-series one; the
paper reports no separation factor between adjacent lanthanides. Second, "no
non-f-element" includes thorium, which the same paper reports taking up from the
lateritic ore, so the product of that particular application carries a
radioactive contaminant into the next step ([](#thorium-management)).

The related work on M₄L₄ tetrahedral cages [@li2018supramolecular] belongs here
as a design principle rather than as a separation result. Self-assembled from a
tris-tridentate ligand, those cages show high-precision metal-ion self-sorting:
a mixture of metals does not give a statistical mixture of cages but sorts
itself into homometallic ones. That is a genuinely surprising piece of
coordination chemistry and the authors present it as a route to
next-generation extractants; they do not report a separation factor, a
recovery, or a purity for a lanthanide mixture, and none should be quoted from
it.

All three papers come from two groups. Nothing in this section has been
reproduced independently or run above bench scale.

## Aqueous Macrocyclic Chelators

Closely related in spirit, and the most recent of these results, is a route that
does the precipitation in water at neutral pH with no organic phase at all.
@jones2025macrocyclic report cyclen-based macrocyclic chelators whose lanthanide
chelates differ enough in solubility that they can be precipitated selectively
from pH-neutral aqueous solution, with the differences tuned further by adding a
simple coordinating co-ligand such as acetate to form ternary complexes. Applied
to the element mix found in NdFeB magnets, repeated precipitations separate even
adjacent lanthanides, and a magnet taken from a current automotive motor was
processed to a 99.7 % pure neodymium product.

The authors state that separation factors comparable to those of industrial
solvent extraction were achieved without organic solvents. That is their
comparison and it is the right claim to make, but note what "repeated
precipitations" concedes: if the per-stage separation factor is comparable to
solvent extraction, then the number of stages is comparable too, and this is a
cascade in a different physical form rather than an escape from one. The
quantity to ask for — how many precipitation cycles the 99.7 % product took, and
what the yield was after them — is the same quantity that governs a mixer-settler
circuit ([](#process-modeling-and-optimization)).

The same paper contributes an unrelated and immediately useful observation.
Analysing magnets from current electric vehicle motors, the authors found
holmium being used as a supplement to or replacement for terbium and dysprosium
— an element that recycling flowsheets designed around Nd, Pr, Dy and Tb are not
looking for, and will therefore lose ([](#recycling-and-urban-mining)).

## DGA Ligands and the Value of a Larger Separation Factor

The diglycolamide work out of Oak Ridge and Idaho National Laboratories is the
least exotic entry in this chapter and, for that reason, the closest to use. It
is also the clearest illustration of why a separation factor is the number that
matters.

The incumbent extractant for adjacent light lanthanides is PC88A, and its
separation factor for the Nd/Pr pair is about 1.2 [@laboratory2021game]. Most
rare earth extractants sit around 1.5 across the series. A β that close to unity
is what forces the hundred-stage cascades of
[](#solvent-extraction-fundamentals); the chemistry is barely selective and the
process makes up for it by running the barely selective step many times.
Diglycolamides bind lanthanides through their ether and amide oxygens with a
preference for the smaller, heavier ions, and TODGA — the standard DGA — reaches
about 2.5. That is a large improvement, and for two decades it did not matter,
because TODGA could be loaded to only about a fifth of the metal concentration
PC88A tolerates before the organic phase gels or a third phase forms
[@laboratory2021game]. A cascade run at one-fifth the loading needs five times
the solvent circulation for the same throughput, which erases the benefit of the
better selectivity.

What @stamberga2020structure did was to attack that constraint directly, by
systematically varying the substituents around the diglycolamide carbonyl
oxygens — twelve new ligands beyond the three the literature had been recycling
— to separate the steric from the electronic contribution to selectivity. The
resulting ligands hold selectivity in the 2.5–3.1 range while staying
homogeneous at extractant concentrations high enough to be industrially useful
[@laboratory2021game]. The technology was licensed to Marshallton Research
Laboratories in 2021 under an exclusive field-of-use agreement, with the process
design developed at Idaho National Laboratory.

Two cautions. A licence is a commercial event and not a demonstration: no plant
has been reported running on these extractants, and the scale-up questions that
[](#the-industrial-landscape) raises for every new circuit apply here unchanged.
And a separation factor of 3 does not make the cascade go away — it shortens it.
That is worth a great deal, because stage count drives both capital and solvent
inventory ([](#process-modeling-and-optimization)), but the flowsheet at the end
is still a countercurrent cascade of mixer-settlers.

## Chemical Separation of Rare Earth Oxalates (CSEREOX)

Oxalate precipitation is the last step of nearly every rare earth flowsheet
([](#hydrometallurgical-leaching)), and it is unselective: the whole series comes
down together as insoluble oxalates. @boronski2020rationally invert that. Rather
than trying to precipitate one element preferentially, CSEREOX precipitates
everything and then selectively *re-dissolves* part of it, using an organic base
to solubilise the normally water-insoluble oxalates of one rare earth subgroup
while leaving the others as solids. The distinction matters and is frequently
reported backwards: the selectivity lives in the dissolution step, not in the
precipitation.

What the authors demonstrate is separation within, rather than between,
subgroups, and they show it working on processed magnet waste at initial rare
earth concentrations below 5 %, which is the regime where a solvent-extraction
circuit is at its least economic. No separation factor, purity or stage count
from this work has been verified for this chapter; it is a four-page
communication from 2020 out of the Critical Materials Institute, and no
independent replication or scale demonstration was found.

## Flash Joule Heating with Chlorination (FJH-Cl₂)

A 2025 result combines {index}`flash Joule heating` with {index}`chlorination` to
recover rare earths from **waste magnets**, exploiting the differences in free
energy of formation and boiling point among the metal chlorides
[@xu2025sustainable]. The chemistry is chlorination, so the full treatment sits
in [](#flash-joule-heating-with-chlorination); the reported performance is
repeated here for comparison against the other technologies in this chapter.

Two of the figures below are laboratory measurements and the rest are not. The
purity and yield were measured on the demonstration; the reductions in energy,
emissions, cost, water and acid are outputs of a life-cycle assessment and
techno-economic analysis comparing a modelled FJH-Cl₂ process against
conventional routes, not plant data [@xu2025sustainable]. The "100 %
elimination of water and acid" applies to the chlorination step itself, and does
not carry the downstream separation of the mixed chloride product, which still
has to happen somewhere.

*Measured on the demonstration:* rare earth purity above 90 % and rare earth
yield above 90 %, in a single step, from waste magnets.

*Modelled by LCA and TEA against a conventional route:* a threefold reduction in
the number of process steps, an 87 % reduction in energy consumption, an 84 %
reduction in greenhouse gas emissions, a 54 % reduction in operating cost, and
complete elimination of water and acid use — for the chlorination step alone.

## Bioseparation

Biological and biomimetic separations are treated in full in
[](#biological-and-biomimetic-separations) and only pointed to here, because one
number from that field is quoted more often and more wrongly than any other in
this book. {index}`Lanmodulin <lanmodulin>` is often described as having about
10⁸-fold selectivity for lanthanides. That figure is for lanthanides *over
calcium* — a group separation — and the protein binds every lanthanide from La
to Lu at nearly the same picomolar affinity, so its discrimination *between*
rare earths is weak. The two numbers differ by seven orders of magnitude and
must not be quoted interchangeably. Engineered dimeric variants do fractionate
the series, but the affinity ratios usually cited for them are for La against
Dy — opposite ends of the series — not for an adjacent pair.
[](#biological-and-biomimetic-separations) gives both numbers and the
demonstrated single-stage purities, and covers the rest of the field:
lanthanide-binding peptides at air-water interfaces, rhamnolipid biosurfactants,
microbial {index}`biosorption` on bacteria, yeast and algae, and phytomining with
hyperaccumulator ferns.

## Supercritical Fluid Extraction

Supercritical CO₂ above its critical point (31.1 °C, 7.38 MPa) is a tunable,
non-toxic, recyclable solvent, and the case for using it on rare earths is that
it replaces both the organic diluent and much of the aqueous acid inventory of a
conventional flowsheet. What it cannot do is dissolve a rare earth ion. CO₂ is a
weak Lewis base and a nonpolar medium, so a charged, hydrated Ln³⁺ has no route
into it. Three conditions have to be met before a metal will dissolve in a
supercritical fluid at all: its charge must be neutralised, its coordination
sphere must be satisfied, and the resulting complex must be lipophilic
[@lin1994supercritical]. Everything in this section is therefore a story about
the ligand dissolved in the CO₂, not about the CO₂.

The workhorse ligand is the {index}`tributyl phosphate <TBP (tributyl phosphate)>`-nitric acid adduct. Nitrate
neutralises the Ln³⁺ charge, TBP displaces the coordinated water, and the
resulting Ln(NO₃)₃·*n*TBP complex is soluble in the supercritical phase.
Fluorinated β-diketones — hexafluoroacetylacetone, thenoyltrifluoroacetone and
their relatives — do the same job by a different route and show a synergistic
enhancement when TBP is added alongside them [@lin1994supercritical;
@lin1995supercritical]. Fluorinated organophosphate derivatives of TBP have been
proposed more recently on the grounds of higher CO₂ solubility
[@deng2024maximized], though the solubility values themselves could not be
verified for this chapter and are not quoted here.

### Bastnäsite: The One Well-Documented Result

The best-characterised supercritical extraction of rare earths from a real ore
is INL and Cornell's work on Mountain Pass {index}`bastnäsite <bastnäsite>` concentrate
[@sinclair2017rare], and it is worth reporting in full because it is unusually
honest about what the technique does and does not buy.

Pretreatment is not optional. Untreated bastnäsite concentrate gave recoveries of
1–3 % for La, Ce, Pr and Nd; the fluorocarbonate has to be broken down before the
adduct can reach the metal. Two industrial pretreatments were compared: dry
roasting at 730 °C for three hours, and digestion in 50 % NaOH at 150 °C for four
hours. Extraction was then run at 34 MPa and 65 °C with TBP-HNO₃ adducts spanning
2 to 6 mol/L H⁺. Recovery was fastest at about 4 M HNO₃ and fell at higher
acidity, which the authors attribute either to condensation of an aqueous phase
that re-sequesters the metal or to nitric acid competing with the lanthanide
nitrates for TBP — the same competition seen in conventional TBP extraction
([](#solvent-extraction-fundamentals)).

At 4 mol/L H⁺ and about 5 mol % adduct in the CO₂, the roasted concentrate gave
72 % La, 96 % Ce, 88 % Pr and 90 % Nd after 120 minutes; the NaOH-digested
concentrate gave 93 % La, 100 % Ce, 99 % Pr and 101 % Nd after only 90 minutes.
Caustic digestion is the faster route, and the difference is largest for
lanthanum.

Now the two conclusions that a bullet list would have hidden. First, in the
authors' own summary, those recoveries are *similar to conventional leaching with
concentrated nitric acid* — supercritical CO₂ does not recover more rare earth
than an acid leach does. What it recovers is less of everything else: at the same
conditions, calcium recovery was about half that of the nitric leach, and barium
and strontium were generally below the reporting limit. The selectivity is over
gangue, and that is the actual product of the technique. Second, heavier
lanthanides extract faster — Nd extraction rates ran 30–100 % faster than La —
because of their greater affinity for TBP. That is a kinetic trend across the
series, not a separation, and the paper closes by saying that separation of
individual rare earths from the supercritical phase remains to be demonstrated.

### Other Feeds

The same TBP-HNO₃ chemistry has been carried to other materials, in every case at
bench scale. A Canadian concentrate holding its rare earths inside zircon
required NaOH cracking before near-complete extraction became possible, and the
mineralogical study alongside it showed hematite converting to magnetite during
the cracking step [@li2024optimization]. {index}`Coal fly ash <coal fly ash>` has been treated with
supercritical CO₂ and multistage stripping for selective recovery
[@zhu2023supercritical], and separately with TBP-HNO₃ on coal by-products
[@veerla2025investigation]. Acid mine drainage from anthracite regions has been
processed by a combined coagulation and complexation route, with wastewater
remediation as a co-benefit [@song2021extraction].

Coal ash is worth a grade check before it is called a resource. Taggart and
co-workers measured more than a hundred U.S. ashes and found total rare earths
averaging 591 mg/kg for Appalachian coals, 403 mg/kg for the Illinois basin and
337 mg/kg for the Powder River basin [@taggart2016trends] — hundreds of parts per
million, two to three orders of magnitude below a monazite concentrate, and the
argument for it is tonnage and disposal liability rather than grade
([](#recycling-and-urban-mining)).

The greenest variant on offer replaces the phosphate ligand entirely. Sandia
reports extracting rare earths from coal and coal ash using only water,
supercritical CO₂ and food-grade citric acid, guided by thermodynamic and DFT
modelling, at 42 % extraction efficiency with a preference for the more critical
elements [@labs2024green]. That figure comes from a laboratory technology-transfer
listing rather than a peer-reviewed paper, and 42 % is well below what the
TBP-HNO₃ systems achieve; it is reported here because the reagent list is
genuinely benign, not because the performance is competitive.

### A Design Study, Not a Plant

The largest number attached to this route is a technoeconomic analysis of a
hypothetical facility in Ontario built around 4,000 L supercritical extraction
reactors, processing the zircon-rich concentrate of @li2024optimization
[@azimi2025technoeconomic]. Nothing in it was measured: the reactor volume is a
design choice and the costs are modelled from it. The study puts total capital
expenditure at \$13.7–14.6 million and first-year operating expenditure at close
to \$3 million, with payback ranging from 6.9 years in the most favourable
scenario to 12.8 years in the least. Profitability is most sensitive to rare
earth prices — Nd₂O₃, Dy₂O₃ and Tb₄O₇ in particular — and then to reagent and
utility costs, which is the same conclusion [](#environment-techno-economics-and-life-cycle)
reaches for every route in this book.

Every supercritical-CO₂ result cited in this chapter is bench-scale, and none of
the sources reports the vessel size it was obtained in. The gap between that and
a 4,000 L reactor is the whole of the scale-up problem, and it is unmeasured.

### What Supercritical Extraction Is Actually For

Read together, the evidence supports a narrower claim than the one usually made
for it. Supercritical CO₂ does not consume an organic diluent and does not
generate the aqueous acid raffinate volumes of a conventional leach, its solvent
power is tunable with pressure and temperature, and the CO₂ itself is non-toxic,
non-flammable and recyclable. Against a nitric leach it demonstrably rejects
gangue better [@sinclair2017rare], which is a real advantage on a
calcium-rich or barium-rich concentrate.

But it is not reagent-free: the TBP and the nitric acid are still consumed, and
the pretreatment that makes the ore extractable at all — roasting at 730 °C or a
four-hour caustic digestion — carries its own energy and reagent burden, which
none of the comparisons above account for. It requires high-pressure vessels,
which is capital, and CO₂ compression and recycle, which is parasitic load. And
it has not been shown to separate individual lanthanides. The size trend across
the series is real but slight, and every source reviewed here defers individual
separation to a downstream step that is not part of the supercritical process.
Supercritical extraction is therefore a candidate replacement for the leach in
[](#hydrometallurgical-leaching), on feeds where gangue rejection is worth
paying for. It is not a candidate replacement for the separation in
[](#solvent-extraction-fundamentals), and no source verified for this chapter
claims that it is.
