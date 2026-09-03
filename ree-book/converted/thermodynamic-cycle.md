# The Goal: Predict K~ex~ from First Principles

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

# Problem: Can\'t Compute ΔG~extraction~ Directly

We **cannot** directly compute the free energy for the overall reaction:

    REE³⁺(aq) + 3 HL(org) → REEL₃(org) + 3 H⁺(aq)

Why not?

1.  Mixing phases (aqueous and organic) in one calculation is difficult
2.  Solvation in kerosene (complex mixture) not well-defined
3.  Need to handle both charged species (REE³⁺, H⁺) and neutral complexes

**Solution**: Break into a thermodynamic cycle using gas phase as reference!

# The Thermodynamic Cycle: Five Steps

## Overview

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

## Step-by-Step Breakdown

### ΔG₁: Dehydration of REE³⁺

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

### ΔG₂: Gas-Phase Complexation (THE CRITICAL TERM)

    REE³⁺(gas) + 3 HL(gas) → REEL₃(gas)

    ΔG₂ = G[REEL₃(gas)] - G[REE³⁺(gas)] - 3×G[HL(gas)]

**Physical meaning**: Formation of REE-extractant bonds (coordination chemistry)

**Always negative** (exothermic): Strong electrostatic and covalent bonding

**This is what your ML model predicts!**

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

### ΔG₃: Solvation of Complex in Organic Phase

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

### ΔG₄: Desolvation of Extractant from Organic Phase

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

### ΔG₅: Proton Solvation in Aqueous Phase

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

# Summing the Cycle: Total ΔG~extraction~

## The Sum

    ΔG_extraction = ΔG₁ + ΔG₂ + ΔG₃ + ΔG₄ + ΔG₅

Let\'s trace the path:

1.  REE³⁺(aq) → REE³⁺(gas): ΔG₁ (+ large, \~1300 kJ/mol)
2.  REE³⁺(gas) + 3HL(gas) → REEL₃(gas): ΔG₂ (- large, \~-2500 kJ/mol)
3.  REEL₃(gas) → REEL₃(org): ΔG₃ (- modest, \~-100 kJ/mol)
4.  3HL(org) → 3HL(gas): ΔG₄ (+ modest, \~+200 kJ/mol)
5.  3H⁺(gas) → 3H⁺(aq): ΔG₅ (- very large, \~-3300 - 17pH kJ/mol)

## Typical Values (Example: La + D2EHPA at pH 3)
| Term | Description            | Approximate Value |
|------|------------------------|-------------------|
| ΔG₁  | Dehydration            | +1250 kJ/mol      |
| ΔG₂  | Binding (DFT/UMA)      | -2500 kJ/mol      |
| ΔG₃  | Complex solvation      | -100 kJ/mol       |
| ΔG₄  | Extractant desolvation | +200 kJ/mol       |
| ΔG₅  | Proton hydration       | -3351 kJ/mol      |
| Sum  | **ΔG~extraction~**     | **-4501 kJ/mol**  |

## Converting to K~ex~

    log K_ex = -ΔG_extraction / (2.303 RT)
             = -(-4501 kJ/mol) / (5.706 kJ/mol)
             = +788.8

Wait, that can\'t be right! K~ex~ = 10^788^ is unphysically large!

## The pH Correction

The issue is that ΔG₅ includes the pH-dependent term. We need to separate the standard state from the pH dependence.

The proper formulation is:

    ΔG_extraction = ΔG°_extraction + 3 × RT ln[H⁺]
                  = ΔG°_extraction - 3 × 2.303 RT × pH

So we should write:

    ΔG°_extraction = ΔG₁ + ΔG₂ + ΔG₃ + ΔG₄ + ΔG°₅

Where ΔG°₅ is the **standard** hydration energy (at pH = 0, i.e., \[H⁺\] = 1 M).

## Corrected Calculation

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

# Reality Check: Where Are the Errors?

Experimental values are typically:

- log K~ex~ ≈ 0 to 10 (not 788!)

What\'s wrong?

## Issue 1: Absolute Solvation Energies are Uncertain

The absolute values of:

- ΔG₁ (ion hydration): ±50 kJ/mol uncertainty
- ΔG₂ (DFT binding): ±50-100 kJ/mol uncertainty (this is why UMA has MAE ≈ 25 kJ/mol)
- ΔG°₅ (proton hydration): ±50 kJ/mol uncertainty

These uncertainties **add up** to ±150-200 kJ/mol, which is:

    Δ(log K_ex) ≈ ±200 / 5.706 ≈ ±35 log units!

Huge!

## Issue 2: Standard States and Activity Coefficients

The thermodynamic formulation assumes:

- Activities, not concentrations
- Standard states properly defined
- Activity coefficients = 1

In reality:

- High ionic strength (I = 1-3 M)
- Activity coefficients ≠ 1
- Extractant dimerization not explicitly treated
- Complex may aggregate at high loading

# Practical Solution: Relative Predictions

Given the absolute uncertainty, we focus on **relative** values:

## Approach 1: Predict ΔΔG (Selectivity)

