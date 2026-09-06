---
title: From Ore to Feed Solution
---

(from-ore-to-feed-solution)=
# From Ore to Feed Solution

A {index}`solvent extraction` circuit does not start from an ore. It starts from an
aqueous solution of a particular acid, at a particular pH, carrying a particular
set of impurities — and almost everything that circuit can achieve is fixed
before the first contactor by decisions made upstream. This chapter covers that
upstream span: which minerals rare earths actually come in, what the mill and
the cracking furnace do to them, and what the resulting liquor has to look like
before extraction can begin.

The organising idea is one that the flowsheet diagrams tend to hide. The acid
chosen at the cracking step is not chosen for the cracking step. It is chosen
for what happens two unit operations later. A leach liquor is the *feed* to a
separation circuit, and its anion decides which extractant chemistries are
available at all, whether the aqueous phase can be closed into a loop, how
concentrated the feed is allowed to be, and what the raffinate does to the
wastewater plant. Chloride, nitrate, and sulfate each buy something real and
each charge for it. Most of this chapter is an accounting of those three bills.

A second decision echoes just as far: impurity removal. Iron, aluminium,
calcium, {index}`thorium`, uranium, and — for the phosphate minerals — phosphate
itself all interfere with extraction, and every part per million left in the
feed is paid for downstream, in emulsions, in crud, in lost loading, and in
regulated waste.

