# Thermodynamic Framework Linking Bastnäsite Dissolution and Rare-Earth Extraction by Acidic Phosphates

## Overview

This document presents a unified thermodynamic framework that connects (i) mineral dissolution of bastnäsite (REECO3F) using acid leaching, and (ii) liquid--liquid extraction (LLE) of rare-earth elements (REEs) using acidic organophosphorus extractants such as D2EHPA and related phosphates. The framework integrates atomistic thermodynamics inspired by first-principles mineral dissolution modeling with empirical and semi-empirical extraction models, providing a pathway toward chemically grounded, computationally extensible benchmarks.

## 1. Bastnäsite Dissolution as a Source of Aqueous REE Chemical Potentials
Bastnäsite (REECO3F, where REE = Y, La, Ce, Pr, Nd, Sm, Gd) is a major rare-earth mineral. Under acidic leaching conditions, it dissolves to release trivalent REE ions into solution. A simplified dissolution reaction is:  
  
REECO3F(s) + 3H+ ⇌ REE3+ + CO2(g) + HF(aq)  
  
In an atomistic thermodynamics framework, the free energy of dissolution can be written as:  
  
ΔG_diss(pH) = μ_REE3+(aq) − μ_REE(solid) + contributions from carbonate and fluoride speciation.  
  
Density functional theory (DFT) provides the solid-state and surface energetics of REE release, while aqueous thermodynamics (hydration, complexation, activity coefficients) provides solution terms. This establishes the aqueous chemical potential μ_REE3+ as a function of pH, ionic strength, and ligand environment.

## 2. Acidic Phosphate Extraction Thermodynamics
Extraction with acidic organophosphorus extractants (HA) proceeds via cation exchange. The dominant extraction reaction for trivalent REEs is:  
  
REE3+(aq) + 3HA(org) ⇌ REEA3(org) + 3H+(aq)  
  
The corresponding extraction equilibrium constant is:  
  
K_ex = (a_REEA3 · a_H+\^3) / (a_REE3+ · a_HA\^3)  
  
The distribution coefficient D is then:  
  
D = C_REE,org / C_REE,aq ≈ K_ex · (a_HA\^3 / a_H+\^3)  
  
Taking logarithms gives a practical working equation:  
  
log D ≈ log K_ex + 3 log\[HA\] − 3 pH + Δγ  
  
where Δγ captures solvent and activity-coefficient effects.

## 3. Solvent and Extractant Effects
Acidic phosphates such as D2EHPA commonly dimerize in nonpolar diluents. Rather than explicitly modeling aggregation equilibria, a simple effective-extractant model can be used:  
  
\[HA\]\_free = \[HA\]\_tot / (1 + K_d \[HA\]\_tot)  
  
Solvent polarity and modifiers are absorbed into solvent-specific K_ex values or activity corrections. This keeps the model simple while retaining predictive capability.

## 4. Linking Dissolution and Extraction via Chemical Potentials
Both dissolution and extraction can be expressed in terms of chemical potentials. The extraction free energy satisfies:  
  
ΔG_ex = −RT ln K_ex  
  
and can be decomposed as:  
  
ΔG_ex ≈ ΔG_bind,org(REEA3) − ΔG_hyd/spec,aq(REE3+) + 3RT ln a_H+  
  
DFT and machine-learning models (e.g., equivariant neural networks trained on REE--ligand binding energies) provide scalable estimates of ΔG_bind,org. Mason-style atomistic dissolution thermodynamics provides μ_REE3+(aq) and its pH dependence. Together, these define a consistent thermodynamic loop from mineral to organic phase.

## 5. Practical Benchmark Workflow
1\. Compute or parameterize bastnäsite dissolution free energies to define aqueous REE availability.  
2. Perform aqueous speciation to obtain free REE3+ activities as a function of pH.  
3. Apply the extraction equilibrium model to compute D values for each REE.  
4. Enforce extractant mass balance for competitive extraction.  
5. Replace fitted K_ex values with atomistically or ML-derived free energies as models mature.

## 6. Scope and Extensions
This framework provides a minimal, extensible benchmark for rare-earth processing. It can be expanded to include Ce redox chemistry, sulfate media, mixed extractants, or kinetic limitations. Most importantly, it enables a chemically interpretable bridge between first-principles mineral chemistry and data-driven ligand discovery for separation science.
