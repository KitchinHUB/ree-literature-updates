---
title: Solvent Extraction Fundamentals
---

(solvent-extraction-fundamentals)=
# Solvent Extraction Fundamentals

This is the core teaching chapter of the book. {index}`Solvent extraction <solvent extraction>` is how nearly
all rare earths are separated today, and everything in Part III is best read as
an attempt to do better than what is described here.

The mechanism is simpler than its industrial complexity suggests. An acidic
extractant dissolved in kerosene is a weak acid; when it coordinates a REE³⁺ ion
it releases three protons. That single fact makes the whole process reversible
by pH: raise the pH and metal moves into the organic phase, drop it and the
metal comes back out, leaving the extractant regenerated and ready to recycle.
The "pH swing" is the entire operating principle, and the −3 slope of log D
against pH is its signature.

What makes rare earths hard is that this mechanism discriminates between
adjacent lanthanides only weakly. A {index}`separation factor` near 1.5 is normal.
Turning a factor of 1.5 into 99.99% purity is not a chemistry problem but a
staging problem, which is why the second half of this chapter is about
contactors, {index}`countercurrent <countercurrent cascade>` cascades, and phase ratios rather than about
molecules.

Along the way the chapter answers the questions that new researchers reliably
ask: why kerosene and not something else, what the salting-out agents are
doing there, and where the extractant goes over the course of a cycle (it stays
in the organic phase — better than 99.99% of it).

## Aqueous Phase Composition and Additives
### Role of pH Control
pH is the **primary control variable** in REE solvent extraction [@xie2014critical; @li2020hydration]. The extraction mechanism for acidic extractants ({index}`D2EHPA`, {index}`PC88A`) involves exchange of H⁺ for REE³⁺:

    REE³⁺(aq) + 3 HL(org) ⇌ REEL₃(org) + 3 H⁺(aq)

Where:

- HL = Extractant in organic phase (acidic form)
- REEL₃ = REE-extractant complex in organic phase

**pH ranges by extractant type** [@xie2014critical; @zhang2016rare]:

| Extractant    | Optimal Extraction pH | Stripping pH |
|---------------|-----------------------|--------------|
| D2EHPA        | 2.5-5.0               | 0.5-1.5      |
| PC88A         | 2.0-4.0               | 0.5-1.0      |
| TBP (neutral) | 0.5-2.0 (high NO₃⁻)   | dilution     |
| Cyanex 272    | 4.0-6.0               | 1.0-2.0      |
| DGA (amides)  | 0.5-3.0               | 0.1-0.5      |

### Aqueous Phase Additives and Their Functions
#### Salting-Out Agents
**Purpose**: Increase extraction efficiency by reducing water activity and suppressing extractant hydration [@rydberg2004solvent].

**Common salting agents**:

1.  **NaCl** (0.5-3 M) [@agarwal2020comparative]:
    - Inexpensive and widely available
    - Moderate salting-out effect
    - Compatible with chloride media
    - Increases ionic strength: I = 0.5 Σ c~i~ z~i²~
2.  **Ca(NO₃)₂** (1-3 M) [@matveev2018solvent]:
    - Strong salting-out effect (divalent cation)
    - Enhances {index}`TBP <TBP (tributyl phosphate)>` extraction via nitrate complex formation
    - Creates REE(NO₃)₃·nTBP extractable species
    - Used industrially for TBP processes
3.  **Al(NO₃)₃** (0.5-2 M):
    - Very strong salting effect (trivalent)
    - Can interfere if Al³⁺ is also extracted
    - Useful for selective extractions

**Mechanism** [@rydberg2004solvent]:

- Salts compete for water of hydration
- Reduces free water available to solvate extractant
- Shifts equilibrium toward organic phase
- Can provide 1-2 orders of magnitude improvement in {index}`distribution ratio`

#### Buffers and pH Control Agents
**Buffering systems** [@xie2014critical]:

1.  **Acetate buffer** (pH 3.5-5.5):
    - CH₃COOH/CH₃COONa
    - Good for D2EHPA, PC88A systems
    - Prevents pH drift during extraction
2.  **Citrate/citric acid** (pH 2-6):
    - Can also act as complexing agent
    - [@dewulf2022effect] shows solvent effects
3.  **Direct acid addition**:
    - HCl or HNO₃ for low pH (\<2)
    - Continuous monitoring and adjustment needed

**pH adjustment during operation**:

- **Extraction stage**: H⁺ released, pH decreases
  - Add base (NaOH, NH₃) to maintain pH
  - Typically 0.2-0.5 pH units drift acceptable
- **Stripping stage**: H⁺ consumed, pH increases
  - Add acid (HCl, HNO₃) to maintain low pH
  - Target pH \< 1.0 for complete stripping

#### Complexing Agents
**Purpose**: Modify selectivity between REEs or suppress co-extraction of impurities [@thiele2020tuning].

1.  **Lactic acid** [@dewulf2022effect]:
    - Forms aqueous complexes with REEs
    - Can enhance selectivity for certain REE pairs
    - 0.01-0.1 M typical concentration
2.  **EDTA/DTPA**:
    - Strong chelators for impurity removal
    - Can suppress {index}`thorium`, uranium extraction
    - Used in pre-treatment
3.  **Thiocyanate (SCN⁻)**:
    - Modifies selectivity in some systems
    - Less common in industrial practice

### Ionic Strength Effects
Ionic strength (I) affects activity coefficients [@rydberg2004solvent]:

    I = 0.5 Σ cᵢ zᵢ²

**Effects on extraction**:

- High ionic strength (I \> 1 M): Salting-out effect dominates
- Low ionic strength (I \< 0.1 M): Activity coefficient corrections needed
- Industrial practice: I = 1-3 M for robust extraction

**Distribution ratio dependence**:

    log D = log D₀ + f(I)

Where f(I) is ionic strength correction (typically positive for REE extraction)

## Organic Phase: Why Kerosene?
### Diluent Requirements for REE Extraction
The organic phase consists of:

1.  **Diluent** (typically 70-95% by volume)
2.  **Extractant** (5-30% by volume)
3.  **Phase modifier** (0-10%, optional)

**Key diluent requirements** [@rydberg2004solvent; @xie2014critical]:

| Property                    | Requirement                    | Kerosene Value |
|-----------------------------|--------------------------------|----------------|
| Density                     | \< 1.0 g/mL (phase separation) | 0.78-0.82 g/mL |
| Viscosity                   | Low (0.5-3 cP)                 | 1-2 cP (25°C)  |
| Water solubility            | \< 100 ppm                     | \~10 ppm       |
| Flash point                 | \> 60°C (safety)               | 60-80°C        |
| Dielectric constant         | 2-3 (low polarity)             | 1.8-2.1        |
| Chemical stability          | Resistant to acids/bases       | Excellent      |
| Interfacial tension         | 15-40 mN/m                     | 25-35 mN/m     |
| Cost                        | \< \$2/kg                      | \$1-2/kg       |
| Environmental acceptability | Low toxicity, biodegradable    | Moderate       |

### Why Kerosene is Preferred
#### Chemical Properties
**Composition**: Kerosene is a mixture of C₉-C₁₆ alkanes (linear and branched) with some aromatic content (10-20%) [@rydberg2004solvent].

**Advantages for REE extraction** [@xie2014critical; @zhang2016rare]:

1.  **Appropriate polarity**:
    - Dielectric constant ε ≈ 2.0
    - Dissolves extractants (D2EHPA, PC88A) well
    - Does not compete for extractant coordination
    - Low water solubility prevents phase mixing
2.  **Solvation properties**:
    - Provides favorable solvation for REE-extractant complexes
    - [@dewulf2022effect] showed polar solvents can interfere
    - Kerosene's low polarity minimizes interference