[](#hydrometallurgical-leaching) treats leaching and cracking in full industrial
detail, and [](#ion-adsorption-clays) treats the clay deposits as deposits.
What follows here is the argument those chapters assume: why the feed solution
looks the way it does, and what that shape costs the circuit in
[](#solvent-extraction-fundamentals).

## What Actually Arrives at the Chemical Plant

Rare earths do not occur as native metals. They occur in oxide, carbonate and
phosphate minerals, and the lattice sites they occupy are hospitable to other
large cations as well — which is why thorium and uranium turn up in the
phosphates and why the impurity problem later in this chapter begins in the
mineralogy [@jha2016hydrometallurgical; @balaram2019rare]. Four sources carry
essentially all of world production.

**{index}`Bastnäsite <bastnäsite>`** (REE·FCO₃) is a fluorocarbonate, strongly
enriched in the light rare earths — La, Ce, Pr, Nd — and it is the mineral
behind {index}`Mountain Pass` in California and a principal rare-earth carrier in
the {index}`Bayan Obo` ore of Inner Mongolia, where it occurs mixed with monazite
[@kim2025rare; @xu2012decomposition].
**{index}`Monazite <monazite>`** ((REE,Th)PO₄) is a light-to-middle-REE
phosphate whose defining feature in processing is that thorium substitutes into
it, which turns every monazite flowsheet into a radioactive-materials flowsheet
[@kumari2015process].
**{index}`Xenotime <xenotime>`** (YPO₄) is the heavy-REE phosphate —
{index}`yttrium <yttrium>`, Dy, Er, Yb. It is recovered alongside monazite by
flotation [@chelgani2015rare], it resists decomposition as monazite does, and
its leach solutions carry thorium and uranium that have to be extracted out
[@hung2020separation].
**{index}`Ion-adsorption clays <ion-adsorption clay>`** are the odd one out and
are treated separately below.

Those four are the ore. A fifth category is not an ore at all: material that has
already been mined, burned or processed for something else and carries rare
earths as a passenger — coal ash, {index}`phosphogypsum`, scrap magnets and
phosphors, oilfield and geothermal waters. None of it needs a mill, some of it
needs no crack at all, and all of it arrives with a different impurity problem
from the one described here. It is collected in
[](#recycling-and-urban-mining), and the oilfield waters — where the critical
mineral that matters turns out not to be a rare earth at all — get a chapter of
their own in [](#produced-water-critical-minerals).

For the three hard-rock minerals, the first plant is a mill, not a reactor.
Crushing and grinding liberate the rare-earth mineral from its host rock; then
gravity, magnetic and flotation stages exploit density, magnetic susceptibility
and surface chemistry to reject gangue and produce a mineral concentrate
[@jordens2013beneficiation; @chelgani2015rare; @zhou2024gravity]. The important
point for this chapter is what beneficiation does *not* do. It is a physical
operation. It raises the grade and it discards mass, but the rare earths that
leave the mill are still locked in a fluorocarbonate or a phosphate lattice, and
a good deal of the gangue that could not be rejected leaves with them. Gangue
minerals are the predominant source of the impurities that appear in the leach
liquor, so what the mill fails to reject, the chemical plant pays for
[@li2025iron].

Reported concentrate grades and mineral REO contents vary widely with deposit
and with flowsheet, and the specific ranges that circulate in teaching material
for bastnäsite, monazite and xenotime could not be traced to a primary source
while this chapter was written. They are therefore not given here; the reviews
cited above are the place to look for deposit-specific figures.

One worked example, drawn from a study that reports its whole chain, shows the
shape of it. A Canadian ore from a peralkaline volcanic deposit was ground and
put through a hybrid magnetic-gravity separation that recovered 92% of the total
rare-earth oxide into a concentrate; that concentrate was then baked with
sulfuric acid at 250 °C and water-leached at 80 °C, extracting 92% of the rare
earths into solution [@li2025iron]. Two physical steps and two chemical steps,
and only now is there something a contactor can be fed.

## Cracking: Making the Mineral Let Go

Between the concentrate and the liquor sits decomposition — "cracking" or
"baking," reviewed as a class by @sadri2017cracking. Each mineral resists in its
own way, and the route chosen to break it is where the anion of the eventual
feed solution is either committed or left open.

Bastnäsite's barrier is fluorine. Roasting drives off carbon dioxide and leaves
a rare-earth oxide or oxyfluoride that acid will attack, but the fluoride has to
be dealt with rather than simply released; ammonium chloride roasting, for
instance, was developed specifically to deactivate the fluorine during recovery
[@chi2004recovery]. Alkali routes take the opposite approach and decompose
bastnäsite and monazite together by calcining with alkali liquid
[@xu2012decomposition].

The phosphates are refractory in a different sense: the REE–PO₄ bond is strong,
and the two classical answers to it are sulfuric acid baking and caustic
digestion [@sadri2017cracking; @kumari2015process]. The distinction between them
matters more than it looks. An acid bake dissolves the mineral *in* an acid, and
the plant thereby inherits that acid's anion whether it wants it or not — the
sulfate liquor in the worked example above is sulfate because the bake was
sulfuric [@li2025iron]. Caustic digestion instead converts the phosphate to a
rare-earth hydroxide, leaving the phosphorus behind in the alkaline stream — and
a hydroxide can be redissolved in whichever acid the downstream circuit actually
wants [@kumari2015process; @sadri2017cracking]. It is also the route in which
thorium is separated from the rare earths during processing rather than after it
[@shahreldin2018selective]. Alkaline cracking is the more expensive operation
and it is the one that decouples the cracking chemistry from the feed chemistry.
That is what the extra cost buys.

## The Anion Is a Downstream Decision

Three families of extractant are used to separate rare earths, and the anion in
the aqueous phase decides which of the three is even on the table
[@larsson2015separation].

*Acidic* extractants — the phosphorus-containing acids D2EHPA (P204), PC88A
(P507), Cyanex 272 — are the workhorses of the industry. They extract rare
earths from chloride, nitrate or sulfate feeds alike, provided the metal is
present as a hydrated cation or a cationic complex, and one extractant can
handle the whole series. *Neutral*, or solvating, extractants —
{index}`TBP <TBP (tributyl phosphate)>`, Cyanex 923, Cyanex 925 — work by
coordinating a neutral metal-anion complex, and they extract rare earths
efficiently from nitrate or thiocyanate media but **not** from chloride.
*Basic* extractants, the quaternary ammonium anion exchangers such as
Aliquat 336, behave similarly:
they have been used from nitrate and thiocyanate, not from a pure chloride
medium [@larsson2015separation]. Choose chloride at the cracking step and two of
those three families are closed to you.

### Chloride

Chloride is the default, and the reasons are commercial and environmental before
they are chemical. Hydrochloric acid is much cheaper and more readily available
than nitric; it is easier to recycle and to run in a closed loop; and treating a
chloride-bearing waste stream is easier than treating a nitrate-bearing one
[@larsson2015separation]. That last point is the one process engineers feel
most, because the raffinate volume of a rare-earth plant is large and it leaves
every day.

What chloride commits you to is acidic-extractant chemistry, with all of its
characteristic costs. The extraction is a proton exchange, so it is pH-sensitive
and requires careful monitoring; stripping the loaded organic is hard, because
the metal's affinity for these extractants is high, and the heavy rare earths
may need concentrated sulfuric acid to come off. Both the pH control and the
back-extraction consume reagents — acid for pH and stripping, base for pH
control and for pre-neutralising (saponifying) the extractant — and the neutral
salt from those acid–base reactions ends up as a large volume of high-salinity
wastewater [@larsson2015separation]. Practical chloride-medium circuits are
built on exactly these extractants and their mixtures [@afonin2024extraction;
@liu2014solvent; @banda2015separation].

There is also a ceiling on feed strength. Acidic-extractant circuits generally
run at 30–50 g/L total rare-earth oxide, because high loading of the organic
phase risks gel formation — with D2EHPA, at roughly 50% saturation of the
extractant [@larsson2015separation]. A dilute feed means a dilute strip liquor
and a low volumetric efficiency for the whole plant.

The claim that chloride liquors demand exotic metallurgy while nitrate liquors
are compatible with ordinary 316L stainless steel appears in lecture material on
this subject but could not be traced to a primary source, and no figure for it
is asserted here.

### Nitrate

Nitrate is the more interesting choice, because what it buys is a different
*kind* of plant rather than a better version of the same one.

Solvating extractants coordinate a neutral rare-earth nitrate complex, so their
distribution ratios are governed by nitrate activity rather than by pH. Three
consequences follow, and all three are worth money. They tolerate very
concentrated feeds — 100 to 500 g/L dissolved rare-earth oxide, an order of
magnitude above what an acidic-extractant circuit accepts — with far less
trouble from gel formation in the loaded organic. They show little pH
dependence, so the pH monitoring and control loop that governs a D2EHPA circuit
is largely absent. And stripping is done with neutral or slightly acidified
water rather than strong acid, which returns a concentrated and comparatively
clean aqueous product instead of a dilute one buried in reagent salt
[@larsson2015separation].

The corollary is that nitrate has to be *supplied*. Because extraction depends
on nitrate activity, a nitrate salt is added as a salting-out agent to drive the
distribution ratio up; @matveev2018solvent studied rare-earth extraction by TBP
and tri-iso-amyl phosphate in the presence of Ca(NO₃)₂ for exactly this reason.
The salt is a reagent cost and it is also a raffinate load, since it leaves the
circuit dissolved in the aqueous phase. The same nitrate dependence recurs
wherever TBP is used — in mixed-extractant systems for intra-lanthanide
separation [@turanov2020solvent], and in the TBP–nitric acid adduct used as the
extracting agent in supercritical-CO₂ extraction from ores
[@li2024optimization].

Against that: nitric acid is more expensive and less available than
hydrochloric, harder to recycle into a closed loop, and its wastewater is harder
to treat [@larsson2015separation]. Nitric acid digestion is also commonly said
to release nitrogen oxides that must be scrubbed and recovered; no source that
establishes this quantitatively for rare-earth cracking could be reached while
this chapter was written, so no figure is given.

The tension is sharp enough that people have tried to have it both ways.
Split-anion extraction runs a chloride aqueous phase against an organic phase
that is itself a nitrate or thiocyanate ionic liquid, so the complexing anion
comes from the organic side. The feed is chloride, the wastewater is chloride,
stripping is done with water, and separation factors between the ends of the
series (La–Lu) exceed 2 × 10⁵ [@larsson2015separation]. The reason it works is
the Hofmeister series: the anions' preference for the organic phase runs
SO₄²⁻ < Cl⁻ < Br⁻ < NO₃⁻ < I⁻ < ClO₄⁻ < SCN⁻, tracking how strongly each is
hydrated, so a thiocyanate or nitrate ionic liquid keeps its own anion and does
not exchange it away to a chloride aqueous phase. The mechanism is therefore
*not* anion exchange, even though the extractant is a quaternary ammonium salt:
the rare earth crosses together with enough chloride to balance the charge.
Thiocyanate systems outperform nitrate ones, and yttrium comes out behaving like
terbium — another instance of the point made in
[](#solvent-extraction-fundamentals) that yttrium's position is set by the
ligand and not by the ion. That the idea exists at all is the clearest evidence
that the anion choice is felt as a constraint rather than a detail.

### Sulfate

Sulfate liquors arrive by two quite different roads. The first is sulfuric acid
baking of a hard-rock concentrate, which is cheap and effective and which is why
monazite sulfuric-acid liquors are a standard object of study — and why
separating thorium and uranium out of them by solvent extraction is a standard
problem [@amaral2010thorium; @li2025iron]. That problem has a literature of
its own on the nuclear side of the divide, treated in
[](#uranium-and-plutonium).

The second is the {index}`ion-adsorption clay <ion-adsorption clay>` deposits,
where there is no cracking step at all. The rare earths are not in a lattice;
they are hydrated cations held electrostatically on clay surfaces, and a more
concentrated electrolyte cation displaces them by mass action:

$$
\mathrm{Clay}\text{--}[\mathrm{REE}^{3+}] + 3\,\mathrm{NH_4^+} \rightarrow \mathrm{Clay}\text{--}[\mathrm{NH_4^+}]_3 + \mathrm{REE}^{3+}(\mathrm{aq})
$$

Across ores of varying origin, all the rare earths reach peak extraction under
ambient conditions with fast kinetics — no roasting, no strong acid, no heat
[@moldoveanu2016overview]. [](#ion-adsorption-clays) takes up the deposits and
the exchange chemistry in detail.

The price of that mildness is dilution, and it is not a price that can be
negotiated away. Lowering the liquid-to-solid ratio, recycling leachate onto
fresh ore, and countercurrent leaching all raise the rare-earth concentration in
the product liquor — but each does so at the expense of the extraction level
achieved. Worse, the solution held in the leached residue carries significant
rare earths and residual lixiviant with it, so the solids need thorough washing
that dilutes the stream again [@moldoveanu2016overview]. A dilute feed is
precisely what the downstream circuit does not want, which is why work on these
liquors concentrates on enrichment before separation [@han2024efficient].

The lixiviant cation is a third decision with an environmental price attached.
Ammonium sulfate is the traditional choice and it is the source of the
ammonia-nitrogen pollution that these operations are known for; magnesium
sulfate was developed as a direct substitute to avoid it [@xiao2015recovery;
@xiao2015leaching]. Sulfate carries its own downstream consequences too: where
calcium is present, gypsum precipitates and drags rare earths with it, and
thorium co-precipitates with rare-earth double sulfates [@li2025iron].

## What Else Is in the Bottle

A leach liquor is not a rare-earth solution with traces of something else in it.
The Canadian sulfate liquor described above contained 750.55 mg/L total rare
earths, of which cerium was the largest single element at 290.25 mg/L — against
1624.00 mg/L of iron, 358.40 mg/L of aluminium, and 12.51 mg/L of thorium, at pH
1.6–1.7 [@li2025iron]. Iron alone outweighed the rare earths taken together by
more than two to one. That ratio, not the rare-earth chemistry, is what makes
the front of a separation circuit hard.

Each impurity misbehaves in a specific way [@li2025iron; @pak2020progress].
Aluminium and iron(III) are *preferentially* extracted ahead of the rare earths
in naphthenic-acid circuits and are the first species stripped during scrubbing,
so they cycle back to the feed stage and accumulate; once concentrated they
hydrolyse to gel-like hydroxides, which emulsify the contactors, destroy contact
area, and degrade extraction. Calcium reports as gypsum and is a principal
constituent of "crud," the interfacial solid that fouls mixer-settlers. Silicon
forms gelatinous precipitates in some newer feedstocks. Thorium and uranium do
not make crud, but they load into the solvent and take capacity away from the
rare earths, and thorium additionally co-precipitates with rare-earth double
sulfates and oxalates and puts the tailings under radiological regulation
[@li2025iron; @iaea2011radiation].

Impurity removal is therefore not a polishing step but a design decision, and
where it sits in the flowsheet is itself a choice — inside the leach, between
leach and extraction, or after a mixed oxide is made [@pak2020progress]. The
common approach is selective precipitation on a rising pH ramp, and the
selectivity is real but partial. In the worked example, magnesium carbonate
precipitation reached equilibrium within 30 minutes in every system tested but
one, and removed iron nearly completely at pH 3.5. At the optimised conditions —
81 °C, pH 3.6, with hydrogen peroxide added to hold all the iron as Fe(III) — it
removed all of the iron, about 95% of the thorium and about 65% of the
aluminium, while losing under 3% of the total rare earths [@li2025iron]. Read
that as an engineer rather than as a chemist: roughly a third of the aluminium
survives the purification and goes into the contactors, and residual soluble
iron and aluminium, together with the operating pH, are known to degrade
rare-earth separation from low-grade feedstocks — demonstrated directly for
supported liquid membranes [@middleton2023separation].

Thorium and uranium usually need a dedicated stage rather than a pH ramp —
solvent extraction from monazite sulfuric liquors [@amaral2010thorium], amine
extraction from xenotime leach solutions [@hung2020separation], or selective
separation during alkaline monazite processing [@shahreldin2018selective] — and
the residues they generate are managed as naturally occurring radioactive
material [@iaea2011radiation]. [](#uranium-and-plutonium) covers where those
actinides go once they leave a rare earth circuit, and why the extractants used
to remove them here are the same ones used to recover uranium from ore.

## What This Fixes for the Rest of the Book

By the end of this span the plant has a liquor, and that liquor has already
foreclosed most of its own options. The anion sets which extractant families are
available and, through them, whether the circuit is pH-controlled or
nitrate-controlled, whether it strips with acid or with water, and how
concentrated the feed can be [@larsson2015separation]. The residual impurity
load sets how much of the first few stages is spent on iron and aluminium rather
than on separation, and how much of the raffinate is regulated waste
[@li2025iron; @pak2020progress]. The reagent and salt balance sets the
wastewater problem that [](#environment-techno-economics-and-life-cycle)
returns to.

None of that is visible from inside [](#solvent-extraction-fundamentals), which
begins with a feed composition and takes it as given. It is worth carrying the
knowledge that the given was chosen.
