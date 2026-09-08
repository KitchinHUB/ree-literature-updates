---
title: Kinetics and Mass Transfer
---

(kinetics-and-mass-transfer)=
# Kinetics and Mass Transfer

Almost everything in this book so far has been an equilibrium argument.
[](#why-rare-earths-are-hard-to-separate) sets the premise — adjacent
lanthanides differ by about one percent in ionic radius, the per-stage
separation factor sits near 1.5, and so you need a great many stages.
[](#solvent-extraction-fundamentals) builds the cascade that pays that bill,
[](#thermodynamics-of-extraction) works the free energies underneath it, and the
comparison table in [](#technology-comparison) is keyed on β — an equilibrium
quantity — for every technology in the book.

There is a question that framing never asks. Two lanthanides that share an
equilibrium need not approach it at the same speed. If the *ratio of rates* were
larger than the ratio of equilibrium constants, a separation could be built on
the difference by stopping the contact early, and the hundred-stage cascade
would be answering a question that did not have to be asked in that form.

Schelter and co-workers put the gap in the literature bluntly in 2017: all
deployed rare earth separation methods rely on thermodynamic properties such as
distribution equilibria, and separations based on kinetic differences "have not
been examined" [@fang2017electrokinetic]. That was an accurate description of
the field, and it remains close to accurate. What has appeared since is a
handful of demonstrations rather than a body of work.

This chapter covers rate in both of its roles, in the order a reader needs them.
First rate as an **engineering constraint** — what is slow, what sets contact
time, why a settler is the size it is. That material is missing from this book
and belongs somewhere: [](#solvent-extraction-fundamentals) raises the question
of phase disengagement and drops it, and no chapter explains what determines how
long two phases must be held together. Then rate as a **separation principle** —
the smaller and more interesting literature, and the one that has to be reported
carefully, because the demonstrations are real, few, and not yet on the pairs
that matter.

A note on what this chapter is doing structurally. Kinetic arguments are already
scattered through the book in four places that do not reference each other:
the shrinking-core treatment in [](#leaching-kinetics-models), the kinetic Pr/Nd
work in [](#coacervates-and-aqueous-biphasic-systems), the interfacial rate
constants in [](#microfluidic-separations), and the polymorph-selection
discussion in [](#selective-crystallization-by-molecular-design). This chapter
does not restate them. It gives them a common footing and points at each.

## Rate Regimes: What Is Actually Slow

An extraction that takes thirty seconds is not slow for one reason. Getting a
rare earth ion from the bulk aqueous phase into the bulk organic phase is a
sequence of steps in series, and the observed rate is set by whichever is
slowest:

1. **Bulk transport** of the ion to the neighbourhood of the interface, by
   convection, which is what agitation buys.
2. **Diffusion through the aqueous film** at the interface, where convection
   dies out and transport reverts to molecular diffusion.
3. **Interfacial chemical reaction** — the actual complexation event in which
   the extractant strips the ion of coordinated water and takes it up.
4. **Diffusion of the loaded complex through the organic film** and away into
   the bulk organic phase.

Which step controls is not a bookkeeping detail. It decides what to change.
Film-diffusion control responds to agitation and to interfacial area, and to
almost nothing else; interfacial-reaction control responds to temperature,
extractant concentration and pH, and barely responds to stirring at all. Turning
up the agitator on a reaction-controlled system spends power and buys nothing
but a harder-to-break dispersion. This is the same series-resistance logic that
[](#leaching-kinetics-models) applies to a dissolving mineral particle, where
the three candidate steps are film diffusion, surface reaction and product-layer
diffusion; the diagnosis there is the same in spirit, and it is empirical.

The honest position on rare earth systems is that mixed control is the common
finding rather than the exception. Kubota and co-workers measured extraction of
rare earths by {index}`PC88A` (2-ethylhexyl phosphonic acid mono-2-ethylhexyl
ester) in *n*-heptane using a microporous hydrophobic hollow-fibre extractor,
which fixes the interfacial area instead of leaving it to be inferred, and
concluded that the permeation rate is controlled *both* by diffusion of the
chemical species in the aqueous and organic phases *and* by interfacial chemical
reaction — they fitted a diffusion model with an interfacial reaction term and
the velocity distributions on either side of the fibre [@kubota1995extraction].
Geist, Nitsch and Kim measured the kinetics of rare earth extraction into
{index}`D2EHPA` [@geist1999kinetics]; the numbers in that paper have not been
read in full here and are therefore not quoted.

### The Measurement Problem

There is a reason this literature is thin, and it is methodological. To extract
a rate constant from a two-phase experiment you need to know the interfacial
area and to be sure that mixing is not the thing you are measuring. A stirred
cell gives you a known area and poor mixing; a shaken flask gives you good
mixing and an unknown, time-varying area. Bulk kinetic methods generally cannot
deliver both at once, which is why much of the older kinetic literature reports
apparent rate constants that are properties of the apparatus as much as of the
chemistry.

The microfluidic answer to this is described in
[](#microfluidic-separations): @nichols2011mechanistic used a plug-based device
with rapid mixing and a known interfacial area to determine absolute interfacial
mass transfer rate constants for every lanthanide except promethium, plus
yttrium, under TALSPEAK conditions. That is the reference measurement of its
kind in this field, and its existence is the strongest argument for microfluidics
as an instrument rather than as a process.

## What Sets Contact Time

[](#solvent-extraction-fundamentals) lists among the diluent's jobs that it
"must separate quickly," and explains that settler volume — the largest
contributor to solvent inventory in a mixer-settler train — is set by how long
the dispersion takes to break. That is the *disengagement* half of the problem.
The *contacting* half is the one this section covers, and the two pull in
opposite directions.

Mass transfer between two liquid phases scales with the interfacial area per
unit volume. Make the dispersion finer and the extraction goes faster; make the
dispersion finer and it takes longer to break. A mixer-settler is the industrial
resolution of that trade, and it resolves it by brute force: mix hard enough to
approach equilibrium in the mixer, then buy back the separation with a settler
several times the mixer's volume. The settler is large because it is undoing
what the mixer did.

Every alternative contactor in [](#solvent-extraction-fundamentals) is an
attempt to escape that trade rather than to pay it. Centrifugal contactors
replace gravity with a much larger acceleration, so a fine dispersion can be
broken quickly and the holdup collapses. Membrane contactors take a different
route: they hold the interface *in place* in the pores of a microporous
membrane, so the interfacial area is set by the module geometry and is known,
and disengagement is not an operation at all because the phases never disperse.
The standard reference on that family is the review of @gabelman1999hollow, and
the same principle is what makes the hollow-fibre extractor usable as a kinetic
instrument in the work cited above. The price is a membrane: pressure balance
between the phases has to be maintained to keep the interface pinned, the
membrane adds a diffusional resistance of its own, and anything that fouls a
small passage is now a process problem.

Microfluidic devices make residence time an independent variable rather than a
consequence of vessel size — flow rate and channel length set contact time
directly, to sub-second resolution, which is the argument
[](#microfluidic-separations) is built on. That is the one architecture in this
book in which "stop the extraction before equilibrium" is a setting rather than
an accident.

## The Interface Itself

The interfacial-reaction step above was written as though it were a single
event. It is not, and what actually happens at a liquid-liquid interface during
extraction was until recently largely unobserved.

@liang2019nanoscale used X-ray surface scattering with a thermal switch for
solvent extraction, supported by molecular dynamics, to look at the interface
directly. For the trivalent rare earths Y(III) and Er(III) with bis(hexadecyl)
phosphoric acid, they find that the ions and extractants form **inverted bilayer
structures** at the interface, which appear to be condensed phases of small
ion-extractant complexes. Those structures are an intermediate state: the moment
at which an ion has crossed the aqueous-organic boundary but has not yet
dispersed into the organic phase. Divalent Sr(II) behaves differently — its
ion-extractant complex is left exposed to the water phase, implying a second,
unobserved transport step, which their calculations suggest could be the budding
of reverse micelles.

The relevance here is that an intermediate state with its own structure is a
place where a rate can be selective. The authors themselves put it as a
suggested connection between the observed interfacial structures and the
extraction mechanism, which ultimately affects selectivity and kinetics
[@liang2019nanoscale]. That is a mechanistic hypothesis about where kinetic
selectivity could originate, not a demonstration that it does. It is worth
knowing precisely because the rest of this chapter is about systems where a rate
difference is observed and its origin is not known.

## TALSPEAK: When Kinetics Decides Whether a Process Exists

The clearest evidence that kinetics is not a second-order concern in f-element
separations is a process whose adoption it prevented.

{index}`TALSPEAK` — Trivalent Actinide Lanthanide Separation with
Phosphorus-Reagent Extraction from Aqueous Komplexes — separates trivalent
actinides from lanthanides by extracting the lanthanides into an acidic
organophosphorus extractant while an aminopolycarboxylate holdback reagent
retains the actinides in the aqueous phase. It works. Under ideal conditions
conventional TALSPEAK separates Am³⁺ from Nd³⁺, the usual limiting pair, with a
single-stage separation factor of about 100, and both lighter and heavier
lanthanides separate from Am³⁺ more completely than that
[@nash2015chemistry]. Set against the β ≈ 1.5 of an adjacent lanthanide pair,
that is an enormous number.

It has nonetheless not been adopted enthusiastically at process scale, and
Nash's review gives two reasons. The first is that every adaptation to process
scale requires rigid pH control within a narrow range. The second is that
**phase-transfer kinetics are often slower than ideal**. The compensation for
both is a concentrated lactate buffer, 0.5-2 M — a large reagent burden accepted
to make the chemistry behave [@nash2015chemistry].

This is worth stating plainly because it inverts the usual framing. TALSPEAK's
thermodynamics are excellent and its kinetics are the reason it sits unused. A
book that only ever computes free energies would predict this process to be a
success.

### Re-engineering the Rates

The response was to redesign the chemistry around its kinetics rather than
around its equilibria. @braley2012alternatives replaced the extractant HDEHP
with its phosphonate analogue HEH[EHP] and surveyed alternative holdback
reagents. Their findings are specific and mostly negative, which is what makes
them useful: TTHA offers little advantage over DTPA in conventional TALSPEAK,
and both DTPA and TTHA are too strong to pair with HEH[EHP]. The combination
that works is HEDTA with HEH[EHP], which shows a nearly flat pH dependence
between pH 2.5 and 4.5 — directly attacking the first of Nash's two problems —
while delivering acceptable Am/Ln separation factors. It also gives **more rapid
phase transfer kinetics for the heavier lanthanides without the need for high
lactate concentrations**, which attacks the second. Substituting HEH[EHP] for
HDEHP additionally suppresses the unwanted partitioning of Na⁺, lactic acid and
water into the organic phase [@braley2012alternatives].

That is what deliberate kinetic engineering of a separation looks like when
someone does it: not a new selectivity, but the same selectivity made operable.

### Rates Across the Series Are Not Ordered Like Equilibria

The underlying aqueous chemistry was measured directly by @nash2012kinetics,
and this is the single most suggestive result in the chapter. Using stopped-flow
spectrophotometry with Arsenazo III as a colorimetric indicator — which enables
the experiment and plays no mechanistic role — they followed lanthanide
complexation by EDTA and DTPA in 0.3 M lactic acid at 0.3 M ionic strength. The
equilibrium perturbation proceeds as a first-order approach to equilibrium over
a wide range of conditions, which lets formation and dissociation rate constants
be extracted simultaneously, and they did this **for the entire lanthanide
series except promethium**.

Two mechanistic results follow: dissociation depends inversely on total lactate
concentration, and formation depends directly on [H⁺], which together indicate
that in 0.3 M lactate the exchange of lanthanide ions between lactate complexes
and the polyaminopolycarboxylate governs the process. But the result that
matters for this chapter is the one the authors themselves flag as unexpected:
in both ligand systems, the complex formation reaction is **fastest for Gd³⁺**
[@nash2012kinetics].

Gadolinium sits in the middle of the series. A rate that peaks in the middle is
not a rate that tracks ionic radius, and it is therefore not ordered the way the
stability constants are ordered. That is precisely the condition under which a
kinetic separation could do something an equilibrium separation cannot: the two
orderings are different, so a pair that is nearly inseparable on one axis need
not be nearly inseparable on the other.

The chapter should stop there rather than over-claim. A non-monotonic rate
profile across the series is a necessary condition for kinetic selectivity to be
useful, not a sufficient one, and this experiment measured aqueous complexation
rather than a separation. Nobody has, as far as the searches behind this chapter
found, turned this particular observation into a process.

## When a Rate Ratio Becomes a Separation

A small number of groups have tried to do exactly that. The results are real,
and they are also narrow enough that the caveats have to travel with the
numbers.

### Redox-Driven Kinetic Separation

The Schelter group's approach exploits differences in *oxidation* rates rather
than in binding equilibria. @fang2017electrokinetic prepared rare earth
complexes of the redox-active tripodal nitroxide ligand
[{2-(*t*BuN(O))C₆H₄CH₂}₃N]³⁻ and separated them by the rate at which they
oxidise, obtaining a **single-step separation factor of up to 261 on a 50:50
yttrium-lutetium mixture**. In follow-up work, @cole2020redox reacted rare earth
cyclopentadienides with the triradical tris(2-*tert*-butylnitroxyl)benzylamine,
observed different rates of chelation for an equimolar La:Y mixture, and
obtained a **separation factor of 26** (26.4 ± 2.1 over three runs).

Both numbers are large by the standards of [](#technology-comparison). Four
qualifications belong with them.

**The separation factor is not the recovery.** @cole2020redox's 26 is the
product of a solid enrichment factor of 20.8 and a filtrate enrichment factor of
only 1.27, and the reason the second is so small is that the reaction does not
go to completion: **total yttrium recovery in the solid is 19 %**. The yttrium
that is recovered is 95 % pure, but the lanthanum left in the filtrate is only
56 % pure. Their own kinetic model, run on the measured rate constants for a
reaction that did drive to completion, predicts an upper limit above 1800 — the
gap between 26 and 1800 is conversion, not selectivity.

**The pairs are not the hard ones.** Y/Lu and La/Y are separations across a
substantial difference in ionic radius, not between adjacent lanthanides. The
book's convention from [](#technology-comparison) applies in full: a separation
factor without an element pair is not a number, and these pairs are not Nd/Pr.
Whether the same chemistry gives anything on an adjacent pair is, as far as this
chapter's searches found, untested.

**The chemistry is organometallic and non-aqueous.** Cyclopentadienide complexes
and nitroxide radicals in organic solvent under inert atmosphere are a long way
from a chloride leach liquor. This is bench chemistry demonstrating a principle,
and it should be read as ranking with the designed-ligand work in
[](#selective-crystallization-by-molecular-design) — proof of concept — rather
than with anything in Part II.

**A single-step batch separation factor is not a cascade.** The whole point of
the equilibrium framing is that a modest β is recoverable by staging. A kinetic
separation is much harder to stage, for reasons taken up at the end of this
chapter.

What the work does establish, and this is not small, is an existence proof:
rare earth separation factors far above the solvent-extraction range are
obtainable from rate differences alone, in a system where the equilibrium is not
doing the work.

### Kinetic Separation in Aqueous Extraction

A separate and more process-adjacent line of work runs through the Chinese
Academy of Sciences group of Huang and co-workers, and parts of it are already
cited in [](#coacervates-and-aqueous-biphasic-systems). They have measured
extraction kinetics and kinetic separation for La(III), Gd(III), Ho(III) and
Lu(III) from chloride medium with HEHEHP [@cao2021extraction]; built a kinetic
"push and pull" column extractor combining extraction kinetics in one direction
with aqueous complexation in the other, for Pr/Nd [@wang2019enhanced];
demonstrated kinetically enhanced Pr/Nd separation induced by specific ion
effects [@sui2023kinetic]; and reported non-equilibrium kinetic separation of
thulium, yttrium and erbium on the surfaces of freely rising oil droplets
[@sui2024nonequilibrium].

This is the closest thing in the literature to a sustained programme on kinetic
rare earth separation in aqueous systems, and it is working on the pairs that
matter — Pr/Nd is the adjacent pair a magnet recycler faces.

The push-and-pull column reaches a **maximum separation factor of 21.7 for
Pr/Nd**, against 1.6-1.8 with the extractant alone and 3.3 with the DTPA
pre-complexed in the same apparatus, which is the comparison that isolates the
kinetic contribution [@wang2019enhanced]. Three qualifications travel with it.
It is a maximum over time, not a steady value — the paper's own table is headed
"maximum separation factor," and the ratio climbs past 10 at 250 minutes before
falling back. It is computed on each organic fraction collected against the
residual aqueous column, so it is an instantaneous, per-fraction ratio and not an
equilibrium β. And it holds only at a Pr:Nd feed ratio of 1:4; at 1:3 it is 18.1,
at 1:2 it is 10.0, and at equimolar feed it is 6.2. The abstract's contrast with
"5 or even less" is a literature figure, not this paper's own control.

Specific ion effects give **β = 8.3 for Pr/Nd** on a synthetic feed at the NdFeB
Pr:Nd ratio, against 1.53 for conventional stirred extraction with the same
extractant [@sui2023kinetic]. On a magnet raffinate reconstructed from published
leach compositions — no magnet is leached in that paper — it is 5.8. The process
depends on 2.0 mol/L LiNO₃ as a salting-out agent, recovered by evaporating the
raffinate, which is a thermal duty on the entire aqueous stream and the sort of
cost a kinetic flowsheet has to carry.

The rising-droplet work gives **a separation coefficient of 2.89 for Tm/Er**
against about 1.5 for conventional extraction, once P507 exceeds 0.05 mol/L
[@sui2024nonequilibrium]. The modest number is not the interesting result. What
the competition between DTPA in the aqueous phase and P507 at the droplet
interface does is change the *order*: yttrium moves from last to middle, so the
sequence goes from Tm > Er > Y to Tm > Y > Er. The dissociation rate of the
RE-DTPA complex runs Y < Tm < Er while the extraction ability of P507 runs
Y < Er < Tm, and the opposing orders relocate yttrium. That is the same class of
result as @smith2019selective below — the contacting regime changes what you
separate, not merely how much.

The HEHEHP study is the exception, and it deserves its own treatment because it
runs against this chapter's thesis rather than for it.

### A Counterexample: When the Rate Ratio Is Smaller

The forward extraction of La(III), Gd(III), Ho(III) and Lu(III) into HEHEHP was
measured as flux equations at 293.15 K, and no separation factor appears anywhere
in the paper [@cao2021extraction]. The rate constants alone are the result, and
the ratios they imply are the point: Gd/La is 3.2, Ho/Gd is 1.4, Lu/Ho is 1.4,
and **the whole spread from lanthanum to lutetium is 6.3**. All four activation
energies fall below 20 kJ/mol — 14.32, 7.99, 7.42 and 6.89 kJ/mol respectively —
which places the system in diffusion control.

Two things follow, and both are unwelcome for the idea this chapter is exploring.
The rate ordering runs in the *same direction* as the equilibrium ordering, since
the extraction equilibrium constant of HEHEHP also increases from La to Lu, so
the kinetics add nothing the thermodynamics did not already offer. And a total
rate spread of 6.3 across fourteen elements is far below the equilibrium β
obtainable with the same reagent across the same range. **For this system the
kinetic separation is strictly worse than the equilibrium one.**

The paper's other finding is a warning about staging. Its non-competitive model,
built from the single-ion rate constants, fails to reproduce a four-element
elution: lanthanum, gadolinium and holmium are all inhibited while lutetium is
extracted, and the authors call the non-competitive assumption unreasonable. The
mechanism they offer is that HEHEHP monomer at the interface is a limited
resource, preferentially occupied by the fastest ion, with direct interfacial
exchange on top of it. Their own summary is the sentence to carry: the
competition is obvious even though the mass transfer flux of lutetium is only
1.41 times that of holmium. Single-ion rates do not predict multi-ion kinetic
separation, which is a harder obstacle to a kinetic cascade than any of the ones
in [](#the-catch).

### Transport Control Changes What You Separate

The most direct evidence that rate control alters *selectivity itself* — not
just throughput — comes from a comparison that holds the chemistry fixed and
varies only the contacting architecture.

@smith2019selective compared three configurations on a real coal fly ash
leachate: conventional solvent extraction, a liquid emulsion membrane (LEM), and
a supported liquid membrane (SLM). All three used the same chemistry — D2EHPA in
kerosene or mineral oil, with 5 M nitric acid as strippant. The LEM gave
recoveries per element similar to conventional solvent extraction. The SLM was
slower than the LEM. And the SLM was **notably more selective for the heavy rare
earths, while conventional extraction and the LEM were more selective for the
light ones**.

Their flux-based model identifies why, and the answer is that the two
configurations are rate-limited by different things: SLM recovery rates were
limited by the affinity of the rare earths for the chelator, while LEM rates
were limited by diffusive mass transfer across the liquid membrane
[@smith2019selective].

Same extractant, same strippant, same feed — opposite ends of the series
favoured, because the slow step is different. That is the cleanest demonstration
in this chapter that the selectivity of a separation is a property of the
process and not only of the chemistry, and it is the result to carry forward
from [](#membranes-mofs-and-emerging-approaches).

### What Has Been Demonstrated

| System | Basis | Pair | Reported result | Medium | Status |
|----|----|----|----|----|----|
| RE complexes of a redox-active tripodal nitroxide [@fang2017electrokinetic] | Difference in oxidation rate | Y/Lu, 50:50 | β up to 261, single step | Non-aqueous, organometallic | Bench proof of concept |
| RE cyclopentadienides + triradical proligand [@cole2020redox] | Difference in chelation rate | La/Y, equimolar | β = 26.4 ± 2.1, but at **19 % yttrium recovery**; Y 95 % pure in the solid, La 56 % pure in the filtrate | Non-aqueous, organometallic | Bench proof of concept |
| HEHEHP from chloride medium [@cao2021extraction] | Extraction-rate difference | La, Gd, Ho, Lu | **No β is reported.** Rate constants only; the La→Lu spread is 6.3, and the ordering matches the equilibrium ordering | Synthetic chloride/organic | Laboratory |
| [A336][NO₃]-DTPA push-pull column [@wang2019enhanced] | Extraction kinetics against aqueous complexation | Pr/Nd | β = 21.7 *maximum*, instantaneous and per-fraction, at a 1:4 Pr:Nd feed; 6.2 at equimolar. Controls in the same rig: 1.6-1.8 extractant alone, 3.3 pre-complexed | Synthetic nitrate/organic, column | Laboratory |
| Specific ion effects [@sui2023kinetic] | Kinetic enhancement | Pr/Nd | β = 8.3 at 60 min, falling to 6.91 at 70 min; 5.8 on a reconstructed magnet raffinate. Conventional stirred control: 1.53 | Synthetic; needs 2.0 M LiNO₃ | Laboratory |
| Rising oil droplets [@sui2024nonequilibrium] | Non-equilibrium contacting | Tm/Er | 2.89, against ~1.5 conventional. Extraction *order* inverts: Tm > Er > Y becomes Tm > Y > Er | Synthetic, 1 mmol/L each | Laboratory |
| SLM vs. LEM vs. SX, same D2EHPA chemistry [@smith2019selective] | Which step is rate-limiting | Heavy vs. light REE as groups | No β reported; selectivity *direction* reverses between configurations | Real coal fly ash leachate | Laboratory, real feed |

Three things are visible in that table and none is comfortable. The large
separation factors — 261 and 26 — are on non-aqueous bench chemistry and on pairs
that are not adjacent. The aqueous work on the pairs that matter is real, and its
best adjacent-pair number, 21.7 for Pr/Nd, is an order of magnitude below them
and is a maximum over time at one particular feed ratio rather than a steady
separation factor. And every feed in the table is synthetic; the only real feed
is @smith2019selective's, which reports no β at all. Nothing in the table is
above laboratory scale.

The honest arithmetic is nonetheless favourable where it has been done. A Pr/Nd
separation factor of 8.3 against a same-apparatus control of 1.53, or 21.7
against 1.6, is a five- to thirteen-fold gain on the one pair that most needs it.
That is worth far more than the 261 on Y/Lu, which is a pair a mixer-settler
handles comfortably. The unresolved question is not whether kinetic enhancement
is real for Pr/Nd — three independent measurements now say it is — but whether a
transient maximum at one feed ratio survives being made into a cascade.

## The Kinetic Data the Series Already Has

There is one more body of kinetic data on the lanthanides, it is far larger than
everything above, and it was not measured for separations.

Water exchange — the rate at which a coordinated water molecule on an aqueous
Ln³⁺ ion swaps with bulk solvent — is the elementary step that any inner-sphere
complexation must go through, including extraction. It was measured across the
lanthanide(III) aqua ions by ¹⁷O NMR by @cossy1988oxygen, and that paper remains
the primary reference. This chapter does not quote its rate constants, because
the paper has not been read in full here; the entry is recorded in
`needs-journal-access.md`.

The much larger literature that grew from it belongs to magnetic resonance
imaging. Water exchange rate governs the relaxivity of a gadolinium contrast
agent, so the MRI community has spent decades characterising and tuning it —
@benetollo2003structural, for instance, determined X-ray structures of six
Ln(DOTA) complexes spanning the series, identified the square-antiprismatic and
twisted-square-antiprismatic coordination geometries that the ¹H NMR solution
work had inferred, and connected them to the markedly different water exchange
rates of the two isomers. Their title says what it was for: insights into the
design of contrast agents for magnetic resonance imaging.

The provenance matters, and this book should say so rather than borrow the data
as though it were separations data. The gradient in exchange rate across the
series is real and well characterised. It was characterised to make images, not
to make a separation, and consequently it has been measured under conditions
chosen for biological compatibility rather than for anything resembling a
process. Whether the gradient is exploitable is an open question, not a
half-finished result — and the relevant caution is @nash2012kinetics above,
where the measured formation rates across the series peaked in the middle rather
than tracking radius.

## Where the Analogy Runs Out

In gas separations, kinetic selectivity is standard practice. A carbon molecular
sieve or a small-pore zeolite separates oxygen from nitrogen not because it
binds one more strongly but because one diffuses into the pore appreciably
faster, and pressure-swing adsorption is built on that difference.

The analogy to [](#metal-organic-framework-mof-nanotraps) is obvious and it is
worth being explicit about its status: for aqueous lanthanides it has not been
done. The searches behind this chapter did not find kinetic-sieving separations
of rare earths in MOFs or zeolites from solution. The MOF result the book does
carry — β = 796 for Pr/Lu on NCU-1 — is an equilibrium partitioning measurement,
and [](#membranes-mofs-and-emerging-approaches) notes that no kinetic data
accompanies it at all.

That absence is a research gap, and it should be stated as a gap rather than as
a capability. A hydrated Ln³⁺ ion entering a framework pore must shed part of
its hydration shell, the energetics of that differ across the series, and the
elementary rate data in the preceding section says the rates need not be ordered
like the equilibria. Whether any of that survives contact with a real pore, a
real solvent and a real feed is unknown, because the experiment has not been
reported.

## Kinetic Control in Crystallization

The one place in this book where kinetic control is already treated as a design
variable is [](#selective-crystallization-by-molecular-design), and that
treatment is not repeated here. In outline: at low supersaturation the
thermodynamically stable phase forms, at high supersaturation kinetic effects
intervene and concomitant polymorphism becomes possible, and the
Stranski-Totomanow conjecture — that polymorph selection follows the lowest
nucleation free-energy barrier — would make phase selection a purely kinetic
problem if it held generally. That chapter's own conclusion is that it does not
hold generally, so a design assuming it is on unsafe ground.

The connection worth drawing is that crystallization is the one rare earth
separation family in which practitioners routinely and deliberately operate away
from equilibrium, and it is also the family in which the resulting control
problem is best documented. The lesson transfers to everything above.

## Leaching Kinetics

Rate as an engineering constraint reaches its largest scale in leaching, and
that material is in [](#hydrometallurgical-leaching) rather than here. The
shrinking-core framework, the diagnostic of plotting the data against the two
candidate rate laws, and the activation-energy cross-check are set out in
[](#leaching-kinetics-models), together with the reason ion-adsorption clays
need a different model altogether: the particle does not shrink, because the
rare earths are surface-adsorbed rather than lattice-bound.

Two further kinetic studies of the weathered-crust elution-deposited ores belong
alongside the treatment in [](#ion-adsorption-clays) and are recorded here for
completeness: @tian2010kinetics on leaching with ammonium sulfate solution, and
@he2016kinetics on column leaching of both rare earth and aluminium with
ammonium salt solutions. Neither paper's numbers are quoted, for the same reason
as elsewhere in this chapter.

The point to carry from leaching into the rest of this chapter is that leaching
is where the industry already thinks in rates as a matter of routine, because
nothing else is available: a heap leach has no equilibrium stage count to hide
behind, and its performance is a rate integrated over residence time.

(the-catch)=
## The Catch

Kinetic separation has been an obvious idea for a long time and it has not
scaled. The reasons are structural rather than accidental, and a chapter that
ended on the separation factors above would be misleading.

**Stopping short of equilibrium costs yield — but not always.** The contact time
that maximises the ratio of extracted amounts is not, in general, the contact
time that maximises how much you extract. An equilibrium stage takes what the
chemistry allows; a kinetic stage deliberately takes less.

Two of the papers above deny that this trade is universal. @sui2024nonequilibrium
states outright that on rising oil droplets the separation coefficients increase
"and the extraction percentages do not decrease obviously." @sui2023kinetic
reports 97.2 % praseodymium extracted in kinetic mode against 57.3 % in the
conventional control, with the higher separation factor as well — better on both
axes at once. The caveat is that the two contactors are not comparable: the
kinetic device renews the interface continuously across a 0.5 mm oil film at
6 mL/min, while the control is 0.5 mL of oil stirred against 30 mL of aqueous, so
the phase ratios differ by orders of magnitude. What those results show is that
the trade-off is a property of a particular contactor and not a law. Where the
contactor supplies enough interfacial area, the kinetically favoured element can
be taken to near-completion before the disfavoured one has begun.

@wang2019enhanced is the counterweight and probably the more representative case:
even at β = 21.7 the neodymium co-extraction reaches 51.4 %, which caps product
purity, and the pre-complexed thermodynamic control in the same apparatus lost
recovery badly — 57.6 % Pr and 23.3 % Nd. The trade is real often enough to plan
for and not often enough to assume.

**Staging is harder.** The countercurrent cascade in
[](#countercurrent-cascade-design) works because each stage is a repeatable
equilibrium contact, and the mathematics of stage-to-stage propagation assumes
it. A cascade of stages that are each deliberately incomplete does not compose
in the same way: the feed to stage *n*+1 depends on the residence time in stage
*n*, so residence-time distribution, not just stage count, becomes a design
variable. The Huang group's column extractor [@wang2019enhanced] and the rising
droplet work [@sui2024nonequilibrium] are, read this way, attempts to build a
contactor in which residence time is uniform enough to stage. The deeper problem
is the one @cao2021extraction ran into: even with uniform residence time, the
single-ion rate constants do not compose, because the extractant at the interface
is a contested resource and the fastest ion takes it.

**The operating window is narrower.** An equilibrium separation is robust to
timing by construction — hold the phases together longer and nothing gets worse.
A kinetic separation has an optimum in time, and both sides of it are worse. This
is not a conjecture: @sui2023kinetic's Pr/Nd separation factor is 8.3 at 60
minutes and 6.91 at 70, and @wang2019enhanced's climbs past 10 at 250 minutes and
then declines. Ten minutes of drift costs seventeen per cent of the separation. In
a plant, residence time is not a number but a distribution, and a distribution
that straddles an optimum performs worse than its mean would suggest. This is
the same class of problem that makes the residence-time control in
[](#microfluidic-separations) the enabling feature rather than an incidental
one, and it is a substantial part of why the demonstrations in this chapter are
all bench work.

**Temperature is now doing two jobs.** [](#solvent-extraction-fundamentals)
notes that stripping is often run warm for viscosity and phase-disengagement
reasons. Rates roughly follow an Arrhenius dependence while equilibria follow a
van 't Hoff dependence, and the two need not want the same temperature. A
process that separates on rates has lost the freedom to set temperature for
hydraulic convenience.

None of this makes the idea wrong. It makes it a different engineering problem
from the one the industry has spent seventy years solving, which is a fair
description of why the literature is the size it is. The honest summary is that
kinetic differences between rare earths are real, are measurable, are in at
least one well-documented case *not ordered the same way as the equilibrium
differences*, and have produced large separation factors on easy pairs in
non-aqueous bench systems. The step that has not been taken is any of it on an
adjacent lanthanide pair in a real medium at a scale where residence time is a
distribution.

## Research Opportunities

Stated as gaps rather than as proposals, and each one is a gap this chapter's
own sources leave open.

**The adjacent-pair test of redox-kinetic separation.** The 261 of
@fang2017electrokinetic is on Y/Lu. The same measurement on Nd/Pr or Dy/Tb would
settle whether the approach is a genuinely new axis of selectivity or an
efficient way of exploiting a radius difference that was already exploitable.

**Kinetic sieving of aqueous lanthanides in a framework material.** Standard in
gas separations, absent here. The MOF work in
[](#membranes-mofs-and-emerging-approaches) reports no kinetic data of any kind;
a single uptake-versus-time series on NCU-1 across a lanthanide pair would be a
cheap experiment with a clear answer.

**A rate profile across the series measured under extraction conditions.**
@nash2012kinetics has one for aqueous complexation, @nichols2011mechanistic has
one for interfacial transfer under TALSPEAK conditions. Neither exists for the
industrial extractants of [](#solvent-extraction-fundamentals) across the whole
series under plant-relevant acidity.

**Residence-time distribution as a design variable.** If a kinetic separation
has an optimum in time, then the width of the residence-time distribution is as
important as its mean, and no source consulted for this chapter treats it as a
quantity to be designed. The process models in
[](#process-modeling-and-optimization) assume equilibrium stages throughout.

**Verification of the aqueous kinetic separation factors.** Four papers in this
chapter report kinetic separations on process-relevant pairs and none of their
numbers could be confirmed here. Obtaining and checking them is a small task
with a large effect on how strongly the section above can be written.
