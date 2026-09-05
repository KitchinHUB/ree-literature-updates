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

### Leaching the magnet out of the steel

Every route above assumes the magnet has been separated from everything it was
attached to. Shredded hard disk drives do not arrive that way: the magnet
fragments come bound to steel, and the table at the head of this chapter records
the consequence. @lister2021recovery take the opposite approach and use the rate
difference instead of fighting it.

In 1 M HCl the Nd--Fe--B magnet alloy dissolves at **0.170 mm/h**, and mild steel
coupons in the same solution corrode at a rate **three orders of magnitude
lower** — a thousandfold rate ratio between the phase you want gone and the phase
you want left behind. The magnet leaching rate is linear in HCl concentration,
so the ratio is a design variable rather than a fixed property. The dissolved
rare earths are then precipitated with solid Na₂SO₄ as the sodium double salt
NaRE(SO₄)₂·xH₂O and converted to the hydroxides in 2 M NaOH at 70 °C, with the
whole leach run under automated pH control below zero by metered addition of 5 M
acid.

Recoveries of rare earth hydroxide **exceeded 80 %** for everything except
lanthanum, which recovered poorly; an independent estimate from acid consumption
put the unrecovered fraction at about 17 %, which agrees. A second digestion in
10 M NaOH raised the hydroxide content of the product by 12 % and cut iron and
zinc by 50 % and 65 % respectively, giving an intermediate at **99.1 % purity on
a metal basis**. Reusing the hydrochloric acid rather than taking it fresh cost
about 10 % of the recovery.

