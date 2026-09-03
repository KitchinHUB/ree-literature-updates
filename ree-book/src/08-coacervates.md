---
title: Coacervates and Aqueous Biphasic Systems
---

(coacervates-and-aqueous-biphasic-systems)=
# Coacervates and Aqueous Biphasic Systems

Coacervates are phase-separated, polymer-rich droplets that form spontaneously
when oppositely charged macromolecules associate in solution. They are
interesting for rare earth separation for a reason that has little to do with
selectivity and everything to do with the solvent: both phases are aqueous. A
coacervate system does the job of a solvent extraction circuit without kerosene,
without the fire risk, and without the volatile organic emissions — and the mild
conditions leave room for biological ligands that would not survive an organic
diluent. This chapter surveys what such systems can currently do.

The headline results:

- Polyelectrolyte complex coacervates offer tunable selectivity through charge
  density, polymer composition, and ionic strength
  cite:sing2025polyelectrolyte,lee2025coacervate.
- Aqueous biphasic systems built from polymers and ionic liquids give promising
  REE separation factors cite:neves2022abs,kumar2021abs.
- Biomimetic approaches using lanthanide-binding proteins such as lanmodulin
  reach separation factors above 100 for *adjacent* lanthanides
  cite:cotruvo2023lanmodulin — a figure that should be read against the
  single-digit factors typical of conventional extractants.
- Stimuli-responsive coacervates allow on-demand capture and release through
  temperature, pH, or redox triggers cite:love2020coacervate,wang2024redox.

