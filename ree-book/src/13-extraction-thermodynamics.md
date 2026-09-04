---
title: Thermodynamics of Extraction
---

(thermodynamics-of-extraction)=
# Thermodynamics of Extraction

Every {index}`separation factor` in this book is, underneath, a difference of free
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

## Predicting $K_\mathrm{ex}$ from First Principles

We want to predict the equilibrium constant $K_\mathrm{ex}$ of the extraction
reaction

$$
\mathrm{REE}^{3+}(\mathrm{aq}) + 3\,\mathrm{HL}(\mathrm{org}) \rightleftharpoons \mathrm{REEL}_3(\mathrm{org}) + 3\,\mathrm{H}^{+}(\mathrm{aq})
$$

The standard thermodynamic relationship is

$$
\Delta G^\circ_\mathrm{extraction} = -RT \ln K_\mathrm{ex}
$$

and therefore

$$
\log K_\mathrm{ex} = -\frac{\Delta G^\circ_\mathrm{extraction}}{2.303\,RT}
$$

At 298 K:

- RT = 8.314 J/(mol·K) × 298 K = 2.478 kJ/mol
- 2.303 RT = 5.706 kJ/mol

So: $\log K_\mathrm{ex} = -\Delta G^\circ_\mathrm{extraction} / 5.706$, with $\Delta G$ in kJ/mol.

### Problem: Can't Compute $\Delta G_\mathrm{extraction}$ Directly

We **cannot** directly compute the free energy for the overall reaction

$$
\mathrm{REE}^{3+}(\mathrm{aq}) + 3\,\mathrm{HL}(\mathrm{org}) \rightarrow \mathrm{REEL}_3(\mathrm{org}) + 3\,\mathrm{H}^{+}(\mathrm{aq})
$$

Why not?

1.  Mixing phases (aqueous and organic) in one calculation is difficult
2.  Solvation in kerosene (complex mixture) not well-defined
3.  Need to handle both charged species (REE³⁺, H⁺) and neutral complexes

**Solution**: Break into a thermodynamic cycle using gas phase as reference!

### The Thermodynamic Cycle: Five Steps

#### Overview

We construct a cycle where all species pass through the gas phase:

The reaction we are trying to reach is

$$
\mathrm{REE}^{3+}(\mathrm{aq}) + 3\,\mathrm{HL}(\mathrm{org}) \rightleftharpoons \mathrm{REEL}_3(\mathrm{org}) + 3\,\mathrm{H}^{+}(\mathrm{aq})
$$

and the protons on the right are not optional bookkeeping: they carry three
units of charge and are the reason the equilibrium responds to pH at all. Every
step of the cycle has to conserve them.

:::{figure} ../figures/13-thermo-cycle.svg
:name: fig-thermo-cycle
:width: 100%

The extraction cycle, with the La + D2EHPA numbers from the table below. Read
around the loop: up the two left arrows into the gas phase, across the top,
down the two right arrows. The figure is drawn from
`tools/figures/fig_thermo_cycle.py`.
:::

