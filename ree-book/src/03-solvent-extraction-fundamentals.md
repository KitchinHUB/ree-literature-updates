---
title: Solvent Extraction Fundamentals
---

(solvent-extraction-fundamentals)=
# Solvent Extraction Fundamentals

This is the core teaching chapter of the book. {index}`Solvent extraction <solvent extraction>` is how nearly
all rare earths are separated today, and everything in Part III is best read as
an attempt to do better than what is described here.

The mechanism is simpler than its industrial complexity suggests. An acidic
extractant dissolved in kerosene is a weak acid; when it coordinates a REE³⁺ ion
it releases three protons. That single fact makes the whole process reversible
by pH: raise the pH and metal moves into the organic phase, drop it and the
metal comes back out, leaving the extractant regenerated and ready to recycle.
The "pH swing" is the entire operating principle, and the +3 slope of log D
against pH is its signature — three protons released per metal ion, so a single
pH unit moves the distribution ratio by three orders of magnitude. (The same
stoichiometry read against log[H⁺] rather than pH gives a slope of −3; both
appear in the literature and they describe the same experiment.)

What makes rare earths hard is that this mechanism discriminates between
adjacent lanthanides only weakly. A {index}`separation factor` near 1.5 is normal.
Turning a factor of 1.5 into 99.99% purity is not a chemistry problem but a
staging problem, which is why the second half of this chapter is about
contactors, {index}`countercurrent <countercurrent cascade>` cascades, and phase ratios rather than about
molecules.

Along the way the chapter answers the questions that new researchers reliably
ask: why kerosene and not something else, what the salting-out agents are
doing there, and where the extractant goes over the course of a cycle (it stays
in the organic phase, and the reason it does is worked out below).

Two reviews cover the same ground at greater length. @xie2014critical is the
critical review of rare earth solvent extraction and is cited throughout this
chapter; @guo2026acidic is the recent one, aimed specifically at extraction from
acidic media and organised around mechanism, process control and outlook
together.

## Aqueous Phase Composition and Additives

### Role of pH Control

pH is the primary control variable in rare earth solvent extraction, and the
reason is the stoichiometry of the exchange itself. For an acidic extractant —
{index}`D2EHPA`, {index}`PC88A` — extraction is a cation exchange of three
protons for one trivalent metal ion [@xie2014critical]:

$$
\mathrm{REE^{3+}(aq)} + 3\,\mathrm{HL(org)} \rightleftharpoons \mathrm{REEL_3(org)} + 3\,\mathrm{H^+(aq)}
$$

with HL the extractant in its acidic form and REEL₃ the metal complex in the
organic phase. Everything in the rest of this chapter — the reversibility, the
reagent bill, the effluent problem, the difficulty of running a hundred stages
in series — follows from the fact that protons appear on the right-hand side.

Where the working pH window sits depends on how acidic the extractant is, and
the three organophosphorus reagents the industry runs on form an ordered series.
Replacing the P–O–C linkages of the phosphoric acid diester D2EHPA with P–C
bonds gives first the phosphonic acid monoester PC88A (also sold as P507 and
described in the literature as EHEHPA), and then the phosphinic acid
{index}`Cyanex 272`; acidity falls along that sequence, and the pH at which each
reagent will load and unload a rare earth climbs correspondingly
[@li2019development; @zhang2016rare]. That ordering is more useful in practice
than any table of windows, because it tells you what to reach for. A feed too
acidic to extract from with a given reagent is not usually fixed by raising the
pH — neutralising a
strong acid liquor costs base and risks hydrolysing the metal — but by moving to
a more acidic extractant. A loaded organic that will not strip without punishing
acid concentrations calls for a move the other way.

Concrete windows do exist, but they are conditional on the medium, the extractant
concentration and the loading, and they should be read that way. Working at
pilot scale with 10 vol% D2EHPA in kerosene on a liquor derived from an apatite
concentrate, @alemrajabi2022separation operated across pH 1.5–3.2 and stripped
with 3 M HCl. For lanthanum with PC88A in kerosene, @agarwal2020comparative
scanned initial pH from 1.5 to 7 and found 1 mol/L acid adequate to strip the
loaded organic. Neutral extractants sit outside this framework altogether:
{index}`TBP <TBP (tributyl phosphate)>` exchanges no protons, it solvates a
neutral nitrate complex, so it extracts from strongly acidic nitrate media and is
stripped by dilution with water rather than by acid.

### Aqueous Phase Additives and What They Are For

Three kinds of additive appear in a rare earth extraction liquor, and it is
worth being clear about which problem each one solves.

**Salting-out agents** are neutral salts added in bulk. They work by competing
for water: a concentrated salt solution ties up water molecules in hydration
shells, lowers the activity of free water, and so shifts every equilibrium that
consumes water to the right — including the dehydration of the aqueous metal ion
that has to happen before it can be coordinated by an extractant
[@rydberg2004solvent]. For neutral solvating extractants the effect is not merely
thermodynamic but structural, because the anion is part of the extracted species:
TBP takes up a rare earth as a neutral nitrate adduct, so a nitrate salt supplies
the ligands that build the extractable complex as well as suppressing hydration.
@matveev2018solvent studied precisely this system, extracting rare earths with
tri-n-butyl phosphate and tri-iso-amyl phosphate from nitrate media in the
presence of Ca(NO₃)₂. At equal molarity a divalent or trivalent cation salts out
more strongly than a monovalent one, because it immobilises more water per mole
and contributes more to ionic strength; that is why calcium and aluminium
nitrates appear where sodium chloride would not be enough. The counter-argument
is that aluminium is itself extractable by acidic organophosphorus reagents and
will compete for the extractant, and that everything added to the aqueous phase
has to leave in the raffinate. The saponification discussion later in this
chapter is the same trade made over a different cation.

**Buffers** hold the pH where the extraction reaction is trying to move it. The
useful ones are the ones whose pKa falls inside the extraction window: acetate
buffers about one unit either side of acetic acid's pKa near 4.8, which overlaps
the D2EHPA and PC88A windows, and citrate, whose three pKa values span roughly
3 to 6, buffers more broadly and also complexes rare earths in the aqueous
phase — a feature or a nuisance depending on what you are doing. Below about
pH 2 there is no useful carboxylate buffer, and pH is simply set by direct
addition of HCl or HNO₃ and held by continuous titration. This is a bench
technique. What replaces it at plant scale is the subject of the section on
{index}`saponification` below, and the reason it has to be replaced is the same
stoichiometry as before: extraction releases protons and drives the pH down,
stripping consumes them and drives it up, and neither drift is small.

