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

    300-400°C:   2 REE·FCO₃ → REE₂O₂CO₃ + 2 HF↑
                 (Oxycarbonate formation, HF evolution)

    500-700°C:   REE₂O₂CO₃ → REE₂O₃ + CO₂↑
                 (Oxide formation)

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
    2 REE·FCO₃ + Na₂CO₃ → REE₂O₂CO₃ + 2 NaF + CO₂↑

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
    REEO(OH) + 2 HCl → REECl₃ + H₂O

    Or direct acid dissolution:
    2 NaREEO₂ + 3 H₂SO₄ → REE₂(SO₄)₃ + Na₂SO₄ + 3 H₂O

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

    REE·FCO₃ + 3 NH₄Cl → REECl₃ + NH₃↑ + NH₄F + CO₂↑ + H₂O

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

### Industrial Example: Mountain Pass (USA)
**Historical process (Molycorp, pre-2015)** [@kim2025rare]:

1.  **Beneficiation**:
    - Flotation of bastnasite ore (7-9% REO)
    - Product: 60% REO concentrate
2.  **Roasting**:
    - Fluidized bed roaster
    - Temperature: 700°C
    - Air atmosphere
    - HF scrubbing system
3.  **Leaching**:
    - 70% H₂SO₄ at 90°C
    - Residence time: 3 hours
    - Extraction: 95% REE
4.  **Solid-liquid separation**:
    - Thickeners and filters
    - Wash to recover entrained REE
5.  **Purification**:
    - pH adjustment to precipitate Fe(OH)₃
    - Filtration
6.  **Product**:
    - Mixed REE chloride solution (after HCl conversion)
    - Feed to solvent extraction cascade

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

    2 (REE,Th)PO₄ + 3 H₂SO₄ → (REE,Th)₂(SO₄)₃ + 2 H₃PO₄

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

#### Hydrochloric Acid Leaching
    (REE,Th)PO₄ + 3 HCl → (REE,Th)Cl₃ + H₃PO₄

    Conditions:
    - HCl: 6-12 M (20-37 wt%)
    - Temperature: 140-180°C
    - Pressure: Autogenous (sealed vessel)
    - Time: 3-6 hours

**Advantages**:

- More aggressive than H₂SO₄ at same temperature
- Chloride medium suitable for solvent extraction

**Disadvantages**:

- Requires pressure vessel (autoclave)
- HCl vapor pressure at temperature
- Equipment corrosion

#### Nitric Acid Leaching
Used in some processes [@borai2016modified]:

    (REE,Th)PO₄ + 3 HNO₃ → (REE,Th)(NO₃)₃ + H₃PO₄

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

    Step 1: Alkaline digestion (300-400°C)
    (REE,Th)PO₄ + 3 NaOH → (REE,Th)(OH)₃ + Na₃PO₄

    Step 2: Water leaching
    Na₃PO₄ dissolves (remove phosphate)
    (REE,Th)(OH)₃ remains as solid

    Step 3: Acid leaching of hydroxides
    (REE,Th)(OH)₃ + 3 HCl → (REE,Th)Cl₃ + 3 H₂O

**Conditions for NaOH digestion**:

- NaOH:monazite ratio: 3-5:1 (w/w)
- Temperature: 140-200°C (autogenous pressure)
- Time: 2-6 hours
- Product: Mixed hydroxides + Na₃PO₄

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

    2 (REE,Th)PO₄ + 3 Na₂CO₃ → (REE,Th)₂O₃ + 2 Na₃PO₄ + 3 CO₂

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

**Primary amine extraction** (from HCl medium):

- Extractant: Alamine 336 (trioctylamine)
- Th extracts preferentially over REE at pH 1-2
- Strip with 6 M HCl

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
Ion-adsorption deposits in Southern China [@shi2022column; @xiao2015leaching; @long2019kinetics]:

**Formation**:

- Weathering of granite with REE-bearing minerals
- REEs released and adsorbed on clay surfaces
- No crystalline REE minerals present

**REE form**:

    Clay−[REE³⁺]_adsorbed   (exchangeable cations)

**Characteristics**:

