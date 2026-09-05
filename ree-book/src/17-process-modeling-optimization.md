---
title: Process Modeling and Optimization
---

(process-modeling-and-optimization)=
# Process Modeling and Optimization

Everything up to here has been about a single contact: an ion, a ligand, a phase
boundary, a distribution ratio. A plant is a few hundred of those contacts wired
together, and the questions it raises are not the questions a single stage
raises. How many stages, split how, at what flow ratio? Where does the feed
enter? What happens to the purity at the far end when the feed grade moves by
ten percent, or when a pump is throttled, or when the operator raises the scrub
rate to fix a problem three stages away? Those questions have answers, and the
answers come from a model of the whole cascade rather than from any one stage in
it.

This chapter is about how those models are built, what software they are built
in, and how far they can be trusted. It runs from the closed-form cascade design
theory that made the modern industry possible, through the commercial flowsheet
simulators, to the open-source equation-oriented frameworks — Pyomo, IDAES,
PrOMMiS — where most of the current rare-earth process modeling work is
happening. It ends on the honest question, which is what an optimized flowsheet
on a screen actually predicts about a plant that has not been built.

The material this chapter needs from elsewhere in the book is the stage model
itself. [](#solvent-extraction-fundamentals) derives the {index}`Kremser`
equation and the McCabe-Thiele stage count from a constant distribution ratio,
and that is the object being scaled up here.
[](#thermodynamics-of-extraction) supplies the equilibrium constants those
models close on, and is candid about how uncertain they are. Nothing in this
chapter repairs that uncertainty; it propagates it.

## What a Process Model Is For

It is worth separating three uses, because they make different demands and
people routinely conflate them.

**Simulation** answers *what would this flowsheet do?* The flowsheet is fixed —
stage counts, flow ratios, feed location, reagent strengths — and the model
computes the streams. This is the easiest of the three and the only one most
commercial tools were built for. It requires no derivatives and tolerates a
model that is a black box internally.

**Parameter estimation** answers *what constants make this model reproduce my
data?* The data are fixed and the parameters float. This is a least-squares
problem wrapped around the simulation, and its answer is only meaningful with an
uncertainty attached to it.

**Optimization** answers *what flowsheet should I build, or how should I run the
one I have?* Here the design variables float and an objective — cost, recovery,
purity, solvent inventory, some weighted mixture — is driven to an extremum
subject to the model equations as constraints. This is the demanding case. It
wants derivatives, it wants the model to stay solvable at every point the solver
visits, and if any integer decisions are present (does this unit exist? is this
stream recycled?) it becomes a mixed-integer problem that a simulator cannot
formulate at all.

The distinction matters because the tool that is best at the first is usually
worst at the third, and the history of process modeling software is largely the
history of that tension.

## The Equilibrium-Stage Model and Its Closure

Nearly every solvent-extraction cascade model in the literature is built on the
same abstraction: the cascade is a chain of well-mixed stages, each stage reaches
equilibrium, and the phases leave it separated. For stage $i$ carrying aqueous
flow $A$ and organic flow $O$, the component balance for element $j$ is

$$
A\,x_{j,i+1} + O\,y_{j,i-1} = A\,x_{j,i} + O\,y_{j,i}
$$

with the equilibrium closure

$$
y_{j,i} = D_j\!\left(x_{1,i},\ldots,x_{n,i},\,\mathrm{pH}_i,\,[\mathrm{HL}]_i\right) x_{j,i}.
$$

The balance is bookkeeping and is never in doubt. Everything difficult sits in
the closure, and specifically in the fact that $D_j$ is written as a function of
the whole composition rather than as a constant. The Kremser derivation in
[](#countercurrent-cascade-design) assumes it *is* a constant, which is what
makes that derivation closed-form and also what makes it a bound rather than a
design. In a real cascade the extractant is a shared, finite resource: the
elements compete for it, so loading one of them depresses the others, and the
three protons each transferred ion releases move the pH, which by the slope-3
dependence moves every $D$ in the stage at once. A cascade model that does not
carry an acid balance alongside the metal balances will predict profiles that
cannot happen.

That single observation — that the acid balance is not optional — is what
separates a working cascade model from a textbook one, and it is the explicit
subject of the dynamic model discussed below.

## Cascade Theory: Design in Closed Form

The first apparatus for designing a rare-earth cascade rather than tuning one
was {index}`Xu Guangxian`'s countercurrent extraction theory, developed in China
from the 1970s [@xu1985theory]. Its move is to accept a strong simplification —
that the extraction ratio of the mixture stays constant along the cascade — and
to get, in exchange, closed-form expressions for the quantities a designer
needs: the number of extraction stages, the number of scrub stages, the feed
stage, and the flow ratios, from the separation factor, the feed composition and
the two purity specifications. [](#countercurrent-cascade-design) sets out what
that buys: a plant can be designed on paper and started at its design point
rather than converged on over months of operation.

### What "Optimum" Means in a Cascade

The word optimum carries a specific and non-obvious meaning in this literature,
and getting it wrong makes the results look inconsistent. It does not mean the
fewest stages, and it does not mean the least reagent. In @zhang2016cascade's
statement of the theory it means **the maximum daily production for a given total
mixer volume** — a capital-productivity objective, not a stage-count one.

The objective function follows from that. For a mixer-settler train with fixed
mixing and settling residence times, the capital tied up is set by the organic
and rare-earth inventory held in the cells, which scales as the solvent flow per
unit feed, `S_o`, times the number of cells. So the design indicator is the
product

$$
\Phi = S_o \,(n + m)
$$

and it has a minimum, because `S_o` and `n + m` move against each other: more
solvent per unit feed means a larger extraction factor and fewer stages to reach
the same purity. Plotting `Φ` against `S_o` gives a U, and the design is chosen
near its bottom.

**The U is very shallow, and that matters.** @zhang2016cascade tabulate the curve
for a three-component design case — separating Gd/Eu/Sm on an acidic extractant
with `β`(Gd/Eu) = 1.40 and `β`(Eu/Sm) = 2.00, from a feed of 0.39/0.10/0.51,
specified at 99.9% Gd₂O₃, 99.99% Sm₂O₃ at 99.9% recovery, and a europium
concentrate above 40%:

| `S_o` | Stages `I` | `n` | `m` | Total `n + m` | `Φ = S_o(n+m)` |
|---|---|---|---|---|---|
| 1.40 | 39 | 22 | 63 | 85 | 119 |
| 1.50 | 36 | 21 | 55 | 76 | **114** |
| 1.75 | 32 | 19 | 47 | 66 | 115 |
| 2.00 | 30 | 18 | 42 | 60 | 120 |
| 2.25 | 29 | 18 | 39 | 57 | 128 |
| 2.50 | 28 | 17 | 38 | 55 | 138 |

Read the two columns that matter against each other. Going from `S_o` = 1.40 to
2.50 cuts the train from 85 stages to 55 — a 35% reduction in installed cells,
which is the kind of change that reorganises a plant. Over that same range the
objective `Φ` moves from 119 down to 114 and back up to 138: the minimum is
**4% below** the value at the left-hand end. For any choice between about 1.5 and
2.0 the objective is flat to within 5%, which is well inside the uncertainty of
the stage-efficiency assumption underneath it. **The objective identifies a
region, not a point**, and the design decision inside that region is made on
grounds the objective does not represent.

The source's own behaviour bears this out: having tabulated the curve, it builds
its detailed process table at `S_o` = 2.00, where `Φ` = 120 — *worse* than the
114 at `S_o` = 1.50. The stated rule is to sit "slightly right side of the curve
bottom", and the justification given is asymmetry of risk rather than the value
of `Φ`: below the minimum solvent flow the stage count rises without bound, so
the left side of the U is a cliff and the right side is a ramp. That is a sound
argument, and it is worth naming as the thing it is — a robustness margin against
a hard constraint, not an optimum. It is the same instinct that puts a
distillation column at 1.2 to 1.5 times minimum reflux.

**A practitioners' rule with no data behind it.** The same source offers a
parameter `k` for backing a design off the thermodynamic extremum, defined
through the scrub flow as `W_a = 1/(β^k − 1)` with `0 < k < 1`; `k` = 1 recovers
the minimum-flow, infinite-stage limit, and lowering it trades reagent for
stages. The recommendation is that "normally the optimum k value is 0.70 based on
the process design of hundreds of systems", with 0.5 to 0.9 used in practice and
the final choice made on a full economic assessment. Two things should be said
about this. It is a useful number, and it comes from an authoritative source
close to the industrial practice. It is also presented with no dataset, no error
estimate and no external citation — the supporting evidence is the authors'
accumulated design experience, asserted rather than shown. The same is true of the
claim that the mixed-solute stage equations "have been approved correct in over
ten years of rare earth production and in hundreds of simulating experiments."
This book uses the rules and reports the basis they rest on, which is expert
practice rather than published validation.

### Three Outlets, and What the Middle Cut Is Worth

A two-outlet cascade yields one pure product and one mixture. The **three-outlet
process**, developed by Chunhua Yan and coworkers at Peking University, draws a
third stream from an intermediate stage so that a single cascade produces two
pure products *and* a concentrated middle fraction [@zhang2016cascade]. For a
feed whose valuable component sits in the middle of the series — europium or
terbium in a light/heavy split — this is worth a great deal, because the
alternative is to pass that component through two separate cascades.

What the middle outlet actually delivers is the part worth stating plainly. In
the Gd/Eu/Sm case above, the converged design meets its end specifications
handsomely: 99.99% Sm₂O₃ in the aqueous outlet and 99.91% Gd₂O₃ in the organic
outlet. The europium stream drawn from stage 30 comes out at **40.0%** Eu₂O₃,
against 10% in the feed — a fourfold concentration, and exactly the specification
that was asked for, but not a product. It is a feed for a further separation.
Gadolinium recovery in that design is **61.8%**, with the balance reporting to the
europium concentrate. The three-outlet process buys concentration of the middle
component at the cost of recovery of the component adjacent to it, and the
published case makes the size of that trade visible.

The complication that follows is a modelling one, and it is why this belongs in
this chapter rather than in [](#solvent-extraction-fundamentals): opening the
third outlet changes the concentration profile of *every* component, so the
two-outlet design equations no longer apply section by section without
re-deriving the concentrating factors around the draw stage. The source's own
verdict is that reaching the optimum "by only experience" is difficult — which is
a statement that the closed-form theory has been pushed to where it stops being
sufficient and a numerical model has to take over.

A later variant, **fuzzy linkage extraction**, attributed to Jiankang Hu and
coworkers, restructures the flowsheet instead: a coarse A/C split that does not
control where the middle component B reports, feeding two second-layer cascades
that finish B/C and A/B, with the strip liquor of the first layer serving
directly as the scrub of the second. The claimed advantage is that scrub and
strip solutions become the same stream, so reagent consumption falls. The
magnitude given — a reduction "to 30%" relative to conventional processes,
attributed to production practice — is both ambiguously worded in the source and
unsupported by data reachable from here, resting on a Chinese-language secondary
reference. The structural argument for the saving is clear; the number is not
one this book will repeat.

### Starting a Cascade That Takes Months to Converge

There is a dynamic problem hiding behind all of the steady-state design above,
and it is the most practical reason a plant needs a model rather than a design
calculation. A cascade with a low separation factor and a high purity target
takes a long time to reach steady state, because the approach to the design
profile is itself governed by the same near-unity stage ratio that makes the
separation hard. During that transient the plant is producing off-specification
material at full rate.

The industrial answer is **circulating solvent extraction**, and the standard
startup sequence is full circulation → partial circulation → normal fractional
operation [@zhang2016cascade]. Full circulation runs the train with no feed and
no discharge: `S_o` = `W_a`, both extraction factors equal 1, and both reflux
ratios are infinite. The cascade is, in effect, run at total reflux to build the
composition profile before any product is drawn — the direct analogue of bringing
a distillation column up on total reflux. Partial circulation then admits feed
with discharge from one end only, and normal operation follows.

This is worth noticing for what it says about the modelling problem. The design
theory answers a steady-state question, but the quantity that decides whether a
separation plant is economic over its first quarter of operation is a transient
one, and no closed-form result addresses it. That is the gap the dynamic models
below are written to fill.

The theory has a second life that is less often described in English-language
reviews, and it is the one relevant to this chapter. Closed-form design was the
starting point, not the end: the same framework was carried into simulation and
then into automated control. A 2020 review by Xu's successors at Peking
University describes the trajectory of the last two decades as running toward
higher product purity, process coupling, and, specifically, "automatically
controlled production based on a special simulation expert system for flow-sheet
optimization design" [@wu2020trends]. The design theory became a plant model,
and the plant model became a controller.

### From Closed-Form Design to Automated Control

That controller line is a substantial literature in its own right, largely from
Chinese control-engineering groups and largely published in control rather than
separations venues, which is one reason it is easy to miss. The binding problem
is that the quantity you want to control — the component content at a given
point in the cascade — is not something an online instrument measures. So the
work splits in two: soft sensors that infer component content from measurable
variables, and controllers that act on the inferred value.

On the control side, @yang2016multiple report multiple-model predictive control
of component content for a CePr/Nd countercurrent extraction process, and
@yang2015component treat the related problem of controlling the *distribution
profile* of component content along the cascade rather than an endpoint alone.
The profile formulation is the more interesting one for a designer, because the
concentration profile across the stages is the state that the cascade design
theory actually predicts, and controlling it is what keeps a running plant on
the design the theory produced.

This book's other treatment of process control,
[](#process-control-and-automation), is written from the instrumentation side —
pH, flow, temperature, interface level — and should be read together with this
one. The instruments are the actuators; the cascade model is what tells them
where to go.

## Dynamic and Rate-Based Models

A steady-state model tells you where a cascade settles. It says nothing about
how it gets there, how long that takes, or what a disturbance does on the way —
and for a train of a hundred mixer-settlers with substantial holdup, "how long"
can be days.

The clearest published example on rare earths is the dynamic model of @lyon2017dynamic,
built at Idaho National Laboratory. It couples a stage-wise REE equilibrium
model to *dynamic acid balances* — the point made above — in MATLAB/Simulink,
and predicts extraction, scrubbing and stripping across a full cascade using
laboratory equilibrium data as its only input. The authors used it to design a
flowsheet producing high-purity neodymium from a 25 wt % Pr / 75 wt % Nd feed
with PC88A, and then validated it against laboratory mixer-settlers.

The M.S. thesis behind that paper [@lyon2016separation] carries the experimental
half in more detail. Mixer-settler testing of the same PC88A chemistry showed
that better than 99 % neodymium purity required a neodymium scrub solution and a
twelve-stage scrubbing circuit, and the flowsheet was designed to produce
didymium and high-purity neodymium simultaneously rather than one at the expense
of the other. Twelve stages for scrubbing alone, on what is effectively a
two-component feed, is a useful number to hold against the Fenske bound in
[](#countercurrent-cascade-design).

What makes the paper useful here is its account of where the agreement stops.
Steady-state concentration profiles across the cascade were predicted
accurately. Transient predictions deviated more, and the authors attribute the
deviation to the assumption that each stage is homogeneous and well-mixed; they
revised the model to carry stage-dependent mixer-settler holdup volumes for
later validation. The stated standing limitation is that every stage is assumed
to reach complete equilibrium.

That limitation is the boundary of the equilibrium-stage abstraction, and it is
worth naming what lies past it. A real mixer-settler is a piece of
hydrodynamic equipment: drop size distribution, dispersion band depth, mixing
intensity, phase continuity and settler residence time all decide whether the
contact time is long enough for equilibrium to be approached at all
[@qi2018equipment]. Where it is not, the honest model is a *rate-based* one, in
which interfacial mass transfer is written explicitly with a transfer
coefficient and an interfacial area rather than assumed instantaneous. Rate-based
models are standard practice in distillation and absorption; in rare-earth
solvent extraction they remain rare, in part because the interfacial kinetics of
organophosphorus extractants are themselves not well characterised. Stage
efficiency — an empirical fraction applied to the equilibrium step — is what
almost everyone uses instead, and it is a fitted number, not a predicted one.

## Commercial Flowsheet Simulators

The tools most process engineers reach for first are the commercial simulators.
The landscape is short:

| Tool | Kind | Where it fits |
|---|---|---|
| Aspen Plus | Sequential-modular flowsheet simulator | Whole-plant balances, utilities, costing |
| Aspen Custom Modeler | Equation-based custom unit models | Writing the extraction unit Aspen does not ship |
| gPROMS | Equation-oriented, dynamic | Dynamic and rate-based models, parameter estimation |
| OLI | Electrolyte thermodynamics engine | Aqueous speciation at high ionic strength |
| DWSIM | Open-source simulator | Teaching, and work without a licence |
| MATLAB/Simulink | General numerical environment | Custom cascade models, as in most REE papers |

### Sequential-Modular and Equation-Oriented

The division that matters is not between vendors but between two ways of solving
a flowsheet. A **sequential-modular** simulator treats each unit as a subroutine
that maps inlet streams to outlet streams, and converges the flowsheet by
iterating around recycle loops. This is robust, it mirrors how engineers think,
and it is why Aspen Plus is built that way. Its weakness is optimization: the
derivatives an optimizer needs have to be recovered by perturbing the whole
converged flowsheet, which is expensive and noisy, and a recycle loop that fails
to converge at some trial point simply returns nothing.

An **equation-oriented** simulator instead assembles every unit's equations into
one large algebraic system and hands the whole thing to a solver. Convergence and
optimization become the same operation, exact derivatives are available, and
design specifications are just more equations. The cost is that the assembled
system is large, ill-scaled and unforgiving of a poor initial guess.

This tension is old and was analysed carefully before either camp had won:
@kisala1987sequential — with Boston, Britt and Evans, who built the simulator
that became Aspen Plus — compared sequential-modular against simultaneous-modular
strategies for flowsheet optimization in 1987. The modern equation-oriented
frameworks in the next section are the other branch of that argument, and the
reason they matter for rare earths is that rare-earth flowsheet questions are
optimization questions almost by definition: nobody wants to know what a
particular 87-stage arrangement does, they want to know which arrangement to
build.

### What the Simulators Do Not Supply

There is no Aspen Plus rare-earth solvent-extraction unit operation. There is no
validated activity-coefficient model for a concentrated chloride or nitrate
rare-earth liquor in contact with a saponified organophosphorus extractant.
These are not oversights; they are the state of the art. What the simulators
supply is the flowsheet infrastructure — stream bookkeeping, utilities, cost
estimation, convergence — and the modeler supplies the extraction physics.

The established pattern is therefore to write the extraction unit yourself and
embed it. @evans2014modelling did this for cobalt in Aspen Custom Modeler, which
exists precisely so that a custom equation-based unit model can be compiled and
dropped into an Aspen Plus flowsheet alongside the standard blocks.
@chen2018flowsheet did the corresponding whole-flowsheet exercise for
cobalt-nickel separation with a phosphonium ionic liquid. Neither is a rare-earth
paper, and both are cited here for their method rather than their chemistry:
cobalt-nickel is the closest well-worked analogue, and the rare-earth versions of
these flowsheets are mostly built in MATLAB instead — which is a statement about
where the effort has gone, not about what is possible.

## Equation-Oriented Open Source: Pyomo, IDAES, PrOMMiS

The most active line of rare-earth process modeling work today is in an
open-source stack developed under U.S. Department of Energy programs. It is
worth understanding as three layers, because they are frequently named
interchangeably and are not the same thing.

### Pyomo and the Solver Underneath

**Pyomo** is an algebraic modeling language embedded in Python
[@hart2011pyomo]. It is the bottom layer: it lets you declare variables,
constraints and objectives as Python objects, and it hands the resulting
model — with exact derivatives, obtained symbolically — to a solver. It is not
a process simulator and knows nothing about chemistry.

The solver most often underneath is **IPOPT**, an interior-point method with a
filter line search for large-scale nonlinear programs [@wachter2006implementation].
The reason this pairing matters for process work rather than being an
implementation detail is that it is what makes optimization of a full flowsheet
tractable at all: an interior-point method with exact second-order information
scales to the hundreds of thousands of variables a rate-based cascade with
detailed thermodynamics generates, where a derivative-free search over a
sequential-modular simulator does not. @biegler2010nonlinear is the standard
treatment of that argument and of the algorithms behind it.

### IDAES

**IDAES** — the Institute for the Design of Advanced Energy Systems Integrated
Platform — is the process-modeling layer built on Pyomo
[@lee2021idaes; @miller2018next]. Its stated aim is to combine what process
simulators are good at (libraries of unit and property models) with what
algebraic modeling languages are good at (advanced solvers), and what it
provides is an open, extensible library of dynamic unit-operation and
thermophysical property models, together with support for superstructure-based
conceptual design and optimization under uncertainty [@lee2021idaes]. The
framework's own summary of its position against the commercial tools is
unusually direct, and is the title of a book chapter by its authors: *Don't
search — solve!* [@biegler2022dont]. The argument is the one in the previous
section: if the model is written as equations rather than as a subroutine, the
design problem stops being a search over simulations and becomes a single
optimization.

### PrOMMiS

**PrOMMiS** — Process Optimization and Modeling for Minerals Sustainability — is
the critical-minerals application layer, begun in 2023, that extends IDAES to
mineral processing and rare-earth flowsheets [@prommis2025software;
@tarka2025advances]. It is a DOE multi-laboratory effort — NETL, LBNL, Sandia,
with university partners — and it is the first open-source modeling platform
aimed specifically at critical-mineral and rare-earth production pathways. What
it adds on top of IDAES is domain content rather than machinery: unit models for
the operations that appear in a hydrometallurgical flowsheet, thermophysical
property packages for the relevant liquors, and capital-cost libraries so that a
flowsheet optimization can carry an economic objective rather than a technical
proxy.

PrOMMiS is young, and this book takes no position on how well its unit models
reproduce plant behaviour, because that comparison has not been published. What
can be said is that it is open, that its source and documentation are public,
and that it is the first serious attempt to give rare-earth process design the
kind of shared modeling substrate that carbon capture and desalination already
have.

## Applied to Rare Earths

The papers below are the ones where these methods have actually been carried
through on a rare-earth problem. There are not many of them, which is itself
worth noticing.

### Multi-Stage Solvent Extraction Design

@srivastava2023design, from Honaker's group, is the most complete published
example of designing a rare-earth solvent-extraction train by model rather than
by trial. Working from bench-scale data on a 10 g/L rare-earth salt mixture with
DEHPA plus TBP as phase modifier and hydrochloric acid as strippant, they fitted
extraction and stripping equilibrium models, programmed them as function blocks
in a MATLAB/Simulink representation of a full SX train, and then ran a particle
swarm optimization over stage combinations with recovery and purity as the
objective criteria.

The results are worth stating precisely, because they show both what the method
delivers and where the chemistry still wins. The optimization identified stage
combinations of 8-12-3 and 10-3-5 (loading, scrubbing, stripping) achieving
99.52 % purity for yttrium and 85.41 % for lanthanum. It also reported that
neodymium, praseodymium and cerium remained difficult to separate. That last
finding is the honest one: an optimizer cannot manufacture a separation factor,
and where β is near unity the optimal design is still a bad design. The
stage counts, meanwhile, are a useful reality check against the Fenske bound in
[](#countercurrent-cascade-design) — twenty-three stages for one clean split of a
mixture, and this is a single train among the several a full fan-out needs.

The dissertation behind that paper [@srivastava2021modeling] is the fuller
account and states the design problem the paper then solves. Its argument is
that McCabe-Thiele construction, which works on a binary, becomes impractical on
a rare-earth feed precisely because so many components extract alike that there
is no single distributing pair to draw against — and that what has to replace it
is a modular process model assembled from separately fitted loading, scrubbing
and stripping blocks. The experimental base is the same DEHPA-plus-TBP system,
measured over a range of equilibrium pH values and phase ratios on a
seven-component solution of yttrium, gadolinium, samarium, praseodymium,
neodymium, cerium and lanthanum whose composition was taken from a rare earth
oxide product made from a coal-based source. That feed is what connects this
work to the section below.

### Integrated Flowsheets from Coal Refuse

@honaker2018conception assembled an integrated flowsheet for recovering rare
earths from coal coarse refuse, combining physical separation, pyrite
bio-oxidation, heap leaching, selective precipitation and solvent extraction,
with each block grounded in laboratory data on characterised plant samples. This
is flowsheet synthesis in the older and still dominant sense — engineering
judgment assembling unit operations that have each been demonstrated — rather
than mathematical optimization over a superstructure. It is included here as the
baseline the optimization work is trying to improve on, and because the
feedstock it addresses is the one
[](#recycling-and-urban-mining) and [](#the-industrial-landscape) treat as the
most credible non-Chinese source of heavy rare earths.

What that ambition costs to test is recorded in the final technical report of
the Minerals Refining and Rare Earth Consortium [@keim2019production]. The DOE
award, under the 2016 solicitation *Production of Rare Earth Elements from
Domestic U.S. Coal and Coal By-Products*, was to design and build a
demonstration plant yielding at least three individual rare earths at 90-99 %
purity and more than ten pounds a day of composite product as oxides, alongside
premium solid fuels and magnetite to carry the economics. Over the project the
feedstock moved from a Lower Kittanning coal in West Virginia to Fire Clay seam
rejects in Kentucky, and the report states plainly that none of the efforts
produced an economically viable venture: the principals elected not to move to a
pilot plant and did not request funding for one. It is the counterweight to
every flowsheet in this chapter that ends at a converged solution. The model can
close and the project can still not be worth building, and the reason is almost
never the solvent-extraction train.

### Surrogate Models for the Leach

A rare-earth flowsheet model is usually not limited by the solvent-extraction
train but by the leach ahead of it, which involves solid dissolution, complex
solution chemistry and kinetics that no compact algebraic model captures well.
Embedding a detailed leach model inside a flowsheet optimization is often simply
not solvable.

The standard response is a **surrogate**: fit a compact algebraic model to the
input-output behaviour of the expensive one, and optimize over the surrogate.
@fardis2025surrogate did this systematically for the leaching process in a
rare-earth recovery plant, testing which surrogate forms are easiest to build
and most accurate, and noting that no systematic study of the question existed
for this application. The authorship — Georgia Tech and NETL, with IDAES
developers — places it squarely in the stack described above.

Surrogates are a real technique with a real hazard, and it is the same hazard
as everywhere else in this book: a surrogate is only valid where it was fitted,
and an optimizer's entire job is to travel to the edge of the feasible region.
A surrogate-based optimum sitting outside the training envelope is not a design;
it is an extrapolation.

Surrogates are the point at which machine learning enters process design in
earnest, and the wider case — learned flowsheet synthesis, learned scheduling,
physics-informed models — is
[](#machine-learning-in-rare-earth-separations).

### Superstructure Optimization of Recycling Routes

The clearest example of optimization used as *design* rather than as tuning is
the work of Torres's group at Carnegie Mellon with PrOMMiS collaborators.
@laliwala2024design formulated the recovery of rare earths from end-of-life hard
disk drives as a superstructure — a network containing every candidate
processing route as an option — and maximized net present value over fifteen
years to select the pathway, with projected oxide prices and projected U.S.
end-of-life HDD volumes as inputs, followed by a sensitivity analysis over the
economic parameters.

@laliwala2026design extends this to end-of-life permanent magnets generally,
across four processing stages — disassembly, demagnetization, leaching and
extraction, and precipitation and calcination — under both net-present-value
maximization and cost-of-recovery minimization, and introduces a bottom-up
costing framework for hydrogen decrepitation. Its conclusion is a negative
result stated plainly: hard disk drive recycling was **unprofitable**, limited
by feedstock availability, while magnets from electric and hybrid vehicles were
profitable across a range of parameters and cost estimates.

That is what this class of model is for. The answer is not a better flowsheet
for HDDs; it is that the HDD stream is the wrong stream, and no amount of
process improvement fixes a feedstock that is not there. A single-flowsheet
simulation cannot produce that conclusion, because it can only evaluate the
flowsheet it is given. The related methodological work on writing precipitation
and dissolution equilibria in a form an optimizer can handle
[@laliwala2025optimization] is the sort of unglamorous groundwork that has to
exist before such models close at all.

## Parameters, Uncertainty, and the Experiments That Fix Them

Every model in this chapter contains fitted constants: extraction equilibrium
constants, stage efficiencies, kinetic parameters, cost coefficients. The model's
predictions are no better than those, and reporting a flowsheet optimum without
an uncertainty on it overstates what was computed.

The open-source stack has tooling for both halves of this. **parmest** performs
parameter estimation on Pyomo models with confidence regions rather than point
estimates [@klise2019parmest]. **Pyomo.DoE** goes one step further and designs
the experiment: given the model and the current parameter estimates, it computes
which measurements would most reduce the uncertainty, using the Fisher
information matrix as the criterion [@wang2022pyomodoe].

The second of these deserves emphasis because of what
[](#research-directions-and-open-questions) identifies as a gap — that
model-based design of experiments is barely used in this field despite fitting
it unusually well. Rare-earth extraction equilibria are exactly the case the
method was built for: experiments are slow and expensive, the parameter space is
continuous, and a mechanistic model already exists. The connection to
[](#high-throughput-and-computational-methods) is direct: that chapter's
{index}`Bayesian optimization` loop optimizes the *process*, while model-based
DoE optimizes the *experiment* that fixes the process model's parameters. They
are complementary and are rarely run together.

## What Optimization Buys, and What It Does Not

Three cautions, in descending order of how often they are ignored.

**The objective is almost always singular, and the problem is not.** Selectivity,
recovery, capital cost, solvent inventory, reagent consumption and environmental
burden trade against one another, and a design that optimizes any one of them
alone is not a design anyone would build.
[](#research-directions-and-open-questions) names this as an open gap, and the
observation holds here: the superstructure papers above optimize net present
value or cost of recovery, which is a defensible single scalar, but it prices
environmental burden only insofar as a regulation has already priced it. A
Pareto surface over cost and burden would be a different and more informative
object, and this book found no published example of one for a rare-earth
separation flowsheet.

**A model validated at steady state is not validated in transients.** This is
the explicit finding of @lyon2017dynamic and it generalises. Cascades are
validated, when they are validated at all, against steady-state profiles,
because those are what a laboratory train can be held at long enough to sample.
Start-up, shutdown, feed excursions and the multi-day settling of a hundred-stage
train after a disturbance are where a plant actually loses product, and they are
the least tested part of any of these models.

**Almost none of this has been checked against an operating plant.** The
validations in the rare-earth literature are against laboratory mixer-settlers
and bench-scale campaigns. The plants that would provide the comparison are
overwhelmingly in China and do not publish their operating data, and the
non-Chinese separators described in [](#the-industrial-landscape) publish
capacities rather than profiles. The gap between "this flowsheet optimum is
correct given the model" and "this flowsheet will work" is therefore not
currently measurable from the open literature, and any claim in this chapter
should be read with that in mind.

## Key Takeaways

1. **The equilibrium-stage model is the workhorse, and its acid balance is not
   optional.** Each extracted REE³⁺ releases three protons; a cascade model that
   omits that coupling predicts profiles that cannot occur.
2. **Cascade theory made design closed-form, and then became control.** Xu
   Guangxian's theory gives stage counts and flow ratios directly from β and the
   purity specifications; its descendants are simulation expert systems and
   predictive controllers for running plants.
3. **Commercial simulators supply the flowsheet, not the extraction.** There is
   no built-in rare-earth SX unit operation and no validated activity model for
   these liquors; the practice is to write the unit model — in Aspen Custom
   Modeler, gPROMS or MATLAB — and embed it.
4. **Equation-oriented frameworks turn design into optimization.** Pyomo, IPOPT,
   IDAES and PrOMMiS make the flowsheet a single algebraic system with exact
   derivatives, which is what allows superstructure and mixed-integer design
   questions to be posed at all.
5. **Optimization answers questions simulation cannot.** The strongest published
   result in this area is a negative one — that end-of-life hard disk drives are
   an unprofitable feedstock while vehicle magnets are not — and no
   single-flowsheet simulation could have produced it.
6. **An optimizer cannot manufacture a separation factor.** Where β is near
   unity the optimal design remains a poor one, as the Nd/Pr/Ce result in the
   most careful published cascade optimization shows.
7. **The validation gap is the real limitation.** These models are checked
   against bench-scale trains at steady state. They are not checked against
   operating plants, and in transients they are known to be weakest.