**Complexing agents** are added to change selectivity rather than to change
capacity, by binding rare earths in the aqueous phase and so competing with the
extractant [@thiele2020tuning]. Hydroxycarboxylates such as lactate and citrate
are the classical choice and are the same chemistry that makes ion-exchange
[](#displacement-chromatography) work. Aminopolycarboxylates — EDTA,
DTPA — bind far more strongly and are used less for tuning lanthanide-lanthanide
selectivity than for holding back an impurity, {index}`thorium` and uranium in
particular, and are more often applied in pre-treatment than in the cascade
itself. The design freedom here is real but under-used: an aqueous complexant
whose size selectivity runs opposite to the extractant's adds its selectivity to
the extractant's rather than cancelling it, which is the point @thiele2020tuning
make for the light lanthanides.

### Ionic Strength Effects

All of the above act partly through ionic strength, which sets the activity
coefficients that the mass-action expressions of the next section quietly assume
away [@rydberg2004solvent]:

$$
I = \tfrac{1}{2} \sum_i c_i z_i^2
$$

At the ionic strengths a real liquor runs at — molar, not millimolar — activity
coefficients are far from unity and are not reliably predictable, which is why
equilibrium constants measured in one medium transfer poorly to another. The
practical consequences are two. First, distribution data must carry the medium
they were measured in or they mean very little; this is the same warning
@tanaka2021revaluating make about separation factors, discussed below. Second, an
extraction circuit is more reproducible at high ionic strength than at low,
because the activity coefficients are then at least slowly varying, which is one
reason concentrated chloride and nitrate liquors are the industrial norm.
[](#thermodynamics-of-extraction) takes up how badly the underlying
thermodynamics is actually known.

## Organic Phase: Why Kerosene?

### What the Diluent Has to Do

The organic phase is mostly diluent. A working solution is typically a few tens
of volume percent extractant, the balance diluent, plus a few percent of a phase
modifier where one is needed — the industrial example at the end of this chapter
uses 30 vol% D2EHPA with 10 vol% TBP, which is representative of the proportions
involved.

The diluent is not inert packing. It has a list of jobs, and the list is what
selects it:

- **It must let the phases separate under gravity.** That means a density well
  away from the aqueous phase. A rare earth chloride liquor carrying molar
  concentrations of salt sits near 1.1–1.2 g/mL; a light hydrocarbon sits near
  0.8; the difference of roughly 0.3 g/mL is what drives settling in every
  gravity-based contactor in this chapter.
- **It must separate quickly.** Settling velocity falls as viscosity rises, and
  settler volume — the single largest contributor to solvent inventory in a
  mixer-settler train — is set by how long the dispersion takes to break. That
  is the disengagement half of a trade whose other half is contacting time;
  [](#kinetics-and-mass-transfer) works the trade through.
- **It must not dissolve in water.** Anything that dissolves leaves in the
  raffinate, as both a reagent loss and a discharge.
- **It must be chemically inert** to strong acid and strong base at temperature,
  through years of continuous recycling.
- **It must not compete with the extractant.** A polar diluent solvates the
  metal-extractant complex, and in doing so changes the extraction equilibrium
  it was supposed to be neutral toward.
- **It must be safe to hold in bulk**, which for a plant holding tens of cubic
  metres of it means a flash point comfortably above the operating temperature.
- **It must be cheap**, for the same reason.

### Why Kerosene

Kerosene — the roughly C₉–C₁₆ petroleum distillate cut — meets that list better
than the alternatives, and the reasons are worth spelling out because they are
the reasons a research paper's choice of n-dodecane does not automatically
transfer to a plant.

Its polarity is right. An alkane mixture has a dielectric constant near 2, which
is low enough that the diluent does not coordinate the metal or hydrogen-bond to
the extractant's phosphoryl oxygen, and yet the extractants themselves — large
branched alkyl esters — are entirely soluble in it. That the surrounding medium
is not neutral is not a hypothetical concern: @dewulf2022effect found extraction
by a solvating extractant to depend strongly on the polarity, donor strength and
hydrogen-bonding capability of the organic medium around it. Kerosene's
contribution is to be as close to nothing as a liquid can be.

Its density and viscosity are right, which is the same statement as saying the
phases disengage. At roughly 0.8 g/mL against a salt-loaded aqueous phase near
1.1–1.2, the density difference is large by liquid-liquid extraction standards,
and the low viscosity of a light hydrocarbon means the dispersion breaks quickly
rather than persisting as a stable band.

It is safe and cheap enough to hold in bulk. A petroleum refinery fraction costs
what fuel costs, and its flash point is high enough that it need not be handled
the way a light alkane such as hexane must. Neither statement is true of the
specialist solvents that outperform it on any single property.

And it is stable. Kerosene does not hydrolyse in acid or base and does not react
with the extractants, so the organic inventory can be recycled indefinitely; what
limits its service life is accumulated degradation product from the *extractant*
and entrained crud, both of which are removed by periodic washing rather than by
replacing the diluent.

**Alternatives, and what they are for.** *n*-Dodecane is a pure compound with
essentially kerosene's properties and none of its batch-to-batch variability,
which is why research papers use it and plants do not — a defined composition is
worth paying for when you are measuring an equilibrium constant and worth nothing
when you are running a cascade. Branched-alkane products sold under trade names
such as Isopar are narrow, low-odour, higher-flash-point cuts used where
workplace exposure or product contamination matters.
{index}`Ionic liquids <ionic liquids>` and supercritical CO₂ are research
diluents rather than alternatives at present, the first because of cost and
viscosity and the second because it requires pressure equipment; both are treated in
[](#membranes-mofs-and-emerging-approaches) and
[](#coacervates-and-aqueous-biphasic-systems), where the argument for them is not
that they are better diluents but that they change the separation chemistry.

### Phase Modifiers

At high extractant concentration or high metal loading the organic phase can
split into two: a dense, extractant-rich third phase separates out and the
circuit stops working. The metal-extractant complexes are polar species held in a
non-polar medium, they aggregate, and beyond some loading the aggregates cease to
be soluble. The fix is a modifier — a small addition of something more polar than
the diluent that solvates the aggregates and keeps them dispersed
[@rydberg2004solvent]. TBP is the usual choice in rare earth circuits, at a few
to ten volume percent, and it is the reason the "30% D2EHPA + 10% TBP" recipe
recurs; long-chain alcohols such as 1-decanol and 1-dodecanol do the same job and
also lower interfacial viscosity, which improves coalescence and suppresses
stable emulsions. The modifier is a cost and a complication — one more component
to analyse, degrade and lose — so it is added when third-phase formation or slow
disengagement demands it, not by default.

(ph-swing-mechanism-for-phase-transfer)=
## pH Swing Mechanism for Phase Transfer

### Extraction Step: Aqueous → Organic

Acidic organophosphorus extractants are hydrogen-bonded dimers in a non-polar
diluent, so the reaction written earlier is more accurately
[@xie2014critical; @tanaka2021revaluating]:

$$
\mathrm{REE^{3+}(aq)} + 3\,\mathrm{(HL)_2(org)} \rightleftharpoons \mathrm{REE(HL_2)_3(org)} + 3\,\mathrm{H^+(aq)}
$$

where (HL)₂ is the dimeric extractant and REE(HL₂)₃ the extracted tris-complex.
The equilibrium constant is

$$
K_\mathrm{ex} = \frac{[\mathrm{REE(HL_2)_3}]_\mathrm{org}\,[\mathrm{H^+}]_\mathrm{aq}^{3}}
                     {[\mathrm{REE^{3+}}]_\mathrm{aq}\,[\mathrm{(HL)_2}]_\mathrm{org}^{3}}
$$

and the quantity actually measured is the {index}`distribution ratio`
[@iloeje2019gibbs]

$$
D = \frac{[\mathrm{REE}]_\mathrm{org}}{[\mathrm{REE}]_\mathrm{aq}}
$$

which, taking logarithms of the mass-action expression, gives the working
relation of the whole chapter:

$$
\log D = \log K_\mathrm{ex} + 3 \log [\mathrm{(HL)_2}]_\mathrm{org} + 3\,\mathrm{pH}
$$

### pH Dependence: The "pH Swing"

The last term is the pH swing. Because three protons are released per metal ion,
log D moves three units for every unit of pH [@tanaka2021revaluating]:

$$
\frac{\partial (\log D)}{\partial\, \mathrm{pH}} \approx +3
\qquad
\left( \text{equivalently,} \ \frac{\partial (\log D)}{\partial \log [\mathrm{H^+}]} \approx -3 \right)
$$

That exponent is the {index}`slope-3 dependence` this book refers to at several
later points, so it is worth naming here. Plot log D against pH for an acidic
organophosphorus extractant and the result is a straight line of slope +3; the 3
is not fitted, it is the stoichiometric coefficient, one for each proton the
tris-complex releases. The relation runs in both directions. Used forward it is
the design lever below. Used backwards it is a diagnostic: the measured slope of
a log D-pH plot counts the protons exchanged, so a slope near 3 is evidence that
the extracted species really is REE(HL₂)₃, and a slope that comes out near 2, or
that drifts with loading, says that some other species — a partly protonated
complex, an adduct with the diluent, a second extractant in the mixture — is
carrying part of the metal [@xie2014critical]. Every use of "slope-3" later in
this book means this line and this stoichiometry.

A single pH unit therefore moves the distribution ratio by a factor of a
thousand, in either direction. That is an unusually steep lever for a chemical
process, and it is what makes the same reagent do both halves of the cycle: the
metal is loaded at one pH and unloaded at another, with no change of chemistry in
between.

**Illustrative slope-3 behaviour**, drawn for a lanthanide with pH₁/₂ = 2.5 at
equal phase volumes. The numbers are the mass-action expression evaluated, not
measurements:

| pH  | log D | D     | % Extraction |
|-----|-------|-------|--------------|
| 1.5 | -3.0  | 0.001 | 0.1%         |
| 2.0 | -1.5  | 0.032 | 3%           |
| 2.5 | 0.0   | 1.0   | 50%          |
| 3.0 | 1.5   | 32    | 97%          |
| 3.5 | 3.0   | 1000  | 99.9%        |

Half a pH unit takes the system from 3% to 97% extraction. That steepness is
what makes the pH swing work, and it is also why pH control is the single most
demanding part of running a cascade. [](#fig-logd-vs-ph) draws the same
relation for two neighbouring lanthanides at once, which is where the steepness
stops being an unmixed blessing: the slope is +3 for both of them, and the two
lines are parallel.

### The Extraction Cycle

The cycle is one argument, not four operations, and it is easiest to follow as a
single pass of the organic phase around the loop.

**Forward transfer.** Aqueous feed meets the organic phase somewhere in the
D2EHPA/PC88A window — the worked example below uses pH 3.0 — and the metal moves
into the organic. In doing so it releases protons, and the pH of the aqueous
phase falls; because of the slope-3 dependence, a drift of even a few tenths of a
pH unit is a substantial loss of D, so the pH has to be held. The material
balance that says how much holding is required is exact and follows from the
stoichiometry alone:

$$
n(\mathrm{H^+})_\text{released} = 3\, n(\mathrm{REE})_\text{extracted} = n(\mathrm{base})_\text{required}
$$

Three equivalents of base per mole of rare earth moved. That is not a detail;
it is one of the two largest reagent costs in a separation plant and, as the
saponification section shows, the origin of its worst effluent problem.

**Scrubbing.** The loaded organic is next washed with an aqueous stream before it
is stripped. Two entirely different operations go by this name and conflating
them causes confusion. Washing co-extracted Fe³⁺, Al³⁺ or Ca²⁺ off the organic is
impurity removal, and it is a minor operation — iron in particular binds D2EHPA
more strongly than any rare earth and has to be removed upstream rather than
scrubbed off here ([](#from-ore-to-feed-solution)). The scrubbing that matters in
a rare earth cascade is REE-on-REE scrubbing, and it is treated below as part of
fractional extraction, because it is not an auxiliary step but the liquid-liquid
analogue of reflux.

**Reverse transfer.** Stripping runs the same equation backwards:

$$
\mathrm{REE(HL_2)_3(org)} + 3\,\mathrm{H^+(aq)} \rightarrow \mathrm{REE^{3+}(aq)} + 3\,\mathrm{(HL)_2(org)}
$$

Contacting the loaded organic with strong acid raises [H⁺] by orders of
magnitude, and the slope-3 dependence collapses D by three orders of magnitude
per pH unit. That is why stripping is fast, why it is done with acid rather than
by any change of extractant, and why it regenerates the extractant in its acidic
form ready to recycle. For PC88A loaded with lanthanum, @agarwal2020comparative
found 1 mol/L acid adequate for effective stripping; the pilot-scale D2EHPA
system of @alemrajabi2022separation used 3 M HCl. Complete stripping is
nonetheless staged, because a single contact leaves the organic in equilibrium
with the strip liquor it has just loaded — the same arithmetic as for extraction,
run in the other direction, and quantified by the stripping factor in the phase
ratio section below.

**Recycle.** The stripped organic returns to the head of the cascade. Nothing
about the extractant has changed; what has happened is that three protons were
picked up in the strip section and released in the extraction section, and the
metal made the opposite journey.

### Where Do Extractants Go?

New researchers reliably ask where the extractant ends up, and the answer is
that it stays in the organic phase [@rydberg2004solvent; @xie2014critical]. The
reason is worth working out rather than asserting, because it is the same
argument that says what the makeup rate is set by.

D2EHPA and PC88A are large branched dialkyl esters of phosphorus acids. They are
surfactants, not salts, and their solubility in water is at the parts-per-million
level, while their concentration in the organic phase is a few tens of volume
percent — hundreds of thousands of parts per million. The partition coefficient
between the phases is therefore enormous, and the fraction of the inventory that
dissolves into the aqueous phase at each contact is correspondingly tiny. What
actually consumes extractant is not dissolution but chemistry: slow hydrolysis of
the ester linkages, oxidative and, in nuclear service, radiolytic degradation.
The degradation products are themselves surface-active and accumulate, which is
why an operating circuit carries a carbonate wash to strip them out rather than
relying on dilution.

TBP is the exception among common reagents. It is appreciably more water-soluble
than the acidic organophosphorus extractants, enough that a TBP circuit needs an
organic-recovery step on its aqueous effluent that a D2EHPA circuit does not.

The metal, meanwhile, does cross. The picture to hold is that the extractant is
dissolved in the organic phase and never leaves it; the reaction happens at or
near the interface; the metal-extractant complex forms on the organic side and
stays there; and what actually traverses the boundary is the aqueous metal ion in
one direction and protons in the other. The rate-limiting step in that sequence
is usually diffusion on the aqueous side rather than the complexation reaction,
which is fast — a fact that matters for contactor design, because it means
interfacial area, not chemistry, sets how long a stage has to be contacted.

**Loading limits.** The extractant is a finite, shared resource, and this is the
constraint that most often bites in practice. Three monomers are consumed per
REE³⁺. A 30 vol% D2EHPA solution is about 0.9 M in monomer and therefore
saturates near 0.3 M rare earth; circuits are run at a fraction of that, because
approaching saturation raises the organic viscosity, invites third-phase
formation, and — since the elements compete for the same ligand — destroys the
selectivity the cascade was built on. Where the operating loading sits is a
design choice, and the industrial example below runs at about half of capacity.

### Selectivity Between REEs

The convenient way to compare elements is not through D, which depends on
conditions, but through the pH at which D = 1 [@tanaka2021revaluating;
@xie2014critical]. Setting log D = 0 in the working relation above,

$$
\mathrm{pH}_{1/2} = -\tfrac{1}{3}\left( \log K_\mathrm{ex} + 3 \log [\mathrm{(HL)_2}] \right)
$$

A *lower* pH₁/₂ means a more strongly extracted element, since it reaches
D = 1 while the aqueous phase is still more acidic.

**The order across the series.** For acidic organophosphorus extractants —
D2EHPA, PC88A, Cyanex 272, the workhorses of the industry — the distribution
ratio rises monotonically from La to Lu, and pH₁/₂ falls correspondingly
[@nash1993basic]. The smaller, more charge-dense heavy ion binds the phosphoryl
oxygens more tightly.
So in any cascade built on these reagents the heavies load into the organic
phase and the lights report to the raffinate. Yttrium is the exception that
matters industrially: it has no 4f electrons and sits by size near Ho, but its
extraction behaviour varies with the extractant and it can fall anywhere from
Dy to Er in the sequence, which is what makes Y/Ho separations awkward.

**What the gap is worth.** Because log D moves with slope +3 for both members of
a pair, the separation factor follows directly from the gap between their
half-extraction pH values:

$$
\beta = 10^{\,3\,\Delta \mathrm{pH}_{1/2}}, \qquad
\Delta \mathrm{pH}_{1/2} = \mathrm{pH}_{1/2}(\mathrm{REE}_1) - \mathrm{pH}_{1/2}(\mathrm{REE}_2)
$$

A gap of 0.1 pH units is a separation factor of 2; a gap of 0.2 is a factor of 4.
This is why pH control at the hundredth of a unit is a real engineering
requirement and not a counsel of perfection. Run the same arithmetic at the value
that actually governs an adjacent light-lanthanide pair, β = 1.5, and the gap is
Δ pH₁/₂ = (log 1.5)/3 = 0.06 pH units — the whole of the chemistry the industry
is built on, drawn to scale in [](#fig-logd-vs-ph).

:::{figure} ../figures/03-logd-vs-ph.svg
:name: fig-logd-vs-ph
:width: 100%

Two neighbouring lanthanides under an acidic organophosphorus extractant. The
lines are the mass-action expression `log D = log Kₑₓ + 3 log[(HL)₂] + 3 pH`
evaluated for β = 1.5, not fitted data; the constants are chosen only to put
D = 1 in the middle of the panel. The triangle is drawn to scale: one pH unit
buys three decades in D. The inset is also at true scale, not exaggerated —
that is its point. The horizontal separation between the two elements,
Δ pH₁/₂ = (log β)/3 = 0.06 pH units, is invisible in the main panel, which is
why the split has to be won by staging rather than by chemistry. Drawn from
`tools/figures/fig_logd_vs_ph.py`.
:::

**Typical separation windows.** Adjacent light-lanthanide pairs are commonly
quoted near β = 1.5-2, which by the relation above is a window of
Δ pH₁/₂ = (log β)/3 ≈ 0.06-0.10 pH units. That is the value
[](#why-rare-earths-are-hard-to-separate) uses and the one every stage count in
this chapter is built on. Windows widen where the lanthanide contraction has
had more room to work -- across a gap of several atomic numbers rather than
between neighbours -- and the largest factors quoted in the literature are for
such pairs, not for the adjacent ones that actually set the size of a plant.

A caution about quoted values themselves. @tanaka2021revaluating recalculated
the extraction equilibria of La, Ce, Pr, Nd, Sm, Eu, Tb, Dy and Y with EHEHPA
(PC-88A), correcting for the nonideality of the organic phase, and then
compared the separation factors that fall out of those constants against the
values already in the literature. The two disagreed, and the disagreement grew
with the difference in atomic number between the pair: a published separation
factor carries its measurement conditions with it, and pairs quoted from
different studies are frequently not comparable. Treat any single tabulated β
as conditional on the medium, the extractant concentration, the loading and the
temperature it was measured at.

There is also a physical reason not to expect the gaps to be large. The ion that
has to be extracted is not a bare cation but a hydrated one, and the same
contraction in ionic radius that strengthens binding to the extractant also
strengthens binding to water. @li2020hydration make this quantitative: hydration
counteracts the separation of the lanthanides, so a large part of the
selectivity built into a ligand is paid back to the aqueous phase before it can
be collected. Designing an extractant is therefore not a matter of maximising
affinity but of maximising the *difference* between two affinities that a
competing solvation equilibrium is working to erase.

### Temperature Effects

**The sign of the temperature effect is system-specific and should not be
assumed.** For lanthanum with PC88A in kerosene over 25-55 °C,
@agarwal2020comparative found extraction *increased* slightly with temperature
-- weakly endothermic, not exothermic. Enthalpies for acidic organophosphorus
extraction of the lanthanides are generally small, so temperature is a weak
lever on the equilibrium compared with pH, and a circuit that runs warm usually
does so for viscosity and phase-disengagement reasons rather than
thermodynamic ones.

**Temperature dependence** follows the van 't Hoff form:

$$
\log K_\mathrm{ex} = \frac{-\Delta H}{2.303\,RT} + \frac{\Delta S}{2.303\,R}
$$

The scale of RT is worth holding on to when reading enthalpies of extraction:
at 298 K, RT is 2.48 kJ/mol, so the free-energy difference corresponding to
β = 1.5 is RT ln 1.5 ≈ 1.0 kJ/mol. That is the energy budget the whole industry
operates inside, and [](#the-energy-scale-of-selectivity) is about what it means
for ligand design.

**Operational implications.** Extraction is generally run at ambient
temperature; stripping is often run warmer, which speeds phase disengagement and
reduces organic viscosity whatever it does to the equilibrium. Extractant classes
other than the acidic organophosphorus reagents behave differently:
@khoshoei2025crown reviews the thermodynamics of crown ether extractants, where
the enthalpic and entropic contributions to selectivity are both larger and
better characterised.

## Liquid-Liquid Contactor Design

### Choosing a Contactor

Every contactor does the same two things in some order: it creates interfacial
area so the metal can cross, and it then destroys that area again so the phases
can be separated and sent on. The families differ in how they do each half, and
almost every engineering property that matters — residence time, solvent
inventory, footprint, startup time, tolerance of dirt — falls out of those two
choices. @zhang2016equipment and @qi2018equipment are the equipment-side
treatments written specifically for rare earths.

**{index}`Mixer-settlers <mixer-settler>`** do the two jobs in two connected
boxes: an agitated mixer that disperses one phase into the other, and a
quiescent settler where gravity pulls the dispersion apart again. Because gravity settling of a fine dispersion is
slow, the settler is the larger of the two vessels, often by a wide margin, and
it dominates both the footprint and the solvent inventory of the train. That is
the standing criticism of the design and it is entirely fair. What is bought with
it is robustness of an unusual kind. A mixer-settler tolerates solids and crud
that would foul anything with a small passage in it; it can be stopped and
restarted; it scales by getting bigger rather than by getting more numerous; and,
decisively, every stage is a vessel with a liquid level in it that can be
sampled, assayed and reasoned about individually. On a train of tens to hundreds
of stages splitting a pair with β near 1.5, the ability to walk the cascade and
find the stage that is misbehaving is worth more than compactness. That is why
mixer-settlers are the industry standard despite being worst on almost every
other axis, and the capability is real rather than notional: @dewulf2022separation
took a heavy rare earth hydroxide concentrate from mining waste and, in sixteen
stages of laboratory mixer-settlers, raised a thulium group from 34% to 99.8%
purity and a dysprosium group from 54% to 98.7% in the same operation.

The cost of the settler volume is paid twice. Once as capital and inventory —
the organic held up in a hundred settlers is extractant that has been bought and
is not extracting — and once as time. A cascade with large holdup has a long time
constant, so it takes a long time to reach steady state after a startup or a
disturbance, and during that time it is producing off-specification product. The
dynamics of rare earth mixer-settler cascades have accordingly been studied as a
problem in their own right [@wichterlova1999dynamic], and the dynamic cascade
models in [](#process-modeling-and-optimization) exist largely because of it.

**Pulsed columns** stack the contacting vertically. A single column packed with
perforated plates or with discs and doughnuts does the work of several
mixer-settler stages on a fraction of the floor area, and the agitation is
supplied by pulsing the whole liquid inventory from an external pump, so there
are no moving parts inside the column at all. The gains are footprint and
mechanical simplicity, and in a nuclear context also containment: nothing has to
penetrate the vessel. What is given up is the property that made the
mixer-settler attractive. A column has no stages to sample. Its performance is
described by a height equivalent to a theoretical stage, which is not a design
constant but an outcome of the hydrodynamics — dispersed-phase holdup and drop
size, which depend on the pulse in ways that are still being characterised.
@li2025extraction is the current rare earth example, a pulsed disc-and-doughnut
column run on NdFeB acid leachate with saponified PC-88A: dispersed-phase holdup
fell and then rose again as pulse intensity increased, while drop diameter fell
monotonically, and the height of a mass transfer unit came out near two metres.
A stage height that responds non-monotonically to the main control handle is an
uncomfortable thing to put many of in series, and it is a large part of why
columns are common in nuclear reprocessing and rare in rare earth separation.

**Centrifugal extractors** replace gravity with a few hundred times gravity.
Mixing and separation happen in the same spinning rotor, so the settler
disappears entirely and with it most of the inventory and the footprint.
@maertens2023design, describing the design of laboratory-scale annular
centrifugal contactors, state the appeal exactly: high throughput at short
residence times, small liquid holdup, and a small footprint. Residence time falls
from minutes to seconds, and startup from days to minutes — which for a
laboratory or a pilot campaign is the whole argument, since a mixer-settler
train may spend longer approaching steady state than running at it.

The short residence time is more than an economy. It can be a separation
mechanism in its own right: @duan2015separation separated Nd³⁺ from Fe³⁺ in an
annular centrifugal contactor by deliberately *not* reaching equilibrium,
exploiting the difference in extraction rate rather than the difference in
equilibrium constant. That is a lever nothing else in this chapter has, because
everything else here is thermodynamic. Against it stands the reason the industry
has not adopted them: a centrifugal extractor is a machine, with a rotor, a
motor, bearings and seals, and a rare earth cascade needs a great many stages of
it. Capital cost and maintenance scale with stage count in a way that tankage
does not, solids are not tolerated, and the drivers that made nuclear
reprocessing pay for them — inventory as a criticality and safeguards concern,
and solvent degradation that accumulates with residence time — simply do not
apply to rare earths. The comparison is not "compact versus bulky" but "a hundred
machines versus a hundred tanks", and for a commodity separation the tanks win.

**Membrane contactors** take the argument to its limit by never dispersing the
phases at all. The two liquids flow on opposite sides of a microporous membrane
and meet only at the interfaces pinned in its pores, so the interfacial area is
set by the fibre geometry rather than by agitation, and no coalescence step is
needed because there is nothing to coalesce. Emulsions and entrainment, the two
chronic operating problems of every design above, cannot occur. The price is that
an interface which no longer has to be made now has to be *maintained*, and the
failure modes are all failures of that maintenance: pore wetting, displacement of
the organic film, and chemical degradation of the membrane. @alemrajabi2022separation
is the most informative rare earth test at scale — a hollow-fibre module of 8 m²
mass transfer area with 10 vol% D2EHPA in kerosene and 3 M HCl strip, comparing a
plain supported liquid membrane against renewal and emulsion-pertraction
configurations. The plain configuration was the most selective and the least
durable: its performance decayed rapidly with time, while the renewal and
pertraction configurations held up much better, with gel formation identified as
an important degradation mechanism. That is the state of the technology — real
selectivity, unsettled durability — and [](#membrane-separation-technologies)
takes it up in full.

The shape of the comparison, then, is this. On residence time, inventory and
footprint the ranking runs membrane and centrifugal at one end and mixer-settlers
at the other, and it is not close. On robustness, observability, tolerance of a
dirty feed and cost per stage the ranking is exactly reversed. Rare earth
separation is a low-margin commodity operation that needs an enormous number of
stages of a thermodynamically marginal separation on feeds that are never clean,
which weights the second list far above the first. The alternatives are better on
paper on the axes that a laboratory notices and worse on the axes that a plant
does.

### Phase Ratio and Material Balance

The distribution ratio alone does not tell you how much metal a stage moves.
That depends on how much of each phase is present, and the quantity that
combines the two is the **{index}`extraction factor`** [@rydberg2004solvent]:

$$
E = D \times (O/A)
$$

`E` is the ratio of metal in the organic phase to metal in the aqueous phase at
equilibrium, counting volumes. The fraction of the entering metal that a single
equilibrium stage transfers is then

$$
\text{fraction extracted} = \frac{E}{1 + E}
$$

and the same algebra run backwards gives the stripping factor
`S = (A/O)_strip / D_strip` with `fraction stripped = S / (1 + S)`.

A large `D` bought at a small `O/A` is not a large `E`. This is the most common
arithmetic error in reading extraction data:

**Example**:

- Extraction: D = 10 at O/A = 1/3 → E = 10/3 = 3.3 → **77% extracted per stage**
- Stripping: D_strip = 0.1 at A/O = 1/5 → S = (1/5)/(0.1) = 2 → **67% stripped
  per stage**

Neither is the ~95% a reader might assume from `D = 10` and `1/D_strip = 10`
alone. Getting to 99%+ is what the extra stages are for.

**Concentration factor**. Running the organic lean (small `O/A`) concentrates
the metal on extraction; running the strip liquor lean (small `A/O`) concentrates
it again. Both enrichments are capped by the fraction actually transferred:

$$
\mathrm{CF} = \frac{[\mathrm{REE}]_\text{product}}{[\mathrm{REE}]_\text{feed}}
     = (A/O)_\text{extraction} \times (O/A)_\text{stripping} \times f \times g
$$

where `f` and `g` are the overall extracted and stripped fractions. For the
numbers above, taken as single stages: 3 × 5 × 0.77 × 0.67 ≈ **7.7×**. Note the
ratios enter inverted relative to how they are written in the extraction and
stripping steps — a lean organic phase concentrates *because* there is little of
it.

**The ceiling on `O/A` is the extractant, not the hydraulics.** Three monomers of
an acidic organophosphorus extractant are consumed per REE³⁺. A 30 vol% D2EHPA
solution is about 0.9 M in monomer, so it saturates near 0.3 M REE and is run at
half that. A phase ratio that would load the organic past saturation does not
give the `D` the equilibrium data predict, no matter what the pH is.

(countercurrent-cascade-design)=
### Countercurrent Cascade Design

**Principle**: Multiple extraction stages in series maximize REE transfer [@rydberg2004solvent].

#### McCabe-Thiele Diagram
Graphical method for determining stage requirements:

**Construction**:

1.  Plot equilibrium curve: y\* = f(x) where y = $[\mathrm{REE}]_\mathrm{org}$, x = $[\mathrm{REE}]_\mathrm{aq}$
2.  Draw operating line: y = (A/O)x + y₀
3.  Step off stages between equilibrium curve and operating line

**Parameters**:

- A/O = aqueous/organic flow ratio
- Slope of operating line = A/O
- Number of graphical steps = number of theoretical stages

[](#fig-mccabe-thiele) is that construction, drawn on this chapter's own
numbers.

:::{figure} ../figures/03-mccabe-thiele.svg
:name: fig-mccabe-thiele
:width: 100%

The McCabe-Thiele construction for the worked example below: `D` = 10 at
`O/A` = 1/3, an 0.05 M rare earth feed, 99.9% recovery. The staircase is
stepped between the operating line and the equilibrium curve, and each tread is
one theoretical stage. Nothing here is measured. The equilibrium curve is a
saturating form given this chapter's initial slope (`D` = 10 as the loading goes
to zero) and this chapter's capacity (0.30 M, from three extractant monomers per
REE³⁺ in an 0.9 M monomer solution); it stands for the *shape* a loaded
extractant follows, not for any isotherm anyone measured. Two things follow from
that shape that the algebra of the next section cannot say. **First, curvature
costs stages**: the straight line the Kremser equation assumes gives six, the
curve gives seven, and the gap widens the harder the organic is loaded.
**Second, there is a phase ratio past which no number of stages is enough.**
Raise `A/O` to 3.75 and the operating line touches the equilibrium curve at the
feed end; the driving force there goes to zero and the staircase can no longer
be closed. That is the {index}`pinch <pinch point>`, and it is the graphical
statement of the point made above — the ceiling on the phase ratio is set by how
much metal the extractant can hold, not by the pumps. The inset is the third
thing worth seeing: the stages are not evenly spaced. Two contacts move most of
the metal and the remaining four are spent on the last two percent, which is the
shape of every recovery duty and the reason recovery targets are expensive at
the margin. Drawn from `tools/figures/fig_mccabe_thiele.py`.
:::

This construction answers a *recovery* question — how many stages to strip one
solute out of one aqueous stream — and nothing else. It is drawn for a single
transferring species; it says nothing about which of two lanthanides ends up
where. Both questions have to be answered, and they have different answers.

#### How Many Stages for Recovery? The Kremser Equation
The graphical construction has an algebraic counterpart that is faster to use
and easier to check. If the equilibrium line is straight over the range of
interest, `y* = m x` with `m` the distribution ratio `D`, and if the phase flows
are constant through the train, the stage-by-stage material balance sums in
closed form. The result is the {index}`Kremser equation`, the same relation that
sizes absorbers and strippers throughout separations practice
[@rydberg2004solvent].

The notation matters, so state it. Take the aqueous phase to be the one losing
metal, and let

- `x_in` = metal concentration in the aqueous feed entering the cascade;
- `x_out` = metal concentration in the raffinate leaving it;
- `y_in` = metal concentration in the organic entering the cascade — zero for
  fresh solvent, non-zero when incompletely stripped organic is recycled;
- `m = D`, the slope of the equilibrium line; and
- `E = m (O/A) = D (O/A)`, the extraction factor defined above, taken constant
  through the cascade.

Then for `N` ideal countercurrent stages,

$$
\frac{x_\mathrm{in} - y_\mathrm{in}/m}{x_\mathrm{out} - y_\mathrm{in}/m}
   = \frac{E^{N+1} - 1}{E - 1}
$$

and inverting for the stage count,

$$
N = \frac{\ln\left[
      \dfrac{x_\mathrm{in} - y_\mathrm{in}/m}{x_\mathrm{out} - y_\mathrm{in}/m}
      \left(1 - \dfrac{1}{E}\right) + \dfrac{1}{E}
    \right]}{\ln E}
$$

Three checks. At `N = 1` the first expression gives `x_out/x_in = 1/(1 + E)`
for fresh solvent — the single-stage result of the previous section, recovered.
At `E = 1` both expressions are indeterminate; the limit is
`(x_in − y_in/m)/(x_out − y_in/m) = N + 1`, so the raffinate falls only as
`1/(N + 1)`. Stages then buy recovery arithmetically rather than geometrically,
and 99.9% recovery would take 999 of them — which is why nobody runs a cascade
at `E = 1` for recovery duty. At `E >> 1` the `1/E` terms drop out and
`N ≈ ln(x_in/x_out) / ln E`: every stage divides the aqueous concentration by
`E`, the geometric behaviour the McCabe-Thiele staircase draws.

**Worked example, using this chapter's own numbers.** Take `D = 10` at
`O/A = 1/3`, so `E = 3.33`, with fresh organic (`y_in = 0`). One stage extracts
77%. For 99.9% recovery, `x_in/x_out = 1000`:

$$
\begin{aligned}
N &= \frac{\ln[1000 \times (1 - 0.30) + 0.30]}{\ln 3.33} \\
  &= \frac{\ln(700.3)}{1.204} \\
  &= 5.4 \ \rightarrow \ 6 \ \text{theoretical stages}
\end{aligned}
$$

Six stages, and at 100% stage efficiency — and six is the number the staircase
in [](#fig-mccabe-thiele) also reaches when it is stepped off against the
straight line, which is the check that the two methods are the same calculation.
Stepped against a curve that saturates, the same duty takes seven. The extra
stage is the price of the one assumption the closed form makes, and it grows
with loading: `m = D` is a constant only while the extractant is far from full,
and the Kremser count is therefore a floor rather than an estimate. Design
practice is to take the algebra for the scoping number and the diagram for the
number you build to.

That is the kind of duty a short
extraction train is sized for: one solute, a large `D`, a target expressed as
percent recovered. It is not a separation duty, and none of it carries over to
the problem of splitting two neighbouring lanthanides.

#### How Many Stages for Separation? A Fenske Bound
When two rare earths with separation factor β are to be split so that one is
pure at the extract end and the other pure at the raffinate end, the governing
estimate is not Kremser but Fenske's — the distillation result for the minimum
number of equilibrium stages at total reflux. It transfers to a fractional
extraction cascade unchanged, because the underlying algebra is the same: a
constant relative separation applied stage after stage.

$$
N_\mathrm{min} = \frac{\ln\left[
    \dfrac{x_P}{1 - x_P} \cdot \dfrac{1 - x_R}{x_R}
  \right]}{\ln \beta}
$$

`x_P` is the mole fraction of the more-extractable element in the product taken
from the extract end; `x_R` is that same element's mole fraction in the
raffinate; β is the pair's separation factor. Each bracketed term is a ratio of
wanted to unwanted, so the logarithm's argument is the product of the two
end-point enrichments — the separation job is shared between the two ends, and
tightening either end costs stages.

Put in the numbers this book keeps returning to. Demand 99.99% at both ends
(`x_P = 0.9999`, `x_R = 0.0001`) of a pair with β = 1.5:

$$
N_\mathrm{min} = \frac{\ln(9999 \times 9999)}{\ln 1.5} = \frac{18.42}{0.405} = 45 \ \text{stages}
$$

Forty-five, and that is a floor, not a design. `N_min` assumes total reflux, a
strictly binary feed, and equilibrium in every stage. A working circuit has
none of those: it runs at **finite reflux**, since the scrub and strip returns
that play the role of reflux are finite streams that cost reagent and pumping;
it splits a feed of eight or ten lanthanides rather than two, so each cut
carries the others through it; and its mixers approach equilibrium without
reaching it, which is why cascade models carry an empirical stage efficiency
that is fitted rather than predicted ([](#process-modeling-and-optimization)).
Installed stage counts are accordingly larger than `N_min`, and the published
model-based designs bear that out: @dewulf2022separation needed sixteen
mixer-settler stages for a *group* split of heavy rare earths, and the
optimization study of @srivastava2023design settled on loading-scrubbing-stripping
combinations totalling around twenty-three stages for one clean cut
([](#process-modeling-and-optimization)). That is the derivation behind the "hundreds of stages" of
[](#why-rare-earths-are-hard-to-separate): it follows from β ≈ 1.5 and the
purity specification, and is not an assertion about industrial habit.

The sensitivity is worth seeing, because it explains what plants actually do.
Relaxing both ends to 99.9% drops `N_min` from 45 to 34. Doubling β to 3.0 — the
gap between an adjacent pair and a pair two apart — drops it to 17. Choosing a
better extractant and choosing a less demanding purity target are the two levers,
and the logarithm means neither one is dramatic. The lower panel of
[](#fig-cascade) draws both cases: plotted against stage number on a log-ratio
axis the profile is a straight line whose slope is log β, so the stage count is
read off as a length, and the whole of what β buys is the difference between two
slopes.

#### Fractional Extraction: Extract, Scrub and Strip
A recovery cascade has the aqueous feed entering at one end. A **{index}`fractional
extraction`** cascade — the configuration every rare earth separation plant
actually runs — has it entering somewhere in the middle, which is what splits the
train into two sections that do different jobs ([](#fig-cascade)).

:::{figure} ../figures/03-cascade.svg
:name: fig-cascade
:width: 100%

**Above**, the fractional extraction cascade — a schematic of the configuration
described here, not of any particular plant. The phases run counter to each
other, organic left to right and aqueous right to left, so the raffinate leaves
the left end and the loaded organic the right; the feed enters partway along,
and the feed point is what divides the extraction section from the scrub
section. The scrub liquor is drawn as what it is, a split of the cascade's own
strip product. The two curved arrows are the sections' jobs: on the left the
more-extractable element pulled into the organic, on the right the co-extracted
less-extractable element displaced back off the extractant and returned toward
the feed. **Below**, the stage profile that goes with it, drawn from the Fenske
relation rather than measured: at total reflux each equilibrium stage multiplies
the ratio of the two elements by β, so on a log-ratio axis the profile is a
straight line of slope log β and the stage count is read off as a length. The
endpoints are this chapter's specification of 99.99% at both ends, and the two
slopes give the 45 and 17 stages derived above — floors, for the reasons given
there. The feed stage is where the profile crosses 50/50, which for an equimolar
binary feed is the middle of the train. Drawn from
`tools/figures/fig_cascade.py`.
:::

In the **extraction section**, between the feed point and the raffinate outlet,
the organic flowing counter to the aqueous pulls the more-extractable element
(for acidic organophosphorus reagents, the heavier lanthanide) out of the
aqueous; what survives to the raffinate end is progressively purer in the
*less*-extractable element. In the **scrub section**, between the feed point and
the loaded-organic outlet, an aqueous stream washes the loaded organic on its way
out, displacing the less-extractable element back off the extractant by mass
action and returning it toward the feed. What makes this work is the choice of
scrub liquor: not acid, and not a buffer, but a portion of the cascade's own
strip product — the purified more-extractable element, returned to the head of
the train [@xu1985theory]. @banda2015separation is a worked example of the
arrangement, separating Nd from Pr with saponified PC-88A and a scrub section.

That is **REE-on-REE scrubbing**, and it is the exact liquid-liquid analogue of
reflux in a distillation column. It is also the reason a cascade can be pure at
*both* ends instead of one. Scrubbing described as impurity removal — washing
Fe³⁺ or Ca²⁺ off the organic — is a different and much smaller operation; iron
in particular binds D2EHPA more strongly than any rare earth does and has to be
taken out upstream ([](#from-ore-to-feed-solution)), not scrubbed off here. The
strip section then returns the metal to an aqueous phase with strong acid and
regenerates the extractant; part of that strip liquor is split off as the scrub,
and the rest is product. The scrub-to-product split is the reflux ratio, and it
is the knob that trades reagent and throughput against stage count.

The design theory that makes such a cascade calculable rather than empirical is
{index}`Xu Guangxian`'s countercurrent extraction theory, developed in China from
the 1970s [@xu1985theory]. Given β, the feed composition and the two purity
specifications, it yields the number of extraction stages, the number of scrub
stages, the feed-stage location, and the flow ratios in closed form, so that a
plant can be designed on paper and brought up at its design point instead of
being tuned over months of operation. Its adoption, and the linking of cascades
in series so that the raffinate of one becomes the feed of the next, is what
turned a fifteen-component feed into a fan-out of individual oxides and made
China the world's separator of rare earths [@yan2006rare].

#### The Closed-Form Design Equations

It is worth seeing what "in closed form" actually amounts to, because the
equations are short and they connect directly to the Fenske bound derived above.
The account here follows @zhang2016cascade, which sets out Xu's apparatus in
English at book length.

Label the more-extractable element `A` and the less-extractable one `B`, so
`β = D_A/D_B > 1`. The central variable is the **extraction factor** `E`, defined
for each solute as the mass flow of that solute in the organic phase divided by
its mass flow in the aqueous phase at a stage; by construction
`E_A/E_B = β`. The specification enters through two **concentrating factors**,
`a` and `b`, each the ratio of wanted to unwanted at an outlet divided by the same
ratio in the feed — so `b = [P_B/(1−P_B)] / (f_B/f_A)` for the aqueous outlet, and
`a` likewise for the organic outlet. Then the two stage counts are

$$
n = \frac{\log b}{\log (\beta E_B)}
\qquad\qquad
m = \frac{\log a}{\log (\beta' / E'_A)}
$$

with `n` the extraction stages, `m` the scrub stages, and the primes marking
quantities evaluated in the scrub section, where the separation factor `β'` need
not equal `β`.

These are Fenske with the reflux put back. Send the reflux to infinity and
`E_B → 1`, the denominator becomes `log β`, and the expressions collapse to the
minimum-stage relation of the previous section. At finite reflux `E_B < 1`, the
denominator shrinks, and the stage count grows. The gap between `N_min` and a
real design, asserted above, is now a quantity you can compute.

**The optimum is at the geometric mean.** The result that makes the theory a
design method rather than a rearrangement is what happens when you ask for the
*best* extraction factor rather than a feasible one. Maximising daily production
at a fixed total mixer volume and a fixed separation target gives, for a cascade
whose stage count is dominated by the extraction section,

$$
E_B = \frac{1}{\sqrt{\beta}}
\qquad\qquad
J_S = \frac{1}{\sqrt{\beta} - 1}
$$

where `J_S` is the extraction reflux ratio. Since `E_A = β E_B`, the companion
result is `E_A = √β`, and therefore `E_A E_B = 1`: the optimum places the two
solutes' extraction factors symmetrically about unity, so that the
more-extractable element climbs toward the organic outlet exactly as fast as the
less-extractable one falls toward the aqueous outlet. A cascade controlled by its
scrub section instead has the mirror result, `E'_A = √β'` and
`J_W = 1/(√β' − 1)`. Which of the two governs is settled by the feed
composition: for aqueous feeding the process is extraction-controlled when the
organic-outlet fraction `f'_B` exceeds `√β/(√β + 1)` and scrub-controlled below
it.

The reflux ratio is the expensive part, and `1/(√β − 1)` is unforgiving for
close-lying pairs. At β = 2.0 it is 2.4; at the β ≈ 1.5 of an adjacent
lanthanide pair it is 4.5; at β = 1.2 it is 10.5. Reflux here is real solvent and
real scrub liquor circulating through every stage, so the same small β that
forces the stage count up also forces the flow through each of those stages up.
The two costs compound rather than trade off.

**Worked example, from the source.** @zhang2016cascade design a cascade for
`β = β' = 2.00` and an equimolar feed, specifying 99.9% purity for `A` in the
organic outlet and 99.99% for `B` in the aqueous outlet. Here
`f'_B = 0.5 < √2/(√2+1) = 0.586`, so the process is scrub-controlled;
`E'_M = √2 = 1.414`, `E_M = 0.773`, and the resulting design needs **24
extraction stages and 21 scrub stages, 45 in all**. The Fenske bound for the same
specification and the same β is `ln(999 × 9999)/ln 2 = 23.3`, so **24 stages** —
close to half. That factor is the price of finite reflux, a real feed and a real
flowsheet, and it is the concrete version of the warning attached to `N_min`
above.

The closed-form design is where a cascade calculation starts, not where it ends.
Relaxing the constant-extraction-ratio assumption, carrying the acid balance the
saponification section below explains, and asking which arrangement of stages is
*best* rather than which one works are all questions for a numerical model of the
whole train. [](#process-modeling-and-optimization) takes them up, from Xu's
theory through commercial flowsheet simulators to the equation-oriented
frameworks that pose cascade design as an optimization problem.

#### Saponification of the Extractant
There is one industrial practice that follows directly from the reaction this
chapter opened with, and that a laboratory description of solvent extraction
never mentions. Each REE³⁺ transferred to the organic phase releases three
protons into the aqueous phase. At a working loading of 0.2 M rare earth, that
is 0.6 mol of H⁺ per litre of aqueous feed — enough to drop the pH by several
units, which by the slope-3 dependence collapses `D` by several *orders* of
magnitude. Left alone, an extraction cascade poisons itself in its first stage.

Adding caustic to each mixer, as this chapter's own extraction-stage description
does, is how it is handled on a bench. It does not survive scale-up: base
injected into a mixer creates local pH excursions that precipitate rare earth
hydroxides and stabilise emulsions, and it has to be dosed and controlled
separately in every one of dozens of stages. Industrial circuits instead
neutralise the extractant *before* it enters the cascade, a step called
**{index}`saponification`**. The organic is contacted with NaOH, aqueous ammonia,
or a magnesium base, converting a substantial fraction of the acidic extractant
from HL to its sodium, ammonium, or magnesium salt. Extraction then proceeds by
exchanging RE³⁺ for Na⁺, NH₄⁺, or Mg²⁺ rather than for H⁺, and the aqueous pH
stays where it was set without any in-stage dosing
[@banda2015separation; @xie2014critical].

The cost is that the saponifying cation has to go somewhere, and where it goes
is the raffinate. Ammonia saponification — long the standard for P507 circuits,
because ammonium salts of the extractant behave well and NH₃ is cheap — puts
ammonium into every aqueous stream leaving the plant. This is the origin of the
{index}`ammonium-nitrogen <ammonia-nitrogen pollution>` effluent that is the
signature pollution problem of Chinese rare earth separation, and it is the same
nitrogen burden, from a different unit operation, that
[](#ion-adsorption-clays) describes for ammonium sulfate clay leaching and that
[](#environment-techno-economics-and-life-cycle) counts in the eutrophication
column of the life-cycle inventory. Sodium saponification trades it for a saline
raffinate; magnesium and calcium saponification, and non-saponification
flowsheets that recycle the acid instead, are the directions the Chinese industry
has been pushed toward on exactly these grounds [@liao2013clean]. Whichever is
chosen, the reagent bill and the effluent are set by the same stoichiometry:
three equivalents of base per mole of rare earth moved.

### Operational Considerations

**Which phase is continuous** is a choice, not an accident, and it is made in the
mixer by how the impeller is started and by which phase is in excess. Running
aqueous-continuous, with the organic dispersed as droplets, is the usual choice
in rare earth circuits: it keeps the organic holdup in the mixer low, which
matters because the organic is the expensive phase, and it is the natural state
when the organic flow is the smaller of the two. Organic-continuous operation is
used where the organic flow is the larger, and it changes the mass transfer
behaviour and the entrainment pattern with it. A circuit that flips
unintentionally between the two — phase inversion — behaves quite differently
before and after, which is one of the reasons flow ratios are controlled tightly.

**Interfacial area** is one of the two factors in the rate at which anything
crosses:

$$
\text{Rate} = K_\mathrm{overall} \, a \, (C^* - C)
$$

with `K` the overall mass transfer coefficient, `a` the interfacial area per unit
volume, and `C* − C` the departure from equilibrium. Since the chemistry is fast
and the resistance is diffusional, `K` is not readily manipulated: what a
contactor designer actually controls is `a`, and the contactor comparison above
is in large part an argument about how each family manufactures `a` and what it
charges for it — an impeller and a large settler, a pulse and a tall column, a
rotor and a motor, or a membrane and its fragility. The same variable is what
microfluidic devices attack directly, by making channels small enough that the
area-to-volume ratio is large without any agitation at all;
[](#microfluidic-separations) takes that up.

**Entrainment** is the carryover of droplets of one phase into the bulk of the
other, and it is the standing loss mechanism of any dispersive contactor: organic
entrained in the raffinate is reagent lost and an effluent problem, and aqueous
entrained in the loaded organic carries unwanted metal forward into the scrub
section, degrading the separation the cascade just achieved. The remedies are all
ways of buying coalescence — longer settler residence time, coalescing packing or
mesh, well-designed weirs and baffles — and they are the reason the settler is as
large as it is. Where a system is prone to stable emulsions, a phase modifier or
a change of contactor family is a better answer than a bigger settler.

(process-control-and-automation)=
### Process Control and Automation

The controlled variables in a solvent extraction circuit follow directly from
the chemistry above, and the ordering of their importance is not a matter of
taste.

**pH comes first.** The Δ pH₁/₂ = 0.06 result derived earlier says that the whole
of an adjacent-pair separation factor is worth six hundredths of a pH unit; a pH
excursion of a tenth of a unit is therefore larger than the effect the cascade
exists to exploit. In-line pH measurement and automatic acid or base addition are
consequently not refinements but the primary control loop, and saponification
exists precisely because dosing that loop in every mixer of a large train does
not work.

**Flow ratio comes second**, because `O/A` enters the extraction factor
multiplicatively alongside `D`, so an error in the phase ratio is an error in
every stage's transfer simultaneously. Drifting flow ratios also move the
operating point toward flooding or phase inversion.

**Temperature and interface level** are supporting loops. Temperature matters
more for viscosity and disengagement than for equilibrium, as the temperature
section argued, and matters most in the strip section where circuits are often
run warm. Interface level in each settler is held by capacitance or conductivity
sensing, and losing it means sending one phase out of the wrong weir.

**Automation in the laboratory.** Nothing above is specific to rare earths;
what is newer is closing the loop around the *chemistry* rather than around the
hydraulics. @augustine2024advancing built an automated high-throughput
extraction platform with ICP-AES analysis and Bayesian optimization choosing
the next condition, reaching some two hundred measurements a day and cutting
the experimental effort for a thorium extraction optimisation by about
three-quarters. That is a bench instrument for finding conditions, not a plant
controller -- but it is the same feedback idea one level up, and
[](#process-modeling-and-optimization) picks up where it leads.

These are the actuators. What tells them where to go is a model of the cascade,
and on an industrial train the controlled variable — component content partway
along the profile — is not something any of the instruments above measures
directly. [](#process-modeling-and-optimization) covers the soft sensors and
predictive controllers built for that problem, and the process models they run
on.

## A Worked Illustration: One Cascade, End to End

The example below is a *worked illustration*, in the same spirit as the
slope-3 table earlier in this chapter. Its numbers are chosen to be internally
consistent with the relations derived above — the loading limit of a 30 vol%
D2EHPA solution, the extraction factor, the pH window — and are not taken from
any operating plant. Read it as an exercise in how the pieces fit together, not
as a specification.

**Feed**: a {index}`bastnäsite <bastnäsite>` concentrate, light-rare-earth
dominated (La, Ce, Pr, Nd).

**Step 1 — dissolution.** Roast the concentrate to convert carbonate and fluoride
to oxide, then dissolve in hydrochloric acid. The product is a strongly acidic
chloride liquor of mixed rare earths. [](#hydrometallurgical-leaching) treats
this step properly.

**Step 2 — purification.** Raise the pH to precipitate ferric hydroxide and
filter it out. Iron has to go here rather than in the cascade, for the reason
given above: it binds D2EHPA more strongly than any rare earth and will not
scrub off.

**Step 3 — cerium removal.** Cerium is the one lanthanide with an accessible
tetravalent state. Oxidising Ce³⁺ to Ce⁴⁺ and precipitating it removes the
single largest component of a light-rare-earth feed in one non-extractive step,
before any solvent extraction is done. This is the largest single simplification
available in the whole flowsheet, and it is available only for cerium.

**Step 4 — La from Pr/Nd.** With acidic organophosphorus extractants the heavier
lanthanides extract more strongly, so **La is the element left behind**: the
split takes lanthanum out of the raffinate, not out of the organic phase. A
concrete arrangement:

- Feed: 0.3 M (La+Pr+Nd) at pH near 3, diluted from Step 3.
- Organic: 30 vol% D2EHPA with 10 vol% TBP in kerosene — about 0.9 M in monomer,
  and so saturating near 0.3 M rare earth.
- Extraction: several stages at O/A = 2/1 with the pH held. Pr and Nd extract
  preferentially, having the lower pH₁/₂. The organic leaves at roughly 0.15 M,
  about half of its capacity, which is where these circuits are run for the
  loading reasons given earlier.
- Scrub: a small number of stages using a split of the strip product — REE-on-REE
  scrubbing, displacing co-extracted La back toward the feed.
- Strip: several stages with strong hydrochloric acid, run warm. The strip liquor
  is enriched in Pr and Nd, and concentrated relative to the feed by the phase
  ratio, as the concentration-factor arithmetic above describes.
- The lanthanum product is recovered from the raffinate by oxalate precipitation
  and calcination.

**Step 5 — Pr from Nd.** The strip liquor from Step 4 becomes the feed to a
second cascade, and this is the hard one. Pr and Nd are adjacent, their
separation factor is in the range this chapter has been using throughout, and the
Fenske bound applies in full: a bulk split takes a modest number of stages, and a
high-purity neodymium takes many times more. The dynamic modelling work discussed
in [](#process-modeling-and-optimization) was done on exactly this split, and
found that better than 99% neodymium purity required a dedicated neodymium scrub
solution and a twelve-stage scrubbing circuit on what is effectively a
two-component feed [@lyon2016separation].

The whole fan-out of a fifteen-component feed into individual oxides is this
pattern repeated, cascade after cascade, with the raffinate of one becoming the
feed of the next. What that costs in reagents, energy and effluent is the subject
of [](#environment-techno-economics-and-life-cycle), which draws on published
life-cycle inventories rather than on an illustration.

## Summary and Key Takeaways

### The Argument in One Page

An acidic organophosphorus extractant is a weak acid that exchanges three protons
for one trivalent rare earth ion. Everything follows:

- Because three protons are exchanged, log D moves with slope +3 against pH, so
  a single pH unit is three decades in D. That makes the process reversible by pH
  alone, and it makes pH the primary control variable.
- Because the same slope applies to every lanthanide, the lines for two adjacent
  elements are *parallel*. Their separation factor is fixed by the horizontal gap
  between them, and for adjacent light lanthanides that gap is around 0.06 pH
  units, or β ≈ 1.5.
- Because β ≈ 1.5, purity has to be bought by staging. The Fenske bound puts the
  floor at 45 equilibrium stages for 99.99% at both ends, and a real cascade needs
  more, because it runs at finite reflux on a multicomponent feed with imperfect
  stages.
- Because a cascade is that long, the contactor is chosen for robustness and
  observability rather than for compactness, which is why mixer-settlers remain
  the industry standard despite losing to every alternative on footprint,
  inventory and startup time.
- Because three equivalents of base are consumed per mole of rare earth moved,
  the reagent bill and the effluent are set by stoichiometry rather than by
  efficiency, and saponification is where that cost is paid.

### Why Kerosene

Kerosene is not chosen for any property it maximises but for the set it satisfies
at once: density far enough below a salt-loaded aqueous phase for the two to
disengage under gravity; viscosity low enough that they disengage quickly;
negligible water solubility; polarity low enough not to interfere with the
extraction chemistry, yet sufficient to dissolve large alkyl phosphorus esters;
chemical inertness to acid and base over years of recycling; a flash point safe
for bulk storage; and a price set by the refinery rather than by a specialty
supplier. Every alternative beats it on one of these and loses on another.

### The pH Swing

```text
Higher pH → REE extracts into organic (D >> 1)
         ↓
    Loaded organic
         ↓
Strong acid → REE strips back to aqueous (D << 1)
         ↓
 Regenerated organic (recycle)
```

Slope: ∂(log D)/∂pH ≈ +3 for trivalent REE with dimeric acidic extractants.

### Practical Implementation

For successful REE solvent extraction:

1.  Control pH tightly — the tolerance is set by Δ pH₁/₂, not by convenience,
    and for an adjacent pair that means hundredths of a unit
2.  Match the salting agent to the acid medium, and count what it costs in the
    raffinate
3.  Hold the phase ratio: it enters the extraction factor as directly as D does
4.  Keep the organic well below its loading limit, or lose the selectivity the
    cascade was built on
5.  Size settlers for clean phase separation, and expect them to dominate the
    inventory
6.  Monitor extractant quality and wash out degradation products periodically
7.  Use countercurrent, and for a separation rather than a recovery use
    fractional extraction with REE-on-REE scrub
