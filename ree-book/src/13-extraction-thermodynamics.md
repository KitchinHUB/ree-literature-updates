---
title: Thermodynamics of Extraction
---

(thermodynamics-of-extraction)=
# Thermodynamics of Extraction

Every separation factor in this book is, underneath, a difference of free
energies. This chapter works that relationship in both directions: forward, from
atomistic calculation to a predicted extraction constant, and backward, from
calorimetric measurement to the enthalpy and entropy terms that a prediction has
to reproduce.

The forward path is a thermodynamic cycle. The overall extraction reaction
cannot be computed directly, so it is decomposed into steps that can be — and
the chapter is candid about what that costs in accuracy. The short version: on
*absolute* extraction constants the errors are large enough to be useless, while
on *relative* predictions between neighbouring lanthanides the systematic errors
cancel and the method becomes worth running. Selectivity, which is what a
separation actually needs, is the easier quantity.

The backward path is microcalorimetry, which measures the heat of ion transfer
directly and so supplies the ΔH and ΔS a computed cycle can be checked against.
The chapter closes by linking extraction thermodynamics back to the mineral it
started from, writing dissolution and extraction in one set of chemical
potentials.

## Predicting K~ex~ from First Principles

We want to predict the extraction equilibrium constant:

    REE³⁺(aq) + 3 HL(org) ⇌ REEL₃(org) + 3 H⁺(aq)     K_ex

The standard thermodynamic relationship is:

    ΔG°_extraction = -RT ln(K_ex)

    Therefore:

    log K_ex = -ΔG°_extraction / (2.303 RT)

At 298 K:

- RT = 8.314 J/(mol·K) × 298 K = 2.478 kJ/mol
- 2.303 RT = 5.706 kJ/mol

So: **log K~ex~ = -ΔG°~extraction~ / 5.706** (if ΔG in kJ/mol)

### Problem: Can't Compute ΔG~extraction~ Directly

We **cannot** directly compute the free energy for the overall reaction:

    REE³⁺(aq) + 3 HL(org) → REEL₃(org) + 3 H⁺(aq)

Why not?

1.  Mixing phases (aqueous and organic) in one calculation is difficult
2.  Solvation in kerosene (complex mixture) not well-defined
3.  Need to handle both charged species (REE³⁺, H⁺) and neutral complexes

**Solution**: Break into a thermodynamic cycle using gas phase as reference!

### The Thermodynamic Cycle: Five Steps

#### Overview

We construct a cycle where all species pass through the gas phase:

``` example
                       ΔG₂ (gas-phase complexation)
   REE³⁺(g) + 3HL(g) ────────────────────────→ REEL₃(g)
        ↑                                            ↓
        │                                            │
     ΔG₁│                                            │ΔG₃
(dehydr)│                                            │(solvation
        │                                            │ in org)
        │                                            ↓
   REE³⁺(aq) ──────────────────────────────→ REEL₃(org)
                    Net extraction
                (what we measure)

   Plus separate paths for:
   3HL(org) ──→ 3HL(g)     (ΔG₄: extractant desolvation)
   3H⁺(g)  ──→ 3H⁺(aq)     (ΔG₅: proton solvation)
```

#### Step-by-Step Breakdown

##### ΔG₁: Dehydration of REE³⁺

    REE³⁺(aq) → REE³⁺(gas)

    ΔG₁ = G[REE³⁺(gas)] - G[REE³⁺(aq)]

**Physical meaning**: Remove REE³⁺ from water (break ion-dipole interactions)

**Always positive** (endothermic): \~1200-1500 kJ/mol for +3 ions

**Computational method**:

- Option 1: Implicit solvation (SMD model in Gaussian/ORCA)

      ΔG₁ = E(REE³⁺ in vacuum) - E(REE³⁺ with SMD water)

- Option 2: Empirical correlations (Born model)

      ΔG_solv ≈ -(z²e²N_A)/(8πε₀r_ion) × (1 - 1/ε_r)

  Where z=3, r~ion~ ≈ 1.0-1.2 Å for REE³⁺, ε~r~ = 78.4 for water

