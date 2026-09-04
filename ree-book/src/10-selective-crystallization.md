---
title: Precipitation and Selective Crystallization
---

(precipitation-and-selective-crystallization)=
# Precipitation and Selective Crystallization

{index}`Precipitation <precipitation>` is the oldest rare earth separation technology and it is still
everywhere in modern flowsheets — as a bulk recovery step at the end of a
{index}`solvent extraction` circuit, as an impurity scrub, and, in the single case of
{index}`cerium`, as a genuine separation. This chapter covers both halves of the subject:
the conventional precipitation chemistry that industry runs today, and the
designed molecular crystals that aim to turn precipitation into a selective
separation in its own right.

The conventional half is largely about choosing a precipitant. Oxalate,
hydroxide, carbonate, double sulfate, fluoride, and phosphate each give a
different combination of recovery, purity, filterability, and cost, and the
choice is usually settled by the downstream calcination step rather than by
selectivity — because none of them discriminates well between adjacent
lanthanides. The exception is cerium, which can be oxidised to Ce(IV) and
dropped out of a trivalent mixture cleanly. That exception is instructive: it
works because oxidation state, unlike ionic radius, is a threshold property.

The second half of the chapter asks whether that kind of threshold can be
engineered. Ionic radius varies by only about 0.15 Å across the whole lanthanide
series, and extractants respond to that difference more or less linearly — which
is why they need so many stages. A crystal lattice does not: it either
accommodates an ion or it does not. Selective borate crystallization,
supramolecular cages, and cyclic peptide hosts are all attempts to convert a
gradient in radius into a discontinuity in what precipitates.

## Conventional Precipitation

### What the precipitation is for

A catalogue of precipitants is not useful on its own, because the seven
reagents below are not competing to do the same thing. Before comparing them it
is worth separating three distinct jobs, since most of the confusion in this
literature comes from quoting a number achieved in one job as though it settled
another.

The first job is **bulk recovery**: getting the rare earths out of a leach
liquor or a loaded strip solution and into a solid that can be filtered, washed
and calcined. Selectivity between lanthanides is irrelevant here — the feed is
already the fraction you want — and what matters is yield, filterability and
what the solid turns into on heating. Oxalate is the classical answer, and
carbonate is the cheaper one.

The second job is **group separation**: splitting one part of the series from
another. Only two conventional precipitations do this. Sodium double sulfate
splits light from heavy, and oxidative precipitation of Ce(IV) removes cerium.
Both give a group or a single element, never a purified individual lanthanide
from the middle of the series.

The third job is **impurity rejection**, and it is not about the rare earths at
all: the target is iron, aluminium, thorium and uranium, and the figure of merit
is how little rare earth is lost while removing them. Staged hydroxide or
carbonate precipitation is the workhorse, and the numbers quoted for it are
impurity removals and rare earth *losses*, not rare earth recoveries.

Read that way, a claim like "95 % recovery by precipitation" means nothing until
you know which of the three it refers to.

### What decides whether anything precipitates

Two thermodynamic surveys of rare earth precipitation, both by Han and
co-workers, cover the common precipitants — sulfate, carbonate, fluoride,
phosphate and oxalate — on a common basis, and their conclusions are the right
starting point [@kim2020characteristics; @han2021thermodynamic].

The first is that pH governs everything, but indirectly: it sets the speciation
of the *precipitant*, and which anion is present determines whether a solid
forms [@kim2020characteristics]. Oxalic acid, carbonic acid and phosphoric acid
are all weak, so at low pH the precipitating anion barely exists. This is why
oxalate precipitation has a pH floor and why a "precipitant strength" ranking
quoted without a pH is not a meaningful quantity.

