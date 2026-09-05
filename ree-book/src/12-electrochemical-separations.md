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

The companion experimental study by the same group is the best-documented
electrodialysis separation of rare earths in this literature, and it is worth
setting out in full because the book's comparison table has carried a number
from it since the first draft — and the number was carried with the wrong
element pair.

@ding2023separation separate dysprosium from a praseodymium-neodymium mixture in
a four-compartment cell. The working part is a PC-400D anion-exchange membrane
chosen because it passes large organic anions; an AMX anion-exchange and a CMX
cation-exchange membrane close the feed and rinse compartments. The chemistry is
entirely in the EDTA stability constants: p*K*~ABS~ is 16.40 for Pr(III), 16.61
for Nd(III) and 18.30 for Dy(III), so at an EDTA-to-Dy molar ratio near unity
the dysprosium takes almost all of the available ligand and travels to the
concentrate compartment as \[Dy-EDTA]⁻, while the praseodymium and neodymium
stay behind as free cations that the anion-exchange membrane will not pass.

Their best result is a separation factor of 125, at 12 V, pH 4, a 0.05 mol/L
sodium sulfate rinse, an EDTA/Dy molar ratio of 1.0 and 180 minutes, giving 93 %
Dy purity in the concentrate at 77 % Dy yield. Three things about that number
need saying, and the first two correct this book.

**It is Dy over Pr *and* Nd together, not Dy over Nd.** The paper's own defining
equation takes the fraction of dysprosium transferred to the concentrate over
the *combined* fraction of neodymium and praseodymium transferred. Quoting it as
a Dy/Nd figure — as [](#technology-comparison) did until this paper was read —
overstates what was measured, because the denominator is a two-element group.

**It is not a separation factor in the sense the rest of this book uses.**
Everywhere else, β is a ratio of equilibrium distribution ratios. This is a ratio
of recovery fractions after a 180-minute batch in a particular cell, and it moves
with voltage, pH and time: 62 at 10 V, 125 at 12 V, 88 at 14 V; 101 at pH 3
against 88 at pH 4 in a shorter run. A quantity that halves when the voltage
changes by 2 V is a process operating point, not a property of a chemistry, and
it cannot be compared with an extraction β without saying so.

**The feed is synthetic.** Pr, Nd and Dy sulfates in deionized water at 0.001
mol/L each — 140.9, 144.2 and 162.5 mg/L — chosen to resemble a South American
ion-adsorption clay leachate. No real leachate was run.

Set against that, the paper does something few in this chapter do: it says what
the method cannot do, and it measures it. The authors cascade the process to
attack the light pair directly. A stage-2 feed of 47 % Pr and 44 % Nd comes out
after 150 minutes at 55 % Pr and 43 % Nd, and a third stage reaches 61 % Pr and
38 % Nd. Their conclusion is that separating dysprosium from a Pr-Nd mixture is
feasible, and that **separating praseodymium from neodymium is not feasible even
with cascading**, because the two stability constants — 16.40 and 16.61 — are
too close. That is the thesis of this whole book restated in an electrochemical
cell: the handle is the ligand's discrimination, and for an adjacent light pair
the ligand has almost none.

The comparison with solvent extraction in the same paper is the most useful
thing in it. Against literature data for the same Nd/Dy separation, D2EHPA
reaches a separation factor of 247 in two stages and PC88A reaches 125 in three;
the electrodialysis cell reaches 125 in one, with higher dysprosium purity in the
product (93 % against 76.7 % for PC88A). The authors qualify their own
comparison — the solvent-extraction results did not use EDTA, and theirs
requires it — and then give two numbers that matter more than the separation
factor. Energy: the electrodialysis experiment works out at about 45 GJ per
tonne of rare earths separated, against a literature figure of 15.60-22.7 GJ per
tonne for solvent extraction, so on this evidence the cell costs roughly twice
the energy. Space-time yield: 0.002 kg L⁻¹ h⁻¹, which the authors place at the
bottom of the industrial range, alongside biocatalytic processes rather than
chemical ones. Both figures come from a bench cell with a 100 cm² membrane and
500 mL per compartment and would improve with scale and a more concentrated
feed, and the authors say so. They also conclude, in their own words, that a
standalone electrodialysis process may offer no major technical or economic
benefit over solvent extraction at industrial scale, and that its prospect is as
a stage-reducing addition to one.

The sentence to carry out of the paper is the authors' own: electrodialysis
without chelation assistance is not capable of separating rare earths. A
chelation-assisted electrodialysis study exists as well
[@mosadeghsedghi2023chelation] and is cited here for existence only, its text
not having been obtainable. A 2024 review places electrodialysis for critical
minerals in a wider setting, covering selective electrodialysis and
liquid-membrane electrodialysis for unconventional sources [@sim2024electrodialysis].

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