**Key insight**: ΔG₁ varies slightly across the lanthanide series (ionic radius changes)

- La³⁺ (larger): ΔG₁ ≈ 1250 kJ/mol
- Gd³⁺ (smaller): ΔG₁ ≈ 1400 kJ/mol
- This contributes to selectivity!

##### ΔG₂: Gas-Phase Complexation (THE CRITICAL TERM)

    REE³⁺(gas) + 3 HL(gas) → REEL₃(gas)

    ΔG₂ = G[REEL₃(gas)] - G[REE³⁺(gas)] - 3×G[HL(gas)]

**Physical meaning**: Formation of REE-extractant bonds (coordination chemistry)

**Always negative** (exothermic): Strong electrostatic and covalent bonding

**This is the term a machine-learned binding model predicts.**

**Computational method**:

****Phase 1 (DFT approach)****:

1.  Optimize geometry of REEL₃ complex (DFT: B3LYP-D4)

2.  Single-point energy calculation

3.  Compute binding energy:

        ΔG₂ ≈ E[REEL₃] - E[REE³⁺] - 3×E[HL]

****Phase 2 (UMA approach)****:

- Use Fairchem UMA model (pre-trained on large dataset)
- Direct prediction of binding energy
- **Much faster** than DFT (seconds vs. hours)
- Following Gupta et al. 2025: MAE ≈ 6.1 kcal/mol ≈ 25 kJ/mol

**Key variations**:

- Different REEs have different binding strengths
- Different extractants (D2EHPA vs. PC88A vs. TBP) give different ΔG₂
- This is the **primary source of selectivity** in gas phase

**Typical values**:

- La³⁺ + 3 D2EHPA: ΔG₂ ≈ -2500 kJ/mol
- Gd³⁺ + 3 D2EHPA: ΔG₂ ≈ -2600 kJ/mol
- Difference drives selectivity (after all terms accounted for)

##### ΔG₃: Solvation of Complex in Organic Phase

    REEL₃(gas) → REEL₃(org)

    ΔG₃ = G[REEL₃ in kerosene] - G[REEL₃(gas)]

**Physical meaning**: Stabilization of neutral complex in organic solvent

**Always negative**: Complex is stabilized by dispersion forces with kerosene

**Computational method**:

****Option 1: Implicit solvation****

- SMD model with ε~r~ ≈ 2 (kerosene dielectric constant)

- Treats kerosene as uniform dielectric medium

      ΔG₃ = E(REEL₃ with SMD, ε=2) - E(REEL₃ in vacuum)

****Option 2: COSMO-RS**** (more accurate)

- Uses realistic molecular description of solvent
- Accounts for surface interactions
- Can handle mixed solvents (kerosene is C₉-C₁₆ alkane mixture)

****Option 3: Empirical estimation****

- For neutral complexes, solvation in non-polar solvents is modest
- ΔG₃ ≈ -50 to -200 kJ/mol
- Mainly dispersion interactions

**Key consideration**:

- This term allows you to screen different solvents!
- Kerosene vs. dodecane vs. ionic liquids
- Different solvents → different ΔG₃ → different extraction efficiency

##### ΔG₄: Desolvation of Extractant from Organic Phase

    3 HL(org) → 3 HL(gas)

    ΔG₄ = 3 × [G[HL(gas)] - G[HL in kerosene]]

**Physical meaning**: Remove extractant from kerosene (break HL-solvent interactions)

**Always positive**: Costs energy to pull HL out of organic phase

**Computational method**:

****Option 1: Implicit solvation (same as ΔG₃)****

    ΔG₄ = 3 × [E(HL vacuum) - E(HL with SMD, ε=2)]

****Option 2: Experimental vaporization enthalpy****

- For D2EHPA, TBP: ΔH~vap~ data available from literature
- Approximate ΔG₄ ≈ 3 × ΔH~vap~ (neglecting entropy)

****Option 3: Cancel with ΔG₃ in first approximation****

- If same solvation model used for both
- Partial cancellation of organic phase solvation effects

**Typical values**:

- ΔG₄ ≈ +150 to +300 kJ/mol (for 3 × HL)

##### ΔG₅: Proton Solvation in Aqueous Phase

    3 H⁺(gas) → 3 H⁺(aq)

    ΔG₅ = 3 × [G[H⁺(aq)] - G[H⁺(gas)]]

**Physical meaning**: Hydration of protons released during extraction

**Always negative**: Protons are **very strongly** hydrated (forms H₃O⁺ and H₉O₄⁺ clusters)

**Computational method**:

****Standard state correction****: The free energy of H⁺(aq) depends on pH:

    G[H⁺(aq)] = G°[H⁺(aq)] + RT ln[H⁺]
              = G°[H⁺(aq)] - 2.303 RT × pH

**Standard value** (literature):

- G°\[H⁺(aq)\] - G\[H⁺(gas)\] ≈ -1100 kJ/mol (single proton hydration)

**Total for 3 protons**:

    ΔG₅ = 3 × [G°[H⁺(aq)] - 2.303 RT × pH - G[H⁺(gas)]]
        = 3 × G°_hydration - 3 × 2.303 RT × pH
        ≈ -3300 kJ/mol - 5.706 × 3 × pH  kJ/mol
        ≈ -3300 - 17.1 × pH  kJ/mol

**Key insight**: The pH appears explicitly here!

### Summing the Cycle: Total ΔG~extraction~

#### The Sum

    ΔG_extraction = ΔG₁ + ΔG₂ + ΔG₃ + ΔG₄ + ΔG₅

Let's trace the path:

1.  REE³⁺(aq) → REE³⁺(gas): ΔG₁ (+ large, \~1300 kJ/mol)
2.  REE³⁺(gas) + 3HL(gas) → REEL₃(gas): ΔG₂ (- large, \~-2500 kJ/mol)
3.  REEL₃(gas) → REEL₃(org): ΔG₃ (- modest, \~-100 kJ/mol)
4.  3HL(org) → 3HL(gas): ΔG₄ (+ modest, \~+200 kJ/mol)
5.  3H⁺(gas) → 3H⁺(aq): ΔG₅ (- very large, \~-3300 - 17pH kJ/mol)

#### Typical Values (Example: La + D2EHPA at pH 3)
| Term | Description            | Approximate Value |
|------|------------------------|-------------------|
| ΔG₁  | Dehydration            | +1250 kJ/mol      |
| ΔG₂  | Binding (DFT/UMA)      | -2500 kJ/mol      |
| ΔG₃  | Complex solvation      | -100 kJ/mol       |
| ΔG₄  | Extractant desolvation | +200 kJ/mol       |
| ΔG₅  | Proton hydration       | -3351 kJ/mol      |
| Sum  | **ΔG~extraction~**     | **-4501 kJ/mol**  |

#### Converting to K~ex~

    log K_ex = -ΔG_extraction / (2.303 RT)
             = -(-4501 kJ/mol) / (5.706 kJ/mol)
             = +788.8

Wait, that can't be right! K~ex~ = 10^788^ is unphysically large!

#### The pH Correction

The issue is that ΔG₅ includes the pH-dependent term. We need to separate the standard state from the pH dependence.

The proper formulation is:

    ΔG_extraction = ΔG°_extraction + 3 × RT ln[H⁺]
                  = ΔG°_extraction - 3 × 2.303 RT × pH

So we should write:

    ΔG°_extraction = ΔG₁ + ΔG₂ + ΔG₃ + ΔG₄ + ΔG°₅

Where ΔG°₅ is the **standard** hydration energy (at pH = 0, i.e., \[H⁺\] = 1 M).

#### Corrected Calculation

Using ΔG°₅ = 3 × (-1100) = -3300 kJ/mol (at standard state):

| Term | Value            |
|------|------------------|
| ΔG₁  | +1250 kJ/mol     |
| ΔG₂  | -2500 kJ/mol     |
| ΔG₃  | -100 kJ/mol      |
| ΔG₄  | +200 kJ/mol      |
| ΔG°₅ | -3300 kJ/mol     |
| Sum  | **-4450 kJ/mol** |

    log K°_ex = -ΔG°_extraction / (2.303 RT)
              = -(-4450) / 5.706
              = +779.9

