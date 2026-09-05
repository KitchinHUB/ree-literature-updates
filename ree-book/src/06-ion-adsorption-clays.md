---
title: Ion-Adsorption Clays
---

(ion-adsorption-clays)=
# Ion-Adsorption Clays

Every other ore in this book is a mineralogical problem. Bastnäsite has to be
defluorinated, monazite and xenotime have a phosphate lattice that must be
broken with concentrated acid or concentrated caustic, and all three arrive at the
leach as a beneficiated concentrate. {index}`Ion-adsorption clays <ion-adsorption clay>`
have none of that. They contain no crystalline rare earth mineral at all. The
rare earths sit on the surfaces of weathered clay as hydrated cations, held there
by nothing stronger than electrostatics, and a salt solution at room temperature
takes them off. There is no beneficiation step, no cracking step, and no
radiological programme: the ore goes straight to chemical treatment without any
beneficiation, and its thorium and uranium oxide contents are about 0.005 %, which
puts the activity concentration below 1 Bq/g and, in the IAEA's assessment, below
the level at which regulatory control is warranted [@iaea2011radiation]. This is the easiest rare earth ore in the world to process,
and it supplies more than 90 % of the world's heavy rare earth production
[@zhou2020genesis].

The price of that easy chemistry is grade. The rare earth content is a few tenths
of a percent REO and does not exceed 1 % [@iaea2011radiation] — two to three
orders of magnitude below a bastnäsite concentrate — so the tonnage of rock, the
volume of solution and the area of hillside per tonne of product are all enormous.
That single trade defines the deposit type. Everything difficult about
ion-adsorption clay follows from it, and almost none of the difficulty is
chemical: it is a matter of moving lixiviant through a low-permeability regolith,
of keeping the solution inside the orebody, of what the leaving reagent does to
the groundwater, and of what happens to the land afterwards. The chemistry is
solved. The engineering and the environmental accounting are not.

