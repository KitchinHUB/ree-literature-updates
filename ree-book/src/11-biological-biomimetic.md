---
title: Biological and Biomimetic Separations
---

(biological-and-biomimetic-separations)=
# Biological and Biomimetic Separations

Biology solved one half of the rare-earth separation problem long before
chemistry did, and left the other half untouched. {index}`Lanmodulin <lanmodulin>`,
a bacterial protein discovered in methylotrophs that use lanthanides as enzyme
cofactors, responds to picomolar concentrations of lanthanides but only to
near-millimolar calcium — a preference of order 10⁸ that no synthetic
extractant approaches [@cotruvo2018lanmodulin].

Before that number is put to work, it has to be read correctly, because the two
selectivities involved in rare-earth processing are entirely different
quantities:

- **Ln/non-Ln selectivity** — telling a rare earth from calcium, iron,
  aluminium, or the rest of a leach liquor. This is a charge-and-radius problem,
  and lanmodulin is spectacular at it. It is also the selectivity that decides
  whether you can pull rare earths out of a dilute, calcium-rich, iron-rich
  pregnant leach solution in one aqueous step.
- **Ln/Ln selectivity** — telling Nd from Pr, or Dy from Ho. This is what
  "hundreds of stages" in [](#solvent-extraction-fundamentals) is about, and it
  is a much harder problem. Lanmodulin is a *weak* discriminator here: the same
  picomolar affinity that gives it the 10⁸-fold edge over calcium applies to
  every element from La to Lu, and the prototypal protein shows only about a
  **fivefold** overall preference for light over heavy rare earths
  [@mattocks2023enhanced].

Seven orders of magnitude separate those two figures, and conflating them
produces the claim — common in reviews and press coverage — that proteins have
already beaten solvent extraction on selectivity. They have not. The best
adjacent-pair separation factor demonstrated by any protein system is about
1.4 (Nd/Pr) to 3.0 (Ce/La) [@larrinaga2024modulating], and the best
*average* over a long run of adjacent pairs is 2.1, across the eleven elements
Nd to Lu [@choi2026near]. Both sit in the band conventional acidic
organophosphorus extractants occupy. What biology has actually delivered is a
group-separation and concentration step that solvent extraction performs poorly
and expensively, plus — through a second, quaternary-structure mechanism
described below — a genuine but modest intra-series fractionation.

This chapter covers what has been built on that observation. Protein and peptide
systems come first, since they carry the highest group selectivities and the
clearest mechanistic picture. Then the routes that trade selectivity for robustness and
cost: biosurfactants, microbial {index}`biosorption`, {index}`bioleaching`, and phytomining. The
economics run in the opposite direction from the selectivity — the most
selective systems are the most fragile and the most expensive to produce, and
the least selective are the ones already operating in the field.

The coacervate systems in [](#coacervates-and-aqueous-biphasic-systems) are the
natural process vehicle for these ligands, since both work in aqueous media
under mild conditions.

(lanmodulin-structure-mechanism-and-engineering)=
## Lanmodulin: Structure, Mechanism, and Engineering
### Discovery and Properties
Lanmodulin (LanM) is a 12 kDa protein identified in *Methylobacterium extorquens*, a methylotrophic bacterium that requires lanthanides for methanol metabolism. LanM is the most selective macromolecule for REEs characterized to date, even outperforming many synthetic chelators [@deblonde2020selective].

The measured properties, each with the paper it comes from, are collected
below; the first three rows are the ones that decide what the protein is good
for.

| Property | Value | Source |
| ---------- | ------- | ------- |
| Selectivity Ln³⁺/Ca²⁺ | ~10⁸-fold (picomolar Ln³⁺ response vs. near-millimolar Ca²⁺) | [@cotruvo2018lanmodulin] |
| Dissociation constant (K_d,app) | Picomolar for every Ln³⁺ from La to Lu and for Y³⁺; tabulated values for the prototypal protein run 70 ± 10 pM (Pr³⁺), 100 ± 10 pM (Gd³⁺), 200 ± 50 pM (Dy³⁺), 260 ± 60 pM (Ho³⁺) and 177 pM (Y³⁺) | [@cotruvo2018lanmodulin; @deblonde2020selective; @cook2019structural], as tabulated in [@yang2025emerging] |
| Selectivity Ln³⁺/Ln³⁺ | **About fivefold**, light over heavy, for the whole series; all lanthanides and Y³⁺ induce essentially the same conformational change | [@mattocks2023enhanced] |
| pH stability | Retains binding down to pH ≈ 2.5 | [@deblonde2020selective] |
| Temperature stability | Up to 95 °C; survives repeated acid treatment | [@deblonde2020selective] |
| Competing metal tolerance | Up to molar amounts of Li, Na, Mg, Ca, Sr, Al, Si, Mn, Fe, Co, Ni, Cu, Zn, U | [@deblonde2020selective] |

Read the first three rows together, because they are the whole story. The
10⁸-fold figure, the near-flat picomolar Kd profile, and the fivefold Ln/Ln
preference are three faces of one fact: lanmodulin binds *all* trivalent rare
earths at nearly the same enormous strength, and calcium essentially not at all.
The tabulated dissociation constants make the point concretely: from Pr³⁺ to
Ho³⁺, nine places across the series, the apparent Kd moves by less than a factor
of four, which is the fivefold light-over-heavy preference seen from the other
side. Set the two selectivities side by side — 10⁸ against Ca²⁺, about 5 across the
entire lanthanide series — and the seven orders of magnitude between them is the
single most important number in this chapter.

That combination is exactly the property wanted for lifting a few hundred ppm of
total REE out of a leach liquor dominated by Ca, Fe and Al — the
{index}`pregnant leach solution` of [](#hydrometallurgical-leaching) — and
exactly the wrong property for splitting Nd from Pr. Quoting the 10⁸-fold number
in a discussion of intra-series separation, which is common in reviews and press
coverage, inverts what the measurement means.

### Structural Basis of Selectivity

The NMR solution structure explains where the group selectivity comes from
[@cook2019structural]. Lanmodulin carries four EF-hand motifs, the same
helix-loop-helix used throughout biology to bind Ca²⁺, but adjacent pairs of
them are fused in a way that has no counterpart among ordinary EF-hand proteins
and that gives the protein a compact fold. The structure was solved with Y³⁺
rather than with a lanthanide, and its central claim about the coordination
sphere is that an *additional* carboxylate ligand, beyond the canonical EF-hand
donor set, is what buys the picomolar affinity. The same work implicates unusual
N$_{i+1}$-H···N$_i$ hydrogen bonds involving the EF-hand prolines in selective
Ln³⁺ recognition. Donor-by-donor assignments and metal-ligand distances live in
the deposited coordinates rather than in the paper's own text, so they are not
quoted here.

Those prolines are the second half of the discrimination against calcium. Each
EF-hand contains one, and it hampers the loop's response to Ca²⁺ while leaving
the response to a lanthanide intact; mutate the prolines to alanine and calcium
becomes able to induce the conformational change at far lower concentrations.
The extra carboxylate raises the affinity for a trivalent ion, and the proline
lowers it for a divalent one --- two independent mechanisms pushing in the same
direction, which is how eight orders of magnitude are assembled.

[](#fig-lanm-efhand) sets the lanmodulin site beside the canonical calcium
EF-hand it is built from, and puts both selectivities on one axis. The three
differences that matter — an extra unit of charge on the ion, three more donors
in the first coordination sphere, and the proline in the loop — are all reasons
to prefer a rare earth over calcium. None of them is a reason to prefer one
rare earth over the next, which is exactly what the flat picomolar profile in
panel C shows.

:::{figure} ../figures/11-lanm-efhand.svg
:name: fig-lanm-efhand
:width: 100%

Why lanmodulin prefers rare earths to calcium, and why that preference says
almost nothing about telling one rare earth from another. **(A, B)** Schematic
coordination spheres — not crystal structures: the donor positions are spaced
evenly for counting and are not real geometry. Both motifs are helix–loop–helix;
the lanmodulin site closes more oxygen donors around a trivalent ion than the
canonical seven around Ca²⁺ [@gifford2007structures], and every lanmodulin
EF-hand carries a proline that blocks the calcium response, with Pro→Ala letting calcium back in. The
extra carboxylate donor in (B) is the one the NMR solution structure singles out
as the source of picomolar affinity [@cook2019structural] -- a structure solved
with Y³⁺ rather than with a lanthanide; the sources cited here do not assign the
sphere donor by donor, so neither does the drawing.
**(C)** Both selectivities on one affinity axis. The ~10⁸-fold preference for
Ln³⁺ over Ca²⁺ is eight units tall; calcium's own position is *implied* by that
ratio rather than measured, and the panel says so. Across the series the site is
nearly flat — picomolar for every lanthanide and Y³⁺ [@cotruvo2018lanmodulin].
The plotted points are the tabulated apparent dissociation constants of the
prototypal protein, 70 ± 10 pM at Pr rising to 260 ± 60 pM at Ho, with 177 pM
for Y³⁺ as the dashed line [@yang2025emerging]: a factor of four across nine
elements, and the same light-over-heavy direction, of roughly the same size, as
the fivefold intrinsic preference reported for this protein
[@mattocks2023enhanced]. Less than one unit on an axis where the gap to calcium
is eight. The binding site does not sharply distinguish neighbouring rare earths: the best adjacent-pair separation factors
any protein system has produced are 1.4 (Nd/Pr) to 3.0 (Ce/La)
[@larrinaga2024modulating], with an average of 2.1 over the eleven adjacent
pairs from Nd to Lu [@choi2026near].
:::

### Metal-Sensitive Dimerization

If the binding site cannot distinguish neighbouring lanthanides, something else
must. In the one mechanism that has worked, the discrimination is moved out of
the coordination sphere and into the *quaternary* structure: whether two protein
molecules associate at all depends on which ion is bound.

Lanmodulin from *Hansschlegelia quercus* (Hans-LanM) has an oligomeric state
sensitive to rare-earth ionic radius [@mattocks2023enhanced]. The La(III)-induced
dimer is more than 100-fold tighter than the Dy(III)-induced one, and the route
by which a picometre-scale difference in ionic radius reaches a protein-protein
interface is a "carboxylate shift" that rearranges second-sphere hydrogen
bonding. The site itself barely notices which lanthanide it holds; the interface
between two copies of the protein notices a great deal.

**What the \>100-fold number is, and what it is not.** It is the ratio of two
*dimerization* affinities, measured for La(III) against Dy(III). It is not a
{index}`separation factor <separation factor>`, and La and Dy are not adjacent
— they sit on opposite sides of the light/heavy split, nine places apart in the
series and about 0.12 Å of six-coordinate ionic radius apart, against the
~0.012 Å that separates a genuinely adjacent pair. Quoting it as "a separation factor above 100 for
adjacent lanthanides", as a good deal of secondary literature does, misstates
both the quantity and the pair. Anyone tempted to do so should look at the
separation factors the same paper actually measured for that same protein:
8.12 ± 0.40 (Hans-LanM) and 12.7 ± 1.3 (the R100K variant) for Nd/Dy, tabulated
below. Roughly an order of magnitude, on a light/heavy pair — not a hundredfold,
and not on neighbours.

The point of the dimerization mechanism is not the size of that ratio; it is
that the ratio exists at all in a system whose *binding site* is nearly
indifferent to which lanthanide it holds. The same paper measured the
prototypal *Methylorubrum extorquens* lanmodulin (Mex-LanM) at only about a
fivefold preference for light over heavy rare earths, with all lanthanides and
Y³⁺ inducing essentially the same conformational change [@mattocks2023enhanced].
Moving the discrimination from the first coordination sphere to the protein
interface is what buys the improvement.

**Separation factors actually measured, with the pair named and the pair type
stated.** These are the numbers the book stands behind; every one is a
distribution-ratio-based separation factor from the cited primary work.

| System | Pair | SF | Pair type | Conditions |
| ------ | ---- | -- | --------- | ---------- |
| Hans-LanM column [@mattocks2023enhanced] | Nd/Dy | 8.12 ± 0.40 | Light/heavy split | Binary Nd/Dy, immobilized protein, 0.9 mL column |
| Hans-LanM(R100K) column [@mattocks2023enhanced] | Nd/Dy | 12.7 ± 1.3 | Light/heavy split | Binary Nd/Dy, immobilized protein, 0.7 mL column |
| LanD–E75Q/E78A [@larrinaga2024modulating] | Ce/La | 3.0 ± 0.4 | **Adjacent** | 5 µM protein, 0.8 µM each of La-Nd, pH 6, \<1 h |
| LanD–E75Q/E78A [@larrinaga2024modulating] | Pr/Ce | 1.7 ± 0.2 | **Adjacent** | as above |
| LanD–E75Q/E78A [@larrinaga2024modulating] | Nd/Pr | 1.4 ± 0.2 | **Adjacent** | as above |
| LanD–E75Q/E78A [@larrinaga2024modulating] | Nd/La | 7.3 ± 0.9 | Three elements apart | as above |

The last three rows are the honest headline: **1.4 for Nd/Pr, 1.7 for Pr/Ce,
3.0 for Ce/La**. Until the dimerizing lanmodulins discussed below they were the
only adjacent-pair separation factors any protein system had produced, and
3.0 remains the largest. That range sits squarely inside the 1.5-3.0 band
[](#solvent-extraction-fundamentals) gives for conventional organophosphorus
extractants — not two orders of magnitude above it. The LanD authors make
exactly this comparison themselves: their separation factors beat
{index}`HDEHP`/D2EHPA and PC88A and are comparable to next-generation
diglycolamides. That is a real achievement, and a far smaller one than
"SF \> 100 for adjacent lanthanides."

Two further cautions. First, LanD is a *different protein* from lanmodulin — a
periplasmic lanthanide chaperone from the same uptake gene cluster, with a
surface-exposed site that supplies only four ligands — so its numbers are not
lanmodulin's. Second, the LanD separations were run on 0.8 µM metal in 5 µM
protein by ultrafiltration; nothing at that scale has been demonstrated on a
process stream. What is genuinely attractive is that both systems are
all-aqueous, need no organic diluent, and reach equilibrium in under an hour
rather than the 24 h typical of synthetic ligand assays.

Where these results *do* deliver a large effect is on purity in a single stage,
because a column amplifies a modest SF over many theoretical plates. Immobilized
Hans-LanM, loaded with a model electronic-waste mixture of 95% Nd and 5% Dy,
upgraded Dy from 5% to 83% purity and recovered Nd at 99.8% purity in one pass;
the R100K variant achieved baseline separation of Nd and Dy to \>98% purity and
\>99% yield in a single stage [@mattocks2023enhanced]. That is the correct way to
state the result: a modest separation factor plus a column, on a light/heavy
pair.

The adjacent *heavy* pairs — Dy/Ho, Ho/Er — are where the separation problem is
hardest and where the industrial cascades are longest, and until recently no
protein had been shown to touch them. The dimerizing lanmodulins Al-LanM and
Xan-LanM now do: the average adjacent-element separation factor for Al-LanM and
its structure-guided variants across the eleven elements Nd to Lu is 2.1, and
tandem dimers immobilized so they self-dimerize on the column separate Y, Dy,
Gd, Sm and Nd from one another to \>95% purities from an allanite-derived
leachate with one pH step per element [@choi2026near]. An SF of 2.1 is inside
the conventional 1.5-3.0 band rather than above it; what has changed is that a
protein now reaches the heavy end at all, and that engineered dimerization is a
handle on selectivity in its own right --- on-column dimerization nearly doubles
SF(Nd/Dy) relative to the immobilized monomer.

### Protein Engineering and Variants

Two residues in each EF-hand loop have been mutated systematically, and between
them they map what the protein is doing. The prolines, unique to lanmodulin
among EF-hand proteins, are what keeps calcium out: replacing them with alanine
moves the calcium response from near-millimolar into the micromolar range while
the picomolar lanthanide affinity survives [@cotruvo2018lanmodulin]. The
conserved aspartate at the ninth position of each loop (D9) sets the affinity
itself, and the loss is graded by how much room the substitute takes up --- about
2-fold for Asp→Asn, 20-fold for Asp→Ala, and up to 100-fold for the bulkier
Met, SeMet and His, as tabulated by Yao and co-workers
[@yao2025computationally].

The computational work that assembled those numbers makes a point worth
carrying beyond lanmodulin. Molecular dynamics on the wild-type protein and five
EF-hand variants reproduces the measured apparent dissociation constants, and it
does so only when residues *outside* the direct coordination motif are included:
a point mutation at D9 propagates a long-range structural perturbation that
shows up as altered helicity elsewhere in the chain, which circular dichroism
also sees [@yao2025computationally]. The practical consequence is that a
protein separation ligand cannot be designed by counting donors in the first
coordination sphere, and the LanD result already made the same argument from the
other direction --- a site supplying only four ligands, weak by any first-sphere
standard, delivers the best adjacent-pair separation factors in the field
because the discrimination lives in a dimer interface rather than in the site
[@larrinaga2024modulating].

### Practical Implementation

The column form of this chemistry was established by Dong and co-workers at
Lawrence Livermore and Penn State, and it is the paper to read if the question
is what a protein separation looks like as a unit operation rather than as a
binding curve [@dong2021bridging]. A lanmodulin carrying a C-terminal cysteine
on a GSG spacer is clicked onto agarose microbeads by thiol-maleimide
chemistry — chosen over physical adsorption or entrapment because a
site-specific covalent link presents the protein accessibly and survives the low
pH and high ionic strength the column is meant to see. Roughly 97 % of the added
protein loads within three hours, giving an immobilization density of 2.47 ±
0.54 µmol LanM per mL of resin.

**Capacity, and a discrepancy worth carrying forward.** The column adsorbs 5.77
± 0.67 µmol Nd per mL, close to a 2:1 stoichiometry of Nd per immobilized LanM.
In solution the same protein binds three equivalents. The authors attribute the
missing site to EF hand 1, the weakest of the three, which they argue is not
stably occupied under flow at pH ≤ 5. A third of the nominal capacity is
therefore lost on immobilization, and any capacity estimate carried over from
solution binding will be optimistic by about that much.

**The pH window is the whole process.** Immobilized LanM binds Nd down to pH
2.4; binding is halved at pH 2.2 and insignificant at pH ≤ 1.7. Breakthrough at
pH 5 comes at \~25 bed volumes, against 1 bed volume — the void volume — for
bare agarose. Desorption at pH ≤ 1.7 gives a sharp peak between 1 and 6 bed
volumes, with the neodymium concentrated more than tenfold relative to the feed;
at pH 2.0 the same elution tails badly and needs 16.5 bed volumes to recover
\>95 %. Ten consecutive adsorption (pH 3.0) and desorption (pH 1.5) cycles
produced no reduction in capacity, and breakthrough curves for Y, La, Dy and Lu
at pH 3 were indistinguishable from Nd's.

**Against base metals the separation is essentially complete.** With Mg, Al, Ca,
Co, Ni, Cu and Zn present at millimolar levels against 0.2 mM Nd at pH 3, Nd
broke through at 24 bed volumes and every non-REE left in the void volume; the
breakthrough and desorption profiles were indistinguishable from the
impurity-free case. This is the flat picomolar profile doing the work it is good
at, and what it is doing is a group separation.

**Within the series the results are real but bounded.** Two handles separate the
adsorbed rare earths: a stepped pH gradient, or citrate, which outcompetes LanM
for the heavies before the lights.

**Pair separations on immobilized LanM columns** [@dong2021bridging]:

| Feed | Method | Result |
| ---- | ------ | ------ |
| 78:22 Nd:Y | Two-step pH | 95.6 % Y purity and 99.8 % Nd purity |
| 78:22 Nd:Y | Citrate, then pH | 95.8 % of the Y at 99.4 %, then 99.7 % of the Nd at \>99.9 % |
| 50:50 Nd:Dy | Two-step pH | 76.2 % of the Dy at 99.9 %, 76.8 % of the Nd at 99.9 % |
| 95:5 Nd:Dy | One cycle, pH 2.2 elution | 88.6 % of the Dy, but at only 46.1 % purity |
| 95:5 Nd:Dy | Second cycle on the pooled fraction | 88 % of the Dy at 99.2 % and 82 % of the Nd at 99.9 % |

Read the yields as carefully as the purities. The 50:50 Dy/Nd result clears the
99.5 % REO salability threshold on both products, but does so on about
three-quarters of each element; the remainder sits in the overlap between the
two elution peaks. And the 95:5 feed — the composition of NdFeB magnet scrap,
where the Nd/Dy split actually matters
([](#recycling-and-urban-mining)) — does not separate in one pass at all. It
takes two. A single-stage purity quoted without its feed ratio says very little
here.

**Performance from a real and very poor feedstock.** The industrial test was a
leachate from Powder River Basin coal fly ash: about 150 µM total rare earths
against millimolar Na, Mg, Al, Ca and Sr, plus significant Zn, Ni, Cu and Mn —
0.043 mol % REE excluding monovalent ions. Rare earths broke through after 30
bed volumes while the non-REEs left in the void volume. Non-selective desorption
at pH 1.5 recovered more than 96.5 % of them in 3.9 bed volumes at 88.2 mol %
total REE purity, a 2,040-fold increase over the feed. Uranium was not
concentrated. Benchmarked against single-stage DEHPA extraction on an ash
leachate of comparable composition, purification factors against base metals ran
from 100 to 500,000 depending on the element, against 10 to 5,000 for the
solvent route — with the exception of Fe and Si, which the authors attribute to
unfilterable colloids that accumulate on the column and dissolve during the
low-pH strip, and which therefore have to be removed upstream of it.

The same PRB feed run with a two-pH desorption gave a grouped split in a single
cycle: 82 % of the heavies at 72.6 % purity at pH 2.3, then 80 % of the lights
at 98.8 % purity at pH 1.7, at about 90 % column loading. Every number in this
section comes from a column of roughly 1 mL bed volume — 0.80 to 1.0 mL — run at
0.5 mL/min, with the fly ash experiment passing 29.1 bed volumes through 0.94 mL
of resin. That is the scale at which the process exists.

Note the shape of the purity result: 0.043 mol% to 88 mol% is a concentration
factor of about 2,000, achieved in one aqueous pass. It is a *purity* figure —
rare earths against everything else — not an individual-element figure. Reading
it as an intra-series result is the same error as reading the 10⁸-fold Ca²⁺
number that way. The intra-series numbers are the ones in the
table above, and they are far more modest.

The authors' own framing is the right scale check, and it is unusually candid:
the process "should not be considered as a direct competitor for liquid-liquid
extraction — particularly with regard to processing concentrated feed solutions
from high-grade ore sources," but a scaled continuous version "would be uniquely
positioned to unlock low-grade leachate solutions that are not currently
profitable" [@dong2021bridging]. That is the conclusion the next section reaches
independently, from the binding data.

#### Where Lanmodulin Belongs in a Flowsheet

The two selectivities place these ligands at a specific and defensible point in
a process, and it is not the point solvent extraction occupies.

- **Upstream, where LanM is strong.** The output of leaching
  ([](#hydrometallurgical-leaching)) is a dilute pregnant leach solution in
  which rare earths are a minor component against Ca, Fe, Al, Mg and Si. Getting
  them out of it, cleanly and without an organic phase, is precisely a group
  separation, and it is what LanM's flat picomolar profile and acid tolerance
  buy. The competing conventional operations — oxalate or double-sulfate
  precipitation, or a dedicated impurity-rejection extraction circuit — are
  reagent-intensive and lossy.
- **Downstream, where LanM is weak.** Once a mixed rare-earth concentrate
  exists, separating it into individual elements needs an adjacent-pair
  separation factor applied over many stages
  ([](#solvent-extraction-fundamentals)). LanM's monomer supplies almost none;
  the dimerization variants supply a group-level split (light versus heavy, or
  light-lanthanide enrichment), which is a coarse cut, not a fractionation.

The honest statement is therefore that lanmodulin is a candidate to *replace the
front end* of a rare-earth flowsheet and to *feed* the cascade, not to replace
it. That is a smaller claim than "biology has beaten solvent extraction," and a
more useful one, because the front end is where the water, acid and reagent
consumption that [](#environment-techno-economics-and-life-cycle) accounts for
actually sits. It is also why the technology comparison in
[](#technology-comparison) must record the element pair
alongside any separation factor: without the pair, a group number and an
adjacent-pair number are indistinguishable on the page.

## Lanthanide Binding Tags and Peptide-Based Separation

If the useful chemistry lives in a helix-loop-helix of about a dozen residues,
there is an obvious question: does the rest of the protein have to be there?
{index}`Lanthanide binding tags <lanthanide binding tags>` (LBTs) are the answer
in its cheapest form --- short peptides lifted from the calcium-binding EF-hand
loops of calmodulin, troponin and parvalbumin, of which a troponin-derived
sequence optimized for Tb³⁺, YIDTNNDGWYEGDELLA, is the canonical example
[@li2024lanthanide]. They are far easier to make than a protein, they can be
synthesized rather than expressed, they can be evolved in a directed-evolution
loop without worrying about folding, and they can be grafted onto a surface. The
price is affinity, and the size of that price is the useful number.

### What a Peptide Costs You

Verma and co-workers took the first EF-hand loop of lanmodulin, called it LanM1,
and measured what it does both free in solution and immobilized ---
which is the condition that matters, because every separation technology built
on these ligands puts them on a solid [@verma2024investigation]. In solution, by
isothermal titration calorimetry, LanM1 binds Ce³⁺ with a dissociation constant
of 3.84 ± 1.47 µM. Immobilized on gold and read by quartz-crystal microbalance
fitted to a Langmuir isotherm, the surface-bound constants are about 0.9 µM for
Ce³⁺ and about 1.8 µM for Nd³⁺ at pH ≈ 5.5. Set those beside the intact
protein's tens-to-hundreds of picomolar and the cost of cutting the protein down
to one loop is four to five orders of magnitude of affinity.

What survives the cut is the group selectivity, which is the more valuable half.
Surface-bound LanM1 shows no measurable affinity for calcium or copper even at
29 µM, and Ce³⁺ stops binding below pH 2, which supplies a pH-swing regeneration
step for free. Grafted onto gold nanoparticles the peptide reaches a saturated
capacity of about 3.5 µmol REE per gram --- and, critically, that figure is a
saturation value, measured over feed concentrations from 20 to 125 µM where the
isotherm has plateaued, not a single-point uptake quoted without its equilibrium
concentration. Two cautions came out of the same work. Loading the peptide too
densely on the surface almost eliminates REE binding, so surface coverage is a
process variable and not a thing to maximize. And high affinity is not the same
as high selectivity between rare earths: nothing in this work separates one
lanthanide from another.

### Interfacial Separation with Peptide Surfactants

Lanthanide binding tags are amphiphilic, so a solution of them will build a
layer at an air-aqueous interface, and the composition of that layer need not
match the bulk. Ortuno Macias and co-workers studied this on a *flat* interface
--- surface tensiometry, X-ray reflectivity, X-ray fluorescence near total
reflection, and molecular dynamics --- rather than in a foam
[@li2024lanthanide]. The peptide complexes the trivalent cation in the bulk and
the complex then adsorbs, with the binding pocket intact on adsorption. What
decides whether the layer is selective is the net charge the complex carries. A
negatively charged complex pulls excess cations to the interface by
indiscriminate Coulombic attraction, and the selectivity is destroyed; at a
peptide net charge of −3 the complex is neutral, and a 1:1 cation-to-peptide
surface ratio is reached.

The demonstrated separation is a switch rather than a fractionation. From an
equimolar Tb³⁺/La³⁺ mixture the adsorbed layer enriches in Tb³⁺ when the bulk
peptide is saturated, and inverts to La³⁺ when it is undersaturated, because the
La³⁺ complex is the more surface-active of the two. That is an interesting
handle and an awkward one: the direction of separation depends on a bulk
concentration ratio that a real feed would not hold constant.

A foam column is the obvious vehicle and it does not yet exist. The nearest
thing is a follow-up from the same group showing that glutaraldehyde
cross-linking of the adsorbed peptide-REE complexes thickens the interfacial
film and stiffens it in both dilation and shear, which is what a foam needs to
survive drainage [@ortunomacias2024enhanced]. That work is still pendant-drop
tensiometry and X-ray reflectivity on a flat interface; it substitutes a
cross-linker for the polymers, surfactants and particles that usually stabilize
a froth, and it stops short of reporting a foam separation.

### Immobilized Peptides and Mineralizing Peptides

Two other peptide formats have been demonstrated at bench scale. Sree and
co-workers immobilized lanthanide binding peptides on microbeads and let gravity
do the phase separation, avoiding any external field or stimulus; they showed
enrichment of europium and terbium, recovery by a change in solution conditions,
and reuse of the beads over successive cycles, with no measurable binding of
common industrial non-REE ions [@sree2023gravity].

The mineralization route inverts the usual logic. Rather than holding the metal
on a ligand and eluting it, the lanthanide ion mineralization peptide (Lamp) of
Hatanaka and co-workers is designed to make the metal fall out of solution
[@hatanaka2017rationally]. The sequence is short:

1. Lamp promotes the formation of rare-earth hydroxide species in the aqueous
   phase;
2. it binds them into hydrophobic complexes;
3. those complexes are insoluble and accumulate spontaneously as a precipitate,
   at pH ≈ 6 and with no added energy.

The attraction is that the product is a solid, so the separation and the
recovery are the same step, and the concept transfers to peptides displayed on
synthetic macromolecules and proteins. The authors propose it for seawater and
industrial wastewater. The limitation is inherent to the mechanism: precipitating
a hydroxide is a group operation, and nothing in this route offers a route to
separating one lanthanide from another.

## EF-Hand Proteins: Why Calcium Chemistry Nearly Works

Everything above is built on a motif that evolved to bind calcium, and it is
worth being precise about why that motif is such a good starting point and why
it is not, on its own, enough. The EF-hand is a helix-loop-helix that closes six
or seven oxygen donors around a divalent ion. A trivalent lanthanide of similar
radius is a better fit for that pocket by simple electrostatics, and ordinary
EF-hand proteins reflect this by binding lanthanides only about 100- to
1000-fold more tightly than calcium [@yao2025computationally]. Lanmodulin's
eight orders of magnitude is therefore not a property of the EF-hand; it is what
the prolines and the extra carboxylate add on top of one.

Nikolova and co-workers computed the Ca²⁺/Ln³⁺ competition across the whole
series in model calcium-signalling and calcium-buffering sites, and their result
explains both halves of this chapter's argument at once [@nikolova2023lanthanides].
The dominant determinant of whether a lanthanide displaces calcium is the *net
charge* of the binding pocket: the more negative, the more the trivalent ion is
favoured. Solvent exposure modulates it, with buried sites at net charge −3 or
−4 strongly lanthanide-selective and sites at −1 preferring calcium. That is the
group selectivity, and it is a charge argument, which is why it is large. Within
the series, by contrast, the competition is set by the balance of two effects
that pull in opposite directions --- an electronic term favouring the heavier
lanthanides and a solvation term favouring the lighter ones. Two large opposed
terms nearly cancelling is exactly the recipe for a small net preference, and
that is the fivefold.

There is a second reason not to read too much into calcium-protein structures.
Lanthanides are used routinely as calcium substitutes in EF-hand proteins, as
luminescent probes and as heavy-atom replacements, on the assumption that the
substitution is isomorphous. Edington and co-workers tested that assumption on
calmodulin by ultrafast two-dimensional infrared spectroscopy backed by
electronic-structure calculation --- a vibrational method, not crystallography
--- and found it fails [@edington2018coordination]. Lanthanide coordination
distorts the binding site: it disrupts the bidentate Glu12 geometry and leaves
the site with greater conformational flexibility and larger structural
fluctuations than calcium does. Their own generalization is the one to carry
forward, that "seemingly innocuous ligand substitutions can significantly alter
protein conformation." A lanthanide-substituted structure is evidence about the
substituted protein, not about the calcium one, and a separation ligand designed
from the calcium structure is being designed from the wrong geometry.

## Biosurfactants for REE Separation

### Rhamnolipids: Group-Selective, but Not for the Group You Want

Rhamnolipids are glycolipid biosurfactants from *Pseudomonas aeruginosa*, and
Hogan and co-workers measured conditional stability constants for 26 metals
against monorhamnolipid by a resin-based ion-exchange method
[@hogan2017rhamnolipid]. The constants fall into three clean groups. The
strongly bound group spans log β = 9.82 down to 8.20 and contains, in the
paper's own order:

| Rank | Species |
| ------ | --------- |
| 1 | UO₂²⁺ (9.82, highest) |
| 2-6 | Eu³⁺, Nd³⁺, Tb³⁺, Dy³⁺, La³⁺ |
| 7-9 | **Cu²⁺, Al³⁺, Pb²⁺** |
| 10-12 | Y³⁺, Pr³⁺, Lu³⁺ (8.20, lowest of the group) |

Below them sit the moderately bound metals --- Cd²⁺, In³⁺, Zn²⁺, Fe³⁺, Hg²⁺ and
Ca²⁺ at log β = 7.17-4.10 --- and the weakly bound ones, Sr²⁺, Co²⁺, Ni²⁺, Ba²⁺,
Mn²⁺, Mg²⁺, Rb⁺ and K⁺ at 3.95-0.96. A mixed-metal study in the same work
confirmed that monorhamnolipids preferentially take the high-log β metals, so
the ranking is predictive and not just a table of constants.

Read the ranking rather than the headline. Rare earths do sit in the strongly
bound group, and they are separated from calcium by four to five orders of
magnitude, which is a real group selectivity of the kind this chapter has been
crediting. But copper, aluminium and lead sit *inside* the rare-earth band,
above Y³⁺, Pr³⁺ and Lu³⁺, and uranyl sits above everything. Rhamnolipid is a
group-selective collector for hard, highly charged cations; it is not a
rare-earth-selective one, and a feed carrying Cu, Al or Pb --- which is to say
most leach liquors, per [](#hydrometallurgical-leaching) --- will compete
directly. The twelve strongly bound species span 1.6 log units in total, so the
eight rare earths among them span less than that, which is why the comparison
table at the end of this chapter rates biosurfactant intra-group selectivity as
weak.

### Sophorolipids and Saponin

Sophorolipids, from the yeast *Starmerella bombicola*, are the hydrophobic
counterpart to the hydrophilic rhamnolipids, and mixtures of the two perform
robustly in applications where neither alone does [@nguyen2011characterization].
That complementarity is the argument for using them together as flotation
collectors. It is also as far as the verified record goes here: no primary
measurement of sophorolipid collector performance on a rare-earth mineral could
be traced for this chapter, so no flotation recovery, contact angle or
comparison against a petroleum-derived collector such as benzohydroxamic acid is
quoted. The reader should treat sophorolipid flotation of rare-earth minerals as
a proposal rather than a result.

Saponin, a non-ionic plant biosurfactant, has been tested against rhamnolipid
for leaching rare earths out of soil [@zhou2018leaching]. Flushing a 15 cm bed
of soil with 400 mL of 25 g/L saponin at pH 5.5 gave cumulative removals of
35.3 % La, 26.1 % Ce, 31.5 % Y and 30.8 % Eu; rhamnolipid at 10 g/L and pH 7
managed 7.3 %, 6.1 %, 7.5 % and 7.7 %, and deionized water removed a negligible
amount. Saponin is thus four to five times the better agent, and the mechanism
offered is 1:1 complexation of the trivalent ion by the saponin, drawing rare
earths out of the acid-soluble *and* reducible fractions where rhamnolipid
reaches the acid-soluble and residual ones.

Two qualifications matter more than the numbers. The soil is **spiked, not
contaminated**: unpolluted agricultural soil from Ganzhou was dosed with
lanthanide nitrates and air-dried to 166 mg/kg La, 196 Ce, 78 Y and 112 Eu, and
the paper's own table calls it simulated. And the work is a 5 cm column holding
80 g of soil. That does not weaken the conclusion, it sharpens it: soil washing
with a biosurfactant is a remediation operation, not a production one. The
target is lowering a soil concentration, the leachate is dilute, and the rare
earths recovered are a by-product of the cleanup. The paper also quotes maximum
removals of 58.05 % La and 57.78 % Ce; those are prior studies it cites, not its
own result, and should not be attributed to it.

(siderophores-and-the-boundary-with-leaching)=
## Siderophores and the Boundary with Leaching

Bioleaching of primary rare-earth ores --- the mechanisms of acidolysis,
redoxolysis and complexolysis, the organisms that run them, and the blunt
question of whether any of it dissolves an ore fast enough to displace acid ---
belongs to [](#hydrometallurgical-leaching), and the quantitative answer given
there is deflationary: measurably more dissolution than an abiotic control, over
weeks rather than hours, into milligram-per-litre liquors. This section does not
revisit that. It covers the *molecules* --- what the organisms secrete, and what
those ligands do once isolated from the organism that made them.

{index}`Siderophores <siderophore>` are the clearest case. They are extracellular
chelators that aerobic microorganisms secrete to solubilize iron, and their
affinity for hard trivalent cations does not stop at Fe³⁺. Osman and co-workers
isolated the siderophore of a rhizosphere *Aspergillus niger* that produces
87 % siderophore units under iron-deficient conditions, established from its
FeCl₃ spectrum, its pH-independent absorbance maximum at 450 nm and its FTIR
and NMR signatures that it is a trihydroxamate of the ferrichrome type, and then
applied the *purified* ligand to Egyptian phosphorites from the Abu Tartur mine
[@osman2019characterization]:

| Element | Removal efficiency |
| --------- | ------------------- |
| Uranium | 69.5 % |
| Samarium | 66.7 % |
| Thorium | 55.0 % |
| Lanthanum | 51.0 % |
| Cerium | 50.1 % |

Two features of that table matter more than the rare-earth numbers in it. The
first is that this is a purified chelator applied to a phosphate rock, not a
live-culture leach of a rare-earth ore, so it is not in tension with the ore
result in [](#hydrometallurgical-leaching); it is a different experiment
answering a different question. The second is the ordering. Uranium is removed
better than any rare earth and thorium better than lanthanum or cerium.
Hydroxamate siderophores are excellent hard-cation chelators and correspondingly
indiscriminate among the actinides and lanthanides, which means any process
built on them inherits a radionuclide-management problem of the sort
[](#environment-techno-economics-and-life-cycle) describes, rather than escaping
one.

Actinobacteria have also been screened on bastnäsite-bearing rock, with
*Streptomyces* strains identified as siderophore producers and with secreted
organic acids and complexing ligands assigned as the dominant extraction agents
[@zhang2018bioleaching]. The best producer, *Streptomyces* sp. FXJ1.172, made
200 µmol/L of a desferrioxamine-family hydroxamate — **in growth medium, with no
rock present.** In the presence of the bastnäsite-bearing rock siderophores were
not readily detected at all, even after a twenty-fold concentration of the
supernatant. The titre and its disappearance have to be quoted together; the
first number alone would misrepresent the paper.

The recovery figures are the most deflationary in this chapter. Over twenty days
the bioleached liquors reached 56 to 342 µg/L total REE in a nutrient-rich
medium and 548 µg/L for the one strain that grew in an oligotrophic one, for a
leaching efficiency of **0.008 to 0.08 %** — and the authors note that even that
is an underestimate, because rare earths are lost to cell-surface sorption and
to re-precipitation as secondary minerals along the way. Those liquors are
sub-milligram-per-litre, an order of magnitude below the milligram-per-litre
leach liquors [](#hydrometallurgical-leaching) treats as dilute. The one
encouraging result is that the leaching is not merely acid attack — the
bioleached concentrations exceeded abiotic controls at the same pH, "suggesting
that pH was not the only factor" — and that it fractionates, preferentially
mobilising the heavy rare earths.

The methylotrophs are the interesting outlier, because they are the organisms
that gave us lanmodulin in the first place. *Methylobacterium extorquens* AM1
acquires lanthanides from its environment as a matter of metabolic necessity ---
its methanol dehydrogenase needs one --- and it is therefore the only common
bioleaching chassis whose selectivity for rare earths is native rather than
engineered. What has been built on that is described under synthetic biology
below.

## Microbial Biosorption

{index}`Biosorption <biosorption>` is passive: a metabolically independent physicochemical
uptake onto cell-surface carboxylates, phosphates and hydroxyls, combining
adsorption, {index}`ion exchange`, surface complexation and
{index}`precipitation` [@vitova2024microbial; @giese2020biosorption]. Because
the cells need not be alive, spent biomass from a fermentation industry is a
legitimate feedstock, and that --- not performance --- is the argument for it.
The surface area per unit mass is large, the functional groups are abundant, the
material is biodegradable and non-toxic, and it costs nothing.

The selectivity is where the literature has to be read carefully, and the
cleanest comparison is Breuker and co-workers, who ran bacteria, fungi and algae
side by side under standardized acidic conditions of the sort a bioleaching
liquor actually presents [@breuker2020biosorption]. Different organisms prefer
different parts of the series: the Gram-positive *Bacillus subtilis* favours the
heaviest elements, ytterbium and lutetium, more strongly than the Gram-negative
*Leisingera methylohalidivorans* and *Phaeobacter inhibens*; the fungi
*Catenulostroma chromoblastomyces* and *Pichia* sp. prefer the middle rare
earths; algae performed poorly across the board. For *B. subtilis* and *Pichia*,
living biomass outperformed dead. That is a genuine, mechanistically
interesting spread, and it is also the whole of it: no element-pair separation
factor is reported.

The one biosorption result that reads as a separation is Bonificio and Clarke's
[@bonificio2016rare]. *Roseobacter* sp. AzwK-3b immobilized on an assay filter
adsorbs lanthanides and releases them as a function of pH, with the desorption
order tracking the basicity of the individual lanthanides. Starting from a
solution containing equal concentrations of every lanthanide --- so about 21 %
of the three heaviest --- preprotonating the bacteria and running two passes
concentrates the eluate to nearly 50 % Tm, Lu and Yb. The authors' comparison to
industrial practice is on the specific basis of that enrichment in two passes.
The important qualification is that a heavy-versus-light grouping is not an
adjacent-pair split; two passes from 21 % to 50 % is real, and it is the coarse
cut, not the cascade.

Engineering the surface improves the capture without changing that conclusion.
Park and co-workers displayed 16 copies of a lanthanide binding tag on the *E.
coli* OmpA protein and tested it on leachates from mine tailings and rare-earth
deposits, where it raised the distribution coefficients of individual rare
earths 2- to 10-fold over the unmodified control and raised the affinity of the
cell surface for rare earths over every non-REE **except copper**
[@park2017recovery]. The copper exception is the part usually dropped in
retelling and the part a real feed would notice. The LBT display also
strengthened binding monotonically with decreasing ionic radius, which is a
genuine handle on separating heavies from lights.

Among non-bacterial biomass, phosphorylated dry baker's yeast is the most
developed. Ojima and co-workers treated *Saccharomyces cerevisiae* with
cyclo-triphosphate to a total phosphorus content of about 1.0 mmol per gram dry
cell weight, doubling the magnitude of the zeta potential to −45 mV
[@ojima2018recovering]. The resulting cells adsorbed Cd²⁺, Cu²⁺, Pb²⁺ and Zn²⁺
to about 1.0 mmol/g, and adsorbed Ce³⁺, Dy³⁺, Gd³⁺, La³⁺, Nd³⁺, Y³⁺ and Yb³⁺
efficiently; from a mixed solution the trivalent rare earths were taken up
preferentially over the divalent heavy metals, and 0.1 M HCl strips the metal
back off. The mechanism is electrostatic, so the selectivity is a charge
selectivity, and it is exactly as coarse as that implies.

Phototrophic biomass illustrates the trap in quoting a capacity. Heilmann and
co-workers measured maximum sorption capacities for the moss *Physcomitrella
patens* and two microalgae from adsorption isotherms, and *P. patens* was the
best of the three at 0.74 ± 0.05 mmol/g for Nd³⁺ and 0.48 ± 0.05 mmol/g for
Eu³⁺ [@heilmann2021rare]. Those are isotherm-derived maxima rather than
single-point uptakes, which is why they are quoted here. But the same paper
measured the same biomass against metals that would share a wastewater with the
rare earths, and found *higher* capacities for Au³⁺ (1.59 ± 0.07 mmol/g) and
Pb²⁺ (0.83 ± 0.02 mmol/g). The microalgae showed the same ordering. A capacity
figure for a single element, quoted alone, says nothing about whether the
sorbent would pick that element out of a mixture --- and here it would not.

## Phytomining and Hyperaccumulator Plants

Phytomining grows a hyperaccumulator on ground that could not support a mine,
harvests it, and treats the biomass as an ore. The sequence is
phytoextraction into the plant tissue, enrichment of the harvested material into
a "bio-ore", and extraction of the metal from that
[@dinh2022phytomining]. The case for it is not throughput; it is that the land
in question --- former tailings, contaminated soil --- has no competing use and
that the operation remediates while it produces.

The fern *Dicranopteris linearis* is the best-studied case. It grows naturally
on former mine tailings in southern China, and the rare-earth concentration in
its aerial parts exceeds that of common low-grade ore, which is what makes the
biomass a candidate bio-ore rather than a curiosity [@jally2021method]. It
survives its own uptake by fixing the metal in a silicon-pectin matrix, which is
the detoxification mechanism [@zheng2023rare].

Jally and co-workers worked out what to do with the harvest, and the hard part
turns out not to be the rare earths but the aluminium [@jally2021method]. The
biomass is incinerated to ash, which raises the bio-ore grade and generates
usable heat. Aluminium is then dissolved out of the ash with 6 M sodium
hydroxide at 80 °C --- the step that limits the whole process, because insoluble
aluminosilicates form and cap how much aluminium can be removed. The
rare-earth-rich residue is rinsed, a step they designed carefully because it
does most of the grade improvement. A mild nitric acid leach at 25 °C and pH 4.8
then produces a solution free of aluminium and carrying 74 % of the rare earths.
The interesting thing about that flowsheet is how conventional it is: a bio-ore
still needs an incinerator, a caustic digest and an acid leach, and the plant has
replaced the mine, not the hydrometallurgy.

A 2025 result may eventually change the last step. He and co-workers found
nanoscale {index}`monazite` --- dendritic nanocrystals, formed in extracellular
tissue at ambient temperature by biologically induced mineralization coupled to
a non-equilibrium self-organization process --- in the living fern *Blechnum
orientale* [@he2025discovery]. This is the first report of rare-earth mineral
crystals forming inside a living plant. It matters twice over: it identifies a
previously unrecognized, plant-mediated pathway for critical-mineral formation
in the supergene environment, which bears on how rare earths are enriched and
sequestered during chemical and biological weathering; and it raises the
possibility of recovering a functional mineral directly from the plant instead
of leaching the biomass, which is the paper's own argument for the feasibility
of phytomining. Whether biogenic monazite carries the thorium and uranium that
geological monazite does is not addressed, and that question decides whether the
route avoids the radioactive-residue problem of
[](#environment-techno-economics-and-life-cycle) or merely relocates it.

Against all of this stands the arithmetic. No peer-reviewed study establishes
commercial viability for rare-earth phytomining; accumulation takes a growing
season; the land area required to feed even a small separation plant is large;
and the biomass processing above is itself a chemical plant. Phytomining is a
remediation technology with a saleable by-product, and it is most defensible
when described that way.

## Biopolymer Adsorbents

Chitosan is the second most abundant biopolymer, it is non-toxic and
biodegradable, and its amine and hydroxyl groups chelate trivalent cations, so
it recurs constantly in the recovery literature as a support
[@kore2024application]. Cellulose and alginate play the same role
[@doyo2023advances]. The chemistry done to them is a short and repetitive list:
cross-linking with glutaraldehyde, which forms covalent bonds through the amine
groups and buys mechanical strength and chemical stability at the cost of some
of those same binding sites; functionalization, most often with EDTA, to install
a denser set of donors; ion imprinting, in which the polymer is cured around a
template ion to leave a cavity shaped for it [@bulin2025preparation]; grafting,
typically acrylic acid, sometimes onto a dialdehyde-cellulose-chitosan hybrid
formed by a Schiff base reaction [@elsayed2023sustainable]; and compositing with
graphene oxide, {index}`metal-organic frameworks <metal-organic framework
(MOF)>`, layered double hydroxides, carbons or clays, usually to add surface
area or a magnetic recovery handle.

Earlier versions of this chapter carried a table of adsorption capacities for
these materials --- several hundred milligrams per gram for Ce(III) and Nd(III),
and a chitosan "adsorption capacity" of 85-100 %. Those numbers have been
deleted, and the reason is worth stating because it applies to a large fraction
of the adsorption literature. A capacity in mg/g is meaningless without the
equilibrium concentration it was measured at and the model it was fitted with: a
Langmuir *q*ₘₐₓ extrapolated from a 500 mg/L feed and a single-point uptake from
a 5 mg/L feed differ by an order of magnitude and are routinely tabulated in the
same column. None of the values previously quoted here could be traced to a
primary measurement with its isotherm conditions attached. The "85-100 %" figure
is worse than untraceable: it is a percentage, not a capacity, and a percentage
removal without a feed concentration and a solid-to-liquid ratio is not a
measurement of anything.

What can be said without a number is the shape of the field. These are
high-capacity, low-selectivity sorbents. They work at near-neutral pH, which
puts them downstream of any acid leach and effectively confines them to
wastewater polishing and dilute secondary streams. Not one of them has a
reported element-pair separation factor. They are competing with ion exchange
resins ([](#displacement-chromatography)) on cost of substrate rather than on
performance, and the case for them is that chitin is a fishery waste.

## Synthetic Biology and Metabolic Engineering

The most convincing biological results in this chapter come from treating the
organism, not the ligand, as the thing to engineer. Two programmes show what
that buys.

*Gluconobacter oxydans* is the workhorse for leaching secondary feedstocks
because it excretes gluconic acid, and Schmitz and co-workers took a
whole-genome approach to improving it. They first built a knockout collection of
single-gene transposon disruption mutants and found 304 genes whose disruption
alters production of the acidic biolixiviant [@schmitz2021generation]. The
screen produced one negative result and one positive one, and both are
mechanistically informative. Losing the biosynthesis of the cofactor
pyrroloquinoline quinone, or losing the PQQ-dependent membrane-bound glucose
dehydrogenase that uses it, nearly eliminates bioleaching --- so the entire
effect runs through one enzyme. Disrupting the phosphate-specific transport
genes *enhances* bioleaching, by up to 18 %. Acting on that, the same group
deleted *pstS* and overexpressed *mgdh*, and the resulting strain improves
rare-earth extraction by up to 73 % [@schmitz2025high]. A 73 % improvement on a
process that dissolves milligram-per-litre quantities over weeks
([](#hydrometallurgical-leaching)) is a genuine and useful gain that does not
change the order of magnitude of the result.

The methylotroph platform is the more radical proposal, because it
consolidates leaching and recovery into one organism. Good and co-workers
showed that *M. extorquens* AM1 grows on electronic waste as its sole source of
rare earths and that this scales to 10 L with consistent metal yields, with no
strong acid and no elevated temperature [@good2024scalable]. Adding organic
acids raises leaching non-specifically; making it *specific* requires
engineering, and they did it by overproducing the organism's own rare-earth
binding ligands --- lanthanophores --- and pyrroloquinoline quinone. The
recovered metal is stored intracellularly in polyphosphate granules, and
knocking out exopolyphosphatase increases accumulation further, which ties the
uptake directly to phosphate metabolism. The same organism grows on pulverized
smartphones. Ten litres is the largest operation reported anywhere in this
chapter, and it is a culture volume, not a separation.

The wider synthetic-biology toolkit being brought to bear on electronic waste
--- metabolic pathway engineering, synthetic gene circuits, cell-surface
display, directed evolution --- is surveyed by Bai and co-workers, whose stated
targets are higher metal selectivity, better tolerance of acidic conditions and
faster kinetics in complex matrices across bioleaching, biosorption and
bioaccumulation [@bai2025harnessing]. Those are objectives rather than
achievements, and the honest reading is that the field has demonstrated the
front end of the problem and not the back end. An earlier version of this
chapter tabulated single-element purities of 99.9 % for europium, 97.1 % for
lanthanum and 92.7 % for dysprosium from a bioconjugated affinity column. No
source for those figures could be identified and they have been removed.

(green-solvents-des-and-ils)=
## Green Solvents: Deep Eutectic Solvents and Ionic Liquids

{index}`Deep eutectic solvents <deep eutectic solvent>` (DESs) and
{index}`ionic liquids` (ILs) are adjacent to this chapter rather than in it ---
they are not biological --- but they arrive with the same claim, that a
sustainable medium can replace kerosene and organophosphorus extractants, and
they are worth including because they are the case where that claim has been
tested longest [@deng2025application; @okamura2020progress]. Both are liquid over
a wide temperature range, non-volatile, non-flammable and ionically conductive,
which removes the fire and vapour-emission hazards of a conventional solvent
extraction house ([](#solvent-extraction-fundamentals)). DESs are the cheaper
half of the pair: two components mixed, no synthesis, no purification, at the
cost of being generally less stable than an IL. Natural deep eutectic solvents
narrow the components further to sugars, organic acids, amino acids and organic
bases. Both classes have been applied to rare earths as lixiviants for
caustic-treated concentrates [@shakiba2023application] and as extractants from
nitrate media [@zinoveva2024extraction; @lu2025separation; @alguacil2023work].

"Green" should not be read as "benign". Amino-acid-based DESs, chosen precisely
because their components are natural and biodegradable, have been measured as up
to 10⁵ times more toxic than conventional choline-chloride-based DESs
[@li2022high]. The provenance of a molecule is not evidence about its toxicology.

(industrial-challenges)=
### Why None of This Has Reached a Plant

After twenty years of academic work on ILs and DESs in extractive metallurgy
there has been no commercial breakthrough, and Binnemans and Jones --- authors
of a good deal of that work themselves --- set out eight reasons why
[@binnemans2023ionic]. High viscosity, which penalizes mass transfer and pumping
throughout a mixer-settler train. Limited chemical stability under real
metallurgical conditions. Difficulty recycling and reusing the solvent, which is
fatal when the solvent is the expensive part of the inventory. No demonstrated
unit processes or flowsheets at pilot scale. Insufficient physical-property data
to do engineering with. The administrative burden of licensing and safety
permits for a novel substance. Very high cost at large scale. And, most
damningly, minimal added value over state-of-the-art hydrometallurgy. Their
conclusion is that innovation in hydrometallurgy is unlikely to come from
these solvents, and that the community's expertise would be better spent on
speciation and chemical thermodynamics of ordinary aqueous systems.

That verdict is a useful calibration for this whole chapter. Every objection on
Binnemans and Jones's list --- cost, stability, recyclability, missing
engineering data, absence of pilot-scale flowsheets --- applies with at least
equal force to a purified protein. The difference is that the protein has a
demonstrated selectivity no conventional reagent can match, and the deep
eutectic solvent, on the evidence, does not.

## Comparison of Biological Separation Technologies

Selectivity is split into two columns, because collapsing them into one is the
error this chapter opened by warning against. *Group* selectivity is
rare-earths-versus-everything-else; *intra-group* selectivity is one lanthanide
versus its neighbour. A technology can be world-leading in the first column and
useless in the second, and lanmodulin is.

| Technology | Group selectivity (REE vs. non-REE) | Intra-group selectivity (Ln vs. Ln) | Largest scale reported in this chapter |
|----|----|----|----|
| Lanmodulin | Exceptional (~10⁸ vs. Ca²⁺) | Weak: ~5× light-over-heavy for the native protein; SF = 8-13 for Nd/Dy on a dimerizing-variant column | 0.9 mL immobilized-protein column [@mattocks2023enhanced] |
| LanD (dimerizing chaperone) | Not characterized | SF 1.4 (Nd/Pr) to 3.0 (Ce/La) — the best protein adjacent-pair figures reported | Bench, µM scale |
| LBT Peptides | High | Not demonstrated | Not reported |
| Biosurfactants | Moderate: rare earths bind strongly, but Cu, Al, Pb and UO₂²⁺ bind as strongly or more so [@hogan2017rhamnolipid] | Weak: all eight rare earths measured fall inside a band under 1.6 log β units wide | Bench; no separation operation reported |
| Siderophore Bioleaching | Moderate | Not demonstrated | Not reported |
| Microbial Biosorption | Variable | Not demonstrated | Not reported |
| Phytomining | Low-Moderate | None (bulk uptake) | Not reported |
| Chitosan Adsorbents | Moderate | Not demonstrated | Not reported |
| Engineered Microbes | High | Not demonstrated | 10 L culture [@good2024scalable] |
| DES/IL Systems | Variable | Variable | Not reported |

*"Not demonstrated" means no element-pair separation factor is reported for that
technology anywhere in this chapter; it is not a claim that the selectivity is
zero. "Not reported" in the last column means the same about scale.*

An earlier version of this table also carried columns for scalability, cost,
environmental impact and Technology Readiness Level, rating several of these
technologies at pilot or industrial scale with TRLs of 5 to 7. Nothing in this
chapter supports those ratings. The largest operation described anywhere above
is a ten-litre culture; the separations themselves run in millilitre columns.
The columns were removed rather than corrected, because a cost or a TRL that
cannot be traced to a source is a number the reader has no way to check.

The pattern in the intra-group column is the chapter's real conclusion. Biology has
produced outstanding group-separation chemistry and, so far, only the beginnings
of intra-group separation. That is a reason to put biological ligands into the
front end of a flowsheet, not a reason to expect them to retire the cascade.