Instead of absolute K~ex~, predict selectivity:

    ΔΔG = ΔG_extraction(REE1) - ΔG_extraction(REE2)

    Separation factor = K_ex(REE1) / K_ex(REE2) = exp(-ΔΔG/RT)

**Why this works**:

- Many systematic errors cancel (ΔG°₅ identical for both REEs)
- ΔG₃, ΔG₄ similar (same extractant, same solvent)
- Main difference: ΔG₁ (different ionic radii) and ΔG₂ (different binding)

## Approach 2: Calibrate with Experimental Data

Use experimental data to correct the absolute scale:

    ΔG_extraction(predicted) = ΔG_extraction(computed) + C

Where C is fitted to match experimental log K~ex~ for 1-2 reference systems.

**Your validation dataset is for this!**

## Approach 3: Focus on Trends

Even if absolute values are off, trends should be correct:

- pH dependence (slope = 3)
- Temperature dependence (via ΔH = ∂ΔG/∂T)
- Solvent effects (relative ΔG₃ for different solvents)
- Extractant comparison (relative ΔG₂ for D2EHPA vs PC88A)

# The Practical Workflow

## Step 1: Compute Each ΔG Term

For a given system (e.g., La³⁺ + D2EHPA in kerosene at pH 3, 298 K):

1.  Compute ΔG₁ using SMD solvation (La³⁺ in water)
2.  Compute ΔG₂ using DFT or UMA (La³⁺ + 3 D2EHPA → La(D2EHPA)₃)
3.  Compute ΔG₃ using SMD (complex in kerosene model)
4.  Compute ΔG₄ using SMD (D2EHPA in kerosene)
5.  Use literature value for ΔG°₅ = -3300 kJ/mol (or fit to data)

## Step 2: Sum to Get ΔG°~extraction~

    ΔG°_extraction = ΔG₁ + ΔG₂ + ΔG₃ + ΔG₄ + ΔG°₅

## Step 3: Convert to K~ex~

    log K°_ex = -ΔG°_extraction / (2.303 RT)

## Step 4: Apply pH Correction

    log K_ex(pH) = log K°_ex + 3 pH

Or equivalently:

    log K_ex = -(ΔG₁ + ΔG₂ + ΔG₃ + ΔG₄ + ΔG°₅) / (2.303RT) + 3 pH

## Step 5: Convert to Distribution Ratio D

    log D = log K_ex + 3 log[(HL)₂]_org - 3 pH

          = log K°_ex + 3 pH + 3 log[(HL)₂]_org - 3 pH

          = log K°_ex + 3 log[(HL)₂]_org

Wait, the pH cancels! That\'s because we already included it in the K~ex~ definition.

Actually, the correct formulation is:

    From the equilibrium: K_ex = ([REEL₃]_org × [H⁺]³_aq) / ([REE³⁺]_aq × [(HL)₂]³_org)

    Rearranging: D = [REEL₃]_org / [REE³⁺]_aq = K_ex × [(HL)₂]³_org / [H⁺]³_aq

    Therefore: log D = log K_ex + 3 log[(HL)₂]_org + 3 pH

So:

    log D = [-(ΔG₁ + ΔG₂ + ΔG₃ + ΔG₄ + ΔG°₅)/(2.303RT)] + 3 log[(HL)₂]_org + 3 pH

## Step 6: Compare with Experimental log D

Your validation dataset has experimental log D values. Compare:

    Error = log D_predicted - log D_experimental

Calculate:

- MAE (mean absolute error)
- RMSE
- R² correlation
- % within ±0.5 log units

# Success Metrics from Your SOW

## Phase 1 (Feasibility):

- Predict **trends** correctly (heavy vs light REE)
- Or K~ex~ within ±1-2 log units (corresponds to ±6-12 kJ/mol in ΔG)
- This is reasonable given UMA MAE ≈ 25 kJ/mol

## Phase 2 (Development):

- Systematic predictions across all 7 REEs
- MAE \< 0.5 log units for log D
- Generate K~ex~(pH, T) surfaces

## Phase 3 (Discovery):

- Use for high-throughput screening
- Relative predictions good enough to rank candidates
- Validate top 10-20 predictions experimentally

# Key Takeaways

1.  **The thermodynamic cycle connects atomistic calculations (DFT/UMA) to measurable K~ex~**

2.  **ΔG₂ (binding energy) is the term you compute with ML** - this is where different REEs and extractants differ most

3.  **Absolute K~ex~ prediction is challenging** (±150 kJ/mol errors → ±25 log units!)

4.  **Relative predictions (selectivity) are more robust** - systematic errors cancel

5.  **Calibration with experimental data** from your validation dataset is essential

6.  **Focus on trends and rankings** rather than absolute values for Phase 1-2

7.  **The pH dependence (+3 slope) comes from the stoichiometry**, not the cycle - it\'s built into the K~ex~ definition

The workflow is:

``` example
DFT/UMA → ΔG₂ → Sum cycle → ΔG°_extraction → log K°_ex → Apply pH → log K_ex → Add extractant conc. → log D → Compare with expt.
```