The deposit and its {index}`ion-exchange <ion exchange>` chemistry are this
chapter's subject. The leach considered as a unit operation — lixiviant
chemistry, liquid-to-solid ratios, kinetics, and the reagent and solution-volume
arithmetic — belongs to [](#ion-adsorption-clay-leaching-the-gentle-approach) and
is not repeated here.

## The Deposit and the Adsorbed State

### What the rare earths are attached to

The rare earths in these ores are adsorbed on clay minerals — chiefly kaolinite
and halloysite, with contributions from illite, smectite and Fe-oxyhydroxides —
and the adsorption is genuinely surface adsorption, not a substitution into a
lattice. That was demonstrated directly by synchrotron X-ray absorption
spectroscopy on economic Chinese ore from the Zhaibei granite and on prospective
Malagasy regolith: the rare earths occur as **eight- to nine-coordinated, hydrated,
outer-sphere complexes** sitting on the basal surfaces of kaolinite, with their
hydration shells intact, rather than as inner-sphere or interlayer complexes
[@borst2020adsorption]. The same study leached its samples with ammonium sulfate
and re-measured them, and the collapse in Y absorption intensity after leaching
confirms that what the spectroscopy had characterised was the leachable fraction
itself — the economically relevant one. What survives the leach shows spectral
features typical of high-symmetry sites, consistent with the residual rare earths
being structurally bound rather than adsorbed.

The clay surface carries a net negative charge, from isomorphic substitution in
the lattice and from pH-dependent broken-edge silanol and aluminol sites, and
recovery is therefore cation exchange driven by mass action. A more concentrated
electrolyte cation displaces the loosely held REE³⁺:

$$
2\,\mathrm{Clay}\text{-}\mathrm{REE} + 3\,\mathrm{M_2SO_4} \rightleftharpoons
  2\,\mathrm{Clay}\text{-}\mathrm{M_3} + \mathrm{REE_2(SO_4)_3}
  \qquad (\mathrm{M} = \mathrm{NH_4^+},\ \tfrac{1}{2}\mathrm{Mg^{2+}},\ \ldots)
$$

Because the bond is electrostatic and the ion is already hydrated, the exchange
needs no acid attack on the mineral and no elevated temperature. Moldoveanu and
Papangelakis put a standardised leaching procedure across ores of several
different origins and found that, regardless of variation in origin and rare earth
content, all the rare earths reached peak extraction under ambient conditions with
fast kinetics [@moldoveanu2016overview]. That result is the whole economic basis
of the deposit type, and the reason a 0.1 % ore competes with a 60 % concentrate.

A second consequence is less often stated and matters more downstream than the
first. Because the exchange is selective for the trivalent cations over the
matrix, the pregnant solution is *clean*. The IAEA's assessment is blunt about it:
leaching is quite selective, very few impurities are present in the solution, and
the rare earth concentrate precipitated from it contains a minimum of 90 % REO and
typically 95 % [@iaea2011radiation]. An ion-adsorption operation therefore reaches
a concentrate purity, in one ambient-temperature contacting step, that the
hard-rock routes reach only after flotation, cracking, leaching and a purification
circuit. Aluminium and iron are the impurities that intrude on that picture, and
they intrude because the liquor is so dilute that they are not two orders of
magnitude behind the rare earths the way they would be in an acid leach.

### Two mechanisms, one of which fractionates

Rare earths attach to clay by two distinct mechanisms, and the distinction has
opposite consequences for a separation engineer [@wu2023rare]. **Ion exchange**,
which is the outer-sphere mechanism and does most of the loading, cannot cause
evident fractionation: it grabs the rare earth block as a block, without
discriminating among adjacent lanthanides. **Surface complexation**, the
inner-sphere mechanism at edge and defect sites, *does* fractionate, and it
enriches the heavies over the lights.

The practical reading is that the abundant mechanism is the useless one and the
selective mechanism is the minor one. That is why the leach recovers essentially
the whole rare earth suite in one pass and hands the separation problem
untouched to solvent extraction, and it is also why any proposal to use clay
itself as a separating medium has to find a way to make the minor mechanism
dominate. Borst and co-workers see the same split in their spectra from the other
side: the outer-sphere complexes are the ones that leach, and the inner-sphere or
interlayer ones are the ones that stay behind [@borst2020adsorption]. The
fractionating sites and the leachable sites are largely different sites.

## How the Deposit Forms, and Where

### Weathering, migration, and vertical zonation

Ion-adsorption deposits form by deep chemical weathering of rare-earth-bearing
parent rock in warm, humid, subtropical climates. The favourable protoliths are
felsic — granites, syenites and volcanic rocks — with the rare earths held in
weathering-susceptible minerals: synchysite, gadolinite and hingganite for the
heavies, allanite, titanite and apatite for the lights. Scandium deposits of the
same regolith-hosted type form instead on clinopyroxene-rich mafic-ultramafic
protoliths. Weathering decomposes those minerals, the liberated cations migrate
downward with groundwater, and they re-adsorb onto the clays formed in the same
process [@zhou2020genesis].

The ore is vertically zoned, and the reason is mineralogical rather than
hydrological. Weathering converts poorly crystalline, nano-sized halloysite and
kaolinite into much more crystalline, larger vermicular kaolinite, and the
adsorption capacity of the clay drops sharply across that transformation
[@zhou2020genesis]. Halloysite-abundant assemblages in the deeper regolith have
significantly higher specific surface area and porosity than the
kaolinite-dominant assemblages above them [@li2020role]. The consequence is that
adsorption is favoured in the deep regolith while desorption dominates in the
shallow soils — the orebody concentrates itself downward, and the mineable horizon
sits under a barren cap. The IAEA describes the resulting bodies as loose layers
3-10 m thick of completely weathered granitic rock [@iaea2011radiation].

The same slow process leaves a compositional signature that is commercially
decisive. Cerium is characteristically low — 0.3-5.5 % of the rare earth content —
while yttrium is generally high [@iaea2011radiation]. Cerium is the cheap,
abundant lanthanide that hard-rock producers cannot avoid co-producing; the clays
have already discarded most of it, in place, over geologic time, and deliver a
suite weighted toward the elements that are actually scarce.

### Geography, and whether the ore can be bought

The commercially attractive deposits are in the south-eastern Chinese provinces —
the IAEA names Jiangxi, Guangdong and Fujian [@iaea2011radiation], and Hunan and
Guangxi host them as well. Myanmar's Kachin State is the other major source, and
the conventional account of it — that China's 2012 shift toward value-added
processing pushed primary extraction across the border — turns out to be only half
right. A Landsat study of two mines on either side of the Myanmar-China border
found mining footprints growing on *both* sides between 2005 and 2020, by 130 % on
the Chinese side and 327 % on the Myanmar side, taking the combined footprint in
the study area from 1.22 km² to 3.78 km², with a continuous decline in vegetated
cover [@chinkaka2023unexpected]. National-level generalisations about where this
ore comes from do not survive contact with the imagery. Outside that core,
Madagascar's Ambohimirahavavy regolith is a genuine structural analogue at the
atomic level rather than a loose one [@borst2020adsorption], and Brazil, Malaysia,
Laos, Vietnam and Tanzania host prospects.

Whether any of this can be bought is a question with a short answer: essentially
no. The ore is low grade, it is processed near the source because moving hundreds
of tonnes of rock per tonne of product is absurd, and Chinese output is governed by
quotas allocated to two state-consolidated groups ([](#the-industrial-landscape)).
What trades openly is the downstream separated oxide, not the clay. A recurring
point of confusion deserves flagging: kaolinite and halloysite are cheap,
widely traded industrial clays, but the commercial product is *purified* clay,
sold specifically without adsorbed cations. Buying a tonne of kaolin gets you the
substrate and none of the value.

## Mining It: In Situ or on a Heap

The clays were originally mined by excavation — open pits worked with power
shovels, the ore going straight to leaching without beneficiation
[@iaea2011radiation] — and leached in heaps or tanks. The dominant modern method
is **in-situ leaching**: lixiviant is injected through shallow wells drilled into
the orebody and the pregnant solution is collected downslope, with no ore mined at
all. The change removed the excavation, the haulage and the visible pit, and it
introduced three problems that are the substance of the modern engineering
literature.

### Permeability decides the outcome

The first is that in-situ leaching is a flow problem in a material that fights
flow, and it gets worse as the leach proceeds. Constant-head permeability tests
on undisturbed ore during simulated in-situ leaching, with the three-dimensional
pore structure imaged by X-ray computed tomography before, during and after,
show permeability falling in three distinct stages — rapid reduction, then less
rapid, then little further change. Of seven pore-structure parameters measured,
the permeability tracked the average coordination number most closely, and pore
throats larger than about 30 µm were the effective seepage channels. The cause of
the decline is mechanical rather than chemical: clay particles migrate and new
clay forms during the leach, and both clog the pore throats, with the newly formed
clays then swelling. The hydraulic head of the injected solution influenced the
degradation more strongly than its concentration did [@zhang2024variations].

That result explains a great deal. It is why in-situ recovery is uneven, why
lixiviant finds preferential paths and leaves ore untouched, and why raising the
injection pressure to push more solution through is self-defeating — it accelerates
the clogging that caused the problem. It also means the permeability at the end
of a leach is not the permeability at the start, so a containment design validated
on virgin ore is validating the wrong material.

### The slope

The second is mechanical stability. In-situ leaching saturates a weathered
regolith on a hillside and chemically alters it while it is saturated, and the
strength parameters of the weathered ore layer fall as a result. A finite-element
seepage-and-stability analysis of an in-situ leaching operation found that the
slope safety factor stayed above the required 1.1 throughout leaching and the
subsequent push-water stage — so the studied slope remained stable overall — but
that the factor fell before it recovered, and that substantial deformation
concentrated in the topsoil and the fully weathered granite zone and at the
interfaces between layers. The authors' conclusion is that the risk window is the
middle and late stages of leaching, which is where prevention measures should be
targeted [@yuan2025analysis]. This is a single modelled case and not a general
result; what it establishes is that slope stability under in-situ leaching is a
time-dependent quantity, not a site property fixed at the design stage.

### What a heap buys back

The third problem is containment, and it is the one that has no engineering fix
in the in-situ mode: solution is injected into an unlined hillside aquifer, and
what does not report to the collection point reports to the groundwater. Heap
leaching gives that back. An excavated heap sits on an impermeable pad, so the
solution inventory is bounded and recoverable, the permeability is set by how the
heap was built rather than by what the leach does to undisturbed regolith, and
there is a defined solid residue at the end instead of a contaminated landscape.

The counter-argument has always been that the excavation is exactly the landscape
destruction the industry moved to in-situ leaching to avoid, and that heaps cost
more. A semi-industrial trial at 200 t of ore is the most substantial recent test
of the alternative. Using biosynthetic sodium citrate as the lixiviant at
50 mmol/L and a solid-to-liquid ratio of 1:2, heap leaching reached 98 % rare
earth extraction; oxalic acid then precipitated the rare earths from the leachate
at 94.5 % yield while carrying only 7.4 % of the aluminium, and — the point of the
design — the residual solution was regenerated and cycled back as fresh lixiviant.
Roasting the precipitate gave a concentrate of 96 % REO [@meng2023heap]. That is
a closed reagent loop demonstrated at a scale well past the bench, and it is the
strongest available argument that the containment advantage of a heap need not be
paid for in reagent cost.

## The Ammonium Problem

### Why ammonium, and what it leaves behind

Ammonium sulfate became the industry's lixiviant because NH₄⁺ is a cheap,
monovalent cation that competes well for clay exchange sites, and because
displacing one REE³⁺ takes three of them, so the reagent is consumed in quantity
and its cost per tonne of ore matters. The reagent arithmetic and the
alternatives — magnesium sulfate, ammonium citrate, ferrous sulfate, sodium
chloride, organic acids, and the aluminium-suppression additives — are set out in
[](#ion-adsorption-clay-leaching-the-gentle-approach).

What concerns this chapter is what happens to the ammonium afterwards, and the
answer is that it stays. The exchange that liberates the rare earths necessarily
loads the clay with NH₄⁺ in their place, and that ammonium is held by the same
weak electrostatic mechanism that held the rare earths — which is to say, it comes
off again with the next rainfall. In in-situ mining the loaded clay is left in
the ground, in an unlined aquifer, in a wet subtropical climate. The mechanism
that makes the deposit cheap to mine is the mechanism that makes it impossible to
decontaminate.

### Choosing the salt on thermodynamic grounds

There is a second, less obvious cost to ammonium, and it shows up in a purely
thermodynamic screening study. @mohamadsobri2025enhancing computed Eh-pH
(Pourbaix) stability fields for La, Nd and Y in three sulfate lixiviants using HSC
Chemistry 10.0, across 0.05-0.6 M and 25-80 °C, asking a narrow question: which
conditions keep the liberated rare earth in solution as REE³⁺ rather than
complexed or precipitated? The answer separates the three reagents cleanly.

| Lixiviant | Behaviour across 0.05-0.6 M at 25 °C | Verdict |
|----|----|----|
| (NH₄)₂SO₄ | La³⁺ maximally stable only to 0.25 M; at 0.3 M and above, nitrate from nitrification of the ammonium forms LaNO₃²⁺. Nd³⁺ maximally stable only at 0.05 M, forming NdNO₃²⁺ from 0.1 M upward. Y³⁺ stable across the whole range | Degrades with dose |
| MgSO₄ | La³⁺, Nd³⁺ and Y³⁺ maximally stable at every concentration tested, with no unwanted species formed | Best |
| Al₂(SO₄)₃ | Sulfate complexes La³⁺ to LaSO₄⁺ and precipitates Nd as Nd₂(SO₄)₃·8H₂O, both regions expanding with concentration. Y³⁺ unaffected | Degrades with dose |

The ammonium result is the interesting one, because the species that spoils it is
not ammonium at all. It is nitrate — produced by nitrifying bacteria oxidising the
NH₄⁺ that the leach put into the ground — and it complexes the light rare earths
out of the ionic form the process needs. The nitrogen pollution and a loss of
process yield are the same phenomenon seen from two directions. Note also that the
threshold is element-dependent and much lower for neodymium than for lanthanum,
which is not what a single "safe concentration" rule of thumb would suggest.

The stability windows are acidic and element-specific — La from pH 0 to 5.8, Nd
from 0 to 5, Y from 0 to 4.2, in all three lixiviants — and stability falls as
temperature rises from 25 to 80 °C, so ambient leaching is thermodynamically
optimal as well as cheap [@mohamadsobri2025enhancing]. The screening's credibility
rests on agreeing with experiments it did not perform, and the study its authors
take as the confirmation is Chen and co-workers, who leached a low-grade
weathered-crust ore with MgSO₄ to 75.48 % extraction in a single stage and up to
96.19 % after a second stage — slightly better than ammonium sulfate achieved on
the same ore — with cerium the worst-leaching element [@chen2018leaching].

The limitation of the screening should be stated as plainly as the result. It
treats one element and one solvent at a time, with no impurities and no kinetics.
It cannot tell you what aluminium does, and aluminium is the impurity that
actually decides the downstream burden. It is a tool for narrowing a reagent list
before an experiment, not a substitute for one.

### Nitrogen in the watershed

The pollution is real and measurable at catchment scale. A coupled SWAT-WASP
hydrological and water-quality model of the upper Dongjiang River Basin,
calibrated and validated against 2016-2018 monthly monitoring, simulated ammonia
nitrogen concentrations above 1.8 mg/L near mining zones against below 0.5 mg/L in
upstream natural areas [@wu2026swat]. Ammonia nitrogen is described there as the
dominant water pollutant of ionic rare earth mining basins, and the spatial
signature is unambiguous even though the model attributes the largest single share
of the variance to population density combined with industrial and agricultural
activity rather than to mining alone.

What a residual process-ammonia inventory costs when it is fully accounted for is
better shown outside rare earths altogether.

#### Precedent: ammonia at the Moab UMTRA site

The Moab uranium mill tailings pile in Utah — some 12 million cubic yards, about
16 million tons, of tailings on the bank of the Colorado River, left by the former
Atlas Minerals mill and now being relocated by the U.S. Department of Energy under
the Uranium Mill Tailings Radiation Control Act — has two contaminants driving its
groundwater programme, and only one of them is uranium [@doe2025moaboverview].
The tailings were pumped to an unlined impoundment, and excess water in the pile
drained through the underlying soils into the aquifer for decades. Ammonia is what
drives the active remediation: elevated ammonia in the backwater channels beside
the pile threatens young-of-year endangered fish [@doe2025moaboverview], among them
the razorback sucker and Colorado pikeminnow, whose measured chronic values for
un-ionized ammonia lie below the concentrations found in those backwaters
[@fairchild2005chronic].

Since 2003 DOE has run a groundwater interim action — now eight extraction wells
and more than thirty freshwater injection wells that dilute what still reaches the
river [@doe2025moaboverview]. Over the life of the project it has extracted
288.5 million gallons of groundwater and reports keeping **1,002,109 pounds of
ammonia** and **5,816 pounds of uranium** out of the Colorado
[@doe2025moabgroundwater]. Ammonia outweighs uranium in that ledger by a factor of
about 170. The tailings removal is currently estimated to finish in 2029, more
than a quarter century after the pumping started [@doe2025moaboverview].

The analogy to rare earth leaching is exact in cause and unfavourable in
geometry. Both are process ammonia introduced by a hydrometallurgical operation
and left in contact with an aquifer. But Moab is a *point* source — one pile,
which can be ringed with extraction wells and eventually dug up and moved — whereas
in-situ rare earth leaching injects ammonium directly into a hillside aquifer over
a large area with no engineered liner and nothing to relocate. Moab is the
multi-decade, million-pound, still-pumping illustration of the bill that ammonium
hydrometallurgy can incur, and it is the most concrete argument available for the
magnesium-sulfate and ammonium-free direction [@xiao2015leaching; @pan2024insights;
@luo2022development].

(electrokinetic-mining)=
## Electrokinetic Mining

The most substantial attempt to answer the ammonium problem does not change the
reagent. It changes what moves the ions.

Conventional in-situ leaching floods the hillside with lixiviant and relies on
gravity and permeability to carry the solution through the regolith and out at
the toe of the slope. That is why the section above spends so long on
permeability: hydraulic flow is the only transport mechanism available, it
follows the path of least resistance rather than the path through the ore, and
the reagent that does not find a rare earth ion stays in the ground.
**Electrokinetic mining** (EKM) emplaces electrodes in the regolith and drives a
direct-current field between them, so that the liberated REE³⁺ move by
electromigration and the pore water by electroosmosis. Transport is then
controlled by the field rather than by the local permeability, and the ions are
pulled towards a collection electrode instead of being flushed towards whatever
drainage the hillside happens to have.

@wang2022electrokinetic introduced the technique and demonstrated it at bench
scale, at scaled-up scale, and in on-site field experiments. Against
conventional practice they report roughly 2.6 times higher recovery efficiency,
an approximately 80 % decrease in leaching agent usage, and an approximately
70 % reduction in metallic impurities in the recovered rare earths. That last
figure is the interesting one for this book, because it is a separation claim:
the authors describe an autonomous purification mechanism in which the
enrichment arises from differences in mobility and reactivity between the rare
earths and the metallic impurities. An electric field sorts ions by mobility,
and aluminium, iron and calcium do not have the mobility of a trivalent
lanthanide.

The follow-up paper takes the technique to industrial scale
[@wang2025industrial]. The engineering problems it reports solving are electrode
reliability and flow leakage, and the new element is a voltage-gradient barrier
strategy based on electroosmosis — in effect using the field itself to contain
the leach rather than relying on the geology to do it. On a 5,000-tonne body of
rare earth ore they report 95 % REE recovery, and an environmental risk
assessment finding a **95 % reduction in ammonia emissions**. A comparative
technoeconomic analysis against the conventional technique is presented in
support of economic viability. A separate study compares leaching agents for EKM
[@xu2024comparative]; it is cited here for existence only, as its text was not
available for verification.

Three cautions belong with those numbers.

**The evidence is from one group.** Both papers come from the same laboratory
and appeared in the same journal. Nothing in the literature surveyed for this
chapter independently reproduces the field results, and a 95 % recovery on a
5,000-tonne ore body is the kind of claim that ought to be confirmed by someone
who did not develop the technique.

**The selectivity is not within the series.** The 70 % impurity reduction is
rare earths against aluminium, iron and calcium. It is a purification of the
pregnant liquor, not a fractionation of the lanthanides, and it does not touch
the argument of [](#clay-ion-exchange-as-a-separation-technology).

**A 95 % reduction in emissions is not a decontaminated aquifer.** The ammonium
already exchanged onto the clay in a conventional operation is the residue this
chapter is concerned with, and a technique that uses 80 % less reagent leaves
proportionately less of it — which is a large improvement and not the same as
none. Whether the field can also be used to recover ammonium already in the
ground is a question the surveyed literature does not answer.

With those qualifications, EKM is the most significant development in
ion-adsorption clay mining since the shift from heap to in-situ leaching, and
the only one that attacks the reagent inventory at its source rather than
treating its consequences. The electrochemistry of the technique, and its place
among the other electrically driven processes in this book, are discussed in
[](#electrochemical-separations).

## Recovering the Rare Earths from a Very Dilute Liquor

The pregnant leach solution from an ion-adsorption operation is roughly two orders
of magnitude more dilute than an acid leach liquor — the arithmetic is worked in
[](#ion-adsorption-clay-leaching-the-gentle-approach) — and concentrating it is
the one genuinely hard unit operation the route contains. Precipitation with
oxalic acid or ammonium bicarbonate and direct solvent extraction of the pregnant
solution are both used; those are treated as unit operations in the leaching
chapter [@han2024efficient; @liu2017enrichment].

What belongs here is the deposit-level lever, which is that liquor concentration
and extraction efficiency trade directly against one another and the trade can be
made deliberately. Moldoveanu and Papangelakis tested three ways of raising the
rare earth concentration in the leachate — decreasing the liquid-to-solid ratio,
re-using leachate on fresh ore, and counter-current leaching — and all three
worked, all three at the expense of the extraction level achieved
[@moldoveanu2016overview]. A plant can have a strong liquor or a high recovery
and must choose, and the right choice depends on whether the cost driver
downstream is solution volume or metal loss. This is the same argument that
justifies the closed lixiviant loop in the heap trial above [@meng2023heap]: the
reagent is only cheap the first time through.

The same study turns up a loss that flowsheets routinely omit. The water trapped
in the leached solid contains significant quantities of both rare earths and
residual lixiviant, and the residue therefore needs thorough washing
[@moldoveanu2016overview]. In a heap that is an extra wash stage and a recoverable
loss. In an in-situ operation, where the leached solid is the hillside, it is
neither: the entrained liquor stays in the ground, and it is both the metal that
was not recovered and the ammonium that will later appear in a stream.

(clay-ion-exchange-as-a-separation-technology)=
## Clay Ion Exchange as a Separation Technology

The forward-looking question about these deposits is whether the clay itself,
which is doing an excellent job of holding rare earths out of a very dilute
aqueous stream, could be used as a separation medium rather than merely as an
orebody. The answer depends entirely on which separation is meant, and the two
cases point in opposite directions.

For **group separation and preconcentration** — pulling the rare earths out as a
block from a dilute, dirty stream while rejecting sodium, potassium, calcium,
magnesium, aluminium and iron — the selectivity required is charge selectivity,
and clay has it in abundance. Natural clay minerals have been characterised
explicitly as adsorbents and as an alternative recovery medium for rare earths
from solution, with the operative parameters mapped [@alshameri2019understanding].
This is the mechanism the orebody already demonstrates at industrial scale.

For **individual-element separation** — resolving adjacent lanthanides — bare clay
is intrinsically weak, and the reason is the mechanism split of the previous
section: the dominant outer-sphere exchange cannot fractionate at all
[@wu2023rare]. No measured adjacent-pair separation factor for clay could be
verified for this chapter, and none is asserted; the qualitative statement that
the dominant mechanism does not fractionate is what the literature supports, and
it is sufficient to rule the approach out in its bare form. Adjacent selectivity
would have to be imported — from the minority surface-complexation sites, from a
complexing eluent, or from a ligand grafted onto the clay.

The existence proof for the clay-as-chromatography idea is the orebody itself.
Regolith profiles are vertically fractionated, with light/heavy zonation and
cerium anomalies, produced by clay loading against carbonate-complexing
groundwater acting as a mobile phase [@zhou2020genesis]. That is ion-exchange
{index}`chromatography` run over geologic time on a column kilometres wide. The
feasibility question is settled; throughput and control are the engineering
questions, and geologic time is not an available residence time.

Set against solvent extraction, then, clay ion exchange is strong exactly where
solvent extraction is weak and weak exactly where it is strong. Solvent extraction
is the incumbent for adjacent-element purity at scale and for bulk throughput, and
nothing about clay threatens that. Clay's advantages are group and matrix
separation, dilute feeds of the kind that make an extraction circuit uneconomic —
mine water, recycle streams, ash leachates — and the absence of a diluent, a crud
layer or a volatile organic inventory. Those are complementary strengths, which
argues for clay ahead of a solvent-extraction plant rather than instead of one.

(clay-research-opportunities)=
## Research Opportunities

**Clay as a preconcentrator ahead of solvent extraction.** This is the strongest
near-term opportunity and the one that follows most directly from the mechanism.
Load a dilute leachate onto clay, reject the monovalent and divalent matrix ions
on charge selectivity, and strip a concentrated, de-salted rare earth eluate into a
much smaller extraction plant or straight into precipitation
[@alshameri2019understanding; @moldoveanu2016overview]. It attacks the dilute,
high-volume penalty at its source rather than downstream of it. What is missing is
a demonstrated loading and stripping cycle with a measured concentration factor;
none could be verified here, and none is claimed.

**A light/heavy rough cut on the fractionating mechanism.** The surface-complexation
sites enrich heavies over lights [@wu2023rare]. A binary roughing split exploiting
that would be well matched to ion-adsorption feeds, which are already heavy-enriched,
and a rough cut does not need the stage selectivity that a pure product needs.

**Functionalised clay as extraction chromatography on a cheap support.** Grafting a
solvent-extraction-grade ligand — a phosphonic acid, or a {index}`diglycolamide`
such as {index}`TODGA` — onto clay would combine the selectivity of solvent
extraction with the convenience of a column. The approach is demonstrated on
porous supports with diglycolamide extractants, explicitly as a cleaner
alternative to liquid-liquid contacting [@momen2019extraction]; clay would be the
cheap and benign support variant, and the open questions are ligand loading,
attachment chemistry and cycle life rather than feasibility in principle.

**Continuous chromatography.** Batch single-column operation is what costs
chromatography its throughput, and simulated moving bed (SMB) operation is the
standard industrial answer — it is how sugars and enantiomers are separated at
scale. Applied to lanthanides it is nearly untried: a title search of the
literature returns two studies, both from the same group and both on resins rather
than clays, modelling SMB separation of lanthanides on a tertiary pyridine resin
and on Reillex HPQ, with the former predicting 118 g of solute per litre of resin
per day at 99.5 % purity for a neodymium-samarium pair
[@sreedhar2014evaluation; @sreedhar2014simulated]. Neither addresses a clay
stationary phase or an ion-adsorption feed. That is a genuine white space, and it
is adjacent to
{index}`counter-current <countercurrent cascade>` practice the field already knows.

**Synthetic and engineered clay analogues.** Synthetic smectites, pillared clays
and layered double hydroxides all have high exchange capacity, so the materials
question is not in doubt. The economic question is, because the value of a natural
deposit is precisely the geologic pre-concentration that put the rare earths onto
already-weathered rock for free [@zhou2020genesis]. Synthesising a sorbent and then
loading it from a dilute stream inverts that economy. The realistic role for
engineered sorbents is polishing and concentrating leachates and effluents, not
substituting for an orebody.

**Multi-element thermodynamic screening with kinetics.** Extending Pourbaix-style
modelling to multi-element, impurity-bearing systems with rate information, and
validating it against column data, would turn a reagent-narrowing exercise into a
design tool [@mohamadsobri2025enhancing]. The aluminium behaviour is the specific
gap: it is the impurity that governs the downstream purification burden, and the
current screening does not include it.

**Whether the field can fractionate.** The electrokinetic work above reports
enrichment of rare earths over metallic impurities on the grounds that the two
groups differ in mobility and reactivity [@wang2022electrokinetic]. Electrophoretic
mobility in a porous medium depends on hydrated radius, and the hydrated radii of
the lanthanides do differ across the series — that being the same contraction the
whole book is about. Nobody has reported measuring whether a field applied to a
regolith produces any lanthanide fractionation at all. It would be a cheap
measurement on an existing apparatus, and either answer is worth having: a
measurable intra-series mobility difference would be a new separation handle, and
a null result would settle whether the "selective" in electrokinetic mining refers
to anything beyond impurity rejection.

**Measured selectivity data.** Adjacent-pair separation factors on smectite and
vermiculite against kaolinite, as a function of edge-site density, pH and ionic
strength, would establish how far the fractionating mechanism can be pushed
[@wu2023rare]. At present the question cannot be answered quantitatively from the
published literature, which is itself the reason it is worth doing.

## The Residue Question

After leaching, the kaolinite and halloysite substrate is still there. The rare
earths desorbed; the clay did not dissolve. What is left is depleted regolith,
loaded with residual lixiviant cations, and the honest description of it is a
waste stream rather than a recycled material — true rare earth circularity comes
from end-of-life magnets, phosphors and electronic scrap
([](#recycling-and-urban-mining)), which is a different stream entirely.

The residue is not inert. Column and batch leaching experiments on tailings from
an ion-adsorption mining area found manganese, zinc and lead at 431.67, 155.05
and 264.33 mg/kg respectively, several times their local background values, with
manganese and lead released under rainfall at concentrations far exceeding
environmental limits and migrating into adjacent paddy soil. Ammonia nitrogen was
identified, alongside chemical speciation, rainfall pH and mineral properties, as
one of the primary controls on that release [@tian2024leaching]. The residual
ammonium is therefore not only a pollutant in its own right; it mobilises other
things.

### Valorisation routes that work

The spent clay is a depleted aluminosilicate — kaolinite and halloysite plus
quartz — and therefore chemically close to ordinary construction-clay feedstocks.
Three reuse routes have been demonstrated at laboratory or pilot scale, and in
most of them the motivation is not the construction value.

The best developed is **alkali activation into a geopolymer binder**.
Ion-adsorption rare earth tailings have been alkali-activated into geopolymers
[@zhang2022ion], and the same chemistry has been applied to rare earth tailings
more broadly [@hu2020synthesis]. In both cases the stated motivation is heavy-metal
immobilisation as much as construction: the geopolymer locks contaminants into its
matrix, so the route doubles as waste stabilisation. Given what
@tian2024leaching measured coming out of these tailings under rainfall, that is
the more valuable of the two functions. **Glass-ceramics** for building and
decorative use have been produced from rare earth tailings, though on hard-rock
mill tailings rather than on leached clay [@zhao2010utilization]. And the
aluminosilicate residue has been converted to high-crystallinity **Zeolite A**,
which then adsorbs pollutants in the mine's own water — a closed loop in which the
waste treats the waste [@cheng2024synthesis].

Two analogies that suggest themselves do not survive inspection. Clays are
generally avoided as **asphalt** filler because they are moisture-sensitive and
promote stripping at the binder-aggregate interface. And **drywall** is gypsum,
CaSO₄·2H₂O; the only connection to this flowsheet is the gypsum byproduct of
sulfate neutralisation, not the clay residue.

### In-situ mining leaves nothing to valorise

The decisive practical objection is structural. In the dominant modern method the
clay is never excavated, so there is no solid residue stream to send anywhere.
For those operations the residue question is not valorisation but in-place land
reclamation and revegetation, which is a soil-science and agronomy problem —
restoring nutrient cycling and plant cover on a substrate stripped of its
exchangeable cations and loaded with ammonium and aluminium
[@liu2022biogeochemical]. Collectable tailings exist mainly at older excavated
operations, and even there the residual reagent and aluminium have to be managed,
while low-value bulk construction materials do not travel far from remote mining
regions.

The net position is that valorisation is real, locally attractive, and most
valuable for its stabilisation function rather than its product value — but it is
not a mainstream fate, and in-situ mining structurally limits how much residue is
ever collectable in the first place. Which fate actually dominates in practice is
poorly documented. It is the most decision-relevant open question about these
deposits and the one with the thinnest published evidence behind it, and this
chapter cannot resolve it.

## Net Assessment

Ion-adsorption clays are environmentally double-edged in a way that resists
summary. The extraction chemistry is the mildest in this book: no roasting, no
strong acid, no fluorine, no thorium programme, ambient temperature, and a 90-95 %
REO concentrate out of a 0.1 % ore in a single selective contacting step
[@iaea2011radiation]. Against that, the *process* footprint is large and diffuse —
nitrogen in the groundwater, permeability loss and uneven recovery underground,
slope deformation, hundreds of tonnes of disturbed regolith per tonne of product,
and a residue stream whose fate is undocumented.

The whole research frontier is an attempt to keep the first while shrinking the
second: magnesium sulfate and ammonium-free lixiviants, aluminium suppression,
closed reagent loops, preconcentration ahead of solvent extraction, and residue
stabilisation. What makes that frontier tractable is that none of the difficulties
are chemical. They are containment, transport and land-use problems attached to a
chemistry that already works.

Electrokinetic mining is the clearest illustration of that. It leaves the
exchange chemistry untouched and replaces the transport mechanism, and on its
developers' own figures that alone cuts reagent use by about 80 % and ammonia
emissions by about 95 % [@wang2022electrokinetic; @wang2025industrial]. If those
results hold up under independent replication, the ammonium problem that
dominates this chapter becomes an engineering choice rather than a property of
the deposit.