This deserves emphasis for a reason that has nothing to do with recycling. The
book's recurring finding is that large kinetic selectivities are available
everywhere *except* between neighbouring lanthanides
([](#kinetics-and-mass-transfer)). A thousandfold rate ratio between magnet alloy
and steel is exactly that pattern: it is a real, exploited, process-scale kinetic
separation, and the two things it separates are as chemically unlike each other
as two metals in a shredder can be. Nothing in it transfers to the Nd/Pr problem
waiting downstream.

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

Coal *waste* — the refuse rock rejected at the preparation plant, as distinct
from the ash left after burning — is the same argument at larger tonnage and
lower grade. @sarswat2021rare put United States generation at 544 Mt/year at an
average rare earth content of about 200 ppm, and target feedstocks above 300 ppm
for a proposed process that biooxidizes the pyrite in the refuse to generate
ferric iron and acid in place, leaching the rare earths with a lixiviant the
waste makes for itself and removing the sulfide that would otherwise become acid
rock drainage. The circularity is genuinely attractive: the same step that
cleans the coal, generates the leachant and defuses a long-term environmental
liability.

The concentrations tell the rest of the story. Ferric sulfate leach solutions in
that work carried total rare earths in the 5--50 ppm range, and the reported
bioleach liquor came in at **about 4 ppm total rare earth**, from which
praseodymium was recovered preferentially by D2EHPA. Four milligrams per litre is
a solution from which recovery is possible and from which economics is a separate
question entirely — the same gap between demonstrated chemistry and demonstrated
process that runs through every unconventional feed in this chapter.

(bauxite-residue)=
## Bauxite Residue: Where the Scandium Is

Alumina refining by the Bayer process leaves 0.9 to 1.5 tonnes of insoluble
residue for every tonne of alumina produced, depending on ore grade and
extraction efficiency [@balomenos2021scandium]. That residue — bauxite residue,
red mud — carries rare earths at a worldwide typical concentration of 800 to
2,500 mg/kg, which is well above coal ash and comparable to phosphogypsum. It is
in the same category as those two: a stockpiled industrial waste whose grade is
respectable and whose problem is everything else in it.

**Scandium is the reason this feed gets attention, and the reason it behaves
unlike the others.** Sc³⁺ is much smaller than any lanthanide ion — closer in
size to Al³⁺, Fe³⁺, V³⁺ and Zr⁴⁺ than to Lu³⁺ — so it does not travel with the
rest of the series through geochemistry and does not concentrate in the minerals
that host them [@eriksen2021scandium]. Scandium is found instead in
titanium-, aluminium-, zirconium- and iron-bearing minerals, which is why looking
for it in xenotime and monazite is the wrong search. In bauxite residue
specifically it associates with goethite rather than with the
alumina-bearing phases that dissolve in the Bayer liquor, so it survives into the
residue while much of the rest of the rare earth content is redistributed into
desilication products. An estimated 70 % of world scandium resources may sit in
bauxite and bauxite residue [@balomenos2021scandium].

There is one more consequence of that ionic-size argument worth naming, because
it is the mirror image of this book's central difficulty. Scandium is hard to
separate from aluminium and iron and easy to separate from the lanthanides —
precisely because it is *not* chemically similar to them. The lanthanide problem
and the scandium problem are different problems, and a process built for one is
not a process for the other.

### What the numbers look like at one refinery

@balomenos2021scandium give a fully instrumented account for Greek bauxite
residue at the Mytilineos alumina refinery, and it is worth following because the
arithmetic is unusually complete. The residue analyses at 39.16 wt% Fe₂O₃,
16.53 % Al₂O₃, 9.90 % SiO₂, 8.40 % CaO, 4.67 % TiO₂ and 3.46 % Na₂O, with
Ce at 657 mg/kg, Y at 132, La at 110 and **Sc at 71 mg/kg**. At the refinery's
production rate that amounts to more than 100 tonnes of scandium discarded each
year in one waste stream.

Set the two ends of that composition against each other. Iron, at 39.16 % Fe₂O₃,
is 27.4 wt% of the residue as the element; scandium is 0.0071 wt%. **Iron
outnumbers scandium by roughly 3,900 to 1 by mass in the feed**, and every step
that follows is an argument with that ratio.

The leaching results show what the argument costs:

| Leach condition | Sc recovery | What comes with it |
|---|---|---|
| 3 M H₂SO₄, 85 °C | 70--95 % | Fe 49.7 g/L, Al 9.7 g/L in the liquor |
| 1 M H₂SO₄, 95 °C | 48--55 % (Sc \~8 mg/L) | Fe and Ti recovery <5 %, but Si >4 g/L |
| 45 g/L H₂SO₄ with filtrate recycle | --- | Sc 8.8, Fe 98, Ti 5.9, Si 213 mg/L |

The first row is the one to sit with. Dissolving nearly all of the scandium also
dissolves about fifty grams per litre of iron, and no amount of downstream
cleverness recovers from a feed like that. The second row buys a five-hundredfold
reduction in iron by giving up half the scandium — and then hits a different
wall, because silica dissolves instead and gels in the column.

### The result that is worth the whole paper

The consequences for the recovery step are stark, and they were measured rather
than assumed. Loading of scandium onto the composite extractant-enhanced
ion-exchange resin from the high-acid liquor was about **60 mg Sc per litre of
resin** — negligible. Removing the silicon and titanium (a 16-hour leach
retention time brought Si below 800 mg/L and Ti to 43 mg/L) produced **no
significant improvement**. Spiking the same solution with scandium to 60 mg/L
raised loading to **2,640 mg/L**. And the optimised low-acid liquor with filtrate
recycle — 8.8 mg/L Sc against 98 mg/L Fe — reached **5,000 mg/L resin**, with the
resin eluted, regenerated and giving equivalent results on a second cycle.

An eighty-fold range in loading capacity, on the same resin, from the same
residue, decided entirely by what else was in the solution. This is the argument
of [](#from-ore-to-feed-solution) arriving from the waste-valorisation direction:
the separation step is not where an unconventional feed is won or lost. It is
won or lost in the leach, and the design variable is not how much of the target
you dissolve but what ratio you dissolve it at.

Two things this case does not establish should be said. The 5,000 mg/L figure is
a column loading capacity, not a process recovery, and no overall scandium
recovery for the integrated flowsheet is given. And the residue contains 657
mg/kg of cerium — nine times as much cerium as scandium — for which this process
takes no credit at all. Whether a scandium circuit on bauxite residue would pay
for itself is a question the paper does not answer; pilot plants for both the
leach and the ion-exchange step were built and operated at the refinery, with the
leach unit processing up to 1,000 kg of pulp containing 300 kg of residue per
shift, so the question is at least being asked at the right scale.

The market context is the last piece, and @eriksen2021scandium puts it bluntly:
the scandium market does not function, in the sense that very little material is
offered at a very high price, which prevents the applications — scandia-stabilised
zirconia for solid oxide fuel cells, Sc--Al--Mg alloys for welded transport
structures — from developing the volume that would justify producing more. That
is a coordination failure rather than a separations problem, and it is the same
shape as the one [](#the-industrial-landscape) describes for the heavy rare
earths.


(phosphogypsum)=
## Phosphogypsum: The Largest Pile

Phosphoric acid manufacture dissolves phosphate rock in sulfuric acid and throws
away the calcium as gypsum. The rare earths that were in the phosphate rock
follow the calcium into that gypsum, which is produced in very large quantity
and stacked. It is the same argument as coal ash — tonnage, prior mining, and an
existing disposal liability — with the same grade problem and one additional
complication. The tonnage of phosphogypsum stacked worldwide is quoted widely
and inconsistently, and no global figure is given here because none could be
traced to a primary source. Nor could a gypsum-per-tonne-of-acid ratio, which is
the number that would let one be estimated. What can be sourced is site-specific
and gives the order of magnitude: about 100 million tonnes stacked over roughly
1,200 hectares of marshland at Huelva in Spain, less than 300 m from the city
[@canovas2019leaching], and about 11 million tonnes at the Sredneuralsky tailings
dump in Russia, holding an estimated 50,000 tonnes of contained rare earths
[@rychkov2018recovery]. Both are the authors' own statements about the stacks
they sampled.

The grade is low, awkward, and above all variable with the source rock — and the
variation is more than an order of magnitude, so any single figure is a figure
about one stack. A review of the recovery literature puts total rare earths in
phosphogypsum at over 2,000 mg/kg depending on the source phosphate rock, that
is, normally below 0.1 wt % [@mukaba2021rare]. The two process studies below
bracket that from both sides. Phosphogypsum from the Huelva stack in southwest
Spain, made from sedimentary carbonate-fluorapatite, assays 345 mg/kg total rare
earths plus yttrium — **0.035 wt %** — of which yttrium alone is 129 mg/kg, with
uranium at 45 mg/kg and thorium at 1.6 mg/kg [@canovas2019leaching].
Phosphogypsum from the Sredneuralsky tailings dump in Russia, made from Kola
Peninsula apatite-nepheline ore, assays **0.43-0.52 wt % REE₂O₃**, more than four
kilograms per tonne, which its authors note is far above phosphogypsum from other
sources [@rychkov2018recovery]. A twelve- to fifteen-fold difference in grade between
two stacks is the first thing to establish about any third one.

@mukaba2021rare identifies the real difficulty as the mineralogical one: the
rare earths are present in trace concentration and in complex, finely divided
phases, which makes recovery hard both technically and economically. The review
also surveys the pre-treatments used to upgrade the material before extraction — carbonation,
roasting, microwave heating, grinding, recrystallization — and concludes that
recrystallization looks the most promising, because it both recovers rare earths
and leaves a clean gypsum phase behind, which matters when the residue is
itself a saleable product.

The most instructive process study runs the leach and the sorbent together.
@virolainen2019recovering compared four lixiviants — H₂SO₄, HCl, H₃PO₄ and NaCl
— in a resin-in-leach configuration, where the ion-exchange resin sits in the
leach slurry and takes the rare earths as they dissolve. A chelating resin let
them work at 1 g/L H₂SO₄, a very low acid concentration, and in a four-stage
cross-current arrangement reached a loading of 19.2 g of rare earths per
kilogram of resin at up to 20 % purity, against 3 % for a strong-acid resin.

The calcium loading is what makes the comparison decisive, and it is the number
to remember from this study. The chelating resin took up 19.2 g of rare earths
and 14.7 g of calcium per kilogram; the strong cation exchanger took up 5.6 g of
rare earths and **67.0** g of calcium. Phosphogypsum is calcium sulfate, so a
sorbent that cannot reject calcium is a sorbent that spends its capacity on the
matrix — a third as much rare earth for four and a half times the calcium. Two
further conclusions are worth carrying forward: neither breaking up the gypsum
structure nor adsorbing the calcium turns out to be necessary to get good
recovery, and calcium and the rare earths can be separated during elution of the
chelating resin. Eluting a strong cation exchanger takes saturated NaCl;
eluting the chelating resin takes EDTA or concentrated HCl.

Two further leaching studies are widely cited in this literature, and they
disagree with each other in a way that is more useful than either alone.

@canovas2019leaching leached real Huelva phosphogypsum at room temperature, a
liquid-to-solid ratio of 1:20, for two to eight hours. **The choice of acid is a
choice about what else comes with the rare earths.** Three molar nitric acid took
out 82 % of the light and 86 % of the heavy rare earths in eight hours — but it
dissolved 63 % of the gypsum with them, and with it 84 % of the phosphorus, 76 %
of the strontium, 79 % of the cadmium and 60 % of the lead. Half-molar sulfuric
acid took only 46 % and 58 % of the rare earths, but dissolved under 6 % of the
gypsum, 5.6 % of the calcium, 0.79 % of the barium, 11 % of the lead. Common-ion
suppression of gypsum solubility is doing the work, and it buys a far cleaner
liquor for about two-thirds of the recovery. Cerium is the outlier in both, at
67 % and 38 %, which the authors attribute to oxidation to Ce(IV) and
reprecipitation as CeO₂. Scandium leaches at about 99 % either way; uranium
barely leaches at all, 21 % and 10 %. Two further results are directly useful: a
plain water wash removes about 80 % of the magnesium, manganese and arsenic and
30 % of the cadmium while leaving the rare earths entirely behind, so it is free
pre-purification; and a DTPA-chelated leach at pH 3 recovers far less of
everything, 22 % and 18 %.

@rychkov2018recovery worked on real aged phosphogypsum from Sredneuralsky and
found the opposite of an easy leach. Direct sulfuric acid leaching recovered only
13.8 to 18.1 % of the rare earths, and did not exceed 30 % even at high acid
concentration, because in that material the rare earths are co-crystallised into
the gypsum lattice itself. Getting them out took mechanical destruction of that
lattice: two hours of bead milling at 3000 rpm, which takes the particle size
from 500-600 µm down to 0.1-5 µm, plus ultrasound to stop the fines
re-aggregating, plus a strong-acid resin sitting in the pulp. The three together
raised recovery **from 15-18 % to over 70 %**, at a sulfuric acid concentration
of only 10-20 g/L. Of the three, the resin-in-pulp is the single largest lever
and the ultrasound on its own is worth almost nothing. The eluate carried 1455
mg/L of rare earths and **8770 mg/L of calcium** — six times as much calcium as
product — which is why the elution used ammonium nitrate rather than a sulfate,
and why the rare earths then had to be precipitated as carbonates to leave the
calcium behind in solution. That is the resin-selectivity problem above showing
up again, one unit operation downstream.

Cánovas points at the disagreement explicitly: 46-58 % from a straight sulfuric
leach at Huelva against roughly 10-18 % at Sredneuralsky under comparable
conditions. Both groups are right about their own material, and the reconciliation
is mineralogical. At Huelva the rare earths sit in unreacted phosphate and
fluoride phases *outside* the gypsum, which is why they come out while the gypsum
stays; at Sredneuralsky, made by the dihydrate route, they are inside the
crystal. @virolainen2019recovering's finding above, that breaking up the gypsum
structure is unnecessary, should therefore be read as a statement about a
feedstock rather than about phosphogypsum in general: for Rychkov's material,
breaking up the structure *is* the process.

Both studies are bench scale, and both say so. Cánovas: the results "only address
bench scale leaching tests." Rychkov's largest experiment is 40 g of
phosphogypsum in 300 mL, and the only kilogram-scale item in that paper is 17 kg
of a granulated cement additive made from the leach residue, not of rare earth
concentrate.

The additional complication is radioactivity, and it is the same complication
monazite has. Phosphate rock carries uranium and thorium and their decay
products, which is why the monazite route in
[](#hydrometallurgical-leaching) is a radioactive-materials flowsheet, and the
same nuclides partition into the byproducts of phosphate processing. That makes
the disposition of phosphogypsum a regulated question in several jurisdictions
rather than purely a chemical one.

The process literature reviewed here still does not treat it quantitatively.
Neither leaching study reports an activity in becquerels, a radium figure, or a
gross-activity measurement; the only hard numbers are Cánovas's chemical assays of
45 mg/kg uranium and 1.6 mg/kg thorium at Huelva, and the observation that
uranium is one of the elements that stays put — 21 % leached by nitric acid,
10 % by sulfuric — so that an acid leach for rare earths does not, at least at
Huelva, drag the uranium out with them. Rychkov goes further and asserts the
opposite case — that his material has no natural radionuclides, so that
deactivation and radioactive-waste disposal are unnecessary — but reports no
measurement of any kind in support, and lists neither uranium nor thorium in his
composition table. The assertion is at least plausible for an igneous
apatite-derived material, since sedimentary phosphorites are the uranium-rich
ones, and it is a reminder that the radiological question is a question about
the source rock rather than about phosphogypsum as a class. It is also
unsupported. A reader assessing a phosphogypsum recovery proposal should
establish the radiological status of the specific stack before anything else, and
should not accept either a blanket warning or a blanket exemption.

(brines-and-produced-water)=
## Brines, Geothermal Fluids and Produced Water

The last non-ore feedstock is water. Geothermal brines, oilfield produced water
and shale gas flowback all carry rare earths at microgram-per-litre levels,
which is three to four orders of magnitude below a leach liquor and far below
anything a solvent extraction cascade would look at. What makes them worth a
paragraph is that the fluid is already being pumped and already being handled
for disposal, so the only marginal cost is the recovery step itself.

This section treats the rare earths in those waters as one more unconventional
feedstock alongside coal ash and phosphogypsum. The broader question of what
*else* is dissolved in them — and why the answer for Pennsylvania is lithium
rather than lanthanides — has its own chapter,
[](#produced-water-critical-minerals).

The concentrations are genuinely small. @tian2020rare measured Sichuan Basin
shale gas flowback and produced water and found total rare earths from 4.5 to
118.3 µg/L, with europium present in every sample at 0.92 to 79.62 µg/L. Their
estimate is that the world's produced water contained on the order of 4.2 tonnes
of Eu₂O₃ in 2016, rising to somewhere between 16.8 and 111.7 tonnes by 2030.
That is a real quantity of a genuinely scarce element in a stream nobody
currently mines, and it is also, as a global annual figure, small.

At those concentrations the recovery step has to be a sorbent, and the binding
has to survive the water chemistry. @brewer2019recovery is the useful study
because it maps exactly that. Using *E. coli* engineered to display lanthanide
binding tags on its surface ([](#biological-and-biomimetic-separations)), they
find that biosorption is robust to total dissolved solids up to 165,000 ppm —
which is the property that matters most in a brine — with an optimum between
pH 5 and 6, a roughly 65 % loss of capacity at pH 2, and increasing recovery and
selectivity with temperature up to about 70 °C, which suits a geothermal fluid.
Uranium, aluminium and lead are the competitive ions, reducing biosorption by
more than 25 % when present at three to eleven times the rare earth
concentration.

Read that as a boundary-condition study rather than a process. It says what a
sorbent has to tolerate to work on a brine, and it says that at least one
sorbent tolerates it. Nobody has published a costed recovery of rare earths from
a geothermal or oilfield stream at any scale, and the arithmetic in
[](#environment-techno-economics-and-life-cycle) is the place to see why a
microgram-per-litre feed is a hard case even when the pumping is free.

The national accounting is worse than that arithmetic suggests, and
[](#produced-water-critical-minerals) sets it out: on the best available
figures the rare earths in all US oil and gas produced water amount to about a
tonne a year against a national consumption of 9,300 t, and the Marcellus
number behind that estimate rests on two samples. The same water is a lithium
resource of national scale. If a rare earth recovery process is ever built on
produced water, it will be built as an attachment to something else.

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
