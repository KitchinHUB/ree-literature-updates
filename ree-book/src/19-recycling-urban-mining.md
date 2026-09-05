---
title: Recycling and Urban Mining
---

(recycling-and-urban-mining)=
# Recycling and Urban Mining

End-of-life magnets, phosphors, and catalysts are a rare earth ore with an
unusual property: the hard part of the separation has already been done. An
{index}`NdFeB` magnet is a concentrated, largely known mixture of a few elements, not a
dilute mixture of seventeen in a silicate matrix. The chemistry of recovering
rare earths from it is therefore closer to the chemistry of purification than
to the chemistry of mining.

The obstacle is not chemical but logistical — collection rates, sorting, and the
economics of a feedstock that arrives in small, dispersed, heterogeneous
batches. Present global recycling rates for rare earths sit below one percent
for that reason, not because the processes do not work.

Several routes covered elsewhere in this book target this feedstock directly:
{index}`carbochlorination` of magnet scrap ([](#pyrometallurgical-and-halogenation-routes)),
{index}`flash Joule heating` ([](#membranes-mofs-and-emerging-approaches)), and
macrocyclic chelator {index}`precipitation`
([](#precipitation-and-selective-crystallization)).

## The Feedstocks and What Is Actually in Them

"Urban mining" is a single phrase covering feedstocks whose rare earth contents
span three orders of magnitude. The table below gives measured compositions
from the primary literature; the point of collecting them in one place is that
the recovery route, and whether a route can pay for itself, follows almost
entirely from the grade and from what the rare earths are mixed with.

| Feedstock | Rare earth content | Elements present | Notes on the stream |
|---|---|---|---|
| Sintered {index}`NdFeB` magnets, end of life | 31-32 wt% REE [@yang2017ree] | Nd, Pr, with Dy and Tb in high-coercivity grades | Unit mass runs from under 1 g in small consumer electronics to about 1 kg in electric and hybrid vehicles and 1000-2000 kg in the generators of modern wind turbines; service life 2-3 years in consumer electronics to 20-30 years in turbines [@yang2017ree] |
| NdFeB manufacturing {index}`swarf` | 25.5 wt% RE, balance 73.7 wt% Fe [@prodius2019sustainable] | Nd, Pr | Pre-consumer, single-composition, already collected at the magnet plant — the easiest feed in the table |
| Shredded hard disk drives | Magnet fraction \~8.8 wt% of the shredded mass; the magnet itself 22.6 wt% RE [@prodius2019sustainable] | Nd, Pr, with 6.2 wt% Ni and 2.2 wt% Cu in the magnet from the plating | Shredding mixes the magnet with steel, aluminium, and polymer |
| Shredded small electric motors | Magnet fraction \~11.7 wt% of the shredded mass [@prodius2019sustainable] | Nd, Pr, Dy | As above |
| Fluorescent lamp {index}`phosphor` powder | \>23 wt% REE [@tan2016innovative] | {index}`Yttrium <yttrium>`, {index}`europium`, {index}`terbium`, La, Ce | The phosphor is only 2-3 wt% of the lamp mass [@tan2016innovative], so the powder must be separated from glass and mercury first |
| Spent {index}`NiMH <nickel-metal hydride (NiMH)>` battery black mass | \~16 wt% total REE (Ce 6.2, La 5.5, Nd 2.4, Pr 1.9) [@weshahy2022efficient] | Ce, La, Nd, Pr | Dominated by 45.8 wt% Ni and 4.2 wt% Co [@weshahy2022efficient]; the nickel and cobalt, not the rare earths, are what pay for the process |
| Spent {index}`FCC <fluid catalytic cracking (FCC)>` catalyst | 1.49 wt% La [@sposato2021towards] | La, some Ce | Roughly 30,000 t/y of rare earth oxide is consumed in fluid catalytic cracking and automotive catalysis [@sposato2021towards]; contaminated with Ni and V from the crude |
| {index}`Coal fly ash <coal fly ash>` | Hundreds of ppm ([](#membranes-mofs-and-emerging-approaches), [](#microfluidic-separations)) | Whole series, La-Lu, Y | Two to three orders of magnitude below the others — see below |

Two things in this table matter more than the individual numbers. First, the
value is not distributed like the mass. In lamp phosphors, {index}`terbium` and
{index}`europium` together account for over ninety percent of the value of the
contained rare earths and yttrium for about seven percent, despite yttrium
being the dominant element by mass at 21 wt% [@tan2016innovative]. A process
optimized for mass recovery and a process optimized for value recovery are not
the same process. Second, every stream except magnet swarf arrives mixed with
something that must be removed before any lanthanide-lanthanide separation
begins — iron, nickel, glass, vanadium — which is the same problem that
dominates primary hydrometallurgy ([](#hydrometallurgical-leaching)).

## How Little Is Actually Recycled

The figure usually quoted for rare earths is an end-of-life recycling rate
below one percent, and it is worth knowing where it comes from, because the
number is often cited to reviews that are themselves citing it.

The primary assessment is the UNEP International Resource Panel's status report
on metal recycling rates, which found that of some sixty metals surveyed fewer
than a third had an end-of-life recycling rate above 50 %, while thirty-four
were below 1 %; the rare earths are in that lowest group, and the report singles
out neodymium and dysprosium for wind turbine magnets and lanthanum for hybrid
vehicle batteries [@unep2011recycling]. The peer-reviewed
statements of the same work-up are Graedel and co-workers in the *Journal of
Industrial Ecology* [@graedel2011what] and Reck and Graedel in *Science*
[@reck2012challenges]. Binnemans and co-workers' critical review is the
standard survey of why the number is what it is and of the routes that would
change it [@binnemans2013recycling]; Yang and co-workers, reviewing the magnet
case specifically, put it flatly — at the time of writing no commercial
operation for recycling end-of-life NdFeB magnets had been identified
[@yang2017ree]. Fifteen years after the UNEP report the USGS still records only
that "limited quantities of rare earths were recovered from batteries,
permanent magnets, and fluorescent lamps" [@usgs2026mineral].

The reasons are collection, not chemistry: magnets are glued or welded inside
sealed assemblies, lamps are dispersed across households, and the recovered
metal competes against a primary supply chain operating at the bottom of a
sixty-year learning curve ([](#the-industrial-landscape)).

## Routes for Magnet Scrap

Four families of route are established well enough to have reported recoveries
on real scrap. They differ in how much of the original engineering they
preserve.

### Direct reuse: hydrogen decrepitation and re-sintering

The least destructive route keeps the alloy. {index}`Hydrogen decrepitation <hydrogen decrepitation>`
exploits the fact that the Nd-rich grain-boundary phase in a sintered magnet
absorbs hydrogen and expands, breaking the magnet into a friable powder that
falls away from the surrounding steel and polymer. Walton and co-workers
applied this to magnets inside whole hard disk drives and reported an
extraction efficiency of 90 ± 5 %, with the recovered powder retaining about
90 % of the magnetic properties of the starting material and requiring
substantially less energy than primary magnet production [@walton2015use].
Zakotnik and co-workers showed the alloy survives the cycle repeatedly, with
sintered magnets recycled multiple times by hydrogen processing and re-sintering
[@zakotnik2009multiple].

This is the route with the clearest environmental case. A life cycle assessment
of magnet-to-magnet recycling for electric vehicle motors found impacts 64-96 %
lower than virgin production across the categories assessed [@jin2018life] —
the same result discussed in
[](#environment-techno-economics-and-life-cycle). Its limitation is equally
clear: the output is a magnet alloy of whatever composition went in. It cannot
correct a composition, cannot separate Dy from Nd, and cannot handle mixed or
unknown scrap. It is a purification route, not a separation route.

### Oxidative roasting, selective leaching, and oxalate precipitation

Where the composition must be changed, the magnet has to be taken back to
oxides. The standard hydrometallurgical sequence oxidizes the iron
deliberately so that it does not follow the rare earths into solution.
Patcharawit and co-workers compared this against simply dissolving everything:
roasting the magnet waste in air at 600 °C, leaching in sulfuric acid, roasting
again at 750-800 °C, water leaching, precipitating with oxalic acid, and
calcining at 1000 °C recovered 75.5 % of the rare earths from sintered magnet
waste, against 31.6 % for whole leaching of the same material. The oxide
product from the selective route ran 68.1 wt% neodymium, 19.8 wt%
praseodymium, and 0.31 wt% iron, against 1.20 wt% iron by whole leaching
[@patcharawit2022comparative]. Sulfation followed by selective roasting and
water leaching achieves the same separation of iron from rare earths through a
different intermediate [@onal2015recycling].

The {index}`oxalate precipitation` and calcination steps
at the end are the same operations used on primary leach liquors
([](#precipitation-and-selective-crystallization)); once the iron is gone, a
magnet leachate is a light-rare-earth mixed feed like any other, and the
downstream Nd/Pr split is conventional {index}`solvent extraction`
([](#solvent-extraction-fundamentals)).

The Nd/Dy split, which matters more for magnet scrap than Nd/Pr does, has one
non-solvent demonstration on a realistic ratio, and it is instructive about
where the difficulty lies. Dong and co-workers loaded a 95:5 Nd:Dy feed —
magnet-scrap composition — onto an immobilized-lanmodulin column and found that
it does not separate in a single pass: one adsorption/desorption cycle gave
88.6 % of the dysprosium at only 46.1 % purity. Passing the pooled fraction
through a second cycle gave 88 % of the Dy at 99.2 % purity and 82 % of the Nd
at 99.9 % [@dong2021bridging]. On a 50:50 feed the same column reaches 99.9 %
purity on both products in one cycle, at about 76 % recovery of each. The feed
ratio, not the chemistry, sets how many cycles are needed
([](#biological-and-biomimetic-separations)).

### Acid-free leaching with copper salts

An alternative avoids mineral acids entirely by using a copper(II) salt as the
oxidant, so that copper is reduced to Cu₂O and Cu while iron and the rare
earths go into solution as nitrates, chlorides, or sulfates. Prodius and
co-workers demonstrated this on four feeds without external heating: 0.5 kg of
(Nd,Pr)-Fe-B swarf stirred with copper(II) nitrate in water for about five
hours, then ammonia to precipitate the hydroxides, oxalic acid at 80 °C, and
calcination at 800 °C in air gave 146.7 g of rare earth oxide at greater than
98 % yield and 99.6 wt% RE purity. Hydrogen-decrepitated magnets from hard disk
drives dissolved in about thirty minutes at room temperature. On shredded
e-waste the recovery falls: 73 wt% of the contained rare earths from shredded
hard disk drives and 65 wt% from a shredded electric motor, at greater than
99.9 % product purity, with the shortfall attributed to solution access to the
magnet surfaces and an estimate that better shredding would reach 80-85 wt%.
The same chemistry applied to Sm-Co swarf gave about 97 % Sm₂O₃ recovery at
greater than 99.9 wt% purity, with the cobalt recovered separately as the
phosphate [@prodius2019sustainable].

The attraction is not the recovery, which is comparable to the roast-leach
route, but the reagent inventory: no volatile mineral acid, no external heat,
and the copper leaves as a saleable oxide rather than as a waste stream.

### Pyrometallurgical and electrochemical routes

The high-temperature routes skip the aqueous stage. Their appeal is that they
produce metal or alloy directly, which is where a magnet maker needs the
material anyway; their difficulty is materials of construction and the handling
of molten halides. Firdaus and co-workers survey the field of high-temperature
Nd and Dy recovery from magnet waste [@firdaus2016review]. Chung and co-workers
took oxidized and carbothermically reduced magnet scrap — a
magnet-recycling-derived oxide running roughly 33 wt% Nd and 10 wt% Pr — and
electrochemically reduced it on molybdenum electrodes in NdF₃-LiF and
NdF₃-PrF₃-LiF fused salts, confirming metallic Nd and Pr at the cathode by XRD
[@chung2023recovery]. The conversion of rare earth oxides to fluorides in
molten fluoride baths, which is the enabling step, is treated by Abbasalizadeh
and co-workers [@abbasalizadeh2017electrochemical]. Related work eliminates
hydrogen fluoride from the metal-production step by using an alternative
feedstock [@karati2025rare]. Molten-salt electrolysis, carbochlorination, and
the rest of the halide chemistry are developed in
[](#pyrometallurgical-and-halogenation-routes) and are not repeated here.

## Phosphors, Batteries, and Catalysts

**Lamp phosphors** are the richest feed by grade, but the rare earths sit in
refractory host lattices — Y₂O₃:Eu, LaPO₄:Ce,Tb — that resist direct acid
attack. Tan and co-workers showed that the barrier is structural rather than
thermodynamic, and that it is element-specific. After ball-milling at 700 rpm
for 120 minutes, terbium, cerium, and lanthanum leached at better than 80 %,
65 %, and 80 % respectively, against under 3 % for the same acids on unmilled
phosphor -- but europium and yttrium leached the same either way, with any
acid, because they are not held in the refractory phosphate. Under optimized
conditions (600 rpm for 60 minutes, then 6 M HCl at 60 °C for 15 minutes) the
process gave 89.4 %, 93.1 %, and 94.6 % dissolution for terbium, europium, and
yttrium [@tan2016innovative]. The
practical difficulty for this stream is now that it is shrinking — fluorescent
lighting is being displaced by LEDs, which use far less rare earth per lumen.

**Spent NiMH batteries** carry the rare earths as a minority phase in the AB₅
electrode powder, and the separation that matters first is rare earths from
nickel and cobalt. Two published routes bracket the options. Weshahy and
co-workers leached with 300 g/L ammonium sulfate at 120 °C for 180 minutes and
dissolved 99.98 % of the rare earths along with almost all the zinc, leaving
the nickel and cobalt in the residue [@weshahy2022efficient]. Ahn, Swain, and
co-workers went the other way: 1 M sulfuric acid at 90 °C dissolved everything,
then more than 99 % of the rare earth metals were precipitated at pH 1.8 with
10 M sodium hydroxide and isolated by calcination at 600 °C, with the base
metals subsequently split by D2EHPA and Cyanex 272 extraction
[@ahn2020valorization]. Which is preferable depends entirely on whether the
plant is being built around the rare earths or around the nickel.

**Spent FCC catalyst** is the largest single stream by tonnage and the leanest
of the concentrated feeds. Sposato and co-workers mapped acid concentration
and temperature against each other: at room temperature, lanthanum recovery
plateaus around 60 % however strong the acid (35-38 % at 0.1 N), but heating
lifts it, and 5 N nitric acid at 80 °C takes lanthanum recovery close to 100 %.
The catch is that selectivity moves the other way — it peaks near 40 °C and
falls off above it as aluminium and iron start dissolving too — so the working
point they characterize is 5 N nitric acid at 60 °C. Coupling that leach to
oxalate precipitation gives a lanthanum solid of greater than 98 % w/w purity,
with the nickel and vanadium poisons together accounting for about 0.2 % of the
precipitate [@sposato2021towards]. Lanthanum is also the cheapest rare earth on the market,
at around \$1/kg for the oxide [@usgs2026mineral], which is the real constraint
on this stream.

## Coal Ash: Tonnage, Not Grade

Coal and coal ash are frequently described as a rare earth resource, and the
description needs qualifying. Coal fly ash carries rare earths at the level of
hundreds of ppm ([](#membranes-mofs-and-emerging-approaches),
[](#microfluidic-separations)). The minimum industrial grade for a primary rare
earth ore is 1.5-2.0 wt% [@tan2016innovative] — one to two orders of magnitude
higher. Coal ash is not a high-grade resource by any reading.

What makes it interesting is the other three columns of the ledger: the
material has already been mined, crushed, and burned at someone else's expense;
it is already collected in known, permitted, characterized impoundments; it is
already a disposal liability; and the annual arisings are enormous. The
argument for coal ash is tonnage and pre-existing handling, not concentration,
and any process proposed for it has to survive a leach of a very dilute,
aluminosilicate-dominated feed ([](#hydrometallurgical-leaching)).

One separation has been shown on exactly that feed. Dong and co-workers pumped
29.1 bed volumes of a Powder River Basin fly ash leachate — 0.043 mol % rare
earths, about 150 µM total REE against millimolar Na, Mg, Al, Ca and Sr —
through a 0.94 mL immobilized-lanmodulin column and recovered more than 96.5 %
of the rare earths in 3.9 bed volumes of pH 1.5 acid at 88.2 mol % purity, a
2,040-fold enrichment, with uranium left behind [@dong2021bridging]
([](#biological-and-biomimetic-separations)). That is a direct answer to the
aluminium problem, which selective precipitation does not solve because rare
earth hydroxides co-precipitate with aluminium hydroxide. Two things temper it:
the column is one millilitre, and iron and silicon are the two impurities it
does not reject, because they arrive as colloids that lodge in the bed and
redissolve in the acid strip. The demonstration does not improve coal ash's
grade. What it shows is that a low grade need not disqualify a feed, provided
the separation is selective enough against everything else that is in it.

## What Actually Limits It

The recurring result across all of these streams is that the recovery
chemistry works — 90 % by hydrogen decrepitation, 75 % by selective roasting,
73 % by copper-salt leaching on shredded e-waste, 89-95 % from activated
phosphors, over 99 % from NiMH leachate — while the end-of-life recycling rate
stays under one percent. The gap is not in the beaker.

It is in collection, in the design of products that were never intended to be
disassembled, in the absence of any sorting infrastructure that can identify a
magnet grade before it enters a shredder, and in an economics that compares a
small, variable, contaminated batch against a commodity with a deep and
subsidized primary supply. Of these, only the last is likely to change quickly,
and it changes for reasons that have nothing to do with chemistry
([](#supply-chain-concerns)).
