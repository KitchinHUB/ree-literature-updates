---
title: Uranium and Plutonium Separations
---

(uranium-and-plutonium)=
# Uranium and Plutonium Separations

This is a book about rare earth separations, and this chapter is about two
elements that are not rare earths. It is here for three reasons, and each of
them is a reason a reader who cares about lanthanides should care about
actinides.

The first is that the separations are already entangled. Every monazite and
xenotime flowsheet in [](#from-ore-to-feed-solution) and
[](#hydrometallurgical-leaching) is also a uranium and thorium flowsheet,
whether or not it is described that way. Monazite carries thorium and uranium in
the same phosphate lattice as the rare earths — tabulated at 0–20 wt % ThO₂ and
0–16 wt % UO₂ depending on the deposit — and the caustic crack that liberates
the rare earths liberates them too, sending all three into one hydroxide cake,
so everything downstream of it has to decide where they go
[@garcia2020separation; @amaral2010thorium]. A rare earth plant that ignores its
actinides is not a plant, it is a licensing problem.

The second is that the hardest separation in the nuclear fuel cycle is the same
separation this book opens with. Trivalent americium and curium sit among the
trivalent fission-product lanthanides at nearly the same ionic radius, with the
same coordination chemistry, and they have to be told apart to close the fuel
cycle. That is the [](#why-rare-earths-are-hard-to-separate) problem with a
different pair of elements — except that the actinide version has a chemical
handle the lanthanide version does not, because 5f orbitals participate in
bonding in a way 4f orbitals do not [@jensen2002comparison]. Watching what that
handle buys is the most useful thing in this chapter for a rare earth chemist,
because it quantifies what you are missing.

The third is seawater. Uranium from seawater is the most thoroughly documented
attempt anyone has made to recover a metal from a feed that is far too dilute to
justify it — three parts per billion, sorbent farms measured in square
kilometres, two decades of field measurements. Everything this book says about dilute feeds in
[](#ion-adsorption-clays) and
[](#produced-water-critical-minerals) has a limiting case, and this is it. The
uranium-from-seawater literature is where you go to find out what happens when
the chemistry works and the arithmetic does not.

## The Elements and Their Chemistry

{index}`Uranium` in aqueous solution is dominated by U(VI), and U(VI) is
dominated by the {index}`uranyl` ion, UO₂²⁺: a linear trans-dioxo cation with
two short, strong, chemically inert axial bonds and four to six coordination
sites in the equatorial plane perpendicular to them. That geometry is the single
most important fact about uranium separations. Uranyl does not behave like a
spherical hard cation the way Nd³⁺ does; it presents a flat equatorial pocket,
and ligands that fit that pocket — carbonate, phosphate, amidoximes, the
tri-*n*-butyl phosphate of [](#solvent-extraction-fundamentals) — bind it far
more strongly than the same donor set binds a trivalent lanthanide. Separation
chemistry that exploits shape rather than size is available for uranium in a way
it simply is not for the lanthanides, and much of what follows is a consequence
of that.

U(IV), by contrast, is a hard tetravalent cation with no oxo groups, and it
behaves much more like Th(IV) or Ce(IV) — sparingly soluble, easily
precipitated, extracted by acidic organophosphorus reagents. The U(VI)/U(IV)
couple is accessible under mild conditions, so redox is a routine tool: reduce
to strip, oxidize to load.

{index}`Plutonium` takes this much further. Plutonium is the element for which
four oxidation states — III, IV, V and VI — can coexist in the same solution at
comparable concentrations, with disproportionation equilibria connecting them.
This is a nuisance for anyone doing analytical chemistry on plutonium and a gift
for anyone separating it: because Pu(III) is poorly extracted by the reagents
that extract Pu(IV) strongly, the entire industrial separation of plutonium from
uranium is a redox operation, not a ligand-design operation. You do not need a
selective extractant. You need a selective electron.

Trivalent americium and curium, the elements the back end of the fuel cycle
actually struggles with, have no such handle. They are trivalent and they stay
trivalent, and their radii place them squarely inside the lanthanide series.
What distinguishes them is that the 5f orbitals are more radially extended than
4f, so a soft nitrogen or sulfur donor can form a bond with more covalent
character to An(III) than to Ln(III). The underlying orbital picture has been
probed directly. Actinide M₄,₅ high-resolution XANES and 3d4f RIXS show that
the 5f orbitals are chemically active in bonding for uranium and neptunium, but
are already localized and largely insensitive to the ligand environment by
plutonium [@vitova2017role]. The covalency the separations community relies on
is a property of the early actinides that fades across the series, which is part
of why Am/Cm is harder than U/Pu.

## Uranium from Ore

Conventional uranium production is a leach followed by a concentration step, and
both halves will look familiar after [](#hydrometallurgical-leaching).

The leach is sulfuric acid for most ores and alkaline carbonate for ores with
carbonate gangue that would consume acid. The chemistry of the alkaline route is
worth pausing on because it recurs later: uranyl forms exceptionally stable
carbonate complexes, culminating in UO₂(CO₃)₃⁴⁻, and that complex is soluble,
selective — few other ore constituents form comparably stable carbonates — and
easily broken by acidification. The alkaline leach is one of the rare cases in
this book where a single complexation equilibrium does the separation for you.

{index}`In-situ leaching` (ISL, also called in-situ recovery) takes this further
by not mining the ore at all. A lixiviant — a carbonate or bicarbonate solution
carrying oxygen as the oxidant, or sulfuric acid with oxygen or hydrogen
peroxide — is injected into a permeable sandstone-hosted deposit through wells,
flows through the ore, and is pumped back up through recovery wells. Its share
of world uranium production rose from 51 % in 2014 to about 63 % in 2021, and
its economics differ fundamentally from conventional mining: capital costs run
up to several times below those of an open pit or an underground mine, and no
tailings or waste rock are generated [@li2024review; @seredkin2016situ]. There
is no rare earth analogue at this depth or scale — scandium, yttrium and the
rare earths have come out of uranium in-situ liquors only in pilot tests — but
the ion-adsorption clay in-situ leaching of [](#ion-adsorption-clays) is the
same idea applied to a shallower host, with the same virtues and the same
groundwater liabilities.

Recovery from the pregnant leach solution is ion exchange or amine solvent
extraction. The amine route — the AMEX process — works because the anionic
uranyl sulfate complexes UO₂(SO₄)₂²⁻ and UO₂(SO₄)₃⁴⁻ pair with a protonated
tertiary amine, and it is the same anion-exchange mechanism that
[](#from-ore-to-feed-solution) describes for chloride and nitrate media
[@zahakifar2025solvent]. The uranium case is easier only because the complex is
stronger and the competition is weaker.

### Where This Meets the Rare Earths

The direct connection is monazite. A rare earth concentrate from monazite
carries thorium and uranium into every downstream unit operation, and the
literature on removing them is a rare earth literature, not a nuclear one: leach
chemistry, selective precipitation, solvent extraction and ion chromatography,
applied to separating Th and U from the light lanthanides they came in with
[@garcia2020separation]. [](#hydrometallurgical-leaching) treats thorium
management at length; the point to carry here is that the same amine and
organophosphorus extractants appear on both sides of the divide, and the
selectivity that makes an extractant good at pulling Th(IV) or U(VI) out of a
rare earth stream is the selectivity that makes it good at recovering uranium
from ore.

The second connection is phosphate. Wet-process phosphoric acid made from
sedimentary phosphate rock carries uranium at 60 to 170 mg per litre, and
recovering it has been done repeatedly at industrial scale: sixteen plants ran
between 1952 and 1999, ten of them on the synergistic D2EHPA/TOPO extractant
pair and the rest on precipitation, DPPA, OPPA or OPAP, and the last closed as
uranium demand and price fell away after Three Mile Island and Chernobyl
[@beltrami2014recovery]. The same phosphoric acid stream is the one that
produces the phosphogypsum discussed in [](#recycling-and-urban-mining) as a
rare earth resource, and the same uranium follows the same acid. An analysis of
the potential US supply puts 5.5 million pounds of U₃O₈ a year within reach of
existing US phosphoric acid production — more than the country mined in 2014 —
and puts ion exchange ahead of solvent extraction on total cost, US\$33–54
against US\$44–61 per pound U₃O₈ depending on discount rate and plant life,
except that ion exchange has never run at commercial scale and both figures sit
above the uranium price of the years around the study [@kim2016potential]. It is
a byproduct recovery problem of exactly the kind that recurs throughout this
book: the metal is already in solution, already paid for by another product, and
the only question is whether the incremental separation cost clears the price.

(uranium-from-seawater)=
## Uranium from Seawater

### The Resource and the Arithmetic

The oceans contain on the order of 4.5 billion tonnes of dissolved uranium
against something like 17 million tonnes in conventional terrestrial resources
— some 260 times more uranium in the sea than on land [@abney2017materials;
@guidez2016extraction]. The ratio usually quoted is a thousandfold, and both of
those sources quote it, but neither reconciles it with the
seventeen-million-tonne denominator printed beside it; the larger ratio is taken
against a narrower reserve base than the conventional-resource figure used here.
Two hundred and sixty is what the two quantities above actually imply, and it is
ample for the argument. That is the entire case for extracting it, and it is a
genuinely good case as far as it goes.

The concentration is about 3.3 parts per billion, roughly 3 µg/L
[@ladshaw2016experiments; @guidez2016extraction]. Everything difficult follows
from that number, and the difficulty is best appreciated by doing the
arithmetic rather than by describing it. World uranium consumption is around
65,000 tonnes a year. At 3 µg/L, supplying that from seawater means stripping
every gram of uranium out of about 2 × 10¹³ tonnes of seawater annually — the
volume of the North Sea — and that figure is a floor, because it assumes
complete recovery. The cost models built on that arithmetic take a sorbent that
picks up roughly 2 g of uranium per kilogram over a sixty-day deployment and
survives about six such deployments; on those numbers a plant producing 1,200
tonnes of uranium a year — under two percent of world demand — needs its sorbent
spread across more than a thousand square kilometres of ocean
[@guidez2016extraction].

There is a counter-argument, and it is worth stating fairly because it is the
strongest form of the optimistic case. The uranium is not stationary. The Kuro
Shio current carries something like 5.2 million tonnes of uranium past Japan
each year, against a Japanese consumption of around 8,000 tonnes before
Fukushima [@guidez2016extraction]. You do not have to process the ocean; you
have to stand in a river of it and let it come to you. Whether that is an
answer or a restatement of the problem depends entirely on how much sorbent
it takes to intercept a useful fraction, which is exactly the question the
deployment literature below is trying to answer.

### The Speciation Problem

Uranium in seawater is not free uranyl. At pH 8.1 and about 2 mM total
carbonate it is predominantly the neutral calcium uranyl tricarbonate complex
Ca₂UO₂(CO₃)₃ — roughly 58 % of the dissolved uranium, with CaUO₂(CO₃)₃²⁻ and
MgUO₂(CO₃)₃²⁻ near 18 % each and the free UO₂(CO₃)₃⁴⁻ anion at only about 6 %.
Molecular dynamics of the solvation shell shows that one sodium ion sits close
enough to that neutral complex — 5.25 Å from the uranium, bridged by a water
molecule — that the whole assembly behaves as a Na[Ca₂UO₂(CO₃)₃]⁺ cation of
effective charge +1 [@wu2016solvation]. Alkaline-earth triscarbonatoactinyl(VI)
complexes of this kind are the predominant form of U(VI) in natural
carbonate-bearing waters, though how the total divides between the neutral
Ca₂UO₂(CO₃)₃ and the singly complexed AeUO₂(CO₃)₃²⁻ anions in seawater turns
out to depend sensitively on which ion-interaction coefficients the calculation
uses, and is not settled [@reiller2024predominance].

This is the central difficulty, and it is not a mass-transfer difficulty. A
sorbent that binds uranium from seawater has to strip uranyl out of a very
stable, essentially neutral, sterically crowded tricarbonate complex — competing
not against water but against three carbonates and two calciums. It has to do
this while surrounded by sodium at 0.5 M, magnesium at 53 mM, and calcium at 10
mM, which is to say by competitors present at seven to eight orders of magnitude
higher concentration than the target. Bicarbonate makes it worse by competing
with the amidoxime ligand for the uranium itself, and calcium and magnesium
occupy so many of the sites that the time for uranium uptake to reach
equilibrium in a simulated-seawater batch roughly doubles, from about five days
to about ten [@ladshaw2016experiments].

### Amidoximes, and the Correction

The workhorse material is polyethylene fibre with amidoxime groups grafted onto
it by radiation-induced graft polymerization: irradiate the fibre, graft
acrylonitrile (usually with a hydrophilic comonomer such as itaconic acid or
methacrylic acid), then convert the nitriles to amidoximes with hydroxylamine
and condition the product with alkali [@das2016alternative]. The result is
cheap, mechanically robust in seawater, and grafted at high enough density to be
useful. The US program's reference material, AF1, is made this way, and a
systematic comparison of graft chemistries found that sodium hydroxide
conditioning outperforms potassium hydroxide and that process changes of this
kind cut the projected cost of recovered uranium by 21–30 %
[@das2016alternative].

The correction is that "amidoxime sorbent" is a misnomer for the part that does
the work. Under the alkaline conditioning step, adjacent amidoxime groups
cyclize to glutarimidedioxime — a cyclic imide-dioxime — and it is the cyclic
form, not the open-chain amidoxime, that forms the strongest metal complexes.
Solid-state ¹³C NMR of blow-spun poly(imide dioxime) fibre confirms that the
binding motif in the working material is the imide-dioxime
[@wang2018significantly], and poly(imide dioxime) is now made and studied as a
sorbent family in its own right rather than as a byproduct of conditioning
[@das2016novel]. This matters beyond nomenclature,
because the two forms have completely different selectivity, as the next section
shows.

### The Vanadium Problem

The dominant competitor for amidoxime sorbents in real seawater is not calcium
or magnesium. It is {index}`vanadium`, present at around 2 µg/L — comparable to
uranium — and bound so tightly that it is difficult to elute and difficult to
displace. Potentiometric and calorimetric titrations, ab initio simulations and
X-ray absorption fine structure on sorbents recovered from seawater together
settled the mechanism: the open-chain amidoxime group does not bind vanadium at
all under these conditions. Vanadium is bound solely by the cyclic
imide-dioxime groups, which form a rare non-oxido V⁵⁺ complex, [V(IDO)₂]⁻,
whose log β of 53.5 is the highest stability constant reported for any V(V)
species [@ivanov2017origin]. The very cyclization that makes the sorbent good
at uranium is what makes it worse at rejecting vanadium.

That result reframed the design problem, and two lines of response followed.
One is to abandon the amidoxime family for a preorganized ligand whose donor
set is arranged to complement uranyl's equatorial plane and not vanadium's
coordination preference: the rigid tetradentate ligand
1,10-phenanthroline-2,9-dicarboxylic acid gives log K₁ = 16.5 for UO₂²⁺ against
7.4 for V(IV) as VO²⁺ and 7.3 for V(V) as VO₂⁺, both at 25 °C and zero ionic
strength — a selectivity gap of nine orders of magnitude in stability constant
[@lashley2016highly]. The other is to build selectivity into a scaffold rather
than a single ligand: a bio-inspired 2-aminobenzamidoxime nano-trap reaches 530
mg/g at high concentration and 4.36 mg/g in real seawater, roughly triple the
then-current benchmark [@sun2018bio], and a DNA-based uranyl-binding hydrogel
achieves 6.06 mg/g in natural seawater with a measured selectivity for uranium
over vanadium of roughly nineteenfold — the paper's abstract and figure say
18.95 and its own text says 17.95 [@yuan2020dna]. A third line borrows from
biology's own solution to binding a metal at vanishing concentration:
siderophore-inspired chelators such as H₂BHT are designed around the
hydroxamate and catecholate motifs that microorganisms use to scavenge iron
from seawater [@ivanov2019siderophore]. Reviews of the broader nanomaterial and
functional-material effort tabulate well over a hundred such systems between
them [@wu2023functional; @zhang2023uranium].

Morphology is the other lever, and it is easy to undervalue. The binding site
does no good if seawater cannot reach it, so a large fraction of the improvement
between generations of sorbent comes from the fibre architecture rather than
from the ligand: three-dimensional hierarchical porous amidoxime fibres expose
far more of the grafted material to the flowing phase than a solid braid does
[@xu2019hierarchical]. This is the same argument [](#membranes-mofs-and-emerging-approaches)
makes about surface area and accessibility in sorbent design generally, and in a
feed at three parts per billion it is as consequential as the binding constant.

### What Deployment Actually Measures

The most valuable body of work in this area is not the synthetic chemistry. It
is the marine testing program that established what the materials do in the sea,
and its results are consistently more sobering and more useful than laboratory
capacities.

For AF1 in flowing natural seawater, the 56-day capacity is 3.9 ± 0.2 g of
uranium per kilogram of sorbent, extrapolating to a saturation capacity of
5.4 ± 0.2 g/kg with a half-saturation time of 23 ± 2 days and a distribution
coefficient of log *K*~D~ = 6.08 at 56 days [@gill2016uranium]. That
half-saturation time is the number that constrains a plant: you cannot cycle the
sorbent quickly, so the annual production of a given mass of sorbent is set by
how many multi-week deployments it survives.

The mass balance on the loaded sorbent is worth quoting exactly, because it is
the sting in the whole enterprise. Of the cations adsorbed from seawater,
calcium and magnesium together are **61 % by mass and 74 % by mole**. Uranium is
fourth by mass and seventh by mole [@gill2016uranium]. The sorbent is,
overwhelmingly, a device for collecting alkaline earths, and uranium is a minor
impurity in its product. PHREEQC modelling of the site competition reproduces
this and adds a useful rule: when binding sites are scarce, vanadium dominates;
when they are abundant, magnesium and calcium do [@gill2016uranium].

Three further deployment findings deserve to be recorded because they are the
kind of thing that never appears in a synthesis paper:

- **Biofouling costs up to 30 % of capacity at 42 days** when the sorbent is
  exposed to light, and the recommended mitigation is to deploy below the
  photic zone — at the cost of deeper operations in colder water, where the
  adsorption itself is slower [@park2016effect; @gill2016uranium]. No
  toxicity was seen in Microtox assays of column effluent from any adsorbent
  tested, and toxicity could be induced with some non-amidoxime materials only
  at adsorbent-to-seawater ratios far above anything a deployment would
  produce.
- **Flow matters, but only in the right geometry.** Current velocity has
  essentially no effect on uptake in packed columns over 0.29–10.2 cm/s and a
  near-linear effect in flume experiments, which the authors attribute both to
  the flow resistance of the braid and to the braid fluttering more vigorously
  as the current rises [@ladshaw2017influence]. A column run at 10.2 cm/s gives
  the same mass-transfer coefficient as a flume current of only 2.61 cm/s. This
  is a mass-transfer result of exactly the kind [](#kinetics-and-mass-transfer)
  describes, and it means column data systematically mispredict field
  performance.
- **A farm perturbs the ocean, but less than a kelp forest does.**
  Hydrodynamic modelling of a 670-square-kilometre farm at 1,780 moorings per
  square kilometre gives a 4–10 % reduction in ambient currents, against up to
  50 % through a natural kelp forest, and a much smaller simulated farm drew
  the local uranium concentration down by at most 0.3 % [@gill2016uranium].
  Neither simulation has been run at the density or the area a production farm
  would need, so self-competition remains an open question rather than a
  bounded one.

Different laboratories measuring the same material do not agree closely: WHOI
column and flume measurements ran 15 % and 55 % higher, respectively, than the
PNNL column values [@gill2016uranium]. Any capacity figure in this literature
should be read with that spread in mind. Integrated first-principles models
that couple aqueous speciation to site competition now exist: DFT-derived
binding constants for uranium and vanadium, fed into an equilibrium adsorption
model, reproduce batch uptake in simulated seawater over the pH range 7.5–9,
which brackets the pH of the ocean [@ladshaw2018first]. They have not yet been
tested against field data, which is what comparing materials measured in
different rigs would require.

### Elution and Reuse

Recovering the uranium from the loaded sorbent is a separation problem in its
own right, and it constrains material design more than it is usually credited
with. Alkali conditioning before deployment is necessary — infrared
spectroscopy shows it strips the proton from the grafted carboxylic acid, though
it also converts some of the amidoxime to carboxylate — and either sodium
carbonate with hydrogen peroxide (1 M each) or 0.5 M hydrochloric acid removes
about 95 % of the uranium loaded over a 42-day seawater exposure. The
carbonate–peroxide route is the more selective, taking only about a quarter of
the iron and a third of the vanadium with the uranium and leaving nickel,
copper, manganese and cobalt behind entirely; the acid route strips the other
transition metals too. Tiron at around pH 7 then removes 94 % of the iron
without altering the sorbent's infrared spectrum, but nothing tested removed
the vanadium, which comes off only in acid above 3 M at 60 °C, and that
treatment destroys the sorbent [@pan2016elution]. Poly(imide dioxime) nanofibre
has been eluted at 98.5 % efficiency by carbonate–peroxide on the first cycle,
but over eight adsorption–desorption cycles in seawater spiked to 8 ppm uranium
that efficiency falls to 83.5 % and the capacity declines about 5 % per cycle
[@wang2018significantly].

### The Honest Capacity Trajectory

It is worth setting the numbers out in order, because the trend is real and the
extrapolation is not:

| Milestone | Capacity in natural seawater | Basis | Source |
|---|---|---|---|
| State of the art, 2013 | 3.2 g U/kg | 180-day exposure | @kim2013recovery |
| AF1, 2016 | 3.9 ± 0.2 g U/kg | 56 d, flow-through column | @gill2016uranium |
| AF8 poly(imide dioxime), 2016 | 4.48 g U/kg | 56 d, flow-through column | @das2016novel |
| Bio-inspired POP nano-trap, 2018 | 4.36 g U/kg | 56 d, shaken tank | @sun2018bio |
| Blow-spun PIDO nanofibre, 2018 | 8.7 g U/kg | 56 d, flow-through | @wang2018significantly |

The basis column is there because without it the rows are not comparable and the
trend is easy to overstate. The 2013 figure is an equilibrium loading reached
over 180 days, not 56; the nano-trap was five milligrams of sorbent shaken in a
tank of seawater rather than a column with the ocean running through it. On the
three rows that were measured the same way — 56-day flow-through in natural
seawater — capacity went from 3.9 to 8.7 g U/kg between 2016 and 2018, a factor
of 2.2 in two years. The best of them is a material whose capacity in natural
seawater spiked to 8 ppm is 951 g/kg, a hundredfold higher than what it achieves
in the sea [@wang2018significantly]. That ratio is the honest summary of the
field: the chemistry is not the limitation, the feed is. Every material in the
table is better than its predecessor and none of them changes the arithmetic in
the resource section by an order of magnitude.

Cost estimates exist, and reviewing them is its own exercise
[@lindner2015review]. That review's headline is that the most recent estimates
it covers put uranium from seawater at \$400–\$1,000/kg U against a 2014 spot
price at or below \$100/kg, and its closing verdict is that none of the reviewed
systems is economically competitive with terrestrial mining. Across the full
five decades it tabulates, normalized to 2010 dollars, the estimates run from
\$210/kg U to \$3,400/kg U. That factor of sixteen is the number worth
remembering, and it is not measurement scatter: it is the propagated effect of
assumptions about capacity, sorbent lifetime and reuse count, which is why the
durability paragraph above matters more to a cost than any chemistry in this
chapter does. This book quotes the range and endorses no point inside it.

The physical arithmetic underneath is firmer, but read it in the right
direction. The cost models are built on a sorbent capacity of 2 g of uranium
per kilogram over sixty days of immersion, six reuses with a 5 % efficiency
loss per chemical rinse, and, on those inputs, over a thousand square
kilometres of sea for a plant making 1,200 tonnes a year — under two percent of
world demand [@guidez2016extraction]. The 2 g/kg is a laboratory point value.
The same paper reports that JAEA's actual marine campaigns averaged **less than
1 g of uranium per kilogram per month**, and says so in as many words: the field
performance is "much lower" than the ideal laboratory figures. A reader who
wants a cost can multiply these by their own assumptions, and will learn more
from doing so — particularly from halving the capacity — than from quoting
someone else's answer.

Electrochemical approaches — driving uranium uptake with an applied potential
rather than relying on passive equilibrium — are a rapidly expanding recent
alternative to passive sorbents, and what they are claimed to buy is speed and
efficiency of uptake, not any change in the concentration of the feed
[@raj2024electrochemical]. They belong to the same family as the
methods in [](#electrochemical-separations).

## Reprocessing: Uranium and Plutonium from Spent Fuel

### PUREX

Dissolve spent oxide fuel in nitric acid and you have uranium at a few hundred
grams per litre, plutonium at a few grams per litre, minor actinides and fission
products including a substantial lanthanide load, all in 3 M HNO₃. The PUREX
process extracts U(VI) and Pu(IV) together into 30 % tri-*n*-butyl phosphate in
an aliphatic diluent as the neutral nitrato complexes UO₂(NO₃)₂·2TBP and
Pu(NO₃)₄·2TBP, leaving the trivalent actinides and the fission products in the
aqueous raffinate [@moyer2011overview].

The mechanism is solvation extraction, and it is the same mechanism
[](#solvent-extraction-fundamentals) describes for neutral organophosphorus
extractants acting on rare earths. What makes it work industrially is not
subtlety of selectivity but magnitude: the distribution ratios for U(VI) and
Pu(IV) at high nitrate are enormous, while those for trivalent species are
small. This is the opposite regime from the one this book usually operates in.
The rare earth chemist fights for β = 1.5 between adjacent elements; the PUREX
designer has β in the thousands between oxidation states and spends the
engineering effort on throughput, radiolysis and criticality instead.

### The Redox Split

Once uranium and plutonium are in the organic phase together, separating them is
a redox operation. Reduce Pu(IV) to Pu(III), which TBP extracts poorly, and it
back-extracts into an aqueous stream while U(VI) stays put. The classical
reductants — U(IV) with hydrazine as a nitrous-acid scavenger, or ferrous
sulfamate — work but add salt to the waste stream, which is the recurring sin of
reductive stripping.

The modern answer is salt-free complexant-reductants, and the chemistry is
directly relevant to the rest of this chapter. Simple hydroxamic acids —
formohydroxamic acid (FHA) and acetohydroxamic acid (AHA) — complex Pu(IV)
strongly and hold it in the aqueous phase, separating uranium from both
neptunium and plutonium without the salt loading that sulfate or ferrous
sulfamate stripping imposes on the waste [@birkett2005recent]. The mechanism is
not a simple complexation: the Pu(IV)–hydroxamate complex undergoes slow
reduction to Pu(III), and careful work establishes that the reductant is the
hydroxamic acid itself rather than any added hydroxylamine, with acid hydrolysis
of the hydroxamate competing on a similar timescale [@carrott2008oxidation]. The
design of an AHA-based flowsheet is therefore a kinetics problem, which is
[](#kinetics-and-mass-transfer)'s subject.

There is a connection here that looks appealing, and this book will not make it.
Glutarimidedioxime — the cyclic imide-dioxime that does the binding in seawater
sorbents — was reported in 2016 to work also as a salt-free
complexant-reductant for plutonium, stripping it from TBP/kerosene into nitric
acid fast enough for centrifugal contactors. That paper was retracted by the
journal in 2021 [@xian2016glutarimidedioxime; @xian2021retraction], and no
replacement result has appeared. The underlying idea — that ligand design
transfers across concentration regimes more readily than process design does —
may well be right, and the amidoxime chemistry of [](#uranium-from-seawater) is
suggestive. It is not established by this example, and the book carries no
number from it.

### The Awkward Fission Products

Technetium and zirconium are the two fission products that follow uranium and
plutonium into TBP rather than staying in the raffinate, and both are extracted
strongly enough to require dedicated handling. Technetium co-extracts with
zirconium and with the actinides, sometimes synergistically, and industrial
plants deal with it using high-acidity scrubs designed specifically to reject it
— a practice in use at La Hague [@george2022review]. This is a good corrective
to the idea that a large separation factor solves a separation: PUREX has
enormous selectivity for the actinides over almost everything, and the two
exceptions still require their own unit operations.

### Contactors

Reprocessing is where annular centrifugal contactors became standard equipment,
for reasons that have nothing to do with selectivity. Short residence time
limits solvent radiolysis, small holdup limits criticality risk, and rapid phase
disengagement gives stage efficiencies near unity in seconds rather than
minutes. The process-intensification case and its principal failure mode — the
accumulation of solids in the rotor, which is what actually ends a run — are
reviewed in @baker2022process. [](#the-landscape-of-separation-technologies) and
[](#process-modeling-and-optimization) treat contactor selection for rare earth
duty; the nuclear experience is where most of the operating knowledge came from.

(actinide-lanthanide-separation)=
## The Actinide–Lanthanide Problem

This is the section that most repays a rare earth reader, because it is the
same problem as this book's, attacked with more money and more urgency, and the
outcome tells you what is achievable when a chemical difference exists and what
is not.

The problem: after PUREX has taken out the uranium and plutonium, the raffinate
contains americium and curium — which dominate the long-term heat load and
radiotoxicity of the waste and are therefore the elements you most want to
transmute — mixed with fission-product lanthanides in large and unfavourable
mass excess [@zsabka2023beyond]. The lanthanides have large neutron capture
cross-sections that would hinder transmutation of the minor actinides, and it
is that mass ratio together with the chemical similarity that makes the
separation demanding [@modolo2012review]. So Am and Cm must be separated from
Nd, Sm, Eu and the rest, at trivalent charge, at nearly identical ionic radius.

That is the [](#why-rare-earths-are-hard-to-separate) problem exactly. The
difference is 5f covalency: soft nitrogen and sulfur donors bind An(III)
measurably more strongly than Ln(III) because of the greater radial extension of
the 5f orbitals [@jensen2002comparison]. The families of ligands built to
exploit this — polyaminocarboxylates, diglycolamides, and above all the
polyazine N-donors — are catalogued in @leoncini2017ligands.

The industrial development went in two stages, and the two-stage structure is
itself the lesson [@modolo2012review]:

1. **DIAMEX**: co-extract all the trivalent f-elements together — actinides and
   lanthanides alike — out of the PUREX raffinate with a malonamide or
   diglycolamide, discarding everything else. This step is easy, because
   trivalent f-elements are chemically distinct from the rest of the raffinate.
2. **SANEX**: split the actinides from the lanthanides in the combined
   trivalent stream using a soft N-donor. This step is the hard one, and it took
   the European programs — NEWPART, PARTNEW, EUROPART, ACSEPT — the better part
   of two decades to demonstrate in centrifugal contactors.

Two refinements are worth knowing about because they generalize. The first is
the hydrophilic holdback reagent: rather than extracting the actinides with a
soft donor, keep them in the aqueous phase with one. Tetrasulfonated
bis-1,2,4-triazines are highly effective at this, selectively forming aqueous
An(III) complexes while a conventional extractant pulls the lanthanides into the
organic phase [@lewis2015hydrophilic]. Putting the selective, expensive,
radiolytically fragile ligand in the aqueous phase where it can be replenished
is a real engineering advantage, and the same trick appears in rare earth
practice as aqueous complexant control.

The second is ALSEP, which is the most completely demonstrated version and
usefully honest about its shortfall. The flowsheet combines HEH[EHP] and T2EHDGA
in *n*-dodecane, with CDTA masking, a citrate-buffered acetohydroxamic acid
scrub for molybdenum, citrate-buffered DTPA for the An/Ln split, and a TEDGA
strip for the lanthanides — run in 32 stages of 1 cm annular centrifugal
contactors on a simulated PUREX raffinate. It recovered 95 % of the americium
and curium into a clean actinide product, losing the remaining 5 % to the
lanthanide stream, which the authors attribute to having too few actinide
stripping stages [@wilden2020countercurrent]. Among the lanthanides themselves,
lanthanum and cerium reported to the raffinate while Pr through Gd plus yttrium
reported to the lanthanide product.

**The transferable number is this.** With a genuine chemical difference to
exploit — 5f covalency, worth orders of magnitude in a soft-donor stability
constant — a 32-stage countercurrent bank achieves a 95 % split. In the
lanthanide series, where the only difference is about one percent in ionic
radius and separation factors sit near 1.5, [](#why-rare-earths-are-hard-to-separate)
shows you need on the order of a hundred stages for 99.99 % purity. The two
numbers are not a like-for-like comparison — recovering 95 % of a minor
component is a different duty from taking a major one to four nines — so the
ratio between them is not a stage-count law. What it does show is that covalency
is the single largest chemical advantage anyone in f-element separations has,
and that is both encouraging and sobering: encouraging because it shows what a
real electronic-structure difference is worth, sobering because even with it the
process is a 32-stage bank of centrifugal contactors, not a clever one-pot
trick.

## Uranium and Plutonium Outside the Plant

Separation chemistry does not end at the plant boundary, and the environmental
behaviour of these elements is a separations problem run in reverse: the
question is not how to concentrate them but why they will not stay put.

At nuclear legacy sites, the mobility of uranium and plutonium is set by
speciation rather than by bulk solubility: for uranium by redox state and by
kinetically limited surface complexation, for plutonium by colloids
[@romanchuk2020speciation]. Over 95 % of the plutonium found in groundwater in
two aquifers 1.3 km from an underground test at the Nevada site was carried on
clay and zeolite colloids rather than dissolved, travelling far beyond where its
solubility would predict, which is the same phenomenon that makes third-phase
formation and crud a nuisance in solvent extraction — a nominally dissolved
species that is actually a suspended one.

The microbial route is more directly a separations technology. Dissimilatory
metal-reducing bacteria reduce soluble U(VI) to sparingly soluble U(IV),
immobilizing it, and phosphatase-active organisms liberate inorganic phosphate
that precipitates U(VI) as uranyl phosphate biominerals. Only the first has
reached the field, in biostimulation trials at the US Department of Energy sites
at Old Rifle, Oak Ridge and Shiprock; uranium phosphate biomineralisation is
still column and microcosm work, and both reviews are careful to say that the
long-term stability of the bioreduced U(IV) is not yet established. The same
microbial redox chemistry is reviewed for technetium, neptunium, plutonium,
americium, iodine, strontium and caesium
[@newsome2014biogeochemistry; @campbell2015biogeochemical]. That is a
redox-driven precipitation separation carried out by an organism, and it belongs
in the same conversation as [](#biological-and-biomimetic-separations) and
[](#precipitation-and-selective-crystallization). The rare earth version — using
biology to reduce or precipitate selectively — is far less developed, and the
actinide field is a useful source of both methods and cautionary results.

## What This Chapter Does Not Contain

Several things a reader might expect to find here are absent, and the absences
are deliberate.

**There is no isotope separation.** Enrichment separates ²³⁵U from ²³⁸U, which
are chemically identical; it is a physical process — centrifugation, diffusion,
laser excitation — and shares no chemistry with anything else in this book. Its
absence is a scope decision, not an oversight.

**There is nothing weapons-relevant.** The plutonium chemistry here is the
chemistry of civil reprocessing and of environmental remediation, drawn from the
open peer-reviewed literature, and it is presented at the level of ligand design
and flowsheet structure that the published literature treats.

**There is no single cost figure for seawater uranium.** The published range is
quoted above, because it is a real published range and a reader is entitled to
it, but no point inside it is endorsed here. The deployment parameters those
estimates depend on — sorbent lifetime, number of reuses, marine operations
cost — are precisely the parameters the field measurements have not pinned
down, and a spread of sixteen between the extremes of the reviewed estimates is
a statement about the assumptions rather than about the ocean
[@lindner2015review]. The physical arithmetic of @guidez2016extraction is
quoted alongside it because it can be checked.

**Sorbent regeneration and multi-cycle durability is the least settled number in
the seawater literature.** About 95 % of the uranium is eluted after a single
42-day seawater exposure [@pan2016elution], and the one material taken through
eight adsorption–desorption cycles — in seawater spiked to 8 ppm uranium, not in
the sea as it is — started at 98.5 %, ended at 83.5 %, and lost roughly 5 % of its capacity per
cycle [@wang2018significantly]. Against that, the economic arithmetic assumes
about six reuses [@guidez2016extraction], and other published cost models have
assumed eighteen, twenty or twenty-five [@lindner2015review]. Iron and vanadium
accumulation is known to degrade performance across cycles without a published
number for how many cycles a real marine deployment survives. Every cost
estimate in the field is more sensitive to this parameter than to sorbent
capacity, and it is the one nobody has measured under deployment conditions.

## What Carries Back to Rare Earths

Four things in this chapter are worth taking back to a rare earth problem.

*Shape can substitute for size.* The uranyl equatorial plane gives a selectivity
handle that has no lanthanide equivalent, and the preorganized ligands built for
it [@lashley2016highly] achieve stability-constant gaps of nine orders of
magnitude against vanadium, a competitor of comparable seawater abundance. The
lanthanides offer no such geometric target, which is a real and often unstated
reason why rare earth ligand design has been less rewarding than uranyl ligand
design.

*Redox is worth more than any ligand when it is available.* Plutonium is
separated from uranium industrially by changing an oxidation state, not by
finding a selective extractant. The rare earth analogues — cerium(IV) and
europium(II) — are exploited for exactly this reason and are the only two
lanthanides that are genuinely easy to separate
([](#electrochemical-separations)).

*A dilute feed is a fatal feed unless the fluid is already moving.* The seawater
program is the best-documented demonstration that no improvement in capacity or
selectivity rescues a feed at parts per billion. What makes the case interesting
at all is that the ocean delivers itself. Where this book finds an encouraging
dilute-feed opportunity — produced water, mine drainage — it is always for the
same reason: someone else is already paying to pump the fluid.

*Measure in the real matrix.* A hundredfold gap between capacity in spiked
seawater and capacity in the sea as it is [@wang2018significantly], a 15–55 % spread
between two laboratories on the same material [@gill2016uranium], and a mass
balance in which the target metal is seventh by mole [@gill2016uranium] are
findings that only a field program produces. The rare earth literature has far
fewer such programs and correspondingly more numbers that will not survive
contact with a real feed.
