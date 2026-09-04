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

This chapter follows that order. It starts with the automated platforms and the
synthesis routes that keep them fed, then with the analytical measurement that
sets the rate at which either can run; it then turns to the computational
methods that propose candidates, to the data-driven models trained on
experiment and on computation, and finally to what it would take to close the
loop between them. The thermodynamic grounding for what these models predict is
in [](#thermodynamics-of-extraction); the analytical methods themselves are in
[](#characterization-methods).

(automated-high-throughput-platforms-for-f-element-separations)=
## Automated High-Throughput Platforms for f-Element Separations

@augustine2024advancing built the platform most of this chapter's experimental
half refers to: a robotic liquid handler coupled to ICP-AES and driven by a
Bayesian optimizer, applied to rare-earth (4f) and actinide (5f) separations.
It is a bench instrument, not a plant, and reading it as anything else is the
main way this literature gets over-sold.

### The LANL Super Separator Platform

#### Platform Specifications

**Hardware configuration:**

- Custom Big Kahuna automated instrument (Unchained Laboratories Inc.)
- Two robotic arms with automated liquid dispensing
  - Delivery accuracy: ±10 μL
  - Precision: ±5%
  - Maximum volume: 10 mL per dispense
- Six vortexers (2 temperature-controlled, 4 ambient)
- Integrated centrifugation for phase separation
- Radiologically compatible design for worker safety

**Throughput capability:**

- Estimated **200 measurements per day**
- Automated sample preparation, extraction, and characterization
- Rigorous control over experimental variables:
  - Analyte, extractant and holdback concentrations
  - pH and temperature
  - Contact times and mixing rates

#### Bayesian Optimization as the Control Loop

The platform is driven by Bayesian Optimization with a Gaussian Process
surrogate model. The surrogate is fitted to every distribution ratio measured so
far and is then asked where to sample next; the batch of conditions it proposes
is run, the model is refitted, and the cycle repeats. Two implementation choices
matter for reproducing the method [@augustine2024advancing]:

- **Acquisition function.** Batches were chosen with *Kriging Believer*, which
  picks one point, provisionally assumes the surrogate's own mean as the
  measured answer there, refits, and picks the next — so that a batch of
  conditions run in parallel does not consist of the same point several times
  over. It was compared against Thompson sampling, distance exploration, and
  random sampling.
- **Kernel.** Anisotropic radial basis function (RBF) and Matérn kernels were
  compared. The Matérn kernel is the less smooth of the two and is the usual
  choice when the response surface is not expected to be infinitely
  differentiable. Hyperparameters were fitted by maximizing the log marginal
  likelihood. The implementation uses scikit-learn and scipy.

The method was developed first as a *virtual* campaign — replayed against a
literature dataset of UO₂²⁺ extraction by DEHiBA, where the answer was already
known — before it was allowed to spend real experiments. In that retrospective
test the optimizer found the maximum D(U) in the dataset after at most 90
experiments out of a 244-point space, a 63% saving against exhaustive sampling
[@augustine2024advancing].

#### Case Study: Thorium Extraction Optimization

The live campaign optimized Th⁴⁺ extraction by
N,N-di-2-ethylhexylbutyramide (DEHBA) in 20 v%
{index}`TBP <TBP (tributyl phosphate)>`/n-dodecane over four variables: feed
Th⁴⁺ concentration, nitric acid concentration, DEHBA concentration, and
temperature.

The {index}`distribution ratio` converged after four experimental cycles — 113
unique conditions and 339 total measurements, the difference being triplicates.
A grid covering the same region would have required an estimated 432 unique
conditions, or 1,296 measurements in triplicate, so the optimizer reached the
same answer for about 26% of the experimental effort — the **74% saving** the
paper reports. The best measured value was D = 4.85 ± 0.8, at:

- $[\mathrm{Th}^{4+}]_\mathrm{feed}$ = 3.0 mM
- \[HNO₃\] = 4.0 M
- \[DEHBA\] = 40 mM
- Temperature = 25°C

**Human-in-the-loop safeguards.** One measurement in cycle 2 returned
D = 6.58 ± 0.05, well above anything else seen. The Gaussian Process model
believed it, and predicted that still higher acid concentrations would do better
still; a fifth batch run around that point produced nothing above D = 4.03 and a
visible collapse in model accuracy. Removing the single anomalous point and
retraining restored the predictions for cycles 4 and 5. An automated campaign
will happily chase a bad measurement, and the only thing that caught this one
was a person reviewing the cycle [@augustine2024advancing].

### Data Management and Reproducibility

The LANL group deposited both datasets in the **Separation Archive for
f-elements (SAFE)** at <https://safe.lanl.gov>. The literature compilation
assembled for the study comprises 2,132 distribution ratios drawn from published
experiments, covering 35 unique monoamide extractants and 11 different actinides
[@augustine2024advancing]. Those 2,132 values are unique reported conditions and
do not account for replicates run within a single study — a caveat worth keeping
in mind whenever such a compilation is used as training data.

(high-throughput-extractant-synthesis-and-screening)=
## High-Throughput Extractant Synthesis and Screening

A screening platform is only as good as the supply of candidate molecules it can
be fed, and for most ligand families synthesis is the bottleneck.
@an2024agile addressed this directly, coupling a deliberately simple synthesis
to automated evaluation in one research, development and deployment loop.

### Agile Diglycolamide Synthesis Platform

#### Green Chemistry Approach: Melt-Amidation

**Innovation:**

- Solvent-free melt-amidation coupling diglycolic acid with secondary amines
- No post-reaction workup or purification required
- Full conversion at 200°C

**Performance:**

- Scalable to **200 grams**
- Yields: 85-96%
- Purities: 88-96%
- Substrate scope: 9 different DGA variants

**Environmental impact:** {index}`Life cycle assessment <life cycle assessment>`
found a **67% reduction in global warming potential** compared with prior
synthetic pathways [@an2024agile]. A life-cycle comparison against the route it
replaces is the part usually missing from papers of this kind.

**Advantages over prior art:**

- No pre-activation of diglycolic acid required
- Eliminates toxic organic solvents
- No toxic side-products or waste
- No tedious purification steps
- Reduced cost and process time
- Feasible industrial scale-up

#### Automated Extraction Screening

The automated workflow completed **over 180 runs in 48 hours**, which is what
made a systematic structure-activity study of alkyl-substituted DGAs practical
rather than merely desirable. The resulting ligand evaluation informed a
flowsheet for separating light from heavy REEs [@an2024agile].

### Why Diglycolamides

{index}`Diglycolamide <diglycolamide>` (DGA) extractants are a natural target
for this treatment because they combine high extraction capacity, ease of
synthesis — now more so, given melt-amidation — and good thermal and radiation
stability, which is what makes them candidates for industrial and nuclear-fuel
service. The point of [@an2024agile] is the coupling: agile synthetic chemistry
feeding automated screening shortens the discovery cycle for sustainable
extractants in a way that neither half achieves alone.

## Analytical Throughput and Its Constraints

Every loop in this chapter turns at the speed of its elemental analysis. The
instruments themselves are covered in [](#characterization-methods); what
matters here is what they cost per sample and where they fail under automation.

### Sample Throughput Requirements

Meaningful high-throughput separations work needs on the order of **100-200+
measurements per day** — the LANL platform reports an estimated 200 per day
[@augustine2024advancing], which is an estimate from its automated cycle time
rather than a sustained measured rate. Reaching it
requires sample preparation, extraction and analysis all to be automated, and
the ICP-AES or ICP-MS to be integrated with the liquid handler rather than
operated as a separate queue.

### Automating ICP-AES and ICP-MS

@augustine2024advancing quantified {index}`thorium` on a PerkinElmer Avio 500
under a protocol built around one specific failure mode:

- Seven-point calibration curve (0-10 ppm Th⁴⁺)
- Extended wash cycle: 50 seconds with 0.1 M HNO₃ + 0.01 w% HF
  - Prevents thorium adhesion to sample introduction hardware
  - Essential for accurate quantification
- Delay time: 65 seconds between samples
- Sample dilution: 10-1000× in 0.1 M HNO₃

The wash and delay together cost nearly two minutes per sample and exist only to
stop the previous sample contaminating the next. That is the general shape of
the problem: the throughput of an automated platform is usually set by carryover
management, not by the spectrometer.

Commercial fast-loop autosamplers and automated dilution modules (Elemental
Scientific's FAST and SimPrep, for example) are marketed for this duty, claiming
2-5× the throughput of a standard autosampler through vacuum sample loading with
valve injection and optical sample detection, trace-element analysis in under
three minutes per sample, automated dilution up to 1:2500, and automated
preparation of calibration standards, on both ICP-OES and ICP-MS. These are
manufacturer specifications rather than independently benchmarked figures, and
should be read as such.

### Element-Specific Analytical Challenges

**For actinides (Th, U, Pu):**

- Surface adhesion to sample introduction systems
- Extended wash protocols required (50 s with HF [@augustine2024advancing])
- Radiological safety considerations
- Specialized facilities and protocols

**For lanthanides:**

- Spectral interferences in ICP-MS
- Matrix effects from high salt concentrations
- Need for appropriate sample dilution strategies
- Calibration across wide concentration ranges

### Data Quality and Validation

High-throughput workflows need automated detection of outliers and anomalies,
replicate measurements for statistical confidence, human review of each cycle
before its data is trusted, and standardized formats and archiving so that the
data outlives the campaign. The thorium case above is the argument for the
third of these; SAFE is an instance of the fourth.

## Computational Approaches

Computational methods enter at the other end: understanding separation
mechanisms, designing ligands, and reducing the number of candidates that ever
need to be made. This section covers the physics-based methods; the models
trained on data follow in the two sections after it.

### Density Functional Theory (DFT) for Ligand Design

DFT calculations provide atomic-level insight into metal-ligand interactions and
extraction mechanisms [@summers2024importance].

**Applications:**

- Geometry optimization of REE-ligand complexes
- Binding energy calculations
- Charge distribution analysis (Mulliken, NBO)
- Molecular orbital interactions
- Selectivity prediction

*{index}`D2EHPA` extractant selectivity.* DFT combined with Born-Haber
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

*Diglycolamide (DGA) complexes.* Electrostatic interactions dominate Ln-DGA
binding, with covalent character increasing along the lanthanide series and the
binding pocket contracting from La to Pr to Eu — a contraction that tracks the
observed selectivity trend [@liu2021theoretical].

**Computational challenges.** Metal complexes can have many stable
configurations whose energy differences exceed the small energy differences that
determine selectivity. Incorrect predictions result if the lowest-energy
configurations are not identified [@summers2024importance]:

| Challenge            | Impact                           |
|----------------------|----------------------------------|
| Configuration search | Multiple minima must be explored |
| Relativistic effects | Important for heavy lanthanides  |
| Solvent effects      | Implicit vs. explicit solvation  |
| Basis set selection  | f-electron treatment             |

The implicit-versus-explicit solvation question is treated at length in
[](#thermodynamics-of-extraction) and is not repeated here.

### COSMO-RS for Solvent Effects

COSMO-RS (Conductor-like Screening Model for Real Solvents) predicts
thermodynamic properties in liquid phases from the surface-charge distribution —
the σ-profile — of each species, which is computed once per molecule and then
reused for any mixture [@cheng2021theoretical].

**DFT + COSMO-RS workflow:**

1. Determine extraction stoichiometry experimentally
2. Optimize extractant/complex structures (DFT)
3. Calculate σ-profiles and chemical potentials
4. Predict partition coefficients and selectivity

**Validated applications:**

- β-diketone extraction of La/Ce
- {index}`Ionic liquid <ionic liquids>` diluent effects
- Temperature dependence prediction
- Multi-component system modeling

Theoretical selectivity trends agree closely with experiment in these systems,
including for the ionic-liquid diluents [@cheng2021theoretical]. Note that the
agreement is on trends; the caution in [](#the-energy-scale-of-selectivity)
about absolute free energies applies here as much as to DFT.

### Molecular Dynamics (MD) Simulations

Where DFT and COSMO-RS give a static or averaged picture, MD gives the dynamic
one: how a ligand's binding pocket flexes, how nitrate and water exchange in and
out of the coordination sphere, what happens at the organic/aqueous interface,
and whether the loaded organic phase aggregates. Interfacial and aggregation
behaviour is not accessible to a single-complex calculation at all, which is the
main reason to run MD in this field.

@chapleski2020molecular is a worked example of the approach applied to REE
beneficiation rather than extraction: molecular simulation combined with
interfacial spectroscopy to work out how a collector binds a mineral surface,
used to explain losses in flotation.

**Typical simulation parameters:**

| Parameter | Typical Value |
| ----------- | --------------- |
| Time scale | 10-100 ns |
| Force field | AMBER, CHARMM, OPLS |
| REE parameters | Specialized (12-6-4 LJ, which adds an induced-dipole term to the usual Lennard-Jones form) |
| Solvation | Explicit water + organic |

### Automated Structure Generation

Building a starting geometry for an f-element complex by hand is both slow and
biased toward the coordination modes the builder already expects. The
Architector package automates it across the periodic table, generating
three-dimensional mononuclear complexes for s-, p-, d- and f-block metals
[@taylor2023architector], and it is the tool behind the configuration-search
argument above [@summers2024importance]:

1. Input: ligand SMILES + metal ion
2. Automated 3D structure generation
3. Configuration exploration
4. Semi-empirical optimization (GFN2-xTB, a fast tight-binding method used to
   triage geometries before DFT)
5. DFT refinement of promising candidates
6. Property prediction

### Speciation Modeling

**Geochemical codes:**

| Software | Capabilities |
| ---------- | ------------- |
| PHREEQC | Aqueous equilibrium, adsorption |
| Geochemist's Workbench | Reaction path modeling |
| MINTEQ | Trace metal speciation |
| EQ3/6 | High T/P geochemistry |

**Thermodynamic databases:**

- NIST Critical Stability Constants
- NEA-TDB (nuclear applications)
- THEREDA (waste disposal)
- Custom databases for novel extractants

### Process Simulation

The computational methods above work at the scale of a molecule or a single
contact. The other computational tradition in this field works at the scale of
the plant: {index}`counter-current <countercurrent cascade>` cascade modeling
[@turgeon2023simulation] built on stage-wise mass balances and equilibrium
closures, parameters estimated from laboratory data, and optimization of
stage count and A/O ratio.

That is a chapter of its own, and it is the next one.
[](#process-modeling-and-optimization) covers the software platforms, the
cascade design theory they implement, and the open-source equation-oriented
frameworks — IDAES and PrOMMiS — where most current rare-earth process modeling
work is being done.

(machine-learning-for-distribution-coefficient-prediction)=
## Machine Learning for Distribution Coefficient Prediction

### Deep Learning on Measured Distribution Ratios

@liu2022advancing trained deep neural networks on measured distribution
coefficients for lanthanide {index}`solvent extraction`, with the aim of
screening candidate ligands before any of them are made.

**Dataset.** 1,202 log D values collected from the literature, restricted to
single neutral ligands as extractants and covering lanthanide extraction across
a range of conditions.

**Inputs.** Molecular physicochemical descriptors and atomic
extended-connectivity fingerprints (ECFP — a hash of the atom environments out
to a fixed bond radius, which encodes substructure presence rather than any
physical property), together with process and solvent variables:

| Category | Examples |
| ---------- | ---------- |
| Molecular descriptors | RDKit (208 descriptors) |
| Fingerprints | ECFP (extended connectivity) |
| Process conditions | Temperature, concentration |
| Solvent properties | Dielectric constant, viscosity |
| Total inputs | \~2291 per prediction |

**Performance.** The best model reached **R² = 0.85** and **RMSE = 0.53** on the
validation set. Four novel ligand structures were predicted, then synthesised
and measured, and the measurements agreed with the predictions
[@liu2022advancing]. That last step is what distinguishes this from a
cross-validation exercise, and it is rarer in this literature than it should be.

**Reading a predicted D.** D > 1 means more than half the lanthanide sits in the
organic phase *at equal phase volumes*; at any other A/O ratio the fraction
extracted moves even though D does not, which is the most common way the number
is misread. Screening on predicted D therefore ranks ligands, and does not by
itself tell you what a stage will do.

### QSPR Models

Quantitative structure-property relationships correlate molecular descriptors
with extraction properties, and remain useful where the dataset is too small for
a neural network.

**Common descriptors:**

| Category | Examples |
| ---------- | ---------- |
| Constitutional | MW, atom counts, bond counts |
| Topological | Connectivity indices, shape |
| Electronic | HOMO/LUMO, partial charges |
| Geometric | Surface area, volume |
| Lipophilicity | log P, polar surface area |

**Model types:** multiple linear regression (MLR), partial least squares (PLS),
random forests, support vector machines, and gradient boosting (XGBoost,
LightGBM).

**Validation:**

| Method | Description |
| -------- | ------------- |
| Cross-validation | K-fold, leave-one-out |
| External test set | Held-out experimental data |
| Y-scrambling | Randomization check |
| Applicability domain | Chemical space coverage |

### Explainable Models

Predictive accuracy alone does not tell a chemist which variable to change.
@nguyen2025explainable trained an explainable system on 572 experimental
datasets compiled from the literature to predict REE leaching efficiency from
secondary resources and to attribute each prediction to the process variables
driving it, reaching R² = 0.81 and identifying silica concentration as the
dominant factor, ahead of light-versus-heavy REE classification, with pH,
aluminium content and temperature contributing less.

Two caveats. The work is on leaching from secondary resources, not on solvent
extraction, so the specific ranking does not transfer. And an attribution is a
statement about the model, not about the chemistry: it says which input the
model is using, which is a hypothesis about mechanism rather than evidence for
one. Read that way, interpretable models are a useful source of leads for
next-generation extractant design.

(learned-binding-energies-as-a-dft-surrogate)=
## Learned Binding Energies as a DFT Surrogate

Where the deep-learning models above are trained on measured distribution
ratios, a second line of work learns the underlying binding energy directly and
so generalises beyond the conditions in the training set. @gupta2025accelerating
trained equivariant neural networks (Allegro) on 5,356 REE-ligand complexes,
reaching a mean absolute error of 6.1 kcal/mol on binding energy predicted
directly from structure. "Equivariant" here means the network's internal
representation rotates with the molecule instead of being invariant to rotation,
which is what lets it predict a directional, geometry-dependent quantity from
coordinates. The point of that number is throughput: it bypasses the DFT
calculation that would otherwise gate every candidate, which is what makes
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

## Closing the Loop

### The Workflow End to End

Each of the pieces above exists. Assembled, they describe a workflow that no
single published study has yet run from end to end for REE separations:

1. **Virtual screening** with a trained model [@liu2022advancing]
   - Rapid prediction of log D for candidate ligands
   - Identification of promising structures
2. **Agile synthesis** of the survivors [@an2024agile]
   - Scalable, sustainable synthetic routes
   - High-throughput synthesis of top candidates
3. **Automated extraction testing** [@augustine2024advancing]
   - Robotic platforms for systematic evaluation
   - ICP-AES/ICP-MS characterization
4. **Process optimization** by Bayesian methods
   - Efficient exploration of a multidimensional parameter space
   - Adaptive experimental design

Steps 1-2 and 3-4 have each been demonstrated as a pair. What has not been
demonstrated is data from step 3 flowing back into the model of step 1 and
changing what step 2 makes next.

### Active Learning and the Gap It Leaves

That feedback is what active learning names: choose the next experiment where
the model is most uncertain, or where the expected improvement is largest, and
retrain. The strategy is well established in adjacent materials-discovery
domains — catalysts, batteries, photovoltaics — where iterative experiment
selection based on model uncertainty is now routine. Applied to separations, it
remains close to unexplored, despite an unusually good fit: expensive
experiments, a continuous design space, and a clear scalar objective. The
Bayesian optimization campaign above is the closest published instance, and it
optimizes process conditions for a fixed ligand rather than searching over
molecules. This gap is discussed alongside the field's other automation gaps in
[](#gaps-in-automation-and-computation).

### Automated Process Control: What Is Demonstrated and What Is Not

A "self-driving" separation plant is a projection, not a description. What has
been demonstrated is a bench platform closing a loop over a few hundred
measurements under expert supervision [@augustine2024advancing]. A plant would
additionally require on-line elemental analysis fast enough to control on,
feedback control of pH, temperature and flow rates against that analysis, and
an optimizer trusted to move setpoints on a stream carrying inventory — and most
automated platforms today still analyse offline, after the fact. The individual
control elements are ordinary process engineering; the closed machine-learning
loop over a live separation circuit is not, and no commercial REE plant is
reported to run one.

### Current Limitations

- Limited experimental training data, inconsistently reported
- Difficulty predicting kinetics rather than equilibrium
- Gap between model compounds and real ores or scrap
- Multi-phase system complexity

The first of these is the binding one and it is not a modelling problem:
distribution ratios are published without the ionic strength, phase ratio or
equilibration time needed to use them, so a compilation such as SAFE is
assembled from records that are individually incomplete.

### Emerging Directions

**Generative models for ligand design:** variational autoencoders, generative
adversarial networks, and reinforcement learning for property optimization,
proposing novel structures rather than ranking a fixed library.

**Graph neural networks:** direct learning on molecular graphs, message passing
for property prediction, transfer learning from large databases.

**Multi-objective optimization:** Pareto optimization of selectivity against
sustainability, and genetic algorithms for extractant design, where the target
is a trade-off surface rather than a single best ligand.

**High-throughput computing:** cloud-based DFT screening, workflow automation
(FireWorks, AiiDA), and integration with materials databases (Materials Project,
NOMAD).

**Physics-informed and multi-scale models:** constraining a learned model with
the thermodynamics it must obey, and carrying a molecular-scale prediction
through to process scale.

These are directions rather than results. The record in this chapter is that the
demonstrated gains — 74% fewer experiments for one four-variable optimization,
180 screening runs in 48 hours, R² = 0.85 on held-out distribution ratios — came
from careful coupling of ordinary methods to automation, not from any single
algorithmic advance.