3.  **Density difference**:
    - ρ(aqueous) ≈ 1.1-1.2 g/mL (with salts)
    - ρ(kerosene) ≈ 0.8 g/mL
    - Δρ ≈ 0.3-0.4 g/mL enables gravity separation
4.  **Viscosity**:
    - Low viscosity → fast phase disengagement
    - Reduces pumping energy
    - Improves mass transfer rates

#### Operational Advantages
1.  **Cost-effectiveness**:
    - Petroleum refinery product
    - \$1-2 per kg (vs. \$5-20/kg for specialized solvents)
    - Critical for industrial-scale operations (1000s of L/day)
2.  **Safety**:
    - Flash point 60-80°C (vs. 40°C for hexane)
    - Reduces fire hazard in large-scale plants
    - Lower vapor pressure than light alkanes
3.  **Chemical stability**:
    - Resistant to acid and base hydrolysis
    - No reaction with extractants
    - Long service life (months to years with purification)
4.  **Low water solubility**:
    - Minimal organic loss to aqueous raffinate
    - Reduces environmental discharge issues
    - Phase separation is clean

#### Alternative Diluents
Other diluents used in specialized applications [@dewulf2022effect]:

1.  **n-Dodecane** (C₁₂H₂₆):
    - Pure compound (better for research)
    - More expensive than kerosene
    - Similar properties to kerosene
2.  **Isopar series** (branched alkanes):
    - Lower odor than kerosene
    - Higher flash point (\>100°C)
    - 2-3× cost of kerosene
    - Used in pharmaceutical/food applications
3.  **{index}`Ionic liquids <ionic liquids>`**:
    - Negligible vapor pressure
    - Tunable properties
    - Very expensive (\$100-1000/kg)
    - Research stage for REE separations
4.  **Supercritical CO₂**:
    - Green solvent
    - Requires high pressure equipment
    - Not yet commercial for REE

### Phase Modifiers
**Purpose**: Prevent third-phase formation and improve phase separation [@rydberg2004solvent].

**Common modifiers**:

1.  **TBP** (tributyl phosphate): 5-10 vol%
    - Increases organic phase polarity
    - Prevents aggregation of metal-extractant complexes
    - Critical when loading \> 20 g/L REE
2.  **1-Decanol, 1-dodecanol**: 3-5 vol%
    - Reduces interfacial viscosity
    - Improves coalescence
    - Prevents emulsion formation

**When needed**:

- High extractant concentration (\>30%)
- High metal loading (\>50% of extractant capacity)
- Systems prone to third-phase formation ({index}`Cyanex 272`, DEHPA)

## pH Swing Mechanism for Phase Transfer
### Extraction Step: Aqueous → Organic
The fundamental extraction reaction for acidic extractants [@xie2014critical; @tanaka2021revaluating]:

    REE³⁺(aq) + 3 (HL)₂(org) ⇌ REE(HL₂)₃(org) + 3 H⁺(aq)

Where:

- (HL)₂ represents dimeric extractant (D2EHPA, PC88A form dimers)
- REE(HL₂)₃ is the extracted tris-complex

**Equilibrium constant**:

    Kₑₓ = ([REE(HL₂)₃]ₒᵣ𝓰 × [H⁺]³ₐ𝓆) / ([REE³⁺]ₐ𝓆 × [(HL)₂]³ₒᵣ𝓰)

**Distribution ratio** [@iloeje2019gibbs]:

    D = [REE]ₒᵣ𝓰 / [REE]ₐ𝓆

    log D = log Kₑₓ + 3 log[(HL)₂]ₒᵣ𝓰 - 3 pH

### pH Dependence (The "pH Swing")
**Key observation**: log D has **strong pH dependence** with slope ≈ -3 [@tanaka2021revaluating; @li2020hydration].

    ∂(log D) / ∂pH ≈ -3

This means:

- Increasing pH by 1 unit → D increases by \~1000×
- Decreasing pH by 1 unit → D decreases by \~1000×

**Example with D2EHPA** [@agarwal2020comparative]:

| pH  | log D (La) | D (La) | % Extraction |
|-----|------------|--------|--------------|
| 1.0 | -1.5       | 0.03   | 3%           |
| 2.0 | 0.0        | 1.0    | 50%          |
| 3.0 | 1.5        | 32     | 97%          |
| 4.0 | 3.0        | 1000   | 99.9%        |

### Extraction Cycle
#### Extraction Stage (Forward Transfer)
**Conditions** [@xie2014critical]:

- pH: 2.5-4.0 (for D2EHPA/PC88A)
- Phase ratio: O/A = 1/1 to 1/5
- Contact time: 2-10 minutes
- Temperature: 20-40°C

**Process**:

1.  Aqueous feed (pH 3.0, REE³⁺ = 1.0 M) contacts organic (30% D2EHPA in kerosene)
2.  REE³⁺ transfers to organic, releasing H⁺
3.  Aqueous pH drops (3.0 → 2.5)
4.  Caustic (NaOH) added to maintain pH at 3.0
5.  Raffinate (depleted in REE) exits at pH 3.0
6.  Loaded organic (REE-extractant complex) advances to scrubbing

**Material balance**:

    H⁺ released = 3 × (moles REE extracted)
    NaOH required = 3 × (moles REE extracted)

For 1.0 M REE feed, 90% extraction:

- H⁺ released: 3 × 0.9 = 2.7 M
- NaOH requirement: 2.7 M (significant operating cost)

#### Scrubbing Stage (Optional)
**Purpose**: Remove co-extracted impurities (Fe³⁺, Al³⁺, Ca²⁺) from loaded organic.

**Conditions**:

- pH: 2.0-3.0 (intermediate between extraction and stripping)
- Scrub solution: dilute HCl or buffer
- O/A ratio: 5/1 to 20/1
- Contact stages: 1-2

**Selectivity**:

- Impurities with lower K~ex~ values strip preferentially
- REEs remain in organic (high K~ex~ at this pH)

#### Stripping Stage (Reverse Transfer)
**Conditions** [@xie2014critical; @zhang2016rare]:

- pH: 0.0-1.5 (strong acid)
- Stripping agent: 2-6 M HCl or HNO₃
- O/A ratio: 2/1 to 10/1
- Contact time: 5-15 minutes
- Temperature: 40-60°C (elevated T improves stripping)

**Process**:

1.  Loaded organic contacts strong acid (e.g., 4 M HCl, pH ≈ 0)
2.  High \[H⁺\] drives equilibrium backward (Le Chatelier)
3.  REE³⁺ transfers back to aqueous phase
4.  Extractant (HL) regenerated in organic phase
5.  Stripped organic (regenerated) recycled to extraction

**Stripping reaction**:

    REE(HL₂)₃(org) + 3 H⁺(aq) → REE³⁺(aq) + 3 (HL)₂(org)

**Stripping efficiency** [@agarwal2020comparative]:

- pH 0.5: \~95% stripping
- pH 1.0: \~85% stripping
- pH 1.5: \~60% stripping
- Complete stripping usually requires 2-3 stages

### Where Do Extractants Go?
**Critical insight**: Extractants remain predominantly in the organic phase throughout the cycle [@rydberg2004solvent; @xie2014critical].

#### Extractant Solubility
**D2EHPA** (di-2-ethylhexyl phosphoric acid):

- Water solubility: \~5 ppm (very low)
- Partition coefficient: P~HL~ = \[HL\]~org~ / \[HL\]~aq~ \> 10,000
- Organic phase loss: \<0.01% per cycle

**PC88A** (2-ethylhexyl phosphonic acid mono-2-ethylhexyl ester):

- Water solubility: \~10 ppm
- Similar partition behavior to D2EHPA
- Slightly higher aqueous loss due to phosphonic acid group