Still huge! But now we apply the pH correction separately:

    log K_ex(pH) = log K°_ex + 3 pH

At pH = 3:

    log K_ex(pH=3) = 779.9 + 3(3) = 788.9

This is still very large, which tells us something is wrong with the absolute values...

### Reality Check: Where Are the Errors?

Experimental values are typically:

- log K~ex~ ≈ 0 to 10 (not 788!)

What's wrong?

#### Issue 1: Absolute Solvation Energies are Uncertain

The absolute values of:

- ΔG₁ (ion hydration): ±50 kJ/mol uncertainty
- ΔG₂ (DFT binding): ±50-100 kJ/mol uncertainty (this is why UMA has MAE ≈ 25 kJ/mol)
- ΔG°₅ (proton hydration): ±50 kJ/mol uncertainty

These uncertainties **add up** to ±150-200 kJ/mol, which is:

    Δ(log K_ex) ≈ ±200 / 5.706 ≈ ±35 log units!

Huge!

#### Issue 2: Standard States and Activity Coefficients

The thermodynamic formulation assumes:

- Activities, not concentrations
- Standard states properly defined
- Activity coefficients = 1

In reality:

- High ionic strength (I = 1-3 M)
- Activity coefficients ≠ 1
- Extractant dimerization not explicitly treated
- Complex may aggregate at high loading

### Practical Solution: Relative Predictions

Given the absolute uncertainty, we focus on **relative** values:

#### Approach 1: Predict ΔΔG (Selectivity)

Instead of absolute K~ex~, predict selectivity:

    ΔΔG = ΔG_extraction(REE1) - ΔG_extraction(REE2)

    Separation factor = K_ex(REE1) / K_ex(REE2) = exp(-ΔΔG/RT)

**Why this works**:

- Many systematic errors cancel (ΔG°₅ identical for both REEs)
- ΔG₃, ΔG₄ similar (same extractant, same solvent)
- Main difference: ΔG₁ (different ionic radii) and ΔG₂ (different binding)

#### Approach 2: Calibrate with Experimental Data

Use experimental data to correct the absolute scale:

    ΔG_extraction(predicted) = ΔG_extraction(computed) + C

Where C is fitted to match experimental log K~ex~ for 1-2 reference systems.

**This is what an experimental validation dataset is for.**

#### Approach 3: Focus on Trends

Even if absolute values are off, trends should be correct:

- pH dependence (slope = 3)
- Temperature dependence (via ΔH = ∂ΔG/∂T)
- Solvent effects (relative ΔG₃ for different solvents)
- Extractant comparison (relative ΔG₂ for D2EHPA vs PC88A)

### The Practical Workflow

#### Step 1: Compute Each ΔG Term

For a given system (e.g., La³⁺ + D2EHPA in kerosene at pH 3, 298 K):

1.  Compute ΔG₁ using SMD solvation (La³⁺ in water)
2.  Compute ΔG₂ using DFT or UMA (La³⁺ + 3 D2EHPA → La(D2EHPA)₃)
3.  Compute ΔG₃ using SMD (complex in kerosene model)
4.  Compute ΔG₄ using SMD (D2EHPA in kerosene)
5.  Use literature value for ΔG°₅ = -3300 kJ/mol (or fit to data)

#### Step 2: Sum to Get ΔG°~extraction~

    ΔG°_extraction = ΔG₁ + ΔG₂ + ΔG₃ + ΔG₄ + ΔG°₅

#### Step 3: Convert to K~ex~

    log K°_ex = -ΔG°_extraction / (2.303 RT)

#### Step 4: Apply pH Correction

    log K_ex(pH) = log K°_ex + 3 pH

Or equivalently:

    log K_ex = -(ΔG₁ + ΔG₂ + ΔG₃ + ΔG₄ + ΔG°₅) / (2.303RT) + 3 pH

