---
title: High-Throughput and Computational Methods
---

(high-throughput-and-computational-methods)=
# High-Throughput and Computational Methods

Rare earth separation has a search-space problem. An extraction system is
defined by an extractant, a diluent, a modifier, an acid, a pH, a temperature,
a salting agent, and a phase ratio, and the interactions between them are not
additive. Exploring that space one flask at a time is why extractant discovery
has historically moved at the pace of a career rather than a grant cycle.

Two things have changed. Robotic platforms now run extraction, phase separation,
and ICP analysis without a person in the loop, turning weeks of bench work into
a day of unattended screening. And machine-learned models trained on the
resulting data — and on quantum chemical calculations — can rank candidate
ligands before any of them are synthesised. Neither is a substitute for the
other: the value comes from the loop, where computation proposes and the
platform disposes.

This chapter covers both halves and the closed loop between them. The
thermodynamic grounding for what these models predict is in
[](#thermodynamics-of-extraction); the analytical throughput that limits how
fast the loop can turn is in [](#characterization-methods).

(automated-high-throughput-platforms-for-f-element-separations)=
## Automated High-Throughput Platforms for f-Element Separations
### LANL Super Separator Platform
@augustine2024advancing developed a comprehensive automated platform that integrates robotic liquid handling with machine learning optimization for rare-earth (4f) and actinide (5f) separations.

#### Platform Specifications

**Hardware Configuration:**

- Custom Big Kahuna automated instrument (Unchained Laboratories Inc.)
- Two robotic arms with automated liquid dispensing
  - Delivery accuracy: ±10 μL
  - Precision: ±5%
  - Maximum volume: 10 mL per dispense
- Six vortexers (2 temperature-controlled, 4 ambient)
- Integrated centrifugation for phase separation
- Radiologically compatible design for worker safety

**Throughput Capability:**

- Estimated ****200 measurements per day****
- Automated sample preparation, extraction, and characterization
- Rigorous control over experimental variables:
  - Analyte and extractant concentrations
  - pH and temperature
  - Contact times and mixing rates

#### Machine Learning Integration: Bayesian Optimization

The platform employs Bayesian Optimization with Gaussian Process surrogate models to guide experimental design:

**Key Features:**

- Adaptive experimental design responding to real-time data
- Kriging Believer acquisition function for batch selection
- RBF and Matérn kernels for model flexibility
- Implementation in scikit-learn and scipy

**Performance Achievements:**

- Identified optimal conditions using only ****63% of experiments**** compared to full factorial screening
- ****74% reduction**** in experimental effort for four-dimensional optimization
- Convergence in 4 experimental cycles (339 total measurements vs. 1,296 for full screening)
- Optimal Th {index}`distribution ratio` (D = 4.85 ± 0.8) achieved

#### Case Study: Thorium Extraction Optimization

The platform was validated on Th⁴⁺ extraction using N,N-di-2-ethylhexylbutyramide (DEHBA) with {index}`TBP <TBP (tributyl phosphate)>` in n-dodecane.

**Optimized Conditions:**

- \[Th⁴⁺\]~feed~ = 3.0 mM
- \[HNO₃\] = 4.0 M
- \[DEHBA\] = 40 mM
- Temperature = 25°C

**Human-in-the-Loop Safeguards:** The research team detected anomalous measurements (D = 6.58 ± 0.05) during cycle review that would have contaminated the Gaussian Process model. This demonstrates the value of expert oversight in automated optimization campaigns [@augustine2024advancing].

### Analytical Characterization Integration
#### ICP-AES Protocol for Thorium Quantification

@augustine2024advancing implemented rigorous ICP-AES analysis:

**Instrumentation:** PerkinElmer Avio 500

**Critical Protocol Elements:**

- Seven-point calibration curve (0-10 ppm Th⁴⁺)
- Extended wash cycle: 50 seconds with 0.1 M HNO₃ + 0.01 w% HF
  - Prevents {index}`thorium` adhesion to sample introduction hardware
  - Essential for accurate quantification
- Delay time: 65 seconds between samples
- Sample dilution: 10-1000× in 0.1 M HNO₃

#### General ICP-MS/ICP-AES Automation

High-throughput elemental analysis requires seamless integration of liquid handlers with ICP instrumentation:

**FAST Automated Systems:**

- 2-5× faster than standard autosamplers
- Rapid vacuum sample loading with valve injection
- Optical sensors for automatic sample detection
- Analysis completed in \<3 minutes per sample for trace elements

**SimPrep Integration:**

- Automated sample dilution up to 1:2500
- Fully automated calibration standard preparation
- Compatible with ICP-OES and ICP-MS platforms

### Data Management and Reproducibility
The LANL group deposited their complete dataset in the ****Separation Archive for f-elements (SAFE)**** at <https://safe.lanl.gov>, comprising 2,132 distribution ratios from literature involving 35 unique monoamide extractants and 11 actinide/lanthanide isotopes [@augustine2024advancing].

(high-throughput-extractant-synthesis-and-screening)=
## High-Throughput Extractant Synthesis and Screening
### Agile Diglycolamide Synthesis Platform
@an2024agile developed an integrated research, development, and deployment (RD&D) methodology combining facile ligand synthesis with rapid extraction evaluation.

#### Green Chemistry Approach: Melt-Amidation

**Innovation:**

- Solvent-free melt-amidation coupling diglycolic acid with secondary amines
- No post-reaction workup or purification required
- Full conversion at 200°C

**Performance:**

- Scalable to ****200 grams****
- Yields: 85-96%
- Purities: 88-96%
- Substrate scope: 9 different DGA variants

**Environmental Impact:** {index}`Life cycle assessment <life cycle assessment>` revealed ****67% reduction in global warming potential**** compared to prior synthetic pathways [@an2024agile].

**Advantages over Prior Art:**

- No pre-activation of diglycolic acid required
- Eliminates toxic organic solvents
- No toxic side-products or waste
- No tedious purification steps
- Reduced cost and process time
- Feasible industrial scale-up

#### Automated Extraction Screening

**Throughput:** The automated workflow completed ****over 180 runs in 48 hours****, enabling rapid structure-activity relationship investigations of alkyl-substituted DGAs [@an2024agile].

**Outcome:** The systematic ligand evaluation informed development of a promising flowsheet for separating light and heavy REEs.

### Diglycolamide Extractant Advantages
{index}`Diglycolamide <diglycolamide>` (DGA) extractants offer several advantages for REE separations:

- High extraction capacity
- Ease of synthesis (now enhanced by melt-amidation)
- Good thermal stability
- Good radiation stability
- Promising industrial applications

The work of [@an2024agile] demonstrates how integrating agile synthetic chemistry with automated screening accelerates discovery of sustainable extractants for critical materials.

(machine-learning-for-distribution-coefficient-prediction)=
## Machine Learning for Distribution Coefficient Prediction
### Deep Learning Approaches
@liu2022advancing developed deep neural networks (DNNs) trained on experimental data to predict distribution coefficients for lanthanide {index}`solvent extraction`, enabling high-throughput virtual screening.

#### Dataset and Model Performance

**Dataset:**

- 1,202 log D values collected from scientific literature
- Focused on single neutral ligands as extractants
- Covers lanthanide extraction across various conditions

**Model Architecture:**

- Combination of molecular physicochemical descriptors and atomic extended-connectivity fingerprints
- Deep neural network architecture

**Performance:**

- Best model: ****R² = 0.85****, ****RMSE = 0.53**** on validation set
- Successfully predicted D values for four novel ligand structures
- Experimental validation showed good agreement with predictions

#### Practical Application

Distribution (D) values assess ligand performance:

- D \> 1: More than 50% of lanthanide extracted into organic solvent
- Enables rapid screening of ligand candidates without synthesis
- Accelerates rational design of selective extractants

### Bayesian Optimization for Process Variables
Beyond ligand screening, [@augustine2024advancing] demonstrated that Bayesian Optimization with high-throughput robotics significantly accelerates optimization of extraction conditions (concentration, pH, temperature).

**Dataset Scope:**

- 2,132 distribution ratios from literature
- 35 unique monoamide extractants
- 11 different actinides and lanthanides

**Key Insight:** The combination of predictive modeling (for ligand selection) and adaptive experimentation (for process optimization) provides a complete workflow from molecular design to process conditions.

### Explainable AI and Future Directions
Recent work (2025) developed explainable AI systems to predict REE leaching efficiency and provide real-time explanations of key extraction factors, trained on 572 experimental datasets.

This trend toward interpretable models will help identify underlying chemical principles governing selectivity and inform next-generation extractant design.

## Integration of Computation and Experimentation
### Computational Pre-Screening → Targeted Experiments
The emerging workflow combines:

1.  **Virtual screening** using ML models ([@liu2022advancing])
    - Rapid prediction of log D for candidate ligands
    - Identification of promising structures
2.  **Automated synthesis** ([@an2024agile])
    - Scalable, sustainable synthesis methods
    - High-throughput synthesis of top candidates
3.  **Automated extraction testing** ([@augustine2024advancing])
    - Robotic platforms for systematic evaluation
    - ICP-AES/ICP-MS characterization
4.  **Process optimization** via Bayesian methods
    - Efficient exploration of multidimensional parameter space
    - Adaptive experimental design

### Active Learning for Closed-Loop Discovery
While not yet extensively demonstrated in REE separations literature, active learning strategies show promise in related materials discovery applications:

- Polymer solar cells: ****75% reduction in discovery time**** through active learning
- Catalysts and batteries: Iterative experiment selection based on model uncertainty
- Potential application: Closed-loop systems combining ML prediction, robotic synthesis/testing, and adaptive sampling

****Gap Identified:**** Integration of active learning specifically for separations chemistry remains an emerging area with significant potential for future development.

## Analytical Chemistry Considerations
### Sample Throughput Requirements
For meaningful high-throughput separations research:

- Target: ****100-200+ measurements per day****
- Requires automation of sample preparation, extraction, and analysis
- ICP-AES/ICP-MS must integrate seamlessly with liquid handling

### Critical Analytical Challenges
#### For Actinides (Th, U, Pu)

- Surface adhesion to sample introduction systems
- Extended wash protocols required ([@augustine2024advancing]: 50 sec with HF)
- Radiological safety considerations
- Specialized facilities and protocols

#### For Lanthanides

- Spectral interferences in ICP-MS
- Matrix effects from high salt concentrations
- Need for appropriate sample dilution strategies
- Calibration across wide concentration ranges

### Data Quality and Validation
High-throughput workflows require:

- Automated detection of outliers and anomalies
- Triplicate measurements for statistical confidence
- Human-in-the-loop review for quality assurance
- Standardized data formats and archiving (e.g., SAFE database)

(learned-binding-energies-as-a-dft-surrogate)=
## Learned Binding Energies as a DFT Surrogate

Where the deep-learning models above are trained on measured distribution
ratios, a second line of work learns the underlying binding energy directly and
so generalises beyond the conditions in the training set. @gupta2025accelerating
trained equivariant neural networks (Allegro) on 5,356 REE-ligand complexes,
reaching a mean absolute error of 6.1 kcal/mol on binding energy predicted
directly from structure. The point of that number is throughput: it bypasses the
DFT calculation that would otherwise gate every candidate, which is what makes
screening at the scale of a ligand library possible.

The thermodynamic cycle in [](#thermodynamics-of-extraction) is where such a
binding energy becomes a predicted extraction constant — and that chapter is
also where the limits of the conversion are set out.

It is worth putting that 6.1 kcal/mol next to the quantity it is meant to
predict. An adjacent-pair separation factor of 1.5 corresponds to a free-energy
difference of RT ln 1.5 ≈ 1.0 kJ/mol, or 0.24 kcal/mol; the Pr/Nd split is
nearer 0.9 kJ/mol ([](#the-energy-scale-of-selectivity)). The model error is
therefore about twenty-five times the signal, and screening only works because
the error is largely *systematic across the series* — the same ligand, the same
geometry, one substituted metal centre — and cancels in the difference. That
cancellation is what a screening campaign is actually relying on, and it is
testable: rank a series whose experimental order is known and check that the
ranking survives, rather than reporting agreement on absolute binding energies.
Nothing in a reported MAE tells you whether it does.

## Automated Process Control

Modern plants incorporate [@augustine2024advancing]:

- Real-time ICP-MS analysis
- Feedback control of pH, temperature, flow rates
- Active learning algorithms optimize extraction conditions
- Potential for "self-driving" separation plants

## Computational Approaches

Computational methods are increasingly important for understanding REE separation mechanisms, designing new ligands, and accelerating the discovery of more selective and sustainable extraction systems.

### Density Functional Theory (DFT) for Ligand Design
DFT calculations provide atomic-level insights into metal-ligand interactions and extraction mechanisms [@summers2024importance].

**Applications:**

- Geometry optimization of REE-ligand complexes
- Binding energy calculations
- Charge distribution analysis (Mulliken, NBO)
- Molecular orbital interactions
- Selectivity prediction

**Key Findings from DFT Studies:**

*{index}`D2EHPA` Extractant Selectivity:* DFT combined with Born-Haber
thermodynamics has been used to rationalise the heavy-REE preference of D2EHPA
[@alizadeh2023deep]. The qualitative argument is the one developed in
[](#thermodynamics-of-extraction): the smaller, more strongly hydrated ion pays
more to leave the aqueous phase but gains more on complexation, and for acidic
organophosphorus extractants the second term wins, so D rises from La to Lu.

The hydration energies tabulated in that preprint should not be carried
forward. They are several times smaller than the accepted single-ion values and
they rank La³⁺ as the more strongly hydrated of the pair, which is backwards.
Marcus gives ΔG_hyd(La³⁺) = -3145 kJ/mol [@marcus1991thermodynamics]; Y³⁺, whose
six-coordinate radius of 0.900 Å falls between Ho³⁺ and Er³⁺
[@shannon1976revised], interpolates to roughly -3450 kJ/mol on the same scale —
more negative than La³⁺, not less. Use the tabulated single-ion values, and
treat any hydration energy quoted without its extrathermodynamic convention as
unusable.

*Diglycolamide (DGA) Complexes:* Electrostatic interactions dominate Ln-DGA binding [@liu2021theoretical]:

- Covalent character increases along lanthanide series
- Binding pocket shrinks from La to Nd to Eu
- Explains observed selectivity trends

**Computational Challenges:** Metal complexes can have many stable configurations whose energy differences exceed the small energy differences determining selectivity. Incorrect predictions result if lowest-energy configurations are not identified [@summers2024importance]:

| Challenge            | Impact                           |
|----------------------|----------------------------------|
| Configuration search | Multiple minima must be explored |
| Relativistic effects | Important for heavy lanthanides  |
| Solvent effects      | Implicit vs. explicit solvation  |
| Basis set selection  | f-electron treatment             |

### COSMO-RS for Solvent Effects
COSMO-RS (Conductor-like Screening Model for Real Solvents) enables prediction of thermodynamic properties in liquid phases [@cheng2021theoretical].

**DFT + COSMO-RS Workflow:**

1.  Determine extraction stoichiometry experimentally
2.  Optimize extractant/complex structures (DFT)
3.  Calculate σ-profiles and chemical potentials
4.  Predict partition coefficients and selectivity

**Validated Applications:**

- β-diketone extraction of La/Ce
- {index}`Ionic liquid <ionic liquids>` diluent effects
- Temperature dependence prediction
- Multi-component system modeling

**Accuracy:** Theoretical selectivity trends agree closely with experimental results, including for ionic liquid systems.

### Molecular Dynamics (MD) Simulations
MD simulations reveal dynamic behavior and solvation structure of REE complexes.

**Applications:**

- Nitrate coordination dynamics in extraction
- Ligand flexibility and binding pocket size
- Interfacial behavior at organic/aqueous interface
- Aggregation phenomena in organic phase

**Key Findings:** BLPhen ligand studies show [@chapleski2020molecular]:

- Dynamic nitrate coordination (bidentate ↔ monodentate switching)
- Binding pocket contraction along La → Nd → Eu series
- Configuration changes correlate with selectivity

**Simulation Parameters:**

| Parameter | Typical Value |
| ----------- | --------------- |
| Time scale | 10-100 ns |
| Force field | AMBER, CHARMM, OPLS |
| REE parameters | Specialized (12-6-4 LJ) |
| Solvation | Explicit water + organic |

### Machine Learning for Extractant Screening
Deep neural networks enable high-throughput virtual screening of potential extractants ([@liu2022advancing], [ORNL](https://www.ornl.gov/publication/advancing-rare-earth-separation-machine-learning)).

**Input Features:**

| Category | Examples |
| ---------- | ---------- |
| Molecular descriptors | RDKit (208 descriptors) |
| Fingerprints | ECFP (extended connectivity) |
| Process conditions | Temperature, concentration |
| Solvent properties | Dielectric constant, viscosity |
| Total inputs | \~2291 per prediction |

**Model Architecture:**

- Deep neural networks trained on experimental D values
- SMILES → RDKit → Descriptor + ECFP pipeline
- Trained on curated solvent extraction database
- Predicts log D for Ln(III) ions

**Performance:**

| Metric | Value |
| -------- | ------- |
| Training data | Thousands of experimental D values |
| Prediction accuracy | R² \> 0.85 for held-out test |
| Throughput | Millions of compounds/day |
| Use case | Virtual screening, prioritization |

**Applications:**

- Rapid evaluation of novel ligand structures
- Identification of structure-activity relationships
- Guidance for synthetic chemistry efforts
- Optimization of extraction conditions

### QSPR Models
Quantitative Structure-Property Relationships correlate molecular descriptors with extraction properties.

**Common Descriptors:**

| Category | Examples |
| ---------- | ---------- |
| Constitutional | MW, atom counts, bond counts |
| Topological | Connectivity indices, shape |
| Electronic | HOMO/LUMO, partial charges |
| Geometric | Surface area, volume |
| Lipophilicity | log P, polar surface area |

**Model Types:**

- Multiple linear regression (MLR)
- Partial least squares (PLS)
- Random forests
- Support vector machines (SVM)
- Gradient boosting (XGBoost, LightGBM)

**Validation:**

| Method | Description |
| -------- | ------------- |
| Cross-validation | K-fold, leave-one-out |
| External test set | Held-out experimental data |
| Y-scrambling | Randomization check |
| Applicability domain | Chemical space coverage |

### Automated Structure Generation
The Architector package automates metal-ligand complex construction [@summers2024importance]:

**Workflow:**

1.  Input: ligand SMILES + metal ion
2.  Automated 3D structure generation
3.  Configuration exploration
4.  Semi-empirical optimization (GFN2-xTB)
5.  DFT refinement of promising candidates
6.  Property prediction

**Advantages:**

- Eliminates human bias in structure construction
- Explores vast conformational space
- Computationally efficient screening
- Interfaces with high-level DFT

### Process Simulation

**Software Platforms:**

| Software | Application |
| ---------- | ------------- |
| Aspen Plus | Flowsheet simulation |
| MATLAB/Python | Custom extraction models |
| gPROMS | Dynamic process modeling |
| DWSIM | Open-source alternative |

**Solvent Extraction Simulation:** {index}`Counter-current <countercurrent cascade>` cascade modeling [@turgeon2023simulation]:

- Stage-wise mass balance
- Equilibrium and kinetic models
- Parameter estimation from lab data
- Optimization of stage count, A/O ratio

### Speciation Modeling

**Geochemical Codes:**

| Software | Capabilities |
| ---------- | ------------- |
| PHREEQC | Aqueous equilibrium, adsorption |
| Geochemist's Workbench | Reaction path modeling |
| MINTEQ | Trace metal speciation |
| EQ3/6 | High T/P geochemistry |

**Thermodynamic Databases:**

- NIST Critical Stability Constants
- NEA-TDB (nuclear applications)
- THEREDA (waste disposal)
- Custom databases for novel extractants

### Emerging Computational Approaches
**Generative Models for Ligand Design:**

- Variational autoencoders (VAE)
- Generative adversarial networks (GAN)
- Reinforcement learning for property optimization
- Automatic generation of novel molecular structures

**Graph Neural Networks:**

- Direct learning on molecular graphs
- Message passing for property prediction
- Transfer learning from large databases

**Multi-Objective Optimization:**

- Pareto optimization of selectivity + sustainability
- Genetic algorithms for extractant design
- Bayesian optimization for process conditions

**High-Throughput Computing:**

- Cloud-based DFT screening
- Workflow automation (FireWorks, AiiDA)
- Database integration (Materials Project, NOMAD)

### Integration with Experimental Workflows
**Closed-Loop Discovery:**

1.  ML model predicts promising candidates
2.  Automated synthesis (if feasible)
3.  High-throughput extraction screening
4.  Data fed back to improve model
5.  Iterate until target selectivity achieved

**Current Limitations:**

- Limited experimental training data
- Difficulty predicting kinetics
- Gap between model compounds and real ores
- Multi-phase system complexity

**Future Directions:**

- Active learning for efficient data collection
- Physics-informed neural networks
- Multi-scale modeling (molecular → process)
- Integration with robotic laboratories
