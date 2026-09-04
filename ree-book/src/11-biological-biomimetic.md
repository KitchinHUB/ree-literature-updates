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
1.4 (Nd/Pr) to 3.0 (Ce/La) [@larrinaga2024modulating], which is the same band
conventional acidic organophosphorus extractants occupy. What biology has actually delivered is a
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

This section provides an in-depth examination of biosurfactants, peptides, proteins, and related biological approaches for REE separation---representing some of the most promising sustainable technologies in this field.

(lanmodulin-structure-mechanism-and-engineering)=
## Lanmodulin: Structure, Mechanism, and Engineering
### Discovery and Properties
Lanmodulin (LanM) is a 12 kDa protein identified in *Methylobacterium extorquens*, a methylotrophic bacterium that requires lanthanides for methanol metabolism. LanM is the most selective macromolecule for REEs characterized to date, even outperforming many synthetic chelators [@deblonde2020selective].

**Key Binding Properties:**

| Property | Value | Source |
| ---------- | ------- | ------- |
| Selectivity Ln³⁺/Ca²⁺ | ~10⁸-fold (picomolar Ln³⁺ response vs. near-millimolar Ca²⁺) | [@cotruvo2018lanmodulin] |
| Dissociation constant (Kd) | Picomolar for every Ln³⁺ from La to Lu, and for Y³⁺ (reported as 0.4-10 pM across the series) | [@cotruvo2018lanmodulin] |
| Selectivity Ln³⁺/Ln³⁺ | **About fivefold**, light over heavy, for the whole series; all lanthanides and Y³⁺ induce essentially the same conformational change | [@mattocks2023enhanced] |
| pH stability | Retains binding down to pH ≈ 2.5 | [@deblonde2020selective] |
| Temperature stability | Up to 95 °C; survives repeated acid treatment | [@deblonde2020selective] |
| Competing metal tolerance | Up to molar amounts of Li, Na, Mg, Ca, Sr, Al, Si, Mn, Fe, Co, Ni, Cu, Zn, U | [@deblonde2020selective] |

Read the first three rows together, because they are the whole story. The
10⁸-fold figure, the flat picomolar Kd profile, and the fivefold Ln/Ln
preference are three faces of one fact: lanmodulin binds *all* trivalent rare
earths at nearly the same enormous strength, and calcium essentially not at all.
Set the two selectivities side by side — 10⁸ against Ca²⁺, about 5 across the
entire lanthanide series — and the seven orders of magnitude between them is the
single most important number in this chapter.

