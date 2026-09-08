---
title: Machine Learning in Rare Earth Separations
---

(machine-learning-in-rare-earth-separations)=
# Machine Learning in Rare Earth Separations

The previous two chapters describe the two things a data-driven model in this
field can be attached to. [](#high-throughput-and-computational-methods) is the
apparatus that generates measurements faster than a person can, and the quantum
chemistry that generates them without an experiment at all.
[](#process-modeling-and-optimization) is the plant model those measurements
eventually have to feed. This chapter is about what sits between: models that
learn a mapping from data rather than deriving one, and what they can and cannot
be trusted to do in a field whose defining feature is that the thing being
predicted is very small.

That last point is the whole difficulty, and it is worth stating before any of
the methods. An adjacent-pair separation factor of 1.5 corresponds to a
free-energy difference of RT ln 1.5 ≈ 1.0 kJ/mol, or 0.24 kcal/mol
([](#the-energy-scale-of-selectivity)). No other application of machine learning
in chemistry asks a model to resolve a target that small. Drug-discovery models
are asked for order-of-magnitude discrimination; a lanthanide separation model
is asked for a quarter of a kilocalorie, in a series of fourteen elements whose
chemistry differs by the width of an ionic radius. Every claim in this chapter
should be read against that number.

The second difficulty is data. @opare2021comparative surveyed rare earth
separation across the 2015-2020 literature using both narrative and bibliometric
methods, and found leaching, solvent extraction, and plasma to be the three most
explored and mature techniques; leaching — with acids, bases, ionic liquids and
salts — is the dominant one across more than forty distinct fields of research.
A field
that broad, published that diffusely, does not produce the kind of uniform
tabulated corpus that machine learning in other domains was built on. Almost
every dataset in this chapter was assembled by hand from the primary literature,
and almost every one is smaller than a thousand points.

This chapter proceeds from what the models are trained on, through the three
prediction targets that have actually been attempted — distribution ratios,
stability constants, and binding energies — to generative and agentic design, to
the process side that the user of a separation flowsheet cares about, and
finally to a section on failure modes that is deliberately as long as any of the
others.

## What the Models Are Trained On

### The Experimental Record

The models below are only as good as a body of careful extraction chemistry that
long predates them, and which is worth naming, because the same handful of
systematic structure-property studies appear as training data again and again.

@stamberga2020structure is the clearest example. Beyond the three
{index}`diglycolamide`s that dominate the literature — TODGA, TEHDGA and DMDODGA
— they designed and measured twelve new diglycolamides with varying substitution
patterns, specifically to separate the steric from the electronic contribution
to lanthanide(III) selectivity in hydrochloric acid, combining extraction
measurements with computation and solution-structure characterization. Their
conclusion is the one that makes the problem hard and the modeling worthwhile at
the same time: subtle changes around the diglycolamide carbonyl oxygens produce
dramatic shifts in both extraction strength and selectivity. The size of those
shifts is worth stating, because this book collects adjacent-pair numbers and
this paper reports them: the best of the twelve, an unsymmetrical
N,N-dimethyl-N′,N′-di(n-octyl) diglycolamide, gives **SF(Nd/Pr) = 3.2** against
2.5 for TODGA on the same pair, and another of them gives 2.2 for Eu/Sm, 1.9 for
Tb/Gd and 2.0 for Er/Ho. Their explanation is the one a first-coordination-sphere
descriptor set cannot represent either: the variation comes from electrostatic
interactions *beyond* the first coordination sphere, in how chloride counterions
pack between the coordinating ligands.

Three further studies in the same tradition define the shape of the design
space:

- @simonnet2021study measured all fourteen stable lanthanides against
  phenanthroline carboxamides, with EXAFS on the Nd and Dy complexes and
  supporting calculations. Tridentate monocarboxamides and tetradentate
  dicarboxamides give different trends across the series though both prefer the
  light lanthanides — and, more usefully for a model, amide substituents that
  never coordinate the metal still shift the distribution ratio, most probably
  through the internal polarity of the molecule. A descriptor set restricted to
  the first coordination sphere cannot represent that effect.
- @diazgomez2023synthesis made diglycolamides in syn- and anti-diastereomer
  pairs, differing within each pair only in the orientation of backbone
  substituents, and found the orientation moves extraction on its own: the
  anti-dipropyl isomers give higher distribution ratios for Pu(IV) than their
  syn-analogues, and anti-p-TODGA extracts Zr and Mo an order of magnitude
  better. Stereochemistry is exactly the information that a connectivity
  fingerprint discards. Read the paper carefully, though, and it also warns
  against overclaiming: the substitution itself matters more than its
  orientation — every substituted ligand extracts trivalents *worse* than the
  unsubstituted parent, on steric grounds — and all the diastereomers converge
  on the same inverse Am/Cm selectivity, a separation factor of about 1.5. No
  lanthanide-over-lanthanide separation factor is reported anywhere in the
  paper.
- @zhang2026design report a monopyridine amine extractant designed for selective
  heavy rare earth extraction, and @han2024efficient the HPOAc system for
  recovering rare earths from the sulfate leachate of ion-adsorption ore. These
  are conventional extractant-design papers, and they are the kind of result a
  successful generative model would have to produce. The first is worth pausing
  on for its numbers, which are among the best adjacent-pair figures anywhere in
  this book: **β(Tm/Er) = 4.18** for the meta-substituted isomer, with 4.04 and
  3.90 for the ortho and para variants, alongside β(Lu/La) of 1688 to 3736. The
  design rationale is covalency — the computed Wiberg bond index rises La < Eu <
  Lu, and extraction efficiency rises with it — which is a mechanistic handle a
  connectivity fingerprint would not find, and one that took DFT rather than a
  learned model to identify.

### Molecular Representation

Before a ligand can be an input it has to be a vector, and the choice of how is
not neutral. @wigh2022review divides the options into four classes — string
representations, connection tables, feature-based descriptors, and
computer-learned representations — and notes that discussion of computation time
and domain of applicability is routinely omitted from papers that introduce new
ones. That omission matters more here than in most fields, because the domain of
applicability is precisely the question when a model trained on TODGA analogues
is asked about a phenanthroline.

The feature-based route is what nearly all rare-earth work uses: RDKit
descriptors, extended-connectivity fingerprints, and hand-added process
variables. The learned route is the one that has transformed molecular property
prediction elsewhere. @ross2022large trained MoLFormer, a transformer encoder
with rotary positional embeddings and linear attention, on the SMILES strings of
1.1 billion unlabelled molecules from PubChem and ZINC, and showed that the
resulting embeddings outperform supervised and self-supervised graph neural
networks and language models across ten benchmark datasets, competing on two
more. Analysis of the attention maps indicates the model has learned spatial
relationships between atoms from strings alone.

Nothing of this kind has been trained on extraction data, for the obvious
reason: the pretraining corpus for MoLFormer is nine orders of magnitude larger
than any lanthanide extraction dataset. The realistic use is transfer — pretrain
on unlabelled chemistry, fine-tune on the few hundred measured distribution
ratios that exist — and it has not been reported for rare earth separations.
The infrastructure to do it is public: @wu2018moleculenet established the
benchmark suite and reference implementations that made molecular machine
learning comparable across papers, and @heid2023chemprop is the message-passing
neural network package that @zahariev2024prediction, below, builds on
directly.

(machine-learning-for-distribution-coefficient-prediction)=
## Predicting Distribution Ratios

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

An RMSE of 0.53 in log D is a factor of 3.4 in D. Against the ratio of two
distribution ratios for adjacent lanthanides — a separation factor of perhaps
1.5 to 3 for a good extractant — that error is larger than the quantity of
interest, and the model is useful only insofar as the error is correlated
between the two elements being compared. This is the same argument that recurs
below for binding energies, and it is the central methodological question of the
whole subject.

### QSPR Models

Quantitative structure-property relationships correlate molecular descriptors
with extraction properties, and remain useful where the dataset is too small for
a neural network. @muratov2020qsar is the review of the field's fifty-five years
of accumulated practice, and its main value here is the validation discipline it
codifies rather than any particular algorithm.

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

### Recent Extraction-Efficiency Models

Two 2026 papers address exactly the target this section is about, and both are
named here without numbers because their full texts were not accessible during
the preparation of this book. @zhang2026predicting report a data-driven machine
learning approach to predicting rare earth extraction efficiency with
organophosphorus ligands — the industrially dominant extractant class, and one
whose acidic members lie outside the neutral-ligand restriction that defines the
dataset above. @liu2026machine report machine-learning-assisted performance
prediction for rare-earth solvent extraction systems together with an analysis
of the governing factors. Both are recorded here as the current state of the
literature; neither is a source for any figure in this book, and readers who
need their numbers should go to the papers.

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
one. That distinction is developed further in
[](#explanations-are-statements-about-models).

## Predicting Binding

### Stability Constants from Compiled Experimental Data

The distribution ratio is a property of a whole biphasic system. The stability
constant is a property of the complex, and there is far more of it on record —
decades of potentiometry compiled into the NIST and IUPAC databases — which
makes it the natural target when the extraction data runs out.

@chaube2020applied trained six supervised algorithms — random forest,
k-nearest neighbours, support vector machines, kernel ridge regression,
multilayer perceptrons and AdaBoost — on **5,266** experimental log K₁ values
for lanthanide cations with structurally diverse ligands, validated in external
ten-fold cross-validation, and then ran a feature-importance analysis to
identify which molecular, metallic and solvent features carry the signal.
AdaBoost was the best of the six, at MAE 0.39 log units and R² 0.98 on the test
set. That 5,266 is the concrete size of the "decades of compiled potentiometry"
this chapter keeps contrasting against the ~1,200 distribution ratios. Their
framing of the motivation is the honest one: molecular modelling gives
structural insight but cannot predict stability constants accurately enough, or
cheaply enough, to screen a large chemical space.

@li2025prediction did the same for actinide-ligand complexes with fourteen
algorithms, found gradient boosting best, reduced 282 ligand, metal and solvent
descriptors to the fifteen most relevant, and reported R² of 0.98 on training and
0.93 on test data, with a compact symbolic correlation extracted afterwards by
SISSO. The training set is **454 experimental log K₁ values** — an order of
magnitude smaller than the lanthanide stability-constant compilation above, and
a reminder that the actinide side of this literature is data-poorer still. @kanahashi2022machine built Gaussian process regression models for both
the first and the higher overall stability constants across a wider range of
cations than earlier work, and found the electronegativities of metal and ligand
to be the most important features for the first constant.

The most directly useful of these for ligand design is @zahariev2024prediction,
because it closes a loop rather than reporting a correlation. Their LOGKPREDICT
program feeds Chemprop-predicted log K values to the HostDesigner
molecular-design software, so that candidate ligands are ranked by predicted
metal-ligand binding strength during design rather than after it. The reported
errors are worth quoting precisely, because the last of them is the one that
matters: RMSE 0.629 ± 0.044 (R² 0.960 ± 0.006) for the multi-metal model trained
on NIST data; RMSE 0.764 ± 0.073 and 0.757 ± 0.071 for two lanthanide-only
models trained on IUPAC data; and, for *relative* log K predictions on an
out-of-sample set of six ligands chosen to demonstrate metal ion selectivity,
RMSE 0.25. The absolute errors are three times the relative error on the
selectivity task. That is the cancellation argument made quantitative, and it is
the strongest published evidence that these models can be trusted for the
difference even where they cannot be trusted for the value.

(learned-binding-energies-as-a-dft-surrogate)=
### Learned Binding Energies as a DFT Surrogate

Where the deep-learning models above are trained on measured distribution
ratios, a second line of work learns the underlying binding energy directly and
so generalises beyond the conditions in the training set. @gupta2025accelerating
trained equivariant neural networks (Allegro) on 5,356 REE-ligand complexes,
reaching a mean absolute error of 6.1 kcal/mol on binding energy predicted
directly from structure. "Equivariant" here means the network's internal
representation rotates with the molecule instead of being invariant to rotation,
which is what lets it predict a directional, geometry-dependent quantity from
coordinates; @batzner2022equivariant introduced the architecture family and
showed that this symmetry constraint buys up to three orders of magnitude in
data efficiency, which is why it appears in a field with 5,356 training points
rather than millions. The point of that number is throughput: it bypasses the
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

There is a further trap underneath the model, which is that the structure the
network is given may not be the structure that matters.
@summers2024importance make the case that the configuration search — finding
the relevant conformers and coordination geometries rather than one plausible
one — is decisive for whether a calculated lanthanide selectivity is
predictive at all. A surrogate trained on single-conformer energies inherits
that error and cannot detect it.

### Learning the Mechanism Instead of the Number

A different use of the same data is to learn what is *happening* rather than
what the answer is. @lee2025data build kinetic reaction networks for the
liquid-liquid extraction of uranium by DEHiBA, and set two ways of fitting them
against each other: a purely data-driven model regularized by chemistry-agnostic
L1 regression, and a chemistry-informed model regularized by relative reaction
energies from quantum-mechanical calculation. The comparison is the result. The
data-driven models are unbiased, simple and accurate given enough data, and hard
to constrain or interpret; the chemistry-informed ones reach comparable accuracy
by ensemble averaging while remaining interpretable, and they recover
UO₂(NO₃)₂(DEHiBA)₂ as the dominant extracted species, which is what slope
analysis, thermodynamic modelling, EXAFS and crystal structures already say.

Two things make this relevant here even though the metal is an actinide. It is
the clearest demonstration in this literature that physics used as a
*regularizer* buys interpretability at no cost in accuracy — the standing answer
to the complaint in [](#explanations-are-statements-about-models) that feature
attributions are not mechanism. And it targets the quantity this chapter
otherwise has almost nothing to say about: rates and speciation along the way,
rather than the equilibrium number at the end.

(designing-molecules-rather-than-ranking-them)=
## Designing Molecules Rather Than Ranking Them

Everything above is a ranking model: it scores structures someone else proposed.
The more ambitious use is to have the model propose them.

### Active Learning

Active learning is the minimal version — choose the next calculation or
experiment where the model is most uncertain or the expected improvement is
largest, retrain, repeat. @laub2025ligand applied it to f-element ligand design,
combining electronic-structure calculation with molecular topology in an active
learning workflow for the in silico design of organic ligands for ²²⁷Ac capture
in solution. The target is actinium rather than a lanthanide, but the structure
of the problem — a large ligand space, an expensive evaluation, a selectivity
objective — is identical. @augustine2026coupling runs the strategy on
lanthanides and on a real platform, using multi-objective Bayesian optimization
over four process variables to reach a fourfold gain in separation factor;
[](#the-campaign-that-joins-screening-to-measurement) treats it, because what it
optimizes is conditions rather than molecules.

### Language Models and Agents

@zhang2026augmenting is the most complete demonstration to date of a generative
workflow aimed squarely at this problem. Their system, SAFE-MolGen, is a large
language model-based agent that uses curated extraction data to propose new
ligands and to rank them with a supervised model trained on experimental
datasets, so that realistic experimental conditions enter the ranking. Ligands
that a human approves are passed to a second automated pipeline that builds the
three-dimensional metal-ligand complexes and runs quantum-mechanical free-energy
calculations to assess selectivity directly. Applied to Am(III)/Eu(III)
separation, the workflow produced several new ligands predicted to be more
selective than the benchmark extractant CyMe₄BTBP.

Three things about that description deserve emphasis. It is *quasi*-autonomous
by the authors' own word, with a human approval step in the middle. The output
is a set of *predictions*, not measurements. And the target is an
actinide/lanthanide separation, which is a larger chemical difference than any
lanthanide/lanthanide pair — a workflow that succeeds on Am/Eu has not thereby
been shown to succeed on Nd/Pr. @yang2026machine take a related
coordination-chemistry-informed approach to the same Am/Eu discrimination
problem, and are explicit that the point is to work under data-scarce
conditions.

The general-purpose agents these build on are worth knowing about, because they
set the expectations. @bran2024augmenting built ChemCrow by giving GPT-4
eighteen expert-designed tools, and reported autonomous planning and execution
of the syntheses of an insect repellent and three organocatalysts, plus guided
discovery of a new chromophore. @boiko2023autonomous reported Coscientist, a
GPT-4-driven system that designed, planned and performed experiments across six
tasks including optimization of palladium-catalysed cross-couplings.
@ramos2025review reviews the field. None of this work touches rare earth
separations, and the gap between "optimized a cross-coupling" and "resolved a
0.24 kcal/mol selectivity difference" is the gap this chapter keeps returning
to.

## Beyond the Extractant

A separation problem is rarely only the extractant. Machine learning has been
applied across the rest of the flowsheet, generally with more data and lower
stakes per prediction.

**Leaching.** @ma2018neural is a clean early example: for the two-stage
hydrochloric-acid dry digestion and water leaching of eudialyte concentrate,
they took the acid-to-concentrate ratio, the water-to-concentrate ratio,
leaching temperature and leaching time as predictors and total REE extraction
efficiency as the response, compared multiple linear regression, stepwise
regression and an artificial neural network on a designed experiment, adopted
the network, and confirmed it against additional tests. @jorjani2008prediction
did the same for yttrium, lanthanum, cerium and neodymium leaching recovery from
apatite concentrate two decades ago — a reminder that neural networks in
hydrometallurgy are not new, and that what changed recently is data volume and
tooling rather than the idea. @saldana2022mineral reviews the application of
neural networks, support vector machines and Bayesian networks to leaching
generally.

**Adsorption.** @bashiri2024artificial modelled adsorbent efficiency for REE
recovery from contaminated water using RDKit-derived features, reporting R² of
0.928 on both training and test sets and identifying the molecular weight of the
first functional group as the dominant feature. The caution from the
explainability section applies in full: that is a statement about which column
the model leans on. Two further things are worth knowing before the R² is read
as performance. The dataset is 225 experimental points harvested from 60 papers
published between 2005 and 2023 — the compilation problem of the previous
section, in its usual size. And the target variable is adsorption capacity in
mg/g, so the model predicts how much an adsorbent takes up, not which rare earth
it prefers.

**Solvent choice.** @oshima2025machine is methodologically the most transferable
paper in this section even though it is about gold rather than rare earths. For
79 organic solvents extracting Au(III) from hydrochloric acid, Hansen solubility
parameters classified extractability against an 80 % threshold with 93.7 %
accuracy, and a support vector regression on 35 RDKit descriptors reached R² =
0.943 on test data. The diluent and modifier are the least-modelled variables in
rare earth extraction, and this is what a serious attempt on them looks like.
@edaugal2025solvent reviews machine learning and high-throughput screening for
separation-process solvents more broadly.

**Mineral processing.** @gomezflores2022critical is the critical review of
artificial intelligence in mineral concentration, and covers the
beneficiation stage that [](#from-ore-to-feed-solution) treats.

## Machine Learning in Process Design

Extractant design is where this literature concentrates, and it is not where
the leverage is. The process systems engineering community has been applying
these methods to plants for longer, with more data, and with a clearer sense of
what a learned model is for.

### The Process Systems Engineering View

Three surveys frame what is realistic. @daoutidis2024machine is a perspective
distilled from a working session, and its conclusion is that machine learning
can be transformational for process systems engineering but that the required
work is *domain-specific* method development in molecular and material design,
data analytics, optimization and control, rather than the application of
off-the-shelf models. @schweidtmann2021machine names six challenges — optimal
decision making, introducing and enforcing physics in learned models,
information and knowledge representation, heterogeneity of data, safety and
trust, and creativity — of which the second and fourth are the binding ones for
rare earths. @dobbelaere2021machine is the most useful for calibrating
expectations: machine learning's advantages over traditional process models are
flexibility, accuracy and execution speed, its principal weakness is
interpretability, and its clearest opportunity is in *time-limited*
applications — real-time optimization, planning, control — where a rigorous
model is too slow to run inside the loop. That framing puts surrogate modeling,
already discussed in [](#process-modeling-and-optimization), at the centre
rather than the periphery.

### Flowsheet Synthesis as a Learning Problem

The most striking work treats the flowsheet itself as the object being
generated.

@vogel2023learning represent flowsheets as strings in the SFILES 2.0 notation,
pretrain a transformer language model on synthetically generated flowsheet
topologies to learn the grammar, fine-tune on real topologies by transfer
learning, and then use causal language modelling to *autocomplete* a partial
flowsheet — the direct analogue of text autocompletion, offering an engineer
recommendations during interactive synthesis. The authors are candid that the
present state has limitations and that further steps are needed before the
method works in realistic synthesis scenarios.

@stops2022flowsheet take the reinforcement-learning route: processes are
represented as graphs, graph convolutional networks process the state, and an
actor-critic agent places unit operations as discrete decisions while choosing
their design variables as continuous ones. Their case study — equilibrium
reactions, azeotropic separation and recycles — is not a rare earth flowsheet,
but a countercurrent extraction cascade with scrub and strip sections and
internal recycles is structurally the same kind of object, and this is the
method that would generate one.

Neither has been applied to rare earth separations. The obstacle is not the
algorithm; it is that both require a fast, reliable evaluator for a candidate
flowsheet, and for rare earths that evaluator is a cascade model whose
equilibrium closure is itself uncertain ([](#thermodynamics-of-extraction)).

### Scheduling, Control, and Hybrid Models

@hubbs2020deep applied deep reinforcement learning to chemical production
scheduling under uncertainty and benchmarked it against mixed-integer linear
programming on a receding horizon, finding that the learned policy beat naive
MILP formulations and was competitive with a shrinking-horizon MILP on
profitability, inventory and customer service. The honest reading, which the
authors give, is that the promise is speed and flexibility for real-time
scheduling rather than better optima, and that integration with model-based
optimization is the direction, not replacement of it.

Two further threads matter for a field with little data and a great deal of
theory. @yang2020hybrid review hybrid models that combine data-driven and
knowledge-enabled components, and @karniadakis2021physics review
physics-informed learning, where the governing equations are imposed on the
model rather than hoped for. For rare earth separations, where mass balance,
charge balance and the three-proton stoichiometry of cation exchange are known
exactly and the equilibrium constants are not, this is the structurally correct
way to spend the small amount of data available.

### Bayesian Optimization

@wang2022bayesian is the review to read, and includes a self-contained primer
for chemical engineers. Its central empirical claim is the one that justifies
the method in this field: Bayesian optimization often requires an order of
magnitude fewer experiments than undirected search. That is exactly the regime a
rare earth extraction campaign is in, and it is what the platform in
[](#automated-high-throughput-platforms-for-f-element-separations) uses as its
control loop. The gap identified there remains: published campaigns optimize
process conditions for a fixed ligand rather than searching over molecules.

## Synthesis: Making What the Model Proposes

A generative model that proposes a ligand nobody can make has not helped. The
synthesis-prediction literature is mature enough to be part of the loop:
@coley2017prediction trained a model on 15,000 reaction records from granted US
patents to rank candidate products and anticipate reaction outcomes, putting the
true major product first in 71.8 % of cases and in the top five in 90.8 % —
useful for triaging a proposed route, not for trusting one unchecked;
@liu2017retrosynthetic treated retrosynthesis as sequence-to-sequence
translation on 50,000 patent reactions across ten reaction types and matched a
rule-based expert system; and @schwaller2021prediction addresses the piece that
receives least attention and matters most for scoring a route, which is
predicted yield.

On the hardware side, @burger2020mobile demonstrated a mobile robot operating
standard analytical instruments in an ordinary wet chemistry laboratory to
optimize a photocatalyst, and @abolhasani2023rise review self-driving
laboratories and give a roadmap for building one without being a specialist.
The rare earth instance of this is the agile diglycolamide synthesis platform in
[](#high-throughput-extractant-synthesis-and-screening), which is the step that
turns a predicted ligand into a measured one.

## Where This Breaks

### The Signal Is Smaller Than the Error

This has been said three times in this chapter with three different numbers —
0.53 in log D, 6.1 kcal/mol in binding energy, 0.63-0.76 in log K — against a
target of 0.24 kcal/mol. In every case the model is usable only if its error
cancels between the two elements being compared. That cancellation is an
empirical property of a particular model on a particular series, it is not
guaranteed by anything in the training procedure, and it is not reported in a
validation metric. @zahariev2024prediction is, at the time of writing, the
clearest published demonstration that the cancellation is real for at least one
class of model, with a relative error of 0.25 against absolute errors of
0.63-0.76.

The practical consequence for anyone building such a model: validate on
*differences*. Report the error on log β for adjacent pairs, not on log D or log
K for single elements, and hold out a whole ligand family rather than random
rows, because random splits leak information between structurally near-identical
molecules and inflate every metric in this chapter.

### The Data Are the Wrong Shape

@thebelt2022maximizing identify four data characteristics that make classical
machine learning difficult in chemical engineering, and rare earth separation
has three of them at once: high-variance, low-volume data; noisy, corrupt or
missing data; and data restricted by physics-based limitations. The concrete
version of the last point is that distribution ratios are published without the
ionic strength, phase ratio or equilibration time needed to reuse them, so any
compilation is assembled from individually incomplete records.

@estay2023challenges make the same argument from the mineral-processing side and
add the operational half of it: data scarcity, difficulty in characterizing
abnormal conditions, the absence of reliable in-line sensors, and the need for
continuous measurement of critical variables. A learned controller for a solvent
extraction circuit is limited by the last of these long before it is limited by
the algorithm — see [](#characterization-methods) for what on-line elemental
analysis of these streams currently requires.

@wang2020machine is the practical companion: a protocol paper on obtaining and
treating data, feature engineering, validation, and benchmarking for materials
work, written for people who are chemists first.

(explanations-are-statements-about-models)=
### Explanations Are Statements About Models

Feature attributions appear throughout this chapter — silica dominates leaching
[@nguyen2025explainable], electronegativity dominates the first stability
constant [@kanahashi2022machine], the first functional group's molecular weight
dominates adsorption [@bashiri2024artificial]. These are useful leads. They are
not mechanistic findings, and the distinction is not pedantic.

@zhong2022explainable set out what "explain" can mean in a materials context and
@esterhuizen2022interpretable do the same for catalysis, where the temptation to
read an attribution as a mechanism is strongest. The sharpest warning is
@slack2020fooling, who showed that the two most widely used post-hoc explanation
methods, LIME and SHAP, can be deliberately fooled: a scaffolding technique lets
an adversary hide a classifier's actual bias behind an arbitrary chosen
explanation while its predictions remain unchanged. Nobody in this field is
adversarial, but the demonstration establishes that the explanation and the
model's actual behaviour are separable, which is enough to require that any
attribution be tested by experiment before it is designed against.

### What Has Not Been Demonstrated

For clarity, and against the tone of much of the literature summarized above,
here is what is absent from the record:

- No model has been shown to predict an adjacent-pair separation factor to
  within its own experimental uncertainty across an unseen ligand family.
- No generative workflow has produced a lanthanide/lanthanide extractant that
  was then synthesised and measured to outperform the incumbent for that pair.
  @zhang2026augmenting comes closest on the generative side and stops at
  computational prediction, for an actinide/lanthanide pair.
- One campaign does run computational selection through to measurement on
  lanthanides: @augustine2026coupling screened, calculated and then measured a
  holdback agent, and optimized four process variables around it. The molecule
  was selected once at the start and never revised, the reagent chosen is an
  aqueous additive rather than an extractant, and the splits reported are
  {Eu, Dy, Ho} from Nd and Eu from {Dy, Ho} — the one adjacent pair in the set,
  Dy and Ho, is not separated.
- No published campaign closes the loop from automated measurement back into a
  molecular design model. The pieces exist separately
  ([](#high-throughput-and-computational-methods)); the connection does not.
- No learned model has been reported controlling an operating rare earth
  separation circuit.
- Nothing in this chapter has been demonstrated on a real leachate rather than a
  synthetic solution or a literature compilation.

@butler2018machine set out the general expectation for machine learning in
molecular and materials science; measured against it, rare earth separation is
an unusually hard instance of the problem and an unusually early one.

## Key Takeaways

1. **The target is 0.24 kcal/mol.** Every reported error in this chapter is
   larger than the free-energy difference that defines an adjacent-pair
   separation factor of 1.5. Models work only through error cancellation across
   the series.
2. **Validate on differences, not values.** The one paper that reports both
   [@zahariev2024prediction] finds a relative error three times smaller than its
   absolute error. That is the number that predicts screening performance, and
   almost nobody reports it.
3. **Three prediction targets, three data situations.** Distribution ratios have
   the most relevance and the least data (~1,200 points, neutral ligands only);
   stability constants have decades of compiled potentiometry; binding energies
   can be generated computationally without limit but inherit the errors of the
   configuration search that produced the structures.
4. **Representation choices discard the effects that matter.** Stereochemistry
   [@diazgomez2023synthesis] and non-coordinating substituent polarity
   [@simonnet2021study] both shift selectivity measurably, and both are invisible
   to a connectivity fingerprint.
5. **Generative design has reached quasi-autonomous computational screening, not
   validated discovery.** The strongest generative result [@zhang2026augmenting]
   is predicted selectivity for Am/Eu, human-approved mid-workflow, and
   unmeasured. The strongest *measured* result from a computationally guided
   campaign [@augustine2026coupling] is a fourfold gain in separation factor on
   four lanthanides — but from optimizing conditions around a molecule chosen
   once at the outset, and not on an adjacent pair.
6. **The process-design literature is further along than the extractant
   literature.** Flowsheet autocompletion and reinforcement-learning process
   synthesis both work on chemical processes generally; neither has been applied
   to a rare earth cascade, and the obstacle is the evaluator, not the learner.
7. **Feature attributions are hypotheses.** They say which input the model uses.
   Treating them as mechanism is the most common way this literature is
   over-read.
