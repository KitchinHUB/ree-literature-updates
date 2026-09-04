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
The "pH swing" is the entire operating principle, and the +3 slope of log D
against pH is its signature — three protons released per metal ion, so a single
pH unit moves the distribution ratio by three orders of magnitude. (The same
stoichiometry read against log[H⁺] rather than pH gives a slope of −3; both
appear in the literature and they describe the same experiment.)

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

$$
\mathrm{REE^{3+}(aq)} + 3\,\mathrm{HL(org)} \rightleftharpoons \mathrm{REEL_3(org)} + 3\,\mathrm{H^+(aq)}
$$

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
    - Increases ionic strength: $I = \tfrac{1}{2} \sum_i c_i z_i^2$
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

$$
I = \tfrac{1}{2} \sum_i c_i z_i^2
$$

**Effects on extraction**:

- High ionic strength (I \> 1 M): Salting-out effect dominates
- Low ionic strength (I \< 0.1 M): Activity coefficient corrections needed
- Industrial practice: I = 1-3 M for robust extraction

**Distribution ratio dependence**:

$$
\log D = \log D_0 + f(I)
$$

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

$$
\mathrm{REE^{3+}(aq)} + 3\,\mathrm{(HL)_2(org)} \rightleftharpoons \mathrm{REE(HL_2)_3(org)} + 3\,\mathrm{H^+(aq)}
$$

Where:

- (HL)₂ represents dimeric extractant (D2EHPA, PC88A form dimers)
- REE(HL₂)₃ is the extracted tris-complex

**Equilibrium constant**:

$$
K_\mathrm{ex} = \frac{[\mathrm{REE(HL_2)_3}]_\mathrm{org}\,[\mathrm{H^+}]_\mathrm{aq}^{3}}
                     {[\mathrm{REE^{3+}}]_\mathrm{aq}\,[\mathrm{(HL)_2}]_\mathrm{org}^{3}}
$$

**Distribution ratio** [@iloeje2019gibbs]:

$$
D = \frac{[\mathrm{REE}]_\mathrm{org}}{[\mathrm{REE}]_\mathrm{aq}}
$$

$$
\log D = \log K_\mathrm{ex} + 3 \log [\mathrm{(HL)_2}]_\mathrm{org} + 3\,\mathrm{pH}
$$

### pH Dependence (The "pH Swing")
**Key observation**: log D has **strong pH dependence** with slope ≈ +3 [@tanaka2021revaluating; @li2020hydration].

$$
\frac{\partial (\log D)}{\partial\, \mathrm{pH}} \approx +3
\qquad
\left( \text{equivalently,} \ \frac{\partial (\log D)}{\partial \log [\mathrm{H^+}]} \approx -3 \right)
$$

This means:

- Increasing pH by 1 unit → D increases by \~1000×
- Decreasing pH by 1 unit → D decreases by \~1000×

**Illustrative slope-3 behaviour**, drawn for a lanthanide with pH₁/₂ = 2.5 at
equal phase volumes; real D2EHPA systems sit close to this
[@agarwal2020comparative]:

| pH  | log D | D     | % Extraction |
|-----|-------|-------|--------------|
| 1.5 | -3.0  | 0.001 | 0.1%         |
| 2.0 | -1.5  | 0.032 | 3%           |
| 2.5 | 0.0   | 1.0   | 50%          |
| 3.0 | 1.5   | 32    | 97%          |
| 3.5 | 3.0   | 1000  | 99.9%        |

