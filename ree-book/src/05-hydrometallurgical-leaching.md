---
title: Hydrometallurgical Leaching
---

(hydrometallurgical-leaching)=
# Hydrometallurgical Leaching

Leaching converts solid rare earth minerals into dissolved ions, and it is the
step that decides what the {index}`solvent extraction` circuit downstream will have to
cope with. Which method works depends almost entirely on mineralogy: {index}`bastnäsite`,
{index}`monazite`, {index}`xenotime`, and {index}`ion-adsorption clays <ion-adsorption clay>` each demand a different strategy,
because each locks its rare earths behind a different chemical barrier — a
fluorocarbonate lattice, a refractory phosphate, a {index}`thorium` burden, or nothing
more than an exchangeable surface site. This chapter follows the flowsheet from
run-of-mine ore through beneficiation, decomposition, leaching, and impurity
removal, ending at the purified aqueous feed that
[](#solvent-extraction-fundamentals) takes as its starting point.

Four themes recur. Bastnäsite must be defluorinated, normally by roasting,
before acid will touch it efficiently. Monazite releases radioactive thorium
that has to be managed as a separate stream. Ion-adsorption clays need no strong
acid at all — a mild salt solution displaces the rare earths by {index}`ion exchange` —
which is why they are treated separately in
[](#ion-adsorption-clays). And across every ore type, the emerging
alternatives — {index}`bioleaching`, supercritical CO₂, {index}`deep eutectic solvents <deep eutectic solvent>` — trade
throughput for environmental burden in ways that are not yet resolved at
industrial scale.

## Introduction: REE Mineralogy and Processing Challenges

Rare earth elements do not occur as native metals. They are found in roughly 250
minerals, of which four matter economically, and those four divide neatly by the
bond that has to be broken to get the metal out
[@jha2016hydrometallurgical; @kim2025rare].

### Major REE Minerals

**Bastnäsite**, (Ce,La,Nd,Pr)CO₃F, is a fluorocarbonate and the principal light
rare earth mineral: it is what is mined at {index}`Mountain Pass` in California
and, with monazite, at {index}`Bayan Obo` in Inner Mongolia. The pure cerium
end-member is 74.9 % rare earth oxide straight from the formula weights — 164.12 g
of Ce₂O₃ in 219.13 g of CeFCO₃ — but a concentrate carries gangue and runs lower,
60-65 % REO at Mountain Pass and 61 % at Bayan Obo [@iaea2011radiation]. The same
formula weights give the mineral's defining problem: fluorine is 8.7 wt% of it,
and acid attack on a fluoride releases HF, so the fluorine has to be dealt with
before or during the leach rather than after.

**Monazite**, (Ce,La,Nd,Th)PO₄, is a phosphate carrying both light and middle
rare earths, and it occurs as a heavy mineral in beach placers in India, Brazil
and Australia. Pure CePO₄ is 69.8 % REO by stoichiometry; natural material is
lower, and Steenkampskraal in South Africa, one of the few deposits for which a
full analysis is published, assays 57 % REO [@iaea2011radiation]. Monazite's
problem is thorium, which substitutes for the rare earths in the same lattice
site and therefore follows them through every physical separation. It is
typically 5-6 wt% ThO₂, rising to 8-10 % at Manavalakurichi in India and at
Steenkampskraal; across rare earth concentrates generally the thorium content
spans from under 0.1 % to about 10 %, with uranium up to about 1 %
[@iaea2011radiation]. That makes a monazite plant a radiological facility, and
the licensing consequences run through the whole flowsheet.

**Xenotime**, YPO₄, is the same phosphate chemistry built on yttrium, and it
carries the heavy lanthanides — dysprosium, erbium, ytterbium — that bastnäsite
and monazite do not. It occurs alongside monazite in the same placers. Pure YPO₄
is 61.4 % REO expressed as Y₂O₃, and natural xenotime assays *higher*, about 67 %
[@iaea2011radiation], because the heavy lanthanides substituting for yttrium are
much heavier than yttrium while the phosphate group they sit on is not. Xenotime
is the most refractory of the four and the hardest to decompose.

**Ion-adsorption clays**, the weathered granites of southern China, are not a
mineralogical problem at all: they contain no crystalline rare earth mineral. The
rare earths sit as hydrated cations held electrostatically on clay surfaces
[@shi2022column; @han2024efficient], which means a dilute salt solution displaces
them at ambient temperature and no cracking step is needed. The deposits are
loose layers of completely weathered granitic rock, 3-10 m thick, enriched in the
heavy elements and in yttrium, europium and terbium. The price of that easy
chemistry is grade: a few tenths of a percent REO and never above 1 %
[@iaea2011radiation], two to three orders of magnitude below a bastnäsite ore, so
the tonnage of rock and of lixiviant per tonne of product is enormous. The
arithmetic later in this chapter uses 0.05-0.3 % REO, which sits inside that
bound. Thorium and uranium are both around 0.005 % [@iaea2011radiation], low
enough that the radiological burden that dominates monazite processing does not
arise here.

### Processing Overview

Every route in this chapter has the same skeleton: mine, beneficiate, decompose
the mineral, leach, separate the solids from the liquor, purify that liquor, and
hand it to solvent extraction [@jha2016hydrometallurgical; @kim2025rare].
[](#fig-leaching-flowsheet), at the end of the chapter, draws that skeleton for
each of the ore types at once, so the routes can be compared step by step
instead of read one after another.

This chapter covers beneficiation through purification — the steps that produce
the aqueous rare earth feed. The separation of that feed into individual elements
is [](#solvent-extraction-fundamentals), and the finished oxides are downstream
of both.

### Challenges in REE Ore Processing

Four difficulties recur across all four ores, and they are worth stating together
because most of the process choices in this chapter are responses to them.

The minerals are *refractory*. Rare earth-oxygen, rare earth-phosphate and rare
earth-fluoride bonds are strong, the minerals are thermally stable, and none of
the three crystalline ores dissolves in dilute acid [@kim2025rare]. Decomposition
therefore means concentrated acid at elevated temperature, a high-temperature
roast, or concentrated caustic — all of which are expensive, and all of which
dissolve the gangue along with the target.

The *problem elements travel with the product*. Fluorine in bastnäsite comes off
as HF, toxic and corrosive, and forces either a defluorinating pre-treatment or a
scrubber on the leach [@chi2004recovery]. Thorium in monazite is radioactive,
chemically similar enough to the rare earths to resist physical separation, and
subject to a regulatory obligation that outlasts the plant
[@borai2016modified; @amaral2010thorium; @iaea2011radiation]. Neither is a trace
contaminant that can be polished out downstream; both are structural features of
the mineral.

The *ores are dilute*, most extremely so for ion-adsorption clay at a few tenths
of a percent [@iaea2011radiation]. Large volumes of rock and of reagent must be
handled per tonne of oxide, which puts reagent consumption and water use at the
centre of the economics rather than at the margins.

And the *gangue is chemically active*. Calcite and dolomite consume acid without
yielding anything; silicates form gels that will not filter; iron oxides dissolve
and contaminate the liquor. The purification circuit later in this chapter exists
almost entirely to undo what these minerals do during the leach.

## Ore Beneficiation and Pre-Concentration
Before any of that chemistry starts, physical separation concentrates the rare
earth minerals away from the gangue, so that the acid or the caustic is spent on
a tonne of concentrate rather than a hundred tonnes of rock
[@jordens2013beneficiation; @chelgani2015rare].

(crushing-and-grinding)=
### Crushing and Grinding

Comminution has exactly one purpose: to break the rock until each rare earth
grain is free of the gangue it grew against, and no further. Grinding past
liberation costs energy, makes slimes that report to the tailings and are never
recovered, and leaves a pulp that filters badly downstream. Grinding short of it
leaves locked particles that no separation can pull apart. Where the liberation
size sits is a property of the deposit and not of the mineral, so the useful
thing here is not a general size band but what two large operations actually do.

At Mountain Pass the ore is crushed in three stages to a maximum of about 10 mm
and stockpiled; different grades are then blended to a uniform 7-9 % REO
feedstock and ground in a ball mill to 100 % passing a 150-mesh screen, roughly
100 μm, before conditioning and flotation [@iaea2011radiation]. At Bayan Obo the
ore is crushed, ground and classified to 90 % below 74 μm before flotation,
magnetic separation, tabling and washing [@iaea2011radiation]. The two targets
agree to within a factor of two, which is about as much agreement as
ore-specific grinding ever shows.

Grinding also reappears much later in the flowsheet, for a different reason.
Monazite fed to caustic digestion is dry-ground to 90 % below about 50 μm and
50 % below 10 μm — finer than any flotation target — because the digestion is a
topochemical reaction and a coarse grain becomes coated with sodium hydroxide
and stops reacting [@iaea2011radiation]. There the grind is set by the
chemistry, not by liberation, and that distinction is worth keeping in mind
whenever a particle size is quoted for a rare earth process.

### Gravity Separation

Every rare earth ore mineral is heavy and the common gangue is not. Measured
densities are 4.9-5.2 g/cm³ for bastnäsite-(Ce), 4.98-5.43 for monazite-(Ce) and
4.4-5.1 for xenotime-(Y), against 2.65 for quartz, 2.71 for calcite and 3.18 for
fluorite [@anthony2001handbook]. A density contrast approaching two to one is
large by mineral-processing standards, and it is why gravity separation is the
primary operation on a placer and a pre-concentration step on hard rock
[@jordens2013beneficiation; @jordens2013processing; @zhou2024gravity].

The equipment is conventional — shaking tables, spiral concentrators, jigs, and
dense-medium separation — and the choice among them turns on particle size
rather than on mineralogy, because the settling velocity that all of these
machines exploit depends on size as strongly as on density. That is also the
method's limitation: a fine dense grain and a coarse light one fall at the same
rate, so a gravity circuit only separates within a narrow size fraction, and a
plant runs several in parallel.

What gravity separation delivers is best read from a placer circuit, where it is
the main operation rather than a scalping step. In a heavy-mineral sand plant,
oversize is screened out and slimes below about 75 μm are removed by
hydrocyclone; the sand then passes through banks of spirals that produce a
pre-concentrate of 80-85 % heavy minerals, which further spirals and wet tables
upgrade to 90-98 % [@iaea2011radiation]. Note what that circuit concentrates:
*heavy minerals* collectively — ilmenite, rutile, zircon, monazite, xenotime —
not rare earths. Pulling monazite out of that mixture is a magnetic problem, and
it happens dry and downstream.

No general recovery or enrichment factor is quoted here. Bands of that kind are
widely repeated for rare earth gravity separation but could not be traced to a
study that measures them, and they would be meaningless in any case without the
feed grade and the deposit they came from. @zhou2024gravity shows the
alternative: on the Balzhe niobium-zirconium-rare earth ore they compare a
dense-medium cyclone, a shaking table and a Knelson centrifuge across three size
fractions and report the grade each achieves, reaching total rare earth oxide
grades of 0.41-0.44 % on a feed of a few tenths of a percent. Those are small
numbers because the ore is poor, which is exactly the point: an enrichment ratio
is a statement about an ore, not about a machine.

### Magnetic Separation

Monazite and xenotime are paramagnetic [@anthony2001handbook], bastnäsite only
weakly so, and the silicate and carbonate gangue is effectively non-magnetic.
That is enough of a difference to sort them, and because magnetic separation is
a dry operation it is normally placed after a wet gravity circuit has already
discarded most of the mass [@chen2023various]. Published susceptibility values
for these minerals vary with iron substitution and with how the measurement was
made, and none is quoted here; what the flowsheet actually relies on is the
ordering — ferromagnetic, paramagnetic, non-magnetic — not the magnitudes.

Three classes of machine work that ordering at three field strengths. A
low-intensity separator takes out ferromagnetic material: magnetite, and the
tramp iron every mill sheds. A high-intensity separator recovers the
paramagnetic rare earth phosphates. A high-gradient separator, in which the
field is concentrated onto a matrix of steel wool or expanded metal, extends the
same principle to particles too fine for a uniform field to move.

The industrially decisive use is the monazite-zircon split in a mineral sands
plant. Ilmenite, which has the highest susceptibility, comes out first; rutile
and zircon are then separated electrostatically on their conductivity
difference; and magnetic separation is what finally removes the paramagnetic
monazite from the non-magnetic zircon. Where that monazite is destined for
chemical processing, its concentrate is upgraded magnetically to 97-99 % purity
[@iaea2011radiation]. That figure is worth holding onto, because it means the
feed to a monazite cracking plant is close to a pure mineral rather than an ore,
and every digestion condition discussed later in this chapter assumes it.

At Bayan Obo magnetic separation does something else entirely. The deposit is an
iron ore that happens to carry rare earths, and the beneficiation circuit
recovers magnetite and haematite, together with fluorite and niobium oxide,
alongside the rare earth concentrate [@iaea2011radiation]. No overall rare earth
recovery for that circuit is reported by the sources used here, and none is
given.

### Froth Flotation
**The principal beneficiation method** for bastnäsite and monazite [@chelgani2015rare; @jordens2013beneficiation]

#### Bastnäsite Flotation

Bastnäsite is floated with anionic collectors — fatty acids such as oleic acid
and tall oil, and increasingly hydroxamic acids — which bind through a
carboxylate or hydroxamate head group to rare earth cations exposed on the
fracture surface and leave a hydrocarbon tail pointing into the water
[@jordens2013beneficiation; @chelgani2015rare]. Making that surface complex is
the whole of the chemistry; everything else in the reagent suite exists to stop
the same thing happening on the gangue. Sodium silicate depresses silicates,
quebracho and other tannins depress calcite, and fluoride is used for selective
depression.

The difficulty is structural rather than a matter of dosage. The principal
gangue minerals of a rare earth carbonatite — calcite, barite, fluorite — are
themselves alkaline-earth salts presenting hard divalent cations at their
surfaces, and a carboxylate collector is perfectly happy to bind those too.
Bastnäsite flotation is therefore a selectivity problem, not a recovery problem,
and it is why hydroxamates, which chelate the rare earth cation rather than
merely ion-pairing with it, have displaced plain fatty acids where the ore can
afford them. Collector dosages and operating pH windows are deposit-specific and none is
quoted here; no primary source could be traced for a general value.

One operating detail deserves naming because it is unusual outside this
industry: Mountain Pass floats *hot*. Conditioning and flotation are run at
elevated temperature [@iaea2011radiation], which sharpens the difference between
the collector's affinity for bastnäsite and its affinity for calcite in a way
that no reagent addition at ambient temperature achieves.

The circuit itself is conventional — rougher, scavenger and cleaner stages in
series, as in any sulphide plant. Grades and recoveries are strongly deposit-
and mineralogy-specific, and no general band is given. One sourced result
conveys the flavour: in a selective-flotation study on Bayan Obo ore, 84.7 % of
the bastnäsite was recovered into a concentrate assaying 97.2 % bastnäsite and
69.5 % REO [@iaea2011radiation]. Even that does not close the problem, because
bastnäsite and monazite are partly intergrown in this ore, so a third product —
a mixed bastnäsite-monazite concentrate of 40-60 % REO — is unavoidable, and it
is that mixed material which feeds the sulfuric route described later.

#### Monazite and Xenotime Flotation

Monazite and xenotime are floated with hydroxamic acids and alkyl phosphates
rather than with plain fatty acids, and the reason is apatite [@chelgani2015rare].
Apatite is another phosphate, it occurs with the rare earth phosphates in most
deposits that carry them, and its surface chemistry is close enough that a
carboxylate collector cannot tell the two apart. A hydroxamate chelates the rare
earth cation instead of simply ion-pairing with it, which buys some selectivity;
the rest has to come from depressants chosen against the particular gangue.

Below about 20 μm the problem changes character rather than degree. Fine
particles carry too little mass to hold a bubble reliably and too much surface
area per tonne to be worth collecting, so they are lost to the tailings whatever
the reagent scheme — which is the same slimes penalty that made the gravity
circuit reject everything below 75 μm. The circuit is the usual
rougher-cleaner-scavenger arrangement, roughers sized for recovery and cleaners
for grade; the number of stages is deposit-specific and no figure is given here.

It is worth being blunt that flotation is not how most of the world's monazite
has actually been recovered. Placer monazite — the Indian, Brazilian and
Australian beach sands that supplied the industry for decades — is concentrated
by wet gravity separation followed by dry magnetic and electrostatic separation,
with flotation appearing only for the fine cleaning of particular minerals
[@iaea2011radiation]. Flotation is the hard-rock route. On a placer, geology has
already done the liberation, and physics is cheaper than chemistry.

### What Beneficiation Hands Over

The product of everything above is a *concentrate*, and the single number that
matters to the rest of this chapter is its grade, because the grade is what
fixes the reagent bill and the residue tonnage per tonne of oxide made. Feed
grade, product grade and recovery are only meaningful together and from one
operation, so rather than a general band, here are two chains taken whole from a
single source.

At **Mountain Pass** the ore carries 10-15 % bastnäsite, 12 % on average, and
2-12 % REO. Stockpiles of different grades are blended to a uniform 7-9 % REO
feed; the ore is crushed in three stages to about 10 mm, ball-milled to roughly
100 μm, conditioned, and floated hot; and the product is a bastnäsite
concentrate of 60-65 % REO [@iaea2011radiation].

At **Bayan Obo** the ore is crushed, ground and classified to 90 % below 74 μm,
then treated by flotation, magnetic separation, tabling and washing to a mineral
concentrate containing 65-67 % bastnäsite and 14-15 % monazite and assaying 61 %
REO [@iaea2011radiation]. Further dressing splits that into separate bastnäsite
and monazite products plus the unavoidable mixed concentrate noted above.

Neither chain carries a recovery figure, and that omission is deliberate. The
source that documents these grades does not report the overall rare earth
recovery of either plant, so none is asserted. The "60-80 % overall recovery"
that circulates for rare earth beneficiation could not be traced to a
measurement and has been removed rather than re-attributed; where a recovery is
needed later in this chapter, the arithmetic is done at perfect recovery to give
a floor, and the shortfall is left explicit.

## Bastnäsite Processing: Roasting and Leaching
### The Fluorine Problem
Fluorine is 8.7 wt% of pure bastnäsite by formula weight (19.00 g of F in
219.13 g of CeFCO₃), and somewhat less of a concentrate diluted by gangue. It is
stoichiometrically unavoidable, and direct acid leaching releases it as HF gas
[@kim2025rare]:

$$
2\,\mathrm{REE}\cdot\mathrm{FCO_3} + 3\,\mathrm{H_2SO_4} \rightarrow
  \mathrm{REE_2(SO_4)_3} + 2\,\mathrm{HF}\uparrow + 2\,\mathrm{CO_2}\uparrow + 2\,\mathrm{H_2O}
$$

Hydrogen fluoride is acutely toxic, attacks glass and most alloys, and is
tightly regulated as an emission; chronic exposure of populations near
uncontrolled plants causes fluorosis. (Occupational exposure limits are set by
national regulators and are not quoted here.) An HF-generating leach therefore
buys three obligations at once — specialised materials of construction, a
scrubbing train on the off-gas, and a fluoride-bearing effluent to neutralise —
and the point of the roasting routes below is to discharge one or more of them
by fixing the fluorine somewhere else before the acid ever arrives
[@chi2004recovery; @kim2025rare].

### Thermal Decomposition (Roasting)
#### Simple Calcination
The simplest route is to heat bastnäsite in air and let the mineral take itself
apart in two steps [@kim2025rare]. Decarbonation to the oxyfluoride comes first,
between 300 and 500 °C:

$$
\mathrm{REE}\cdot\mathrm{FCO_3} \rightarrow \mathrm{REEOF} + \mathrm{CO_2}\uparrow
$$

Between 500 and 700 °C the oxyfluoride is hydrolysed to the oxide, which evolves
HF only if water vapour is present:

$$
2\,\mathrm{REEOF} + \mathrm{H_2O} \rightarrow \mathrm{REE_2O_3} + 2\,\mathrm{HF}\uparrow
$$

Calcination is the cheapest option available, because it adds no reagent at all:
heat, air, and a scrubber. Two operating points are on record. Mountain Pass
calcines its acid-washed concentrate at 600-800 °C, which decomposes any
remaining carbonate and converts about half of the Ce(III) present to Ce(IV),
producing an oxide mixture assaying 85-90 % REO [@iaea2011radiation]. In the
laboratory, @sinclair2017rare dry-roast bastnäsite concentrate at 730 °C for
three hours as a pretreatment. No general window is given: the roast is set on the
particular concentrate, and those two operating points are what the sources
actually report.

What the calcine costs is set by where the fluorine goes and by what the product
is. The fluorine leaves as HF, so the scrubbing obligation is not discharged, it
is merely moved from the leach to the furnace — which is at least an easier
place to put it, because the off-gas is dry, hot and of known composition rather
than mixed with acid mist. The larger price is the product. A calcined
sesquioxide is refractory: having driven off the carbonate that made the mineral
vulnerable, the roast leaves a lattice that dilute acid does not attack quickly,
and dissolution then wants concentrated acid at temperature. The two routes that
follow both exist to avoid that outcome, by roasting the mineral into something
soluble rather than into an oxide.

#### Alkaline Roasting (Sodium Carbonate Process)
The alkaline route mixes the concentrate with sodium carbonate before roasting,
which gives the fluorine somewhere to go that is not the off-gas [@kim2025rare].

Step 1, defluorination at 400-500 °C:

$$
2\,\mathrm{REE}\cdot\mathrm{FCO_3} + \mathrm{Na_2CO_3} \rightarrow
  \mathrm{REE_2O_2CO_3} + 2\,\mathrm{NaF} + 2\,\mathrm{CO_2}\uparrow
$$

Step 2, complete decomposition at 700-900 °C:

$$
\mathrm{REE_2O_2CO_3} + \mathrm{Na_2CO_3} \rightarrow 2\,\mathrm{NaREEO_2} + 2\,\mathrm{CO_2}\uparrow
$$

The soda-ash charge and the residence time are process variables set on the
particular concentrate, and no representative values are asserted. What the
stoichiometry does fix is the minimum: one mole of Na₂CO₃ per two moles of mineral for the defluorination
step, and a second mole per two moles for the conversion to sodium rare earth
oxide, so a soda-ash charge below about 0.5 mol per mole of REE cannot complete
the reaction whatever the temperature.

The product, NaREEO₂, is the reason for the route: unlike a calcined
sesquioxide it is attacked by water and by dilute acid.

**Water leaching of roasted product**:

$$
\mathrm{NaREEO_2} + \mathrm{H_2O} \rightarrow \mathrm{NaOH} + \mathrm{REEO(OH)}
$$

$$
\mathrm{REEO(OH)} + 3\,\mathrm{HCl} \rightarrow \mathrm{REECl_3} + 2\,\mathrm{H_2O}
$$

Or, by direct acid dissolution of the roasted product:

$$
2\,\mathrm{NaREEO_2} + 4\,\mathrm{H_2SO_4} \rightarrow
  \mathrm{REE_2(SO_4)_3} + \mathrm{Na_2SO_4} + 4\,\mathrm{H_2O}
$$

Two things are bought here and both are real. The fluorine is captured as solid
sodium fluoride in the calcine rather than evolved as HF, which converts a
gas-handling problem into a solids-handling one; and the roasted product
dissolves under conditions a calcined oxide would not yield to, which cuts the
acid consumption and the corrosion duty of the leach that follows. The price is
paid three times over: soda ash is a bulk reagent bought by the tonne, the
furnace still has to reach the higher of the two reaction temperatures, and the
sodium that captured the fluorine leaves in the effluent as sodium fluoride and,
once sulfuric acid is used downstream, as sodium sulfate. Neither salt has much
value, and the fluoride is the one that constrains discharge. In effect the
route trades an air-emission problem for a solid- and liquid-waste problem, and
whether that is an improvement depends entirely on the local regulatory regime
and on whether there is a fluoride offtake nearby.

#### Ammonium Chloride Roasting (Fluorine Deactivation)
The third roasting route, developed by Chinese researchers, uses ammonium
chloride and converts the mineral straight to a soluble chloride
[@chi2004recovery]:

$$
\mathrm{REE}\cdot\mathrm{FCO_3} + 3\,\mathrm{NH_4Cl} \rightarrow
  \mathrm{REECl_3} + \mathrm{NH_4F} + 2\,\mathrm{NH_3}\uparrow + \mathrm{CO_2}\uparrow + \mathrm{H_2O}
$$

The stoichiometry fixes the reagent demand at three moles of NH₄Cl per mole of
mineral and nothing else about the operating point. What can be said without a
number is why the route is attractive. It converts the mineral directly to REECl₃, which water alone will
dissolve — no acid leach at all, and no medium conversion before a chloride-based
extraction circuit. And the fluorine is *deactivated* rather than volatilised: it
leaves in the solid as ammonium fluoride instead of leaving up the stack as HF.
Whether that fluoride is sold, converted, or disposed of is a question the source
does not settle, and it matters, because ammonium fluoride is soluble and will
follow the water leach unless it is deliberately removed.

The cost side has two entries. Ammonium chloride is the more expensive reagent
per tonne of the three roasting routes here, and the reaction liberates ammonia,
which has to be scrubbed and is worth recycling as NH₄Cl if the plant is large
enough to justify the loop. The route is Chinese in origin and is not, so far as
the sources here establish, operated at Western plants [@chi2004recovery].

### Acid Leaching of Roasted Bastnäsite
#### Sulfuric Acid Leaching
**After alkaline roasting** [@kim2025rare]:

The roasted material is REE₂O₃ or NaREEO₂, and it dissolves as the sulfate:

$$
\mathrm{REE_2O_3} + 3\,\mathrm{H_2SO_4} \rightarrow \mathrm{REE_2(SO_4)_3} + 3\,\mathrm{H_2O}
$$

No operating window is given here, and no extraction efficiency. Both belong to a
specific concentrate under specific conditions rather than to the route as such,
and neither could be traced to a primary measurement. One qualitative dependence
is worth keeping: leaching efficiency depends on the roast that preceded it, and
there is an optimum rather than a monotone improvement, because a roast hot
enough to sinter the charge closes the porosity the acid needs.

The industrial version of this chemistry is not a dilute-acid leach at all. At
Bayan Obo the concentrate is mixed with *concentrated* sulfuric acid and reacted
in a kiln; 200 °C is enough for the reaction to proceed, but the mass is taken to
as much as 600 °C on purpose, because at that temperature thorium and iron
sulfates decompose to insoluble products while the rare earth sulfates survive
[@iaea2011radiation]. The high-temperature bake is therefore doing a separation,
not just a dissolution. Water then leaches the rare earth sulfate out of the
calcine and leaves thorium, iron, barium sulfate, calcium sulfate and silica in
the cake.

#### Hydrochloric Acid Leaching

$$
\mathrm{REE_2O_3} + 6\,\mathrm{HCl} \rightarrow 2\,\mathrm{REECl_3} + 3\,\mathrm{H_2O}
$$

The industrial operating point is a 30 % hydrochloric acid leach of the calcined
material at Mountain Pass [@iaea2011radiation]. No general band is given for the
others.

The case for hydrochloric acid over sulfuric is almost entirely about what
happens downstream. Rare earth chlorides are considerably more soluble than the
sulfates, so the leach liquor can be more concentrated and the circuit smaller;
and the acidic organophosphorus extractants that do the separation work —
{index}`D2EHPA`, {index}`PC88A` — are operated in chloride medium, so a chloride
leach hands solvent extraction a feed it can use without a precipitation and
redissolution cycle in between. That is the whole of the argument, and it is
enough: the conversion step avoided is a real capital and yield cost, treated in
[](#solvent-extraction-fundamentals).

What is paid for it is corrosion. Hot concentrated HCl attacks stainless steel,
so the leach train is rubber- or glass-lined or titanium, and the vapour above it
is itself a corrosive emission requiring containment and scrubbing. Hydrochloric
acid is also the more expensive reagent per mole of protons delivered. A plant
choosing between the two acids is choosing between paying at the leach (HCl) and
paying at the conversion (H₂SO₄), and the two large bastnäsite operations went
opposite ways — which is why they are worth comparing directly.

### Alternative: Supercritical CO₂ Extraction
**Emerging method** [@sinclair2017rare]

Roasted bastnäsite is contacted with supercritical CO₂ carrying a complexing
agent, which is what makes the rare earths CO₂-soluble at all.

What follows is a single laboratory operating point, not a process window, and it
is worth giving in full because the supercritical literature is usually quoted as
a vague band. @sinclair2017rare pretreat bastnäsite concentrate two ways — dry
roasting at 730 °C for three hours, or decomposition in 50 % NaOH at 150 °C for
four hours — and extract the pretreated powder in supercritical CO₂ at **34 MPa
and 65 °C** using nitric acid/{index}`TBP` adducts. Adduct composition is the
variable that matters: across 2 to 6 mol/L H⁺, extraction is fastest at about
**4 M HNO₃**, and *more* acid is worse, cutting the extraction of cerium,
praseodymium and neodymium — the authors attribute this either to aqueous
droplets forming and imposing an equilibrium limit, or to nitric acid competing
with the rare earth nitrates for coordination to TBP.

The recoveries are the reason to take the method seriously. With the 4 mol/L H⁺
adduct at 5.0 mol %, the *roasted* material gave 72 % La, 96 % Ce, 88 % Pr and
90 % Nd after 120 minutes; the *NaOH-digested* material, at 5.1 mol % adduct,
gave 93 % La, 100 % Ce, 99 % Pr and 101 % Nd after only 90 minutes
[@sinclair2017rare]. (The 101 % is theirs, and it is the honest indication of the
uncertainty on these assays.) Note that the caustic pretreatment beats the roast
on every element and is faster — the same conclusion the monazite literature
reached by a different road.
The attraction is the solvent. Carbon dioxide is cheap, non-toxic,
non-flammable, and depressurises to a gas that can be recompressed and reused,
so the extraction leaves no spent aqueous stream to neutralise — the rare earths
come out of the vessel with the complexing agent and the CO₂ simply leaves. The
temperature is mild by hydrometallurgical standards.

The catch is that none of that removes the pretreatment. The concentrate still
has to be roasted or caustic-digested before the extraction works at all, so the
furnace and its off-gas train stay in the flowsheet: supercritical CO₂ replaces
the leach tank, not the plant. Against that, the vessel is now a pressure vessel
at 34 MPa, which is a different capital class from a stirred tank, and it is a
batch unit where the aqueous route is continuous. The method is at laboratory
scale — the authors themselves describe their results as a step toward
demonstrating applicability rather than as a demonstration — and no comparison of
extraction rate against aqueous leaching under matched conditions is available to
quote [@sinclair2017rare].
### Two Industrial Routes Compared: Mountain Pass and Bayan Obo

The two large bastnäsite operations chose opposite acids, and the choice
propagates all the way to the solvent extraction circuit. It is worth setting
them side by side, because the difference is often blurred in secondary
sources.

#### Mountain Pass (USA): oxidative roast, then HCl

The Molycorp route is a *chloride* route throughout
[@gupta2004extractive; @castor2006rare]:

1.  **Beneficiation**: flotation of the carbonatite ore to a bastnäsite
    concentrate of 60-65 % REO [@iaea2011radiation].
2.  **Acid pre-leach**: hydrochloric acid dissolves the carbonate gangue —
    calcite and strontianite — raising the concentrate from 60-65 % to a leached
    concentrate of 68-72 % rare earths before it ever sees a furnace
    [@iaea2011radiation]. This is a gangue-removal step, not a REE-dissolution
    step: the bastnäsite itself is barely touched by dilute acid at ambient
    temperature, and the barite is not touched at all.
3.  **Oxidative roast**: calcination at 600-800 °C decomposes any carbonate that
    survived the pre-leach and converts about half the Ce³⁺ present to Ce⁴⁺,
    giving an oxide mixture of 85-90 % REO [@iaea2011radiation]. Cerium is close
    to half of the REE inventory in this ore, so this one step does the single
    largest separation in the flowsheet.
4.  **HCl leach**: the calcine is slurried with water and leached in 30 %
    hydrochloric acid [@iaea2011radiation]. The trivalent rare earths dissolve
    as REECl₃; Ce(IV) does not, and stays in the residue with the fluorides. The
    leach liquor is therefore already cerium-depleted before solvent extraction
    begins.
5.  **Cerium by-product**: that residue becomes a low-grade cerium concentrate
    of 65-70 % REO and 55-60 % CeO₂, sold as-is for glass polishing or upgraded
    to a 96 % cerium product by digesting the fluorides with sodium hydroxide
    and releaching in HCl [@iaea2011radiation]. The upgrade is not free: it
    generates barium sulfates, a residue of mixed rare earth fluorides, and a
    sodium chloride wastewater.
6.  **Purification and hand-off**: the leachate, carrying Ce³⁺, the other rare
    earths, iron and lead, is contacted with soda ash and tailings slurry to
    convert iron chloride to insoluble iron hydroxide, which reports to the
    tailings [@iaea2011radiation]. The iron-free mixed REE chloride solution
    goes to the solvent extraction cascade — no medium conversion is required,
    because the circuit never left chloride.

Note what this flowsheet does *not* contain: there is no sulfuric acid bake and
no sulfate-to-chloride conversion. Descriptions that leach Mountain Pass with
concentrated H₂SO₄ and then "evaporate the sulfuric acid" to reach a chloride
feed are not describing this plant, and are not describing a process that can
work — H₂SO₄ boils at 337 °C, far above HCl, so it is the hydrochloric acid
that leaves first. Converting a sulfate liquor to a chloride liquor requires
precipitating the rare earths as hydroxide, carbonate or oxalate and
redissolving the solid in HCl.

#### Bayan Obo (China): concentrated sulfuric acid roast

The sulfuric route is the Chinese practice for bastnäsite and mixed
bastnäsite-monazite concentrates [@kim2025rare]:

1.  Mix the mixed bastnäsite-monazite concentrate, 40-60 % REO, with
    concentrated H₂SO₄ and react it in a furnace or kiln. Two hundred degrees is
    enough for the decomposition to proceed, but the mass is taken to as much as
    600 °C deliberately, because at that temperature the thorium and iron
    sulfates convert to insoluble products while the rare earth sulfates remain
    stable [@iaea2011radiation]. HF, CO₂ and SO₃ leave together, and the off-gas
    is scrubbed through milk of lime.
2.  Water-leach the calcine to dissolve REE₂(SO₄)₃, filtering off a cake of
    thorium, iron, barium sulfate, calcium sulfate and silica.
3.  Recover the rare earths from the sulfate liquor — historically by
    precipitating the sodium double sulfate, now preferentially by solvent
    extraction — and strip with HCl if a chloride feed is wanted for the
    separation circuit [@iaea2011radiation].

The sulfuric route tolerates a lower-grade, more variable concentrate and does
not require the cerium oxidation step; it pays for that with fluorine and
sulfate management, and with the extra recovery-and-strip cycle if the
downstream extractant wants chloride. It also pays in slag: the slag-to-
concentrate mass ratio runs as high as 0.66, so thousands of tonnes a year of
material assaying 0.2 % Th must be stored as a radioactive residue
[@iaea2011radiation]. That number is the honest measure of what the route costs,
and it is the kind of figure that a comparison table of "advantages and
disadvantages" never carries.

## Monazite Processing: Phosphate Decomposition
### The Phosphate and Thorium Problems
Monazite is a rare earth orthophosphate, (REE,Th)PO₄, and both halves of that
formula are a problem [@borai2016modified; @amaral2010thorium].

The phosphate is the chemical problem. It is a dense, thermodynamically stable
lattice that a strong acid does not attack at ambient conditions, because there
is no anion in it that protonation can carry away as a gas or a weak acid at
moderate temperature — the contrast with a carbonate, which gives up CO₂ and
falls apart, is exactly the point. Every monazite route in industrial use is
therefore a *decomposition* rather than a leach: something has to break the
RE–PO₄ bond before any dissolution chemistry begins, and the two candidates are
concentrated sulfuric acid at 200 °C and above, or concentrated caustic. Which
one a plant picks determines the rest of its flowsheet, including where the
thorium ends up.

The thorium is the regulatory problem, and it is not a trace. Monazite from
heavy-mineral sands typically carries 5-6 wt% ThO₂; Indian monazite runs 6-11 %,
while the 'black monazite' of Taiwan, China is unusually low at 0.2-0.9 %
[@iaea2011radiation]. At 5-6 % ThO₂ the ²³²Th activity concentration is around
200 Bq/g, an order of magnitude or more above the levels at which material
enters regulatory control in most jurisdictions. Thorium has no large market, so
a monazite plant produces a radioactive residue it must store rather than sell —
which is the reason monazite processing was abandoned in several countries that
had the ore, and the reason a monazite flowsheet is judged as much by where it
puts the thorium as by how much rare earth it recovers.

### Acid Leaching Methods
#### Sulfuric Acid Digestion (Classical Method)
Concentrated sulfuric acid attacks the phosphate lattice directly, taking the
rare earths and the thorium into solution together and leaving phosphoric acid
behind [@jha2016hydrometallurgical]:

$$
2\,\mathrm{REEPO_4} + 3\,\mathrm{H_2SO_4} \rightarrow \mathrm{REE_2(SO_4)_3} + 2\,\mathrm{H_3PO_4}
$$

$$
\mathrm{Th_3(PO_4)_4} + 6\,\mathrm{H_2SO_4} \rightarrow 3\,\mathrm{Th(SO_4)_2} + 4\,\mathrm{H_3PO_4}
$$

This is the oldest industrial monazite route and it is worth understanding
properly, because it explains both why it dominated for decades and why it was
displaced. Ground monazite is mixed with 98 % sulfuric acid and digested at
200-220 °C [@iaea2011radiation]. The decomposition is exothermic and the charge
does not stay a slurry: it thickens into a pasty mass of sulfates and acid
sulfates suspended in the phosphoric acid the reaction has just liberated and in
the excess sulfuric acid. That paste is the defining feature of the process. It
is why the vessel is a heavy, acid-resistant digester with a substantial agitator
rather than a leach tank, why the residence time is long, and why the step is
hard to run continuously. The reagent charge and the residence time are set on
the particular concentrate and no general band is given. The stoichiometry sets a
floor
of 1.5 mol H₂SO₄ per mole of rare earth, and industrial practice runs in excess
of that, but by how much is a plant variable.

Water then dissolves the sulfates. Historically the rare earths were taken out of
that liquor by adding sodium sulfate, which precipitates the light rare earths
selectively as the double sulfate RE₂(SO₄)₃·Na₂SO₄·3H₂O and leaves thorium, some
of the heavy rare earths, iron and uranium in solution [@iaea2011radiation]. The
double sulfate is converted to hydroxide with NaOH, and fractional dissolution in
hydrochloric acid then reprecipitates the residual thorium, uranium and iron and
gives a rare earth chloride solution — the classical starting point for
commercial products.

Three things killed this route, and they are all visible in that description.
The first is the thorium: the separation is not clean, a significant part of the
thorium comes down with the rare earth double sulfate, and the rare earth
fraction then needs extensive purification to reach market specification
[@iaea2011radiation]. The second is yield: the fractional-dissolution version
gives a low recovery of rare earths, which is why solvent extraction from the
sulfate liquor, stripped with HCl to give the chloride, replaced it where the
route survived at all. The third is the phosphate, which does not leave as a
product but stays in solution as H₃PO₄ mixed into the rare earth liquor, from
which it must be removed — usually by gypsum co-precipitation — as a waste rather
than sold as a by-product. Add hot concentrated acid as the working fluid, with
the corrosion and energy that implies, and the caustic route's advantages become
obvious. No extraction efficiency is quoted: the sources that describe this route describe
its recovery as poor in the classical form, and no measured figure for it could
be traced.

#### Why There Is No Direct Hydrochloric Acid Route

Hydrochloric acid, which handles roasted bastnäsite easily, does not attack
monazite. The monazite lattice is a dense, thermodynamically stable orthophosphate,
and unlike a carbonate or an oxide it offers no anion that a strong acid can
protonate and carry off as a gas or a weak acid at moderate temperature.
Hydrochloric acid also cannot be pushed to the temperatures that make
concentrated H₂SO₄ work: it azeotropes at 110 °C and 20 wt%, so a hot digestion
means a pressure vessel full of HCl vapour, and even then the phosphate matrix
survives.

This is why every industrial monazite flowsheet reaches a chloride liquor
*indirectly* — by concentrated sulfuric acid digestion or caustic digestion
first, then precipitation of the rare earths as hydroxide and redissolution of
that hydroxide in HCl. The hydroxide dissolves in dilute acid in minutes; the
phosphate never would.

#### Nitric Acid Leaching
Used in some processes:

$$
\mathrm{REEPO_4} + 3\,\mathrm{HNO_3} \rightarrow \mathrm{REE(NO_3)_3} + \mathrm{H_3PO_4}
$$

$$
\mathrm{Th_3(PO_4)_4} + 12\,\mathrm{HNO_3} \rightarrow 3\,\mathrm{Th(NO_3)_4} + 4\,\mathrm{H_3PO_4}
$$

No operating conditions are given, because nitric acid is not a primary monazite
decomposition reagent in industrial practice — the IAEA
describes it as a *variation* on the caustic route, in which the hydroxide cake
from a NaOH digestion is leached with HNO₃ instead of HCl to give rare earth
nitrates rather than chlorides [@iaea2011radiation].

The reason to want nitrates is entirely downstream. {index}`TBP` extracts from
nitrate medium and extracts thorium preferentially over the trivalent rare
earths, so a nitrate liquor lets one extractant do the thorium separation and the
rare earth recovery in the same circuit. If the plant's separation train is
chloride-based, the nitrate offers nothing and the extra reagent cost is wasted.

### Alkaline Decomposition Methods
#### Sodium Hydroxide Digestion
The alkaline route inverts the order: it converts the phosphates to hydroxides
first, and only then chooses an acid
[@xu2012decomposition; @shahreldin2018selective].

Step 1, alkaline digestion at 140-160 °C in 60-70 wt% NaOH at atmospheric
pressure, converts the phosphates to hydroxides:

$$
\mathrm{REEPO_4} + 3\,\mathrm{NaOH} \rightarrow \mathrm{REE(OH)_3} + \mathrm{Na_3PO_4}
$$

$$
\mathrm{Th_3(PO_4)_4} + 12\,\mathrm{NaOH} \rightarrow 3\,\mathrm{Th(OH)_4} + 4\,\mathrm{Na_3PO_4}
$$

Step 2, water leaching, dissolves the Na₃PO₄ and removes the phosphate, leaving
REE(OH)₃ and Th(OH)₄ as solids. Step 3 redissolves those hydroxides in dilute
acid:

$$
\mathrm{REE(OH)_3} + 3\,\mathrm{HCl} \rightarrow \mathrm{REECl_3} + 3\,\mathrm{H_2O}
$$

$$
\mathrm{Th(OH)_4} + 4\,\mathrm{HCl} \rightarrow \mathrm{ThCl_4} + 4\,\mathrm{H_2O}
$$

Industrial practice is well documented, and the numbers are worth having exactly
[@iaea2011radiation]. The monazite is dry ground in a ball mill to 90 % below
about 50 µm and 50 % below about 10 µm — not for surface area alone, but because
coarse grains become coated with sodium hydroxide and stop reacting, so the
digestion is incomplete. The ground material is digested at 140-160 °C for 3-9 h
in a 60-70 % sodium hydroxide solution, at atmospheric pressure. The caustic
charge is about **0.75 kg of NaOH per kilogram of monazite**, an excess of
roughly 50 % over stoichiometry, and that excess is recovered and reused. The
"3-5:1 NaOH-to-monazite ratio" that circulates in secondary accounts is high by a
factor of about five against this figure.

The atmospheric-pressure operation is the point of the concentrated caustic and
deserves a sentence of its own, because it is routinely misreported. A 60-70 wt%
NaOH solution boils well above 140 °C — the boiling-point elevation of the
concentrated caustic is large enough that the digester can be an open, stirred,
steam-jacketed vessel rather than an autoclave. That is the whole economic
argument for the caustic route against the sulfuric one: no pressure vessel, no
200-250 °C acid, and the phosphate leaves as a saleable trisodium phosphate
solution instead of as phosphoric acid mixed into the rare earth liquor. Figures
in the 300-400 °C range belong to *caustic fusion*, a different (and much
harsher) laboratory and analytical procedure in which the sample is fused with
solid NaOH; do not carry them into a description of the industrial digestion.

Hot water then dissolves the trisodium phosphate, and the numbers here are the
reason the route won. The phosphate solution carries **99.7 % of the phosphate
originally in the monazite**, along with sodium hydroxide at 47 %; it is
clarified, vacuum-evaporated, and the Na₃PO₄ crystals are centrifuged and dried
for sale as a by-product containing 17.5-19 % P₂O₅. The entire thorium and rare
earth content stays behind as a hydroxide cake.

The hydroxide cake is then leached selectively, and this is where the caustic
route earns its second advantage. The cake is slurried in water and 30 %
hydrochloric acid is added while the pH is held at 3-4 and the temperature at
70-80 °C. Because the rare earth and thorium hydroxides differ in basicity,
**97.7 % of the rare earths dissolve as chlorides** while most of the thorium
stays behind in the solid hydroxide residue [@iaea2011radiation]. Thorium
separation, which the sulfuric route could only achieve by extensive downstream
purification, here falls out of a pH-controlled dissolution.

So the caustic route wins on four counts: the phosphate leaves as a saleable
product rather than as a contaminant in the liquor, the acid demand collapses
because dissolving a fresh hydroxide is trivial next to decomposing a phosphate
lattice, the thorium is rejected early and as a solid, and the digester is an
open vessel. What it costs is caustic soda — a bulk reagent, though half the
excess is recycled — and the fact that the thorium rejection is not complete:
residual rare earths stay locked in the thorium cake and can only be recovered by
processing that cake, which most plants do not do. Two independent studies of
Egyptian monazite reach the same conclusion about phosphate-first processing
[@xu2012decomposition; @shahreldin2018selective].

#### Sodium Carbonate Roasting
Similar to bastnäsite:

$$
2\,\mathrm{REEPO_4} + 3\,\mathrm{Na_2CO_3} \rightarrow
  \mathrm{REE_2O_3} + 2\,\mathrm{Na_3PO_4} + 3\,\mathrm{CO_2}\uparrow
$$

$$
\mathrm{Th_3(PO_4)_4} + 6\,\mathrm{Na_2CO_3} \rightarrow
  3\,\mathrm{ThO_2} + 4\,\mathrm{Na_3PO_4} + 6\,\mathrm{CO_2}\uparrow
$$

No operating conditions are given: soda-ash roasting of monazite is not, on the
evidence assembled here, in industrial use — the caustic digestion above
displaced it. The stoichiometry fixes a floor of 1.5
mol Na₂CO₃ per mole of rare earth phosphate, and the roast has to be hot enough
to drive CO₂ off, which puts it above the caustic digestion's temperature and
back into a furnace. The attraction, as with bastnäsite, is that the phosphate
leaves as Na₃PO₄ and the rare earths are left as an oxide the acid can reach.

### Modified Leaching for Thorium Separation
Both routes above leave thorium and rare earths together in the same solid, and
both then rely on a difference in solubility rather than on a dedicated
separation unit to pull them apart. Two published variants show how far that can
be pushed.

**Method 1: Modified acid leaching.** @borai2016modified separate thorium,
phosphate and a rare earth concentrate from Egyptian crude monazite by
controlling the leaching conditions rather than by adding a separation step:
the strategy is to exploit the different solubilities of the thorium and rare
earth phases under a chosen acidity, and take them off in sequence.

**Method 2: Alkaline processing, then extraction.** @shahreldin2018selective
process Egyptian monazite concentrate through alkali solution and remove the
phosphate first — an early washing step takes out 92.8 % of the P₂O₅, which is
what makes the rest of the separation tractable, and recovers it as a product
rather than a waste. Thorium is then taken out by solvent extraction with a
**secondary amine**, which removes Th and Fe at 100 % and 98 % efficiency
respectively while leaving uranium and the rare earths behind; the rare earths
are precipitated quantitatively as the oxalate and separated from the uranium.
Note that the thorium here leaves by extraction, not by hydroxide
precipitation.

(thorium-management)=
### Thorium Management
After leaching, thorium must be separated [@amaral2010thorium]:

#### Solvent Extraction Methods

**Amine extraction** (from sulfate medium) [@amaral2010thorium]:

Amines extract anionic metal complexes, so they work where the metal forms
one. Th(IV) and U(VI) both form anionic sulfato complexes — Th(SO₄)₃²⁻ and
Th(SO₄)₄⁴⁻, UO₂(SO₄)₂²⁻ — in the sulfuric liquor that comes off a monazite
digestion, while REE(III) does not to any comparable degree. That difference,
not a size effect, is what makes the separation work.

- @amaral2010thorium apply amine solvent extraction directly to monazite
  sulfuric acid liquor and report thorium and uranium extracted with the rare
  earths left in the raffinate.
- Amine class matters and is often misreported, so it is worth naming the
  classes rather than the trade names alone. Primary (Primene JM-T), secondary
  (Amberlite LA-2) and tertiary (Alamine 336, a tri-C₈/C₁₀-alkylamine, and
  *not* a primary amine however often it is called one) amines differ in
  basicity and in their affinity for the sulfato complexes. Any account of a
  Th/U circuit that does not say which class was used has not said enough to
  be reproduced.
- Strip with a salt or acid solution that breaks the anionic complex
  (Na₂CO₃ or dilute acid, depending on the amine).

**TBP extraction** (from nitrate medium). {index}`TBP` is a neutral solvating
extractant, so it works on the neutral nitrate complex rather than on an anion.
Th(NO₃)₄ is a tetravalent nitrate and is solvated far more strongly than the
trivalent RE(NO₃)₃, which is what gives the separation; the same chemistry, at
the same concentration in kerosene, is what the nuclear industry uses to separate
tetravalent actinides, and it is the reason a nitrate leach liquor is worth
having if thorium is the problem. No extractant concentration or separation
factor is quoted: both depend on the aqueous nitrate activity and on the rare
earth distribution of the particular liquor.

**Ion exchange.** On a strong-acid cation resin the retention order follows
charge density, so Th⁴⁺ is held more strongly than RE³⁺ and the rare earths can
be eluted with dilute acid while thorium requires a stronger acid or a
complexant such as {index}`EDTA`. This is the laboratory and small-scale answer;
resin inventory and elution volumes make it uncompetitive against solvent
extraction at plant throughput, which is why the two industrial descriptions
above both use amines.

### Industrial Practice
The Indian plants are the reference case for monazite, because India has both
the placer resource and a long operating history with it
[@jha2016hydrometallurgical; @iaea2011radiation]. The chain runs: beach sand
mining of monazite placers; gravity, magnetic and electrostatic separation to a
monazite concentrate; decomposition — historically the 200-220 °C concentrated
sulfuric acid digestion, now the caustic route described above; water leaching
and filtration to take out the phosphate; thorium removal, by amine extraction
from a sulfate liquor or by pH-controlled selective dissolution from a hydroxide
cake; and precipitation of the rare earths as hydroxide or carbonate for
redissolution and individual separation.

Two numbers from that circuit are worth carrying, because they say what a
monazite plant actually generates. The effluent treatment cake — the settled
solids from co-precipitating residual radionuclides, phosphate and fluoride with
lime and calcium chloride — amounts to about **10 % of the original monazite
mass**, and India generates roughly 250 t (300 m³) of it a year, bagged and
buried in earthen trenches with soil cover and periodic groundwater monitoring
[@iaea2011radiation]. Annual ²²⁸Ra discharge is reported as under 1 GBq. That is
what "thorium management" means in practice: not a unit operation, but a
permanent storage obligation and a monitoring programme.

(ion-adsorption-clay-leaching-the-gentle-approach)=
## Ion-Adsorption Clay Leaching: The Gentle Approach

The fourth ore type breaks the pattern of this chapter. Ion-adsorption deposits
carry no crystalline rare earth mineral at all: the REEs sit as exchangeable,
hydrated cations on weathered kaolinite and halloysite surfaces, so there is
nothing to defluorinate and no phosphate lattice to break. A dilute salt
solution displaces them at ambient temperature by mass action,

$$
\mathrm{Clay}\text{-}\mathrm{REE^{3+}} + 3\,\mathrm{NH_4^+} \rightleftharpoons
  \mathrm{Clay}\text{-}\mathrm{(NH_4)_3} + \mathrm{REE^{3+}(aq)}
$$

and that single fact is why deposits grading 0.05-0.3 % REO — two to three
orders of magnitude below a bastnäsite ore — are economic at all, and why they
supply over 90 % of the world's heavy rare earths [@zhou2020genesis].

The deposits themselves, the ion-exchange chemistry in detail, the
reagent-substitution literature and the environmental case are the subject of
[](#ion-adsorption-clays). What this chapter needs from them is narrower: the
shape of the leach, and the liquor it hands downstream.

### Lixiviants and Contacting

Ammonium sulfate is the traditional reagent [@shi2022column]:

$$
\mathrm{Clay}\text{-}\mathrm{REE^{3+}} + 1.5\,\mathrm{(NH_4)_2SO_4} \rightarrow
  \mathrm{Clay}\text{-}\mathrm{(NH_4)_3} + \mathrm{REE^{3+}} + 1.5\,\mathrm{SO_4^{2-}}
$$

The leach runs at ambient temperature — that is the whole point of it — and
@shi2022column operate ammonium sulfate at pH 2 and a liquid-to-solid ratio of
4:1. Reagent concentrations, contact times and pH windows vary with the deposit and
with the contacting mode, and no representative band is given.

Contacting is either **in situ** — lixiviant injected through wells drilled into
the orebody, pregnant leach solution collected downslope, and no ore mined at
all, which is now the dominant mode — or **heap leaching** of excavated ore on
an impermeable pad. Heap geometry, irrigation rate and residence time are
site-specific and no representative values are asserted.

What can be stated is the consequence of the grade, because it follows from
arithmetic rather than from practice. At an ore grade of 0.05-0.3 % REO and the
4:1 liquid-to-solid ratio of @shi2022column, complete extraction would give a
pregnant leach solution of only **125-750 mg/L REE**, and real recoveries put it
below that. Aluminium, iron and calcium are the impurities that matter at those
concentrations, because they are not two orders of magnitude dilute. That
dilution, not the chemistry, is the engineering problem this route creates, and
it propagates straight into the solution volumes tabulated later in the chapter.

Because the mechanism is cation exchange, ammonium sulfate needs a *high*
ammonium concentration to work, and the sulfate anion contributes essentially
nothing to the leach — it is along for the ride, and it is part of the effluent
problem. That is the argument @shi2022column make for changing the anion rather
than the concentration: column leaching with **ammonium citrate**, where both
the cation and the anion take part, recovered rare earths well at a
substantially lower ammonium concentration, at a liquid-to-solid ratio of 4:1
and pH 6 (against pH 2 for ammonium sulfate). The lever is the molecular
structure of the leaching agent, not the dose. The rate is set by diffusion
through the clay particle pores
rather than by the exchange itself, so the leach follows the
product-layer-diffusion form of the shrinking-core model set out in
[](#leaching-kinetics-models) [@long2019kinetics].

The ammonium is also the route's liability: the NH₄⁺ left on the clay after the
rare earths are gone leaches into groundwater [@xiao2015recovery]. The
alternatives are magnesium sulfate,

$$
\mathrm{Clay}\text{-}\mathrm{REE^{3+}} + 1.5\,\mathrm{MgSO_4} \rightarrow
  \mathrm{Clay}\text{-}\mathrm{Mg_{1.5}} + \mathrm{REE^{3+}} + 1.5\,\mathrm{SO_4^{2-}}
$$

which carries no nitrogen and is a somewhat weaker competitor for the exchange
sites, needing 1.5 mol of divalent Mg²⁺ per mole of REE³⁺ against 3 mol of NH₄⁺
[@xiao2015leaching; @pan2024insights]; ferrous sulfate, which adds a reducing
environment that helps mobilise cerium [@xiao2016reduction]; sodium chloride,
environmentally the mildest of all but a weaker competitor for the exchange
sites, so it needs higher concentrations for a given recovery; and organic acids
such as citric, which combine complexation with exchange at higher reagent cost
[@wang2017effects].
Suppressing aluminium co-dissolution — with hexamethylenetetramine, or by
staging the leach — is the other active line [@pan2024insights; @he2025stepwise].
[](#ion-adsorption-clays) weighs these reagents against one another and against
their environmental arithmetic.

### Recovery from the Dilute Liquor

Because the PLS is roughly two orders of magnitude more dilute than an acid
leach liquor, it has to be concentrated before anything downstream can use it
[@han2024efficient; @liu2017enrichment]. Two routes are used:

- **Precipitation.** Add oxalic acid, REE³⁺ + 1.5 H₂C₂O₄ → REE₂(C₂O₄)₃↓, or
  ammonium bicarbonate, REE³⁺ + 3 NH₄HCO₃ → REE(OH)CO₃↓ + 3 NH₄⁺, and calcine
  the precipitate to REE₂O₃.
- **Solvent extraction applied directly to the PLS.** This concentrates the
  liquor and produces a purified feed for the separation circuit — the same
  unit operation that will later do the separating. @han2024efficient do this
  on the sulfate leachate of an ion-adsorption ore with HPOAc, chosen over the
  conventional acidic organophosphorus reagents for this duty.

## Xenotime Processing
Xenotime is YPO₄, the heavy-rare-earth counterpart of monazite, and it is the
most refractory of the four minerals in this chapter [@hung2020separation]. The
reason is the same phosphate lattice, made tighter: yttrium and the heavy rare
earths are the smallest of the trivalent ions, so the charge density at the
cation site is highest and the RE–O–P framework is correspondingly harder to
break. It carries about 67 % REO and, unlike monazite, it is recovered largely as
a by-product — of heavy-mineral sand separation in Australia, and of tin mining
residues in southeast Asia [@iaea2011radiation]. Its radioactivity is elevated
but less so than monazite's: Australian xenotime runs about 60 Bq/g of ²³²Th and
about 50 Bq/g of ²³⁸U [@iaea2011radiation], against monazite's 140-250 Bq/g of
²³²Th. That difference is why xenotime is processed commercially in places where
monazite is not.

The two routes are the two monazite routes, and Malaysia has run both
[@iaea2011radiation]. In the sulfuric route the xenotime is milled and roasted
before digestion — the roast is there specifically to secure yttrium recovery in
the digestion that follows — the yttrium phosphate is converted to water-soluble
sulfate, water leaches it out, oxalic acid precipitates yttrium oxalate, and
calcination gives an yttrium oxide concentrate assaying **60 % yttrium**. In the
caustic route, finely ground xenotime is fused with sodium hydroxide at 400 °C —
a true fusion, not the 140-160 °C slurry digestion used for monazite, which is
the concrete sense in which xenotime demands more severe conditions — then water
extracts the trisodium phosphate and residual caustic, the hydroxide cake is
dissolved in hydrochloric acid, and oxalate precipitation and calcination give a
concentrate of **40-60 % yttrium**. The hydroxide residue is managed exactly as
the monazite residue is.

Note that the sulfuric route gives the higher-grade product here, which is the
reverse of the monazite case, and note also that neither figure is a recovery:
they are product grades. No digestion temperatures, acid
strengths, residence times or extraction efficiencies are given; none could be
traced to a primary measurement. Thorium and uranium follow the rare earths
through both routes and are separated by the same means described for monazite.

## Bioleaching: Emerging Green Technology

Microorganisms mobilise rare earths from minerals by three routes
[@rasoulnia2020critical; @brisson2015bioleaching]: **acidolysis**, in which
secreted organic acids — citric, oxalic, gluconic — dissolve the mineral;
**redoxolysis**, in which iron- and sulfur-oxidising bacteria generate Fe³⁺ and
sulfuric acid that attack the host matrix indirectly; and **complexolysis**, in
which metabolites bind the released REE³⁺ and hold it in solution. The organisms,
the ligands they secrete and the engineering of both are the subject of
[](#biological-and-biomimetic-separations). The question here is narrower:
whether any of this leaches an ore fast enough, or completely enough, to stand
in for acid.

Two organism classes recur in the ore literature. The phosphate-solubilising
fungi, chiefly *Aspergillus niger*, secrete a mixture of organic acids — acetic,
citric, gluconic, itaconic, oxalic and succinic were identified in the monazite
work — and use the mineral as a phosphate source, which is why they are the ones
that work on monazite [@brisson2015bioleaching; @wang2025rare]. The acidophilic
chemolithotrophs, chiefly *Acidithiobacillus ferrooxidans*, oxidise Fe²⁺ and S²⁻
and can drive the pH to 1-2, which suits sulfide-bearing ores [@wang2025rare].
*Gluconobacter oxydans*, a gluconic-acid producer, is the organism of choice for
secondary feedstocks — coal ash, e-waste — rather than for ores
[@jindra2018developing]. In every case the leach runs for weeks at ambient
temperature and needs a fermentable carbon source, glucose or a waste sugar
stream, which is a real operating cost and a real carbon burden.

The fungal attack on monazite is written schematically as

$$
\text{fungal organic acids} + \mathrm{REEPO_4} \rightarrow
  \text{REE-organic acid complexes} + \mathrm{H_3PO_4}
$$

with the caveat that the acids are a mixture and the stoichiometry is not fixed.

### Bioleaching Performance: What the Primary Literature Actually Reports

This is a place where secondary sources have inflated the numbers badly, so it
is worth being careful about what the underlying experiments measured.

**Monazite** [@brisson2015bioleaching]. Brisson and co-workers screened
*Aspergillus niger* ATCC 1015 and two new isolates, an *A. terreus* strain and
a *Paecilomyces* sp. They report **dissolved rare earth concentrations**, not
percentage extractions, and the concentrations are in the milligram-per-litre
range. Their headline comparison is that cell-free spent medium from the two
isolates leached rare earths to concentrations **1.7-3.8 times** those reached
by HCl solutions of the same pH — the point being that something in the
metabolite mixture beyond the identified organic acids is doing the work, since
laboratory-prepared mixtures of those acids performed worse than the spent
medium. They also found that the fungi preferentially solubilised the rare
earths over thorium, leaving Th in the residue, which is a genuinely attractive
feature. What they did not report, and what is sometimes attributed to them, is
a 65-92 % monazite extraction.

**Ion-adsorption ore** [@wang2025rare]. Wang and co-workers compared *A. niger*
and *Acidithiobacillus ferrooxidans* on ionic rare earth ore and characterised
the *mechanisms*: *A. niger* releases rare earths by secreting organic acids
that complex REE³⁺ (and it adsorbs Yb strongly onto the mycelium, a loss
mechanism), while *A. ferrooxidans* works through iron-sulfur oxidation. This is
a mechanistic study, not a recovery benchmark, and no extraction percentage
should be quoted from it.

The honest summary is that bioleaching of primary rare earth minerals has been
demonstrated to work in the sense that it dissolves measurably more rare earth
than an abiotic control at the same pH, on a timescale of weeks rather than
hours, and that quantitative recoveries competitive with acid leaching have not
been shown for monazite.

The balance, then, is this. Bioleaching needs no harsh chemicals and no heat,
it shows a genuine preference for the rare earths over thorium in monazite
[@brisson2015bioleaching], and it is the only route with a plausible claim on
feedstocks too low-grade or too contaminated to pay for an acid plant
[@rasoulnia2020critical; @joshi2025bioleaching]. Against that it is slow, it
recovers less, it needs fermenters and sterile handling that a leach tank does
not, and it has not left laboratory and pilot scale.

### Indigenous Microorganism Enhancement
Native microorganisms already living on an ore body are pre-adapted to it, and
Corbett and co-workers tested whether adding them to a known phosphate-
solubilising strain helps [@corbett2017incorporation]. On Western Australian
monazite, a *Penicillium* sp. released 12.3 mg/L total REE in 8 days on
sterilised ore, and 23.7 mg/L — roughly double — on non-sterile ore carrying its
native consortium. The abiotic control reached 0.65 mg/L. Similar behaviour was
seen with *Enterobacter aerogenes*, *Pantoea agglomerans* and *Pseudomonas
putida*, and the native consortium combined with a known solubiliser beat either
one alone.

Two things are worth taking from this. The biological effect over the abiotic
control is large — a factor of twenty — so the microorganisms are unambiguously
doing something. But the absolute numbers are tens of milligrams per litre after
eight days, which is one to two orders of magnitude below what an acid leach
delivers in hours, and it is the absolute number, not the ratio, that a
flowsheet has to live with.

## Leach Solution Purification
After leaching, the solution requires purification before solvent extraction [@jha2016hydrometallurgical].

### Common Impurities

Which impurities a liquor carries follows from the ore and the route, not from a
general table, and their concentrations vary over orders of magnitude between deposits, so no table
of "typical" values is given. What *is* general is the list and the reason each
entry matters. Iron comes from gangue oxides and
co-extracts with the rare earths, colouring the product. Aluminium comes from
clays and co-extracts. Calcium comes from calcite and dolomite and, in a sulfate
liquor, precipitates as gypsum wherever it is not wanted. Thorium comes from
monazite and xenotime and is radioactive. Phosphate comes from the phosphate
minerals themselves and will precipitate the rare earths back out of solution.
Fluoride comes from bastnäsite, corrodes, and does the same.

Of these, the four that industry finds most troublesome are aluminium, iron,
thorium and uranium, and the controlling insight from the review literature is
that how hard they are to remove depends on their concentration, their redox
ratio, and how pure the product has to be — not on the element alone
[@pak2020progress]. That single sentence organises everything below.
### Iron Removal
**pH adjustment method** (most common):

$$
\mathrm{Fe^{3+}} + 3\,\mathrm{H_2O} \rightleftharpoons \mathrm{Fe(OH)_3}\downarrow + 3\,\mathrm{H^+}
$$

The method works because ferric iron hydrolyses at a lower pH than the trivalent
rare earths do, so raising the pH with sodium or ammonium hydroxide precipitates
Fe(OH)₃ and leaves the rare earths in solution [@pak2020progress]. The window is real but narrow, and where it sits
depends on the liquor, so no pH, temperature or removal figure is given. What
controls the rare earth loss is the same thing in every case — how far the pH is
allowed to overshoot before the base is stopped — which is why this step is a
controlled titration and not a batch addition.

The redox state is the complication. **Ferrous** iron does not hydrolyse in the
same range, and it also does not usually co-extract with the rare earths in an
ion exchange or solvent extraction circuit [@pak2020progress] — so an Fe(II)
liquor can sometimes simply be left alone. If the iron has to go, it must first
be oxidised to Fe(III), by air or peroxide, and then hydrolysed. A liquor
carrying both oxidation states is the awkward case, and it is the reason the
review makes redox ratio one of its three controlling variables.

At Mountain Pass this step is done without a hydroxide reagent at all: the
leachate is contacted with soda ash and tailings slurry, which converts the iron
chloride to insoluble iron hydroxide and precipitates it into the tailings
[@iaea2011radiation]. The waste stream absorbs the impurity.
### Aluminum Removal
More challenging than Fe (Al(OH)₃ soluble at low and high pH):

Like ferric iron, most aluminium precipitates as the hydroxide before the rare
earths do [@pak2020progress], so hydroxide precipitation is the first answer. But
aluminium hydroxide is amphoteric — it redissolves as aluminate if the pH goes
too high — so the window has a ceiling as well as a floor, and it is narrower
than iron's. No pH values are quoted.

Where the window is too narrow to hold, the alternative is to change the
chemistry rather than the pH. @wang2020removal precipitate aluminium from an
ion-adsorption rare earth leach solution as its 8-hydroxyquinoline complex,
using 1.25 times the theoretical reagent requirement, ten minutes at 60 °C and a
final pH of 4.5: **94.4 % of the aluminium is removed for an 8.2 % rare earth
loss**, and the aluminium leaves as a large-crystal, fast-filtering solid with a
value of its own as an optoelectronic material. That is a real number for a real
liquor, and it also shows the honest cost of the step — eight per cent of the
rare earths go with it.

The third option is to do nothing at the purification stage and let the solvent
extraction circuit reject the aluminium, either by choosing an extractant that
discriminates against it or by extracting the rare earths preferentially and
leaving aluminium in the raffinate.

### Calcium Removal

Calcium is the one impurity that a sulfuric leach largely removes by itself.
Calcium sulfate is sparingly soluble, so

$$
\mathrm{Ca^{2+}} + \mathrm{SO_4^{2-}} \rightarrow \mathrm{CaSO_4}\downarrow \quad \text{(gypsum)}
$$

proceeds during the leach and the gypsum leaves with the residue — which is
convenient here and is a nuisance elsewhere, since the same reaction scales
pipework and coats unreacted mineral. In a chloride or nitrate liquor there is no
sulfate to do the work, and calcium is taken out as the carbonate instead:

$$
\mathrm{Ca^{2+}} + \mathrm{CO_3^{2-}} \rightarrow \mathrm{CaCO_3}\downarrow
$$

Calcium is a nuisance rather than a hazard: it does not co-extract strongly, so
the reason to remove it is scaling and crud in the extraction circuit rather than
product contamination. That is also why it tolerates the crudest available
method.

### Thorium Removal
Thorium admits both answers, and which one a plant uses depends on how clean the
product has to be. Because Th(IV) hydrolyses before the trivalent rare earths, a
controlled pH rise takes most of it out as Th(OH)₄ [@pak2020progress] — this is
the same chemistry that makes the caustic route's selective HCl dissolution work,
seen from the other side. It is cheap and it is adequate for a partial removal.

But taking thorium and uranium out to the *highest* degree requires a dedicated
solvent extraction or ion exchange step designed specifically for them, usually
by anion exchange of their anionic complexes [@pak2020progress]. That is the
circuit described in [](#thorium-management): an amine from a sulfate liquor
[@amaral2010thorium], or {index}`TBP` from a nitrate one, run *before* the rare
earth extraction so that the thorium never enters it.
### Phosphate Removal
**Gypsum co-precipitation** (H₂SO₄ leach):

Add CaCl₂ or lime:

$$
3\,\mathrm{Ca^{2+}} + 2\,\mathrm{PO_4^{3-}} \rightarrow \mathrm{Ca_3(PO_4)_2}\downarrow
$$

$$
\mathrm{Ca^{2+}} + \mathrm{SO_4^{2-}} + 2\,\mathrm{H_2O} \rightarrow
  \mathrm{CaSO_4}\cdot 2\mathrm{H_2O}\downarrow
$$

the gypsum occluding residual phosphate as it forms.

Where iron is present, phosphate will also leave as ferric phosphate during the
iron removal step, which is convenient when it happens and is not something to
rely on when it does not: the two impurities are then coupled, and a liquor
short of iron keeps its phosphate.
### Purified Solution Specification

There is no universal specification for a solvent extraction feed, so none is
tabulated here. It is set by the extractant, the number of stages, and the purity
the product must reach; @pak2020progress make exactly this point in reviewing the
impurity-removal literature — the required degree of removal is one of the three
variables that decides the method.

What can be said without numbers is the shape of the requirement, and it is
worth stating because it explains why this section exists at all. The feed must
be **clarified**, because entrained solids stabilise emulsions and a crudded
solvent is the most common way a rare earth extraction circuit fails. It must be
**consistent** in acidity, because the extraction equilibrium of an acidic
organophosphorus extractant is a function of pH and a cascade tuned at one
acidity will not hold at another. It must be low enough in the co-extracting
impurities — iron and aluminium above all — that they do not accumulate in the
organic phase over many cycles. And it must be low enough in thorium to satisfy
the regulator, which is a limit set by law rather than by chemistry, and
therefore varies by jurisdiction.

This solution is the feed for the solvent extraction circuit described in
[](#solvent-extraction-fundamentals).
## Complete Process Flowsheets

Everything above comes together in [](#fig-leaching-flowsheet), which puts the
routes on one grid rather than drawing each separately. Side by side they show
something none of them shows alone: the routes differ only in how the mineral is
*cracked*. From the leach onward they converge on the same kind of stream — a
clarified aqueous liquor of mixed rare earth salts — and that liquor is what
[](#solvent-extraction-fundamentals) takes as its input.

:::{figure} ../figures/05-flowsheet.svg
:name: fig-leaching-flowsheet
:width: 100%

Schematic flowsheet for the ore types this chapter treats, drawn on one grid:
bastnäsite by the Mountain Pass chloride route and by the Bayan Obo
concentrated-sulfuric route, monazite by sulfuric digestion and by caustic
digestion, and ion-adsorption clay by ion exchange. Colour marks the medium a
stream is in — black for solids, purple for a sulfate liquor, blue for a
chloride one — because the medium is what decides whether a route needs a
conversion step. Unit operations and their order only: this is not a mass
balance and it is not to scale. Steps whose numbers this chapter gives
inconsistently are drawn unlabelled. Drawn from
`tools/figures/fig_flowsheet.py`.
:::

The two bastnäsite lanes are the Mountain Pass chloride route
[@gupta2004extractive; @castor2006rare] and the Bayan Obo concentrated-sulfuric
route [@kim2025rare]. Two design decisions carry the first: the roast is
*oxidative*, so cerium leaves for free as an insoluble residue rather than as
fifteen more extraction stages, and the acid is HCl end to end, so the liquor
never has to be converted between media before it reaches the extractant. The
second route gives up the cerium separation and buys tolerance for a
lower-grade, more variable concentrate; it pays for that with a fluorine off-gas
that needs a serious scrubbing train, and with a precipitation-redissolution
cycle it cannot avoid.

The two monazite lanes are the Indian sulfuric route [@gupta2004extractive;
@jha2016hydrometallurgical] and the caustic alternative [@xu2012decomposition;
@shahreldin2018selective]. What distinguishes them from the bastnäsite routes is
structural, not numerical. Thorium is pulled out as a separate stream *before*
the rare earths are separated from one another, because a thorium-bearing
organic phase would contaminate every stage of the cascade downstream. And a
sulfate liquor is converted to chloride the only way it can be — precipitate the
rare earths as hydroxide, filter, redissolve the solid in HCl — rather than by
trying to drive the sulfuric acid out of solution. The caustic route arrives at
the same place in a different order, dropping the phosphate out first as a
soluble trisodium salt that can be sold.

That conversion node is why the figure colours streams by medium. Three of the
four mineral routes leach into sulfate, and every one of the three has to go
back through a solid before it can feed a chloride circuit. Only the Mountain
Pass route, which never leaves chloride, runs straight across the conversion
column, and that unbroken arrow is the strongest argument the flowsheet makes
for it.

The ion-adsorption lane [@chi2008weathered; @shi2022column] is drawn as a long
arrow across two empty columns, and the emptiness is the content: there is no
beneficiation and no decomposition step at all. Nothing is roasted and nothing
is digested; the whole route is an ion exchange followed by a concentration
step, and the solvent extraction that does the concentrating is the same
operation that will later do the separating. That is why these deposits are
economic at grades two to three orders of magnitude below a bastnäsite ore, and
also why the environmental problem they create is a solution-management problem
— ammonium in groundwater, slope stability — rather than an emissions problem.

Read the figure for its logic rather than for its numbers. Where this chapter
states a quantity in two incompatible ways — the ore grade feeding flotation,
the acid strength of the bastnäsite leach, the lixiviant strength for the clays,
and every leach residence time — the step is drawn without a number rather than
committed to one of the values.

## Process Optimization and Kinetics

The optimization in this section is parameter-by-parameter: temperature, acid
strength, particle size, each considered against the others held fixed. That is
how leaching is optimized in practice and how the underlying literature reports
it. Treating the leach as one block inside a flowsheet model, so that its
operating point is chosen against the cost of everything downstream of it, is a
different exercise; [](#process-modeling-and-optimization) describes it, and the
surrogate-modeling work it discusses exists precisely because a detailed leach
model is too expensive to embed in a flowsheet optimization directly.

### Key Operating Parameters

Five variables set an acid leach, and each is a trade rather than a maximisation.
No representative values are given for any of them: activation energies, particle
sizes, agitation speeds, acid molarities and roasting windows are precisely the
quantities a plant determines on its own ore. What generalises is the *shape* of
each trade.

**Temperature.** The rate follows Arrhenius, $k = A\exp(-E_\mathrm{a}/RT)$, so
heat buys rate cheaply in principle. What limits it is the vessel — a leach above
the atmospheric boiling point of the liquor needs a pressure vessel, and that is
a step change in capital, not an increment — and the energy bill. The activation
energy itself is diagnostic rather than something to look up: a value in the
range typical of chemical control tells you the surface reaction is limiting and
that temperature will help; a low value tells you the process is
diffusion-limited and that stirring or finer grinding will help more than heat
will. No "typical" value is given, because a typical value would defeat the
diagnosis.

**Acid concentration.** More protons means faster attack, up to the point where
the limiting step stops being the surface reaction. Past that, extra acid does
nothing for the leach and everything for the neutralisation bill and the
corrosion allowance — every mole of excess acid is a mole of base later, and a
mole of salt in the effluent. The optimum is mineral-specific, and the contrast
runs through this whole chapter: roasted bastnäsite yields to dilute acid because
the roast has already done the hard part, while unroasted monazite needs
concentrated sulfuric acid at 200 °C and above because nothing has.

**Particle size.** Finer particles leach faster, and grinding is one of the two
largest energy consumers in the plant, as the beneficiation section above set
out. It also
makes the residue harder to filter and wash, which shows up as lost rare earth in
the entrained liquor rather than as a grinding cost. Grinding to the point where
the leach is fast and the filter cake is unmanageable is a real and common
failure, and the optimum sits well short of "as fine as possible" — except in the
caustic monazite digestion, where the grind is set by a different constraint
entirely: coating of coarse grains by NaOH stops the reaction, which is why that
route specifies 90 % below about 50 µm [@iaea2011radiation].

**Solid-to-liquid ratio.** A thinner pulp mass-transfers better and leaches more
completely; it also means bigger tanks, more water to heat, and a more dilute
liquor for everything downstream to concentrate again. Since dilution is already
this chapter's recurring engineering complaint, the pull is toward the densest
pulp the agitator and the rheology will carry.

**Agitation.** Enough to keep the solids suspended and the boundary layer thin;
past that, more power buys attrition of the particles and, if organics are
present anywhere in the circuit, emulsions.

Roasting has its own three, and only the first is subtle. **Temperature** has an
optimum rather than a monotone benefit, because an underroast leaves the mineral
undecomposed and an overroast sinters the charge and closes the porosity the acid
needs — the same non-monotonicity noted for roasted bastnäsite above. Where that
optimum lies is a property of the concentrate. **Time** must be long enough for
the reaction front to cross the particle, which couples it to grind size and to
bed depth in the kiln. **Atmosphere** is the one that does chemistry rather than
kinetics: an oxidising roast is what converts Ce(III) to Ce(IV) at Mountain Pass
and hands the flowsheet its largest single separation for free
[@iaea2011radiation], so air, or oxygen-enriched air, is not a detail here but a
design decision.
(leaching-kinetics-models)=
### Leaching Kinetics Models
#### Shrinking Core Model

A dissolving mineral particle is modelled as a shrinking unreacted core inside a
growing shell of product and depleted solid, and the rate is set by whichever of
three steps in series is slowest: diffusion of reagent through the liquid film
around the particle, reaction at the core surface, or diffusion through the
product layer. Which one controls is not a detail — it decides what to change.
Film control responds to agitation; surface-reaction control responds to
temperature and acid concentration; product-layer control responds to particle
size and to almost nothing else, because the diffusion path is inside the
particle.

**Rate equations**:

**Surface reaction control**:

$$
1 - (1-X)^{1/3} = k_\mathrm{s}\, t
$$

**Product layer diffusion control**:

$$
1 - 3(1-X)^{2/3} + 2(1-X) = k_\mathrm{d}\, t
$$

Where:

- X = fraction leached
- $k_\mathrm{s}$, $k_\mathrm{d}$ = rate constants
- t = time

The diagnosis is empirical and cheap: plot the extraction data both ways and see
which form is linear in time. The activation energy from a temperature series is
the cross-check, since chemical control carries a substantially larger $E_a$ than
diffusion control does. No claim is made about which mechanism controls
"most" rare earth leaching: the answer depends on the mineral, the roast and the
grind.

The ion-adsorption clays need a different model altogether, and this is worth
noting because it is a case where the standard shrinking-core forms do not apply.
@long2019kinetics treat the clay leach as three steps — ammonium diffusing
through the boundary layer to the particle, reversible ion exchange at the
surface, and rare earth diffusing back out — with Fick's law for the diffusion
and the Kerr model for the exchange, and with the particle size held *constant*,
since nothing dissolves. The core does not shrink because there is no core: the
rare earths are surface-adsorbed, not lattice-bound.
### Process Intensification
**Ultrasound and microwaves.** Stojković and co-workers combined both on a
secondary feedstock — coal fly and bottom ash rather than an ore — using
ultrasonic alkaline roasting (95 °C, 10 min, 3 M NaOH) to break up the silica
matrix, followed by microwave-assisted acid leaching (174 °C, 30 min, 1:1
HCl/HNO₃). Against the NIST 1633c reference material the two-step procedure
recovered about 80 % of the rare earths, and they note explicitly that it is
*greener* than a high-temperature roast but recovers *less*
[@stojkovic2024recovery]. That trade — lower energy for lower recovery — is the
honest characterisation of most intensification work in this area, and it is not
the same as the "faster and better" claim these techniques usually attract.

**Mechanochemistry.** Grinding is treated in this chapter as a size-reduction
step ([](#crushing-and-grinding)), but mechanical energy can also drive a
chemical conversion that would otherwise need heat or a stronger reagent, and
the mechanism is usually the destruction of a passivating product layer rather
than any bulk activation. @liu2023mechanochemical give a clean example. Yttrium
fluoride does not convert to the hydroxide under alkaline conditions because a
Y(OH)₃ layer forms on the particle and stops the reaction; applying mechanical
force destroys that coating as it forms, and the conversion runs to 98.2 % at
room temperature. Applied to the YF₃-bearing slag from calciothermic reduction
smelting, the yttrium leaching rate reached 96.2 %. A second study shows the principle generalising to a different obstacle
[@zhang2023mechanochemical]. Oxidative roasting of NdFeB wire-cutting swarf is
necessary to convert the iron to Fe₂O₃ so that dilute acid attacks the rare earth
oxides preferentially — it drops iron leaching from 53.4 % to under 10 % — but
above 700 °C the roast forms NdFeO₃, a perovskite that 0.2 mol/L HCl cannot
dissolve, and rare earth recovery falls to about 40 %. Four hours of dry planetary
milling at 800 rpm, with no reagent added, takes the NdFeO₃ content from 21.0 wt %
to 3.50 wt %, and the leaching efficiencies rise to 96.1 % Nd, 89.7 % Pr, 93.2 %
Gd and 97.6 % Dy — roughly double, and in half an hour of leaching rather than
three. Here the milling drives no reaction of its own; it destroys a lattice that
resists acid, where in the yttrium case it destroyed a product layer that formed
during one. The feed is a real commercial waste, over half of it cutting-coolant
sludge as received, at 3 g per mill charge.

Two things follow. The first is that this is leaching and activation, not
separation — nothing in the mechanochemical rare earth literature reports a
separation factor between lanthanides, and it should not be read as an
alternative to a cascade. The second paper makes the point about as plainly as it
can be made: its four lanthanides leach at 89.7 to 97.6 %, which is a quantitative
co-dissolution and the exact opposite of a fractionation. What mechanochemistry
buys is acid consumption and leach time, and what neither paper reports is the
energy cost of four hours of milling, so the "green" claim rests on reagent
savings alone. The second is the usual intensification trade in a new
form: a mill that runs at room temperature has replaced a furnace, and the
energy has gone into the mill. Whether that is a net saving is a question for
[](#energy-and-carbon-where-the-burden-sits), and neither of these papers
answers it.

**High-pressure leaching.** An autoclave lifts the temperature ceiling above the
atmospheric boiling point of the liquor and the rate follows. The cost is the
vessel, and it is not incremental: a pressure vessel with the corrosion
resistance an acid rare earth leach needs is among the most expensive items in
the plant, and it brings its own maintenance and safety regime. Hence the
insistence above that the caustic monazite digestion runs at atmospheric
pressure — the cheapest way to win on kinetics is chemistry that does not need
the pressure at all.
## Environmental and Sustainability Considerations
### Waste Generation

Numbers in this area are frequently quoted without saying what they are per unit
*of*, and the resulting comparisons are meaningless. Before tabulating anything,
fix the basis.

Bastnäsite and monazite are beneficiated before they are leached, so the
material a leaching plant consumes is a **concentrate**, and the ore behind that
concentrate is a much larger and separate quantity. Ion-adsorption clay is not
beneficiated at all — there is no rare earth mineral to concentrate — so the
**ore is the leach feed**. A table that puts 1.5 t of bastnäsite in the same
column as 20 t of ion-adsorption material is comparing a concentrate against an
ore, and it is out by whatever the beneficiation ratio happens to be.

The arithmetic is elementary. Feed required per tonne of REO is

$$
\text{feed} = \frac{1}{\text{grade} \times \text{recovery}}
$$

with grade as the mass fraction REO in that feed and recovery the fraction of
contained REO that survives to product. The grades below are all plant figures
with a source. The recoveries are not: as the beneficiation section explained, no
traceable overall recovery figure could be found, so **every number here is
computed at 100 % recovery** and is therefore a *floor* — the true feed
requirement is larger by however much the plant loses, and the shortfall is left
explicit rather than filled with an invented efficiency.

**Leach feed, per tonne of REO, at perfect recovery:**

| Ore type       | Basis           | Grade (REO)  | Source              | Feed per t REO |
|----------------|-----------------|--------------|---------------------|----------------|
| Bastnäsite     | **concentrate** | 60-65 %      | Mountain Pass       | ≥1.5-1.7 t     |
| Monazite       | **concentrate** | 44-60 %      | Steenkampskraal, placer | ≥1.7-2.3 t |
| Ion-adsorption | **ore**         | 0.05-0.3 %   | grade range         | ≥330-2,000 t   |

Grades from @iaea2011radiation except the ion-adsorption range, which is the
deposit grade used throughout this chapter [@zhou2020genesis]. Worked, so the
reader can check it: a Mountain Pass bastnäsite concentrate at 60 % REO needs
1/0.60 = 1.67 t per tonne of REO and at 65 % needs 1.54 t. An ion-adsorption ore
at 0.3 % REO needs 1/0.003 = 333 t; at 0.05 % it needs 2,000 t. Three orders of
magnitude separate the two feeds, which is the single most important fact about
ion-adsorption mining and the reason its environmental footprint is a
land-and-groundwater problem rather than a reagent problem.

**Ore behind the concentrate.** Mountain Pass blended its crushed stockpiles to a
uniform flotation feed of 7-9 % REO [@iaea2011radiation], so at perfect recovery
the mined ore behind a tonne of REO is 1/0.09 = 11.1 t to 1/0.07 = 14.3 t —
**at least 11-14 t of ore** — against 1.5-1.7 t of concentrate, with the
difference reporting to the flotation tailings pond. Real flotation does not
recover everything, so the true figure is higher; no recovery is asserted. For
monazite the question is not well posed: beach placers are mined for ilmenite,
rutile and zircon, and monazite is recovered as a minor byproduct of a separation
that would happen anyway, so attributing a placer ore tonnage to the rare earths
is an allocation choice, not a measurement.
**Reagents.** Two of the three follow from stoichiometry:

- *Bastnäsite, sulfuric route.* REE₂O₃ + 3 H₂SO₄ gives 3 × 98 / 328 = 0.90 t of
  H₂SO₄ per tonne of REO as a floor. Real consumption is higher, by an amount
  set by the carbonate gangue, which is why the HCl pre-leach that removes
  calcite before the roast pays for itself.
- *Monazite, sulfuric route.* 2 REEPO₄ + 3 H₂SO₄ is the same 1.5 mol of acid per
  mole of rare earth, so the floor is the same **0.89 t of H₂SO₄ per tonne of
  REO** (6.06 kmol RE × 147.1 g). Actual plant consumption is much higher,
  because the digestion is run in a large excess — the charge must stay workable
  as it thickens to a paste, and the thorium and any carbonate gangue take their
  own share. How much higher is a plant variable, and no figure is asserted.
- *Monazite, caustic route.* This one is a plant figure rather than a floor:
  0.75 kg of NaOH per kilogram of monazite [@iaea2011radiation], which on
  1.7-2.3 t of concentrate is **1.3-1.7 t of NaOH per tonne of REO**, of which
  the ~50 % stoichiometric excess is recovered and reused.
- *Ion-adsorption.* Displacing REE³⁺ takes three equivalents of NH₄⁺, so
  1.5 mol of (NH₄)₂SO₄ per mol of REE. A tonne of REO is about 6.1 kmol of REE
  (Ln₂O₃ ≈ 330 g/mol), giving 9.2 kmol × 132 g/mol = **1.2 t of (NH₄)₂SO₄ as a
  stoichiometric minimum**, and practice uses a multiple of that because the
  exchange is an equilibrium against the clay's whole cation exchange capacity,
  not just its rare earth loading. Figures below 1.2 t are below the
  thermodynamic floor and cannot be right.

**Solution volumes.** No plant solid-to-liquid ratio could be sourced for the
acid routes, so no leach volume is given for them. Order of magnitude:
with only 1.5-2.3 t of concentrate to wet, the acid routes are *cubic metres* per
tonne of REO, not thousands of them.

For ion-adsorption ore the volume is set by the pregnant leach solution
concentration instead, and that follows from the grade. At the 4:1
liquid-to-solid ratio of @shi2022column and complete extraction, an ore of
0.05-0.3 % REO gives a PLS of 125-750 mg/L, so a tonne of REO arrives dissolved
in **1,300-8,000 m³** — three to four orders of magnitude more solution than an
acid leach for the same metal. Most of that volume is recirculated rather than
discharged, but it is all in contact with the ore body and all of it is a
containment problem.

**Solid residues.** At perfect recovery the acid routes leave 0.5-0.7 t
(bastnäsite) and 0.7-1.3 t (monazite) of leach residue per tonne of REO, simply
as the difference between concentrate in and REO dissolved, plus any gypsum
precipitated to fix phosphate. Bayan Obo's sulfuric route reports the same
quantity from the other direction: a slag-to-concentrate mass ratio of up to
0.66, containing 0.2 % Th and stored as radioactive residue
[@iaea2011radiation]. The monazite residue is likewise the regulated stream, and
the Indian effluent treatment cake — about 10 % of the monazite mass, roughly
250 t/a — is what that obligation looks like in practice [@iaea2011radiation].
The ion-adsorption case has no leach residue in the usual sense and is often
tabulated as "minimal", which is misleading: the solid left behind is the entire
330-2,000 t of ore, either in place after in-situ leaching or as a spent heap,
loaded with residual ammonium and structurally weakened by the leach.
### Major Environmental Concerns
The burdens follow the route, and each one has already been named where it
arises. Monazite leaves thorium-bearing residues and tailings that need licensed
disposal. Bastnäsite roasting evolves HF, and the sulfuric variant SO₂ as well,
both of which need a scrubbing train. Every acid route leaves spent liquor to
neutralise and a sulfate or chloride load to discharge. Ion-adsorption leaching
leaves residual NH₄⁺ in the orebody and disturbs a large area of land for a very
small quantity of metal.

Quantifying those impacts, comparing them across ore types and placing them in a
life-cycle framework is the business of
[](#environment-techno-economics-and-life-cycle); the ammonium-nitrogen problem
in particular, including what it has cost to remediate elsewhere, is treated in
[](#ion-adsorption-clays).

### Waste Minimization Strategies
Three levers belong to the leach itself. Spent acid can be regenerated — sulfate
roasting to recover H₂SO₄ is the established example — which cuts the fresh
reagent bill and the neutralisation load together. Several of the byproducts
have markets of their own: fluorine as HF or as AlF₃ for the aluminium industry,
phosphate as fertiliser, iron as pigment or steel feedstock, and thorium as
nuclear fuel if a use is ever found for it. And the lixiviant can be substituted
outright — magnesium salts for ammonium, biodegradable organic acids, or
{index}`ionic liquids` at research scale — which is the direction the
ion-adsorption industry has been pushed.

Process water recycling, heat integration and the wider circular-economy
arguments are not specific to leaching and are treated in
[](#environment-techno-economics-and-life-cycle).

(energy-and-carbon-where-the-burden-sits)=
### Energy and Carbon: Where the Burden Sits

Leaching itself is not the energy-intensive step. Qualitatively, and this much
is safe to say from [](#fig-leaching-flowsheet), the energy is concentrated in
the operations that move or heat large masses: comminution in beneficiation, and
the roast. Everything downstream of the roast happens at 25-95 °C in aqueous
solution, and the solvent extraction cascade — which has hundreds of stages —
consumes energy mostly as pumping and mixing, not as heat.

That ordering explains why the ion-adsorption route, which has neither
comminution nor a roast, is the least energy-intensive of the three per tonne of
REO despite handling a thousand times more solid, and why proposals to eliminate
the roast (direct leaching, bioleaching, chloride volatilisation) are pursued
even when they recover less.

Quantitative energy and CO₂ intensities per tonne of REO are not given here.
Published values disagree by large factors depending on system boundary, ore,
co-product allocation and grid, and a number carried without its boundary is
worse than no number.
[](#environment-techno-economics-and-life-cycle) treats life cycle assessment
properly, and is the place to look for figures.

## Emerging Technologies and Future Directions
### Green Leaching Methods

**Deep eutectic solvents.** A DES is a mixture of a hydrogen-bond acceptor —
typically a quaternary ammonium salt — and a hydrogen-bond donor, which together
melt far below either component. The attraction for hydrometallurgy is a liquid
with negligible vapour pressure, a composition that can be tuned rather than
selected from a catalogue, and, in principle, recyclability.

It is worth being precise about what has actually been shown, because the
literature is often read as more than it is. The demonstrated rare-earth-adjacent
application is **thorium**, not the rare earths: Ni and co-workers extract
thorium selectively from a radioactive waste leachate with a hydrophobic DES
[@ni2023sustainable]. That is the impurity problem monazite processing has, which
makes it directly relevant to this chapter — but it is not a rare earth
separation and should not be cited as one. Cost, viscosity, and the difficulty of
stripping the loaded phase are what keep DES out of production.
**Ionic liquids**: task-specific ionic liquids can in principle combine the
leach and the extraction in one liquid, at the price of cost and scale-up.
[](#biological-and-biomimetic-separations) covers them alongside deep eutectic
solvents as green solvent systems, and
[](#environment-techno-economics-and-life-cycle) weighs the environmental claim.

### Process Integration

Both candidates here delete a step rather than improve one. **Roasting and
leaching in one vessel** is the more ambitious and the less advanced: the roast
is the energy-intensive step and the leach the corrosive one, each with its own
equipment train, but the conditions the two want are close to incompatible and
the work remains at development stage. **Extraction directly from the leach
liquor** is nearer term and attacks the dilution problem that runs through this
chapter. @liu2017enrichment extract from a lean leach solution instead of
precipitating the rare earths and redissolving them, removing a precipitation, a
filtration and a redissolution. It costs extractant — a dilute feed means more
organic phase circulating per tonne of metal — so the trade is favourable exactly
when the liquor is lean, which is why the ion-adsorption route is where it has
been pursued.

### Selective Leaching

If the leach itself could reject the impurities, the purification section above
would largely disappear. @he2025stepwise pursue this by staging the leach, so
that impurities and rare earths come off in different fractions — the
pH-controlled selective dissolution of the caustic monazite cake, generalised.
The difficulty is that leaching selectivity is blunt compared with extraction
selectivity, and a partial separation that still needs a purification circuit has
bought little. **Electrochemically assisted leaching** applies a potential during
the leach to drive a redox change at the mineral surface — the lever the Mountain
Pass oxidative roast uses on cerium, applied *in situ*. It is at research stage,
and no performance data are quoted.
### Artificial Intelligence and Process Control

The argument for machine learning on a leach is that ore is variable and the
optimum moves with it. The argument against is data: a leach is slow, its assays
are offline, and a plant generates few well-labelled operating points a year,
which is the opposite of the regime these methods want. Nothing in this book
demonstrates machine learning controlling a leach; what has been demonstrated is
adjacent — extractant design and separation modelling
([](#machine-learning-in-rare-earth-separations)) and closed-loop control of the
solvent extraction cascade ([](#process-modeling-and-optimization)). In-line
sensing for rare earths, pH and impurities is the precondition for any of it
reaching the leach, and it is the genuinely hard part: there is no cheap online
assay for a mixed rare earth liquor.
### Urban Mining
Magnet scrap, spent phosphors, catalysts, polishing powders and
{index}`coal fly ash <coal fly ash>` are leached with much the same acids and
much the same equipment as an ore, often at a higher rare earth grade and always
without a mine. What differs is upstream of the leach — collection, sorting, and
the variability of the feed — and that is where the difficulty actually lies.
[](#recycling-and-urban-mining) treats these feedstocks, the routes that have
been demonstrated on them, and why the end-of-life recycling rate is
nevertheless still under one percent.

## Comparison of Leaching Methods
### Summary Table

The table below carries no recovery column. Recoveries for these routes could not
be traced to sources that actually measure them, and a column of plausible
percentages is exactly the kind of thing this book exists to avoid; what is
tabulated instead is the operating point a named plant actually runs, with its
source.

| Ore type | What must be broken | Industrial cracking step | Governing burden |
|----|----|----|----|
| Bastnäsite (Mountain Pass) | Fluorocarbonate | HCl pre-leach; calcine 600-800 °C; leach in 30 % HCl [@iaea2011radiation] | Fluorine; cerium disposition |
| Bastnäsite-monazite (Bayan Obo) | Fluorocarbonate + phosphate | Conc. H₂SO₄ in a kiln, to 600 °C; water leach [@iaea2011radiation] | HF off-gas; slag at 0.66 t/t concentrate, 0.2 % Th [@iaea2011radiation] |
| Monazite (classical) | Phosphate | 98 % H₂SO₄ at 200-220 °C [@iaea2011radiation] | Thorium follows the product; phosphate is a waste |
| Monazite (current) | Phosphate | 60-70 % NaOH at 140-160 °C, 3-9 h, 0.75 kg NaOH/kg [@iaea2011radiation] | Caustic consumption; Th cake |
| Xenotime | Phosphate (tighter) | Roast then H₂SO₄, or NaOH fusion at 400 °C [@iaea2011radiation] | Most refractory of the four |
| Ion-adsorption clay | Nothing — ion exchange | Ammonium or magnesium salt at ambient [@shi2022column] | Ammonium in groundwater; land area |
| Bioleaching (any) | Varies | Microbial organic acids, ambient, weeks | Milligram-per-litre liquors [@brisson2015bioleaching] |

### On Cost Comparisons

Operating costs per tonne of REO are not tabulated here. They are dominated by
site-specific quantities — ore grade, labour rate, energy price, reagent
logistics, the disposal regime for thorium, and above all the value of the
particular basket of rare earths a given ore yields — and a cost table that
omits those is not a comparison of processes but a comparison of assumptions.
What can be said structurally, from the reagent arithmetic above, is that the
sulfuric monazite route pays in acid — at least 0.89 t per tonne of REO by
stoichiometry and considerably more in practice — plus a regulated radioactive
residue; that the caustic monazite route substitutes 1.3-1.7 t of NaOH per tonne
of REO for that acid and gets a saleable phosphate by-product in return; that the
bastnäsite chloride route spends its money on the roast; and that the
ion-adsorption route spends almost nothing on reagents or energy and almost
everything on land, water and remediation. Techno-economics is treated in
[](#environment-techno-economics-and-life-cycle).

## Conclusions and Recommendations
### Key Findings
**The mineral dictates the route, and it does so through one bond.** Bastnäsite
is a fluorocarbonate, so the fluorine has to be dealt with before any acid
arrives — volatilised as HF and scrubbed, fixed as NaF by a soda-ash roast, or
deactivated as NH₄F by an ammonium chloride roast. Monazite and xenotime are
phosphates, so the RE–PO₄ bond has to be broken by concentrated sulfuric acid at
200 °C and above or by concentrated caustic, and the thorium that rides in the
same lattice has to go somewhere. Ion-adsorption clay is not a mineral problem at
all: the rare earths are surface-adsorbed cations and a dilute salt solution
displaces them at ambient temperature. Everything else in this chapter follows
from those three facts.

**The chemistry sets the economics, and stoichiometry sets the floor.** Reagent
consumption cannot be argued below what the reaction requires — 0.89 t of H₂SO₄
per tonne of REO on either acid route, 1.2 t of ammonium sulfate on the
ion-adsorption route — and real consumption sits above it by an amount the gangue
determines. The roast, where there is one, is the energy-intensive step, which is
why every proposal to eliminate it survives even when it recovers less. And waste
treatment is not a line item at the end: for the monazite routes it is the
thorium obligation that decides whether the plant can be licensed at all, and for
ion-adsorption ore it is most of the cost.

**The industry's open problems are environmental, and they are specific.**
Fluorine capture from bastnäsite, ammonium-free lixiviants for ion-adsorption
clay, and something to do with thorium other than store it. Bioleaching is the
most-discussed green alternative and, on the evidence assembled here, the least
ready: it dissolves measurably more than an abiotic control, on a timescale of
weeks, into milligram-per-litre liquors.

**Practice is mature and moving slowly.** The flowsheets for all four ore types
are established and most of them are decades old; the caustic displacement of the
sulfuric monazite route is the last change of that magnitude. Deep eutectic
solvents, ionic liquids and supercritical CO₂ are all at laboratory scale, and
none of them removes the step that costs the most.
(research-gaps)=
### Research Gaps
Four gaps are worth naming, and each of them is a gap in the same sense: a place
where the current answer is known to be poor and no better one has been
demonstrated at scale.

**Leach selectivity.** Every flowsheet in this chapter dissolves the rare earths
along with iron, aluminium, calcium, thorium and phosphate, and then spends a
purification circuit undoing that. A leach that discriminated at the dissolution
step would remove the purification section, cut the acid, and shrink the waste
together. Staged leaching is the current best attempt [@he2025stepwise].

**Refractory decomposition.** Xenotime needs a caustic fusion at 400 °C or a
roast-plus-digestion, and monazite needs concentrated acid at 200 °C or
concentrated caustic. A lower-energy way to break a rare earth phosphate would
change both, and nothing in the current literature offers one.

**Bioleaching at scale.** The kinetics are the barrier, not the chemistry:
strain engineering, process intensification, and — conspicuously absent from the
literature — an economic analysis at industrial scale that takes the fermentable
carbon feed and the vessel residence time seriously.

**Closing the loop.** Reagent regeneration, water reuse, and a genuinely
zero-discharge circuit. Sulfate roasting to recover H₂SO₄ and the ~50 % caustic
recycle of the monazite digestion [@iaea2011radiation] show the principle works;
neither is close to closing a whole plant.
## The Feed Handed to Solvent Extraction

What leaves this chapter is a clarified aqueous solution of mixed rare earth
salts, low in iron, aluminium and thorium, at a controlled acidity. The
concentration, free acidity and impurity ceilings are not specified: as the
purification section above explains, no single specification exists, and no
sourced general values could be traced.

What *is* fixed, and what matters most for the chapter that follows, is the
**medium**. It is not a free choice made at the extraction circuit; it was
decided at the leach, several unit operations earlier, and changing it later
costs a precipitation and a redissolution.

- A **chloride** medium suits the acidic organophosphorus extractants, D2EHPA
  and PC88A. Mountain Pass leaches in HCl for exactly this reason and never
  leaves chloride [@iaea2011radiation].
- A **nitrate** medium suits {index}`TBP`, which extracts the neutral nitrate
  complex and takes thorium preferentially. Nitric acid appears in monazite
  processing as a variant of the caustic route, chosen when the separation
  circuit wants nitrate [@iaea2011radiation].
- A **sulfate** medium is what the Bayan Obo route and the ion-adsorption clays
  deliver, and it usually has to be converted — precipitate as hydroxide,
  carbonate or oxalate, redissolve in HCl — before an organophosphorus circuit
  can use it.

That coupling is the main reason the leach and the extraction cascade have to be
designed together, and it is why the flowsheet figure above colours streams by
medium. [](#solvent-extraction-fundamentals) takes the story from there.
A thermodynamic treatment of this same handoff — dissolution and extraction
written in one set of chemical potentials, so that a leaching condition and an
extraction constant can be computed on the same footing — appears in
[](#linking-dissolution-and-extraction-thermodynamically).

## Further Reading

Essential reviews:

- [@jha2016hydrometallurgical] — comprehensive hydrometallurgy review
- [@kim2025rare] — recent bastnäsite processing review
- [@xie2014critical] — solvent extraction, including a leaching overview
- [@rasoulnia2020critical] — bioleaching critical review

By ore type. **Bastnäsite**: [@chi2004recovery] (NH₄Cl roasting),
[@xu2012decomposition] (alkali decomposition), [@sinclair2017rare]
(supercritical CO₂). **Monazite**: [@borai2016modified] (modified acid leaching for thorium
separation), [@amaral2010thorium] (thorium extraction), [@brisson2015bioleaching]
(bioleaching). **Ion-adsorption clays**: [@xiao2015leaching] (ammonia-free
MgSO₄ leaching), [@shi2022column] (ammonium citrate as a low-ammonium lixiviant),
[@long2019kinetics] (kinetics modeling), [@han2024efficient] (recent sulfate
leaching advances).

Industrial practice: [@gupta2004extractive] is the standard textbook.
