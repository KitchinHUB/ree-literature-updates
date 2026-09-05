---
title: Environment, Techno-Economics, and Life Cycle
---

(environment-techno-economics-and-life-cycle)=
# Environment, Techno-Economics, and Life Cycle

Three questions get asked of every new separation technology, and they are
usually asked too late: what does it emit, what does it cost, and what does it
do over a full life cycle? This chapter gathers the three.

They are grouped together because they interact, and because a claim made
against one of them is routinely refuted by another. A process that eliminates
organic solvent looks clean until its energy intensity is counted. A process
with lower operating cost may carry capital costs that only make sense above a
throughput no one has yet demonstrated. And the environmental burden of rare
earth production is dominated, in most life cycle studies, not by the separation
step at all but by mining, radioactive residue management, and the acid and
reagent load upstream — which means an improvement confined to the separation
stage moves a smaller number than its advocates usually claim.

The {index}`techno-economic <techno-economic analysis (TEA)>` and life cycle sections that follow are the right place to
check the claims made in Part III.

## Environmental and Sustainability Considerations

### Environmental Impacts of Traditional Methods

The environmental burden of conventional rare earth production falls into five
categories, and it is worth being clear that only two of them belong to the
separation step. Mining destroys habitat and moves overburden. Cracking and
leaching generate acidic or alkaline wastewater at a volume set by the reagent
stoichiometry ([](#hydrometallurgical-leaching)). The thorium and uranium that
accompany monazite and bastnasite become a radioactive residue that has to be
managed rather than discharged ([](#thorium-management)). Pyrometallurgical
routes carry the energy cost of holding a reactor at several hundred degrees
([](#pyrometallurgical-and-halogenation-routes)). Only the last two —
organophosphorus extractant and kerosene diluent inventories, and the acid
consumed in stripping and pH adjustment — are attributable to solvent
extraction itself.

That accounting matters for the rest of this chapter, because it sets a ceiling
on what any new separation chemistry can deliver. Life cycle studies of rare
earth production repeatedly find the upstream stages dominant; a technology
that halves the burden of the separation step alone moves a much smaller
number than its proponents typically claim.

Some of the highest pollution levels on Earth are associated with rare earth
production in China, which mined **69%** of world output in 2025 and supplied
**71%** of United States imports of rare-earth compounds and metals over
2021–24 [@usgs2026mineral]. The share of world *separation* capacity is commonly
put near 90%, but no agency publishes it and this book could not trace the
figure to a primary source; see [](#supply-chain-concerns).

### Green Chemistry Approaches

Three classes of alternative are usually offered as the environmental answer:
deep eutectic solvents, ionic liquids, and bioleaching. All three are treated
in detail elsewhere in this book, and the treatment there is deliberately less
enthusiastic than the label "green" implies.

Deep eutectic solvents and ionic liquids are covered in
[](#green-solvents-des-and-ils). Both are non-volatile and non-flammable, which
genuinely removes the fire and vapour-emission hazards of a solvent extraction
house, and DESs are cheap to make. But "green" is not a synonym for "benign":
amino-acid-based DESs, chosen precisely because their components are natural
and biodegradable, have been measured as up to 10⁵ times more toxic than
conventional choline-chloride formulations [@li2022high]. No life cycle
assessment consulted for this book compares a DES or IL flowsheet against a
conventional one on a cradle-to-gate basis, so the environmental case for them
rests on hazard properties rather than on a measured impact.

Bioleaching is covered in [](#siderophores-and-the-boundary-with-leaching) and
[](#hydrometallurgical-leaching). The mechanisms, organisms and process
parameters are reviewed comprehensively by @rasoulnia2020critical. Recovery
efficiencies quoted for bioleaching span a wide range and depend on the
organism, the substrate mineralogy, the pulp density and the residence time;
no single figure characterises the method, and none is given here. What the
literature does establish is that bioleaching is slow relative to acid
leaching, which is the constraint that governs whether its lower reagent
burden can ever be cashed in.

### Molecular Recognition Technology

Ligand-on-support column chemistry, marketed as SuperLig® Molecular
Recognition Technology, is regularly cited as an ambient-temperature
alternative to solvent extraction. The recovery and purity figures in
circulation for it come from the vendor's own product literature. No
peer-reviewed source consulted for this book reports them, and no entry for
them appears in this bibliography, so they are not quoted here. The technology
and the status of the claims made for it are discussed alongside the other
commercial players in [](#industrial-status-and-key-players).

## Techno-Economic Analysis

Techno-economic analysis is essential for evaluating the commercial viability of REE separation processes, comparing alternative technologies, and guiding investment decisions. This section summarizes key economic parameters and recent TEA studies.

### Cost Structure Overview
REE separation projects involve significant capital and operating costs that vary substantially by technology, scale, and feedstock [@obrien2024simplified].

Capital cost divides across the same categories as any hydrometallurgical plant:
process equipment (reactors, mixer-settlers, columns), installation, engineering
and project management, instrumentation and control, civil works, and a
contingency allowance. Operating cost divides across reagents, energy, labor,
maintenance, and effluent treatment. The share each category takes in a rare
earth separation plant specifically is not published, and the generic factors
tabulated in cost-engineering texts are not REE data; no percentage breakdown is
given here.

What the REE-specific studies do establish is which items dominate. In the acid
mine drainage assessment discussed below, capital cost and HCl consumption are
the two factors that move the internal rate of return most
[@larochelle2021fundamental]. In the Mountain Pass analysis, oxide recovery has a
larger effect on project economics than either capital or operating cost
[@uysal2022economic].

### Solvent Extraction Economics
Solvent extraction remains the dominant commercial technology, with well-established cost profiles.

**Aclara Resources separation plant (2024).** The figures below are a
*company disclosure*, not an independent assessment, and they are reproduced
here because published cost estimates for a dedicated rare earth separation
plant are otherwise almost impossible to find. Two qualifications travel with
them. First, an AACE Class 5 estimate is a screening-grade number prepared on
minimal engineering definition; the class is conventionally understood to carry
an accuracy range of roughly −50% to +100%, so US\$354 million should be read
as an order of magnitude rather than a budget. Second, the recoveries are
design targets for a plant that has not been built.

| Parameter             | Value           |
|-----------------------|-----------------|
| Total CAPEX           | US\$354 million |
| SX plant              | US\$244 million |
| Zero liquid discharge | US\$110 million |
| OPEX                  | US\$12/kg REO   |
| NdPr recovery         | 94%             |
| Dy recovery           | 92%             |
| Tb recovery           | 91%             |
| Product purity        | \>99.5%         |

**{index}`Mountain Pass` Processing:** The published economic analysis of
{index}`bastnäsite` from Mountain Pass compares *beneficiation* routes — direct
leaching, attrition scrubbing followed by leaching, and flotation followed by
leaching — rather than separation routes, and its costs are therefore costs of
REO in concentrate, not of separated oxide [@uysal2022economic]. Flotation plus
leaching is the most profitable of the three: it adds capital and operating cost
but delivers a higher grade and a higher recovery, which more than compensate.

**Sensitivity Analysis:** In that study, oxide recovery has a larger effect on
project economics than either capital cost or operating cost
[@uysal2022economic]. Note that costs quoted per kilogram of *concentrate* and
per kilogram of *separated oxide* differ by well over an order of magnitude; the
basis must be stated before any two figures in this section are compared.

### Alternative Technology Economics
**Supercritical Fluid Extraction (2025):** TEA for 4000 L industrial-scale sc-CO₂ facility [@azimi2025technoeconomic]:

| Parameter        | Value                              |
|------------------|------------------------------------|
| CAPEX            | \$13.7-14.6 million                |
| Year 1 OPEX      | \~\$3 million                      |
| Key cost drivers | High-pressure equipment, CO₂       |
| Break-even       | Competitive for niche applications |

**Coal Refuse REE Recovery (2025):** Chemical recycling with 90% reagent recovery [@nili2025reclaiming]:

| Parameter        | Value           |
|------------------|-----------------|
| Initial CAPEX    | \$35 million    |
| NPV              | \$262.4 million |
| ROROI            | 42%             |
| Product          | RE-hydroxide    |
| Reagent recovery | 90%             |

**Electrokinetic mining (2025):** @wang2025industrial cost their 5,000-tonne
industrial-scale trial against conventional in-situ leaching, and the result is
more interesting than "economically viable" suggests. On direct production cost
the electrokinetic route is **more expensive**: US$7,078 per tonne of REO
against US$6,214 for conventional leaching, about 14 % higher. The gap is
electricity and electrode. Producing a tonne of REO consumes roughly 4,286 kWh,
costing US$420, and the conductive polymer electrode adds US$812 per tonne; the
authors name both as the items that must come down before the technique is
practical. For the trial itself, equipment was US$43,527 and materials
US$16,641.

What reverses the comparison is the cost the conventional route does not carry
on its own books. Vegetation restoration, soil remediation and water treatment
run to **US$16,477 per tonne of REO** for conventional in-situ leaching — more
than twice the entire direct production cost — and the authors' figure is that
including them makes conventional mining three times more expensive than the
electrokinetic route.

That is a textbook externality argument, and it should be read as one. The
comparison holds only where remediation is actually paid for. Where it is not —
which describes most of the historical record of this ore type
([](#ion-adsorption-clays)) — an operator comparing the two techniques sees a
14 % cost increase and no offsetting saving. The case for electrokinetic mining
is a regulatory case before it is an economic one. All of these figures come
from a single group's single trial, and none has been reproduced. The technique
is described in [](#electrokinetic-mining).

### Mining Project Cost Estimation
**Simplified Cost Framework:** Screening a greenfield project before a
feasibility study exists is the problem @obrien2024simplified set out to solve.
Their model approximates capital and operating expenditures for greenfield REE
mines from a handful of project descriptors rather than from site knowledge,
and covers open-pit and underground mines whose processing ranges from
beneficiation alone through to individual REE separation. No single CAPEX range
per project type is given, and none should be quoted: the point of the model is
that the number is a function of scale and flowsheet depth, not a category.

What the model is for is visible in what it found. Of twelve projects outside
China in early to advanced development, nine had a positive NPV at the 2011
peak in rare earth prices, **none** had a positive NPV at the 2016 trough, and
two were positive on 2022 and projected 2028 prices [@obrien2024simplified].
The same flowsheet is economic or not depending on which year you price it in,
which is the honest answer to why announced projects so rarely reach
production.

**Blended product economics.** A mine sells a basket, not an element, so the
economics turn on a blended price across the oxides the deposit actually
contains — which is why two projects with identical flowsheets and identical
recoveries can have opposite verdicts. Break-even prices, required rates of
return and capital intensities for integrated mining-and-refining projects
circulate widely in consultancy notes. They are not quoted here: the ones
traced for this book sit behind paywalls, carry no published methodology, and
could not be checked against a primary filing. @obrien2024simplified, discussed
above, is the peer-reviewed treatment of the same question.

### Acid Mine Drainage REE Recovery
Acid mine drainage is an unusual feed: the rare earths are already in solution,
already at low pH, and the water has to be treated whether or not anything is
recovered from it, so part of the cost is borne by an existing obligation.
@larochelle2021fundamental assessed recovery from a network of AMD sources
rather than a single site, using the conventional organophosphorus extractants
— {index}`D2EHPA`, {index}`EHEHPA`, CA-12, {index}`Cyanex 272` and Cyanex 572.
Two conclusions carry beyond that study. Capital cost and hydrochloric acid
consumption dominate the economics, and credits for the cobalt and manganese
co-recovered with the rare earths materially improve them. Feed concentration
matters in the direction expected, which is why a network of sources beats a
single dilute one.

The same "the water is being handled anyway" argument is made for oilfield
produced water, and [](#produced-water-critical-minerals) is where it is
tested. The result there is a warning about how far the argument carries: the
one published techno-economic analysis of centralised produced water treatment
finds the evaporator dominating every case at more than twice the levelized
cost of the membranes, and the divalent-removal step that AMD gets cheaply by
precipitation is cost-prohibitive at Appalachian hardness
[@wenzlick2020techno]. An existing disposal obligation lowers the cost of
getting the water; it does not lower the cost of the separation.

**Monte Carlo Sensitivity:** The tornado analysis is unusually clean, and
worth quoting for what it rules out as much as for what it finds: "only two
project parameters have a significant impact on the profitability of the
project, the capital cost of the project and the pricing of hydrochloric acid"
[@larochelle2021fundamental]. Rare earth price was among the distributed inputs
and did *not* emerge as a significant driver; recovery rate was not given a
distribution at all. With raw-material and consumable prices sampled over their
2014-2021 market ranges and capital cost given a normal distribution matching
the ±40% precision of the estimate, the simulated rate of return is
approximately normal between about **18% and 35%**, its shape set mostly by
capital cost.

### Process Comparison Economics
Separation factors, purities, demonstrated scale, and technology readiness levels
for the technologies covered in Parts II and III are compared in a single table in
[](#technology-comparison), and are not repeated here.

### Key Economic Drivers
The drivers divide into two groups: what is in the ground, and what is done to
it. The first group is fixed before a process is chosen. Grade sets how much
rock must be moved and crushed per kilogram of product, and the distribution
within the ore decides what that product is worth — a heavy-rich deposit
commands a premium because the heavies are where the value and the scarcity
are. The second group is what engineering can act on: recovery across the
flowsheet, reagent consumption (extractant and acid, which the AMD analysis
above found dominant), whatever credit can be taken for by-products such as
thorium, uranium, iron, phosphorus and fluorine, the scale of the facility, and
where it is built, which sets infrastructure, labour and permitting costs.

Against those sit risks that no flowsheet controls. Rare earth prices have
historically moved by an order of magnitude within a few years, and
[](#the-industrial-landscape) is where that volatility and its causes are
treated. Permitting is slow where radioactive residues
are involved. Any process not yet built at scale carries scale-up risk, which is
the thing a techno-economic assessment of a laboratory result systematically
underprices. And trade policy can change the price of the product and the
availability of the reagents at once.

## Life Cycle Assessment

{index}`Life cycle assessment <life cycle assessment>` provides a comprehensive framework for evaluating the environmental impacts of REE production, enabling comparison of technologies and identification of improvement opportunities.

### LCA Framework for REE Production

Rare earth life cycle studies conventionally draw a cradle-to-gate boundary
[@navarro2014life], running from mining through beneficiation, cracking and
leaching, separation, precipitation and calcination to a rare earth oxide:

Mining → Beneficiation → Cracking/Leaching → Separation → {index}`Precipitation <precipitation>` → Calcination → REO

Most take 1 kg of rare earth oxide as the functional unit, though some report
per individual element — a distinction that matters more than it sounds,
because the burden allocated to a kilogram of dysprosium and to a kilogram of
undifferentiated mixed oxide differ by a large factor. The impact categories
usually reported, and what drives each in a rare earth flowsheet, are these:

| Category | Unit | Key Contributors |
| ---------- | ------ | ------------------ |
| Global Warming Potential (GWP) | kg CO₂-eq | Energy, chemicals |
| Acidification Potential (AP) | kg SO₂-eq | Acid production, SO₂ emissions |
| Eutrophication Potential (EP) | kg PO₄-eq | Ammonium, phosphate releases |
| Human Toxicity (HT) | kg 1,4-DCB-eq | Heavy metals, radioactivity |
| Water Depletion | m³ | Process water, cooling |
| Land Use | m²·year | Mining, waste storage |

### Carbon Footprint of REE Production
**Global Warming Potential Ranges:** Carbon footprint varies significantly by
ore type and process. @zapp2022environmental put the reason plainly -- impacts
are "mainly related to the geology of a deposit, mineral type and composition,
the methods of extraction, local supply of energy and auxiliary materials, and
regulatory conditions", so they "vary considerably" and no single figure
represents the industry. That review compares process chains in normalized
person-equivalents rather than tabulating absolute cradle-to-gate GWP across
studies, so the spread has to be read from the individual studies. Two values
with a clear published basis anchor it:

| Source/Process                          | GWP (kg CO₂-eq/kg REO) | Source                   |
|-----------------------------------------|------------------------|--------------------------|
| Monazite processing (average)           | 65.4                   | [@browning2017life]      |
| Ionic rare earth clays, mixed REO       | 17.8-24.3              | [@wan2022lca]            |

The ionic-clay figure carries a stated uncertainty of about 16%, and it rises
when magnesium-salt leaching replaces ammonium-salt leaching: the substitution
that relieves the ammonia problem described in [](#ion-adsorption-clays)
increases the carbon footprint of the product [@wan2022lca].

**Element-Specific GWP from {index}`Monazite <monazite>`:** Allocating impacts
to individual elements reveals a spread of nearly an order of magnitude across
the fifteen rare earths produced from monazite [@browning2017life]:

| Quantity                        | Value | Element                     |
|---------------------------------|-------|-----------------------------|
| Average, 15 REEs from monazite  | 65.4  | --                          |
| Lowest                          | 21.3  | Europium                    |
| Highest                         | 197.9 | Yttrium                     |

(kg CO₂-eq per kg of oxide.) The intermediate elements are reported
graphically rather than numerically in that study, and its allocation groups
several elements together -- samarium and gadolinium share a single flowsheet
group, and so a single value -- so per-element figures between the two extremes
should not be quoted from it. Browning and colleagues also caution that
yttrium's position at the top is a consequence of how little heavy rare earth
there is in monazite, and is not representative of heavies recovered from
xenotime or from ion-adsorption clays.

Which activities dominate each impact category is tabulated in the hotspot
analysis later in this chapter. Percentage shares of total GWP are not given:
the published studies draw their system boundaries and allocate between
co-products differently, so shares taken from separate studies do not add up to a
single accounting.

### Water Footprint
**Water Consumption by Process:** REE production is highly water-intensive.
The same monazite inventory that gives the carbon figures above also reports
water [@browning2017life]:

| Element            | Water Consumption (kg/kg REO) |
|--------------------|-------------------------------|
| Average (all REEs) | 11,170                        |
| Samarium           | 3,803 (lowest)                |
| Gadolinium         | 3,803 (lowest)                |
| Yttrium            | 29,902 (highest)              |

Samarium and gadolinium share the low figure because they share a flowsheet
group, not because they were separately measured. Gross energy follows the same
pattern -- 917 MJ/kg on average, 311 MJ/kg for the samarium-gadolinium group
and 3,401 MJ/kg for yttrium. These inventories report water and energy per
kilogram of oxide and per element; they do not resolve either by process stage,
and no stage-by-stage split is given here.

### Ore-Specific Environmental Impacts
The four feedstocks fail in four different directions, and the mineralogy
predicts which.

Bastnäsite carries little thorium or uranium, so the radioactive residue problem
that dominates monazite is largely absent. What it has instead is a
sulfuric-acid roast, and with it SO₂, and open-pit mining dust that shows up in
the particulate-matter category.

Monazite is the opposite case. The thorium and uranium that come with it have to
be managed as radioactive waste, which drives both the human toxicity result and
the permitting timeline; the caustic cracking route adds a sodium hydroxide
waste stream on top.

{index}`Ion-adsorption clays <ion-adsorption clay>` avoid hard-rock mining
altogether and their energy intensity is correspondingly lower, but in-situ
leaching puts ammonium sulfate into the ground and it does not stay there. The
consequence is ammonia in groundwater and marine eutrophication, which is why
that impact category has a different dominant contributor for this route than
for any other. [](#ion-adsorption-clays) treats the chemistry and the remediation
problem.

The one reported intervention that acts on that category directly is
{index}`electrokinetic mining`, which replaces hydraulic flow through the
regolith with an applied electric field and so needs far less lixiviant to
contact the same ore. @wang2022electrokinetic report roughly 80 % less leaching
agent than conventional in-situ practice, and @wang2025industrial report a 95 %
reduction in ammonia emissions in an environmental risk assessment of a
5,000-tonne ore body — ammonium in groundwater down 94.89 % and in surface water
down 98.08 % against the conventional comparison — alongside a comparative
technoeconomic analysis, whose figures are set out under
**Electrokinetic mining (2025)** earlier in this chapter. Two qualifications belong with those figures and are
made in full in [](#electrokinetic-mining): both papers come from one
laboratory and neither result has been independently reproduced, and an
emissions reduction is not a remediation — the ammonium already exchanged onto
the clay at existing sites is unaffected by a technique that puts less in at new
ones. No published life cycle assessment of the electrokinetic route was found
for this chapter, so the comparison above is between a reported emission
reduction and a category total, not between two LCAs.

Eudialyte has neither monazite's radioactivity nor bastnäsite's grade. Its
difficulty is that the rare earths are a small fraction of a complex silicate,
so the gangue-to-product ratio is high and the chemical consumption per kilogram
of oxide rises with it.

### Comparative LCA of Technologies

The comparison a reader wants at this point — global warming potential, water,
waste, and toxicity for each separation method on a common basis — cannot be
assembled from the published literature. Cradle-to-gate assessments exist for
primary production routes built on solvent extraction
[@zapp2022environmental; @navarro2014life; @browning2017life; @zaimes2015environmental]
and for ionic clays [@wan2022lca]; supercritical CO₂ has been assessed
techno-economically but not on a comparable life cycle basis
[@azimi2025technoeconomic]. Molecular recognition, membrane, and biological
routes have no cradle-to-gate LCA at boundaries that would let them be ranked
against solvent extraction. A table ranking all five would be assertion rather
than measurement, and none is given.

**Recycling vs. Primary Production:** Secondary recovery from waste streams
performs better than primary production, but the published evidence supports
fewer numbers than the claim is usually made with. The systematic review of the
LCA literature reports one headline figure: recycling NdFeB magnets reduces
environmental impact by **64-96%** relative to virgin production, stated as a
general impact reduction rather than for any one category
[@mugion2025systematic]. Within that, acid-free dissolution is credited with a
**73%** reduction in global warming impact against conventional routes. A
category-by-category table of reductions -- acidification, water, toxicity,
land use -- is not available from that review, and is not given here.

### Process Hotspot Analysis
**Dominant Impact Contributors:** [@zapp2022environmental]

| Impact Category    | Primary Contributor                |
|--------------------|------------------------------------|
| GWP                | Chemical production (acids, NaOH)  |
| Acidification      | Energy generation, acid use        |
| Eutrophication     | Ammonium emissions (IAC leaching)  |
| Particulate matter | Mining dust (bastnäsite, monazite) |
| Human toxicity     | Heavy metals, radionuclides        |
| Water              | Process water, washing             |

**Energy Intensity:** Two anchors are available, and neither is a breakdown.
@browning2017life put the gross energy requirement for rare earths from monazite
at 917 MJ/kg on average, spanning 311 MJ/kg for the samarium-gadolinium group to
3,401 MJ/kg for yttrium; the integrated mining-and-refining estimate quoted
earlier in this chapter puts total energy use above 100 MWh per ton of REO. For
scale, @zaimes2015environmental find that producing heavy rare earth oxides
consumes **over twenty times** more primary energy per unit mass than steel.
Where that energy goes inside the flowsheet is the question this chapter opened
with, and it is the one the literature does not answer. Mining together with
extraction and roasting are identified as the dominant contributors for the
Bayan Obo route [@zaimes2015environmental], but no study splits the total
between mining, cracking, and the separation train itself, and no split is given
here.

### Data Challenges and Uncertainties

Every number in this chapter should be read with the same caveat, and it is
worth stating once rather than attaching to each. Most rare earth production is
in China, and the process data behind a life cycle inventory for it is not
generally available; what circulates instead is a small number of inventories,
reused, adapted and re-aggregated. Process information that is available is
often proprietary in its details. Rare earth flowsheets are multi-output by
nature — a mixed oxide is separated into fourteen products of wildly differing
value — so the allocation choice between mass, economic value and exergy moves
the answer per kilogram of any one element by more than most process
improvements would. Studies differ in vintage, in the grid mix they assume, and
in where they draw the system boundary, and those three differences are enough
to explain much of the spread between published figures without anyone having
made an error.

The honest consequence is that the *ordering* of impacts is more robust than
their magnitudes. That chemical production dominates global warming potential,
that ammonium emissions dominate eutrophication for the ion-adsorption clay
route, and that heavy rare earths cost far more energy per kilogram than light
ones, are conclusions that survive the assumptions. The absolute values do not
travel as well, and no aggregate uncertainty range is quoted here, because none
of the sources consulted for this chapter reports one in a form that could be
carried across studies.

### Improvement Opportunities

The reductions available divide into three kinds, and they differ in how much
evidence stands behind them.

The first is ordinary process engineering applied to the flowsheet that already
exists: recycling reagents rather than neutralizing them, integrating heat
between the roasting and the leaching steps, moving the electricity supply off
coal, treating and reusing process water, and finding buyers for by-products
that are currently waste. These are unglamorous, and they act directly on the
hotspots identified above — chemical production and energy generation — which is
what makes them the most reliable of the three.

The second is substituting a technology for one of the unit operations, which is
what most of this book is about. Supercritical CO₂ in place of an organic
diluent, a biological or biomimetic system in place of a cascade, a membrane for
a bulk split, an electrochemical route to the metal
([](#electrochemical-separations)). The chapters on each treat
what has actually been demonstrated, and the summary that applies here is that
none has yet been shown at a scale where a life cycle assessment of it would
mean much. The environmental case for them is a projection.

The third is not a process change at all but a change in what is fed to the
process: urban mining from e-waste, industrial symbiosis that treats
{index}`red mud` and coal ash as feedstocks rather than tailings, designing
products so the magnets can be recovered, and extended producer responsibility
to make someone accountable for the end of life.
[](#recycling-and-urban-mining) treats the recovery chemistry; the point
here is that a secondary feed skips mining, comminution and cracking altogether,
and that is where the impacts of the primary route are concentrated. It is the
only one of the three that changes the denominator rather than the numerator.