#### Step 5: Convert to Distribution Ratio D

    log D = log K_ex + 3 log[(HL)₂]_org - 3 pH

          = log K°_ex + 3 pH + 3 log[(HL)₂]_org - 3 pH

          = log K°_ex + 3 log[(HL)₂]_org

Wait, the pH cancels! That's because we already included it in the K~ex~ definition.

Actually, the correct formulation is:

    From the equilibrium: K_ex = ([REEL₃]_org × [H⁺]³_aq) / ([REE³⁺]_aq × [(HL)₂]³_org)

    Rearranging: D = [REEL₃]_org / [REE³⁺]_aq = K_ex × [(HL)₂]³_org / [H⁺]³_aq

    Therefore: log D = log K_ex + 3 log[(HL)₂]_org + 3 pH

So:

    log D = [-(ΔG₁ + ΔG₂ + ΔG₃ + ΔG₄ + ΔG°₅)/(2.303RT)] + 3 log[(HL)₂]_org + 3 pH

#### Step 6: Compare with Experimental log D

A validation dataset supplies experimental log D values. Compare:

    Error = log D_predicted - log D_experimental

Calculate:

- MAE (mean absolute error)
- RMSE
- R² correlation
- % within ±0.5 log units

### Key Takeaways

1.  **The thermodynamic cycle connects atomistic calculations (DFT/UMA) to measurable K~ex~**

2.  **ΔG₂ (binding energy) is the term computed with machine learning** — this is where different REEs and extractants differ most

3.  **Absolute K~ex~ prediction is challenging** (±150 kJ/mol errors → ±25 log units!)

4.  **Relative predictions (selectivity) are more robust** - systematic errors cancel

5.  **Calibration against experimental data** is essential

6.  **Focus on trends and rankings** rather than absolute values

7.  **The pH dependence (+3 slope) comes from the stoichiometry**, not the cycle - it's built into the K~ex~ definition

The workflow is:

``` example
DFT/UMA → ΔG₂ → Sum cycle → ΔG°_extraction → log K°_ex → Apply pH → log K_ex → Add extractant conc. → log D → Compare with expt.
```

## Microcalorimetry for Liquid-Liquid Extraction Thermodynamics
Microcalorimetry, particularly **Isothermal Titration Calorimetry (ITC)**, has emerged as a key technique for directly measuring the heats of reaction during liquid-liquid extraction of metal ions. This allows determination of complete thermodynamic profiles (ΔH, ΔS, ΔG) for ion transfer between aqueous and organic phases in both extraction and stripping directions.

### Experimental Techniques
#### Two-Phase Calorimetry (Direct ITC Measurement)
The foundational work on two-phase calorimetry was developed using the **HDEHP (bis(2-ethylhexyl) phosphoric acid)/lanthanide** system as a model. Key findings:

- Enthalpies of extraction of lanthanide ions by HDEHP from aqueous nitrate solutions have been determined using isothermal titration microcalorimetry
- Validation: Calorimetric ΔH values agree well with **van't Hoff analysis** of temperature-dependent distribution coefficients
- First direct calorimetric measurements of heat of liquid-liquid partitioning for transuranic elements (Am³⁺)

