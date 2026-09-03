---
title: The Landscape of Separation Technologies
---

(the-landscape-of-separation-technologies)=
# The Landscape of Separation Technologies

Part I closes with a map. This chapter sketches the two technologies that
actually run at industrial scale today — {index}`solvent extraction` and {index}`ion exchange` —
and then places every approach in this book on a single comparison, so that the
detailed chapters that follow can be read against a common frame.

Ion exchange deserves particular attention here because it has no chapter of
its own. It is the only route that routinely delivers the ≥99.9999% purities
required for optical and electronic applications, and it does so by displacement
{index}`chromatography` rather than by staging. Its limitation is throughput, which is
why it survives industrially as a polishing step downstream of solvent
extraction rather than as a replacement for it.

The comparison at the end of the chapter is worth reading carefully, and worth
reading sceptically. {index}`Separation factors <separation factor>` quoted for laboratory systems are
measured under conditions chosen to show them at their best; the TRL column is
the honest one. Two technologies in that table are at TRL 9 and everything else
is at 3–7.

## Solvent Extraction (Liquid-Liquid Extraction)
Solvent extraction is the dominant industrial method for REE separation, chosen because high-purity rare earths can be produced in large quantities continuously and economically [@xie2014critical].

### Principle of Operation
Solvent extraction operates on mass transfer between two immiscible phases:

1.  An aqueous solution containing REE ions is mixed with an organic phase containing extractant molecules
2.  REEs selectively transfer to the organic phase, forming complexes with extractant molecules
3.  The phases separate (like oil and vinegar), allowing recovery of concentrated REEs

### Commercial Extractants
Key industrial extractants include:

- **{index}`D2EHPA`** (Di-2-ethylhexyl phosphoric acid)
- **{index}`PC88A`/HEHEHP** (2-ethylhexyl phosphonic acid mono-2-ethylhexyl ester) - industrial standard
- **Versatic 10** (neodecanoic acid)
- **{index}`TBP <TBP (tributyl phosphate)>`** (Tributyl phosphate)
- **{index}`Aliquat 336`** (quaternary ammonium salt)
- **Cyanex® 572** - emerging alternative that reduces acid consumption by \>30% compared to PC88A

### Industrial Scale
- Up to **hundreds of stages** of {index}`mixer-settlers <mixer-settler>` may be required
- Typical purities: **95-99.9%**
- For optical/phosphor-grade materials (5-6 nines purity), ion exchange post-processing is required

### Separation Groups
Industrial processes typically separate REEs into groups:

- **Light REEs (LREEs)**: La, Ce, Pr, Nd
- **Medium REEs**: Sm, Eu, Gd
- **Heavy REEs (HREEs)**: Tb, Dy, Ho, Er, Tm, Yb, Lu, Y

## Ion Exchange
Ion exchange was the predominant method before the 1960s and remains important for ultra-high purity applications [@elouardi2023progress].

### Conventional Ion Exchange Resins
**Advantages:**

- Capable of refining all REEs
- Adaptable to various raw material compositions
- Can achieve purities \>99.99999% (7 nines)

**Disadvantages:**

- Low throughput
- Prolonged batch processes (up to a month)
- High operational costs
- Low concentrations of REEs in solutions

**Resin Types:**

| Resin Type | Functional Group | Application |
|----|----|----|
| Strong acid cation | Sulfonic acid (-SO₃H) | General REE separation |
| Weak acid cation | Carboxylic acid (-COOH) | pH-selective extraction |
| Chelating | Iminodiacetic acid, aminophosphonic | High selectivity |
| Anion exchange | Quaternary ammonium | REE-anionic complex capture |

### Magnetic Ion Exchange Adsorbents
Magnetic adsorbents combine polymer ion-exchange functionality with magnetic particles for easy recovery, representing an emerging approach for REE separation [@molinacaldern2022advances].

**Design Approaches:**

| Approach | Description | Advantages |
|----|----|----|
| Impregnated beads | Magnetite (Fe₃O₄) grown or embedded in polymer beads | Simple fabrication |
| Core-shell | Magnetic core with polymer shell | High magnetic response |
| Composite | Magnetic particles dispersed in polymer matrix | Tunable properties |

**Functional Groups:**

- Sulfonic acid groups for general cation exchange
- Chelating groups (iminodiacetic acid, EDTA-type) for selectivity
- Phosphonic acid groups for enhanced REE binding

**Operational Benefits:**

- Magnetic collection after use eliminates filtration/centrifugation
- Rapid solid-liquid separation
- Reusable through desorption and regeneration
- Demonstrated for heavy metal removal (Cu²⁺, Pb²⁺) with translation to REE recovery

### Polymer Inclusion Beads (µPIBs)
Micro {index}`polymer inclusion beads <polymer inclusion membranes>` represent a recent advance for online separation of critical rare-earth elements from end-of-life permanent magnets [@croft2024online].

**Features:**

- Functionalized polymer phase for selective REE binding
- Magnetic responsiveness for easy recovery
- Designed specifically for magnet recycling applications
- Online separation capability

**Target Applications:**

- {index}`NdFeB` permanent magnet recycling
- Recovery of Nd, Pr, Dy from e-waste
- Separation of critical REEs from non-critical elements

### Ion-Imprinted Polymers (IIPs)
{index}`Ion-imprinted polymers <ion-imprinted polymer>` create binding cavities complementary in size and coordination to target REE ions, enabling high selectivity [@zhao2025ultra].

**Imprinting Process:**

1.  Template REE ion complexed with functional monomers
2.  Cross-linking polymerization around template
3.  Template removal creates selective cavities
4.  Rebinding occurs with high specificity

**Multi-Ion Imprinted Polymers (MIIPs):** Recent developments enable simultaneous imprinting for multiple REEs:

- Cavities for both light and heavy REEs
- Group selectivity (LREE vs. HREE)
- Higher capacity than single-ion IIPs

**Performance Characteristics:**

| Parameter               | Typical Value             |
|-------------------------|---------------------------|
| Selectivity coefficient | 10-100× vs. non-imprinted |
| Adsorption capacity     | 20-100 mg/g               |
| Reusability             | \>10 cycles               |
| Equilibrium time        | 30-120 minutes            |

### Advanced Chelating Resins
Modern chelating resins offer improved selectivity through tailored functional groups:

**Aminophosphonic Acid Resins:**

- Strong affinity for trivalent REEs
- pH-dependent selectivity
- Effective for HREE enrichment

**Diglycolamic Acid Resins:**

- Selective for middle and heavy REEs
- Applied in spent nuclear fuel processing
- High radiation stability

**Bis-picolinic Acid Resins:**

- Exceptionally high selectivity for Am/Cm over lanthanides
- Used in minor actinide separations

## Comparison of Separation Technologies

| Technology | Separation Factor | Purity | Environmental Impact | Scalability | TRL |
|----|----|----|----|----|----|
| Solvent Extraction | 2-10 (per stage) | 95-99.9% | High (organic solvents) | Industrial | 9 |
| Ion Exchange | High | \>99.9999% | Moderate | Industrial | 9 |
| Membrane Separation | Variable | \>90% | Low | Pilot | 5-7 |
| MOF Nanotraps | 270-800 | High | Low | Lab | 3-4 |
| Lanmodulin | High | \>99.9% | Very Low | Pilot | 4-5 |
| Flash Joule Heating | High | \>90% | Very Low | Lab | 3-4 |
| Supramolecular | High | \>95% | Low | Lab | 4-5 |
| Molten Salt Electrolysis | N/A (reduction) | \>99% | Moderate | Industrial | 9 |

*TRL = Technology Readiness Level (1-9 scale)*