Read around the loop in [](#fig-thermo-cycle). Charge is +3 on both sides at
every point, and three protons enter the top-right corner and leave at the
bottom. The version of this
cycle that omits them — writing ΔG₂ as
$\mathrm{REE}^{3+}(\mathrm{g}) + 3\,\mathrm{HL}(\mathrm{g}) \rightarrow \mathrm{REEL}_3(\mathrm{g})$,
neutral on the right — is short by three gas-phase deprotonations, roughly
+4,000 kJ/mol, and no amount of care with the other four terms will recover it.

#### Step-by-Step Breakdown

##### ΔG₁: Dehydration of REE³⁺

$$
\mathrm{REE}^{3+}(\mathrm{aq}) \rightarrow \mathrm{REE}^{3+}(\mathrm{g})
$$

$$
\Delta G_1 = G[\mathrm{REE}^{3+}(\mathrm{g})] - G[\mathrm{REE}^{3+}(\mathrm{aq})]
$$

**Physical meaning**: Remove REE³⁺ from water (break ion-dipole interactions)

**Always positive** (ΔG₁ > 0; the reverse, hydration, is what is tabulated):
\~3100-3500 kJ/mol for lanthanide +3 ions

**Computational method**:

- Option 1: Implicit solvation (SMD model in Gaussian/ORCA)

  $$
  \Delta G_1 = E(\mathrm{REE}^{3+}\ \text{in vacuum}) - E(\mathrm{REE}^{3+}\ \text{with SMD water})
  $$

- Option 2: Empirical correlations (Born model)

  $$
  \Delta G_\mathrm{solv} \approx -\frac{z^2 e^2 N_A}{8 \pi \varepsilon_0 r_\mathrm{ion}} \left( 1 - \frac{1}{\varepsilon_r} \right)
  $$

  Where z=3, $r_\mathrm{ion}$ ≈ 1.0-1.2 Å for REE³⁺, $\varepsilon_r$ = 78.4 for water

**Key insight**: ΔG₁ varies across the lanthanide series with ionic radius.
Experimental hydration free energies [@marcus1991thermodynamics]:

- La³⁺ (largest): ΔG₁ ≈ +3145 kJ/mol
- Gd³⁺: ΔG₁ ≈ +3375 kJ/mol
- Lu³⁺ (smallest): ΔG₁ ≈ +3515 kJ/mol

That is a 370 kJ/mol spread across the series, and it is one of the two terms
that carries selectivity. Note that the Born expression above, with z = 3 and
r = 1.0-1.2 Å, returns 5,000-6,000 kJ/mol: it overestimates trivalent-ion
hydration by roughly 1.7× and is useful for trends, not for magnitudes.

##### ΔG₂: Gas-Phase Complexation (THE CRITICAL TERM)

$$
\mathrm{REE}^{3+}(\mathrm{g}) + 3\,\mathrm{HL}(\mathrm{g}) \rightarrow \mathrm{REEL}_3(\mathrm{g}) + 3\,\mathrm{H}^{+}(\mathrm{g})
$$

$$
\Delta G_2 = G[\mathrm{REEL}_3(\mathrm{g})] + 3\,G[\mathrm{H}^{+}(\mathrm{g})] - G[\mathrm{REE}^{3+}(\mathrm{g})] - 3\,G[\mathrm{HL}(\mathrm{g})]
$$

**Physical meaning**: The extractant gives up three protons and its three
conjugate bases coordinate the metal. It is useful to split this into the two
physical processes it contains:

$$
\Delta G_2 = \underbrace{3\,\Delta G_\mathrm{acid}(\mathrm{HL})}_{\text{gas-phase deprotonation}} + \underbrace{\Delta G_\mathrm{assoc}(\mathrm{REE}^{3+} + 3\,\mathrm{L}^{-} \rightarrow \mathrm{REEL}_3)}_{\text{ion-ion association}}
$$

The first piece runs about +1,300 to +1,400 kJ/mol per proton, so around
+4,000 kJ/mol for three, and the second is around −4,200, so **ΔG₂ is a small
residual between two enormous numbers**. Its sign is not obvious in advance and
neither piece can be dropped.

**This is the term a machine-learned binding model predicts** — which makes it
essential to state which of the two reactions a published "binding energy"
refers to. A model trained on
$\mathrm{REE}^{3+} + 3\,\mathrm{L}^{-} \rightarrow \mathrm{REEL}_3$ is not interchangeable with
one trained on the proton-conserving reaction above; they differ by ~4,000
kJ/mol, and papers are not always explicit about which they report.

**Computational method**:

The direct route is DFT: optimize the geometry of the REEL₃ complex and of each
isolated species, then take the difference of the electronic energies with the
appropriate thermal and entropic corrections,

$$
\Delta G_2 = G[\mathrm{REEL}_3(\mathrm{g})] + 3\,G[\mathrm{H}^{+}(\mathrm{g})] - G[\mathrm{REE}^{3+}(\mathrm{g})] - 3\,G[\mathrm{HL}(\mathrm{g})]
$$

which for a complex of three bulky organophosphorus ligands is hours of compute
per candidate, and more if conformers are searched properly
([](#high-throughput-and-computational-methods) makes the case that they must be).

The surrogate route replaces that calculation with a model trained on it.
@gupta2025accelerating trained equivariant neural networks (Allegro) on 5,356
REE-ligand complexes and predict binding energy from structure with a mean
absolute error of 6.1 kcal/mol (\~25 kJ/mol), in seconds rather than hours.
Universal machine-learned potentials trained on broad inorganic datasets are a
third option, but their published errors are for structures and formation
energies of solids, not for lanthanide-organic binding, and should not be
assumed to transfer to this quantity without a test set of its own.

**Key variations**:

- Different REEs have different binding strengths
- Different extractants ({index}`D2EHPA` vs. {index}`PC88A` vs. {index}`TBP <TBP (tributyl phosphate)>`) give different ΔG₂
- This is the **primary source of selectivity** in gas phase

**Magnitudes**: with the protons conserved, ΔG₂ for the lanthanides with
acidic organophosphorus extractants is on the order of ±100 kJ/mol — a residual,
not a large binding energy. The *difference* between two adjacent lanthanides is
a few kJ/mol, and that difference is the entire selectivity.

##### ΔG₃: Solvation of Complex in Organic Phase

$$
\mathrm{REEL}_3(\mathrm{g}) \rightarrow \mathrm{REEL}_3(\mathrm{org})
$$

$$
\Delta G_3 = G[\mathrm{REEL}_3\ \text{in kerosene}] - G[\mathrm{REEL}_3(\mathrm{g})]
$$

**Physical meaning**: Stabilization of neutral complex in organic solvent

**Always negative**: Complex is stabilized by dispersion forces with kerosene

**Computational method**:

****Option 1: Implicit solvation****

- SMD model with $\varepsilon_r$ ≈ 2 (kerosene dielectric constant)

- Treats kerosene as uniform dielectric medium

  $$
  \Delta G_3 = E(\mathrm{REEL}_3\ \text{with SMD}, \varepsilon_r = 2) - E(\mathrm{REEL}_3\ \text{in vacuum})
  $$

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
- Kerosene vs. dodecane vs. {index}`ionic liquids`
- Different solvents → different ΔG₃ → different extraction efficiency

##### ΔG₄: Desolvation of Extractant from Organic Phase

$$
3\,\mathrm{HL}(\mathrm{org}) \rightarrow 3\,\mathrm{HL}(\mathrm{g})
$$

$$
\Delta G_4 = 3 \left( G[\mathrm{HL}(\mathrm{g})] - G[\mathrm{HL}\ \text{in kerosene}] \right)
$$

**Physical meaning**: Remove extractant from kerosene (break HL-solvent interactions)

**Always positive**: Costs energy to pull HL out of organic phase

**Computational method**:

****Option 1: Implicit solvation (same as ΔG₃)****

$$
\Delta G_4 = 3 \left( E(\mathrm{HL}\ \text{in vacuum}) - E(\mathrm{HL}\ \text{with SMD}, \varepsilon_r = 2) \right)
$$

****Option 2: Experimental vaporization enthalpy****

- For D2EHPA, TBP: $\Delta H_\mathrm{vap}$ data available from literature
- Approximate ΔG₄ ≈ 3 × $\Delta H_\mathrm{vap}$ (neglecting entropy)

****Option 3: Cancel with ΔG₃ in first approximation****

- If same solvation model used for both
- Partial cancellation of organic phase solvation effects

**Typical values**:

- ΔG₄ ≈ +150 to +300 kJ/mol (for 3 × HL)

##### ΔG₅: Proton Solvation in Aqueous Phase

$$
3\,\mathrm{H}^{+}(\mathrm{g}) \rightarrow 3\,\mathrm{H}^{+}(\mathrm{aq})
$$

$$
\Delta G_5 = 3 \left( G[\mathrm{H}^{+}(\mathrm{aq})] - G[\mathrm{H}^{+}(\mathrm{g})] \right)
$$

**Physical meaning**: Hydration of protons released during extraction

**Always negative**: Protons are **very strongly** hydrated (forms H₃O⁺ and H₉O₄⁺ clusters)

**Computational method**:

****Standard state correction****: The free energy of H⁺(aq) depends on pH:

$$
\begin{aligned}
G[\mathrm{H}^{+}(\mathrm{aq})] &= G^\circ[\mathrm{H}^{+}(\mathrm{aq})] + RT \ln [\mathrm{H}^{+}] \\
&= G^\circ[\mathrm{H}^{+}(\mathrm{aq})] - 2.303\,RT \cdot \mathrm{pH}
\end{aligned}
$$

**Standard value** (literature):

- G°[H⁺(aq)] - G[H⁺(gas)] ≈ -1104 kJ/mol (single proton hydration
  [@tissandier1998proton])

**Total for 3 protons**:

$$
\begin{aligned}
\Delta G_5 &= 3 \left( G^\circ[\mathrm{H}^{+}(\mathrm{aq})] - 2.303\,RT \cdot \mathrm{pH} - G[\mathrm{H}^{+}(\mathrm{g})] \right) \\
&= 3\,\Delta G^\circ_\mathrm{hydration} - 3 \times 2.303\,RT \cdot \mathrm{pH} \\
&\approx -3312 - 5.706 \times 3 \times \mathrm{pH} \quad \text{kJ/mol} \\
&\approx -3312 - 17.1\,\mathrm{pH} \quad \text{kJ/mol}
\end{aligned}
$$

**Key insight**: The pH appears explicitly here!

### Summing the Cycle: Total $\Delta G_\mathrm{extraction}$

#### The Sum

$$
\Delta G^\circ_\mathrm{extraction} = \Delta G_1 + \Delta G_2 + \Delta G_3 + \Delta G_4 + \Delta G^\circ_5
$$

Tracing the path, with orders of magnitude for a light lanthanide and an acidic
organophosphorus extractant:

1.  REE³⁺(aq) → REE³⁺(g): ΔG₁ (+ very large, \~+3150 kJ/mol)
2.  3HL(org) → 3HL(g): ΔG₄ (+ modest, \~+200 kJ/mol)
3.  REE³⁺(g) + 3HL(g) → REEL₃(g) + 3H⁺(g): ΔG₂ (small residual of two \~4000
    kJ/mol terms, \~±100 kJ/mol)
4.  REEL₃(g) → REEL₃(org): ΔG₃ (− modest, \~−120 kJ/mol)
5.  3H⁺(g) → 3H⁺(aq): ΔG°₅ (− very large, \~−3312 kJ/mol)

Note what steps 1 and 5 do to each other. Stripping the water off a REE³⁺ ion
costs +3150 kJ/mol; hydrating the three protons that replace it returns −3312.
**They cancel to within about 5%**, and the residual is the same order as ΔG₂.
The cycle is not a sum of a large term and some corrections; it is a difference
of four large terms whose near-cancellation is the entire physical content.

#### Typical Values (La + D2EHPA, standard state)

| Term | Description            | Value        | Where it comes from             |
|------|------------------------|--------------|---------------------------------|
| ΔG₁  | Dehydration            | +3145 kJ/mol | experiment [@marcus1991thermodynamics] |
| ΔG₄  | Extractant desolvation | +200 kJ/mol  | implicit solvation, estimated   |
| ΔG₂  | Complexation + 3 H⁺    | *computed*   | DFT or a learned surrogate      |
| ΔG₃  | Complex solvation      | −120 kJ/mol  | implicit solvation, estimated   |
| ΔG°₅ | Proton hydration       | −3312 kJ/mol | experiment [@tissandier1998proton] |
| Sum of the four known terms |         | **−87 kJ/mol** |                       |

#### Converting to $K_\mathrm{ex}$

$$
\log K_\mathrm{ex} = -\frac{\Delta G^\circ_\mathrm{extraction}}{2.303\,RT}
$$

with 2.303 RT = 5.706 kJ/mol at 298 K.

Now run the requirement backwards. Experimental log $K_\mathrm{ex}$ for these systems
falls between roughly 0 and 10, so $\Delta G^\circ_\mathrm{extraction}$ must land between 0 and
−57 kJ/mol. With the four known terms summing to −87, **ΔG₂ has to fall between
+30 and +87 kJ/mol** — a window 57 kJ/mol wide, on a quantity assembled from a
+4,000 kJ/mol deprotonation and a −4,200 kJ/mol association.

That is the real difficulty, and it is worth stating as a number: predicting
log $K_\mathrm{ex}$ from first principles requires ΔG₂ to about **1% of its own
constituents**. It has nothing to do with the chemistry being subtle and
everything to do with the arithmetic being a difference of large numbers.

### Reality Check: Where Are the Errors?

Two failure modes, and it is important to keep them apart.

#### Failure 1: The cycle does not close (mis-specification)

If the cycle is written without the three protons on ΔG₂ — as
$\mathrm{REE}^{3+}(\mathrm{g}) + 3\,\mathrm{HL}(\mathrm{g}) \rightarrow \mathrm{REEL}_3(\mathrm{g})$,
neutral on the right — then the three gas-phase
deprotonations, roughly +4,000 kJ/mol, are simply missing. The sum comes out
near −4,450 kJ/mol and

$$
\log K_\mathrm{ex} = 4450 / 5.706 \approx 780
$$

which is not a large error, it is a different reaction. **A result of 10⁷⁸⁰ is
never noise**; it is a diagnostic that a term of ~4,000 kJ/mol is absent. Check
that charge and atom counts balance around the loop before looking anywhere
else.

#### Failure 2: The cycle closes but the terms are uncertain (numerical error)

Once the cycle balances, the honest error budget is:

- ΔG₁ (ion hydration): ±20 kJ/mol — the tabulated values depend on the
  extrathermodynamic split of a measured salt into single ions
- ΔG°₅ (proton hydration): ±10 kJ/mol, and it is *common to all lanthanides*
- ΔG₃, ΔG₄ (implicit solvation of neutrals in a hydrocarbon): ±20 kJ/mol each,
  and partially cancelling since the same model is used for both
- ΔG₂ (DFT): ±50-100 kJ/mol; a learned surrogate at 6.1 kcal/mol MAE adds
  ±25 kJ/mol on top of whatever the training data inherited

Taken in quadrature this is ±60-120 kJ/mol, or **±10-20 log units** on an
absolute log $K_\mathrm{ex}$ whose true value is between 0 and 10. Absolute prediction is
therefore out of reach, and saying so plainly is more useful than reporting a
number to three figures.

#### Failure 3: Standard states and activity coefficients

The formulation above assumes activities equal concentrations. In a real
circuit:

- ionic strength is 1-3 M and activity coefficients are not 1
- extractant dimerization is not treated explicitly (see below)
- the complex aggregates at high loading, and can form a third phase

These are second-order next to Failure 2, but they set a floor on how well any
calibration can transfer between systems.

### Practical Solution: Relative Predictions

Given the absolute uncertainty, we focus on **relative** values:

#### Approach 1: Predict ΔΔG (Selectivity)

Instead of absolute $K_\mathrm{ex}$, predict selectivity:

$$
\Delta\Delta G = \Delta G_\mathrm{extraction}(\mathrm{REE}_1) - \Delta G_\mathrm{extraction}(\mathrm{REE}_2)
$$

from which the separation factor follows as

$$
\beta = \frac{K_\mathrm{ex}(\mathrm{REE}_1)}{K_\mathrm{ex}(\mathrm{REE}_2)} = \exp\left(-\frac{\Delta\Delta G}{RT}\right)
$$

**Why this works**:

- Many systematic errors cancel (ΔG°₅ identical for both REEs)
- ΔG₃, ΔG₄ similar (same extractant, same solvent)
- Main difference: ΔG₁ (different ionic radii) and ΔG₂ (different binding)

(the-energy-scale-of-selectivity)=
##### The energy scale this has to reach

It is worth inverting that expression and asking how large ΔΔG actually is,
because the answer sets the accuracy target for everything in
[](#high-throughput-and-computational-methods) and it is rarely stated.

At 298 K, RT = 2.48 kJ/mol, so ΔΔG = RT ln β:

| β (adjacent pair) | ΔΔG (kJ/mol) | ΔΔG (kcal/mol) |
|-------------------|--------------|----------------|
| 1.4               | 0.83         | 0.20           |
| 1.5               | 1.01         | 0.24           |
| 2.0               | 1.72         | 0.41           |
| 3.0               | 2.72         | 0.65           |

**The entire industry runs on one to three kilojoules per mole.** Take the
Pr/Nd split, the hardest one in the light-rare-earth train
([](#solvent-extraction-fundamentals)): β ≈ 1.4-1.5 is ΔΔG ≈ 0.9 kJ/mol, about
a fifth of a kilocalorie, or roughly a third of the thermal energy available at
room temperature.

Now compare that against the error bars on the terms it is a difference of. A
DFT ΔG₂ carries ±50-100 kJ/mol; a learned surrogate at 6.1 kcal/mol MAE carries
±25 kJ/mol [@gupta2025accelerating]. Predicting the Pr/Nd separation factor to
even a factor of two therefore requires the errors in two separate ΔG₂
calculations to cancel to about **96 % for the surrogate and 99 % for DFT**.

That is the real premise of the computational programme, and it is a defensible
one: the two calculations differ only in which lanthanide sits at the centre of
an otherwise identical complex, so most of the error is genuinely common and
does cancel. But it is a premise, not a result. It should be *demonstrated* —
by predicting a whole series and checking that the ordering and the spacing come
out, not by reporting an absolute number to three figures. A method validated
only on absolute $K_\mathrm{ex}$ has been validated on the quantity that does not matter.

#### Approach 2: Calibrate with Experimental Data

Use experimental data to correct the absolute scale:

$$
\Delta G_\mathrm{extraction}(\text{predicted}) = \Delta G_\mathrm{extraction}(\text{computed}) + C
$$

Where C is fitted to match experimental log $K_\mathrm{ex}$ for 1-2 reference systems.

**This is what an experimental validation dataset is for.**

#### Approach 3: Focus on Trends

Even if absolute values are off, trends should be correct:

- pH dependence (slope = +3)
- Temperature dependence, via the Gibbs-Helmholtz relation
  $\partial(\Delta G/T)/\partial(1/T) = \Delta H$ — equivalently
  $\Delta S = -\partial \Delta G/\partial T$, which is the identity
  the van't Hoff analysis later in this chapter uses
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

#### Step 2: Sum to Get $\Delta G^\circ_\mathrm{extraction}$

$$
\Delta G^\circ_\mathrm{extraction} = \Delta G_1 + \Delta G_2 + \Delta G_3 + \Delta G_4 + \Delta G^\circ_5
$$

#### Step 3: Convert to $K_\mathrm{ex}$

$$
\log K_\mathrm{ex} = -\frac{\Delta G^\circ_\mathrm{extraction}}{2.303\,RT}
$$

#### Step 4: Convert to a Distribution Ratio

There is no separate "pH correction" to apply. $K_\mathrm{ex}$ is an equilibrium constant
and does not depend on pH; the pH dependence appears when the mass-action
expression is rearranged for D, because H⁺ is a product of the extraction
reaction:

$$
K_\mathrm{ex} = \frac{[\mathrm{REEL}_3]_\mathrm{org}\,[\mathrm{H}^{+}]^3_\mathrm{aq}}{[\mathrm{REE}^{3+}]_\mathrm{aq}\,[(\mathrm{HL})_2]^3_\mathrm{org}}
$$

$$
D = \frac{[\mathrm{REEL}_3]_\mathrm{org}}{[\mathrm{REE}^{3+}]_\mathrm{aq}} = K_\mathrm{ex}\,\frac{[(\mathrm{HL})_2]^3_\mathrm{org}}{[\mathrm{H}^{+}]^3_\mathrm{aq}}
$$

$$
\log D = \log K_\mathrm{ex} + 3 \log [(\mathrm{HL})_2]_\mathrm{org} + 3\,\mathrm{pH}
$$

Substituting the result of Step 3,

$$
\log D = -\frac{\Delta G_1 + \Delta G_2 + \Delta G_3 + \Delta G_4 + \Delta G^\circ_5}{2.303\,RT} + 3 \log [(\mathrm{HL})_2]_\mathrm{org} + 3\,\mathrm{pH}
$$

One cycle calculation therefore predicts a whole family of log D values — one
for every pH and extractant loading. Only the intercept comes from the
calculation; the slopes are fixed by the stoichiometry, which is why they are
the part of this expression experiment agrees with
([](#solvent-extraction-fundamentals)).

#### Step 5: Compare with Experimental log D

A validation dataset supplies experimental log D values. Compare them term by
term, $\text{error} = \log D_\mathrm{predicted} - \log D_\mathrm{experimental}$, and
report:

- MAE (mean absolute error)
- RMSE
- R² correlation
- % within ±0.5 log units

### Key Takeaways

1.  **The thermodynamic cycle connects atomistic calculations (DFT, or a learned surrogate for the binding step) to measurable $K_\mathrm{ex}$**

2.  **ΔG₂ (binding energy) is the term computed with machine learning** — this is where different REEs and extractants differ most

3.  **Absolute $K_\mathrm{ex}$ prediction is out of reach** — ±60-120 kJ/mol on the sum is ±10-20 log units on a quantity whose true value spans 0-10

4.  **Selectivity lives on a 1-3 kJ/mol scale** (ΔΔG = RT ln β; β = 1.5 is 1.0 kJ/mol), so every computational claim about separation rests on 96-99 % error cancellation between two nearly identical calculations — see [](#the-energy-scale-of-selectivity)

5.  **Calibration against experimental data** is essential

6.  **Focus on trends and rankings** rather than absolute values

7.  **The pH dependence (+3 slope) comes from the stoichiometry**, not from the cycle: $K_\mathrm{ex}$ itself is pH-independent, and the slope appears only when the mass-action expression is rearranged for D

The workflow is:

```text
DFT or learned surrogate → ΔG₂ → sum cycle → ΔG°_extraction → log K_ex → add pH and extractant concentration → log D → compare with expt.
```

## Microcalorimetry for Liquid-Liquid Extraction Thermodynamics
Microcalorimetry, particularly **Isothermal Titration Calorimetry (ITC)**, has emerged as a key technique for directly measuring the heats of reaction during {index}`liquid-liquid extraction <solvent extraction>` of metal ions. This allows determination of complete thermodynamic profiles (ΔH, ΔS, ΔG) for ion transfer between aqueous and organic phases in both extraction and stripping directions.

### Experimental Techniques
#### Two-Phase Calorimetry (Direct ITC Measurement)
The foundational work on two-phase calorimetry was developed using the **{index}`HDEHP` (bis(2-ethylhexyl) phosphoric acid)/lanthanide** system as a model. Key findings:

- Enthalpies of extraction of lanthanide ions by HDEHP from aqueous nitrate
  solutions have been determined using isothermal titration microcalorimetry
  [@zalupski2008two]
- Validation: calorimetric ΔH values agree well with **van't Hoff analysis** of
  temperature-dependent distribution coefficients
- The same methodology gave the first direct calorimetric measurement of the
  heat of liquid-liquid partitioning of a transuranic element, Am³⁺ transferred
  from pH 3.2 nitrate solution into 0.2 M HDEHP in *n*-dodecane
  [@martin2010thermodynamics]

#### Van't Hoff Analysis (Indirect Method)
- Plot ln(D) vs 1/T to obtain ΔH and ΔS from slope and intercept
- Valid over small temperature ranges where ΔH and ΔS are approximately
  constant. Distler and co-workers work over 15-45 °C, and take the reaction
  enthalpy and entropy from the distribution coefficients measured there; note
  that this is the indirect route throughout, with no calorimetry to check it
  against [@distler2020thermodynamic]

### Thermodynamic Results by Extractant System
#### HDEHP/D2EHPA Systems

Two-phase calorimetry on HDEHP in *n*-dodecane gives an exothermic heat of
transfer opposed by an unfavourable entropy term, the entropy penalty coming
from the ordering of the extracted complex together with the rehydration of the
three protons exchanged back into the aqueous phase [@martin2010thermodynamics].
Am³⁺ falls on the lanthanide ΔG, ΔH and ΔS trend lines at the radius where
Pm³⁺ would sit, which is what a purely electrostatic picture of a hard-donor
extractant predicts.

#### Malonamide Diamide (DMDBTDMA) Systems

Malonamide diamides extract the neutral metal nitrate rather than exchanging
cations, and one of the few enthalpy series measured right across the
lanthanides belongs to them, so they are worth putting alongside the
organophosphorus numbers. For 0.5 M DMDBTDMA in TPH — a
hydrogenated-tetrapropylene kerosene diluent — extracting La, Nd, Eu, Er, Yb and
Am nitrates from 3 M HNO₃ [@charbonnel2000thermodynamics]:

| Parameter | Observation                                              |
|-----------|----------------------------------------------------------|
| ΔH_extr   | Exothermic: −35 kJ/mol (La³⁺) to −27 kJ/mol (Yb³⁺)       |
| Am³⁺      | ΔH_extr ≈ −36 kJ/mol                                     |
| Trend     | Slight increase (less negative) across lanthanide series |
| Method    | van't Hoff, cross-checked against titration calorimetry  |

The van't Hoff and calorimetric enthalpies for Nd³⁺ agree to within a few
kJ/mol, which is the cross-validation the two methods exist to provide. The same
work shows that the diamide concentration and the aqueous-phase composition move
the reaction enthalpy substantially, so a single ΔH quoted without its medium is
not transferable.

#### Diglycolamide (DGA) Systems
{index}`TODGA` and related DGAs show:

- **Enthalpy-driven extraction** for Am(III) and U(VI), with the entropy term
  working against extraction [@ansari2006extraction]
- **Both enthalpy and entropy favorable** for Pu(IV) [@ansari2006extraction]
- Complexation shows **negative ΔH with positive ΔS** - driven by both factors

**References:** [@ansari2011chemistry; @sharov2024specific]

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

**Reference:** [@gujar2023complexation]

### Thermodynamics of Stripping (Reverse Extraction)
#### General Principles
- **Forward extraction**: Often exothermic (negative ΔH), with stripping requiring reversal of these thermodynamics
- **Stripping mechanisms**: Achieved using acidic aqueous solutions to protonate extractant, releasing metal ion
- Temperature effects on stripping are often less pronounced than on extraction

#### Uranium Stripping Studies
- Extraction: Rapid, exothermic, spontaneous
- Stripping: ΔH values obtained; less temperature-dependent than forward extraction
- Both extraction and stripping thermodynamics can be characterized using van't Hoff analysis

**Reference:** [@zahakifar2025solvent]

#### Thermodynamic Balance
The thermochemistry of metal ion partitioning represents a balance between:

1.  **Endothermic**: Metal ion dehydration in aqueous phase
2.  **Exothermic**: Formation of lipophilic complexes in organic phase

For stripping, this balance reverses - breaking organic-phase complexes and rehydrating the metal ion.

### Molecular-Level Insights
#### Ion Transfer at Liquid-Liquid Interfaces
MD simulations reveal:

- **Water/nitrobenzene interface**: Energetic costs include interfacial deformation and co-transfer of hydration waters [@karnes2016geometric]
- **Free energy profile**: Small local minimum (\~−5.9 kJ/mol) near interface, then monotonic increase into organic phase
- **SCN⁻ at oil-water**: Transfer driven by **entropy increase** with minimal enthalpic contribution (different from air-water interfaces)

**References:**

- [@devlin2022mechanisms]
- [@benjamin1993mechanism]

#### Synergistic Extraction
- Synergy enhances extraction by increasing **entropy of the extracted ion** (final state)
- Reciprocal effect of chelation: enhances final entropy while chelation reduces initial entropy

**Reference:** [@spadina2019synergistic]

### Where This Body of Work Comes From

Most of the two-phase calorimetry cited above traces to one lineage. The
solution chemistry of the trivalent f-elements that the method rests on was set
out by Nash [@nash1993basic]; the two-phase calorimetric methodology itself was
developed on the HDEHP/lanthanide system by Zalupski and Nash
[@zalupski2008two]; and it was carried into the TALSPEAK-relevant regime and
extended to Am³⁺ at Idaho National Laboratory [@martin2010thermodynamics]. The
diamide numbers come from an independent French line of work on the DIAMEX
process [@charbonnel2000thermodynamics]. Nothing here should be read as a
survey of the field's activity — these are the specific measurements the
sections above depend on.

### Experimental Considerations for ITC in Two-Phase Systems
#### Challenges
1.  Heat measured represents **total process heat** - difficult to distinguish diffusion vs. binding contributions
2.  Buffer matching critical - organic solvent composition must be consistent
3.  Competing reactions (hydrolysis, {index}`precipitation`) must be controlled
4.  High equilibrium constants (\>10⁴-10⁵ M⁻¹) require specialized protocols

#### Best Practices
- Use well-characterized model systems (HDEHP/Eu³⁺) for method validation
- Compare calorimetric ΔH with van't Hoff analysis for consistency
- Control ionic strength and pH carefully
- Consider using ITC + molecular modeling for mechanistic insights

**Reference:** [@sprakel2019improving]

### Summary of Thermodynamic Trends
| System          | ΔH_extr                        | ΔS_extr     | Driving Force |
|-----------------|--------------------------------|-------------|---------------|
| HDEHP/Ln³⁺      | Exothermic                     | Negative    | Enthalpy      |
| DMDBTDMA/Ln³⁺   | Exothermic (−27 to −36 kJ/mol) | Negative    | Enthalpy      |
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

- [@papadopoulou2025extraction]
- [@coquil2022interactions]
- [@li2021nonaqueous]


(linking-dissolution-and-extraction-thermodynamically)=
## Linking Dissolution and Extraction Thermodynamically

The cycle above begins with REE³⁺ already dissolved. That ion had to come from a
mineral, and [](#hydrometallurgical-leaching) is where it did. The two halves of
the process share one variable — the chemical potential of REE³⁺ in the aqueous
phase — so they can be written in a single set of books. This section does that
for {index}`bastnäsite` leached in acid and then extracted with an acidic
organophosphorus extractant. It is deliberately the crudest version that closes:
atomistic thermodynamics on the mineral side, an empirical cation-exchange model
on the extraction side, and the aqueous chemical potential as the quantity the
two must agree on. What it buys is a benchmark in which a change to the mineral
chemistry and a change to the ligand chemistry are expressed in the same units.

### Bastnäsite Dissolution as a Source of Aqueous REE Chemical Potentials

Bastnäsite (REECO₃F, where REE is dominantly La, Ce, Pr and Nd) is a major
rare-earth mineral. Under acidic leaching conditions it dissolves to release
trivalent REE ions into solution; a simplified dissolution reaction is

$$
\mathrm{REECO_3F(s)} + 3\,\mathrm{H}^{+} \rightleftharpoons \mathrm{REE}^{3+} + \mathrm{CO_2(g)} + \mathrm{HF(aq)} + \mathrm{H_2O}
$$

In an atomistic thermodynamics framework the free energy of dissolution is

$$
\Delta G_\mathrm{diss}(\mathrm{pH}) = \mu_{\mathrm{REE}^{3+}(\mathrm{aq})} - \mu_\mathrm{REE(solid)} + \text{carbonate and fluoride speciation terms}
$$

Density functional theory supplies the solid-state and surface energetics of REE
release, while aqueous thermodynamics (hydration, complexation, activity
coefficients) supplies the solution terms. Together they fix the aqueous
chemical potential $\mu_{\mathrm{REE}^{3+}}$ as a function of pH, ionic strength
and ligand environment.

### Acidic Phosphate Extraction Thermodynamics

Extraction with acidic organophosphorus extractants (HA) proceeds by cation
exchange. The dominant extraction reaction for trivalent REEs is

$$
\mathrm{REE}^{3+}(\mathrm{aq}) + 3\,\mathrm{HA}(\mathrm{org}) \rightleftharpoons \mathrm{REEA_3}(\mathrm{org}) + 3\,\mathrm{H}^{+}(\mathrm{aq})
$$

with extraction equilibrium constant

$$
K_\mathrm{ex} = \frac{a_{\mathrm{REEA_3}}\,a_{\mathrm{H}^{+}}^{3}}{a_{\mathrm{REE}^{3+}}\,a_{\mathrm{HA}}^{3}}
$$

The distribution coefficient follows as

$$
D = \frac{C_\mathrm{REE,org}}{C_\mathrm{REE,aq}} \approx K_\mathrm{ex}\,\frac{a_{\mathrm{HA}}^{3}}{a_{\mathrm{H}^{+}}^{3}}
$$

and taking logarithms gives the practical working equation

$$
\log D \approx \log K_\mathrm{ex} + 3 \log [\mathrm{HA}] + 3\,\mathrm{pH} + \Delta\gamma
$$

where $\Delta\gamma$ absorbs solvent and activity-coefficient effects. This is
the working equation the cycle produced earlier in the chapter, written in
activities rather than concentrations and with dimerisation folded into
$[\mathrm{HA}]$ instead of shown explicitly.

### Solvent and Extractant Effects

Acidic phosphates such as D2EHPA dimerise in nonpolar diluents. Rather than
model the aggregation equilibria explicitly, a simple effective-extractant form
can be used,

$$
[\mathrm{HA}]_\mathrm{free} = \frac{[\mathrm{HA}]_\mathrm{tot}}{1 + K_d\,[\mathrm{HA}]_\mathrm{tot}}
$$

with solvent polarity and modifiers absorbed into solvent-specific
$K_\mathrm{ex}$ values or activity corrections. That keeps the model small at
the price of making $K_\mathrm{ex}$ non-transferable between diluents.

### Linking Dissolution and Extraction via Chemical Potentials

Both dissolution and extraction can be written in chemical potentials. The
extraction free energy satisfies

$$
\Delta G_\mathrm{ex} = -RT \ln K_\mathrm{ex}
$$

and decomposes as

$$
\Delta G_\mathrm{ex} \approx \Delta G_\mathrm{bind,org}(\mathrm{REEA_3}) - \Delta G_\mathrm{hyd/spec,aq}(\mathrm{REE}^{3+}) + 3RT \ln a_{\mathrm{H}^{+}}
$$

DFT and machine-learning models — equivariant neural networks trained on
REE-ligand binding energies, for instance [@gupta2025accelerating] — give
scalable estimates of $\Delta G_\mathrm{bind,org}$, and atomistic dissolution
thermodynamics gives $\mu_{\mathrm{REE}^{3+}(\mathrm{aq})}$ and its pH
dependence. Together they close a loop from mineral to organic phase. The
caveats of the first half of this chapter apply here in full: the loop closes on
paper, and the absolute numbers it produces are not yet trustworthy.

### Practical Benchmark Workflow

1.  Compute or parameterise bastnäsite dissolution free energies to define
    aqueous REE availability.
2.  Perform aqueous speciation to obtain free REE³⁺ activities as a function of
    pH.
3.  Apply the extraction equilibrium model to compute D values for each REE.
4.  Enforce extractant mass balance for competitive extraction.
5.  Replace fitted $K_\mathrm{ex}$ values with atomistically or ML-derived free
    energies as the models earn it.

### Scope and Extensions

That is a minimal, extensible benchmark for rare-earth processing, not a
predictive model. It can be widened to Ce redox chemistry, sulfate media, mixed
extractants or kinetic limitations, and its value is that mineral chemistry and
ligand chemistry are stated in one currency — so a claim made on either side can
be checked against the other.