**Reference:** [Two-Phase Calorimetry: Studies on Thermodynamics of Lanthanide Extraction by HDEHP](https://www.researchgate.net/publication/244611960_Two-Phase_Calorimetry_I_Studies_on_the_Thermodynamics_of_Lanthanide_Extraction_by_Bis2-EthylHexyl_Phosphoric_Acid)

#### Van't Hoff Analysis (Indirect Method)
- Plot ln(D) vs 1/T to obtain ΔH and ΔS from slope and intercept
- Valid over small temperature ranges (15-40°C) where ΔH and ΔS are approximately constant
- Results typically agree with direct calorimetric measurements within experimental error

**Reference:** [Thermodynamic Parameters of Am(III), Cm(III) and Eu(III) Extraction](https://centaur.reading.ac.uk/86832/1/MS-Thermodynamic_parameters_revised_v190915_all%20(1).pdf)

### Thermodynamic Results by Extractant System
#### HDEHP/D2EHPA Systems
| Parameter | Observation                                              |
|-----------|----------------------------------------------------------|
| ΔH_extr   | Exothermic: −35 kJ/mol (La³⁺) to −27 kJ/mol (Yb³⁺)       |
| Am³⁺      | ΔH_extr ≈ −36 kJ/mol                                     |
| Trend     | Slight increase (less negative) across lanthanide series |
| Entropy   | Negative ΔS (increase in order)                          |

The **entropy-enthalpy compensation effect** has been observed - less compact hydration zones of light lanthanides are disrupted more readily, reducing the energetic cost of dehydration.

#### TOPO Systems
| Parameter | Value                                                        |
|-----------|--------------------------------------------------------------|
| ΔH_extr   | Constant \~29 kJ/mol from La³⁺-Er³⁺                          |
| Tm³⁺-Lu³⁺ | Slight decrease observed                                     |
| Method    | Complete ΔG, ΔH, ΔS sets for Eu(NO₃)₃, Am(NO₃)₃ and Cm(NO₃)₃ |

**Reference:** [OSTI Thermodynamics Studies](https://www.osti.gov/etdeweb/servlets/purl/20176396)

#### Diglycolamide (DGA) Systems
TODGA and related DGAs show:

- **Enthalpy-driven extraction** for Am(III) and U(VI)
- **Both enthalpy and entropy favorable** for Pu(IV)
- Novel unsymmetrical DGA: ΔH = −64.94 kJ/mol, ΔS = −144.42 J/(mol·K)
- Complexation shows **negative ΔH with positive ΔS** - driven by both factors

**References:**

- [Chemistry of Diglycolamides (Chemical Reviews)](https://pubs.acs.org/doi/10.1021/cr200002f)
- [Temperature Influence on TODGA Extraction](https://link.springer.com/article/10.1007/s10967-024-09902-y)
- [TODGA Thermodynamics (IAEA)](https://inis.iaea.org/records/5cbkn-fw635)

#### Ionic Liquid Systems
Lanthanide extraction into **Bumim·Tf₂N** with HTTA:

| Species            | ΔH° (kJ/mol) | ΔS° (J/mol·K) |
|--------------------|--------------|---------------|
| Nd(TTA)²⁺          | +4.81        | +128          |
| Nd(TTA)₂⁺          | +17.4        | +134          |
| Nd(TTA)₃           | +23.3        | +94           |
| Nd(TTA)₄⁻          | +37.9        | +112          |
| Overall extraction | +42.5        | --            |

Key insight: **Endothermic complexation** driven by **favorable entropy** in ionic liquid media.

**Reference:** [RSC - Complexation Thermodynamics of Lanthanides in Ionic Liquids](https://pubs.rsc.org/en/content/articlelanding/2023/nj/d2nj05314d/unauth)

### Thermodynamics of Stripping (Reverse Extraction)
#### General Principles
- **Forward extraction**: Often exothermic (negative ΔH), with stripping requiring reversal of these thermodynamics
- **Stripping mechanisms**: Achieved using acidic aqueous solutions to protonate extractant, releasing metal ion
- Temperature effects on stripping are often less pronounced than on extraction

#### Uranium Stripping Studies
- Extraction: Rapid, exothermic, spontaneous
- Stripping: ΔH values obtained; less temperature-dependent than forward extraction
- Both extraction and stripping thermodynamics can be characterized using van't Hoff analysis

**Reference:** [Nature - Solvent Extraction and Stripping of Uranium with Alamine 336](https://www.nature.com/articles/s41598-025-96421-9)

#### Thermodynamic Balance
The thermochemistry of metal ion partitioning represents a balance between:

1.  **Endothermic**: Metal ion dehydration in aqueous phase
2.  **Exothermic**: Formation of lipophilic complexes in organic phase

For stripping, this balance reverses - breaking organic-phase complexes and rehydrating the metal ion.

### Molecular-Level Insights
#### Ion Transfer at Liquid-Liquid Interfaces
MD simulations reveal:

- **Water/nitrobenzene interface**: Energetic costs include interfacial deformation and co-transfer of hydration waters
- **Free energy profile**: Small local minimum (\~−5.9 kJ/mol) near interface, then monotonic increase into organic phase
- **SCN⁻ at oil-water**: Transfer driven by **entropy increase** with minimal enthalpic contribution (different from air-water interfaces)

**References:**

- [PNAS - Mechanisms of Ion Adsorption to Aqueous Interfaces](https://www.pnas.org/doi/10.1073/pnas.2210857119)
- [Science - Mechanism and Dynamics of Ion Transfer](https://www.science.org/doi/10.1126/science.261.5128.1558)

#### Synergistic Extraction
- Synergy enhances extraction by increasing **entropy of the extracted ion** (final state)
- Reciprocal effect of chelation: enhances final entropy while chelation reduces initial entropy

**Reference:** [ACS Nano - Synergistic Solvent Extraction is Driven by Entropy](https://pubs.acs.org/doi/10.1021/acsnano.9b07605)

### Key Research Groups & Resources
#### Kenneth Nash Group (Washington State University)

- Extensive work on actinide/lanthanide thermodynamics
- Two-phase calorimetry methodology development
- TALSPEAK process thermodynamics

**Reference:** [Nash Group Publications](https://nash.chem.wsu.edu/publications/)

#### Idaho National Laboratory

- Thermodynamics and kinetics of advanced separations
- HDEHP, TOPO, and DGA systems
- First transplutonium calorimetric measurements

**Reference:** [INL Technical Report](https://inldigitallibrary.inl.gov/sites/sti/sti/4781579.pdf)

### Experimental Considerations for ITC in Two-Phase Systems
#### Challenges
1.  Heat measured represents **total process heat** - difficult to distinguish diffusion vs. binding contributions
2.  Buffer matching critical - organic solvent composition must be consistent
3.  Competing reactions (hydrolysis, precipitation) must be controlled
4.  High equilibrium constants (\>10⁴-10⁵ M⁻¹) require specialized protocols

#### Best Practices
- Use well-characterized model systems (HDEHP/Eu³⁺) for method validation
- Compare calorimetric ΔH with van't Hoff analysis for consistency
- Control ionic strength and pH carefully
- Consider using ITC + molecular modeling for mechanistic insights

**Reference:** [ScienceDirect - ITC and Molecular Modeling in Solvent Extraction](https://www.sciencedirect.com/science/article/abs/pii/S1226086X18310049)

### Summary of Thermodynamic Trends
| System          | ΔH_extr                        | ΔS_extr     | Driving Force |
|-----------------|--------------------------------|-------------|---------------|
| HDEHP/Ln³⁺      | Exothermic (−27 to −36 kJ/mol) | Negative    | Enthalpy      |
| TOPO/Ln³⁺       | Exothermic (\~29 kJ/mol)       | Negative    | Enthalpy      |
| TODGA/Am³⁺,U⁶⁺  | Exothermic                     | Unfavorable | Enthalpy      |
| TODGA/Pu⁴⁺      | Exothermic                     | Favorable   | Both          |
| HTTA/Ln³⁺ in IL | Endothermic (+4 to +42 kJ/mol) | Positive    | Entropy       |
| Crown ethers    | Exothermic                     | Negative    | Enthalpy      |

### Recent Developments (2023-2025)
1.  **Thermomorphic ionic liquids** for REE extraction with in-situ thermodynamic characterization
2.  **Combined ITC + MD simulations** for understanding extractant-diluent interactions
3.  **Crown ether systems** for group/individual REE separation with full thermodynamic data
4.  **Nonaqueous solvent extraction (NASX)** systems - quantitative thermodynamic studies still lacking

**References:**

- [Thermomorphic IL Extraction (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1383586624034257)
- [ITC + MD for Binary Mixtures (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0167732221017098)
- [NASX Review (ACS I&EC Research)](https://pubs.acs.org/doi/10.1021/acs.iecr.1c02287)


(linking-dissolution-and-extraction-thermodynamically)=
## Linking Dissolution and Extraction Thermodynamically

### Overview

This document presents a unified thermodynamic framework that connects (i) mineral dissolution of bastnäsite (REECO3F) using acid leaching, and (ii) liquid--liquid extraction (LLE) of rare-earth elements (REEs) using acidic organophosphorus extractants such as D2EHPA and related phosphates. The framework integrates atomistic thermodynamics inspired by first-principles mineral dissolution modeling with empirical and semi-empirical extraction models, providing a pathway toward chemically grounded, computationally extensible benchmarks.

### Bastnäsite Dissolution as a Source of Aqueous REE Chemical Potentials
Bastnäsite (REECO3F, where REE = Y, La, Ce, Pr, Nd, Sm, Gd) is a major rare-earth mineral. Under acidic leaching conditions, it dissolves to release trivalent REE ions into solution. A simplified dissolution reaction is:  
  
REECO3F(s) + 3H+ ⇌ REE3+ + CO2(g) + HF(aq)  
  
In an atomistic thermodynamics framework, the free energy of dissolution can be written as:  
  
ΔG_diss(pH) = μ_REE3+(aq) − μ_REE(solid) + contributions from carbonate and fluoride speciation.  
  
Density functional theory (DFT) provides the solid-state and surface energetics of REE release, while aqueous thermodynamics (hydration, complexation, activity coefficients) provides solution terms. This establishes the aqueous chemical potential μ_REE3+ as a function of pH, ionic strength, and ligand environment.

### Acidic Phosphate Extraction Thermodynamics
Extraction with acidic organophosphorus extractants (HA) proceeds via cation exchange. The dominant extraction reaction for trivalent REEs is:  
  
REE3+(aq) + 3HA(org) ⇌ REEA3(org) + 3H+(aq)  
  
The corresponding extraction equilibrium constant is:  
  
K_ex = (a_REEA3 · a_H+\^3) / (a_REE3+ · a_HA\^3)  
  
The distribution coefficient D is then:  
  
D = C_REE,org / C_REE,aq ≈ K_ex · (a_HA\^3 / a_H+\^3)  
  
Taking logarithms gives a practical working equation:  
  
log D ≈ log K_ex + 3 log\[HA\] − 3 pH + Δγ  
  
where Δγ captures solvent and activity-coefficient effects.

### Solvent and Extractant Effects
Acidic phosphates such as D2EHPA commonly dimerize in nonpolar diluents. Rather than explicitly modeling aggregation equilibria, a simple effective-extractant model can be used:  
  
\[HA\]\_free = \[HA\]\_tot / (1 + K_d \[HA\]\_tot)  
  
Solvent polarity and modifiers are absorbed into solvent-specific K_ex values or activity corrections. This keeps the model simple while retaining predictive capability.

### Linking Dissolution and Extraction via Chemical Potentials
Both dissolution and extraction can be expressed in terms of chemical potentials. The extraction free energy satisfies:  
  
ΔG_ex = −RT ln K_ex  
  
and can be decomposed as:  
  
ΔG_ex ≈ ΔG_bind,org(REEA3) − ΔG_hyd/spec,aq(REE3+) + 3RT ln a_H+  
  
DFT and machine-learning models (e.g., equivariant neural networks trained on REE--ligand binding energies) provide scalable estimates of ΔG_bind,org. Mason-style atomistic dissolution thermodynamics provides μ_REE3+(aq) and its pH dependence. Together, these define a consistent thermodynamic loop from mineral to organic phase.

### Practical Benchmark Workflow
1\. Compute or parameterize bastnäsite dissolution free energies to define aqueous REE availability.  
2. Perform aqueous speciation to obtain free REE3+ activities as a function of pH.  
3. Apply the extraction equilibrium model to compute D values for each REE.  
4. Enforce extractant mass balance for competitive extraction.  
5. Replace fitted K_ex values with atomistically or ML-derived free energies as models mature.

### Scope and Extensions
This framework provides a minimal, extensible benchmark for rare-earth processing. It can be expanded to include Ce redox chemistry, sulfate media, mixed extractants, or kinetic limitations. Most importantly, it enables a chemically interpretable bridge between first-principles mineral chemistry and data-driven ligand discovery for separation science.
