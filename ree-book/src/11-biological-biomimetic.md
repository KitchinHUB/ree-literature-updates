---
title: Biological and Biomimetic Separations
---

(biological-and-biomimetic-separations)=
# Biological and Biomimetic Separations

Biology solved selective lanthanide binding before chemistry did. {index}`Lanmodulin <lanmodulin>`, a
bacterial protein discovered in methylotrophs that use lanthanides as enzyme
cofactors, binds them with roughly a hundred-million-fold preference over
calcium — a discrimination no synthetic extractant approaches. That single
result reframes the separation problem: the reason conventional processes need
hundreds of stages is not that the underlying differences are too small to
exploit, but that the ligands in use are the wrong shape to exploit them.

This chapter covers what has been built on that observation. Protein and peptide
systems come first, since they carry the highest selectivities and the clearest
mechanistic picture. Then the routes that trade selectivity for robustness and
cost: biosurfactants, microbial {index}`biosorption`, {index}`bioleaching`, and phytomining. The
economics run in the opposite direction from the selectivity — the most
selective systems are the most fragile and the most expensive to produce, and
the least selective are the ones already operating in the field.

The coacervate systems in [](#coacervates-and-aqueous-biphasic-systems) are the
natural process vehicle for these ligands, since both work in aqueous media
under mild conditions.

This section provides an in-depth examination of biosurfactants, peptides, proteins, and related biological approaches for REE separation---representing some of the most promising sustainable technologies in this field.

(lanmodulin-structure-mechanism-and-engineering)=
## Lanmodulin: Structure, Mechanism, and Engineering
### Discovery and Properties
Lanmodulin (LanM) is a 12 kDa protein identified in *Methylobacterium extorquens*, a methylotrophic bacterium that requires lanthanides for methanol metabolism. LanM is the most selective macromolecule for REEs characterized to date, even outperforming many synthetic chelators [@deblonde2020selective].

**Key Binding Properties:**

| Property | Value |
| ---------- | ------- |
| Selectivity Ln³⁺/Ca²⁺ | 100,000,000-fold |
| Dissociation constant (Kd) | 0.4-10 pM across lanthanide series |
| pH stability | Retains binding down to pH ≈ 2.5 |
| Temperature stability | Up to 95°C |
| Competing metal tolerance | Up to molar amounts of Mg, Ca, Zn, Cu |

### Structural Basis of Selectivity
The NMR solution structure reveals LanM's unique architecture [@mattocks2019structural]:

- **Four EF-hand motifs**: Metal coordination sites typically associated with Ca²⁺ binding
- **Unusual fusion of adjacent EF-hands**: Creates a compact fold unique among EF-hand proteins
- **Coordination sphere**: La³⁺ ions coordinated by:
  - Asparagine side chains (monodentate)
  - Aspartate/glutamate carboxylates (bidentate)
  - Backbone carbonyls
  - Total coordination number: 10
  - La³⁺-ligand distances: 2.5-2.7 Å

**Critical Proline Residues:** Each EF-hand contains a crucial proline residue that hampers response to calcium while maintaining lanthanide selectivity. When prolines are mutated to alanine, calcium can induce conformational change at much lower concentrations, demonstrating proline's role in selectivity.

### Metal-Sensitive Dimerization
A breakthrough discovery revealed that lanmodulin from *Hansschlegelia quercus* (Hans-LanM) exhibits oligomeric state sensitivity to rare-earth ionic radius [@cotruvo2023enhanced]:

- **La(III)-induced dimer**: \>100-fold tighter than Dy(III)-induced dimer
- **Mechanism**: Picometre-scale differences in ionic radius propagate to quaternary structure through a "carboxylate shift" that rearranges second-sphere hydrogen bonding
- **Application**: Selective dimerization enriches high-value Pr³⁺/Nd³⁺ relative to low-value La³⁺/Ce³⁺

**Separation Performance:**

- Achieves higher {index}`separation factors <separation factor>` than standard lanmodulins
- Comparable or better than common industrial extractants (e.g., {index}`HDEHP`)
- All-aqueous process without organic solvents

### Protein Engineering and Variants
Computational and experimental studies have revealed key engineering principles [@yao2025computationally]:

**D9 Residue Mutations:**

| Mutation | Effect on Affinity |
| ---------- | ------------------- |
| Asp→Asn | 2-fold decrease |
| Asp→Ala | 20-fold decrease |
| Bulky side chains | Up to 100-fold decrease |

**Key Insights:**

- Amino acids outside direct metal binding motif are crucial for coordination
- Point mutations can induce long-range structural perturbations
- Weak chelators can achieve high selectivity through allosteric mechanisms

### Practical Implementation
**Immobilized Lanmodulin Systems:**

- Conjugated onto porous support materials via thiol-maleimide chemistry
- Enables tandem REE purification and separation under flow-through conditions
- Column systems with multiple adsorption (pH 3) and desorption (pH \<1.7) cycles
- Protein can be reused for many cycles

**Performance from Real Feedstocks:**

- Transforms low-grade leachate (0.043 mol% REEs) into 88 mol% purity fractions
- Uses \~90% of column capacity in single run
- Achieves tandem extraction and grouped separation without organic solvents

## Lanthanide Binding Tags and Peptide-Based Separation
### EF-Hand Derived Peptides
{index}`Lanthanide binding tags <lanthanide binding tags>` (LBTs) are short peptides derived from calcium-binding EF-hand loops that selectively coordinate REE cations [@li2024lanthanide].

**Design Principles:**

- Based on EF-hand metal binding loops from calmodulin, troponin, and parvalbumin
- Typical sequence: YIDTNNDGWYEGDELLA (troponin-derived, Tb³⁺-optimized)
- Net charge of -3 on binding loop creates neutral 1:1 cation:peptide complex

**Selectivity Characteristics:**

- DGA resins: Selectivity at high acid (pH \<1)
- Bioderived ligands: Selectivity at moderate pH (\>3)
- LBT Kd range: 0.9-1.8 μM (immobilized) vs. 0.4-10 pM (full LanM protein)

### Lanmodulin-Derived Peptides
Mimicking lanmodulin with shorter peptides offers advantages [@verma2024investigation]:

**LanM1 Peptide (from EF-hand loop 1):**

- Simpler to produce and manipulate
- Easier to optimize through directed evolution
- Surface-immobilizable for separation technologies
- Maintains REE binding when bound to solid substrates

**Challenges:**

- Lower affinity than full protein
- High affinity doesn't necessarily correlate with high selectivity between REEs

### Foam-Based Interfacial Separation
A novel approach uses peptide surfactants for foam flotation separation [@li2024lanthanide]:

**Mechanism:**

1.  LBT peptides selectively complex with trivalent REE cations
2.  Metal-peptide complexes adsorb to air/aqueous interfaces of bubbles
3.  Foam carries REE-enriched complexes for recovery

**Glutaraldehyde Enhancement:**

- Cross-linking of metal-peptide complexes in solution
- Acts as "facilitating agent" for enhanced surface adsorption
- Significantly improves separation efficiency

**Demonstrated Separations:**

- Selective extraction from equimolar Tb³⁺/La³⁺ mixtures
- Validated LBT-mediated interfacial REE separation

### Gravity-Driven Separation
Microbead technology using immobilized lanthanide binding peptides (LBPs) [@sree2023gravity]:

- Selective adsorption of REEs onto functionalized microbeads
- Gravity-based separation of bound vs. unbound REEs
- Demonstrated enrichment of {index}`Europium <europium>` and {index}`Terbium <terbium>`

### Mineralization Peptides
Lanthanide ion mineralization peptide (Lamp) enables direct extraction [@hatanaka2017rationally]:

**Mechanism:**

1.  Lamp promotes REE hydroxide species generation in aqueous solution
2.  Binds to form hydrophobic complexes
3.  Spontaneous accumulation as insoluble precipitates
4.  Works under physiological conditions (pH \~6.0)

**Applications:**

- Selective separation from seawater
- Industrial wastewater treatment
- No additional energy input required

## EF-Hand Calcium Binding Proteins
### Structural Overview
The EF-hand motif is a helix-loop-helix structural domain found in diverse calcium-binding proteins:

**Key Proteins:**

| Protein | Function | REE Binding |
| --------- | ---------- | ------------- |
| Calmodulin | Ca²⁺ signaling | Strong Ln³⁺ binding |
| Troponin C | Muscle contraction | LBT source sequences |
| Parvalbumin | Ca²⁺ buffering | NMR probe applications |
| S100 proteins | Cell signaling | Eu³⁺ Kd = 660 nM |

### Lanthanide Substitution Properties
Lanthanides can replace Ca²⁺ in EF-hand proteins isomorphously [@edington2018coordination]:

- X-ray crystallography shows lanthanides bind more strongly than calcium
- Proteins retain biochemical activity after Ln³⁺ substitution
- Same degree of conformational changes as with Ca²⁺
- Widely used as luminescent probes (Eu³⁺, Tb³⁺)

**Calmodulin Studies:**

- Ln³⁺ associates with binding pockets more strongly than Ca²⁺
- Though coordination distorts structure slightly, perturbations are small
- Useful for structure-function studies

### Applications for REE Recovery
**Calmodulin-Based Systems:**

- Peptide binding loop conjugated to polymer scaffold particles
- Applied to {index}`cerium` recovery from solution
- Exploits natural EF-hand selectivity

## Biosurfactants for REE Separation
### Rhamnolipid Biosurfactants
Rhamnolipids are glycolipid biosurfactants produced by *Pseudomonas aeruginosa* with strong REE complexation properties [@hogan2017rhamnolipid].

**REE Binding Characteristics:**

Stability constants (log β) place REEs in the "strongly bound" group:

| Element | log β |
| --------- | ------- |
| UO₂²⁺ | 9.82 (highest) |
| Eu³⁺ | \~9.5 |
| Nd³⁺ | \~9.3 |
| Tb³⁺ | \~9.1 |
| Dy³⁺ | \~9.0 |
| La³⁺ | \~8.8 |
| Y³⁺ | \~8.5 |
| Lu³⁺ | 8.20 |

**Key Finding:** REEs are bound more strongly than common soil/water cations, enabling selective recovery.

**Properties:**

- Hydrophilic surfactant
- Biodegradable and environmentally friendly
- Reduces surface tension more effectively than chemical surfactants at same CMC
- Potential green technology for REE recovery

### Sophorolipid Biosurfactants
Sophorolipids (produced by *Starmerella bombicola*) show promise for rare earth mineral flotation:

**Flotation Applications:**

- Evaluated as collectors for ultrafine ceria (model REE mineral)
- Both acidic (ASL) and lactonic (LSL) forms tested
- Compared favorably to petroleum-based collectors like benzohydroxamic acid (BHA)

**Complementary Properties:**

- Sophorolipids: Very hydrophobic
- Rhamnolipids: Hydrophilic
- Mixtures show robust performance in combined applications

### Saponin for Soil Remediation
Non-ionic biosurfactant saponin has been evaluated for REE leaching from contaminated soils [@zhou2018leaching]:

**Performance (25 g/L saponin, 400 mL):**

| Element | Removal Efficiency |
| --------- | ------------------- |
| La | 35.3% |
| Y | 31.5% |
| Eu | 30.8% |
| Ce | 26.1% |

Saponin outperformed rhamnolipid for soil leaching applications.

## Siderophore-Mediated Bioleaching
### Siderophore Overview
Siderophores are extracellular chelating compounds produced by aerobic microorganisms to acquire iron. They also complex REEs effectively for bioleaching applications [@others2019characterization].

### Key Microorganisms
**Aspergillus niger:**

- Produces 87% siderophore units in iron-deficient conditions
- Main siderophore identified as **ferrichrome** (FTIR/NMR confirmed)
- Metabolites weather rock and destroy mineral crystal structures
- REE dissolution via proton exchange, redox, and ligand complexation

**Extraction Performance from Egyptian Phosphorites:**

| Element | Removal Efficiency |
| --------- | ------------------- |
| Uranium | 69.5% |
| Samarium | 66.7% |
| Thorium | 55.0% |
| Lanthanum | 51.0% |
| Cerium | 50.1% |

**Actinobacteria:**

- Four strains tested for bastnaesite-bearing rock bioleaching
- *Streptomyces* strains FXJ1.172 and FXJ1.532 produced 200 and 9.3 µmol/L siderophores
- Secreted organic acids and complexing ligands as dominant extraction agents

### Methylotrophic Bacteria
*Methylobacterium extorquens* AM1 provides a unique approach:

- Natural ability to acquire lanthanides from environment
- First demonstration of REE bioaccumulation/biomineralization in mesophilic bacteria
- Attractive for sustainable bioleaching due to inherent lanthanide metabolism

### Mineral Source Selectivity

Microorganism selection depends on mineral type:

| Mineral Type | Preferred Organisms | Mechanism |
| -------------- | -------------------- | ---------- |
| Iron-bearing (sulfide/oxide) | Siderophore-producing chemoautotrophs | Sc extraction |
| Phosphate-rich | Chemoheterotrophic bacteria | Organic acid secretion |
| Carbonate minerals | Chemoheterotrophic bacteria | Acid dissolution |

## Microbial Biosorption
### Overview
Biosorption is a physicochemical, metabolically-independent process based on absorption, adsorption, {index}`ion-exchange <ion exchange>`, surface complexation, and {index}`precipitation`. It represents a cost-effective, biotechnological approach for REE recovery [@vitova2024microbial].

**Advantages:**

- Large surface area per unit mass
- Abundant cell surface functional groups (carboxylates, phosphates, hydroxyls)
- Good metal coordination capacity
- Biodegradable and non-toxic

### Bacterial Biosorption
**Gram-Positive vs. Gram-Negative Selectivity:**

*Bacillus subtilis* (Gram-positive) showed higher selectivity for heavy REEs (Yb, Lu) compared to Gram-negative species like *Leisingera methylohalidivorans* and *Phaeobacter inhibens* [@breuker2020biosorption].

**Roseobacter-Based Separation:**

- *Roseobacter* sp. AzwK-3b immobilized on assay filter
- pH-dependent adsorption/desorption
- Preprotonation concentrates solution to \~50% of three heaviest lanthanides (Tm, Lu, Yb) in just two passes

**Engineered E. coli Systems [@bonificio2016rare]:**

- OmpA protein functionalized with 16 copies of LBT
- 2-10-fold increase in distribution coefficients for individual REEs
- LBT-display enhances affinity as function of decreasing atomic radius
- Enables separation of high-value heavy REEs from common light REEs

### Yeast Biosorption
Phosphorylated dry baker's yeast (*Saccharomyces cerevisiae*) has demonstrated effective REE adsorption [@ojima2018recovering]:

**Metals Adsorbed:**

- Ce³⁺, Dy³⁺, Gd³⁺, La³⁺, Nd³⁺, Y³⁺, Yb³⁺

**Advantages:**

- Lower biomass requirement for relevant biosorption
- Cost-effective and simple technique
- Eukaryotes (especially fungi/yeasts like *Pichia* sp.) should be prioritized

### Algal Biosorption
**Seaweed (*Sargassum* sp.):**

- Quick and efficient acquisition of Eu, Gd, La, Nd, Pr, Sm

**Microalgae and Moss [@heilmann2021rare]:**

| Organism | Nd³⁺ Capacity | Eu³⁺ Capacity |
| ---------- | --------------- | --------------- |
| *Physcomitrella patens* (moss) | 0.74 mmol/g | 0.48 mmol/g |
| *Calothrix brevissima* | Lower | Lower |
| *Chlorella kessleri* | Lower | Lower |

**Two-Stage Adsorption Process:**

1.  **Passive stage**: Rapid surface uptake
2.  **Active stage**: Slow membrane transport to cytoplasm

Cell wall chemistry determines biosorption efficiency.

## Phytomining and Hyperaccumulator Plants
### Overview
Phytomining uses hyperaccumulator plants to extract REEs from soils, offering an ecologically sound technique for contaminated lands where traditional mining is not competitive.

**Process Stages:**

1.  **Phytoextraction**: REE accumulation in plant tissues
2.  **Enrichment**: Concentration into bio-ores
3.  **Extraction**: REE recovery from harvested biomass

### Dicranopteris linearis (Forked Fern)
The strongest known REE hyperaccumulator [@jally2021method]:

**Accumulation Capacity:**

- Up to **0.7 wt% REEs** in above-ground tissues
- Total REE concentrations: 2-3 mg/g in fronds
- Most abundant: La, Nd, Ce, Pr

**Processing:**

- 92.3% weight reduction after incineration (550°C, 3 hours)
- REEs enriched to **30,000 mg/kg** in ash
- \~11-fold concentration vs. original woody biomass

**Detoxification Mechanism:** \[Silicon-pectin\] matrix fixation protects plant from REE toxicity [@zheng2023rare].

### Blechnum orientale: Biomineralization Discovery (2025)
A groundbreaking discovery of naturally formed REE minerals in living plants [@he2025discovery]:

**Key Findings:**

- **Nanoscale {index}`monazite`** crystals form within extracellular tissues
- Ambient temperature biomineralization process
- Dendritic nanocrystal morphology
- First discovery of REE mineral crystals in living plants

**Advantages of "Biological Monazite":**

- **Pure and non-radioactive** (unlike natural monazite containing U/Th)
- Strong potential for green extraction
- No mining-associated radioactive waste concerns

### Challenges and Future Potential
While promising, phytomining faces hurdles:

- No peer-reviewed studies establishing commercial viability
- Slow accumulation rates
- Land requirements for large-scale operations
- Need for optimized processing of plant biomass

## Biopolymer Adsorbents
### Chitosan-Based Adsorbents
Chitosan, the second most abundant biopolymer, offers exceptional properties for REE recovery [@kore2024application]:

**Properties:**

- Non-toxic and biodegradable
- High adsorption capacity (85-100%)
- Excellent surface area and porosity
- High chelating power and hydrophilicity

**Modifications for Enhanced Performance:**

| Modification                 | REE     | Capacity (mg/g) | Conditions   |
|------------------------------|---------|-----------------|--------------|
| EDTA-magnetic graphene oxide | Ce(III) | 353.28          | pH 7, 25 min |
| Ion imprinted polymer        | Ce(III) | Selective       | pH 7         |
| Acrylic acid graft           | Various | High            | Variable     |

**Key Functional Groups:** C(=O)NH, CN, and C-O-C provide heterogeneous affinity for REE chemical adsorption.

### Cellulose Composites

**Graphene Oxide-Cellulose Systems:**

| Adsorbent | Nd(III) Capacity | Ce(III) Capacity |
| ----------- | ------------------ | ------------------ |
| GO-sodium carboxymethyl cellulose | 661.21 mg/g | 436.55 mg/g |

**Dialdehyde Cellulose-Chitosan:**

- Chemically hybridized via Schiff base reaction
- Followed by acrylic acid graft copolymerization
- High adsorption efficiency for heavy metals

### Modification Strategies
**Cross-linking:**

- Covalent bonds with amine groups
- Increases mechanical strength and chemical stability
- Glutaraldehyde commonly used

**Functionalization:**

- Introduction of new functional groups
- EDTA functionalization creates high-capacity adsorbents
- Example: EDTA-Fe₃O₄-chitosan-CMC nanocomposite: 432.34 mg/g for Pb²⁺

**Composite Materials:**

- {index}`Metal-organic frameworks <metal-organic framework (MOF)>` (MOFs)
- Layered double hydroxides
- Carbon materials
- Clays

## Synthetic Biology and Metabolic Engineering
### Engineered Microbes for Bioleaching
Systems biology-guided engineering has dramatically improved REE extraction [@schmitz2025high]:

**Gluconobacter oxydans Engineering:**

- Whole-genome screening identified key genes
- Deletion of *pstS* gene (phosphate transport)
- Overexpression of *mgdh* gene
- Result: **Up to 73% improvement** in REE extraction

**Transposon Mutant Library:**

- High-throughput genome editing approach
- Disruption of phosphate-specific transport genes
- 18% increase in bioleaching rates

### Scalable Microbial Platforms
**Methylobacterium extorquens AM1 Platform [@good2024scalable]:**

- Grows using electronic waste as sole REE source
- Scalable to 10 L with consistent metal yields
- No harsh acids or high temperatures required
- Engineered overproduction of:
  - REE-binding ligands (lanthanophores)
  - Pyrroloquinoline quinone (PQQ)

### Synthetic Biology for E-Waste Recovery
Advanced approaches for sustainable e-waste processing [@bai2025harnessing]:

**Capabilities Achieved:**

- Higher metal selectivity
- Enhanced tolerance to acidic conditions
- Faster recovery kinetics in complex matrices
- Selective bioleaching, biosorption, and bioaccumulation

**Technologies Applied:**

- Metabolic pathway engineering
- Synthetic gene circuits
- Cell surface display systems
- Directed evolution

### High-Purity REE Biomanufacturing
Microbial synthesis systems achieve active biomanufacturing:

**Affinity Column Systems:**

- Bioconjugated with structurally engineered proteins
- Outstanding separation achieved

**Purity Results:**

| Element Pair | Purity Achieved |
| -------------- | ----------------- |
| Eu recovery | 99.9% |
| La recovery | 97.1% |
| Dy recovery | 92.7% |

## Green Solvents: Deep Eutectic Solvents and Ionic Liquids
### Overview
{index}`Deep eutectic solvents <deep eutectic solvent>` (DESs) and {index}`ionic liquids` (ILs) represent green alternatives to conventional organic solvents for REE separation [@deng2025application].

**Shared Properties:**

- Liquid over wide temperature range
- Non-volatile
- Non-flammable
- Good ionic conductivity

**DES Advantages:**

- Easier preparation (simple mixing of two components)
- Much cheaper than ILs
- Generally less stable than ILs

### Natural Deep Eutectic Solvents (NADESs)
NADESs use natural compounds as components:

- Sugars
- Organic acids
- **Amino acids**
- Organic bases

**Amino Acid-Based DESs:**

- Cheap and natural source
- Biodegradable
- **Important Caveat:** Recent studies show amino acid-based DESs can be unexpectedly toxic---up to 10⁵ times more toxic than conventional choline chloride-based DESs [@li2022high]

### REE Extraction Performance

**Choline Chloride-Urea-Malonic Acid System:**

| Condition | Y Dissolution |
| ----------- | -------------- |
| Without activation | 49% |
| 60 min mechanical activation | 85% |

**IL Extraction Systems:**

- Extracted complexes often different from organic solvent systems
- REE extraction and separation efficiencies significantly enhanced
- Synergistic IL extraction improves extractability and separability

(industrial-challenges)=
### Industrial Challenges
Despite academic promise, commercial breakthroughs have been limited:

- High cost of some ILs
- Stability issues with DESs
- Scale-up challenges
- Toxicity concerns with some formulations
- Need for {index}`life cycle assessment`s

## Comparison of Biological Separation Technologies
| Technology | Selectivity | Scalability | Cost | Environmental Impact | TRL |
|----|----|----|----|----|----|
| Lanmodulin | Exceptional | Pilot scale | Moderate | Very Low | 4-5 |
| LBT Peptides | High | Lab scale | Moderate | Very Low | 3-4 |
| Biosurfactants | Moderate | Pilot scale | Low | Very Low | 4-5 |
| Siderophore Bioleaching | Moderate | Pilot scale | Low | Very Low | 5-6 |
| Microbial Biosorption | Variable | Lab-Pilot | Low | Very Low | 4-6 |
| Phytomining | Low-Moderate | Field trials | Low | Very Low | 3-4 |
| Chitosan Adsorbents | Moderate | Industrial | Low | Very Low | 6-7 |
| Engineered Microbes | High | Lab scale | Moderate | Very Low | 3-4 |
| DES/IL Systems | Variable | Pilot scale | Moderate | Low | 5-6 |

*TRL = Technology Readiness Level (1-9 scale)*