**TBP** (tributyl phosphate):

- Water solubility: \~400 ppm (higher than acidic extractants)
- More significant aqueous loss
- Requires organic wash/recovery step

#### Extractant Cycling
**Form during extraction**:

- Free extractant: (HL)₂ (dimer in organic phase)
- Metal-loaded: REE(HL₂)₃ (tris-complex)

**Form during stripping**:

- Metal complex dissociates: REE(HL₂)₃ → REE³⁺(aq) + (HL)₂(org)
- Extractant regenerated in free form

**Loading capacity** [@xie2014critical]:

- Maximum loading: \~50-70% of extractant molecules coordinated
- Typical operation: 30-40% loading
- Higher loading → increased viscosity, third-phase risk

**Degradation and makeup**:

- Hydrolysis: HL + H₂O → H₃PO₄ + organics (slow)
- Oxidation: exposure to air, radiolysis
- Makeup rate: 0.1-1% per cycle (depends on conditions)
- Purification: carbonate wash to remove degradation products

#### Phase Transfer Dynamics
**Extractant never "crosses" into aqueous permanently**:

1.  Extractant dissolved in kerosene at molecular level
2.  At interface, extractant adsorbs and reacts with REE³⁺
3.  REE-extractant complex remains in organic phase
4.  Only dissolved REE³⁺ moves between phases
5.  H⁺ exchanges across interface

**Mass transfer mechanism** [@rydberg2004solvent]:

- Diffusion of REE³⁺ to interface (aqueous side)
- Interfacial complexation reaction (fast)
- Diffusion of REE-complex away from interface (organic side)
- Rate-limiting step: usually aqueous diffusion

### Selectivity Between REEs
**pH1/2 concept** [@tanaka2021revaluating; @xie2014critical]:

pH₁/₂ is defined as the pH where D = 1 (50% extraction).

From: log D = log K~ex~ + 3 log\[(HL)₂\] - 3 pH

At D = 1: pH₁/₂ = (log K~ex~ + 3 log\[(HL)₂\]) / 3

**Selectivity**:

    Δ pH₁/₂(REE1-REE2) = pH₁/₂(REE1) - pH₁/₂(REE2)

**Typical separation windows** [@tanaka2021revaluating]:

| REE Pair | Δ pH₁/₂ (D2EHPA) | Separation Factor |
|----------|------------------|-------------------|
| La-Ce    | 0.2              | 4                 |
| Ce-Pr    | 0.3              | 8                 |
| Pr-Nd    | 0.2              | 4                 |
| Nd-Sm    | 0.4              | 16                |
| Gd-Tb    | 0.5              | 32                |
| Y-Ho     | 0.1              | 2                 |

**Challenges**:

- Adjacent REEs have small Δ pH₁/₂ (0.1-0.3 pH units)
- Requires many stages for high purity separations
- [@li2020hydration] shows hydration effects counteract separability

### Temperature Effects
**Extraction is typically exothermic** [@khoshoei2025crown]:

    ΔH_extraction ≈ -20 to -40 kJ/mol (for D2EHPA systems)

**Temperature dependence**:

    log K_ex = -ΔH / (2.303RT) + ΔS / (2.303R)

**Operational implications**:

- Extraction: 20-30°C (ambient, favors exothermic forward reaction)
- Stripping: 40-60°C (elevated T favors endothermic reverse reaction)
- [@khoshoei2025crown] provides recent thermodynamic data

## Liquid-Liquid Contactor Design
### Types of Contactors
#### Mixer-Settler
**Most common industrial design** [@rydberg2004solvent; @zhang2016rare].

**Mixer section**:

- Intense agitation (turbine impeller, 100-300 rpm)
- Residence time: 2-10 minutes
- Disperses one phase into other (typically organic dispersed in aqueous)
- Creates high interfacial area for mass transfer

**Settler section**:

- Quiescent zone for phase separation
- Gravity settling (Δρ = 0.3-0.4 g/mL)
- Residence time: 10-30 minutes
- Collect separated phases from different heights

**Advantages**:

- Simple, robust design
- Easy to scale (demonstrated up to 100 m³ units)
- Handles solids, impurities well
- Low maintenance

**Disadvantages**:

- Large footprint (long settling tanks)
- High holdup volume (inventory costs)
- Slow startup/shutdown
- Energy intensive mixing

**Typical dimensions** (per stage):

- Mixer: 1-5 m³
- Settler: 5-20 m³ (settler larger than mixer)
- Number of stages: 4-8 extraction, 2-4 stripping

#### Pulsed Columns
**Design**:

- Vertical column packed with perforated plates
- Pulsing action (sinusoidal flow) provides agitation
- Countercurrent flow: heavy phase down, light phase up

**Advantages**:

- Compact vertical design (small footprint)
- No moving parts in column (pulse from external pump)
- High throughput per unit volume
- Better stage efficiency than {index}`mixer-settlers <mixer-settler>`

**Disadvantages**:

- Sensitive to fouling (requires clean feeds)
- More difficult to troubleshoot
- Limited turndown ratio
- Emulsion-prone systems problematic

**Operating parameters**:

- Pulse frequency: 60-120 cycles/min
- Pulse amplitude: 5-25 mm
- Superficial velocity: 5-15 m/h
- HETS (height equivalent to theoretical stage): 0.5-1.5 m

#### Centrifugal Extractors
**Design**:

- High-speed rotor (2000-4000 rpm)
- Centrifugal force accelerates phase separation
- Compact design

**Examples**:

- Podbielniak extractor
- Robatel CINC extractors
- Alfa Laval extractors

**Advantages**:

- Very compact (10-100× smaller than mixer-settlers)
- Fast startup/shutdown (minutes vs. hours)
- Low holdup volume
- Excellent for emulsion-prone systems

**Disadvantages**:

- High capital cost
- Maintenance of rotating seals
- Power consumption
- Not suitable for solids-containing feeds

**Applications**:

- High-value products (justified cost)
- Space-constrained installations
- Pilot plants and research (fast testing)

#### Membrane Contactors
**Design**:

- Microporous hollow fiber membranes
- Phases flow on opposite sides of membrane
- Mass transfer through membrane pores

**Advantages**:

- Very high interfacial area (500-2000 m²/m³)
- No emulsion formation
- Modular, compact design
- Low energy consumption

**Disadvantages**:

- Membrane fouling and degradation
- Limited to clean systems
- Pore wetting issues
- Not yet widely commercial for REE

**Research status** [@pramanik2024emerging]:

- Emerging technology for REE separations
- Demonstrated in lab/pilot scale
- [@augustine2024advancing] may incorporate in future HT systems

### Countercurrent Cascade Design
**Principle**: Multiple extraction stages in series maximize REE transfer [@rydberg2004solvent].

#### McCabe-Thiele Diagram
Graphical method for determining stage requirements:

**Construction**:

1.  Plot equilibrium curve: y\* = f(x) where y = \[REE\]~org~, x = \[REE\]~aq~
2.  Draw operating line: y = (A/O)x + y₀
3.  Step off stages between equilibrium curve and operating line

**Parameters**:

- A/O = aqueous/organic flow ratio
- Slope of operating line = A/O
- Number of graphical steps = number of theoretical stages

#### Typical Cascade Configuration
**Extraction section**:

- Feed enters at intermediate point
- Fresh organic enters at bottom
- Loaded organic exits at top
- Raffinate (depleted aqueous) exits at bottom
- Stages required: N = 4-8 (depends on separation factor)

**Scrubbing section**:

- 1-2 stages
- Removes co-extracted impurities

**Stripping section**:

- 2-4 stages
- Strong acid strip solution
- Regenerates organic for recycle
- Product (concentrated REE) exits

**Overall plant**:

- Total stages: 8-15 (extraction + scrub + strip)
- Each stage = 1 mixer-settler unit

### Phase Ratio and Material Balance
**Phase ratio selection** [@rydberg2004solvent]:

    (O/A)_extraction × D = (A/O)_stripping × (1/D_strip)

**Example**:

- Extraction: D = 10, O/A = 1/3 → 97% extraction per stage
- Stripping: D = 0.1 (1/D = 10), A/O = 1/5 → 95% stripping per stage

**Concentration factor**:

    CF = ([REE]_product) / ([REE]_feed) = (O/A)_extraction × (A/O)_stripping

Example: (1/3) × (5/1) = 5/3 ≈ 1.7× concentration

### Operational Considerations
#### Phase Continuity
**Choice**: Organic continuous vs. aqueous continuous

**Aqueous continuous** (typical for REE):

- Organic dispersed as droplets
- Better when O/A \< 1
- Lower organic holdup and inventory
- Easier to control

**Organic continuous**:

- Used when O/A \> 1
- Can reduce aqueous reagent consumption

#### Interfacial Area and Mass Transfer
**Mass transfer rate**:

    Rate = K_overall × a × (C* - C)

Where:

- K~overall~ = overall mass transfer coefficient (cm/s)
- a = interfacial area per unit volume (cm²/cm³)
- C\* - C = driving force (concentration difference)

**Typical values**:

- Mixer-settlers: a = 50-200 cm²/cm³
- Pulsed columns: a = 100-500 cm²/cm³
- Centrifugal extractors: a = 500-2000 cm²/cm³

#### Entrainment and Coalescence
**Entrainment**: Carryover of one phase into the other

**Mitigation**:

- Adequate settling time (residence time in settler)
- Coalescers (packed beds, mesh pads)
- Proper settler design (weirs, baffles)

**Coalescence aids**:

- Glass fiber beds
- Membrane coalescers
- Increased residence time

### Process Control and Automation
**Key control variables** [@augustine2024advancing]:

1.  **pH control**:
    - In-line pH meters
    - Automatic acid/base addition
    - Critical for consistent distribution ratios
2.  **Flow rate control**:
    - Mass flow controllers
    - Maintain O/A ratio within ±5%
    - Prevents flooding or phase inversion
3.  **Temperature control**:
    - Heat exchangers
    - Especially important for stripping stage
4.  **Interface level control**:
    - Capacitance or conductivity sensors
    - Maintains interface in settler

**Modern automation** [@augustine2024advancing]:

- LANL Super Separator uses automated sampling and ICP-AES analysis
- Closed-loop control with Bayesian optimization
- Real-time adjustment of pH, flow rates based on analytical feedback

## Industrial Example: Complete Process Flow
### Typical REE Separation Plant (Simplified)
**Feed**: {index}`Bastnasite <bastnäsite>` concentrate (60% REO, mostly La, Ce, Pr, Nd)

#### Step 1: Dissolution

- Roast concentrate at 500°C (convert to oxides)
- Dissolve in HCl: 6 M HCl, 80°C, 4 hours
- Result: 1.5 M total REE in 1 M HCl (pH ≈ 0)

#### Step 2: Purification

- Adjust pH to 3.5 with NaOH
- Precipitate Fe(OH)₃, filter
- Result: Clean 1.0 M REE solution in 0.01 M HCl

#### Step 3: Group Separation (Ce removal)

- Oxidize Ce³⁺ to Ce⁴⁺ (add NaOCl at pH 9)
- Ce(OH)₄ precipitates
- Filter, wash
- Result: La-Pr-Nd mixture (Ce-free)

#### Step 4: Individual Separation (e.g., La from Pr-Nd)
- Feed: 1.0 M (La+Pr+Nd), pH 2.8

- Organic: 30% D2EHPA + 10% TBP in kerosene