The second is that the anion carried over from the leach step is not a
spectator. Cl⁻, NO₃⁻ and SO₄²⁻ all complex the dissolved rare earths, and the
medium changes the precipitation behaviour measurably: in that analysis the
nitrate environment is the most conducive to precipitation, followed by sulfate
and then chloride [@kim2020characteristics]. A precipitation recipe developed on
a chloride liquor is therefore not directly transferable to a sulfate one, which
matters because the two large bastnäsite routes use opposite acids
([](#hydrometallurgical-leaching)).

The third undercuts the usual hierarchy. Double salt precipitation — sodium
double sulfate on the cation side, the fluoride-carbonate system on the anion
side — is *frequently as effective as oxalate and phosphate, even at low pH*
[@han2021thermodynamic]. The familiar ordering that puts oxalate at the top and
sulfate somewhere in the middle is a statement about single-salt solubility
products, not about what precipitates from a real acidic liquor.

### Oxalate: recovery, and the form the product leaves in

Oxalic acid is the classical final-recovery reagent, and it is worth being clear
that it is chosen for the *product*, not for selectivity. The reaction is

$$
2\,\mathrm{RE}^{3+} + 3\,\mathrm{C_2O_4^{2-}} + 10\,\mathrm{H_2O} \rightarrow \mathrm{RE_2(C_2O_4)_3}\!\cdot\!10\,\mathrm{H_2O} \downarrow
$$

so the stoichiometric requirement is 1.5 mol of oxalate per mole of rare earth,
and the decahydrate calcines directly to a mixed oxide. Everything downstream of
a rare earth plant — oxide product, reduction to metal, feed for
{index}`molten salt electrolysis` — wants an oxide, and oxalate is the cheapest
route to a filterable solid that becomes one.

The parametric picture is well documented for a chloride liquor. Nawab, Yang and
Honaker ran a central composite design on a low-grade pregnant leach solution
and found oxalic acid dosage and pH to be the two dominant factors:
raising the oxalic acid concentration from 0 to 80 g/L took precipitation
efficiency from about 4.2 % to 95.0 %, and raising the pH from 0.5 to 2.5 took
it from 0.0 % to 98.9 % [@nawab2022parametric]. Two secondary results in the
same study matter more for process design than either headline number. Raising
the temperature *decreased* recovery, which identifies the rare-earth-oxalate
reaction as exothermic — so the common instruction to warm a precipitation to
improve kinetics is the wrong instruction here. And product purity fell as pH
rose, so recovery and purity pull against each other; the authors settled on pH
1.0-2.0 as the window that serves both [@nawab2022parametric].

Iron is the reason oxalate precipitation is not simply a matter of adding enough
acid. Fe(III) forms a series of oxalate complexes — Fe(C₂O₄)₃³⁻, Fe(C₂O₄)₂⁻ and
Fe(C₂O₄)⁺ — which consume the oxalate anion before the rare earths can, so a
contaminated liquor needs more reagent for less product [@nawab2022parametric].
That is a direct argument for putting an iron removal stage upstream rather than
paying for it in oxalic acid.

The choice of oxalate over hydroxide or carbonate also has consequences that
only show up in the washing and the water balance. In a study of spent NiMH
battery leachates, where the pregnant solution carries roughly 46 g/L nickel,
all three conversion routes gave similarly high yields and similarly fast
kinetics; what separated them was that the oxalate route avoids co-precipitating
nickel, and so cuts the water needed to wash the intermediate double sulfate
salt free of impurities by a factor of five [@laskar2025conversion]. The same
work states the cost of that choice plainly: rare earth oxalates are poorly
soluble, so they are a dead end for further *aqueous* processing and suit a
thermal decomposition route only [@laskar2025conversion].

The one attempt to make oxalate do a separation rather than a recovery runs the
chemistry backwards. The CSEREOX method selectively *solubilizes*
water-insoluble rare earth oxalates, separating within two rare earth subgroups,
and works at low initial rare earth concentration — below 5 % — on processed
magnet waste [@boronski2020rationally]. This is a redissolution-based
separation, not a selective precipitation, and it belongs with the designed
systems in the second half of this chapter rather than with the bulk chemistry
here.

### Carbonate: the cheaper solid, and the one that redissolves

Carbonate is chosen when the precipitate has to go back into solution. Rare
earth carbonates dissolve in mild acid, which makes them the natural handoff
between a sulfate circuit and a chloride one, or between a crude precipitation
and a purification. That is a property oxalate does not have.

For acid mine drainage, Vaziri Hassas and co-workers compared precipitants
directly and found that hydroxide alone tops out: only up to 70 % of the total
rare earths can be recovered with NaOH at circumneutral pH, whereas a two-step
treatment based on Na₂CO₃ recovered over 85 % [@hassas2021effect]. The gain is
not from carbonate being a stronger precipitant in isolation but from what the
two-step arrangement does to aluminium: staging the carbonate addition lets
aluminium be taken out in its own step without dragging the rare earths with it,
which is exactly what a single hydroxide ramp cannot do
[@hassas2021effect; @vazirihassas2022selective; @zhao2022selective].

### Double sulfate: a group separation, not a purification

Sodium rare earth double sulfate, NaRE(SO₄)₂·H₂O, is the one conventional
precipitation that splits the series. The light rare earths form the less
soluble sodium double salts, so adding Na₂SO₄ to a sulfate liquor drops out a
light-enriched solid and leaves the heavies and yttrium behind. Solubility data
for the various rare earth salts on which this rests are compiled in Forsberg's
review of crystallization-based separation [@forsberg2024separation].

Two things must be said about it, and they are usually left out. The first is
that the product is an intermediate, not a product. Silva and co-workers
precipitated a purified rare earth sulfate liquor with Na₂SO₄ and obtained a
sodium rare earth double sulfate containing 41.4 wt % rare earth oxides, having
precipitated 88 % of the rare earths in the feed at a reagent cost of 0.82 t of
sodium per tonne of rare earths [@liu2019selective]. Roughly 40 % REO is a
concentrate, and it still has to be converted — to hydroxide, carbonate or
oxalate — before it is worth anything, which is the whole subject of the NiMH
conversion study above [@laskar2025conversion].

The second is that double sulfate precipitation is temperature-gated in a way
oxalate and phosphate are not: in the same comparison, precipitation with
Na₂SO₄ occurred only at 70 °C, while Na₂HPO₄ worked anywhere from 20 to 70 °C
[@liu2019selective]. On a leachate from spent NiMH batteries, selective
precipitation of the sodium double sulfate is nonetheless described as the most
direct route to the light rare earths — La, Ce, Pr and Nd — because it leaves
the nickel and potassium in solution [@laskar2025conversion].

(cerium-oxidative-precipitation)=
### Cerium: where precipitation actually separates an element

Cerium is the exception that proves the rule about ionic radius. It is the most
abundant rare earth and typically the largest single component of hard-rock
rare earth ores, and because demand has concentrated on neodymium and
dysprosium, the cerium market has saturated and its price collapsed — so the
economic case for removing cerium before solvent extraction is to stop paying to
separate something nobody wants [@elizalde2019oxidative]. The chemistry that
makes this possible is a change of oxidation state rather than a change of size:

$$
\mathrm{Ce}^{3+} \rightarrow \mathrm{Ce}^{4+} + \mathrm{e}^-
$$

$$
\mathrm{Ce}^{4+} + 4\,\mathrm{OH}^- \rightarrow \mathrm{Ce(OH)_4} \downarrow
$$

Ce(IV) hydrolyses at a far lower pH than any trivalent lanthanide, which is why
this is a clean split rather than a gradient. That is the discontinuity in
[](#fig-precipitation-ph).

McNeice, Kim and Ghahreman tested four oxidants — hydrogen peroxide, sodium
hypochlorite, potassium permanganate and Caro's acid — in acidic chloride
solution over pH 1.0 to 4.0 at 25, 45 and 65 °C, and built Pourbaix and
speciation diagrams for the conditions under which cerium is oxidised. Complete
cerium removal was achievable with potassium permanganate and with Caro's acid —
but, importantly, *in the absence of other rare earths*
[@elizalde2019oxidative]. That qualifier is the whole difficulty: an oxidant
strong enough to take Ce(III) to Ce(IV) quantitatively will also carry other
rare earths into the solid by occlusion and co-precipitation.

The best-documented recent result on a real mixture comes from a mixed rare
earth oxide recovered from waste NiMH batteries, where potassium permanganate
precipitated Ce(OH)₄ at 99.8 % efficiency while keeping co-precipitation of the
other rare earths below 1.5 % [@salehi2025tailored]. The mechanism of the
cheaper peroxide route has been worked out separately
[@moldoveanu2025separation; @moldoveanu2023cerium], and manganese ferrites have
been proposed as a low-cost sorbent for taking Ce(IV) out of highly acidic
liquors [@meng2024efficient].

Industrially the split is usually done in the furnace rather than the tank. The
Mountain Pass route calcines the bastnäsite concentrate in air at roughly
600 °C, which decomposes the fluorocarbonate and oxidises Ce(III) to Ce(IV);
the subsequent hydrochloric acid leach dissolves the trivalent rare earths and
leaves cerium behind as a residue, so the liquor reaching solvent extraction is
already cerium-depleted [@gupta2004extractive; @castor2006rare]. That flowsheet
is set out in full in [](#hydrometallurgical-leaching).

### Hydroxide: an impurity-rejection step that is often mistaken for a recovery

Hydroxide precipitation is where the "three jobs" distinction earns its keep,
because a staged hydroxide ramp is doing impurity rejection for most of its
range and only becomes a rare earth recovery at the very top.

The underlying trend is real. Modelled across the whole series, the solubilities
of the rare earth hydroxides decrease from La to Lu as the cation radius
contracts — most visibly among the lighter lanthanides — and they vary far more
in the acidic-to-neutral range than above about pH 9.5, where all of them are
low [@liu2024modeling]. That same modelling contains a warning against reading
the trend as a radius rule: Y(OH)₃ falls between the cerium and praseodymium
hydroxides in solubility even though yttrium's crystal radius is close to
holmium's [@liu2024modeling]. Yttrium tracks the heavy rare earths in solvent
extraction; it does not necessarily do so here.

The sourced picture of where things actually come out of a real acidic liquor is
this:

| Species | pH window | Source |
|---------|-----------|--------|
| Fe³⁺ | removed over 2.0-3.0; essentially complete by 3.5 | [@zhang2018rare; @li2025iron] |
| Al³⁺ | removed over 3.5-4.5 | [@zhang2018rare] |
| Th⁴⁺ | \~95 % removed at 3.6 with MgCO₃ and H₂O₂ | [@li2025iron] |
| Rare earths, as hydroxide | thermodynamically favourable over 7.0-10.0 | [@zhang2018rare] |

The gap between the fourth row and the first three is what makes staged
precipitation work at all. But the interesting result in that study is what
happens *in* the gap. Treating a natural coal-refuse leachate, Zhang and Honaker
recovered more than 80 % of the rare earths in the pH range 4.85-6.11 — well
below the window in which rare earth hydroxides are predicted to precipitate —
and model-system experiments showed why: the rare earths are not precipitating
as hydroxides there at all, but adsorbing onto the iron and aluminium
hydroxysulfate solids that are. In a liquid containing only Fe³⁺ and SO₄²⁻,
about 40 % of the lanthanum was removed at pH 3.5; in one containing Al³⁺ but no
Fe³⁺, none was; with both present, competitive adsorption limited removal to
around 10 % at pH 3.5, rising to complete removal by about pH 6.5
[@zhang2018rare].

That is a mechanistic result with a practical edge. Rare earth losses in an
impurity-rejection stage are largely adsorption losses onto iron and aluminium
solids, so they are controlled by how much iron and aluminium there is and by
the sulfate that bridges the metal to the oxide surface — not by the rare earth
hydroxide solubility products.

[](#fig-precipitation-ph) shows the consequence for selectivity within the
series, which is the point at which hydroxide precipitation stops being useful.

:::{figure} ../figures/10-precipitation-ph.svg
:name: fig-precipitation-ph
:width: 100%

Where the rare earths come out as hydroxide. The bands are flat because no
per-element data supports anything else. The figure was drawn from group
precipitation windows — light rare earth 6.8–7.5, heavy rare earth 7.0–8.0,
yttrium 6.5–7.5 — which are widely quoted as process figures but which this
book was unable to trace to a primary source; they are shown here for the
overlap they display rather than for their exact values, and the sourced
thermodynamic modelling in the text puts rare earth hydroxide precipitation
across the whole series in the single band pH 7.0–10.0 [@zhang2018rare], which
supports the same conclusion more directly: one hydroxide step returns a group,
not an element. No solubility product is used, and nothing here is a fitted or
interpolated curve. Cerium is drawn as a discontinuity rather than a trend,
because that is what it is: oxidised to Ce(IV) it comes out around pH 3–5,
several pH units below its neighbours — oxidation state is a threshold where
radius is only a gradient. The same pH window takes Fe, Th, Al and U, which is
why the industrial sequence oxidises cerium only after those are gone. Yttrium
is placed between Ho and Er by six-coordinate ionic radius, 0.900 Å against
0.901 and 0.890 [@shannon1976revised]; note that the hydroxide-solubility
modelling cited in the text places Y(OH)₃ between the Ce and Pr hydroxides
instead [@liu2024modeling], so this placement reflects radius, not measured
hydroxide behaviour. Promethium is greyed because it appears in no real feed.
Drawn by `tools/figures/fig_precipitation.py`.
:::

### Removing thorium, uranium and aluminium

The elements that have to be rejected before a rare earth product is saleable
are iron, aluminium and — because the product specification is radiological, not
chemical — thorium and uranium ([](#thorium-management)). Four approaches appear
in the recent literature, and they trade reagent cost against how much rare
earth they take with them.

Magnesium carbonate with hydrogen peroxide is the cheapest. On a rare earth
pregnant leach solution, a response-surface optimisation put the best conditions
at 81 °C and pH 3.6, giving complete iron removal, about 95 % thorium removal
and about 65 % aluminium removal for total rare earth losses under 3 %;
kinetic experiments showed equilibrium reached within 30 minutes
[@li2025iron]. The same study attaches a technoeconomic estimate to a
1000 m³/day plant, which is unusual and worth having.

For aluminium specifically, complexing precipitants do better than pH control.
8-hydroxyquinoline dosed at 1.25 times the theoretical requirement, for ten
minutes at 60 °C and a final pH of 4.5, removed 94.39 % of the aluminium from an
ion-adsorption rare earth leach solution at a rare earth loss of 8.21 %, and the
solid was coarse and easy to filter [@wang2020removal]. Note that an 8 % rare
earth loss is not negligible; this is a reagent that buys aluminium rejection
with rare earth units.

For thorium and uranium, alkyl-substituted aminobis(phosphonates) are the most
striking recent result. The longer-chain ligands separate thorium, uranium and
scandium from the rare earths in a 15-minute precipitation with separation
factors generally in the range 100 to 2000 in acidic aqueous solution, and the
metals can be stripped from the ligand with 3 M HNO₃ without decomposing it, so
the ligand recycles. The same ligands improve separation factors between
adjacent lanthanides relative to conventional oxalate precipitation
[@szczesniak2021alkyl]. Trialkyl phosphine oxide grafted onto a porous
silica-polymer support is the adsorption analogue of the same idea, aimed at the
same separation [@he2025efficiently].

### Phosphate and fluoride: choosing the form of the product

Phosphate and fluoride are less about separation than about what the rare earths
need to be for the next step.

Disodium hydrogen phosphate is a more aggressive precipitant than sodium sulfate
on the same liquor and a cheaper one in sodium terms. In Silva's comparison,
Na₂HPO₄ precipitated 100 % of the rare earths in the feed at 0.31 t Na per tonne
of rare earths, against 88 % at 0.82 t Na for Na₂SO₄, and worked from 20 to
70 °C rather than only at 70 °C; the phosphate product — a mixture of rare earth
phosphate and sodium rare earth double sulfate — assayed 42.9 wt % REO
[@liu2019selective]. That study is also a good illustration of the impurity
argument above: the liquor was first purified with limestone to pH 3.5 and then
lime to pH 5.0 to strip Fe³⁺, Th⁴⁺ and PO₄³⁻ and to cut Al³⁺, Ca²⁺, UO₂²⁺ and
SO₄²⁻, at a cost of about 7 % of the rare earths in the feed, and the
higher-purity products came from the purified liquor [@liu2019selective].

Fluoride precipitation exists mainly because {index}`molten salt electrolysis`
runs on rare earth fluorides. Converting rare earth oxides to fluorides is a
recognised feed-preparation step for electrowinning in molten fluoride baths
[@abbasalizadeh2017electrochemical], and the direct gas-solid route has been
characterised in reactor terms: fluorination of neodymium carbonate monohydrate
with anhydrous HF to the trifluoride is independent of temperature and linear in
HF partial pressure [@pretorius2019fluorination]. Rare earth fluorides can also
be recovered from spent molten-salt electrolytic slag by vacuum distillation
rather than by aqueous precipitation at all [@yang2024investigation]. Whichever
route is used, hydrogen fluoride handling dominates the engineering: it is the
one reagent in this chapter whose safety case is harder than its chemistry.

### Fractional crystallization: the method everything here replaced

{index}`Fractional crystallization <selective crystallization>` deserves to be
described as history, because that is what it is, and the chapter is worse if it
blurs the line.

Before ion exchange and solvent extraction, repeated recrystallization was the
*only* way anyone obtained a pure individual rare earth. The principle is
straightforward: dissolve a mixed rare earth double salt, crystallize part of
it, and the less soluble component is enriched in the crystals while the more
soluble one concentrates in the mother liquor. Neither fraction is pure, so both
are recrystallized, and the operation is repeated. Because the solubility
difference between adjacent lanthanides in any given salt is very small, the
enrichment per operation is very small, and the number of operations needed to
reach a pure product is correspondingly very large. Salts were chosen for having
the widest solubility spread available over the part of the series being worked;
the double magnesium nitrates, used for the samarium-europium-gadolinium region,
are the example most often named.

It is common to see a specific figure attached to this — a stated number of
recrystallizations, usually in the thousands, for the hardest separations.
**This book does not assert one.** Such figures are widely repeated and I could
not trace any of them to a primary source, and the same applies to the tabulated
lists of which double salt was used for which part of the series. What can be
stated is that the effort was large enough that the method did not survive the
arrival of anything better.

What replaced it is precisely dated. Spedding and co-workers at Ames reported
rare earth separation by ion exchange at pilot-plant scale in 1947
[@spedding1947separation], and the theory for separating adjacent rare earths
with chelating eluants followed within a decade [@powell1956basic]; solvent
extraction then displaced ion exchange for bulk production. Fractional
crystallization is not part of a modern separation flowsheet.

The reason to keep it in the chapter is that it is the clearest statement of the
idea the second half of the chapter is trying to rescue. Fractional
crystallization failed not because crystallization is a bad separation principle
but because *unengineered* salts have almost no selectivity, so the process was
forced to buy separation with repetition. Everything in
[](#selective-crystallization-by-molecular-design) is an attempt to buy it with
molecular design instead. Crystallization-based separation as a research area is
active again for exactly this reason
[@forsberg2024separation; @chen2025selective; @wang2025selective].

### What industrial practice constrains that laboratory practice does not

Three constraints separate a precipitation that works in a beaker from one that
works in a plant, and they explain most of the choices above.

**The product form is chosen by the step after it, not by the precipitation.**
Oxalate is picked because it calcines to an oxide and because it rejects nickel;
its poor solubility, which would be a defect if the solid had to be redissolved,
is irrelevant on a thermal route and disqualifying on an aqueous one
[@laskar2025conversion]. Carbonate is picked when the solid has to go back into
acid. Fluoride is picked when the next unit operation is an electrolysis cell.
None of these is a selectivity argument.

**Reagent consumption is a real design variable, and it is set by the
impurities.** The sodium consumption difference between Na₂SO₄ and Na₂HPO₄ —
0.82 against 0.31 tonnes of sodium per tonne of rare earths — is a plant-scale
cost, not a detail [@liu2019selective]. So is the oxalic acid consumed by iron
oxalate complexes rather than by rare earths [@nawab2022parametric], and so is
the fivefold difference in wash water between the oxalate and hydroxide
conversion routes on a nickel-bearing liquor [@laskar2025conversion]. Each of
these is an argument for spending money on impurity removal upstream.

**Recovery and purity move in opposite directions, and the plant has to choose.**
This is visible in every well-designed study in this section: oxalate purity
falls as pH rises even though recovery climbs [@nawab2022parametric]; the
higher-purity phosphate and sulfate products came from the purified liquor,
which itself cost 7 % of the rare earths [@liu2019selective]; aluminium
rejection by 8-hydroxyquinoline costs 8 % of the rare earths
[@wang2020removal]; the magnesium carbonate route holds total losses under 3 %
but leaves 35 % of the aluminium behind [@li2025iron]. A flowsheet is a
particular resolution of that trade-off, and quoting one side of it without the
other is the most common way this literature is misread.

(selective-crystallization-by-molecular-design)=
## Selective Crystallization by Molecular Design

### Key Mechanisms for Selectivity

#### Structural Divergence Across the Lanthanide Series

Different lanthanides form different crystal structures under identical
conditions [@yin2017rare; @chen2025selective], and three mechanisms are
invoked to explain it. The larger early lanthanides prefer higher coordination
numbers than the smaller late ones; the same ligand can polymerize differently
depending on the metal centre it is built around; and soft donors such as Cl⁻
bind the early lanthanides preferentially. None of these is a gradient in
radius — each is a discrete change in what structure forms — which is the point.

#### Thermodynamic vs. Kinetic Control

The interplay between thermodynamics and kinetics is where these systems are
hardest to control. At low supersaturation the thermodynamically stable form
dominates; at high supersaturation kinetic effects intervene and concomitant
polymorphism becomes possible, so two phases appear at once and have to be
separated afterwards. Reaction time is a variable in its own right, as the
Nd/Sm borate system shows [@yin2017rare], and surface thermodynamics can drive
one crystal structure into another after it has formed.

The Stranski-Totomanow conjecture holds that polymorph selection is governed by
the lowest free-energy barrier for nucleation, which would make this a purely
kinetic problem. Recent work shows that kinetic effects do not fully explain
structural transformation in every polymorphic situation, so a design that
assumes they do is on unsafe ground.

### Promising Approaches

#### Selective Borate Crystallization

Yin, Wang and co-workers demonstrated that six distinct borate phases form under
identical reaction conditions across the lanthanide series [@yin2017rare]. The
divergence comes from alterations in Ln³⁺ coordination, from the diversity of
borate polymerization — different fundamental building blocks assemble around
different metals — and from soft-ligand coordination selectivity. Two
separations follow from it: a one-step quantitative Nd/Dy separation using
density-based flotation of the two crystal phases, and an enhanced Nd/Sm
separation obtained by controlling the reaction kinetics [@yin2017rare].

The density-based flotation step is worth noticing. It is a separation performed
on a *physical* property of the crystals rather than a chemical one, which is
possible only because the two lanthanides ended up in structurally different
solids.

The simple rare earth orthoborates LnBO₃ are themselves polymorphic across the
series, with a vaterite-type structure adopted over part of it
[@bradley1966vaterite]; structural divergence of this kind is what the borate
crystallization route exploits.

#### Supramolecular M₄L₄ Cage Self-Assembly

Tetrahedral M₄L₄ cages assembled from tris-tridentate ligands show multivalent
cooperative enhancement of metal ion selectivity [@li2018supramolecular]. The
cages form with metal ions from across the periodic table — Ca²⁺, Cd²⁺ and the
full Ln³⁺ series — and they self-sort with high precision during mixed-metal
assembly, which the corresponding M₂L₃ assemblies do not. They are also stable
to excess metal and excess ligand, unlike the tridentate and bis-tridentate
ligands carrying the same coordination motif.

The design argument is that the tiny differences in a single metal-ligand
interaction are amplified by the multivalent cooperativity of the assembly,
which is precisely what is needed to separate metal ions with near-identical
properties; the authors put this forward as a principle for next-generation
lanthanide extractants [@li2018supramolecular].

#### Phenanthroline-Dicarboxylic Acid (H₂PDA) Systems

Yin and co-workers used 1,10-phenanthroline-2,9-dicarboxylic acid (H₂PDA) with
N,N'-dimethylformamide and its decomposition products to achieve selective
crystallization separation, exploiting the differing crystallization periodicity
of the lanthanides in a solvothermal system [@yin2025selective]:

| Lanthanide Pair | Separation Factor |
|-----------------|-------------------|
| La/Ce           | 2.0 ± 0.1         |
| La/Sm           | 8.9 ± 0.1         |
| La/Lu           | 26.9 ± 3.1        |

Structurally distinct lanthanide compounds crystallize from the same
mixed-organic solvent system depending on which lanthanide is present
[@yin2025selective]. Note the shape of that table: the separation factor grows
with the separation in the series, which is what a structural-divergence
mechanism should do, and the adjacent-pair value of 2.0 is the number that would
have to carry a real cascade.

#### Cyclic Peptide Hosts (Biomimetic Approach)

Inspired by natural biomineralization, lanthanide-binding cyclic peptides (Lamp)
recognize Ln³⁺ through a 1:1 complexation-precipitation process
[@hosokawa2022improved], promoting hydroxide-like Ln species that bind the
peptide and accumulate as insoluble precipitates [@hatanaka2017rationally]. The
system operates in water at near-neutral pH, around 6, without organic solvents
or additional energy input [@hatanaka2017rationally] — which for a separation
technology is an unusual set of operating conditions and the main reason to be
interested in it.

The major driving force in Ln³⁺ recognition is electrostatic interaction from
the side-chain COOH moieties of the acidic amino acids, aspartic and glutamic
acid [@hatanaka2017rationally]. Moving those acidic residues to different
positions in the ring changes the selectivity, and the repositioned variants
show high Lu³⁺ selectivity; the authors rationalize this through dipole moment,
LUMO energy and cohesion energy [@hosokawa2022improved].

#### Macrocyclic Chelator Precipitation

Jones and co-workers developed cyclen-based macrocyclic chelators that induce
large solubility differences among the rare earth chelates, enabling selective
precipitation from pH-neutral aqueous solution; simple coordinating additives
such as acetate form ternary compounds whose solubility can be tuned
[@jones2025macrocyclic]. Repeated precipitations separated even adjacent
lanthanides, and an automotive NdFeB magnet was processed to a 99.7 % pure
neodymium product without organic solvents [@jones2025macrocyclic].

The failure mode of this approach is instructive, and the authors state it. In
solution the lanthanide chelates behave as discrete, independent entities, but
the growth of a microcrystalline precipitate involves interactions between
chelate units — so errors in lattice assembly can incorporate significant
amounts of the *soluble* chelate into the matrix of the insoluble one. The
selectivity that exists in solution is not automatically inherited by the solid.

#### Reverse-Size Selective Aqueous Complexants

Replacing the pyridyl-2-carboxylic acid pendant arms of macropa with
pyridyl-2-phosphinic acid arms (macrophosphi) dramatically enhances
discrimination among the light lanthanides [@thiele2020tuning]. The binding
affinity of macrophosphi for La³⁺ is over five orders of magnitude higher than
for Gd³⁺, and separation factors up to 45 were achieved for the Ce/La pair with
macrophosphi as the aqueous complexant in a biphasic system against the
industrial extractant bis(2-ethylhexyl)phosphoric acid (HDEHP).

#### Ligand-Assisted Selective Precipitation

Two designed-ligand strategies sit between the conventional chemistry of the
first half of this chapter and the crystal engineering of the second.

Pre-organized triamidoarene platforms selectively precipitate light rare earth
nitratometalates as supramolecular capsules under acidic biphasic conditions,
with intra- and intermolecular hydrogen bonds dictating the selectivity; the
receptor can be recycled [@oconnelldanes2022selective].

The "tug of war" strategy uses two ligands with opposite selectivity at once: a
water-soluble bis-lactam-1,10-phenanthroline with affinity for the light
lanthanides against an oil-soluble {index}`diglycolamide` that binds the heavy
ones. The opposed preferences magnify the split, giving quantitative separation
of the lightest lanthanides (La-Nd) from the heaviest (Ho-Lu) and enabling
separation of the neighbouring lanthanides in between, Sm through Dy
[@johnson2023size].

### What stands in the way

Five obstacles recur across every system above, and they are not
interchangeable.

The first is that solution selectivity does not transfer to the solid.
Lattice-assembly errors incorporate soluble chelates into the insoluble matrix,
so a system with excellent solution-phase discrimination can still crystallize a
mixed solid [@jones2025macrocyclic].

The second and third are two faces of the same control problem. Whether the
kinetic or the thermodynamic product forms depends on conditions that have to be
held tightly, and when control is lost the result is concomitant polymorphism —
several phases at once, requiring a further separation to undo.

The fourth is scale. Almost every demonstration in this section is at
proof-of-concept scale, on synthetic feeds, with gram quantities.

The fifth is the physical reason the whole problem is hard: the 4f orbitals are
shielded and do not participate in bonding with ligand orbitals, so the
interactions available to a designer are essentially electrostatic and steric
[@yin2025selective]. This is the same constraint that limits solvent extraction;
crystallization does not evade it, it only converts a small energetic difference
into a discrete structural outcome instead of a small distribution-ratio
difference.

### Design Principles for New Systems

Reading the systems above together, and against the recent surveys of
crystallization-based separation
[@chen2025selective; @wang2025selective; @forsberg2024separation], an effective
molecular crystal system for rare earth separation needs four things. It must
amplify small ionic radius differences, which in practice means multivalent
cooperativity rather than a single binding site. It must offer multiple
coordination modes so that different lanthanides can be accommodated
differently. It must expose a handle — temperature, solvent, time, pH — through
which the balance between kinetic and thermodynamic control can actually be set.
And it should produce crystalline products that differ in some bulk physical
property, solubility or density, so that the final separation can be performed
mechanically on the solids rather than chemically all over again.
