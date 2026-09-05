---
title: Electrochemical Separations
---

(electrochemical-separations)=
# Electrochemical Separations

Four quite different things travel under the word "electrochemical" in the rare
earth literature, and a reader who does not keep them apart will come away
believing that a field can separate neodymium from praseodymium.

The first is **electrowinning**: reducing a rare earth compound to metal in a
molten salt. That is a production step, not a separation, and it belongs with
the halide chemistry that feeds it — [](#molten-salt-electrolysis).

The second is **electrodialysis**, in which an electric field drives ions
through ion-exchange membranes. The field supplies the transport; the
discrimination, where there is any, comes from a chelating agent added to the
feed.

The third is **electrosorption**, including capacitive deionization, in which
ions accumulate in the electrical double layer of a high-area electrode and are
released when the polarity is reversed. The field supplies the driving force;
the discrimination comes from the surface chemistry of the electrode.

The fourth is **redox separation**, in which the electrode changes the oxidation
state of one element and the separation follows from the chemistry of the new
state. This is the only one of the four in which the electrochemistry is itself
the selectivity.

The distinction runs through the whole chapter and is worth stating in advance
as a rule: **in three of these four families, the electrode is a pump and
something else is the filter.** When a paper in this field reports a
selectivity, the first question is whether it is a property of the
electrochemistry or a property of a ligand, a membrane, or a surface that would
work just as well without the cell.

The field has recently acquired review coverage of its own. @ghosh2025electrochemical
survey electrolysis- and electrosorption-based recovery in *Chemical Reviews*,
framing electrochemical separations as a modular alternative to thermal and
solvent-based extraction and drawing feedstocks from mining and unconventional
sources including coal mining byproducts; @su2020electrochemical gives a shorter
and more general account of electrochemical metal recycling that is useful
mainly for the Faradaic/non-Faradaic distinction used below. A further review of
electrochemical methods for rare earths appeared in 2025
[@akcaguler2025comprehensive]; it is cited here for existence only, because its
text was not available for verification.

(why-an-electrode-is-a-weak-handle)=
## Why an Electrode Is a Weak Handle on the Series

An electrode potential sorts species by their willingness to gain or lose
electrons. If every ion in the feed has the same accessible oxidation state,
that sorting does nothing at all, and this is very nearly the situation across
the lanthanides: they occur in a stable trivalent oxidation state, which is what
makes their chemical properties so similar and their separation so expensive
[@vandenbogaert2015photochemical]. It is the same fact that
[](#why-rare-earths-are-hard-to-separate) states in terms of ionic radius, seen
from the other side.

Reduction to the metal is not available in water either. Rare earth metals are
produced by electrolysis at 800–1000 °C in molten fluoride or chloride melts
([](#molten-salt-electrolysis)), and the reason that industry accepts a
high-temperature cell with a consumable carbon anode is that an aqueous cell
would evolve hydrogen long before it deposited a lanthanide.

Two elements break the pattern, and one of them breaks it only partly.

**Cerium** oxidises to Ce(IV), which hydrolyses at a far lower pH than any
trivalent lanthanide. That is the sharpest split available anywhere in this
book, and it is treated where the resulting precipitation is treated —
[](#cerium-oxidative-precipitation). Anodic oxidation is one way to make the
Ce(IV); chemical oxidants are another, and are what the documented industrial
practice uses.

**Europium** reduces to Eu(II), and the divalent sulfate is far less soluble
than any trivalent sulfate — 0.001 g per 100 g of water for EuSO₄, against
2.10 for Eu₂(SO₄)₃ and 7.47 for Y₂(SO₄)₃ [@vandenbogaert2015photochemical]. Add
sulfate, reduce, and europium alone leaves the solution. The reduction can be
done chemically with zinc powder or zinc amalgam, electrochemically on graphite
or titanium electrodes, or photochemically; and each route has a characteristic
problem. Zinc contaminates the liquor with Zn(II); the amalgam risks mercury
pollution; and — the point that matters for this chapter — **the current
efficiency of electrochemical Eu(III) reduction in aqueous solution is low,
because hydrogen is evolved instead** [@vandenbogaert2015photochemical]. That is
why the photochemical route exists at all, and it is treated with the
crystallization it enables in
[](#photochemical-reduction-of-europium).

Samarium and ytterbium have divalent states as well, but they are reached under
strongly reducing conditions rather than in an aqueous cell; the divalent
chlorides EuCl₂ and YbCl₂ appear in the halide chemistry of
[](#pyrometallurgical-and-halogenation-routes), not in water.

That is the whole of the redox handle: one element that oxidises, one that
reduces, and nothing at all for the fourteen adjacent pairs that make rare earth
separation difficult. Everything else in this chapter uses electricity to move
ions that some other chemistry has already sorted.

(electrodialysis)=
## Electrodialysis

Electrodialysis drives the ions with an electric field instead of a pressure or
a concentration difference. In the configuration studied for rare earths, the
feed is complexed with {index}`EDTA`
and passed between two adjacent anion-exchange membranes, so that the anionic
Ln-EDTA complexes migrate and the uncomplexed cations do not; the selectivity is
the selectivity of the EDTA complexation, and the membranes only sort by charge.

@ding2024mathematical built and validated an extended Nernst-Planck model of
this cell for the separation of Dy from Pr and Nd, and the useful part of the
result is the shape of the trade-off rather than a separation number. Raising
the applied voltage above 8 V speeds the separation and costs disproportionately
more energy; dropping the rinse-solution concentration below 0.05 mol/L improves
energy efficiency but depletes the rinse before the separation finishes; and the
required rinse concentration scales linearly with feed concentration, so a more
concentrated feed is cheaper per kilogram separated. The authors also identify
the flaw in their own cell: independent migration of sulphate carries current
without carrying rare earths, which caps the current efficiency, and they
recommend alternating cation and anion exchange membranes instead. That is
modelling work on a laboratory cell, not a demonstrated separation, and no
throughput or product purity is reported.

The companion experimental study by the same group [@ding2023separation] is the
source of the Dy/Nd separation factor carried in
[](#technology-comparison). That number could not be checked against the
paper's own text, which was not obtainable, and it is listed in
`needs-journal-access.md` as resting on unverified content. A chelation-assisted
electrodialysis study exists as well [@mosadeghsedghi2023chelation] and is cited
here for existence only, on the same grounds. A 2024 review places
electrodialysis for critical minerals in a wider setting, covering selective
electrodialysis and liquid-membrane electrodialysis for unconventional sources
[@sim2024electrodialysis].

What is worth noticing is where the selectivity lives. Strip the EDTA out of
these cells and nothing separates: the membranes discriminate between anions and
cations, not between lanthanides. Electrodialysis is therefore best understood
as a contacting geometry for aqueous complexation chemistry — a way of running a
selective complexation without an organic phase — and its ceiling is the ceiling
of the aqueous ligand. That ceiling is discussed in
[](#the-energy-scale-of-selectivity), and it is not high.

(electrosorption-and-capacitive-deionization)=
## Electrosorption and Capacitive Deionization

{index}`Capacitive deionization <capacitive deionization>` charges a pair of high-surface-area electrodes
and lets ions accumulate in the electrical double layer; reversing the polarity
releases them into a small concentrate stream. Nothing is oxidised or reduced,
which is what @su2020electrochemical means by calling the process non-Faradaic,
and the appeal is that the energy cost scales with the salt removed rather than
with the water processed.

@zhao2022selectively report the first application of capacitive deionization to
rare earth capture from aqueous solution. Their electrode is a pyrrolic-nitrogen
doped activated carbon, made by polymerising pyrrole in situ on the carbon and
then carbonising it, reaching 9.55 at.% nitrogen doping and a capacitance of
128.98 F/g. It takes up 23.66 mg/g of La(III) within 25 minutes and captures
La(III) selectively from a quaternary La/Fe/Ca/Na solution. That last clause is
the one to read carefully: **the demonstrated selectivity is rare-earth over
base-metal, not lanthanide over lanthanide.**

@zhan2024regulating push the same idea onto a different material, using
oxygen-doped MoS₂ electrodes in which chemisorption and electrosorption are
deliberately coupled, and report essentially complete recovery of rare earths
from low-concentration feeds, with the mechanism attributed to interactions
between outer-shell electrons and the exposed sulfur and oxygen sites. La, Gd
and Y are all studied. Again no separation factor for any lanthanide pair is
given.

The most convincing electrosorption result in this literature is not a
separation of rare earths from each other at all but the removal of an impurity
from them. @aziman2021rapid electrosorb thorium from a sulfate medium onto
thermally cross-linked activated-carbon electrodes, reaching a maximum capacity
of 8.4 mg of thorium per gram of carbon, with Langmuir and Freundlich isotherms
both fitting and pseudo-first- and second-order kinetics describing the uptake.
Thorium management is a real and expensive problem in monazite processing —
[](#thorium-management) — and an electrode that removes it selectively is doing
useful work even though it separates nothing within the series.

Taken together, the electrosorption literature on rare earths is a
preconcentration and impurity-rejection literature. It reports capacities, rate
constants, and discrimination against iron, calcium and sodium. It does not
report a separation factor for an adjacent lanthanide pair, and until it does,
the technology's place in a flowsheet is upstream of the separation rather than
inside it.

(what-electrochemistry-is-actually-for)=
## What Electrochemistry Is Actually For

Three duties in a rare earth flowsheet are genuinely electrochemical, and it is
worth naming them plainly because the promotional literature blurs them into a
single claim.

**Making metal.** Molten salt electrolysis is the commercial route from oxide or
chloride to metal, at TRL 9, and the choice of halide upstream determines the
cell — [](#molten-salt-electrolysis) and [@abbasalizadeh2017electrochemical].
Nothing in this chapter changes that, and no aqueous cell competes with it.

**Changing an oxidation state so that another separation can work.** This is the
cerium case, and in principle the europium case. The electrode is a reagent
delivery system: it supplies or removes electrons without adding a chemical
oxidant that must later be washed out. That is a real advantage — it is why
anodic Ce(III) oxidation keeps being proposed — and it is bounded by the two
elements that have a second accessible oxidation state.

**Moving ions without a solvent.** Electrodialysis and electrosorption both do
this, and both are attractive for exactly the reason that solvent extraction is
unattractive: no organic phase, no diluent inventory, no phase disengagement, no
crud. The cost is that neither has yet shown it can do the sorting that the
organic phase does.

**Driving the leach itself.** A field applied to the orebody rather than to a
cell is the subject of the electrokinetic mining work discussed in
[](#electrokinetic-mining), and it is by some distance the largest-scale
demonstration of electrically driven rare earth processing outside a smelter.

(electrochemical-net-assessment)=
## Net Assessment

No electrochemical process in the reviewed literature has separated one
lanthanide from its neighbour on a real feed at any scale. The strongest aqueous
results are a modelled electrodialysis cell, a set of capacitive-deionization
electrodes characterised on synthetic quaternary solutions, and a thorium
scavenger. Against that, the industrial fact is that every gram of rare earth
metal in the world is made in an electrochemical cell, and that a field driven
through an orebody now recovers rare earths at the scale of thousands of tonnes
of ore.

The honest reading is that electrochemistry has a secure and large role in rare
earth processing at both ends of the flowsheet — mobilising the elements out of
the ground and reducing them to metal at the end — and no demonstrated role in
the middle, where the elements are told apart. The chemistry gives a clear
reason for that shape: an electrode acts on oxidation state, and the lanthanides
do not differ in oxidation state.

Two things would change the assessment. The first is a report of a lanthanide
pair separated in an electrochemical cell with the selectivity attributable to
the electrode rather than to an added chelator — a redox-active surface with a
measurable preference across the series would qualify. The second is an
electrodialysis or electrosorption stage placed in a real flowsheet and costed
against the solvent-extraction stages it would replace, of the kind
[](#environment-techno-economics-and-life-cycle) requires. Neither exists yet.
