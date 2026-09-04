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
### Major REE Minerals
Rare earth elements do not occur as native metals but are found in approximately 250 minerals, with only four types being economically viable for large-scale extraction [@jha2016hydrometallurgical; @kim2025rare].

#### Primary Minerals

1.  **Bastnäsite** (REE·FCO₃) - Carbonate-fluoride
    - Composition: (Ce,La,Nd,Pr)CO₃F
    - REO content: 60-75%
    - Light REE enriched (La, Ce, Pr, Nd)
    - Major source: {index}`Mountain Pass` (USA), {index}`Bayan Obo` (China)
    - Challenge: Fluorine content requires defluorination
2.  **Monazite** ((REE,Th)PO₄) - Phosphate
    - Composition: (Ce,La,Nd,Th)PO₄
    - REO content: 50-70%
    - Contains 0.1-12 wt% ThO₂ (radioactive)
    - Mixed light and middle REEs
    - Major source: Beach placers (India, Brazil, Australia)
    - Challenge: Thorium management, refractory phosphate matrix
3.  **Xenotime** (YPO₄) - {index}`Yttrium <yttrium>` phosphate
    - Composition: YPO₄ with heavy REEs
    - REO content: 50-67%
    - Heavy REE enriched (Y, Dy, Er, Yb)
    - Associated with monazite in placers
    - Challenge: Very refractory, difficult to decompose
4.  **Ion-Adsorption Clays** (Southern China deposits)
    - REEs weakly bound to clay surfaces [@shi2022column; @han2024efficient]
    - REO content: 0.05-0.3% (very low grade)
    - Heavy REE enriched (Y, Dy, Tb, Eu)
    - Unique: No crystalline REE minerals
    - Advantage: Easy leaching with mild electrolytes