Half a pH unit takes the system from 3% to 97% extraction. That steepness is
what makes the pH swing work, and it is also why pH control is the single most
demanding part of running a cascade. [](#fig-logd-vs-ph) draws the same
relation for two neighbouring lanthanides at once, which is where the steepness
stops being an unmixed blessing: the slope is +3 for both of them, and the two
lines are parallel.

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

$$
n(\mathrm{H^+})_\text{released} = 3\, n(\mathrm{REE})_\text{extracted} = n(\mathrm{NaOH})_\text{required}
$$

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

- Impurities with lower $K_\mathrm{ex}$ values strip preferentially
- REEs remain in organic (high $K_\mathrm{ex}$ at this pH)

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

$$
\mathrm{REE(HL_2)_3(org)} + 3\,\mathrm{H^+(aq)} \rightarrow \mathrm{REE^{3+}(aq)} + 3\,\mathrm{(HL)_2(org)}
$$

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
- Partition coefficient: $P_\mathrm{HL}$ = $[\mathrm{HL}]_\mathrm{org}$ / $[\mathrm{HL}]_\mathrm{aq}$ \> 10,000
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

From: log D = log $K_\mathrm{ex}$ + 3 log[(HL)₂] + 3 pH

At D = 1: pH₁/₂ = −(log $K_\mathrm{ex}$ + 3 log[(HL)₂]) / 3

A *lower* pH₁/₂ means a more strongly extracted element, since it reaches
D = 1 while the aqueous phase is still more acidic.

**The order across the series.** For acidic organophosphorus extractants —
D2EHPA, PC88A, Cyanex 272, the workhorses of the industry — the distribution
ratio rises monotonically from La to Lu, and pH₁/₂ falls correspondingly. The
smaller, more charge-dense heavy ion binds the phosphoryl oxygens more tightly.
So in any cascade built on these reagents the heavies load into the organic
phase and the lights report to the raffinate. Yttrium is the exception that
matters industrially: it has no 4f electrons and sits by size near Ho, but its
extraction behaviour varies with the extractant and it can fall anywhere from
Dy to Er in the sequence, which is what makes Y/Ho separations awkward.

**Selectivity**:

$$
\Delta \mathrm{pH}_{1/2} = \mathrm{pH}_{1/2}(\mathrm{REE}_1) - \mathrm{pH}_{1/2}(\mathrm{REE}_2)
$$

Because log D moves with slope +3, the separation factor follows directly from
the gap between two elements' half-extraction pH values:

$$
\beta = 10^{\,3\,\Delta \mathrm{pH}_{1/2}}
$$

A gap of 0.1 pH units is a separation factor of 2; a gap of 0.2 is a factor of 4.
This is why pH control to ±0.05 units is a real engineering requirement and not
a counsel of perfection. Run the same arithmetic at the value that actually
governs an adjacent light-lanthanide pair, β = 1.5, and the gap is
Δ pH₁/₂ = (log 1.5)/3 = 0.06 pH units — the whole of the chemistry the industry
is built on, drawn to scale in [](#fig-logd-vs-ph).

:::{figure} ../figures/03-logd-vs-ph.svg
:name: fig-logd-vs-ph
:width: 100%

Two neighbouring lanthanides under an acidic organophosphorus extractant. The
lines are the mass-action expression `log D = log Kₑₓ + 3 log[(HL)₂] + 3 pH`
evaluated for β = 1.5, not fitted data; the constants are chosen only to put
D = 1 in the middle of the panel. The triangle is drawn to scale: one pH unit
buys three decades in D. The inset is also at true scale, not exaggerated —
that is its point. The horizontal separation between the two elements,
Δ pH₁/₂ = (log β)/3 = 0.06 pH units, is invisible in the main panel, which is
why the split has to be won by staging rather than by chemistry. Drawn from
`tools/figures/fig_logd_vs_ph.py`.
:::

**Typical separation windows** [@tanaka2021revaluating]. These are at the
optimistic end of the published range; adjacent light-lanthanide pairs are
commonly quoted nearer β = 1.5-2 (Δ pH₁/₂ ≈ 0.05-0.10), which is the value
[](#why-rare-earths-are-hard-to-separate) uses and the one the stage counts in
this chapter are built on. Treat the table as the best case a well-chosen
extractant and diluent can reach, not as what an arbitrary circuit will deliver:

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

$$
\Delta H_\mathrm{extraction} \approx -20 \ \text{to} \ -40 \ \mathrm{kJ/mol} \quad \text{(D2EHPA systems)}
$$

**Temperature dependence**:

$$
\log K_\mathrm{ex} = \frac{-\Delta H}{2.303\,RT} + \frac{\Delta S}{2.303\,R}
$$

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
- Number of stages: 4-8 extraction, 2-4 stripping *for a bulk-recovery duty*; an
  adjacent-pair separation needs tens to hundreds (see below)

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

### Phase Ratio and Material Balance
The distribution ratio alone does not tell you how much metal a stage moves.
That depends on how much of each phase is present, and the quantity that
combines the two is the **{index}`extraction factor`** [@rydberg2004solvent]:

$$
E = D \times (O/A)
$$

`E` is the ratio of metal in the organic phase to metal in the aqueous phase at
equilibrium, counting volumes. The fraction of the entering metal that a single
equilibrium stage transfers is then

$$
\text{fraction extracted} = \frac{E}{1 + E}
$$

and the same algebra run backwards gives the stripping factor
`S = (A/O)_strip / D_strip` with `fraction stripped = S / (1 + S)`.

A large `D` bought at a small `O/A` is not a large `E`. This is the most common
arithmetic error in reading extraction data:

**Example**:

- Extraction: D = 10 at O/A = 1/3 → E = 10/3 = 3.3 → **77% extracted per stage**
- Stripping: D_strip = 0.1 at A/O = 1/5 → S = (1/5)/(0.1) = 2 → **67% stripped
  per stage**

Neither is the ~95% a reader might assume from `D = 10` and `1/D_strip = 10`
alone. Getting to 99%+ is what the extra stages are for.

**Concentration factor**. Running the organic lean (small `O/A`) concentrates
the metal on extraction; running the strip liquor lean (small `A/O`) concentrates
it again. Both enrichments are capped by the fraction actually transferred:

$$
\mathrm{CF} = \frac{[\mathrm{REE}]_\text{product}}{[\mathrm{REE}]_\text{feed}}
     = (A/O)_\text{extraction} \times (O/A)_\text{stripping} \times f \times g
$$

where `f` and `g` are the overall extracted and stripped fractions. For the
numbers above, taken as single stages: 3 × 5 × 0.77 × 0.67 ≈ **7.7×**. Note the
ratios enter inverted relative to how they are written in the extraction and
stripping steps — a lean organic phase concentrates *because* there is little of
it.

**The ceiling on `O/A` is the extractant, not the hydraulics.** Three monomers of
an acidic organophosphorus extractant are consumed per REE³⁺. A 30 vol% D2EHPA
solution is about 0.9 M in monomer, so it saturates near 0.3 M REE and is run at
half that. A phase ratio that would load the organic past saturation does not
give the `D` the equilibrium data predict, no matter what the pH is.

### Countercurrent Cascade Design
**Principle**: Multiple extraction stages in series maximize REE transfer [@rydberg2004solvent].

#### McCabe-Thiele Diagram
Graphical method for determining stage requirements:

**Construction**:

1.  Plot equilibrium curve: y\* = f(x) where y = $[\mathrm{REE}]_\mathrm{org}$, x = $[\mathrm{REE}]_\mathrm{aq}$
2.  Draw operating line: y = (A/O)x + y₀
3.  Step off stages between equilibrium curve and operating line

**Parameters**:

- A/O = aqueous/organic flow ratio
- Slope of operating line = A/O
- Number of graphical steps = number of theoretical stages

This construction answers a *recovery* question — how many stages to strip one
solute out of one aqueous stream — and nothing else. It is drawn for a single
transferring species; it says nothing about which of two lanthanides ends up
where. Both questions have to be answered, and they have different answers.

#### How Many Stages for Recovery? The Kremser Equation
The graphical construction has an algebraic counterpart that is faster to use
and easier to check. If the equilibrium line is straight over the range of
interest, `y* = m x` with `m` the distribution ratio `D`, and if the phase flows
are constant through the train, the stage-by-stage material balance sums in
closed form. The result is the {index}`Kremser equation`, the same relation that
sizes absorbers and strippers throughout separations practice
[@rydberg2004solvent].

The notation matters, so state it. Take the aqueous phase to be the one losing
metal, and let

- `x_in` = metal concentration in the aqueous feed entering the cascade;
- `x_out` = metal concentration in the raffinate leaving it;
- `y_in` = metal concentration in the organic entering the cascade — zero for
  fresh solvent, non-zero when incompletely stripped organic is recycled;
- `m = D`, the slope of the equilibrium line; and
- `E = m (O/A) = D (O/A)`, the extraction factor defined above, taken constant
  through the cascade.

Then for `N` ideal countercurrent stages,

$$
\frac{x_\mathrm{in} - y_\mathrm{in}/m}{x_\mathrm{out} - y_\mathrm{in}/m}
   = \frac{E^{N+1} - 1}{E - 1}
$$

and inverting for the stage count,

$$
N = \frac{\ln\left[
      \dfrac{x_\mathrm{in} - y_\mathrm{in}/m}{x_\mathrm{out} - y_\mathrm{in}/m}
      \left(1 - \dfrac{1}{E}\right) + \dfrac{1}{E}
    \right]}{\ln E}
$$

Three checks. At `N = 1` the first expression gives `x_out/x_in = 1/(1 + E)`
for fresh solvent — the single-stage result of the previous section, recovered.
At `E = 1` both expressions are indeterminate; the limit is
`(x_in − y_in/m)/(x_out − y_in/m) = N + 1`, so the raffinate falls only as
`1/(N + 1)`. Stages then buy recovery arithmetically rather than geometrically,
and 99.9% recovery would take 999 of them — which is why nobody runs a cascade
at `E = 1` for recovery duty. At `E >> 1` the `1/E` terms drop out and
`N ≈ ln(x_in/x_out) / ln E`: every stage divides the aqueous concentration by
`E`, the geometric behaviour the McCabe-Thiele staircase draws.

**Worked example, using this chapter's own numbers.** Take `D = 10` at
`O/A = 1/3`, so `E = 3.33`, with fresh organic (`y_in = 0`). One stage extracts
77%. For 99.9% recovery, `x_in/x_out = 1000`:

$$
\begin{aligned}
N &= \frac{\ln[1000 \times (1 - 0.30) + 0.30]}{\ln 3.33} \\
  &= \frac{\ln(700.3)}{1.204} \\
  &= 5.4 \ \rightarrow \ 6 \ \text{theoretical stages}
\end{aligned}
$$

Six stages, and at 100% stage efficiency. That is where the "4-8 extraction
stages" figure quoted for a mixer-settler train comes from: it is a **recovery**
duty — one solute, a large `D`, a target expressed as percent recovered. It is
not a separation duty, and none of it carries over to the problem of splitting
two neighbouring lanthanides.

#### How Many Stages for Separation? A Fenske Bound
When two rare earths with separation factor β are to be split so that one is
pure at the extract end and the other pure at the raffinate end, the governing
estimate is not Kremser but Fenske's — the distillation result for the minimum
number of equilibrium stages at total reflux. It transfers to a fractional
extraction cascade unchanged, because the underlying algebra is the same: a
constant relative separation applied stage after stage.

$$
N_\mathrm{min} = \frac{\ln\left[
    \dfrac{x_P}{1 - x_P} \cdot \dfrac{1 - x_R}{x_R}
  \right]}{\ln \beta}
$$

`x_P` is the mole fraction of the more-extractable element in the product taken
from the extract end; `x_R` is that same element's mole fraction in the
raffinate; β is the pair's separation factor. Each bracketed term is a ratio of
wanted to unwanted, so the logarithm's argument is the product of the two
end-point enrichments — the separation job is shared between the two ends, and
tightening either end costs stages.

Put in the numbers this book keeps returning to. Demand 99.99% at both ends
(`x_P = 0.9999`, `x_R = 0.0001`) of a pair with β = 1.5:

$$
N_\mathrm{min} = \frac{\ln(9999 \times 9999)}{\ln 1.5} = \frac{18.42}{0.405} = 45 \ \text{stages}
$$

Forty-five, and that is a floor, not a design. `N_min` assumes total reflux, a
strictly binary feed, and equilibrium in every stage. A working circuit has
none of those: it runs at **finite reflux**, since the scrub and strip returns
that play the role of reflux are finite streams that cost reagent and pumping;
it splits a feed of eight or ten lanthanides rather than two, so each cut
carries the others through it; and its mixers reach 90-95% of equilibrium, not
100%. Installed stage counts are accordingly two to three times `N_min`. That
is the derivation behind the "hundreds of stages" of
[](#why-rare-earths-are-hard-to-separate): it follows from β ≈ 1.5 and the
purity specification, and is not an assertion about industrial habit.

The sensitivity is worth seeing, because it explains what plants actually do.
Relaxing both ends to 99.9% drops `N_min` from 45 to 34. Doubling β to 3.0 — the
gap between an adjacent pair and a pair two apart — drops it to 17. Choosing a
better extractant and choosing a less demanding purity target are the two levers,
and the logarithm means neither one is dramatic. The lower panel of
[](#fig-cascade) draws both cases: plotted against stage number on a log-ratio
axis the profile is a straight line whose slope is log β, so the stage count is
read off as a length, and the whole of what β buys is the difference between two
slopes.

#### Fractional Extraction: Extract, Scrub and Strip
A recovery cascade has the aqueous feed entering at one end. A **{index}`fractional
extraction`** cascade — the configuration every rare earth separation plant
actually runs — has it entering somewhere in the middle, which is what splits the
train into two sections that do different jobs ([](#fig-cascade)).

:::{figure} ../figures/03-cascade.svg
:name: fig-cascade
:width: 100%

**Above**, the fractional extraction cascade — a schematic of the configuration
described here, not of any particular plant. The phases run counter to each
other, organic left to right and aqueous right to left, so the raffinate leaves
the left end and the loaded organic the right; the feed enters partway along,
and the feed point is what divides the extraction section from the scrub
section. The scrub liquor is drawn as what it is, a split of the cascade's own
strip product. The two curved arrows are the sections' jobs: on the left the
more-extractable element pulled into the organic, on the right the co-extracted
less-extractable element displaced back off the extractant and returned toward
the feed. **Below**, the stage profile that goes with it, drawn from the Fenske
relation rather than measured: at total reflux each equilibrium stage multiplies
the ratio of the two elements by β, so on a log-ratio axis the profile is a
straight line of slope log β and the stage count is read off as a length. The
endpoints are this chapter's specification of 99.99% at both ends, and the two
slopes give the 45 and 17 stages derived above — floors, for the reasons given
there. The feed stage is where the profile crosses 50/50, which for an equimolar
binary feed is the middle of the train. Drawn from
`tools/figures/fig_cascade.py`.
:::

In the **extraction section**, between the feed point and the raffinate outlet,
the organic flowing counter to the aqueous pulls the more-extractable element
(for acidic organophosphorus reagents, the heavier lanthanide) out of the
aqueous; what survives to the raffinate end is progressively purer in the
*less*-extractable element. In the **scrub section**, between the feed point and
the loaded-organic outlet, an aqueous stream washes the loaded organic on its way
out, displacing the less-extractable element back off the extractant by mass
action and returning it toward the feed. What makes this work is the choice of
scrub liquor: not acid, and not a buffer, but a portion of the cascade's own
strip product — the purified more-extractable element, returned to the head of
the train [@banda2015separation].

That is **REE-on-REE scrubbing**, and it is the exact liquid-liquid analogue of
reflux in a distillation column. It is also the reason a cascade can be pure at
*both* ends instead of one. Scrubbing described as impurity removal — washing
Fe³⁺ or Ca²⁺ off the organic — is a different and much smaller operation; iron
in particular binds D2EHPA more strongly than any rare earth does and has to be
taken out upstream ([](#from-ore-to-feed-solution)), not scrubbed off here. The
strip section then returns the metal to an aqueous phase with strong acid and
regenerates the extractant; part of that strip liquor is split off as the scrub,
and the rest is product. The scrub-to-product split is the reflux ratio, and it
is the knob that trades reagent and throughput against stage count.

The design theory that makes such a cascade calculable rather than empirical is
{index}`Xu Guangxian`'s countercurrent extraction theory, developed in China from
the 1970s [@xu1985theory]. Given β, the feed composition and the two purity
specifications, it yields the number of extraction stages, the number of scrub
stages, the feed-stage location, and the flow ratios in closed form, so that a
plant can be designed on paper and brought up at its design point instead of
being tuned over months of operation. Its adoption, and the linking of cascades
in series so that the raffinate of one becomes the feed of the next, is what
turned a fifteen-component feed into a fan-out of individual oxides and made
China the world's separator of rare earths [@yan2006rare].

The closed-form design is where a cascade calculation starts, not where it ends.
Relaxing the constant-extraction-ratio assumption, carrying the acid balance the
saponification section below explains, and asking which arrangement of stages is
*best* rather than which one works are all questions for a numerical model of the
whole train. [](#process-modeling-and-optimization) takes them up, from Xu's
theory through commercial flowsheet simulators to the equation-oriented
frameworks that pose cascade design as an optimization problem.

#### Saponification of the Extractant
There is one industrial practice that follows directly from the reaction this
chapter opened with, and that a laboratory description of solvent extraction
never mentions. Each REE³⁺ transferred to the organic phase releases three
protons into the aqueous phase. At a working loading of 0.2 M rare earth, that
is 0.6 mol of H⁺ per litre of aqueous feed — enough to drop the pH by several
units, which by the slope-3 dependence collapses `D` by several *orders* of
magnitude. Left alone, an extraction cascade poisons itself in its first stage.

Adding caustic to each mixer, as this chapter's own extraction-stage description
does, is how it is handled on a bench. It does not survive scale-up: base
injected into a mixer creates local pH excursions that precipitate rare earth
hydroxides and stabilise emulsions, and it has to be dosed and controlled
separately in every one of dozens of stages. Industrial circuits instead
neutralise the extractant *before* it enters the cascade, a step called
**{index}`saponification`**. The organic is contacted with NaOH, aqueous ammonia,
or a magnesium base, converting 30-50% of the acidic extractant from HL to its
sodium, ammonium, or magnesium salt. Extraction then proceeds by exchanging
RE³⁺ for Na⁺, NH₄⁺, or Mg²⁺ rather than for H⁺, and the aqueous pH stays where
it was set without any in-stage dosing [@banda2015separation; @xie2014critical].

The cost is that the saponifying cation has to go somewhere, and where it goes
is the raffinate. Ammonia saponification — long the standard for P507 circuits,
because ammonium salts of the extractant behave well and NH₃ is cheap — puts
ammonium into every aqueous stream leaving the plant. This is the origin of the
{index}`ammonium-nitrogen <ammonia-nitrogen pollution>` effluent that is the
signature pollution problem of Chinese rare earth separation, and it is the same
nitrogen burden, from a different unit operation, that
[](#ion-adsorption-clays) describes for ammonium sulfate clay leaching and that
[](#environment-techno-economics-and-life-cycle) counts in the eutrophication
column of the life-cycle inventory. Sodium saponification trades it for a saline
raffinate; magnesium and calcium saponification, and non-saponification
flowsheets that recycle the acid instead, are the directions the Chinese industry
has been pushed toward on exactly these grounds [@liao2013clean]. Whichever is
chosen, the reagent bill and the effluent are set by the same stoichiometry:
three equivalents of base per mole of rare earth moved.

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

$$
\text{Rate} = K_\mathrm{overall} \, a \, (C^* - C)
$$

Where:

- $K_\mathrm{overall}$ = overall mass transfer coefficient (cm/s)
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

These are the actuators. What tells them where to go is a model of the cascade,
and on an industrial train the controlled variable — component content partway
along the profile — is not something any of the instruments above measures
directly. [](#process-modeling-and-optimization) covers the soft sensors and
predictive controllers built for that problem, and the process models they run
on.

## Industrial Example: Complete Process Flow
### Typical REE Separation Plant (Simplified)
**Feed**: {index}`Bastnäsite <bastnäsite>` concentrate (60% REO, mostly La, Ce, Pr, Nd)

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

#### Step 4: Individual Separation (La from Pr-Nd)
With acidic organophosphorus extractants the heavier lanthanides are extracted
more strongly, so **La is the element left behind**. The split takes La out of
the raffinate, not out of the organic phase.

- Feed: 0.3 M (La+Pr+Nd), pH 2.8, diluted from Step 3

- Organic: 30% D2EHPA + 10% TBP in kerosene (≈0.9 M monomer, saturating near
  0.3 M REE)

- Extraction: 6 stages, O/A = 2/1, pH 3.0 (controlled)

  - Pr and Nd extract preferentially (lower pH₁/₂, higher D)
  - Loaded organic: ≈0.15 M, enriched in Pr and Nd — about half of the
    extractant's capacity, which is where these circuits are run
  - Raffinate: enriched in La

- Scrub: 2 stages, pH 2.5, with dilute strip liquor (removes co-extracted La
  from the organic; the scrub is REE-on-REE here, not impurity removal)

- Strip: 3 stages, 4 M HCl, 50°C

  - Product: ≈0.45 M Pr+Nd in HCl at A/O = 1/3

- La product: recovered from the raffinate by oxalate precipitation and
  calcination

#### Step 5: Repeat for the Pr/Nd Separation

- The Pr-Nd strip liquor becomes the feed to a second cascade
- Pr/Nd is the hardest split in this sequence: β ≈ 1.4-1.5
- Typically requires 8-12 stages for a bulk split, and many more for
  99.9%-grade Nd

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
| Number of stages  | 4-8          | 2-4         | Bulk recovery only; an adjacent-pair split needs ≥45 (Fenske, β = 1.5) |

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

```text
High pH (3-4) → REE extracts into organic (D >> 1)
         ↓
    Loaded organic
         ↓
Low pH (0-1) → REE strips back to aqueous (D << 1)
         ↓
 Regenerated organic (recycle)
```

Slope: ∂(log D)/∂pH ≈ +3 for trivalent REE with dimeric acidic extractants

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
