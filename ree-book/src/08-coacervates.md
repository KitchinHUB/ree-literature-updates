---
title: Coacervates and Aqueous Biphasic Systems
---

(coacervates-and-aqueous-biphasic-systems)=
# Coacervates and Aqueous Biphasic Systems

Coacervates are phase-separated, polymer-rich droplets that form spontaneously
when oppositely charged macromolecules associate in solution. They are
interesting for rare earth separation for a reason that has little to do with
selectivity and everything to do with the solvent: both phases are aqueous. A
coacervate system does the job of a {index}`solvent extraction` circuit without kerosene,
without the fire risk, and without the volatile organic emissions — and the mild
conditions leave room for biological ligands that would not survive an organic
diluent. This chapter surveys what such systems can currently do.

The headline results:

- Polyelectrolyte complex coacervates offer tunable selectivity through charge
  density, polymer composition, and ionic strength
  [@sing2025polyelectrolyte; @lee2025polyelectrolyte].
- Aqueous biphasic systems built from polymers and {index}`ionic liquids` give promising
  REE {index}`separation factors <separation factor>` [@neves2022liquid; @kumar2022separation].
- Biomimetic approaches using lanthanide-binding proteins such as {index}`lanmodulin`
  separate the rare earths from *everything else* with a sharpness no synthetic
  extractant matches — roughly 10⁸-fold discrimination against Ca²⁺, and
  quantitative recovery of REEs from leachates carrying molar quantities of Na,
  Mg, Ca, Al, Fe, Cu and Zn [@cotruvo2018lanmodulin; @deblonde2020selective].
  They discriminate one lanthanide from its *neighbour* only weakly. That makes
  them group-separation agents rather than replacements for a fractionation
  cascade; the distinction is developed in
  [](#lanmodulin-structure-mechanism-and-engineering).
- Stimuli-responsive coacervates allow on-demand capture and release through
  temperature, pH, or redox triggers [@love2020reversible; @wang2025quantification].

Lanmodulin and the other protein-based systems are treated more fully in
[](#biological-and-biomimetic-separations); here the focus is the coacervate
phase itself.

## Introduction to Coacervates
Coacervation is a liquid-liquid phase separation (LLPS) process in polyelectrolyte solutions induced by environmental factors such as pH, ionic strength, temperature, and solubility, resulting in the formation of a colloid-rich phase known as a coacervate [@lee2025polyelectrolyte]. The term "coacervate" derives from the Latin *coacervare*, meaning "to cluster together." These polymer-dense phases represent a thermodynamically stable state where electrostatic attraction between oppositely charged species drives demixing from the bulk solution.

Driving forces for coacervation include:

- Electrostatic attraction between oppositely charged polyelectrolytes
- Entropy gain from counterion release [@zhang2022driving]
- Hydrophobic interactions
- Hydrogen bonding

The properties of coacervates can be controlled by adjusting parameters such as pH, polymer ratio, ionic strength, and molecular characteristics [@spruijt2014polyelectrolyte; @sing2025polyelectrolyte].

### Complex Coacervation
Complex coacervation occurs when two oppositely charged polyelectrolytes (polycation and polyanion) are mixed in aqueous solution. At appropriate stoichiometries and ionic strengths, the system phase-separates into a polymer-rich coacervate phase and a polymer-dilute supernatant [@spruijt2014polyelectrolyte].

The earliest theoretical framework for complex coacervation was developed by Overbeek and Voorn in 1957, who estimated the total free energy of mixing as a sum of Flory-Huggins mixing entropy terms and Debye-Hückel electrostatic interactions [@overbeek1957phase; @priftis2012early]. This mean-field approach captures the essential physics: the electrostatic free energy provides the driving force, while entropic mixing favors the disordered homogeneous state.

Key polymer systems for coacervation include:

- Polypeptides: poly(L-lysine)/poly(L-glutamate), poly(L-arginine)/poly(L-aspartate)
- Polysaccharides: chitosan/alginate, chitosan/hyaluronic acid
- Synthetic polymers: poly(diallyldimethylammonium chloride) (PDADMAC)/poly(styrene sulfonate) (PSS)
- Protein-polymer pairs: gelatin/gum arabic, BSA/polycations

Phase diagrams for coacervate systems typically show a two-phase region at intermediate ionic strengths, bounded by a single-phase region at very low salt (kinetically trapped precipitates) and at high salt (electrostatic screening suppresses coacervation) [@sing2020progress].

### Simple Coacervation
Simple coacervation involves a single polyelectrolyte species that undergoes phase separation induced by salt, solvent, or temperature changes. This process is particularly relevant for intrinsically disordered proteins (IDPs), which can self-coacervate due to their unique charge patterns and low-complexity sequences [@uversky2015intrinsically].

Temperature and pH are critical parameters:

- Temperature affects both the dielectric constant of water and polymer solubility
- pH determines the ionization state of weak polyelectrolytes and thus the effective charge density

The cloud point (temperature at which the solution becomes turbid due to coacervate formation) is a key characteristic of thermoresponsive coacervate systems.

## Coacervates for Metal Ion Separations
The dense, water-rich environment of coacervates provides a unique medium for metal ion partitioning. Unlike organic solvents used in conventional liquid-liquid extraction, coacervates maintain aqueous compatibility while offering distinct chemical environments in the polymer-rich and polymer-dilute phases [@kim2022facile].

### Mechanism of Ion Uptake
Metal ions partition into coacervates through multiple mechanisms:

1.  **Electrostatic interactions**: Multiply charged metal cations are attracted to negatively charged functional groups (carboxylates, sulfonates, phosphates) in the polymer backbone
2.  **Coordination chemistry**: Specific ligand-metal interactions involving donor atoms (N, O, S) in the polymer or added chelating agents
3.  **{index}`Ion exchange <ion exchange>`**: Displacement of polymer-bound counterions (Na+, K+) by metal ions with higher affinity
4.  **Hydrophobic partitioning**: Neutral metal complexes preferentially partition into the less polar coacervate interior

Polyelectrolyte complex resins fabricated from PDADMAC-PSS coacervates show outstanding performance for heavy metal adsorption, with significant uptakes of Cu2+, Pb2+, and Cd2+ and easy phase separation [@kim2022facile]. PEC capsules have demonstrated selective Au(III) recovery from multimetal mixtures containing Pt, Pd, Cu, Co, and Zn [@wang2023polyelectrolyte].

### Selectivity and Separation Factors
Selectivity in coacervate-based separations arises from:

1.  **Size-based selectivity**: The mesh size of the polymer network can exclude larger ions or complexes
2.  **Charge density effects**: Higher charge density metals bind more strongly to polyanionic domains
3.  **{index}`Lanthanide contraction <lanthanide contraction>`**: The systematic decrease in ionic radius across the lanthanide series (La3+ = 1.03 Å to Lu3+ = 0.86 Å) can be exploited for selectivity

For rare earth elements, the challenge is that all lanthanides exhibit similar charge (+3), coordination preferences (typically 8-9), and chemistry. The small ionic radius differences (typically 0.01-0.02 Å between adjacent elements) require highly selective ligands or separation media.

Separation factors (SF) quantify selectivity: $$SF = \frac{[M_1]_{coacervate}/[M_1]_{supernatant}}{[M_2]_{coacervate}/[M_2]_{supernatant}}$$

For adjacent lanthanides, conventional solvent extraction achieves SF = 1.5-3.0. Protein-based systems are sometimes quoted at "SF \> 100", but that number is a misreading. The figure in circulation is the \>100-fold ratio of *dimerization affinities* between the La³⁺- and Dy³⁺-loaded forms of Hans-LanM [@mattocks2023enhanced] — neither a separation factor nor an adjacent pair, since La and Dy sit nine places apart on opposite sides of the light/heavy split. The separation factors the same work actually measured are Nd/Dy = 8.1 (wild type) and 12.7 (the R100K variant), and the best adjacent-pair figures from any protein system are Ce/La = 3.0, Pr/Ce = 1.7 and Nd/Pr = 1.4 [@larrinaga2024modulating]. That is the same band as conventional extractants, not a hundred times better. Against Ca²⁺ and the other non-rare-earth cations in a leachate the protein discrimination genuinely is enormous; against a neighbouring lanthanide it is not. The two selectivities must be kept apart, and only the second is what a fractionation cascade is built to supply.

## Biomimetic and Natural Coacervate Systems
Nature provides inspiration for REE-selective materials through the discovery of lanthanide-dependent bacteria and their associated proteins. Biological phase separation in the form of membraneless organelles also offers insights into coacervate function and design.

### Intrinsically Disordered Proteins (IDPs)
IDPs are proteins that lack a fixed three-dimensional structure but remain functional. An estimated 30-40% of residues in the eukaryotic proteome are located in disordered regions [@uversky2015intrinsically]. IDPs undergo liquid-liquid phase separation (LLPS) to form membrane-less organelles (MLOs) that play critical roles in cellular organization [@brangwynne2015polymer].

Key features of IDP phase separation:

- Low-complexity sequences enriched in charged and polar amino acids
- Multivalent interactions through repetitive motifs
- Charge patterning---clustering of like charges into "patches" amplifies phase separation [@wang2025role]
- Responsiveness to ionic strength, pH, and temperature [@lin2019intrinsically]

Complete phase diagrams for IDP coacervation reveal that block-charged sequences have larger coacervation windows than randomly patterned sequences [@pal2019complete]. This insight guides the design of synthetic polymers with optimized phase behavior.

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
Short peptides (10-30 amino acids) can form coacervates and offer advantages of defined sequence, scalable synthesis, and tunable properties [@li2019coassembly].

#### Lanthanide Binding Tags (LBTs)

{index}`Lanthanide binding tags <lanthanide binding tags>` are amphiphilic peptide sequences based on the EF-hand metal binding loops of calcium-binding proteins [@li2024lanthanide; @schmitz2022lanmodulin]. The EF-hand motif consists of two alpha helices linked by a 12-residue loop that coordinates metal ions through carboxylate-rich sidechains.

Key characteristics:

- Pentagonal bipyramidal coordination geometry
- Positions 1, 3, 5, 7, 9, and 12 provide coordinating residues (denoted X, Y, Z, -Y, -X, -Z)
- Disorder-to-order conformational change upon lanthanide binding

Isolated tags are much weaker binders than the protein they are derived from:
micromolar dissociation constants for immobilized LBTs against picomolar ones
for full-length lanmodulin, a difference of roughly six orders of magnitude
(see [](#biological-and-biomimetic-separations)). The picomolar affinity and the
10⁸-fold Ca²⁺ discrimination quoted in the literature belong to the whole
protein [@cotruvo2018lanmodulin], not to the excised loop.

Isolated EF-hand loop peptides dimerize when saturated with lanthanide ions, reproducing the structure of native protein domains [@shaw1997isolated; @ma2000lanthanide]. This metal-induced self-assembly could be exploited for coacervate formation and REE separation.

#### Lanmodulin (LanM)

Lanmodulin is a natural lanthanide-binding protein discovered in methylotrophic bacteria that use lanthanides in methanol dehydrogenase enzymes [@cotruvo2018lanmodulin; @deblonde2020selective]. LanM possesses four EF-hand motifs and undergoes a large disorder-to-order conformational change on metal binding. Two of its properties matter here, and they are different properties:

- **Ln³⁺ versus everything else.** LanM responds to picomolar concentrations of every trivalent lanthanide from La to Lu (and Y), but only to near-millimolar Ca²⁺ — a discrimination of order 10⁸ [@cotruvo2018lanmodulin]. It holds that binding down to pH ≈ 2.5, survives 95 °C and repeated acid cycling, and recovers rare earths quantitatively from coal and electronic-waste leachates containing molar amounts of Li, Na, Mg, Ca, Sr, Al, Si, Mn, Fe, Co, Ni, Cu, Zn and U [@deblonde2020selective]. This is a *group* selectivity, and it is the strongest one known for a macromolecule.
- **Ln³⁺ versus Ln³⁺.** The same property — picomolar affinity for the whole series — means the monomer barely distinguishes one lanthanide from the next. Discriminating Nd from Pr, which is what a fractionation cascade exists to do, is a different problem, and native LanM does not solve it.

The route to intra-series discrimination is not the binding site but the *quaternary* structure. A homologue from *Hansschlegelia quercus* (Hans-LanM) dimerizes in a way that is sensitive to ionic radius: the La³⁺-induced dimer is \>100-fold tighter than the Dy³⁺-induced dimer [@mattocks2023enhanced]. X-ray crystal structures reveal how picometer-scale radius differences between La³⁺ and Dy³⁺ are propagated to quaternary structure through carboxylate shifts in second-sphere hydrogen bonding networks.

Note carefully what that \>100-fold number is and is not. It is a ratio of dimerization affinities for La versus Dy — nine places apart, on opposite sides of the light/heavy split — and not a separation factor for any pair, least of all an adjacent one. The measured separation factors from the same work are Nd/Dy = 8.12 ± 0.40 on a Hans-LanM column and 12.7 ± 1.3 on an R100K variant column [@mattocks2023enhanced]. Amplified down a column, an SF of that size still does real work: loaded with a model electronic-waste mixture of 95% Nd and 5% Dy, the R100K column achieved baseline separation to \>98% purity and \>99% yield in a single stage. The result is genuine; the mechanism is a modest separation factor plus many theoretical plates, not a separation factor above 100.

For an adjacent pair the honest numbers are smaller still. Applying the same dimerization strategy to *Methylorubrum extorquens* LanD — a related periplasmic lanthanide chaperone, not lanmodulin — an engineered variant enriches Pr³⁺ and Nd³⁺ relative to La³⁺ and Ce³⁺ in an all-aqueous ultrafiltration step, with SF Ce/La = 3.0 ± 0.4, Pr/Ce = 1.7 ± 0.2 and Nd/Pr = 1.4 ± 0.2 [@larrinaga2024modulating]. Those are the best protein-based adjacent-pair separation factors reported, they sit inside the conventional 1.5-3.0 band, and they were measured on micromolar solutions at bench scale.

Recent computational studies provide structural insights into REE selectivity in lanmodulin variants [@yao2025computationally] enabling rational design of engineered proteins for specific separation challenges [@chen2025lanmodulin].

## Stimuli-Responsive Coacervates
Stimuli-responsive coacervates undergo phase transitions in response to external triggers, enabling controlled capture and release of metal ions. This "smart" behavior is essential for practical separation processes requiring both extraction and stripping steps.

### Temperature-Responsive Systems
#### LCST and UCST Polymers

Poly(N-isopropylacrylamide) (PNIPAM) is the prototypical thermoresponsive polymer, exhibiting a lower critical solution temperature (LCST) around 32°C [@das2024poly]. Below the LCST, PNIPAM is water-soluble and hydrated; above the LCST, it undergoes a reversible transition to an insoluble, dehydrated state.

The LCST can be tuned by:

- Copolymerization with hydrophilic monomers (increases LCST)
- Copolymerization with hydrophobic monomers (decreases LCST)
- Addition of salts following the Hofmeister series
- Metal ion binding [@zhong2021thermoresponsive]

For metal extraction, PNIPAM copolymers with metal-binding groups (acrylic acid, chelating monomers) capture metals at low temperature and release them upon heating above the LCST. This enables thermal cycling for extraction and back-extraction [@kumar2023comprehensive].

#### Thermoseparating Coacervates

Cloud point extraction (CPE) uses temperature-induced phase separation of non-ionic surfactants for metal preconcentration [@favrerguillon2004cloud]. At temperatures above the cloud point, micellar solutions separate into surfactant-rich and surfactant-dilute phases. Metal complexes with hydrophobic ligands preferentially partition into the surfactant-rich phase.

For lanthanide separation, CPE with Triton X-114 and 8-hydroxyquinoline achieves Gd3+/La3+ selectivity \> 30 and decontamination factors of 50 [@favrerguillon2004cloud]. Water-soluble calixarenes as chelating agents with Triton X-100 enable CPE of La3+, Gd3+, and Yb3+ with tunable selectivity [@depierro2008cloud].

### pH-Responsive Coacervates
pH-responsive coacervates exploit the charge-switching behavior of weak polyelectrolytes above and below their pKa values [@love2020reversible].

Mechanisms:

- Below pKa: weak polyacids (poly(acrylic acid), poly(glutamic acid)) are protonated and uncharged
- Above pKa: ionization increases charge density and promotes coacervation with polycations
- The process is completely reversible, enabling pH-triggered assembly and disassembly

Complex coacervates formed from peptides and polyoxometalates undergo pH-induced phase transitions from fluid coacervate to gel state [@li2019coassembly]. Metal ions can trigger similar transitions, providing a readout for metal binding and a mechanism for metal-responsive materials.

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

Recent work quantified redox thermodynamics shifts within coacervates using temperature-dependent electrochemistry, extracting reaction entropy, enthalpy, and Gibbs energy for redox processes in the condensed phase [@wang2025quantification].

For {index}`cerium` separation specifically, the Ce3+/Ce4+ redox couple enables selective oxidation and {index}`precipitation`, which could be integrated with coacervate extraction for enhanced Ce selectivity [@pramanik2024emerging].

## Coacervates for Rare Earth Element Separations
The application of coacervate-based systems specifically to REE separations is an emerging field, with most work focusing on aqueous biphasic systems, cloud point extraction, and protein-based approaches rather than classical polyelectrolyte coacervates.

### Polyelectrolyte Systems for REE
While PEC coacervates have been extensively studied for heavy metal removal [@kim2022facile; @wang2023polyelectrolyte] their application to REE separation is limited. The similar chemistry of lanthanides means that non-specific electrostatic binding provides poor selectivity.

Design strategies for improved selectivity include:

- Incorporation of specific chelating groups (phosphonates, aminocarboxylates)
- Charge density matching between polymer and target metal
- Use of water-soluble ligands (DTPA, EDTA) as holdback reagents


### Aqueous Biphasic Systems (ABS)
Aqueous biphasic systems form when two water-soluble polymers (PEG/dextran) or a polymer and kosmotropic salt (PEG/ammonium sulfate) are mixed above critical concentrations [@neves2022liquid; @kee2020development]. Unlike organic-aqueous extraction, both ABS phases are aqueous, reducing environmental and safety concerns.

#### Polymer-Salt ABS

PEG-salt ABS have been applied to lanthanide separation with added extractants:

- Separation factors depend on PEG molecular weight, salt type and concentration, and pH
- DTPA as a complexing agent in the salt-rich phase can tune selectivity

#### Ionic Liquid-Based ABS

Ionic liquid (IL) ABS offer additional tunability through IL cation and anion selection [@kumar2022separation]:

The tributyltetradecylphosphonium chloride (\[P444,14\]Cl) ABS enables separation of Sm/Co, Nd/Fe, Eu/Zn, and La/Ni pairs. A one-pot leaching-extraction process using \[P44414\]Cl-HCl ABS selectively extracts Fe (\>99%) while leaving REEs in the aqueous phase (\<10% extracted), enabling efficient REE/Fe separation from {index}`NdFeB` magnets [@liu2022one].

#### Three-Liquid-Phase Systems (TLPS)

TLPS consisting of salt-rich bottom aqueous phase, polymer-rich middle phase, and organic top phase provide gradients of hydrophobicity for enhanced selectivity [@wang2021strategy].

The {index}`Cyanex272 <Cyanex 272>`/PEG 2000/(NH4)2SO4-H2O system enables stripping of heavy rare earths with separation factors adjustable by polymer concentration, salt concentration, pH, and DTPA addition.

### Coordination-Enhanced Coacervates
Functionalization of coacervate-forming polymers with specific REE-binding ligands can dramatically improve selectivity:

#### Phosphonate-Modified Systems

Phosphonate ligands are the basis of industrial REE extractants ({index}`HDEHP`, {index}`PC88A`, Cyanex 272). Polymer-supported phosphonate extractants \[D201\]\[DEHP\] and \[D201\]\[C272\] show excellent {index}`scandium` selectivity with maximum adsorption at pH 0.78 [@cui2016high].

#### Aminocarboxylate-Modified Systems

DTPA, EDTA, and related ligands provide strong lanthanide binding with modest size-based selectivity. Incorporation into polymers or use as holdback agents in ABS can enhance separation.

#### Diglycolamide Systems

{index}`Diglycolamides <diglycolamide>` (DGA) show size-dependent lanthanide binding correlated with the "lanthanide contraction" in ionic radii.

### Case Studies: Specific REE Pair Separations
#### Light REE: La/Ce and Ce/Pr Separations
Cerium is unique among lanthanides in exhibiting stable ~~4 oxidation state, enabling oxidative separation. Ce4~~ can be selectively precipitated as CeO2 or extracted with different partition coefficients than Ce3+.

The ionic radius differences (La3+ = 1.03 Å, Ce3+ = 1.01 Å, Pr3+ = 0.99 Å) are sufficient for protein-based separation but challenging for conventional extractants [@pramanik2024emerging].

#### Nd/Pr Separation
The Nd/Pr separation ("didymium" problem) is critical for permanent magnet recycling. These elements have nearly identical ionic radii (Nd3+ = 0.98 Å, Pr3+ = 0.99 Å) and similar coordination chemistry, making separation extremely difficult [@zhang2024remarkably].

Recent advances:

- Ionic liquid extraction with β-diketones achieves unprecedented separation factor \>500 [@zhang2024remarkably]
- PC88A-impregnated surfaces achieve SF = 171 with 92% Pr+Nd purity [@gao2023separation]
- Kinetic separation strategies with specific ion effects achieve SF \> 8 [@sui2023kinetic]
- Push-and-pull systems with \[A336\]\[NO3\]-DTPA enhance separation in column extractors [@wang2019enhanced]

Coacervate-based approaches remain to be developed but could benefit from:

- Time-resolved separation exploiting kinetic differences
- Integration with selective oxidation for Pr (Pr3+/Pr4+)
- Protein engineering for Nd/Pr discrimination

#### Heavy REE Separations (Dy, Ho, Er, Yb, Lu)
Heavy REEs have smaller ionic radii and typically prefer lower coordination numbers than light REEs. The ionic radius differences between adjacent heavy REEs are very small (\< 0.02 Å), making separation particularly challenging.

Three-liquid-phase systems with Cyanex272/PEG/ammonium sulfate show promise for heavy REE stripping with tunable selectivity [@wang2021strategy].

Protein-based approaches:

- Hans-LanM discriminates light from heavy REEs through metal-sensitive dimerization, and an interface mutant separates an Nd/Dy mixture to \>98% purity in a single-stage column [@mattocks2023enhanced]. Nd/Dy is a light/heavy split; no protein system has been shown to fractionate an adjacent heavy pair such as Dy/Ho.
- The related LanD chaperone, engineered at the same interface, fractionates *within* the light lanthanides, enriching Pr and Nd over La and Ce [@larrinaga2024modulating]

#### Sc Separation
Scandium is geochemically associated with REEs but has distinct chemistry: smaller ionic radius (0.75 Å), lower coordination number preference, and unique complexation behavior. This enables high separation factors from lanthanides.

Effective scandium separation methods:

- Polymer-supported phosphonate extractants with SF \> 50 vs other REEs [@cui2016high]
- Amic acid extractants (D2EHAF) in {index}`polymer inclusion membranes` for complete Sc separation from transition metals [@kim2019separation]
- Mesoporous silica with unmodified silanols for selective Sc extraction over Fe [@ramasamy2017selective]
- TRPO-modified resins in sulfuric and hydrochloric acid media [@hou2024adsorption]

A critical review of Sc/Fe separation emphasizes the importance of functional ligands and complexing agents for solid-phase extraction [@gangadari2025critical].

## Computational and Modeling Approaches
Computational methods provide fundamental understanding of coacervate thermodynamics, structure, and metal ion interactions, guiding the rational design of separation systems.

### Molecular Dynamics Simulations
Molecular dynamics (MD) simulations capture atomistic details of coacervate structure and dynamics [@zhang2022driving]:

- Ion solvation and coordination environments
- Polymer-polymer and polymer-ion interactions
- Water structure in coacervate vs supernatant phases
- Free energy profiles for ion transfer between phases

A key finding from MD simulations is that the thermodynamic driving force for coacervation is entropy-dominated under typical aqueous conditions. The temperature dependence of the dielectric constant of water contributes substantially to the entropic term in electrostatic interactions [@zhang2022driving].

### Thermodynamic Modeling
#### Voorn-Overbeek Theory

The classical Voorn-Overbeek (VO) theory combines Flory-Huggins mixing entropy with Debye-Hückel electrostatics [@overbeek1957phase; @priftis2012early]. While capturing the essential physics of coacervation, VO theory treats backbone charges as disconnected free ions and neglects chain connectivity correlations.

#### Random Phase Approximation (RPA)

RPA extends mean-field theory by including correlation corrections to the electrostatic free energy, improving predictions for charge sequence effects and salt dependence.

#### PC-SAFT and Molecular Equations of State

Perturbed-chain statistical associating fluid theory (PC-SAFT) and related equations of state provide rigorous molecular thermodynamic models for polyelectrolyte solutions [@ascani2025molecular]. These approaches address strong charge correlations and the complex interplay of short-range and long-range interactions.

### Field-Theoretic Simulations
Field-theoretic simulations (FTS) using complex Langevin sampling provide approximation-free phase diagrams for coacervate systems [@lee2008complex; @delaney2017theory].

Key advantages of FTS:

- No mean-field approximations
- Proper sampling of fluctuations in electrostatic and composition fields
- Prediction of spinodal and binodal boundaries
- Extension to multicomponent and multiphase systems [@chen2022multiphase]

FTS has been applied to IDP coacervation, revealing how charge patterning affects phase boundaries [@pal2019complete].

### Machine Learning Approaches
Machine learning offers opportunities for:

- Polymer property prediction from sequence
- High-throughput virtual screening of coacervate-forming systems
- Inverse design of polymers with target metal selectivity
- Analysis of MD trajectories to identify binding motifs

Bridging theoretical frameworks (field theory, ion pairing, explicit simulations) remains an active area providing unified understanding of polyelectrolyte complexation [@qin2023bridging; @li2024thermodynamic].

## Process Considerations
Translation of coacervate-based separations from laboratory to industrial scale requires addressing process engineering challenges.

### Continuous Processing
#### Flow-Based Coacervate Systems

{index}`Microfluidic <microfluidics>` platforms enable precise control of coacervate formation through:

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

Rigorous {index}`techno-economic <techno-economic analysis (TEA)>` analysis is needed comparing:

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
- {index}`Chromatographic <chromatography>` methods (coacervate-coated stationary phases)
- Electrochemical methods (redox-driven separations)
- Precipitation (coacervate-assisted crystallization)

### Hybrid Coacervate-Membrane Systems

Polymer inclusion membranes (PIMs) containing coacervate-forming polymers or selective extractants offer continuous separation with reduced solvent inventory [@kim2019separation].

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

1.  **Biomimetic approaches show the highest *group* selectivity**: lanmodulin discriminates rare earths from calcium and the common leachate cations by roughly eight orders of magnitude, and does so at pH 2.5 in real coal and e-waste liquors [@cotruvo2018lanmodulin; @deblonde2020selective]. Its intra-series discrimination is far weaker. Engineered dimer-interface variants have delivered a light/heavy split (Nd/Dy, \>98% purity, single-stage column) [@mattocks2023enhanced] and a light-lanthanide enrichment (Pr,Nd over La,Ce) [@larrinaga2024modulating], but no adjacent-pair separation factor comparable to a solvent-extraction cascade has been reported. The right place for these ligands in a flowsheet is therefore upstream concentration and group separation, not adjacent-pair fractionation.

2.  **Aqueous biphasic systems are most mature**: IL-based ABS and polymer-salt systems have demonstrated practical REE separations with good efficiency [@neves2022liquid; @kumar2022separation; @liu2022one].

3.  **Stimuli-responsive coacervates enable process integration**: Temperature, pH, and redox triggers allow controlled capture and release essential for continuous processes [@love2020reversible; @kumar2023comprehensive].

4.  **Computational methods guide rational design**: MD simulations, field-theoretic methods, and machine learning accelerate the discovery of improved coacervate systems [@zhang2022driving; @lee2008complex].

5.  **Significant challenges remain**: Selectivity for adjacent lanthanides (especially Nd/Pr), polymer cost and recyclability, and scale-up require further development.

### Recommended Research Directions

1.  Design of peptide-based coacervates incorporating lanthanide-selective motifs
2.  Development of stimuli-responsive systems for continuous extraction/stripping
3.  Integration of coacervates with membrane and electrochemical separations
4.  Techno-economic and lifecycle assessment comparing coacervate vs solvent extraction
5.  Pilot-scale demonstration with real REE-bearing feedstocks

The transition to sustainable REE processing requires new separation paradigms. Coacervate-based systems, operating under mild aqueous conditions with biological or bio-inspired selectivity, offer a path toward greener hydrometallurgy while potentially achieving higher separation efficiency than conventional methods.