- Very low grade: 0.05-0.3% REO
- Enriched in heavy REEs (Y, Dy, Tb, Eu)
- Strategic importance (50% of world's heavy REE supply)
- Easy to leach (no roasting needed!)

### In-Situ Leaching Process
**Principle**: Ion exchange with leaching agent [@xiao2015leaching; @long2019kinetics]

    Clay−[REE³⁺] + 3 NH₄⁺ ⇌ Clay−[NH₄⁺]₃ + REE³⁺(aq)

#### Ammonium Sulfate Leaching (Traditional)
**Process** [@xiao2015leaching]:

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

**Magnesium sulfate**:

    Clay−[REE³⁺] + 1.5 MgSO₄ → Clay−[Mg²⁺]₁.₅ + REE³⁺ + 1.5 SO₄²⁻

- MgSO₄ concentration: 1-3 wt%
- No ammonia pollution
- Mg²⁺ naturally occurring (less environmental impact)
- Leaching efficiency: 80-90% (vs. 90-95% for (NH₄)₂SO₄)

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

- Produces citric, oxalic, gluconic acids
- pH 2-4 after growth
- REE extraction from monazite: 65-85%
- Time: 14-30 days

**Mechanism**:

    Fungal organic acids + (REE,Th)PO₄ → REE-organic acid complexes + H₃PO₄

**Advantages**:

- Environmentally benign
- Simultaneous phosphate recovery
- Operates at ambient temperature

**Disadvantages**:

- Slow (weeks vs. hours for acid leaching)
- Lower extraction efficiency
- Requires sterile conditions

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

### Bioleaching Performance
**Monazite bioleaching** [@brisson2015bioleaching]:

| Microorganism        | Time (days) | REE Extraction | Conditions   |
|----------------------|-------------|----------------|--------------|
| Aspergillus niger    | 28          | 65-92%         | 25°C, pH 2-3 |
| A. terreus           | 21          | 55-75%         | 25°C, pH 2-4 |
| Penicillium tricolor | 30          | 60-80%         | 25°C, pH 2-3 |

**Ion-adsorption ores** [@wang2025rare]:

- Aspergillus niger: 75% extraction in 14 days
- Acidithiobacillus ferrooxidans: 65% in 21 days
- Compare to chemical leaching: 90% in hours

### Advantages and Limitations
**Advantages** [@rasoulnia2020critical; @joshi2025bioleaching]:

- Low environmental impact (no harsh chemicals)
- Ambient temperature and pressure
- Selective REE dissolution
- Potential for low-grade ores
- Carbon-neutral process

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
**Strategy** [@corbett2017incorporation]:

- Use native microorganisms from ore deposits
- Pre-adapted to local conditions
- Better performance than lab strains

**Western Australian monazite**:

- Indigenous microorganisms increased leaching rate 3×
- 80% extraction in 14 days vs. 45% with lab strains

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
- Primary amine (Alamine 336) or TBP
- Th⁴⁺ extracts preferentially
- See [](#thorium-management)

**Selective precipitation**:

- pH 4-5: Th(OH)₄ precipitates
- REE remain soluble

### Phosphate Removal
**Gypsum co-precipitation** (H₂SO₄ leach):

    Add CaCl₂ or lime:
    Ca²⁺ + SO₄²⁻ + PO₄³⁻ → CaSO₄·xH₂O↓ (traps phosphate)

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

This solution feeds into the solvent extraction process described in the chemistry fundamentals review.

## Complete Process Flowsheets
### Bastnasite (Mountain Pass Type)
``` example
Mining (open pit)
  ↓
Crushing (jaw + cone crushers)
  ↓
Grinding (ball mill to 100 μm)
  ↓
Flotation (3-stage: rougher, scavenger, cleaner)
  ├─→ Tailings (to pond)
  └─→ Concentrate (60% REO)
        ↓
      Roasting (fluidized bed, 700°C, 2 h)
        ├─→ HF gas (to scrubber, produce HF acid)
        └─→ Roasted product (REE₂O₃)
              ↓
            Sulfuric acid leaching (4 M H₂SO₄, 90°C, 3 h)
              ↓
            Filtration
              ├─→ Residue (to waste or Si recovery)
              └─→ REE sulfate solution
                    ↓
                  Purification (pH 4, precipitate Fe, Al)
                    ↓
                  Conversion to chloride (add HCl, evaporate H₂SO₄)
                    ↓
                  REE chloride solution (1.0 M, pH 2-3)
                    ↓
                  Solvent extraction (D2EHPA or PC88A)
                    ↓
                  Individual REE oxides
```

**Key metrics**:

- Overall REE recovery: 65-75% (mining to final product)
- Processing time: 3-5 days (roast to solution)
- Energy: \~15 GJ/ton REO (mainly roasting)

### Monazite (Indian Process)
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

**Key metrics**:

- REE recovery: 85-92%
- Thorium recovery: 95% (separate product)
- Processing time: 2-3 days
- Phosphate byproduct: Used for fertilizer

### Ion-Adsorption Clay (Southern China)
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
  Pregnant leach solution (200-500 ppm REE)
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

**Key metrics**:

- REE recovery: 70-85% (in-situ), 85-95% (heap)
- No roasting or high-T processing
- Energy: \~2 GJ/ton REO (mainly solvent extraction)
- Strategic source for heavy REE

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
**Ultrasonic assistance** [@stojkovic2024recovery]:

- Ultrasound enhances mass transfer
- Reduces leaching time 30-50%
- Energy input required

**Microwave heating**:

- Rapid, selective heating
- Reduced processing time
- Higher capital cost

**High-pressure leaching**:

- Autoclaves allow higher temperature
- Faster kinetics
- Requires pressure vessels

## Environmental and Sustainability Considerations
### Waste Generation
**Per ton of REO produced** [@jha2016hydrometallurgical]:

| Ore Type       | Ore Consumed | Acid Used      | Solid Waste | Wastewater |
|----------------|--------------|----------------|-------------|------------|
| Bastnasite     | 1.5-2 tons   | 1-2 tons H₂SO₄ | 0.5-1 ton   | 5-10 m³    |
| Monazite       | 2-3 tons     | 2-4 tons H₂SO₄ | 1-2 tons    | 8-15 m³    |
| Ion-adsorption | 20-50 tons   | 0.5 tons salt  | Minimal     | 100-300 m³ |

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

### Life Cycle Assessment
**Energy consumption** [@jha2016hydrometallurgical]:

| Process Step     | Energy (GJ/ton REO) |
|------------------|---------------------|
| Mining           | 0.5-2               |
| Beneficiation    | 3-8                 |
| Roasting         | 8-15                |
| Leaching         | 1-3                 |
| Purification     | 0.5-1               |
| Solvent extract. | 2-5                 |
| **Total**        | **15-35 GJ/ton**    |

**CO₂ footprint**:

- Bastnasite: 15-25 tons CO₂/ton REO
- Monazite: 20-30 tons CO₂/ton REO
- Ion-adsorption: 8-15 tons CO₂/ton REO

## Emerging Technologies and Future Directions
### Green Leaching Methods
**Deep eutectic solvents (DES)** [@ni2023sustainable]:

- Mixtures of quaternary ammonium salts + H-bond donors
- Low vapor pressure, recyclable
- REE extraction from waste: 60-80%
- High cost currently limits application

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
- Demonstrated for ion-adsorption leaching

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
| Bioleaching (all) | None | Microbial organic acids | Ambient, 14-30 days | 60-85% | Slow kinetics |

### Economic Comparison (Approximate Operating Costs per ton REO)

| Process Step      | Bastnasite  | Monazite    | Ion-adsorption |
|-------------------|-------------|-------------|----------------|
| Mining & benefic. | \$2,000     | \$1,500     | \$500          |
| Roasting          | \$800       | \$600       | \$0            |
| Leaching          | \$500       | \$800       | \$200          |
| Purification      | \$400       | \$600       | \$300          |
| **Subtotal**      | **\$3,700** | **\$3,500** | **\$1,000**    |

(Note: Costs vary widely by location, scale, ore grade. Ion-adsorption cheaper per ton REO but processes much more ore volume.)

## Conclusions and Recommendations
### Key Findings
1.  **Ore-specific processing is essential**:
    - Bastnasite: Requires defluorination (roasting) before acid leaching
    - Monazite: Needs thorium management; alkaline pre-treatment advantageous
    - Ion-adsorption clays: Mild salt leaching at ambient conditions
2.  **Leaching chemistry dominates process economics**:
    - Acid consumption 20-40% of operating cost
    - Roasting energy-intensive (8-15 GJ/ton REO)
    - Waste treatment significant cost component
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