- Extraction: 6 stages, O/A = 1/3, pH 3.0 (controlled)

  - La extracts preferentially (higher K~ex~)
  - Raffinate: enriched in Pr, Nd
  - Loaded organic: enriched in La

- Scrub: 2 stages, pH 2.5 (remove Pr, Nd contamination)

- Strip: 3 stages, 4 M HCl, pH 0, 50°C

  - Product: 1.8 M La in HCl (95% pure)

#### Step 5: Repeat for Pr/Nd Separation

- Adjust raffinate to pH 2.5
- Extraction cascade for Pr/Nd split
- Typically requires 8-12 stages (small separation factor)

### Material and Energy Balance (Approximate)
**For 1000 kg/day REO production**:

**Materials**:

- Concentrate: 1700 kg/day (60% REO)
- HCl (37%): 3000 kg/day
- NaOH (50%): 2500 kg/day (pH control)
- Extractant: 5000 L (inventory, makeup 50 L/day)
- Kerosene: 15,000 L (inventory, makeup 100 L/day)
- Water: 50,000 L/day

**Energy**:

- Roasting: 1.5 GJ/day
- Heating (dissolution, stripping): 3 GJ/day
- Pumping: 500 kWh/day
- Mixing: 1000 kWh/day
- Total: \~2000 kWh/day + 4.5 GJ thermal

## Summary and Key Takeaways
### Critical Parameters Summary
| Parameter         | Extraction   | Stripping   | Impact                        |
|-------------------|--------------|-------------|-------------------------------|
| pH                | 2.5-4.0      | 0.0-1.0     | Primary control variable      |
| Temperature       | 20-30°C      | 40-60°C     | Modest effect (ΔH = -30 kJ)   |
| Extractant conc.  | 20-40% (v/v) | Same        | Linear effect on log D        |
| Salting agent     | 1-3 M        | Not needed  | 1-2 order improvement in D    |
| Phase ratio (O/A) | 1/1 to 1/5   | 2/1 to 10/1 | Determines concentration      |
| Contact time      | 2-10 min     | 5-15 min    | Usually adequate for kinetics |
| Number of stages  | 4-8          | 2-4         | Depends on separation factor  |

### Why Kerosene?
In summary:

1.  **Low cost** (\$1-2/kg) for large-scale operations (1000s L)
2.  **Appropriate polarity** (ε ≈ 2) dissolves extractants, not too polar
3.  **Low water solubility** (\<10 ppm) prevents phase mixing
4.  **Density** (0.78-0.82 g/mL) enables gravity separation
5.  **Low viscosity** (1-2 cP) for fast phase disengagement
6.  **Chemical stability** resistant to acids/bases, long service life
7.  **Safety** (flash point 60-80°C) reduces fire hazard
8.  **Environmental** moderate toxicity, acceptable for industrial use

### pH Swing Mechanism
The fundamental principle:

    High pH (3-4) → REE extracts into organic (D >> 1)
             ↓
        Loaded organic
             ↓
    Low pH (0-1) → REE strips back to aqueous (D << 1)
             ↓
     Regenerated organic (recycle)

Slope: ∂(log D)/∂pH ≈ -3 for trivalent REE with dimeric acidic extractants

### Extractant Behavior
**Throughout the cycle**:

- Extractants stay in organic phase (\>99.99%)
- Aqueous solubility: 5-10 ppm for D2EHPA/PC88A
- Form transitions: free (HL)₂ ⇌ loaded REE(HL₂)₃
- Degradation slow, makeup \~0.1-1% per cycle
- Never "transfer" to aqueous permanently

### Practical Implementation
For successful REE solvent extraction:

1.  Control pH tightly (±0.1 units) - this is the primary variable
2.  Match the salting agent to the acid medium
3.  Maintain O/A ratio consistently
4.  Design for adequate contact time (not rate-limiting)
5.  Size settlers for clean phase separation
6.  Monitor extractant quality, purify periodically
7.  Use countercurrent cascades for high recovery/purity
