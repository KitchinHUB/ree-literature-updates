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
methods that propose candidates, and finally to what it would take to close the
loop between them. The data-driven models trained on the experiments and
calculations described here have a chapter of their own,
[](#machine-learning-in-rare-earth-separations). The thermodynamic grounding for
what these models predict is in [](#thermodynamics-of-extraction); the
analytical methods themselves are in [](#characterization-methods).

(automated-high-throughput-platforms-for-f-element-separations)=
## Automated High-Throughput Platforms for f-Element Separations

@augustine2024advancing built the platform most of this chapter's experimental
half refers to: a robotic liquid handler coupled to ICP-AES and driven by a
Bayesian optimizer, applied to rare-earth (4f) and actinide (5f) separations.
It is a bench instrument, not a plant, and reading it as anything else is the
main way this literature gets over-sold.

### The LANL Super Separator Platform

#### Platform Specifications

The platform is a customized Big Kahuna instrument (Unchained Laboratories) with
two robotic arms dispensing liquid to ±10 μL and ±5% precision, up to 10 mL per
dispense; six vortexers, two of them temperature-controlled; and integrated
centrifugation to break the phases. The whole thing is built to be
radiologically compatible, which is not a detail — it is what allows actinides
to be run on the same platform as the lanthanides, and it is why the analytical
problems below include plutonium.

The estimated throughput is 200 measurements per day, and the reason that number
is worth more than it looks is the list of variables the automation holds fixed
while it varies one: analyte, extractant and holdback concentrations, pH,
temperature, contact time and mixing rate. A distribution ratio measured by hand
carries the uncertainty of all seven. Measured this way it carries the
uncertainty of the dispense.

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
f-elements (SAFE)** at <https://safe.lanl.gov>, since announced formally in the
literature as the Separation Archive for Elements [@leite2025creation]. The
literature compilation
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

The synthesis is the part that makes the rest possible. Diglycolic acid and a
secondary amine are heated together without solvent until they melt and react;
at 200 °C the conversion is complete, and because nothing else is in the pot
there is nothing to separate out afterwards. No pre-activation of the acid, no
organic solvent, no toxic by-product, no column. The reported scope is nine DGA
variants, at yields of 85-96% and purities of 88-96%, on a scale as large as
200 grams [@an2024agile].

Every one of those is a claim about convenience rather than about chemistry, and
convenience is exactly what decides whether a structure-activity study of
twenty ligands happens or does not. The route that melt-amidation replaces
requires activating the acid, running in solvent, and purifying each product,
which is enough friction to keep most groups working with the three or four
diglycolamides they can buy.

The environmental case is made the same way and, unusually, is measured:
{index}`life cycle assessment <life cycle assessment>` puts the reduction in
global warming potential at 67% against the prior synthetic pathways
[@an2024agile]. A life-cycle comparison against the route being replaced is the
part usually missing from papers of this kind.

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

The actinides and the lanthanides fail differently, and both failures are
carry-over problems rather than chemistry problems.

Thorium, uranium and plutonium stick to the sample introduction system, so what
the instrument reports for one sample is contaminated by the one before it. The
fix is a longer wash — 50 seconds with hydrofluoric acid in the protocol reported
here [@augustine2024advancing] — which costs throughput directly, and the whole
of it has to happen inside a facility licensed for the material.

The lanthanides do not adhere, but they interfere. Their ICP-MS spectra overlap
each other and their oxides overlap the next elements along; the high salt
loading of a real extraction raffinate suppresses the signal; and the
concentrations across a distribution-ratio measurement span orders of magnitude,
so both the dilution strategy and the calibration have to be designed rather than
defaulted.

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

What DFT is asked to do here is a short list: optimize the geometry of a
lanthanide-ligand complex, compute a binding energy, look at where the charge
sits and which orbitals overlap, and from those predict which of two neighbouring
lanthanides a ligand will prefer. The last item is the one that matters and the
one that is hard, for the reason @summers2024importance make central: the energy
differences that set lanthanide selectivity are smaller than the energy
differences between alternative stable configurations of the same complex, so a
calculation that models the wrong configuration can get the selectivity trend
backwards while looking perfectly converged. Their answer is to automate the
construction and search of the configuration space rather than build structures
by hand, and they show across a crown ether, a phenanthroline monocarboxamide
and a malonamide that the search is what decides whether the predicted trend
matches experiment.

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

## Machine Learning: A Pointer

The data-driven half of this subject — models trained on measured distribution
ratios, on compiled stability constants, and on computed binding energies, and
the generative and agentic workflows built on top of them — is
[](#machine-learning-in-rare-earth-separations), the chapter after next. It is
separated out because it now extends well past extractant screening into
flowsheet synthesis and process control, and because its failure modes need
more room than a section allows. The platform and the analytical throughput
described above are what supply it with data.

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

Steps 1-2 and 3-4 have each been demonstrated as a pair, and one campaign has
now joined 1, 3 and 4. What has not been demonstrated is data from step 3
flowing back into the model of step 1 and changing what step 2 *makes* next.

(the-campaign-that-joins-screening-to-measurement)=
### The Campaign That Joins Screening to Measurement

@augustine2026coupling is the closest thing in the literature to the workflow
above, and it is worth being exact about which links it makes. The target is a
pH-controlled extraction in which selectivity is tuned not by changing the
extractant but by adding an aqueous-phase *holdback agent* that competes for the
metal. Database screening, density functional theory and a first round of
experiment picked oxaloacetic acid out of the candidates; automated
high-throughput experiments then mapped the response over four variables at once
— pH, extractant concentration, holdback concentration and salt concentration —
under multi-objective Bayesian optimization. Against HDEHP alone the optimizer
reported a fourfold increase in separation factors, without the exhaustive grid
that mapping four variables would otherwise demand.

The chemistry it reports is a pH switch. At pH ≈ 2.0 Eu, Dy and Ho extract
selectively over Nd; dropping to pH ≈ 0.5 changes which pair splits, and Eu
separates from Dy and Ho. Those are four real lanthanides and the numbers are
measured, not predicted, which is what distinguishes this campaign from the
generative workflows in [](#machine-learning-in-rare-earth-separations).

What it does not do is close the molecular loop. The molecule was chosen once,
computationally, at the start; the learning that follows searches *conditions*
for a fixed pair of reagents. Nothing measured on the platform goes back into a
model that then proposes a different molecule to synthesize. That link is still
the missing one. Nor are the splits adjacent-pair splits: the reported
separations are {Eu, Dy, Ho} from Nd, and Eu from {Dy, Ho}. Dy and Ho are the
one adjacent pair in the set, and they stay together. This work is read here
from its abstract; the full text was not available.

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

### What the Record Actually Shows

The demonstrated gains in this chapter — 74% fewer experiments for one
four-variable optimization, 180 screening runs in 48 hours — came from careful
coupling of ordinary methods to automation, not from any single algorithmic
advance. That is the right expectation to carry into
[](#machine-learning-in-rare-earth-separations), where the modelling side is
treated on its own terms and its own limits.