Lanmodulin and the other protein-based systems are treated more fully in
[](#biological-and-biomimetic-separations); here the focus is the coacervate
phase itself.

## Introduction to Coacervates
Coacervation is a liquid-liquid phase separation (LLPS) process in polyelectrolyte solutions induced by environmental factors such as pH, ionic strength, temperature, and solubility, resulting in the formation of a colloid-rich phase known as a coacervate cite:lee2025coacervate. The term "coacervate" derives from the Latin *coacervare*, meaning "to cluster together." These polymer-dense phases represent a thermodynamically stable state where electrostatic attraction between oppositely charged species drives demixing from the bulk solution.

Driving forces for coacervation include:

- Electrostatic attraction between oppositely charged polyelectrolytes
- Entropy gain from counterion release cite:zhang2022driving
- Hydrophobic interactions
- Hydrogen bonding

The properties of coacervates can be controlled by adjusting parameters such as pH, polymer ratio, ionic strength, and molecular characteristics cite:spruijt2014polyelectrolyte,sing2025polyelectrolyte.

### Complex Coacervation
Complex coacervation occurs when two oppositely charged polyelectrolytes (polycation and polyanion) are mixed in aqueous solution. At appropriate stoichiometries and ionic strengths, the system phase-separates into a polymer-rich coacervate phase and a polymer-dilute supernatant cite:spruijt2014polyelectrolyte.

The earliest theoretical framework for complex coacervation was developed by Overbeek and Voorn in 1957, who estimated the total free energy of mixing as a sum of Flory-Huggins mixing entropy terms and Debye-Hückel electrostatic interactions cite:overbeek1957coacervation,priftis2012thermodynamic. This mean-field approach captures the essential physics: the electrostatic free energy provides the driving force, while entropic mixing favors the disordered homogeneous state.

Key polymer systems for coacervation include:

- Polypeptides: poly(L-lysine)/poly(L-glutamate), poly(L-arginine)/poly(L-aspartate)
- Polysaccharides: chitosan/alginate, chitosan/hyaluronic acid
- Synthetic polymers: poly(diallyldimethylammonium chloride) (PDADMAC)/poly(styrene sulfonate) (PSS)
- Protein-polymer pairs: gelatin/gum arabic, BSA/polycations

Phase diagrams for coacervate systems typically show a two-phase region at intermediate ionic strengths, bounded by a single-phase region at very low salt (kinetically trapped precipitates) and at high salt (electrostatic screening suppresses coacervation) cite:sing2020review.

### Simple Coacervation
Simple coacervation involves a single polyelectrolyte species that undergoes phase separation induced by salt, solvent, or temperature changes. This process is particularly relevant for intrinsically disordered proteins (IDPs), which can self-coacervate due to their unique charge patterns and low-complexity sequences cite:uversky2014idp.

Temperature and pH are critical parameters:

- Temperature affects both the dielectric constant of water and polymer solubility
- pH determines the ionization state of weak polyelectrolytes and thus the effective charge density

The cloud point (temperature at which the solution becomes turbid due to coacervate formation) is a key characteristic of thermoresponsive coacervate systems.

## Coacervates for Metal Ion Separations
The dense, water-rich environment of coacervates provides a unique medium for metal ion partitioning. Unlike organic solvents used in conventional liquid-liquid extraction, coacervates maintain aqueous compatibility while offering distinct chemical environments in the polymer-rich and polymer-dilute phases cite:kim2021pec.

### Mechanism of Ion Uptake
Metal ions partition into coacervates through multiple mechanisms:

1.  **Electrostatic interactions**: Multiply charged metal cations are attracted to negatively charged functional groups (carboxylates, sulfonates, phosphates) in the polymer backbone
2.  **Coordination chemistry**: Specific ligand-metal interactions involving donor atoms (N, O, S) in the polymer or added chelating agents
3.  **Ion exchange**: Displacement of polymer-bound counterions (Na+, K+) by metal ions with higher affinity
4.  **Hydrophobic partitioning**: Neutral metal complexes preferentially partition into the less polar coacervate interior

Polyelectrolyte complex resins fabricated from PDADMAC-PSS coacervates show outstanding performance for heavy metal adsorption, with significant uptakes of Cu2+, Pb2+, and Cd2+ and easy phase separation cite:kim2021pec. PEC capsules have demonstrated selective Au(III) recovery from multimetal mixtures containing Pt, Pd, Cu, Co, and Zn cite:wang2023pec.

### Selectivity and Separation Factors
Selectivity in coacervate-based separations arises from:

1.  **Size-based selectivity**: The mesh size of the polymer network can exclude larger ions or complexes
2.  **Charge density effects**: Higher charge density metals bind more strongly to polyanionic domains
3.  **Lanthanide contraction**: The systematic decrease in ionic radius across the lanthanide series (La3+ = 1.03 Å to Lu3+ = 0.86 Å) can be exploited for selectivity

For rare earth elements, the challenge is that all lanthanides exhibit similar charge (+3), coordination preferences (typically 8-9), and chemistry. The small ionic radius differences (typically 0.01-0.02 Å between adjacent elements) require highly selective ligands or separation media.

Separation factors (SF) quantify selectivity: $$SF = \frac{[M_1]_{coacervate}/[M_1]_{supernatant}}{[M_2]_{coacervate}/[M_2]_{supernatant}}$$

For adjacent lanthanides, conventional solvent extraction achieves SF = 1.5-3.0, while protein-based systems can achieve SF \> 100 cite:cotruvo2023lanmodulin.

## Biomimetic and Natural Coacervate Systems
Nature provides inspiration for REE-selective materials through the discovery of lanthanide-dependent bacteria and their associated proteins. Biological phase separation in the form of membraneless organelles also offers insights into coacervate function and design.

### Intrinsically Disordered Proteins (IDPs)
IDPs are proteins that lack a fixed three-dimensional structure but remain functional. An estimated 30-40% of residues in the eukaryotic proteome are located in disordered regions cite:uversky2014idp. IDPs undergo liquid-liquid phase separation (LLPS) to form membrane-less organelles (MLOs) that play critical roles in cellular organization cite:brangwynne2015phase.

Key features of IDP phase separation:

- Low-complexity sequences enriched in charged and polar amino acids
- Multivalent interactions through repetitive motifs
- Charge patterning---clustering of like charges into "patches" amplifies phase separation cite:wang2021peptide
- Responsiveness to ionic strength, pH, and temperature cite:lin2020idp

Complete phase diagrams for IDP coacervation reveal that block-charged sequences have larger coacervation windows than randomly patterned sequences cite:pal2020idp. This insight guides the design of synthetic polymers with optimized phase behavior.

### Protein-Polyelectrolyte Coacervates
Protein-polymer coacervates combine the structural selectivity of proteins with the processability of synthetic polymers. Key systems include:

- Globular proteins (BSA, lysozyme, gelatin) with synthetic polyelectrolytes
- Enzyme-containing coacervates for biocatalysis
- Antibody-polymer systems for sensing applications

For REE applications, protein-based coacervates offer:

- Pre-organized metal binding sites with defined coordination geometry
- Allosteric regulation of binding affinity
- Biocompatibility and biodegradability

### Peptide-Based Coacervates
Short peptides (10-30 amino acids) can form coacervates and offer advantages of defined sequence, scalable synthesis, and tunable properties cite:li2019peptide.

#### Lanthanide Binding Tags (LBTs)

Lanthanide binding tags are amphiphilic peptide sequences based on the EF-hand metal binding loops of calcium-binding proteins cite:li2024lanthanide,schmitz2022lanm. The EF-hand motif consists of two alpha helices linked by a 12-residue loop that coordinates metal ions through carboxylate-rich sidechains.

Key characteristics:

- Pentagonal bipyramidal coordination geometry
- Positions 1, 3, 5, 7, 9, and 12 provide coordinating residues (denoted X, Y, Z, -Y, -X, -Z)
- Picomolar affinity for Ln3+ with 10^8^-fold selectivity over Ca2+ cite:cotruvo2023lanmodulin
- Disorder-to-order conformational change upon lanthanide binding

Isolated EF-hand loop peptides dimerize when saturated with lanthanide ions, reproducing the structure of native protein domains cite:shaw2000ef,nitz2000lbt. This metal-induced self-assembly could be exploited for coacervate formation and REE separation.

#### Lanmodulin (LanM)

Lanmodulin is a natural lanthanide-binding protein discovered in methylotrophic bacteria that use lanthanides in methanol dehydrogenase enzymes cite:cotruvo2023lanmodulin,deblonde2022lanmodulin. LanM possesses four EF-hand motifs with remarkable lanthanide selectivity:

- Picomolar affinity for Ln3+ (Kd \~ 10^-12^ M)
- 10^8^-fold selectivity over Ca2+
- Large conformational change upon metal binding

A variant from *Hansschlegelia quercus* (Hans-LanM) exhibits metal-sensitive dimerization, with the La3+-induced dimer being \>100-fold tighter than the Dy3+-induced dimer cite:cotruvo2023lanmodulin. X-ray crystal structures reveal how picometer-scale radius differences between La3+ and Dy3+ are propagated to quaternary structure through carboxylate shifts in second-sphere hydrogen bonding networks.

Structure-guided mutagenesis at the dimer interface enables single-stage, column-based separation of Nd3+/Dy3+ mixtures to \>98% individual element purities cite:park2024lanmodulin. This represents a breakthrough in achieving industrial-scale separation factors under mild, aqueous conditions.

Recent computational studies provide structural insights into REE selectivity in lanmodulin variants cite:yao2025lanm, enabling rational design of engineered proteins for specific separation challenges cite:chen2025lanmodulin.

## Stimuli-Responsive Coacervates
Stimuli-responsive coacervates undergo phase transitions in response to external triggers, enabling controlled capture and release of metal ions. This "smart" behavior is essential for practical separation processes requiring both extraction and stripping steps.

### Temperature-Responsive Systems
#### LCST and UCST Polymers

Poly(N-isopropylacrylamide) (PNIPAM) is the prototypical thermoresponsive polymer, exhibiting a lower critical solution temperature (LCST) around 32°C cite:das2024pnipam. Below the LCST, PNIPAM is water-soluble and hydrated; above the LCST, it undergoes a reversible transition to an insoluble, dehydrated state.

The LCST can be tuned by:

- Copolymerization with hydrophilic monomers (increases LCST)
- Copolymerization with hydrophobic monomers (decreases LCST)
- Addition of salts following the Hofmeister series
- Metal ion binding cite:zhong2020pnipam

For metal extraction, PNIPAM copolymers with metal-binding groups (acrylic acid, chelating monomers) capture metals at low temperature and release them upon heating above the LCST. This enables thermal cycling for extraction and back-extraction cite:kumar2023stimuli.

#### Thermoseparating Coacervates

Cloud point extraction (CPE) uses temperature-induced phase separation of non-ionic surfactants for metal preconcentration cite:castiho2003cpe. At temperatures above the cloud point, micellar solutions separate into surfactant-rich and surfactant-dilute phases. Metal complexes with hydrophobic ligands preferentially partition into the surfactant-rich phase.

For lanthanide separation, CPE with Triton X-114 and 8-hydroxyquinoline achieves Gd3+/La3+ selectivity \> 30 and decontamination factors of 50 cite:castiho2003cpe. Water-soluble calixarenes as chelating agents with Triton X-100 enable CPE of La3+, Gd3+, and Yb3+ with tunable selectivity cite:depierro2008cpe.

### pH-Responsive Coacervates
pH-responsive coacervates exploit the charge-switching behavior of weak polyelectrolytes above and below their pKa values cite:love2020coacervate.

Mechanisms:

- Below pKa: weak polyacids (poly(acrylic acid), poly(glutamic acid)) are protonated and uncharged
- Above pKa: ionization increases charge density and promotes coacervation with polycations
- The process is completely reversible, enabling pH-triggered assembly and disassembly

Complex coacervates formed from peptides and polyoxometalates undergo pH-induced phase transitions from fluid coacervate to gel state cite:li2019peptide. Metal ions can trigger similar transitions, providing a readout for metal binding and a mechanism for metal-responsive materials.

For REE separation, pH cycling can be used for:

- Selective extraction at optimal pH for target metal binding
- Back-extraction by pH adjustment to release metals
- Polymer regeneration for repeated use

### Light and Redox-Responsive Systems
#### Photoswitchable Coacervates

Azobenzene-containing polymers undergo *cis-trans* isomerization upon UV/visible light irradiation, changing their hydrophobicity and charge distribution. This enables light-triggered coacervate formation or dissolution without chemical addition.

#### Redox-Responsive Systems

Redox-responsive coacervates respond to changes in oxidation state, either through:

- Polymer backbone redox changes (ferrocene, disulfide bonds)
- Metal ion oxidation state changes (Ce3+/Ce4+, Fe2+/Fe3+)

Recent work quantified redox thermodynamics shifts within coacervates using temperature-dependent electrochemistry, extracting reaction entropy, enthalpy, and Gibbs energy for redox processes in the condensed phase cite:wang2024redox.

For cerium separation specifically, the Ce3+/Ce4+ redox couple enables selective oxidation and precipitation, which could be integrated with coacervate extraction for enhanced Ce selectivity cite:pramanik2024emerging.

## Coacervates for Rare Earth Element Separations
The application of coacervate-based systems specifically to REE separations is an emerging field, with most work focusing on aqueous biphasic systems, cloud point extraction, and protein-based approaches rather than classical polyelectrolyte coacervates.

### Polyelectrolyte Systems for REE
While PEC coacervates have been extensively studied for heavy metal removal cite:kim2021pec,wang2023pec, their application to REE separation is limited. The similar chemistry of lanthanides means that non-specific electrostatic binding provides poor selectivity.

Design strategies for improved selectivity include:

- Incorporation of specific chelating groups (phosphonates, aminocarboxylates)
- Charge density matching between polymer and target metal
- Use of water-soluble ligands (DTPA, EDTA) as holdback reagents

Stimuli-responsive polymers that bind lanthanides selectively have been developed at UNC, featuring hydrophobic components that confer protein-like structure and improve selectivity over common metals like calcium cite:unc2024smart.

### Aqueous Biphasic Systems (ABS)
Aqueous biphasic systems form when two water-soluble polymers (PEG/dextran) or a polymer and kosmotropic salt (PEG/ammonium sulfate) are mixed above critical concentrations cite:neves2022abs,li2020abs. Unlike organic-aqueous extraction, both ABS phases are aqueous, reducing environmental and safety concerns.

#### Polymer-Salt ABS

PEG-salt ABS have been applied to lanthanide separation with added extractants:

- Separation factors depend on PEG molecular weight, salt type and concentration, and pH
- DTPA as a complexing agent in the salt-rich phase can tune selectivity

#### Ionic Liquid-Based ABS

Ionic liquid (IL) ABS offer additional tunability through IL cation and anion selection cite:kumar2021abs:

The tributyltetradecylphosphonium chloride (\[P444,14\]Cl) ABS enables separation of Sm/Co, Nd/Fe, Eu/Zn, and La/Ni pairs. A one-pot leaching-extraction process using \[P44414\]Cl-HCl ABS selectively extracts Fe (\>99%) while leaving REEs in the aqueous phase (\<10% extracted), enabling efficient REE/Fe separation from NdFeB magnets cite:chen2021abs.

#### Three-Liquid-Phase Systems (TLPS)

TLPS consisting of salt-rich bottom aqueous phase, polymer-rich middle phase, and organic top phase provide gradients of hydrophobicity for enhanced selectivity cite:wang2021tlps.

The Cyanex272/PEG 2000/(NH4)2SO4-H2O system enables stripping of heavy rare earths with separation factors adjustable by polymer concentration, salt concentration, pH, and DTPA addition.

### Coordination-Enhanced Coacervates
Functionalization of coacervate-forming polymers with specific REE-binding ligands can dramatically improve selectivity:

#### Phosphonate-Modified Systems

Phosphonate ligands are the basis of industrial REE extractants (HDEHP, PC88A, Cyanex 272). Polymer-supported phosphonate extractants \[D201\]\[DEHP\] and \[D201\]\[C272\] show excellent scandium selectivity with maximum adsorption at pH 0.78 cite:cui2016sc.

#### Aminocarboxylate-Modified Systems

DTPA, EDTA, and related ligands provide strong lanthanide binding with modest size-based selectivity. Incorporation into polymers or use as holdback agents in ABS can enhance separation.

#### Diglycolamide Systems

Diglycolamides (DGA) show size-dependent lanthanide binding correlated with the "lanthanide contraction" in ionic radii.

### Case Studies: Specific REE Pair Separations
#### Light REE: La/Ce and Ce/Pr Separations
Cerium is unique among lanthanides in exhibiting stable ~~4 oxidation state, enabling oxidative separation. Ce4~~ can be selectively precipitated as CeO2 or extracted with different partition coefficients than Ce3+.

The ionic radius differences (La3+ = 1.03 Å, Ce3+ = 1.01 Å, Pr3+ = 0.99 Å) are sufficient for protein-based separation but challenging for conventional extractants cite:pramanik2024emerging.

#### Nd/Pr Separation
The Nd/Pr separation ("didymium" problem) is critical for permanent magnet recycling. These elements have nearly identical ionic radii (Nd3+ = 0.98 Å, Pr3+ = 0.99 Å) and similar coordination chemistry, making separation extremely difficult cite:zhang2025ndpr.

Recent advances:

- Ionic liquid extraction with β-diketones achieves unprecedented separation factor \>500 cite:zhang2025ndpr
- PC88A-impregnated surfaces achieve SF = 171 with 92% Pr+Nd purity cite:gao2023ndpr
- Kinetic separation strategies with specific ion effects achieve SF \> 8 cite:chen2023ndpr
- Push-and-pull systems with \[A336\]\[NO3\]-DTPA enhance separation in column extractors cite:wang2019ndpr

Coacervate-based approaches remain to be developed but could benefit from:

- Time-resolved separation exploiting kinetic differences
- Integration with selective oxidation for Pr (Pr3+/Pr4+)
- Protein engineering for Nd/Pr discrimination

#### Heavy REE Separations (Dy, Ho, Er, Yb, Lu)
Heavy REEs have smaller ionic radii and typically prefer lower coordination numbers than light REEs. The ionic radius differences between adjacent heavy REEs are very small (\< 0.02 Å), making separation particularly challenging.

Three-liquid-phase systems with Cyanex272/PEG/ammonium sulfate show promise for heavy REE stripping with tunable selectivity cite:wang2021tlps.

Protein-based approaches:

- Hans-LanM discriminates light from heavy REEs based on metal-sensitive dimerization cite:cotruvo2023lanmodulin
- Engineered lanmodulin variants can achieve Nd/Dy separation to \>98% purity in single-stage columns cite:park2024lanmodulin

#### Sc Separation
Scandium is geochemically associated with REEs but has distinct chemistry: smaller ionic radius (0.75 Å), lower coordination number preference, and unique complexation behavior. This enables high separation factors from lanthanides.

Effective scandium separation methods:

- Polymer-supported phosphonate extractants with SF \> 50 vs other REEs cite:cui2016sc
- Amic acid extractants (D2EHAF) in polymer inclusion membranes for complete Sc separation from transition metals cite:kim2019sc
- Mesoporous silica with unmodified silanols for selective Sc extraction over Fe cite:ramasamy2017sc
- TRPO-modified resins in sulfuric and hydrochloric acid media cite:hou2024sc

A critical review of Sc/Fe separation emphasizes the importance of functional ligands and complexing agents for solid-phase extraction cite:li2025sc.

## Computational and Modeling Approaches
Computational methods provide fundamental understanding of coacervate thermodynamics, structure, and metal ion interactions, guiding the rational design of separation systems.

### Molecular Dynamics Simulations
Molecular dynamics (MD) simulations capture atomistic details of coacervate structure and dynamics cite:zhang2022driving:

- Ion solvation and coordination environments
- Polymer-polymer and polymer-ion interactions
- Water structure in coacervate vs supernatant phases
- Free energy profiles for ion transfer between phases

A key finding from MD simulations is that the thermodynamic driving force for coacervation is entropy-dominated under typical aqueous conditions. The temperature dependence of the dielectric constant of water contributes substantially to the entropic term in electrostatic interactions cite:zhang2022driving.

### Thermodynamic Modeling
#### Voorn-Overbeek Theory

The classical Voorn-Overbeek (VO) theory combines Flory-Huggins mixing entropy with Debye-Hückel electrostatics cite:overbeek1957coacervation,priftis2012thermodynamic. While capturing the essential physics of coacervation, VO theory treats backbone charges as disconnected free ions and neglects chain connectivity correlations.

#### Random Phase Approximation (RPA)

RPA extends mean-field theory by including correlation corrections to the electrostatic free energy, improving predictions for charge sequence effects and salt dependence.

#### PC-SAFT and Molecular Equations of State

Perturbed-chain statistical associating fluid theory (PC-SAFT) and related equations of state provide rigorous molecular thermodynamic models for polyelectrolyte solutions cite:shen2024thermodynamics. These approaches address strong charge correlations and the complex interplay of short-range and long-range interactions.

### Field-Theoretic Simulations
Field-theoretic simulations (FTS) using complex Langevin sampling provide approximation-free phase diagrams for coacervate systems cite:lee2008fts,delaney2017fts.

Key advantages of FTS:

- No mean-field approximations
- Proper sampling of fluctuations in electrostatic and composition fields
- Prediction of spinodal and binodal boundaries
- Extension to multicomponent and multiphase systems cite:chen2023multiphase

FTS has been applied to IDP coacervation, revealing how charge patterning affects phase boundaries cite:pal2020idp.

### Machine Learning Approaches
Machine learning offers opportunities for:

- Polymer property prediction from sequence
- High-throughput virtual screening of coacervate-forming systems
- Inverse design of polymers with target metal selectivity
- Analysis of MD trajectories to identify binding motifs

Bridging theoretical frameworks (field theory, ion pairing, explicit simulations) remains an active area providing unified understanding of polyelectrolyte complexation cite:qin2023modeling,li2024arxiv.

## Process Considerations
Translation of coacervate-based separations from laboratory to industrial scale requires addressing process engineering challenges.

### Continuous Processing
#### Flow-Based Coacervate Systems

Microfluidic platforms enable precise control of coacervate formation through:

- Controlled mixing of polymer streams
- Defined residence times and flow rates
- In-situ monitoring of phase separation
- Droplet-based extraction with high surface-to-volume ratios

#### Integration with Hydrometallurgical Processes

Coacervate extraction could be integrated with existing REE processing:

- Leaching: acidic dissolution of REE-bearing minerals
- Coacervate extraction: selective partitioning into polymer-rich phase
- Back-extraction: stimuli-triggered release to stripping solution
- Polymer recovery: regeneration for reuse

### Environmental and Economic Factors
#### Comparison with Organic Solvent Extraction

Advantages of aqueous coacervate systems:

- Elimination or reduction of organic solvents
- Reduced volatile organic compound (VOC) emissions
- Lower fire and explosion risk
- Compatibility with biological components
- Potential for milder operating conditions

Challenges:

- Lower metal loading capacity than organic extractants
- Polymer cost and recovery
- Process intensification requirements
- Limited industrial experience

#### Techno-Economic Assessment

Rigorous techno-economic analysis is needed comparing:

- Capital costs (equipment, polymer inventory)
- Operating costs (energy, chemicals, polymer replacement)
- Separation efficiency and purity
- Environmental impact (waste generation, emissions)

The biodegradability and recyclability of polymer components are important factors in lifecycle assessment.

(challenges-and-future-directions)=
## Challenges and Future Directions
### Selectivity Challenges for Adjacent Lanthanides

The fundamental challenge in REE separation is the chemical similarity of lanthanides. Coacervate systems must achieve selectivity through:

- Size discrimination via pre-organized binding sites
- Coordination number preferences
- Kinetic differences in metal binding/release
- Multi-stage separation processes

### Polymer Design Strategies

Future polymer development should focus on:

- Incorporation of highly selective ligands (lanmodulin-inspired, diglycolamides)
- Responsive behavior for controlled capture/release
- Recyclability and stability over multiple cycles
- Scalable synthesis from sustainable feedstocks

### Integration with Other Separation Methods

Hybrid approaches combining coacervates with:

- Membrane separations (polymer inclusion membranes)
- Chromatographic methods (coacervate-coated stationary phases)
- Electrochemical methods (redox-driven separations)
- Precipitation (coacervate-assisted crystallization)

### Hybrid Coacervate-Membrane Systems

Polymer inclusion membranes (PIMs) containing coacervate-forming polymers or selective extractants offer continuous separation with reduced solvent inventory cite:kim2019sc.

### Industrial Translation Barriers

Key barriers to commercialization:

- Scale-up of polymer synthesis
- Process robustness and reliability
- Regulatory approval for REE products
- Competition with established solvent extraction infrastructure
- Need for demonstration at pilot scale

## Conclusions
Coacervate-based separation methods represent a promising, environmentally-friendly approach to rare earth element separations. This review has examined the fundamental science of coacervation, mechanisms of metal ion partitioning, and emerging applications to REE recovery.

Key conclusions:

1.  **Biomimetic approaches show highest selectivity**: Lanmodulin and engineered variants achieve separation factors \>100 for adjacent lanthanides, approaching the theoretical limits of protein-based recognition cite:cotruvo2023lanmodulin,park2024lanmodulin.

2.  **Aqueous biphasic systems are most mature**: IL-based ABS and polymer-salt systems have demonstrated practical REE separations with good efficiency cite:neves2022abs,kumar2021abs,chen2021abs.

3.  **Stimuli-responsive coacervates enable process integration**: Temperature, pH, and redox triggers allow controlled capture and release essential for continuous processes cite:love2020coacervate,kumar2023stimuli.

4.  **Computational methods guide rational design**: MD simulations, field-theoretic methods, and machine learning accelerate the discovery of improved coacervate systems cite:zhang2022driving,lee2008fts.

5.  **Significant challenges remain**: Selectivity for adjacent lanthanides (especially Nd/Pr), polymer cost and recyclability, and scale-up require further development.

### Recommended Research Directions

1.  Design of peptide-based coacervates incorporating lanthanide-selective motifs
2.  Development of stimuli-responsive systems for continuous extraction/stripping
3.  Integration of coacervates with membrane and electrochemical separations
4.  Techno-economic and lifecycle assessment comparing coacervate vs solvent extraction
5.  Pilot-scale demonstration with real REE-bearing feedstocks

The transition to sustainable REE processing requires new separation paradigms. Coacervate-based systems, operating under mild aqueous conditions with biological or bio-inspired selectivity, offer a path toward greener hydrometallurgy while potentially achieving higher separation efficiency than conventional methods.
