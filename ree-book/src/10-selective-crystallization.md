---
title: Precipitation and Selective Crystallization
---

(precipitation-and-selective-crystallization)=
# Precipitation and Selective Crystallization

{index}`Precipitation <precipitation>` is the oldest rare earth separation technology and it is still
everywhere in modern flowsheets — as a bulk recovery step at the end of a
{index}`solvent extraction` circuit, as an impurity scrub, and, in the single case of
{index}`cerium`, as a genuine separation. This chapter covers both halves of the subject:
the conventional precipitation chemistry that industry runs today, and the
designed molecular crystals that aim to turn precipitation into a selective
separation in its own right.

The conventional half is largely about choosing a precipitant. Oxalate,
hydroxide, carbonate, double sulfate, fluoride, and phosphate each give a
different combination of recovery, purity, filterability, and cost, and the
choice is usually settled by the downstream calcination step rather than by
selectivity — because none of them discriminates well between adjacent
lanthanides. The exception is cerium, which can be oxidised to Ce(IV) and
dropped out of a trivalent mixture cleanly. That exception is instructive: it
works because oxidation state, unlike ionic radius, is a threshold property.

The second half of the chapter asks whether that kind of threshold can be
engineered. Ionic radius varies by only about 0.15 Å across the whole lanthanide
series, and extractants respond to that difference more or less linearly — which
is why they need so many stages. A crystal lattice does not: it either
accommodates an ion or it does not. Selective borate crystallization,
supramolecular cages, and cyclic peptide hosts are all attempts to convert a
gradient in radius into a discontinuity in what precipitates.

## Conventional Precipitation

Precipitation is a fundamental and cost-effective method for group separation of REEs, capable of producing high-purity products when properly optimized. The technique exploits differences in solubility of REE salts with various precipitants [@kim2020characteristics].

### Precipitant Effectiveness Hierarchy
Thermodynamic studies have established the relative precipitation power of common precipitants:

| Precipitant | Relative Power | Primary Application               |
|-------------|----------------|-----------------------------------|
| Oxalate     | Highest        | High-purity REE recovery          |
| Phosphate   | Very High      | Selective LREE precipitation      |
| Fluoride    | High           | REE concentration                 |
| Sulfate     | Moderate       | Double salt formation             |
| Carbonate   | Moderate       | Cost-effective bulk precipitation |
| Hydroxide   | Lower          | pH-controlled separation          |

System pH has a profound effect on determining the chemical species responsible for REE precipitation.

