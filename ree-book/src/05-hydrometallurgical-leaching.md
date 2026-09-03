---
title: Hydrometallurgical Leaching
---

(hydrometallurgical-leaching)=
# Hydrometallurgical Leaching

Leaching converts solid rare earth minerals into dissolved ions, and it is the
step that decides what the {index}`solvent extraction` circuit downstream will have to
cope with. Which method works depends almost entirely on mineralogy: {index}`bastnasite <bastnäsite>`,
{index}`monazite`, {index}`xenotime`, and {index}`ion-adsorption clays <ion-adsorption clay>` each demand a different strategy,
because each locks its rare earths behind a different chemical barrier — a
fluorocarbonate lattice, a refractory phosphate, a {index}`thorium` burden, or nothing
more than an exchangeable surface site. This chapter follows the flowsheet from
run-of-mine ore through beneficiation, decomposition, leaching, and impurity
removal, ending at the purified aqueous feed that
[](#solvent-extraction-fundamentals) takes as its starting point.

Four themes recur. Bastnasite must be defluorinated, normally by roasting,
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

1.  **Bastnasite** (REE·FCO₃) - Carbonate-fluoride
    - Composition: (Ce,La,Nd,Pr)CO₃F
    - REO content: 60-75%
    - Light REE enriched (La, Ce, Pr, Nd)
    - Major source: {index}`Mountain Pass` (USA), {index}`Bayan Obo` (China)
    - Challenge: Fluorine content requires defluorination
2.  **Monazite** ((REE,Th)PO₄) - Phosphate
    - Composition: (Ce,La,Nd,Th)PO₄
    - REO content: 50-70%
    - Contains 0-12% ThO₂ (radioactive)
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
The general hydrometallurgical flowsheet [@jha2016hydrometallurgical; @kim2025rare]:

``` example
Mining
  ↓
Beneficiation (crushing, grinding, flotation, magnetic separation)
  ↓
Pre-treatment (roasting, calcination) ← [if needed for bastnasite/monazite]
  ↓
Leaching (acid or alkali)
  ↓
Solid-liquid separation (filtration, settling)
  ↓
Purification (remove Fe, Th, Ca, Al, etc.)
  ↓
Solvent Extraction (REE separation)
  ↓
Product (individual REE oxides or mixed REO)
```

**This chapter covers steps 2-5**: beneficiation through purification, which produce the aqueous REE feed for solvent extraction.

### Challenges in REE Ore Processing
1.  **Refractory nature**: REE minerals resist decomposition [@kim2025rare]
    - Strong REE-O, REE-P, REE-F bonds
    - High thermal stability
    - Resistant to acid attack
2.  **Fluorine in bastnasite**: Environmental concern [@chi2004recovery]
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
Before leaching, physical separation methods concentrate REEs from gangue [@jordens2013processing; @chelgani2015rare].

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

- Bastnasite: 4.9-5.2 g/cm³
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
- Bastnasite: Weakly paramagnetic
- Gangue: Typically diamagnetic or weakly paramagnetic

**Equipment**:

1.  Low-intensity magnetic separator (LIMS): Remove magnetite, hematite
2.  High-intensity magnetic separator (HIMS): Concentrate paramagnetic REE minerals
3.  High-gradient magnetic separator (HGMS): Fine particle separation

**Industrial application**:

- Bayan Obo (China): Magnetic separation of bastnasite-magnetite ore
- Recovery: 70-85%

### Froth Flotation
**Most important beneficiation method** for bastnasite and monazite [@chelgani2015rare; @jordens2013processing]

#### Bastnasite Flotation
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

**Performance** [@jordens2013processing]:

- REE recovery: 70-90%
- Grade: 60-75% REO (from 10-30% feed)
- Requires multiple stages (rougher, scavenger, cleaner)

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

**Mountain Pass (USA) beneficiation** [@kim2025rare]:

- Feed: 7-9% REO bastnasite ore
- Crushing → grinding → flotation (3 stages)
- Product: 60% REO concentrate
- Recovery: 70%

## Bastnasite Processing: Roasting and Leaching
### The Fluorine Problem
Bastnasite (REE·FCO₃) contains 5-10% fluorine. Direct acid leaching releases HF gas [@kim2025rare]:

    2 REE·FCO₃ + 3 H₂SO₄ → REE₂(SO₄)₃ + 2 HF↑ + 2 CO₂↑ + 2 H₂O

**Problems with HF**:

- Highly toxic (PEL = 3 ppm)
- Corrosive to equipment (requires specialized alloys)
- Environmental regulations restrict emission
- Causes fluorosis in surrounding areas

**Solution**: Pre-roasting to defluorinate [@chi2004recovery; @kim2025rare]

### Thermal Decomposition (Roasting)
#### Simple Calcination
**Process**: Heat bastnasite in air [@kim2025rare]

    Temperature progression:

    300-500°C:   REE·FCO₃ → REEOF + CO₂↑
                 (Decarbonation to the oxyfluoride)

    500-700°C:   2 REEOF + H₂O → REE₂O₃ + 2 HF↑
                 (Steam hydrolysis; HF evolves only if water vapour is present)

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
**Process**: Mix bastnasite with Na₂CO₃, roast [@xu2012decomposition; @kim2025rare]

    Step 1 (400-500°C): Defluorination
    2 REE·FCO₃ + Na₂CO₃ → REE₂O₂CO₃ + 2 NaF + 2 CO₂↑

    Step 2 (700-900°C): Complete decomposition
    REE₂O₂CO₃ + Na₂CO₃ → 2 NaREEO₂ + 2 CO₂↑

**Conditions**:

- Temperature: 700-900°C
- Na₂CO₃:REO mass ratio: 1.5-2.5:1
- Time: 1-2 hours
- Atmosphere: Air

**Product**: NaREEO₂ (sodium rare earth oxide)

- Water soluble!
- Easy to dissolve

**Water leaching of roasted product**:

    NaREEO₂ + H₂O → NaOH + REEO(OH) (hydrated oxide)
    REEO(OH) + 3 HCl → REECl₃ + 2 H₂O

    Or direct acid dissolution:
    2 NaREEO₂ + 4 H₂SO₄ → REE₂(SO₄)₃ + Na₂SO₄ + 4 H₂O

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

    REE·FCO₃ + 3 NH₄Cl → REECl₃ + NH₄F + 2 NH₃↑ + CO₂↑ + H₂O

    Temperature: 400-600°C
    NH₄Cl:bastnasite molar ratio: 3-4:1
    Time: 1-2 hours

**Product**:

- REECl₃ (water soluble)
- NH₄F (ammonium fluoride, byproduct)

**Advantages**:

- Fluorine captured as NH₄F (can be recovered for HF production)
- REECl₃ directly water-soluble
- Lower temperature than Na₂CO₃ roasting
- NH₃ can be recycled

**Disadvantages**:

- NH₄Cl cost
- NH₃ emissions (need scrubbing)

### Acid Leaching of Roasted Bastnasite
#### Sulfuric Acid Leaching
**After alkaline roasting** [@kim2025rare]:

    Roasted material: REE₂O₃ or NaREEO₂

    Leaching:
    REE₂O₃ + 3 H₂SO₄ → REE₂(SO₄)₃ + 3 H₂O

    Conditions:
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
    REE₂O₃ + 6 HCl → 2 REECl₃ + 3 H₂O

    Conditions:
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

    Roasted bastnasite + scCO₂ + complexing agent

    Conditions:
    - Pressure: 10-30 MPa
    - Temperature: 40-80°C
    - Complexing agent: {index}`TBP <TBP (tributyl phosphate)>`, organophosphates
    - CO₂ flow rate: 1-5 mL/min

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

The two large bastnasite operations chose opposite acids, and the choice
propagates all the way to the solvent extraction circuit. It is worth setting
them side by side, because the difference is often blurred in secondary
sources.

#### Mountain Pass (USA): oxidative roast, then HCl

The Molycorp route is a *chloride* route throughout
[@gupta2004extractive; @castor2006rare]:

1.  **Beneficiation**: flotation of the carbonatite ore to a bastnasite
    concentrate of roughly 60 % REO.
2.  **Acid pre-leach**: dilute HCl dissolves the carbonate gangue — calcite and
    strontianite — upgrading the concentrate before it ever sees a furnace.
    This is a gangue-removal step, not a REE-dissolution step: the bastnasite
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

The sulfuric route is the Chinese practice for bastnasite and mixed
bastnasite-monazite concentrates [@kim2025rare]:

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

    2 REEPO₄ + 3 H₂SO₄ → REE₂(SO₄)₃ + 2 H₃PO₄

    Th₃(PO₄)₄ + 6 H₂SO₄ → 3 Th(SO₄)₂ + 4 H₃PO₄

    Conditions:
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

Hydrochloric acid, which handles roasted bastnasite easily, does not attack
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
Used in some processes [@borai2016modified]:

    REEPO₄ + 3 HNO₃ → REE(NO₃)₃ + H₃PO₄

    Th₃(PO₄)₄ + 12 HNO₃ → 3 Th(NO₃)₄ + 4 H₃PO₄

    Conditions:
    - HNO₃: 6-10 M
    - Temperature: 100-150°C
    - Time: 4-8 hours

**Advantages**:

- Nitrate medium suitable for TBP extraction
- Easier thorium separation (TBP preferentially extracts Th)

### Alkaline Decomposition Methods
#### Sodium Hydroxide Digestion
**Process** [@borai2016modified; @shahreldin2018selective]:

    Step 1: Alkaline digestion (140-150°C, 60-70 wt% NaOH, atmospheric pressure)
    REEPO₄ + 3 NaOH → REE(OH)₃ + Na₃PO₄
    Th₃(PO₄)₄ + 12 NaOH → 3 Th(OH)₄ + 4 Na₃PO₄

    Step 2: Water leaching
    Na₃PO₄ dissolves (remove phosphate)
    REE(OH)₃ and Th(OH)₄ remain as solids

    Step 3: Acid leaching of hydroxides
    REE(OH)₃ + 3 HCl → REECl₃ + 3 H₂O

    Th(OH)₄ + 4 HCl → ThCl₄ + 4 H₂O

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
Similar to bastnasite [@xu2012decomposition]:

    2 REEPO₄ + 3 Na₂CO₃ → REE₂O₃ + 2 Na₃PO₄ + 3 CO₂↑

    Th₃(PO₄)₄ + 6 Na₂CO₃ → 3 ThO₂ + 4 Na₃PO₄ + 6 CO₂↑

    Temperature: 800-900°C
    Time: 1-2 hours
    Na₂CO₃:monazite ratio: 2:1 to 3:1

### Modified Leaching for Thorium Separation
**Selective thorium extraction** [@borai2016modified]:

Strategy: Exploit different solubilities in specific conditions

**Method 1: Low-temperature H₂SO₄**

- 2-4 M H₂SO₄, 40-60°C, 4 hours
- Preferentially dissolves thorium (5-15% Th extraction)
- REEs remain in solid (refractory)
- Follow with high-T leaching for REE

**Method 2: Alkaline decomposition + selective dissolution** [@shahreldin2018selective]:

1.  NaOH digest → mixed hydroxides
2.  Dissolve in dilute HCl or HNO₃
3.  Adjust pH to precipitate Th(OH)₄ (pH 4-5)
4.  REEs remain in solution (precipitate at higher pH 6-8)

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

- Extractant: a **primary** amine (Primene JM-T) in kerosene, applied directly
  to monazite sulfuric acid liquor. Amaral and Morais report Th and U
  extraction with rare earths left in the raffinate.
- Amine class matters and is often misreported. Primary (Primene JM-T),
  secondary (Amberlite LA-2) and tertiary (**Alamine 336**, a
  tri-C₈/C₁₀-alkylamine, not a primary amine) amines have different basicities
  and different affinities for the sulfato complexes; the primary amines are
  the ones used industrially for Th/U from sulfate.
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

**Production**: \~3000 tons/year REO (historical)

(ion-adsorption-clay-leaching-the-gentle-approach)=
## Ion-Adsorption Clay Leaching: The Gentle Approach
### Unique Mineralogy
Ion-adsorption deposits in Southern China [@shi2022column; @long2019kinetics]:

**Formation**:

- Weathering of granite with REE-bearing minerals
- REEs released and adsorbed on clay surfaces
- No crystalline REE minerals present

**REE form**:

    Clay−[REE³⁺]_adsorbed   (exchangeable cations)

**Characteristics**:

- Very low grade: 0.05-0.3% REO
- Enriched in heavy REEs (Y, Dy, Tb, Eu)
- Strategic importance: these deposits supply over 90 % of the world's
  heavy rare earths [@zhou2020genesis]
- Easy to leach (no roasting needed!)

### In-Situ Leaching Process
**Principle**: Ion exchange with leaching agent [@shi2022column; @long2019kinetics]

    Clay−[REE³⁺] + 3 NH₄⁺ ⇌ Clay−[NH₄⁺]₃ + REE³⁺(aq)

#### Ammonium Sulfate Leaching (Traditional)
**Process** [@shi2022column]:

    Clay−[REE³⁺] + 1.5 (NH₄)₂SO₄ → Clay−[(NH₄⁺)]₃ + REE³⁺ + 1.5 SO₄²⁻

    Conditions:
    - (NH₄)₂SO₄ concentration: 2-5 wt%
    - Temperature: Ambient (15-25°C)
    - Contact time: 2-8 hours
    - pH: 4-6

**In-situ application**:

1.  Drill injection wells into ore body
2.  Inject dilute (NH₄)₂SO₄ solution
3.  Solution percolates through ore
4.  Collect pregnant leach solution from collection wells
5.  Process solution to recover REE

**Advantages**:

- No mining required (leave ore in ground)
- Low reagent concentration (environmentally mild)
- Ambient temperature
- Selective for REE (minimal gangue dissolution)

**Disadvantages**:

- Ammonia-nitrogen pollution [@xiao2015recovery]
  - NH₄⁺ remains on clay after REE removal
  - Leaches into groundwater
  - Environmental concern

#### Alternative Lixiviants (Ammonia-Free)
To address environmental concerns [@xiao2015recovery; @xiao2016reduction]:

**Magnesium sulfate** [@xiao2015leaching]:

    Clay−[REE³⁺] + 1.5 MgSO₄ → Clay−[Mg²⁺]₁.₅ + REE³⁺ + 1.5 SO₄²⁻

- MgSO₄ concentration: 1-3 wt%
- No ammonia pollution
- Mg²⁺ naturally occurring (less environmental impact)
- Somewhat lower leaching efficiency than (NH₄)₂SO₄ at equal concentration:
  Mg²⁺ is a divalent exchanger and needs 1.5 mol per mol of REE³⁺ against 3 mol
  for NH₄⁺, but it is the weaker competitor for the exchange sites

**Ferrous sulfate (reduction leaching)** [@xiao2016reduction]:

- FeSO₄ provides both cation exchange and reducing environment
- Helps mobilize Ce (can oxidize to Ce⁴⁺ and precipitate)

**Sodium chloride**:

- Very low environmental impact
- Lower leaching efficiency (60-75%)
- Requires higher concentrations

**Citric acid/organic acids** [@wang2017effects]:

- Complexation + ion exchange
- Biodegradable
- Higher cost

### Heap Leaching Process
For ore brought to surface [@shi2022column]:

1.  **Ore preparation**:
    - Crush to 5-20 mm (minimal processing)
    - Heap on impermeable pad
    - Height: 2-5 m
2.  **Leaching**:
    - Drip irrigation with lixiviant
    - Flow rate: 5-10 L/(m²·h)
    - Residence time in heap: 20-100 days
    - Collect pregnant leach solution (PLS)
3.  **PLS composition**:
    - REE: 200-1000 mg/L (0.02-0.1%)
    - pH: 4-6
    - Major impurities: Al, Fe, Ca (minimal)

### Column Leaching Studies
Laboratory simulation [@shi2022column; @long2019kinetics]:

**Experimental setup**:

- Column diameter: 5-10 cm
- Column height: 50-200 cm
- Ore particle size: 5-20 mm
- Percolation rate: 0.5-2 mL/min

**Key findings** [@shi2022column]:

- Lower (NH₄)₂SO₄ concentration increases efficiency
  - 0.2% (NH₄)₂SO₄: 93% recovery
  - 1.0% (NH₄)₂SO₄: 85% recovery
  - (Lower conc. reduces competitive adsorption)
- Temperature effect modest:
  - 15°C: 88% recovery
  - 25°C: 92% recovery
  - (Ambient conditions adequate)

**Leaching kinetics** [@long2019kinetics]:

    Model: Shrinking core model (particle diffusion controlled)

    Rate equation:
    1 - 3(1-X)^(2/3) + 2(1-X) = k_app × t

    Where:
    - X = fraction leached
    - k_app = apparent rate constant
    - t = time

Diffusion through clay particle pores is rate-limiting.

### Environmental Advantages and Concerns
**Advantages**:

- No roasting (energy savings)
- No strong acids (safer, less corrosive)
- Ambient temperature
- Selective leaching (minimal gangue)
- In-situ option (no mining)

**Concerns** [@xiao2015recovery]:

- Ammonia-nitrogen pollution from (NH₄)₂SO₄
  - Residual NH₄⁺ on ore body
  - Groundwater contamination
  - Regulatory pressure
- Large volumes of solution
  - 0.05% ore requires processing large tonnage
  - Dilute PLS requires concentration

**Recent advances** [@pan2024insights; @he2025stepwise]:

- Developing "anti-impurity leaching" (suppress Al, Fe)
- HMTA (hexamethylenetetramine) to inhibit Al dissolution
- Multi-stage leaching to maximize REE while minimizing impurities

### Recovery from Leach Solution
Pregnant leach solution processing [@han2024efficient; @liu2017enrichment]:

**Option 1: Precipitation**

- Add oxalic acid: REE³⁺ + 1.5 H₂C₂O₄ → REE₂(C₂O₄)₃↓
- Or ammonium bicarbonate: REE³⁺ + 3 NH₄HCO₃ → REE(OH)CO₃↓ + 3 NH₄⁺
- Calcine precipitate to REE₂O₃

**Option 2: Solvent extraction directly** [@han2024efficient]

- P507 (2-ethylhexyl phosphonic acid mono-2-ethylhexyl ester)
- D2EHPA
- Concentration factor: 10-50×
- Produces purified REE solution for further separation

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
### Principles of Bioleaching
Microorganisms mobilize REEs through [@rasoulnia2020critical; @brisson2015bioleaching]:

1.  **Acidolysis**:
    - Bacteria produce organic acids (citric, oxalic, gluconic acid)
    - Acids dissolve REE minerals
    - Complexation enhances solubility
2.  **Redoxolysis**:
    - Oxidation of Fe²⁺ to Fe³⁺ (by Acidithiobacillus)
    - Fe³⁺ oxidizes sulfide minerals
    - Indirect REE release
3.  **Complexolysis**:
    - Bacterial metabolites form REE complexes
    - Increases effective solubility

### Microorganisms Used
#### Fungi
**Aspergillus niger** [@brisson2015bioleaching; @wang2025rare]:

- Produces a mixture of organic acids — acetic, citric, gluconic, itaconic,
  oxalic and succinic were identified in the monazite work
- Uses the mineral as a phosphate source, which is why phosphate-solubilising
  fungi are the ones that work on monazite
- pH 2-4 after growth
- Time: weeks

**Mechanism**:

    Fungal organic acids + REEPO₄ → REE-organic acid complexes + H₃PO₄
    (schematic: the acids are a mixture and the stoichiometry is not fixed)

**Advantages**:

- Environmentally benign
- Simultaneous phosphate recovery
- Operates at ambient temperature

**Disadvantages**:

- Slow (weeks vs. hours for acid leaching)
- Lower extraction efficiency
- Needs a fermentable carbon source (glucose or a waste sugar stream), which is
  a real operating cost and a real carbon burden

#### Bacteria
**Acidithiobacillus ferrooxidans** [@wang2025rare]:

- Acidophilic bacteria
- Oxidizes Fe²⁺ and S²⁻
- Produces H₂SO₄ from sulfur oxidation
- pH can reach 1-2

**Application**:

- Suitable for sulfide-containing REE ores
- Indirect leaching via acid generation

**Gluconobacter oxydans** [@jindra2018developing]:

- Produces gluconic acid
- Industrial waste bioleaching
- REE recovery from coal ash, e-waste

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
been shown for monazite. See [](#biological-and-biomimetic-separations) for the biological
chemistry in depth.

### Advantages and Limitations
**Advantages** [@rasoulnia2020critical; @joshi2025bioleaching]:

- Low environmental impact (no harsh chemicals)
- Ambient temperature and pressure
- Some selectivity for REE over Th in monazite [@brisson2015bioleaching]
- Potential for low-grade ores and waste streams

**Limitations**:

- Slow kinetics (weeks)
- Lower extraction efficiency
- Requires biological infrastructure
- Contamination risks
- Scale-up challenges

**Current status**:

- Laboratory and pilot scale
- Not yet industrial implementation
- Active research area
- May be economical for low-grade/waste materials

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
| F⁻       | Bastnasite (if present) | 0.1-2 g/L     | Corrosion, precipitates REE |

### Iron Removal
**pH adjustment method** (most common):

    Fe³⁺ + 3 H₂O ⇌ Fe(OH)₃↓ + 3 H⁺

    Conditions:
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

    Ca²⁺ + SO₄²⁻ → CaSO₄↓ (gypsum)

- Occurs naturally during leaching
- Filter to remove

**Carbonate precipitation**:

    Ca²⁺ + CO₃²⁻ → CaCO₃↓

### Thorium Removal
**Solvent extraction** [@amaral2010thorium]:

- Before REE extraction
- Primary amine (Primene JM-T) from sulfate liquor, or TBP from nitrate
- Th extracts preferentially
- See [](#thorium-management)

**Selective precipitation**:

- pH 4-5: Th(OH)₄ precipitates
- REE remain soluble

### Phosphate Removal
**Gypsum co-precipitation** (H₂SO₄ leach):

    Add CaCl₂ or lime:
    3 Ca²⁺ + 2 PO₄³⁻ → Ca₃(PO₄)₂↓
    Ca²⁺ + SO₄²⁻ + 2 H₂O → CaSO₄·2H₂O↓  (gypsum; occludes residual phosphate)

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
### Bastnasite, Chloride Route (Mountain Pass Type)

The unit operations, in order [@gupta2004extractive; @castor2006rare]:

``` example
Mining (open pit)
  ↓
Crushing and grinding
  ↓
Flotation (rougher, scavenger, cleaner)
  ├─→ Tailings (to pond)
  └─→ Bastnasite concentrate
        ↓
      Dilute HCl pre-leach (dissolves carbonate gangue)
        └─→ Upgraded concentrate
              ↓
            Oxidative roast (air; decarbonation + Ce(III) → Ce(IV))
              ↓
            HCl leach
              ├─→ Residue: cerium concentrate (Ce(IV) does not dissolve)
              └─→ REE chloride solution (Ce-depleted)
                    ↓
                  Purification (raise pH; precipitate Fe, Al)
                    ↓
                  Solvent extraction (D2EHPA or PC88A, chloride medium)
                    ↓
                  Individual REE oxides
```

Read the flowsheet for its logic rather than for numbers. Two design decisions
carry the whole thing: the roast is *oxidative* so that cerium is removed for
free as an insoluble residue rather than as fifteen more extraction stages, and
the acid is HCl end to end so that the liquor never has to be converted between
media before it reaches the extractant.

### Monazite, Sulfuric Route (Indian Process)

The unit operations, in order [@gupta2004extractive; @jha2016hydrometallurgical]:

``` example
Beach sand mining
  ↓
Gravity separation (spiral concentrators)
  ↓
Magnetic separation (HIMS)
  ↓
Electrostatic separation
  ├─→ Monazite concentrate (55% REO)
  ├─→ Ilmenite (TiO₂ source)
  └─→ Zircon (ZrO₂ source)
        ↓ (Monazite)
      Grinding (to 100 μm)
        ↓
      Sulfuric acid digestion (93% H₂SO₄, 220°C, 4 h)
        ↓
      Water leaching + filtration
        ↓
      Thorium separation (amine extraction)
        ├─→ Th concentrate (to disposal/storage)
        └─→ REE sulfate solution
              ↓
            Precipitation as hydroxide (pH 8, NaOH)
              ↓
            REE(OH)₃ solid
              ↓
            Dissolution in HCl
              ↓
            REE chloride solution
              ↓
            Solvent extraction (separation into La, Ce, Pr, Nd, Sm, etc.)
              ↓
            Individual REE oxides
```

The two features that distinguish this route are structural, not numerical.
Thorium is pulled out as a separate stream *before* the rare earths are
separated from one another, because a thorium-bearing organic phase would
contaminate every stage of the cascade downstream. And the sulfate liquor is
converted to chloride the only way it can be — precipitate the rare earths as
hydroxide, filter, redissolve the solid in HCl — rather than by trying to remove
the sulfuric acid from solution.

### Ion-Adsorption Clay (Southern China)

The unit operations, in order [@chi2008weathered; @shi2022column]:

``` example
In-situ leaching:
  Injection wells
    ↓
  (NH₄)₂SO₄ solution (2-3%, ambient temp)
    ↓
  Percolation through ore body (20-100 days)
    ↓
  Collection wells
    ↓
  Pregnant leach solution (200-1000 mg/L REE)
    ↓
  Solvent extraction (P507, concentration + separation)
    ├─→ Loaded organic (concentrated REE)
    └─→ Raffinate (recycle as lixiviant)
          ↓
        Stripping (HCl)
          ↓
        REE chloride (concentrated, 0.5-1 M)
          ↓
        Precipitation (oxalic acid or carbonate)
          ↓
        Calcination
          ↓
        REE oxide (enriched in heavy REE: Y, Dy, Tb)

Or heap leaching:
  Mined ore (minimal processing)
    ↓
  Heap on pad
    ↓
  Drip irrigation with (NH₄)₂SO₄
    ↓
  Collect PLS
    ↓
  [Same as above from PLS]
```

The distinguishing feature here is that there is no decomposition step at all.
Nothing is roasted and nothing is digested; the entire flowsheet is an ion
exchange followed by a concentration step. That is why these deposits are
economic at grades two to three orders of magnitude below a bastnasite ore, and
also why the environmental problem they create is a solution-management problem
(ammonium in groundwater, slope stability) rather than an emissions problem.

## Process Optimization and Kinetics
### Key Operating Parameters
#### Acid Leaching
**Temperature effect**:

- Arrhenius relationship: k = A exp(-E~a~/RT)
- Typical E~a~: 40-80 kJ/mol (diffusion-controlled)
- Doubling temperature → 2-5× faster leaching
- But: equipment limits, energy cost

**Acid concentration**:

- Higher \[H⁺\] → faster kinetics
- Optimal depends on mineral:
  - Bastnasite (roasted): 2-6 M H₂SO₄
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

### Leaching Kinetics Models
#### Shrinking Core Model

For solid particle dissolution [@long2019kinetics]:

**Three steps**:

1.  Diffusion through solution film (external)
2.  Reaction at solid surface
3.  Diffusion through product layer (internal)

**Rate equations**:

**Surface reaction control**:

    1 - (1-X)^(1/3) = k_s × t

**Product layer diffusion control**:

    1 - 3(1-X)^(2/3) + 2(1-X) = k_d × t

Where:

- X = fraction leached
- k~s~, k~d~ = rate constants
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

Bastnasite and monazite are beneficiated before they are leached, so the
material a leaching plant consumes is a **concentrate**, and the ore behind that
concentrate is a much larger and separate quantity. Ion-adsorption clay is not
beneficiated at all — there is no rare earth mineral to concentrate — so the
**ore is the leach feed**. A table that puts 1.5 t of bastnasite in the same
column as 20 t of ion-adsorption material is comparing a concentrate against an
ore, and it is out by whatever the beneficiation ratio happens to be.

The arithmetic is elementary. Feed required per tonne of REO is

    feed = 1 / (grade × recovery)

with grade as the mass fraction REO in that feed and recovery the fraction of
contained REO that survives to product. Every figure below is computed that way
from grades and recoveries stated elsewhere in this chapter; none is taken from
a secondary compilation.

**Leach feed, per tonne of REO:**

| Ore type       | Basis           | Grade (REO)  | Recovery | Feed per t REO |
|----------------|-----------------|--------------|----------|----------------|
| Bastnasite     | **concentrate** | 60-75 %      | 90-98 %  | 1.4-1.9 t      |
| Monazite       | **concentrate** | 50-70 %      | 85-95 %  | 1.5-2.4 t      |
| Ion-adsorption | **ore**         | 0.05-0.3 %   | 80-95 %  | 350-2,500 t    |

Worked, so the reader can check it: a bastnasite concentrate at the bottom of
its grade range and the bottom of its recovery range needs
1/(0.60 × 0.90) = 1.85 t per tonne of REO, and at the top of both,
1/(0.75 × 0.98) = 1.36 t. An ion-adsorption ore at 0.3 % REO leached at 95 %
recovery needs 1/(0.003 × 0.95) = 351 t; the same calculation at 0.05 % and 80 %
gives 1/(0.0005 × 0.80) = 2,500 t. Three orders of magnitude separate the two
feeds, which is the single most important fact about ion-adsorption mining and
the reason its environmental footprint is a land-and-groundwater problem rather
than a reagent problem.

**Ore behind the concentrate.** For bastnasite, the chapter's own flotation
numbers — a 10-30 % REO flotation feed recovered at 70-90 % — put the mined ore
at 1/(0.10 × 0.70 × 0.90) = 16 t down to 1/(0.30 × 0.90 × 0.98) = 3.8 t per
tonne of REO, so roughly **4-16 t of ore**, with the difference between that and
the 1.4-1.9 t of concentrate reporting to the flotation tailings pond. For
monazite the question is not well posed: beach placers are mined for ilmenite,
rutile and zircon, and monazite is recovered as a minor byproduct of a
separation that would happen anyway, so attributing a placer ore tonnage to the
rare earths is an allocation choice, not a measurement.

**Reagents.** Two of the three follow from stoichiometry:

- *Bastnasite, sulfuric route.* REE₂O₃ + 3 H₂SO₄ gives 3 × 98 / 328 = 0.90 t of
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

**Solid residues.** The acid routes leave 0.4-0.9 t (bastnasite) and 0.5-1.4 t
(monazite) of leach residue per tonne of REO, simply as the difference between
concentrate in and REO dissolved, plus any gypsum precipitated to fix phosphate.
The monazite residue carries the thorium and is the regulated stream. The
ion-adsorption case has no leach residue in the usual sense and is often
tabulated as "minimal", which is misleading: the solid left behind is the entire
350-2,500 t of ore, either in place after in-situ leaching or as a spent heap,
loaded with residual ammonium and structurally weakened by the leach.

### Major Environmental Concerns
1.  **Radioactive waste** (monazite):
    - Thorium residues and tailings
    - Require licensed disposal
    - Public opposition to processing
2.  **Acid waste**:
    - Spent acid requiring neutralization
    - Sulfate/chloride discharge
    - pH control in effluent
3.  **Fluorine emissions** (bastnasite):
    - HF gas from roasting
    - Requires scrubbing
    - Fluoride in wastewater
4.  **Ammonia-nitrogen** (ion-adsorption):
    - Residual NH₄⁺ in ore body
    - Groundwater contamination
    - Regulatory pressure in China
5.  **Large land disturbance**:
    - Ion-adsorption mining (low grade)
    - Tailings ponds
    - Acid mine drainage risk

### Waste Minimization Strategies
**Acid recycling**:

- Regenerate spent acid
- Reduced fresh acid consumption
- Example: Sulfate roasting to recover H₂SO₄

**Byproduct recovery**:

- Fluorine → HF acid or AlF₃ (aluminum industry)
- Phosphate → fertilizer
- Thorium → nuclear fuel (if viable)
- Iron → pigments, steel feedstock

**Closed-loop water systems**:

- Recycle process water
- Minimal discharge
- Requires treatment (ion exchange, RO)

**Alternative lixiviants**:

- Biodegradable organic acids
- Recyclable {index}`ionic liquids` (research stage)
- Magnesium salts instead of ammonium

### Energy and Carbon: Where the Burden Sits

Leaching itself is not the energy-intensive step. Qualitatively, and this much
is safe to say from the flowsheets above, the energy is concentrated in the
operations that move or heat large masses: comminution in beneficiation, and the
roast. Everything downstream of the roast happens at 25-95 °C in aqueous
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

**Ionic liquids**:

- Task-specific ionic liquids with extraction capability
- Can combine leaching and extraction
- Expensive, scale-up challenges

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

### Urban Mining
**REE recovery from secondary sources**:

- E-waste (magnets, phosphors)
- Industrial waste (catalysts, polishing powders)
- {index}`Coal fly ash <coal fly ash>`

**Advantages**:

- Higher REE grades than primary ores (often)
- No mining required
- Circular economy

**Leaching methods similar to primary ores**:

- Acid leaching most common
- Bioleaching promising for e-waste

## Comparison of Leaching Methods
### Summary Table

| Ore Type | Pre-treatment | Leaching Method | Conditions | REE Recovery | Major Challenge |
|----|----|----|----|----|----|
| Bastnasite | Roasting (700°C) | H₂SO₄ or HCl | 2-6M, 60-90°C, 2-4h | 90-98% | Fluorine emissions |
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
REO plus a regulated radioactive residue, that the bastnasite chloride route
spends its money on the roast, and that the ion-adsorption route spends almost
nothing on reagents or energy and almost everything on land, water and
remediation. Techno-economics is treated in
[](#environment-techno-economics-and-life-cycle).

## Conclusions and Recommendations
### Key Findings
1.  **Ore-specific processing is essential**:
    - Bastnasite: Requires defluorination (roasting) before acid leaching
    - Monazite: Needs thorium management; alkaline pre-treatment advantageous
    - Ion-adsorption clays: Mild salt leaching at ambient conditions
2.  **Leaching chemistry sets the shape of the process economics**:
    - Reagent consumption is fixed by stoichiometry and gangue, and for the
      monazite sulfuric route it is several tonnes of acid per tonne of REO
    - The roast, where there is one, is the energy-intensive step
    - Waste treatment is a significant cost component, and for ion-adsorption
      ore it is most of the cost
3.  **Environmental challenges drive innovation**:
    - Fluorine capture from bastnasite
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
- [@kim2025rare] — recent bastnasite processing review
- [@xie2014critical] — solvent extraction, including a leaching overview
- [@rasoulnia2020critical] — bioleaching critical review

By ore type. **Bastnasite**: [@chi2004recovery] (NH₄Cl roasting),
[@xu2012decomposition] (alkali decomposition), [@sinclair2017rare]
(supercritical CO₂). **Monazite**: [@borai2016modified] (selective thorium
separation), [@amaral2010thorium] (thorium extraction), [@brisson2015bioleaching]
(bioleaching). **Ion-adsorption clays**: [@xiao2015leaching] (ammonia-free
MgSO₄ leaching), [@shi2022column] (column leaching optimization),
[@long2019kinetics] (kinetics modeling), [@han2024efficient] (recent sulfate
leaching advances).

Industrial practice: [@gupta2004extractive] is the standard textbook.