That combination is exactly the property wanted for lifting a few hundred ppm of
total REE out of a leach liquor dominated by Ca, Fe and Al — the
{index}`pregnant leach solution` of [](#hydrometallurgical-leaching) — and
exactly the wrong property for splitting Nd from Pr. Quoting the 10⁸-fold number
in a discussion of intra-series separation, which is common in reviews and press
coverage, inverts what the measurement means.

### Structural Basis of Selectivity
The NMR solution structure reveals LanM's unique architecture [@cook2019structural]:

- **Four EF-hand motifs**: Metal coordination sites typically associated with Ca²⁺ binding
- **Unusual fusion of adjacent EF-hands**: Creates a compact fold unique among EF-hand proteins
- **Coordination sphere**: the structure was solved with Y³⁺, not with a
  lanthanide, and the paper's point about the sphere is that an *additional*
  carboxylate ligand beyond the canonical EF-hand set is what buys the picomolar
  affinity. It also implicates unusual N$_{i+1}$-H···N$_i$ hydrogen bonds
  involving the EF-hand prolines in selective Ln³⁺ recognition. Donor-by-donor
  assignments and metal-ligand distances are in the deposited coordinates rather
  than in the paper's own text, so they are not quoted here.

**Critical Proline Residues:** Each EF-hand contains a crucial proline residue that hampers response to calcium while maintaining lanthanide selectivity. When prolines are mutated to alanine, calcium can induce conformational change at much lower concentrations, demonstrating proline's role in selectivity.

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
Ln³⁺ over Ca²⁺ is eight units tall. Across the series the site is nearly flat —
$K_\mathrm{d}$ = 0.4–10 pM for every lanthanide and Y³⁺ [@cotruvo2018lanmodulin], with
only about a fivefold light-over-heavy preference for the prototypal protein
[@mattocks2023enhanced], drawn to scale as the dashed line inside the band,
where the tilt is half the width of the band that contains it. The binding site
does not sharply distinguish neighbouring rare earths: the best adjacent-pair
separation factors any protein system has produced are 1.4 (Nd/Pr) to 3.0
(Ce/La) [@larrinaga2024modulating].
:::

### Metal-Sensitive Dimerization

If the binding site cannot distinguish neighbouring lanthanides, something else
must. In the one mechanism that has worked, the discrimination is moved out of
the coordination sphere and into the *quaternary* structure: whether two protein
molecules associate at all depends on which ion is bound.

Lanmodulin from *Hansschlegelia quercus* (Hans-LanM) has an oligomeric state
sensitive to rare-earth ionic radius [@mattocks2023enhanced]:

- **La(III)-induced dimer**: \>100-fold tighter than the Dy(III)-induced dimer
- **Mechanism**: picometre-scale differences in ionic radius propagate to quaternary structure through a "carboxylate shift" that rearranges second-sphere hydrogen bonding

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

The last three rows are the honest headline, and they are the only adjacent-pair
separation factors any protein system has produced: **1.4 for Nd/Pr, 1.7 for
Pr/Ce, 3.0 for Ce/La**. That range sits squarely inside the 1.5-3.0 band
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
Computational and experimental studies have revealed key engineering principles [@yao2025computationally]:

**D9 Residue Mutations:**

| Mutation | Effect on Affinity |
| ---------- | ------------------- |
| Asp→Asn | 2-fold decrease |
| Asp→Ala | 20-fold decrease |
| Bulky side chains | Up to 100-fold decrease |

**Key Insights:**

- Amino acids outside direct metal binding motif are crucial for coordination
- Point mutations can induce long-range structural perturbations
- Weak chelators can achieve high selectivity through allosteric mechanisms

### Practical Implementation
**Immobilized Lanmodulin Systems:**

- Conjugated onto porous support materials via thiol-maleimide chemistry
- Enables tandem REE purification and separation under flow-through conditions
- Column systems with multiple adsorption (pH 3) and desorption (pH \<1.7) cycles
- Protein can be reused for many cycles

**Performance from Real Feedstocks:**

- Transforms low-grade leachate (0.043 mol% REEs) into 88 mol% purity fractions
- Uses \~90% of column capacity in single run
- Achieves tandem extraction and grouped separation without organic solvents

Note the shape of that last result: 0.043 mol% to 88 mol% is a concentration
factor of about 2,000, achieved in one aqueous pass. It is a *purity* figure —
rare earths against everything else — not an individual-element figure. Reading
it as an intra-series result is the same error as reading the 10⁸-fold Ca²⁺
number that way.

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
### EF-Hand Derived Peptides
{index}`Lanthanide binding tags <lanthanide binding tags>` (LBTs) are short peptides derived from calcium-binding EF-hand loops that selectively coordinate REE cations [@li2024lanthanide].

**Design Principles:**

- Based on EF-hand metal binding loops from calmodulin, troponin, and parvalbumin
- Typical sequence: YIDTNNDGWYEGDELLA (troponin-derived, Tb³⁺-optimized)
- Net charge of -3 on binding loop creates neutral 1:1 cation:peptide complex

**Selectivity Characteristics:**

- DGA resins: Selectivity at high acid (pH \<1)
- Bioderived ligands: Selectivity at moderate pH (\>3)
- LBT Kd range: 0.9-1.8 μM (immobilized) vs. 0.4-10 pM (full LanM protein)

### Lanmodulin-Derived Peptides
Mimicking lanmodulin with shorter peptides offers advantages [@verma2024investigation]:

**LanM1 Peptide (from EF-hand loop 1):**

- Simpler to produce and manipulate
- Easier to optimize through directed evolution
- Surface-immobilizable for separation technologies
- Maintains REE binding when bound to solid substrates

**Challenges:**

- Lower affinity than full protein
- High affinity doesn't necessarily correlate with high selectivity between REEs

### Interfacial Separation with Peptide Surfactants
Lanthanide binding tags are amphiphilic, so a solution of them will build a
layer at an air-aqueous interface, and the composition of that layer need not
match the bulk. Ortuno Macias and co-workers studied this on a *flat*
interface -- surface tensiometry, X-ray reflectivity, X-ray fluorescence near
total reflection, and molecular dynamics -- rather than in a foam
[@li2024lanthanide]:

**Mechanism:**

1.  LBT peptides complex trivalent REE cations in the bulk
2.  The metal-peptide complex adsorbs to the air/aqueous interface, with MD
    showing the binding pocket stays intact on adsorption
3.  Net charge decides what happens next. A negatively charged complex recruits
    excess cations to the interface by nonselective Coulombic attraction, which
    destroys the selectivity; at a peptide net charge of −3 the complex is
    neutral and a 1:1 cation-to-peptide surface ratio is reached

**Demonstrated Separations:**

- From an equimolar Tb³⁺/La³⁺ mixture, the adsorbed layer enriches in Tb³⁺ when
  the bulk peptide is saturated and switches to La³⁺ when it is undersaturated
- A flat-interface proof of principle. Turning it into a foam-flotation unit
  operation is future work, not something this paper reports

### Gravity-Driven Separation
Microbead technology using immobilized lanthanide binding peptides (LBPs) [@sree2023gravity]:

- Selective adsorption of REEs onto functionalized microbeads
- Gravity-based separation of bound vs. unbound REEs
- Demonstrated enrichment of {index}`Europium <europium>` and {index}`Terbium <terbium>`

### Mineralization Peptides
Lanthanide ion mineralization peptide (Lamp) enables direct extraction [@hatanaka2017rationally]:

**Mechanism:**

1.  Lamp promotes REE hydroxide species generation in aqueous solution
2.  Binds to form hydrophobic complexes
3.  Spontaneous accumulation as insoluble precipitates
4.  Works under physiological conditions (pH \~6.0)

**Applications:**

- Selective separation from seawater
- Industrial wastewater treatment
- No additional energy input required

## EF-Hand Calcium Binding Proteins
### Structural Overview
The EF-hand motif is a helix-loop-helix structural domain found in diverse calcium-binding proteins:

**Key Proteins:**

| Protein | Function | REE Binding |
| --------- | ---------- | ------------- |
| Calmodulin | Ca²⁺ signaling | Strong Ln³⁺ binding |
| Troponin C | Muscle contraction | LBT source sequences |
| Parvalbumin | Ca²⁺ buffering | NMR probe applications |
| S100 proteins | Cell signaling | Eu³⁺ Kd = 660 nM |

### Lanthanide Substitution Properties
Lanthanides are routinely used as Ca²⁺ substitutes in EF-hand proteins -- as
luminescent probes (Eu³⁺, Tb³⁺) and as heavy-atom replacements -- on the
assumption that the substitution is isomorphous. Edington and co-workers tested
that assumption on calmodulin with ultrafast 2D IR spectroscopy and found it
does not hold [@edington2018coordination]:

- The method is vibrational (FTIR and 2D IR) plus electronic-structure
  calculation, not crystallography
- Lanthanide coordination **distorts** the binding-site conformation: it
  disrupts the bidentate Glu12 geometry and leaves greater conformational
  flexibility and larger structural fluctuations than Ca²⁺ does
- The caution generalizes: "seemingly innocuous ligand substitutions can
  significantly alter protein conformation," so a lanthanide-substituted
  structure is evidence about the substituted protein, not about the calcium
  one

**Calmodulin Studies:**

- Ln³⁺ associates with the binding pockets more strongly than Ca²⁺ does
- The perturbation is not negligible, which is exactly the point of the 2D IR
  work above: it is large enough to matter for structure-function inference

### Applications for REE Recovery
**Calmodulin-Based Systems:**

- Peptide binding loop conjugated to polymer scaffold particles
- Applied to {index}`cerium` recovery from solution
- Exploits natural EF-hand selectivity

## Biosurfactants for REE Separation
### Rhamnolipid Biosurfactants
Rhamnolipids are glycolipid biosurfactants produced by *Pseudomonas aeruginosa* with strong REE complexation properties [@hogan2017rhamnolipid].

**REE Binding Characteristics:**

Stability constants (log β) place REEs in the "strongly bound" group:

The strongly bound group, in the paper's own order, runs log β = 9.82 down to
8.20 and is **not** all rare earths:

| Rank | Element |
| ------ | --------- |
| 1 | UO₂²⁺ (9.82, highest) |
| 2-6 | Eu³⁺, Nd³⁺, Tb³⁺, Dy³⁺, La³⁺ |
| 7-9 | **Cu²⁺, Al³⁺, Pb²⁺** |
| 10-12 | Y³⁺, Pr³⁺, Lu³⁺ (8.20, lowest of the group) |

**Key Finding:** rare earths bind far more strongly than the moderately bound
metals (Cd²⁺, In³⁺, Zn²⁺, Fe³⁺, Hg²⁺, Ca²⁺ at log β = 7.17-4.10) and the weakly
bound ones (Sr²⁺, Co²⁺, Ni²⁺, Ba²⁺, Mn²⁺, Mg²⁺, Rb⁺, K⁺ at 3.95-0.96), and a
mixed-metal study confirms monorhamnolipids preferentially take the high-log β
metals. But copper, aluminium and lead sit *inside* the rare earth band, above
Y, Pr and Lu -- and uranyl sits above everything. Rhamnolipid is a
group-selective collector for hard, highly charged cations, not a rare-earth
selective one, and a real feed carrying Cu, Al or Pb will compete.

**Properties:**

- Hydrophilic surfactant
- Biodegradable and environmentally friendly
- Reduces surface tension more effectively than chemical surfactants at same CMC
- Potential green technology for REE recovery

### Sophorolipid Biosurfactants
Sophorolipids (produced by *Starmerella bombicola*) show promise for rare earth mineral flotation:

**Flotation Applications:**

- Evaluated as collectors for ultrafine ceria (model REE mineral)
- Both acidic (ASL) and lactonic (LSL) forms tested
- Compared favorably to petroleum-based collectors like benzohydroxamic acid (BHA)

**Complementary Properties:**

- Sophorolipids: Very hydrophobic
- Rhamnolipids: Hydrophilic
- Mixtures show robust performance in combined applications

### Saponin for Soil Remediation
Non-ionic biosurfactant saponin has been evaluated for REE leaching from contaminated soils [@zhou2018leaching]:

**Performance (25 g/L saponin, 400 mL):**

| Element | Removal Efficiency |
| --------- | ------------------- |
| La | 35.3% |
| Y | 31.5% |
| Eu | 30.8% |
| Ce | 26.1% |

Saponin outperformed rhamnolipid for soil leaching applications.

## Siderophore-Mediated Bioleaching
### Siderophore Overview
Siderophores are extracellular chelating compounds produced by aerobic microorganisms to acquire iron. They also complex REEs effectively for bioleaching applications [@osman2019characterization].

### Key Microorganisms
**Aspergillus niger:**

- Produces 87% siderophore units in iron-deficient conditions
- Main siderophore identified as **ferrichrome** (FTIR/NMR confirmed)
- Metabolites weather rock and destroy mineral crystal structures
- REE dissolution via proton exchange, redox, and ligand complexation

**Extraction Performance from Egyptian Phosphorites:**

| Element | Removal Efficiency |
| --------- | ------------------- |
| Uranium | 69.5% |
| Samarium | 66.7% |
| Thorium | 55.0% |
| Lanthanum | 51.0% |
| Cerium | 50.1% |

**Actinobacteria:**

- Four strains tested for bastnäsite-bearing rock bioleaching
- *Streptomyces* strains FXJ1.172 and FXJ1.532 produced 200 and 9.3 µmol/L siderophores
- Secreted organic acids and complexing ligands as dominant extraction agents

### Methylotrophic Bacteria
*Methylobacterium extorquens* AM1 provides a unique approach:

- Natural ability to acquire lanthanides from environment
- First demonstration of REE bioaccumulation/biomineralization in mesophilic bacteria
- Attractive for sustainable bioleaching due to inherent lanthanide metabolism

### Mineral Source Selectivity

Microorganism selection depends on mineral type:

| Mineral Type | Preferred Organisms | Mechanism |
| -------------- | -------------------- | ---------- |
| Iron-bearing (sulfide/oxide) | Siderophore-producing chemoautotrophs | Sc extraction |
| Phosphate-rich | Chemoheterotrophic bacteria | Organic acid secretion |
| Carbonate minerals | Chemoheterotrophic bacteria | Acid dissolution |

## Microbial Biosorption
### Overview
Biosorption is a physicochemical, metabolically-independent process based on absorption, adsorption, {index}`ion-exchange <ion exchange>`, surface complexation, and {index}`precipitation`. It represents a cost-effective, biotechnological approach for REE recovery [@vitova2024microbial].

**Advantages:**

- Large surface area per unit mass
- Abundant cell surface functional groups (carboxylates, phosphates, hydroxyls)
- Good metal coordination capacity
- Biodegradable and non-toxic

### Bacterial Biosorption
**Gram-Positive vs. Gram-Negative Selectivity:**

*Bacillus subtilis* (Gram-positive) showed higher selectivity for heavy REEs (Yb, Lu) compared to Gram-negative species like *Leisingera methylohalidivorans* and *Phaeobacter inhibens* [@breuker2020biosorption].

**Roseobacter-Based Separation [@bonificio2016rare]:**

- *Roseobacter* sp. AzwK-3b immobilized on assay filter
- pH-dependent adsorption/desorption
- Preprotonation concentrates solution to \~50% of three heaviest lanthanides (Tm, Lu, Yb) in just two passes

**Engineered E. coli Systems [@park2017recovery]:**

- OmpA protein functionalized with 16 copies of LBT
- 2-10-fold increase in distribution coefficients for individual REEs
- LBT-display enhances affinity as function of decreasing atomic radius
- Enables separation of high-value heavy REEs from common light REEs

### Yeast Biosorption
Phosphorylated dry baker's yeast (*Saccharomyces cerevisiae*) has demonstrated effective REE adsorption [@ojima2018recovering]:

**Metals Adsorbed:**

- Ce³⁺, Dy³⁺, Gd³⁺, La³⁺, Nd³⁺, Y³⁺, Yb³⁺

**Advantages:**

- Lower biomass requirement for relevant biosorption
- Cost-effective and simple technique
- Eukaryotes (especially fungi/yeasts like *Pichia* sp.) should be prioritized

### Algal Biosorption
**Seaweed (*Sargassum* sp.):**

- Quick and efficient acquisition of Eu, Gd, La, Nd, Pr, Sm

**Microalgae and Moss [@heilmann2021rare]:**

| Organism | Nd³⁺ Capacity | Eu³⁺ Capacity |
| ---------- | --------------- | --------------- |
| *Physcomitrella patens* (moss) | 0.74 mmol/g | 0.48 mmol/g |
| *Calothrix brevissima* | Lower | Lower |
| *Chlorella kessleri* | Lower | Lower |

**Two-Stage Adsorption Process:**

1.  **Passive stage**: Rapid surface uptake
2.  **Active stage**: Slow membrane transport to cytoplasm

Cell wall chemistry determines biosorption efficiency.

## Phytomining and Hyperaccumulator Plants
### Overview
Phytomining uses hyperaccumulator plants to extract REEs from soils, offering an ecologically sound technique for contaminated lands where traditional mining is not competitive.

**Process Stages:**

1.  **Phytoextraction**: REE accumulation in plant tissues
2.  **Enrichment**: Concentration into bio-ores
3.  **Extraction**: REE recovery from harvested biomass

### Dicranopteris linearis (Forked Fern)
The best-studied REE hyperaccumulator. It grows naturally on former mine
tailings in southern China, and the REE concentration in its aerial parts is
higher than in common low-grade ore -- which is what makes the biomass a
candidate "bio-ore" rather than a curiosity [@jally2021method].

**Processing the bio-ore.** Jally and co-workers worked out the flowsheet after
harvest, and the hard part is not the rare earths but the aluminium:

- Incinerate the biomass to ash, which raises the bio-ore grade and generates
  usable heat
- Dissolve aluminium out of the ash with 6 M NaOH at 80 °C. This is the step
  that limits the process: insoluble aluminosilicates form and cap how much Al
  can be removed
- Rinse the REE-rich residue, a step they designed carefully because it does
  most of the grade improvement
- Leach under mildly acidic conditions -- nitric acid, 25 °C, pH 4.8 -- giving
  a solution free of aluminium and carrying **74 % of the REEs**

**Detoxification Mechanism:** \[Silicon-pectin\] matrix fixation protects plant from REE toxicity [@zheng2023rare].

### Blechnum orientale: Biomineralization Discovery (2025)
A groundbreaking discovery of naturally formed REE minerals in living plants [@he2025discovery]:

**Key Findings:**

- **Nanoscale {index}`monazite`** crystals form within extracellular tissues
- Ambient temperature biomineralization process
- Dendritic nanocrystal morphology
- First discovery of REE mineral crystals in living plants

**Why it matters:**

- It is a previously unrecognized, plant-mediated pathway for critical mineral
  formation in the supergene environment, which bears on how REE are enriched
  and sequestered during chemical and biological weathering
- It raises the possibility of recovering a functional REE material directly
  from the plant rather than leaching the biomass -- the paper's argument for
  the feasibility of phytomining. Whether the biogenic monazite carries the
  thorium and uranium that geological monazite does is not addressed
- No mining-associated radioactive waste concerns

### Challenges and Future Potential
While promising, phytomining faces hurdles:

- No peer-reviewed studies establishing commercial viability
- Slow accumulation rates
- Land requirements for large-scale operations
- Need for optimized processing of plant biomass

## Biopolymer Adsorbents
### Chitosan-Based Adsorbents
Chitosan, the second most abundant biopolymer, offers exceptional properties for REE recovery [@kore2024application]:

**Properties:**

- Non-toxic and biodegradable
- High adsorption capacity (85-100%)
- Excellent surface area and porosity
- High chelating power and hydrophilicity

**Modifications for Enhanced Performance:**

| Modification                 | REE     | Capacity (mg/g) | Conditions   |
|------------------------------|---------|-----------------|--------------|
| EDTA-magnetic graphene oxide | Ce(III) | 353.28          | pH 7, 25 min |
| Ion imprinted polymer        | Ce(III) | Selective       | pH 7         |
| Acrylic acid graft           | Various | High            | Variable     |

**Key Functional Groups:** C(=O)NH, CN, and C-O-C provide heterogeneous affinity for REE chemical adsorption.

### Cellulose Composites

**Graphene Oxide-Cellulose Systems:**

| Adsorbent | Nd(III) Capacity | Ce(III) Capacity |
| ----------- | ------------------ | ------------------ |
| GO-sodium carboxymethyl cellulose | 661.21 mg/g | 436.55 mg/g |

**Dialdehyde Cellulose-Chitosan:**

- Chemically hybridized via Schiff base reaction
- Followed by acrylic acid graft copolymerization
- High adsorption efficiency for heavy metals

### Modification Strategies
**Cross-linking:**

- Covalent bonds with amine groups
- Increases mechanical strength and chemical stability
- Glutaraldehyde commonly used

**Functionalization:**

- Introduction of new functional groups
- EDTA functionalization creates high-capacity adsorbents
- Example: EDTA-Fe₃O₄-chitosan-CMC nanocomposite: 432.34 mg/g for Pb²⁺

**Composite Materials:**

- {index}`Metal-organic frameworks <metal-organic framework (MOF)>` (MOFs)
- Layered double hydroxides
- Carbon materials
- Clays

## Synthetic Biology and Metabolic Engineering
### Engineered Microbes for Bioleaching
Systems biology-guided engineering has dramatically improved REE extraction [@schmitz2025high]:

**Gluconobacter oxydans Engineering:**

- Whole-genome screening identified key genes
- Deletion of *pstS* gene (phosphate transport)
- Overexpression of *mgdh* gene
- Result: **Up to 73% improvement** in REE extraction

**Transposon Mutant Library [@schmitz2021generation]:**

- A whole-genome collection of single-gene disruption mutants; 304 genes alter
  biolixiviant production
- Losing PQQ synthesis, or the PQQ-dependent membrane-bound glucose
  dehydrogenase, nearly eliminates bioleaching
- Disruption of phosphate-specific transport genes enhances bioleaching by up
  to 18% -- the screen that pointed at *pstS* and led to the engineered strain
  above

### Scalable Microbial Platforms
**Methylobacterium extorquens AM1 Platform [@good2024scalable]:**

- Grows using electronic waste as sole REE source
- Scalable to 10 L with consistent metal yields
- No harsh acids or high temperatures required
- Engineered overproduction of:
  - REE-binding ligands (lanthanophores)
  - Pyrroloquinoline quinone (PQQ)

### Synthetic Biology for E-Waste Recovery
Advanced approaches for sustainable e-waste processing [@bai2025harnessing]:

**Capabilities Achieved:**

- Higher metal selectivity
- Enhanced tolerance to acidic conditions
- Faster recovery kinetics in complex matrices
- Selective bioleaching, biosorption, and bioaccumulation

**Technologies Applied:**

- Metabolic pathway engineering
- Synthetic gene circuits
- Cell surface display systems
- Directed evolution

### High-Purity REE Biomanufacturing
Microbial synthesis systems achieve active biomanufacturing:

**Affinity Column Systems:**

- Bioconjugated with structurally engineered proteins
- Outstanding separation achieved

**Purity Results:**

| Element Pair | Purity Achieved |
| -------------- | ----------------- |
| Eu recovery | 99.9% |
| La recovery | 97.1% |
| Dy recovery | 92.7% |

## Green Solvents: Deep Eutectic Solvents and Ionic Liquids
### Overview
{index}`Deep eutectic solvents <deep eutectic solvent>` (DESs) and {index}`ionic liquids` (ILs) represent green alternatives to conventional organic solvents for REE separation [@deng2025application].

**Shared Properties:**

- Liquid over wide temperature range
- Non-volatile
- Non-flammable
- Good ionic conductivity

**DES Advantages:**

- Easier preparation (simple mixing of two components)
- Much cheaper than ILs
- Generally less stable than ILs

### Natural Deep Eutectic Solvents (NADESs)
NADESs use natural compounds as components:

- Sugars
- Organic acids
- **Amino acids**
- Organic bases

**Amino Acid-Based DESs:**

- Cheap and natural source
- Biodegradable
- **Important Caveat:** Recent studies show amino acid-based DESs can be unexpectedly toxic---up to 10⁵ times more toxic than conventional choline chloride-based DESs [@li2022high]

### REE Extraction Performance

**Choline Chloride-Urea-Malonic Acid System:**

| Condition | Y Dissolution |
| ----------- | -------------- |
| Without activation | 49% |
| 60 min mechanical activation | 85% |

**IL Extraction Systems:**

- Extracted complexes often different from organic solvent systems
- REE extraction and separation efficiencies significantly enhanced
- Synergistic IL extraction improves extractability and separability

(industrial-challenges)=
### Industrial Challenges
Despite academic promise, commercial breakthroughs have been limited:

- High cost of some ILs
- Stability issues with DESs
- Scale-up challenges
- Toxicity concerns with some formulations
- Need for {index}`life cycle assessment`s

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
| Biosurfactants | Moderate | Weak (log β spans ~1.3 units across the series) | 400 mL at 25 g/L saponin |
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