### Processing Overview
Every route in this chapter has the same skeleton: mine, beneficiate, decompose
the mineral, leach, separate the solids from the liquor, purify that liquor, and
hand it to solvent extraction [@jha2016hydrometallurgical; @kim2025rare].
[](#fig-leaching-flowsheet), at the end of the chapter, draws that skeleton for
each of the ore types at once, so the routes can be compared step by step
instead of read one after another.

**This chapter covers beneficiation through purification** — the steps that
produce the aqueous REE feed. The separation of that feed into individual
elements is [](#solvent-extraction-fundamentals), and the finished oxides are
downstream of both.

### Challenges in REE Ore Processing
1.  **Refractory nature**: REE minerals resist decomposition [@kim2025rare]
    - Strong REE-O, REE-P, REE-F bonds
    - High thermal stability
    - Resistant to acid attack
2.  **Fluorine in bastnäsite**: Environmental concern [@chi2004recovery]
    - HF released during acid leaching (toxic, corrosive)
    - Requires defluorination pre-treatment
3.  **Thorium in monazite**: Radioactive [@borai2016modified; @amaral2010thorium]
    - 0.1-12 wt% ThO₂
    - Regulatory challenges
    - Requires separate disposal/recovery
4.  **Low grade ores**: Economic challenge
    - Ion-adsorption clays: 0.05-0.3% REO
    - Requires processing large volumes
    - High reagent consumption
5.  **Complex gangue minerals**: Processing difficulty
    - Calcite, dolomite (consume acid)
    - Silicates (form gels)
    - Iron oxides (contaminate products)

## Ore Beneficiation and Pre-Concentration
Before leaching, physical separation methods concentrate REEs from gangue [@jordens2013beneficiation; @chelgani2015rare].

### Crushing and Grinding
**Purpose**: Liberate REE minerals from host rock

**Typical process**:

1.  Primary crushing: Jaw crusher (1 m → 10 cm)
2.  Secondary crushing: Cone crusher (10 cm → 1 cm)
3.  Grinding: Ball mill or rod mill (1 cm → 100-200 μm)
4.  Classification: Cyclones or screens

**Target particle size**:

- Flotation feed: 75-150 μm (optimal)
- Gravity separation: 100-500 μm
- Magnetic separation: 50-200 μm

### Gravity Separation
**Principle**: Density difference between REE minerals and gangue [@zhou2024gravity]

**Density values**:

- Bastnäsite: 4.9-5.2 g/cm³
- Monazite: 4.9-5.3 g/cm³
- Xenotime: 4.4-5.1 g/cm³
- Gangue (quartz, calcite): 2.6-2.9 g/cm³

**Methods**:

1.  Shaking tables
2.  Spiral concentrators
3.  Jigs
4.  Heavy media separation (DMS)

**Performance**:

- Recovery: 60-80% REE
- Grade improvement: 2-5× enrichment
- Used as pre-concentration before flotation

### Magnetic Separation
**Principle**: Magnetic susceptibility differences [@chen2023various]

**Magnetic properties**:

- Monazite: Paramagnetic (χ ≈ 500-900 × 10⁻⁶ CGS)
- Xenotime: Paramagnetic (χ ≈ 100-300 × 10⁻⁶ CGS)
- Bastnäsite: Weakly paramagnetic
- Gangue: Typically diamagnetic or weakly paramagnetic

**Equipment**:

1.  Low-intensity magnetic separator (LIMS): Remove magnetite, hematite
2.  High-intensity magnetic separator (HIMS): Concentrate paramagnetic REE minerals
3.  High-gradient magnetic separator (HGMS): Fine particle separation

**Industrial application**:

- Bayan Obo (China): Magnetic separation of bastnäsite-magnetite ore
- Recovery: 70-85%

### Froth Flotation
**The principal beneficiation method** for bastnäsite and monazite [@chelgani2015rare; @jordens2013beneficiation]

#### Bastnäsite Flotation
**Collectors** (promote hydrophobicity):

- Fatty acids: Oleic acid, tall oil, hydroxamic acids
- Optimal pH: 8-10 (alkaline)
- Concentration: 500-2000 g/ton

**Mechanism**:

- COO⁻ groups adsorb on REE-F surface sites
- Forms hydrophobic REE-oleate surface complex
- Enables bubble attachment

**Depressants** (suppress gangue):

- Na₂SiO₃ (sodium silicate): Depresses silicates
- Quebracho, tannin: Depress calcite
- NaF: Selective depression

**Circuit structure**: rougher, scavenger and cleaner stages in series, as in
any sulphide flotation plant. Grades and recoveries are strongly deposit- and
mineralogy-specific; the Mountain Pass figures below are given as one sourced
example rather than as a general band.

#### Monazite/Xenotime Flotation
**Collectors**:

- Hydroxamic acids (more selective than fatty acids)
- Alkyl phosphates
- Optimal pH: 6-9

**Challenges**:

- Similar flotation behavior to gangue apatite
- Requires selective depressants
- Fine particle losses (\<20 μm)

**Typical flowsheet**:

1.  Rougher flotation (high recovery)
2.  Cleaner flotation (high grade)
3.  Scavenger flotation (treat rougher tailings)
4.  3-6 stages total

### Beneficiation Summary
**Typical concentration factors**:

- Raw ore: 5-15% REO → Concentrate: 50-75% REO
- Overall recovery: 60-80%
- Produces "concentrate" suitable for leaching

Treat those bands as an order-of-magnitude orientation across deposits, not as
a flowsheet: feed grade, product grade and recovery are only meaningful
together, from one operation. The Mountain Pass case immediately below is such
a chain -- feed grade, product grade and recovery all from the same source --
and is the one to reason from.

**Mountain Pass (USA) beneficiation** [@kim2025rare]:

- Feed: 7-9% REO bastnäsite ore
- Crushing → grinding → flotation (3 stages)
- Product: 60% REO concentrate
- Recovery: 70%

## Bastnäsite Processing: Roasting and Leaching
### The Fluorine Problem
Bastnäsite (REE·FCO₃) contains 5-10% fluorine. Direct acid leaching releases HF gas [@kim2025rare]:

$$
2\,\mathrm{REE}\cdot\mathrm{FCO_3} + 3\,\mathrm{H_2SO_4} \rightarrow
  \mathrm{REE_2(SO_4)_3} + 2\,\mathrm{HF}\uparrow + 2\,\mathrm{CO_2}\uparrow + 2\,\mathrm{H_2O}
$$

**Problems with HF**:

- Highly toxic (PEL = 3 ppm)
- Corrosive to equipment (requires specialized alloys)
- Environmental regulations restrict emission
- Causes fluorosis in surrounding areas

**Solution**: Pre-roasting to defluorinate [@chi2004recovery; @kim2025rare]

### Thermal Decomposition (Roasting)
#### Simple Calcination
**Process**: Heat bastnäsite in air [@kim2025rare]. Decarbonation to the
oxyfluoride comes first, between 300 and 500 °C:

$$
\mathrm{REE}\cdot\mathrm{FCO_3} \rightarrow \mathrm{REEOF} + \mathrm{CO_2}\uparrow
$$

Between 500 and 700 °C the oxyfluoride is hydrolysed to the oxide, which evolves
HF only if water vapour is present:

$$
2\,\mathrm{REEOF} + \mathrm{H_2O} \rightarrow \mathrm{REE_2O_3} + 2\,\mathrm{HF}\uparrow
$$

**Conditions**:

- Temperature: 500-700°C
- Time: 2-4 hours
- Atmosphere: Air or O₂-enriched

**Advantages**:

- Simple process
- No reagent addition
- Fluorine removed as HF (needs scrubbing)

**Disadvantages**:

- REE₂O₃ is highly refractory (difficult to leach)
- Requires concentrated H₂SO₄ at high temperature for dissolution
- HF emission requires treatment

#### Alkaline Roasting (Sodium Carbonate Process)
**Process**: Mix bastnäsite with Na₂CO₃, roast [@kim2025rare]

Step 1, defluorination at 400-500 °C:

$$
2\,\mathrm{REE}\cdot\mathrm{FCO_3} + \mathrm{Na_2CO_3} \rightarrow
  \mathrm{REE_2O_2CO_3} + 2\,\mathrm{NaF} + 2\,\mathrm{CO_2}\uparrow
$$

Step 2, complete decomposition at 700-900 °C:

$$
\mathrm{REE_2O_2CO_3} + \mathrm{Na_2CO_3} \rightarrow 2\,\mathrm{NaREEO_2} + 2\,\mathrm{CO_2}\uparrow
$$

**Conditions**:

- Temperature: 700-900°C
- Na₂CO₃:REO mass ratio: 1.5-2.5:1
- Time: 1-2 hours
- Atmosphere: Air

**Product**: NaREEO₂ (sodium rare earth oxide)

- Water soluble!
- Easy to dissolve

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

**Advantages**:

- Fluorine captured as NaF (solid, easier to handle than HF gas)
- Product more easily leached
- Lower acid consumption for subsequent leaching

**Disadvantages**:

- High Na₂CO₃ consumption (cost)
- NaF and Na₂SO₄ byproducts (disposal)
- Requires high temperature furnace

#### Ammonium Chloride Roasting (Fluorine Deactivation)
**Process developed by Chinese researchers** [@chi2004recovery]

$$
\mathrm{REE}\cdot\mathrm{FCO_3} + 3\,\mathrm{NH_4Cl} \rightarrow
  \mathrm{REECl_3} + \mathrm{NH_4F} + 2\,\mathrm{NH_3}\uparrow + \mathrm{CO_2}\uparrow + \mathrm{H_2O}
$$

**Conditions**:

- Temperature: 400-600°C
- NH₄Cl:bastnäsite molar ratio: 3-4:1
- Time: 1-2 hours

**Product**:

- REECl₃ (water soluble)
- NH₄F (ammonium fluoride, byproduct)

**Advantages**:

- Fluorine is deactivated rather than volatilised, which is the point of the
  route; whether the fluoride is recovered as a product or disposed of is a
  separate question this source does not settle
- REECl₃ directly water-soluble
- Lower temperature than Na₂CO₃ roasting
- NH₃ can be recycled

**Disadvantages**:

- NH₄Cl cost
- NH₃ emissions (need scrubbing)

### Acid Leaching of Roasted Bastnäsite
#### Sulfuric Acid Leaching
**After alkaline roasting** [@kim2025rare]:

The roasted material is REE₂O₃ or NaREEO₂, and it dissolves as the sulfate:

$$
\mathrm{REE_2O_3} + 3\,\mathrm{H_2SO_4} \rightarrow \mathrm{REE_2(SO_4)_3} + 3\,\mathrm{H_2O}
$$

**Conditions**:

- H₂SO₄ concentration: 2-6 M (20-60 wt%)
- Temperature: 60-95°C
- Time: 1-4 hours
- Solid:liquid ratio: 1:3 to 1:5 (w/v)
- Agitation: 200-400 rpm

**Leaching efficiency**:

- REE extraction: 90-98%
- Depends on roasting temperature (optimal 700-800°C)
- Over-roasting (\>900°C) reduces leaching (sintering)

#### Hydrochloric Acid Leaching

$$
\mathrm{REE_2O_3} + 6\,\mathrm{HCl} \rightarrow 2\,\mathrm{REECl_3} + 3\,\mathrm{H_2O}
$$

**Conditions**:

- HCl concentration: 4-8 M (15-30 wt%)
- Temperature: 60-90°C
- Time: 1-3 hours
- S/L ratio: 1:4 to 1:6

**Advantages**:

- Faster leaching than H₂SO₄
- Higher REE solubility
- Better for {index}`D2EHPA`/{index}`PC88A` solvent extraction (chloride medium)

**Disadvantages**:

- More corrosive (requires glass-lined or Ti equipment)
- HCl vapor emission issues
- Higher reagent cost

### Alternative: Supercritical CO₂ Extraction
**Emerging method** [@sinclair2017rare]

Roasted bastnäsite is contacted with supercritical CO₂ carrying a complexing
agent, which is what makes the rare earths CO₂-soluble at all.

**Conditions**: a single laboratory operating point, not a process window.
@sinclair2017rare work well above the CO₂ critical point (7.4 MPa, 31 °C) and
only modestly above ambient temperature, with an organophosphate — TBP and
relatives — as the complexing agent. The pressures and flows quoted for
supercritical extraction vary widely between studies and should be taken from
the specific study being cited rather than from a general band.

**Advantages**:

- "Green" solvent (CO₂)
- Lower temperature than traditional leaching
- Selective REE extraction
- No liquid waste

**Disadvantages**:

- High pressure equipment (expensive)
- Requires pre-roasting
- Lower extraction rates than aqueous leaching
- Not yet commercial scale

### Two Industrial Routes Compared: Mountain Pass and Bayan Obo

The two large bastnäsite operations chose opposite acids, and the choice
propagates all the way to the solvent extraction circuit. It is worth setting
them side by side, because the difference is often blurred in secondary
sources.

#### Mountain Pass (USA): oxidative roast, then HCl

The Molycorp route is a *chloride* route throughout
[@gupta2004extractive; @castor2006rare]:

1.  **Beneficiation**: flotation of the carbonatite ore to a bastnäsite
    concentrate of roughly 60 % REO.
2.  **Acid pre-leach**: dilute HCl dissolves the carbonate gangue — calcite and
    strontianite — upgrading the concentrate before it ever sees a furnace.
    This is a gangue-removal step, not a REE-dissolution step: the bastnäsite
    itself is barely touched by dilute acid at ambient temperature, and the
    barite is not touched at all.
3.  **Oxidative roast**: calcination in air at roughly 600 °C decomposes the
    fluorocarbonate and, critically, oxidises Ce(III) to Ce(IV). Cerium is
    close to half of the REE inventory in this ore, so this one step does the
    single largest separation in the flowsheet.
4.  **HCl leach**: the roasted material is leached with hydrochloric acid. The
    trivalent rare earths dissolve as REECl₃; Ce(IV) does not, and stays in
    the residue as a cerium concentrate. The leach liquor is therefore already
    cerium-depleted before solvent extraction begins.
5.  **Purification and hand-off**: pH adjustment to precipitate Fe(OH)₃,
    filtration, and the resulting mixed REE chloride solution goes directly to
    the solvent extraction cascade — no medium conversion is required, because
    the circuit never left chloride.

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

1.  Mix the concentrate with concentrated H₂SO₄ and roast at 400-600 °C. The
    rare earths convert to water-soluble sulfates; fluorine leaves as HF (and
    SiF₄ if silica is present), which is the reason the route needs a serious
    off-gas train.
2.  Water-leach the calcine to dissolve REE₂(SO₄)₃.
3.  Precipitate as double sulfate or hydroxide, then redissolve in HCl if a
    chloride feed is wanted for the extraction circuit.

The sulfuric route tolerates a lower-grade, more variable concentrate and does
not require the cerium oxidation step; it pays for that with fluorine and
sulfate management, and with the extra precipitation-redissolution cycle if
the downstream extractant wants chloride.

## Monazite Processing: Phosphate Decomposition
### The Phosphate and Thorium Problems
Monazite ((REE,Th)PO₄) presents two major challenges [@borai2016modified; @amaral2010thorium]:

1.  **Refractory phosphate matrix**:
    - Very stable REE-PO₄ bonds
    - Resistant to acid attack at ambient conditions
    - Requires harsh conditions or pre-treatment
2.  **Radioactive thorium** (0.1-12 wt% ThO₂):
    - Regulatory restrictions on processing
    - Many countries banned monazite processing
    - Requires thorium separation and disposal

### Acid Leaching Methods
#### Sulfuric Acid Digestion (Classical Method)
**Process** [@jha2016hydrometallurgical]:

$$
2\,\mathrm{REEPO_4} + 3\,\mathrm{H_2SO_4} \rightarrow \mathrm{REE_2(SO_4)_3} + 2\,\mathrm{H_3PO_4}
$$

$$
\mathrm{Th_3(PO_4)_4} + 6\,\mathrm{H_2SO_4} \rightarrow 3\,\mathrm{Th(SO_4)_2} + 4\,\mathrm{H_3PO_4}
$$

**Conditions**:

- Concentrated H₂SO₄: 93-98 wt%
- Temperature: 200-250°C (high!)
- Time: 2-8 hours
- Monazite:H₂SO₄ ratio: 1:1.5 to 1:2 (w/w)

**Process details**:

1.  Mix ground monazite with concentrated H₂SO₄
2.  Heat in cast iron vessel or glass-lined reactor
3.  Temperature increases exothermically to 200-250°C
4.  Cool, add water to dissolve sulfates
5.  Filter to remove insoluble residues

**Leaching efficiency**:

- REE extraction: 90-98%
- Th co-extracted
- Phosphate remains as H₃PO₄ in solution

**Challenges**:

- Very corrosive conditions (hot concentrated acid)
- High energy requirement
- Phosphate removal needed (gypsum {index}`precipitation`)
- Thorium separation required

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

**Conditions**:

- HNO₃: 6-10 M
- Temperature: 100-150°C
- Time: 4-8 hours

**Advantages**:

- Nitrate medium suitable for TBP extraction
- Easier thorium separation (TBP preferentially extracts Th)

### Alkaline Decomposition Methods
#### Sodium Hydroxide Digestion
**Process** [@xu2012decomposition; @shahreldin2018selective]:

Step 1, alkaline digestion at 140-150 °C in 60-70 wt% NaOH at atmospheric
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

**Conditions for NaOH digestion**:

- NaOH concentration: 60-70 wt% (a hot caustic melt-slurry, not a dilute solution)
- NaOH:monazite ratio: 3-5:1 (w/w)
- Temperature: 140-150 °C at **atmospheric pressure**
- Time: 2-6 hours
- Particle size: below ~45 μm; the reaction is topochemical and coarse grains
  do not fully decompose
- Product: mixed hydroxides + Na₃PO₄ solution

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

**Advantages** [@shahreldin2018selective]:

- Separates phosphate (as soluble Na₃PO₄)
- REE/Th hydroxides easily leached with dilute acid
- Lower acid consumption than direct acid leaching
- Phosphate recovered for fertilizer use

**Disadvantages**:

- High NaOH consumption
- Thorium still co-precipitates with REE

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

**Conditions**:

- Temperature: 800-900°C
- Time: 1-2 hours
- Na₂CO₃:monazite ratio: 2:1 to 3:1

### Modified Leaching for Thorium Separation
**Selective thorium extraction** [@borai2016modified]:

Strategy: Exploit different solubilities in specific conditions

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

**TBP extraction** (from HNO₃ medium):

- 30% TBP in kerosene
- Th(NO₃)₄ very soluble in TBP
- REE(NO₃)₃ less soluble
- Efficient Th/REE separation

#### Ion Exchange

- Strong acid cation resin
- Th⁴⁺ more strongly retained than REE³⁺
- Elute REE with dilute HCl
- Elute Th with stronger acid or EDTA

### Industrial Practice
**Indian Rare Earths Ltd (IREL)** [@jha2016hydrometallurgical]:

1.  Beach sand mining (monazite placers)
2.  Gravity + magnetic + electrostatic separation
3.  Sulfuric acid digestion (220°C, concentrated H₂SO₄)
4.  Water leaching, filtration
5.  Thorium extraction with amine extractants
6.  REE precipitation as hydroxides or carbonates
7.  Redissolve for individual REE separation

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

**Conditions**:

- (NH₄)₂SO₄ concentration: 2-5 wt%
- Temperature: ambient (15-25°C)
- Contact time: 2-8 hours
- pH: 4-6

Contacting is either **in situ** — lixiviant injected through wells drilled into
the orebody, pregnant leach solution collected downslope, and no ore mined at
all — or **heap leaching** of excavated ore crushed to 5-20 mm, heaped 2-5 m
deep on an impermeable pad, drip-irrigated at 5-10 L/(m²·h) and drained over a
residence time of 20-100 days. Either way the pregnant leach solution (PLS) is
dilute: 200-1000
mg/L REE at pH 4-6, with Al, Fe and Ca as the impurities that matter. That
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
alternatives are magnesium sulfate at 1-3 wt%,

$$
\mathrm{Clay}\text{-}\mathrm{REE^{3+}} + 1.5\,\mathrm{MgSO_4} \rightarrow
  \mathrm{Clay}\text{-}\mathrm{Mg_{1.5}} + \mathrm{REE^{3+}} + 1.5\,\mathrm{SO_4^{2-}}
$$

which carries no nitrogen and is a somewhat weaker competitor for the exchange
sites, needing 1.5 mol of divalent Mg²⁺ per mole of REE³⁺ against 3 mol of NH₄⁺
[@xiao2015leaching; @pan2024insights]; ferrous sulfate, which adds a reducing
environment that helps mobilise cerium [@xiao2016reduction]; sodium chloride,
environmentally the mildest of all but weaker (60-75 % recovery) and needing
higher concentrations; and organic acids such as citric, which combine
complexation with exchange at higher reagent cost [@wang2017effects].
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
### Challenges
Xenotime (YPO₄) is the most refractory REE mineral [@hung2020separation]:

- Very stable Y-O-P bonds
- Higher crystallinity than monazite
- Heavy REEs (higher charge density, stronger bonds)

### Leaching Methods
Similar to monazite but requires more severe conditions:

**Concentrated H₂SO₄ digestion**:

- Temperature: 250-300°C (higher than monazite)
- H₂SO₄: 95-98%
- Time: 6-12 hours
- Extraction: 85-95%

**Alkaline decomposition**:

- NaOH at 180-220°C, 4-8 hours
- More effective than acid for xenotime

### Thorium and Uranium Co-extraction
Xenotime often contains [@hung2020separation]:

- ThO₂: 0.1-3%
- U₃O₈: 0.5-5%

Requires similar separation strategies as monazite.

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
From leaching [@jha2016hydrometallurgical]:

| Impurity | Source                  | Typical Conc. | Issue                       |
|----------|-------------------------|---------------|-----------------------------|
| Fe³⁺     | Gangue iron oxides      | 1-10 g/L      | Co-extracts, colors product |
| Al³⁺     | Clay minerals           | 0.5-5 g/L     | Co-extracts                 |
| Ca²⁺     | Calcite, dolomite       | 2-20 g/L      | Sulfate precipitation       |
| Th⁴⁺     | Monazite/xenotime       | 0.1-5 g/L     | Radioactive, must remove    |
| PO₄³⁻    | Phosphate minerals      | 5-50 g/L      | Precipitates REE, foaming   |
| F⁻       | Bastnäsite (if present) | 0.1-2 g/L     | Corrosion, precipitates REE |

### Iron Removal
**pH adjustment method** (most common):

$$
\mathrm{Fe^{3+}} + 3\,\mathrm{H_2O} \rightleftharpoons \mathrm{Fe(OH)_3}\downarrow + 3\,\mathrm{H^+}
$$

**Conditions**:

- Add NaOH or NH₄OH to increase pH
- Target pH: 3.5-4.5 (Fe precipitates, REE remain soluble)
- Temperature: 60-80°C (improves settling)
- Time: 1-2 hours

**Performance**:

- Fe removal: \>99%
- REE loss: \<2% (if pH controlled)

**Alternative: Oxidation-precipitation**:

- If Fe²⁺ present, oxidize to Fe³⁺ first (air, H₂O₂)
- Then pH adjustment

### Aluminum Removal
More challenging than Fe (Al(OH)₃ soluble at low and high pH):

**Selective precipitation**:

- pH 4.5-5.5: Al(OH)₃ precipitates
- REE remain soluble (precipitate at pH 6-8)
- Narrow operating window

**Alternative: Solvent extraction**:

- Some extractants selective against Al
- Or preferential REE extraction leaves Al in raffinate

### Calcium Removal
**Sulfate precipitation** (if H₂SO₄ leach):

$$
\mathrm{Ca^{2+}} + \mathrm{SO_4^{2-}} \rightarrow \mathrm{CaSO_4}\downarrow \quad \text{(gypsum)}
$$

- Occurs naturally during leaching
- Filter to remove

**Carbonate precipitation**:

$$
\mathrm{Ca^{2+}} + \mathrm{CO_3^{2-}} \rightarrow \mathrm{CaCO_3}\downarrow
$$

### Thorium Removal
**Solvent extraction** [@amaral2010thorium]:

- Before REE extraction
- An amine from sulfate liquor, or TBP from nitrate
- Th extracts preferentially
- See [](#thorium-management)

**Selective precipitation**:

- pH 4-5: Th(OH)₄ precipitates
- REE remain soluble

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

**Precipitation as FePO₄**:

- If Fe present, FePO₄ precipitates
- Remove during Fe removal step

### Purified Solution Specification
**Target composition for solvent extraction feed**:

| Parameter | Typical Value         |
|-----------|-----------------------|
| Total REE | 0.5-2.0 M             |
| Free acid | 0.1-1.0 M             |
| Fe        | \<100 ppm             |
| Al        | \<500 ppm             |
| Ca        | \<1000 ppm            |
| Th        | \<10 ppm (regulated)  |
| PO₄³⁻     | \<500 ppm             |
| Clarity   | \<100 NTU (turbidity) |

This solution is the feed for the solvent extraction circuit described in
[](#solvent-extraction-fundamentals).

## Complete Process Flowsheets

Everything above comes together in [](#fig-leaching-flowsheet), which puts the
routes on one grid rather than drawing each separately. Side by side they show
something none of them shows alone: the routes differ only in how the mineral is
*cracked*. From the leach onward they converge on a single purified liquor with
a single specification, and that liquor is what
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
#### Acid Leaching
**Temperature effect**:

- Arrhenius relationship: k = A exp(-$E_\mathrm{a}$/RT)
- Typical $E_\mathrm{a}$: 40-80 kJ/mol (diffusion-controlled)
- Doubling temperature → 2-5× faster leaching
- But: equipment limits, energy cost

**Acid concentration**:

- Higher \[H⁺\] → faster kinetics
- Optimal depends on mineral:
  - Bastnäsite (roasted): 2-6 M H₂SO₄
  - Monazite: 6-12 M H₂SO₄ or HCl
- Excess acid wasteful, increases neutralization cost

**Particle size**:

- Smaller particles → faster leaching (higher surface area)
- But: grinding cost, filtration difficulty
- Optimal: 100-200 μm for most applications

**Solid/liquid ratio**:

- Lower S/L → better mass transfer
- But: larger vessels, more water
- Typical: S/L = 1:3 to 1:5 (w/v)

**Agitation**:

- Maintain particles in suspension
- Typical: 200-400 rpm
- Too high → attrition, emulsions

#### Roasting
**Temperature**:

- Underroasting → incomplete decomposition
- Overroasting → sintering (reduced leaching)
- Optimal: 700-800°C for most REE minerals

**Time**:

- Sufficient for complete reaction
- Typical: 1-2 hours
- Depends on particle size, bed depth

**Atmosphere**:

- Air vs. O₂-enriched vs. inert
- Oxidizing for sulfide-containing ores
- Reducing for selective Ce oxidation

(leaching-kinetics-models)=
### Leaching Kinetics Models
#### Shrinking Core Model

For solid particle dissolution [@long2019kinetics]:

**Three steps**:

1.  Diffusion through solution film (external)
2.  Reaction at solid surface
3.  Diffusion through product layer (internal)

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

**Determining rate-limiting step**:

- Plot both equations
- Linear fit indicates controlling mechanism
- Most REE leaching: diffusion-controlled

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

**High-pressure leaching**:

- Autoclaves allow higher temperature
- Faster kinetics
- Requires pressure vessels

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
contained REO that survives to product. Every figure below is computed that way
from grades and recoveries stated elsewhere in this chapter; none is taken from
a secondary compilation.

**Leach feed, per tonne of REO:**

| Ore type       | Basis           | Grade (REO)  | Recovery | Feed per t REO |
|----------------|-----------------|--------------|----------|----------------|
| Bastnäsite     | **concentrate** | 60-75 %      | 90-98 %  | 1.4-1.9 t      |
| Monazite       | **concentrate** | 50-70 %      | 85-95 %  | 1.5-2.4 t      |
| Ion-adsorption | **ore**         | 0.05-0.3 %   | 80-95 %  | 350-2,500 t    |

Worked, so the reader can check it: a bastnäsite concentrate at the bottom of
its grade range and the bottom of its recovery range needs
1/(0.60 × 0.90) = 1.85 t per tonne of REO, and at the top of both,
1/(0.75 × 0.98) = 1.36 t. An ion-adsorption ore at 0.3 % REO leached at 95 %
recovery needs 1/(0.003 × 0.95) = 351 t; the same calculation at 0.05 % and 80 %
gives 1/(0.0005 × 0.80) = 2,500 t. Three orders of magnitude separate the two
feeds, which is the single most important fact about ion-adsorption mining and
the reason its environmental footprint is a land-and-groundwater problem rather
than a reagent problem.

**Ore behind the concentrate.** For bastnäsite, the chapter's own flotation
numbers — a 10-30 % REO flotation feed recovered at 70-90 % — put the mined ore
at 1/(0.10 × 0.70 × 0.90) = 16 t down to 1/(0.30 × 0.90 × 0.98) = 3.8 t per
tonne of REO, so roughly **4-16 t of ore**, with the difference between that and
the 1.4-1.9 t of concentrate reporting to the flotation tailings pond. For
monazite the question is not well posed: beach placers are mined for ilmenite,
rutile and zircon, and monazite is recovered as a minor byproduct of a
separation that would happen anyway, so attributing a placer ore tonnage to the
rare earths is an allocation choice, not a measurement.

**Reagents.** Two of the three follow from stoichiometry:

- *Bastnäsite, sulfuric route.* REE₂O₃ + 3 H₂SO₄ gives 3 × 98 / 328 = 0.90 t of
  H₂SO₄ per tonne of REO as a floor. Real consumption is higher, by an amount
  set by the carbonate gangue, which is why the HCl pre-leach that removes
  calcite before the roast pays for itself.
- *Monazite.* The digestion recipe in this chapter is 1.5-2 parts H₂SO₄ per part
  of concentrate by weight, which on 1.5-2.4 t of concentrate is **2.3-4.8 t of
  H₂SO₄** per tonne of REO. This is a genuinely large number and it is the main
  argument for the caustic route.
- *Ion-adsorption.* Displacing REE³⁺ takes three equivalents of NH₄⁺, so
  1.5 mol of (NH₄)₂SO₄ per mol of REE. A tonne of REO is about 6.1 kmol of REE
  (Ln₂O₃ ≈ 330 g/mol), giving 9.2 kmol × 132 g/mol = **1.2 t of (NH₄)₂SO₄ as a
  stoichiometric minimum**, and practice uses a multiple of that because the
  exchange is an equilibrium against the clay's whole cation exchange capacity,
  not just its rare earth loading. Figures below 1.2 t are below the
  thermodynamic floor and cannot be right.

**Solution volumes.** For the acid routes, a solid-to-liquid ratio of 1:3 to 1:5
on 1.4-2.4 t of concentrate gives **4-12 m³** of leach liquor per tonne of REO.
For ion-adsorption ore the volume is set by the pregnant leach solution
concentration instead: at 200-1,000 mg/L REE, a tonne of REO is dissolved in
**1,000-5,000 m³**. Cross-checking against the ore tonnage at a typical
liquid-to-solid ratio of 1-2 m³/t gives 350-5,000 m³, which agrees. Most of that
volume is recirculated rather than discharged, but it is all in contact with the
ore body and all of it is a containment problem.

**Solid residues.** The acid routes leave 0.4-0.9 t (bastnäsite) and 0.5-1.4 t
(monazite) of leach residue per tonne of REO, simply as the difference between
concentrate in and REO dissolved, plus any gypsum precipitated to fix phosphate.
The monazite residue carries the thorium and is the regulated stream. The
ion-adsorption case has no leach residue in the usual sense and is often
tabulated as "minimal", which is misleading: the solid left behind is the entire
350-2,500 t of ore, either in place after in-situ leaching or as a spent heap,
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
**Deep eutectic solvents (DES)**:

- Mixtures of a hydrogen-bond acceptor (typically a quaternary ammonium salt)
  and a hydrogen-bond donor, liquid well below the melting points of either
- Low vapour pressure, tunable, in principle recyclable
- The demonstrated rare-earth-adjacent application is **thorium**, not the rare
  earths: Ni and co-workers used a hydrophobic DES to extract Th selectively
  from a radioactive waste leachate [@ni2023sustainable], which is the impurity
  problem monazite processing has rather than the separation problem
- Cost, viscosity and the difficulty of stripping the loaded phase currently
  limit application

**Ionic liquids**: task-specific ionic liquids can in principle combine the
leach and the extraction in one liquid, at the price of cost and scale-up.
[](#biological-and-biomimetic-separations) covers them alongside deep eutectic
solvents as green solvent systems, and
[](#environment-techno-economics-and-life-cycle) weighs the environmental claim.

### Process Integration
**Combined roasting-leaching**:

- Single-step process
- Reduced equipment and energy
- Under development

**Leaching + solvent extraction** [@liu2017enrichment]:

- Direct extraction from lean leach solutions
- Eliminates precipitation step
- Higher extractant consumption

### Selective Leaching
**Targeted dissolution** [@he2025stepwise]:

- Multi-stage leaching with different conditions
- Separate REE from major impurities
- Reduces purification cost

**Electrochemical-assisted leaching**:

- Apply potential during leaching
- Selective oxidation/reduction
- Enhanced kinetics
- Research stage

### Artificial Intelligence and Process Control
**Machine learning optimization**:

- Predict optimal conditions for new ore batches
- Real-time process adjustment
- Still prospective for leaching; the demonstrated applications of machine
  learning in this book are in extractant design and separation modelling
  rather than in plant control

**Automated monitoring**:

- In-line sensors for REE, pH, impurities
- Closed-loop control
- Consistent product quality

Where closed-loop control of a rare-earth operation *has* been demonstrated is
downstream, on the solvent-extraction cascade rather than on the leach; see
[](#process-modeling-and-optimization).

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

| Ore Type | Pre-treatment | Leaching Method | Conditions | REE Recovery | Major Challenge |
|----|----|----|----|----|----|
| Bastnäsite | Roasting (700°C) | H₂SO₄ or HCl | 2-6M, 60-90°C, 2-4h | 90-98% | Fluorine emissions |
| Monazite | Optional alkali roast | Conc. H₂SO₄ (220°C) | 93%, 220°C, 4-8h | 85-95% | Thorium separation |
| Xenotime | Alkali roast preferred | H₂SO₄ or NaOH (high T) | 250-300°C, 6-12h | 80-95% | Very refractory |
| Ion-adsorption | None | (NH₄)₂SO₄ or MgSO₄ | 2-5%, ambient, 4-8h | 80-95% | Ammonia pollution |
| Bioleaching (all) | None | Microbial organic acids | Ambient, weeks | Not established; mg/L liquors in the published monazite work | Slow kinetics, dilute liquor |

### On Cost Comparisons

Operating costs per tonne of REO are not tabulated here. They are dominated by
site-specific quantities — ore grade, labour rate, energy price, reagent
logistics, the disposal regime for thorium, and above all the value of the
particular basket of rare earths a given ore yields — and a cost table that
omits those is not a comparison of processes but a comparison of assumptions.
What can be said structurally, from the reagent arithmetic above, is that the
sulfuric monazite route buys its high recovery with 2-5 t of acid per tonne of
REO plus a regulated radioactive residue, that the bastnäsite chloride route
spends its money on the roast, and that the ion-adsorption route spends almost
nothing on reagents or energy and almost everything on land, water and
remediation. Techno-economics is treated in
[](#environment-techno-economics-and-life-cycle).

## Conclusions and Recommendations
### Key Findings
1.  **Ore-specific processing is essential**:
    - Bastnäsite: Requires defluorination (roasting) before acid leaching
    - Monazite: Needs thorium management; alkaline pre-treatment advantageous
    - Ion-adsorption clays: Mild salt leaching at ambient conditions
2.  **Leaching chemistry sets the shape of the process economics**:
    - Reagent consumption is fixed by stoichiometry and gangue, and for the
      monazite sulfuric route it is several tonnes of acid per tonne of REO
    - The roast, where there is one, is the energy-intensive step
    - Waste treatment is a significant cost component, and for ion-adsorption
      ore it is most of the cost
3.  **Environmental challenges drive innovation**:
    - Fluorine capture from bastnäsite
    - Ammonia-free leaching for ion-adsorption ores
    - Bioleaching as green alternative (but slow)
4.  **Industrial practice is mature but evolving**:
    - Established flowsheets for major ore types
    - Incremental improvements in efficiency
    - New methods (DES, ionic liquids) not yet commercial

(research-gaps)=
### Research Gaps
1.  **Selective leaching**:
    - Separate REEs from gangue in single step
    - Reduce acid consumption
    - Minimize waste generation
2.  **Refractory ore processing**:
    - More efficient xenotime decomposition
    - Lower energy roasting methods
    - Alternative to high-temperature acid digestion
3.  **Bioleaching scale-up**:
    - Faster kinetics (strain engineering)
    - Process intensification
    - Economic analysis at industrial scale
4.  **Closed-loop processes**:
    - Reagent recycling
    - Water reuse
    - Zero-discharge systems

## The Feed Handed to Solvent Extraction

After leaching and purification, a typical purified liquor arriving at the
solvent extraction circuit looks like this [@jha2016hydrometallurgical]:

- **REE concentration**: 0.5-2.0 M (total mixed REEs)
- **Acid medium**: chloride (from HCl) or nitrate (from HNO₃)
- **pH**: 0.5-2.0
- **Temperature**: ambient to 40 °C
- **Major impurities**: Fe (\<100 ppm), Al (\<500 ppm), Ca (\<1000 ppm)

Turning that liquor into separated products means adjusting the pH into the
extraction range (2.5-4.0) with base and contacting it with an organic phase —
D2EHPA, PC88A, or TBP in kerosene. [](#solvent-extraction-fundamentals) takes
the story from there.

The choice of acid in leaching is not independent of the extractant chosen
downstream, which is the main reason the two steps have to be designed together:

- A chloride medium suits D2EHPA and PC88A.
- A nitrate medium suits TBP.
- Ion-adsorption leachates arrive as sulfates and may need conversion.

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