### Oxalate Precipitation
Oxalic acid is the most widely used precipitant for high-purity REE recovery due to its exceptional selectivity and effectiveness ([OSTI 2022](https://www.osti.gov/servlets/purl/1977455)).

**Reaction Stoichiometry:**

    2RE³⁺ + 3C₂O₄²⁻ + 10H₂O → RE₂(C₂O₄)₃·10H₂O ↓

**Key Characteristics:**

- Requires **1.5 mol oxalic acid per mol REE**
- Product purity: **\>98% REE oxides** after roasting
- Avoids co-precipitation of nickel (5× less water for washing vs. hydroxide route)
- Limited in further aqueous processing due to poor solubility
- Ideal for thermal processing pathways

**pH-Dependent Behavior:** Oxalate forms soluble REE complexes at low pH and precipitates as pH increases. The saturation index of REE-oxalate decreases at higher pH due to competition with hydroxide precipitation:

| pH  | La-oxalate SI | La-hydroxide SI |
|-----|---------------|-----------------|
| 7   | 5.76          | -3.81           |
| 8   | 5.48          | -1.99           |

**Selective Oxalate Solubilization (CSEREOX):** The CSEREOX method enables selective solubilization of water-insoluble REE oxalates, allowing efficient extraction even at low initial REE concentrations (\<5%) from processed magnet wastes. LREEs precipitate first due to lower solubility, enabling sequential separation.

### Hydroxide Precipitation
Hydroxide precipitation exploits the decreasing solubility of lanthanide hydroxides from La to Lu as ionic radii decrease ([OLI Systems](https://olisystems.com/resources/blog/modeling-phase-equilibria-and-recovery-of-rare-earth-elements-with-hydroxide-and-organic-ligands/)).

**Solubility Trends:**

- Solubilities show greatest variability in pH 3-9 range
- Above pH 9.5, all REE hydroxides have similar low solubility
- Precipitation pH threshold varies systematically across lanthanide series

**Industrial pH Thresholds:**

| Element/Group | Precipitation pH | Notes                      |
|---------------|------------------|----------------------------|
| Fe³⁺          | 2.5-3.5          | Removed first              |
| Al³⁺          | 4.0-5.0          | Co-precipitates with Th    |
| Th⁴⁺          | 3.5-4.5          | Selective removal possible |
| U⁴⁺           | 4.0-5.5          | Overlaps with REEs         |
| Light REEs    | 6.8-7.5          | Sequential precipitation   |
| Heavy REEs    | 7.0-8.0          | Slightly higher pH         |
| Y             | 6.5-7.5          | Behaves as HREE            |

**Staged Hydroxide Precipitation:** Industrial processes use multi-stage precipitation to sequentially remove impurities before REE recovery:

1.  **Stage 1 (pH 3-4)**: Remove Fe, Al, Th
2.  **Stage 2 (pH 4.5-5.5)**: Remove remaining Th, U
3.  **Stage 3 (pH 6.5-8)**: Precipitate REEs

Over **99% REE precipitation** achieved at pH 6.5, though some Al and \~40% Fe co-precipitate.

**Limitations:**

- Poor selectivity for metal ions (Fe²⁺, Mn²⁺, Zn²⁺) in pH 6-8 range
- Only \~70% REE recovery at circumneutral pH using NaOH alone
- Ammonium hydroxide suppresses REE precipitation up to pH 8

### Carbonate and Bicarbonate Precipitation
Carbonate precipitation offers a cost-effective alternative with good REE recovery [@laskar2025conversion].

**Advantages:**

- Carbonates readily available and inexpensive
- Precipitates easily dissolved in mild acid for further purification
- Particularly effective at high pH
- Na₂CO₃ found most effective for AMD treatment considering cost and performance

**Staged Carbonate Precipitation from AMD:** A three-stage process developed for acid mine drainage:

1.  **Stage 1**: Selective Al precipitation via CO₂ mineralization
2.  **Stage 2**: REE precipitation at controlled pH
3.  **Stage 3**: Co-Mn precipitation via oxidative or ammoniacal treatment

No interference observed between Al and REE precipitation stages when using Na₂CO₃, unlike hydroxide precipitation.

### Double Sulfate Precipitation
Double sulfate salts (Na₂SO₄·RE₂(SO₄)₃·nH₂O) exploit differential solubility between light and heavy REEs.

**Selectivity:**

- LREEs form less soluble double sulfates
- Effective for separating cerium earths from {index}`yttrium` earths
- Most direct recovery method for La, Ce, Nd, Pr from NiMH battery leachates

**Process Conditions:**

- Sodium sulfate addition to REE-bearing sulfate solutions
- Temperature and concentration control critical
- Yields LREE-enriched precipitate with \~57% light REE recovery

### Fluoride Precipitation
Fluoride forms strong complexes with REEs, enabling effective precipitation as REF₃ ([Alfa Chemistry](https://www.alfa-chemistry.com/resources/preparation-method-of-rare-earth-fluoride.html)).

**Synthesis Methods:**

1.  **Hydrofluoric acid precipitation-vacuum dehydration**
2.  **Hydrofluoride fluorination**
3.  **Ammonium hydrogen fluoride (NH₄HF₂) fluorination**

**Applications:**

- REE concentration from dilute solutions
- Production of REE fluorides for {index}`molten salt electrolysis`
- Recovery from electrolytic slag (Nd, Pr, Dy precipitation rates \>87%)

**Caution:** HF handling requires specialized safety protocols.

### Phosphate Precipitation
Phosphate is a powerful precipitant, ranking second only to oxalate in effectiveness.

**Characteristics:**

- Disodium hydrogen phosphate (Na₂HPO₄) used for selective precipitation
- Increases REE precipitation yield at lower pH values
- Can separate REEs from sulfate liquors containing Th⁴⁺ and UO₂²⁺
- Produces rare earth phosphate (REPO₄) intermediate products

### Selective Oxidative Precipitation of Cerium
Cerium separation by oxidation to Ce(IV) is a critical first step in REE purification, as Ce typically comprises up to 50% of ore REE content [@moldoveanu2025separation].

**Principle:** Ce³⁺ is readily oxidized to Ce⁴⁺, which has much lower solubility:

    Ce³⁺ → Ce⁴⁺ + e⁻     E° = 1.74 V
    Ce⁴⁺ + 4OH⁻ → Ce(OH)₄ ↓

**Oxidizing Agents:**

| Oxidant | Effectiveness | Notes |
|----|----|----|
| Potassium permanganate (KMnO₄) | Excellent | Highest Ce precipitation, low other REE loss |
| Hydrogen peroxide (H₂O₂) | Very Good | 80-95% Ce removal at pH 3-5 |
| Peroxysulfate (S₂O₈²⁻) | Good | Historical industrial use |
| Calcium hypochlorite | Good | Used in chloride solutions |
| Ozone (O₃) | Good | Clean oxidant, no residue |

**Performance Data (H₂O₂ Method):**

| Parameter             | Optimal Range      | Result                        |
|-----------------------|--------------------|-------------------------------|
| pH                    | 3-5                | 80-95% Ce removal             |
| H₂O₂ stoichiometry    | 1.5-2× excess      | REE losses \<5%               |
| Ce(OH)₄ precipitation | Fast, quantitative | Rate-limiting: Ce³⁺ oxidation |

**Industrial Molycorp Process:**

1.  Calcination of bastnaesite at 620°C to oxidize Ce³⁺ to Ce⁴⁺
2.  Acidic treatment with 30% HCl to leach trivalent lanthanides
3.  Filtration yields solid CeO₂ concentrate and LREE solution

**Recent Advances:**

- **\>99.8% selective Ce precipitation** achieved using KMnO₄
- Co-precipitation of other REEs maintained below 1.5%
- Manganese ferrite adsorbents for Ce(IV) separation from highly acidic solutions

### Ligand-Assisted Selective Precipitation
Organic ligands and complexing agents enable enhanced selectivity in REE precipitation, representing an emerging approach for challenging separations [@oconnelldanes2022selective; @johnson2023size].

**Supramolecular Encapsulation:** Pre-organized triamidoarene platforms selectively precipitate light REE nitratometalates as supramolecular capsules under acidic biphasic conditions:

- Intra- and intermolecular hydrogen bonds dictate selectivity
- Promotes precipitation and facilitates REE release
- Receptor can be recycled

**"Tug of War" Strategy:** Employs competing ligands with opposite selectivity profiles:

- **Lipophilic ligand** (oil-soluble {index}`diglycolamide`): Binds heavy lanthanides
- **Hydrophilic ligand** (water-soluble bis-lactam-1,10-phenanthroline): Binds light lanthanides
- Result: **Quantitative separation** of lightest (La-Nd) and heaviest (Ho-Lu) lanthanides

**Aminobis(phosphonate) Precipitants:** Alkyl-substituted aminobis(phosphonates) offer exceptional selectivity:

- Recover Th and U from REE concentrates in **15 minutes**
- Separation of adjacent lanthanides comparable or superior to oxalates
- Particularly effective for radioactive element removal

**8-Hydroxyquinoline for Aluminum Removal:**

- Selectively precipitates Al³⁺ from REE leaching solutions
- High selectivity with good precipitate morphology
- Minimal REE entrainment losses

**CEPPA (3-hydroxyphenylphosphoryl propionic acid):**

- At 50°C, pH 1: **90.5% RE³⁺ extraction**, only 9.5% Al³⁺
- Effective selective complexation in feed liquid

**Staged Precipitation with Ligands (AMD Processing):**

| Ligand/Ion | Effect on REE Precipitation      |
|------------|----------------------------------|
| OH⁻        | \~70% recovery at neutral pH     |
| CO₃²⁻      | Increases yield at lower pH      |
| PO₄³⁻      | Increases yield at lower pH      |
| NH₄⁺       | Suppresses precipitation to pH 8 |
| SO₄²⁻      | Moderate, forms double salts     |

### Fractional Crystallization
{index}`Fractional crystallization <selective crystallization>` was the earliest industrial method for REE separation and remains relevant for high-purity production [@forsberg2024separation].

**Principle:** Solubility differences of REE double salts enable separation by temperature or evaporation control:

- Less soluble compounds crystallize first
- More soluble compounds concentrate in mother liquor

**Preferred Compounds:**

| REE Group  | Optimal Double Salt       |
|------------|---------------------------|
| La, Pr, Nd | Ammonium nitrates         |
| Sm, Eu, Gd | Double magnesium nitrates |
| Heavy REEs | Bromates, ethyl sulfates  |

**Advantages:**

- Simple equipment with large capacity per unit volume
- No reagent addition during crystallization
- Easy crystal-mother liquor separation
- Capable of producing individual elements with high purity

**Disadvantages:**

- Multiple (often hundreds of) crystallization stages required
- Time-intensive process
- Largely superseded by solvent extraction for bulk separation

### Impurity Removal by Selective Precipitation
Effective REE recovery requires prior removal of impurities through staged precipitation [@li2025iron].

**{index}`Thorium <thorium>` and Uranium Removal:**

| Method                | Th Removal | U Removal               | REE Loss |
|-----------------------|------------|-------------------------|----------|
| pH 4.8 precipitation  | \~100%     | 97%                     | 20%      |
| Oxalate at pH 1.5     | High       | Low (stays in solution) | Low      |
| MgCO₃ at pH 3.6, 81°C | \~95%      | Variable                | \<3%     |
| TRPO/SiO₂-P adsorbent | \>99%      | \>99%                   | Minimal  |

**Optimal Multi-Stage Impurity Removal:** Using magnesium carbonate with H₂O₂:

- Complete Fe removal at pH 3.5
- \~95% Th removal at pH 3.6
- \~65% Al removal
- TREE losses under 3%

**Radioactive Impurity Considerations:** For high-purity REE products (electronics, phosphors), trace Th and U must be reduced to ppb levels:

- Phosphine oxide modified adsorbents achieve {index}`separation factors <separation factor>` \>15,000
- Equilibrium reached in 30 minutes in 0.1 M HNO₃

### Industrial Process Parameters
**Typical Industrial Precipitation Sequence:**

| Stage | pH Range | Target Species | Precipitant          |
|-------|----------|----------------|----------------------|
| 1     | 2.5-3.5  | Fe³⁺           | NaOH or Na₂CO₃       |
| 2     | 3.5-4.5  | Al³⁺, Th⁴⁺     | NaOH + H₂O₂          |
| 3     | 4.5-5.5  | U⁴⁺/UO₂²⁺      | Na₂CO₃               |
| 4     | --       | Ce⁴⁺           | Oxidant + base       |
| 5     | 6.5-8.0  | Bulk REEs      | Oxalate or carbonate |

**Key Process Considerations:**

- pH control precision: ±0.2 units for selective stages
- Temperature: 50-80°C improves kinetics and selectivity
- Oxidant dosing: Stoichiometric excess (1.5-2×) for Ce oxidation
- Aging time: 30-60 minutes for complete precipitation
- Washing: Oxalate route requires 5× less water than hydroxide

**Recovery Rates by Method:**

| Precipitant    | Typical REE Recovery | Product Purity |
|----------------|----------------------|----------------|
| Oxalic acid    | \>95%                | \>98% REO      |
| Na₂CO₃         | 85-95%               | 90-95% REO     |
| NaOH           | 70-85%               | Variable       |
| Double sulfate | 55-65% (LREE)        | LREE enriched  |

## Selective Crystallization by Molecular Design

### Key Mechanisms for Selectivity

#### Structural Divergence Across the Lanthanide Series

Different lanthanides form different crystal structures under identical conditions due to:

- **Coordination number variations** - Larger early lanthanides (La, Ce) prefer higher coordination numbers than smaller late lanthanides
- **Ligand polymerization diversity** - The same ligand can polymerize differently depending on the metal center
- **Soft/hard donor selectivity** - Soft donors (e.g., Cl⁻) preferentially bind early lanthanides

#### Thermodynamic vs. Kinetic Control
The interplay between thermodynamics and kinetics is complex:

- At **lower supersaturation**: the thermodynamically stable form dominates
- At **higher supersaturation**: kinetic effects can lead to concomitant polymorphism
- **Reaction time** significantly affects which phase crystallizes (as seen in Nd/Dy systems)
- Surface thermodynamics can drive transformations between crystal structures

According to the Stranski-Totomanow conjecture, polymorph selection is governed by the lowest free-energy barrier for nucleation. However, recent research shows that kinetic effects may be unable to fully explain structural transformation in all polymorphic situations.

### Promising Approaches

#### Selective Borate Crystallization

Research from Wang et al. demonstrated that **six distinct borate phases** form under identical conditions across the lanthanide series. The mechanism involves:

- Ln³⁺ coordination alterations
- Borate polymerization diversity (different fundamental building blocks)
- Soft ligand coordination selectivity

Key results:

- One-step quantitative separation of Nd/Dy using density-based flotation
- Nd/Sm separation through controlled reaction kinetics
- Rare earth borates (LnBO₃) are isomorphous with different forms of CaCO₃ depending on the radius of the rare earth ion:
  - LaBO₃, PrBO₃, NdBO₃ crystallize in aragonite structure
  - SmBO₃ crystallizes in H-form
  - TbBO₃, EuBO₃, GdBO₃, DyBO₃, YBO₃ crystallize in vaterite structure

#### Supramolecular M₄L₄ Cage Self-Assembly

Tetrahedral M₄L₄ cages assembled from tris-tridentate ligands exhibit **multivalent cooperative enhancement** of metal ion selectivity:

- Tiny differences in single metal-ligand interactions are **amplified** through cooperativity
- Strong preference for incorporating **smaller lanthanide ions**
- High-precision self-sorting during mixed-metal assembly
- All M₄L₄ cages are stable to excess metal ions and ligands
- Introduction of hydrophobic alkyl groups enables liquid-liquid extraction with water

The advantage of such self-assembled systems lies in that the tiny differences in single metal-ligand interactions can be amplified by the multivalent cooperativity effect, which is beneficial in the separation of metal ions with similar properties.

#### Phenanthroline-Dicarboxylic Acid (H₂PDA) Systems

A 2025 study used 1,10-phenanthroline-2,9-dicarboxylic acid (H₂PDA) with N,N'-dimethylformamide (DMF) and its decomposition products to achieve selective crystallization separation:

| Lanthanide Pair | Separation Factor |
|-----------------|-------------------|
| La/Ce           | 2.0 ± 0.1         |
| La/Sm           | 8.9 ± 0.1         |
| La/Lu           | 26.9 ± 3.1        |

Four structurally distinct lanthanide compounds crystallize from the same DMF/H₂O/TFA solvent system depending on the lanthanide present.

#### Cyclic Peptide Hosts (Biomimetic Approach)

Inspired by natural biomineralization (such as pearl formation), lanthanide-binding cyclic peptides (Lamp) can:

- Recognize Ln³⁺ through **1:1 complexation-precipitation** process
- Form amorphous hydroxide-like precipitates
- Show **high Lu³⁺ selectivity** when acidic amino acid positions are modified
- Operate under ambient conditions in water without organic solvents

The major driving force of Lamp1 in Ln³⁺ recognition is the electrostatic interactions from the side-chain COOH moieties of the acidic amino acids (aspartic acid and glutamic acid). The selectivity was explained by considering:

- Dipole moment
- Lowest unoccupied molecular orbital (LUMO) energy
- Cohesion energy

#### Macrocyclic Chelator Precipitation

Recent work developed cyclen-based macrocyclic chelators that:

- Induce significant **solubility differences** among REE chelates
- Enable selective precipitation from pH-neutral aqueous solution
- Use simple additives (acetate) to form ternary compounds with tuned solubility

A fundamental challenge with this approach: while Ln chelates in solution behave as discrete, independent entities, the growth of a microcrystalline precipitate involves interactions between chelate units. Errors in crystal lattice assembly may incorporate significant amounts of the soluble Ln chelate into the matrix of the insoluble chelate.

#### Reverse-Size Selective Aqueous Complexants

Substitution of pyridyl-2-carboxylic acid pendant arms (macropa) with pyridyl-2-phosphinic acid arms (macrophosphi) gives rise to dramatic enhancement in discrimination between light lanthanides:

- Binding affinity of macrophosphi for La³⁺ is over 5 orders of magnitude higher than for Gd³⁺
- Separation factors of up to 45 achieved for the Ce/La pair in biphasic extraction

### Challenges and Considerations

1.  **Crystal lattice assembly errors** - Soluble Ln chelates can be incorporated into the matrix of insoluble chelates during microcrystalline precipitate growth

2.  **Kinetic vs. thermodynamic products** - Reaction conditions must be carefully controlled to favor the desired phase

3.  **Concomitant polymorphism** - Multiple phases may form simultaneously, requiring post-separation

4.  **Scale-up** - Most demonstrations are at proof-of-concept scale

5.  **Shielded 4f orbitals** - Lanthanide separation remains challenging because the 4f orbitals are shielded, preventing bonding with ligand orbitals

### Design Principles for New Systems

Based on the literature, effective molecular crystal systems for REE separation should:

1.  **Amplify small ionic radius differences** through multivalent cooperative effects
2.  **Provide multiple coordination modes** that favor different lanthanides
3.  **Allow kinetic/thermodynamic control** through adjustable parameters (temperature, solvent, time, pH)
4.  **Form crystalline products with distinct properties** (solubility, density) for physical separation

## Sources

1.  Wang, S. et al. "Rare earth separations by selective borate crystallization." *Nature Communications* 8, 14438 (2017). <https://www.nature.com/articles/ncomms14438>

2.  Yan, L.-L. et al. "A supramolecular lanthanide separation approach based on multivalent cooperative enhancement of metal ion selectivity." *Nature Communications* 9, 3201 (2018). <https://www.nature.com/articles/s41467-018-02940-7>

3.  Yin, J. et al. "Selective Crystallization Separation Driven by Structural Divergence in Lanthanide Mixed-Organic Systems." *Inorganic Chemistry* (2025). <https://pubs.acs.org/doi/10.1021/acs.inorgchem.5c00183>

4.  Hatanaka, T. et al. "Improved Recovery and Selectivity of Lanthanide-Ion-Binding Cyclic Peptide Hosts by Changing the Position of Acidic Amino Acids." *Minerals* 12(2), 148 (2022). <https://www.mdpi.com/2075-163X/12/2/148>

5.  "Selective crystallization strategies for lanthanides." *Chemical Communications* (2025). <https://pubs.rsc.org/en/content/articlelanding/2025/cc/d5cc03636d>

6.  "Macrocyclic Chelators for Aqueous Lanthanide Separations via Precipitation: Toward Sustainable Recycling of Rare-Earths from NdFeB Magnets." *Journal of the American Chemical Society* (2025). <https://pubs.acs.org/doi/10.1021/jacs.5c04150>

7.  Marsh, M. L. et al. "Rationally designed mineralization for selective recovery of the rare earth elements." *Nature Communications* 8, 15670 (2017). <https://www.nature.com/articles/ncomms15670>

8.  Pramanik, S. et al. "Emerging Rare Earth Element Separation Technologies." *European Journal of Inorganic Chemistry* (2024). <https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/ejic.202400064>

9.  "Selective separation of light rare-earth elements by supramolecular encapsulation and precipitation." *Nature Communications* 13, 4590 (2022). <https://www.nature.com/articles/s41467-022-32178-3>

10. Bryantsev, V. S. et al. "Tuning the Separation of Light Lanthanides Using a Reverse-Size Selective Aqueous Complexant." *Inorganic Chemistry* 60(3), 1604-1613 (2021). <https://pubs.acs.org/doi/10.1021/acs.inorgchem.0c02413>

11. "Selective-crystallization strategy for the separation of rare earth elements: A minireview." *Coordination Chemistry Reviews* (2025). <https://www.sciencedirect.com/science/article/abs/pii/S0010854525002565>

12. Forsberg, K. "Separation of Rare Earth Elements by Crystallization." *Special Publications*, Wiley (2024). <https://agupubs.onlinelibrary.wiley.com/doi/10.1002/9781119515005.ch6>
