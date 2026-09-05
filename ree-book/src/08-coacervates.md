---
title: Coacervates and Aqueous Biphasic Systems
---

(coacervates-and-aqueous-biphasic-systems)=
# Coacervates and Aqueous Biphasic Systems

Coacervates are phase-separated, polymer-rich droplets that form spontaneously
when oppositely charged macromolecules associate in solution. They are
interesting for rare earth separation for a reason that has little to do with
selectivity and everything to do with the solvent: both phases are aqueous. A
coacervate system does the job of a {index}`solvent extraction` circuit without kerosene,
without the fire risk, and without the volatile organic emissions — and the mild
conditions leave room for biological ligands that would not survive an organic
diluent. This chapter surveys what such systems can currently do.

This is the least mature technology in the book. There is a large and
well-founded physical chemistry literature on coacervation itself, a smaller
one on coacervates and biphasic systems for metals in general, and — for
polyelectrolyte coacervates applied to separating one rare earth from another —
essentially nothing. Most of what follows is therefore either established
physics being pointed at a problem it has not yet been applied to, or a result
from a single group that no one else has reproduced. Where that is the case the
text says so. Nothing here should be read as a process option available today.

Three lines of work are worth separating, because they are at very different
stages. **Polyelectrolyte complex coacervates** are the best understood
physically: charge density, polymer composition and ionic strength give real,
predictable control over where the two-phase window sits
[@sing2025polyelectrolyte; @lee2025polyelectrolyte]. They have been used to
take up heavy metals and precious metals; they have not been shown to separate
lanthanides from one another. **Aqueous biphasic systems** built from polymers,
salts and {index}`ionic liquids` are the most developed as separations, and are
also the ones whose reported successes need the closest reading: the headline
{index}`separation factors <separation factor>` in this area are almost always
for a rare earth against a *transition metal*, not against another rare earth
[@neves2022liquid; @kumar2022separation]. **Biomimetic systems** built on
lanthanide-binding proteins such as {index}`lanmodulin` are the newest and the
most striking. They separate the rare earths from *everything else* with a
sharpness no synthetic extractant matches — roughly 10⁸-fold discrimination
against Ca²⁺, and quantitative recovery of REEs from leachates carrying molar
quantities of Na, Mg, Ca, Al, Fe, Cu and Zn [@cotruvo2018lanmodulin;
@deblonde2020selective] — and they discriminate one lanthanide from its
*neighbour* only weakly. That makes them group-separation agents rather than
replacements for a fractionation cascade; the distinction is developed in
[](#lanmodulin-structure-mechanism-and-engineering) and is the single most
frequently misread result in this field.

A fourth idea, stimuli-responsive capture and release, runs through all three
and deserves a warning up front. Reversible, trigger-driven coacervation is
real and well demonstrated [@love2020reversible; @wang2025quantification] — on
enzymes, on dyes, on Cu(II), not on a rare earth in a coacervate. The step from
"this phase can be switched on and off" to "this is a strip stage" has not been
taken in any published work known to this chapter. Lanmodulin and the other
protein-based systems are treated more fully in
[](#biological-and-biomimetic-separations); here the focus is the coacervate
phase itself.

## Introduction to Coacervates
Coacervation is a liquid-liquid phase separation (LLPS) in polyelectrolyte solutions, induced by pH, ionic strength, temperature or solubility, that produces a colloid-rich phase known as a coacervate [@lee2025polyelectrolyte]. The term derives from the Latin *coacervare*, "to cluster together." These polymer-dense phases are a thermodynamically stable state in which electrostatic attraction between oppositely charged species drives demixing from the bulk solution.

What drives the demixing is wrong in the naive account, instructively so. The
obvious story is that the polycation and polyanion attract and the enthalpy of
that attraction pays for the lost mixing entropy. The classical answer is
instead that the dominant gain is *entropic*: each ion pair formed between the
chains releases a pair of small counterions condensed on the backbones, and
those gain far more entropy than the chains lose. Coarse-grained simulation
complicates even that. In a symmetric polyelectrolyte mixture at monovalent
ionic strength and room temperature, the temperature dependence of the
dielectric constant of water makes the electrostatic interaction itself partly
entropic, and it is *this* solvent-reorganization term, rather than counterion
release, that dominates [@chen2022driving]. Hydrophobic interactions and
hydrogen bonding contribute where the polymers carry the relevant groups, and
in polypeptide systems can matter as much as the charges do.

The practical consequence is that coacervation is tunable by everything that
touches the solvent: pH, polymer ratio, ionic strength, temperature, and the
molecular architecture of the chains [@wang2014polyelectrolyte;
@sing2025polyelectrolyte]. That breadth is what makes the systems attractive
and also what makes them hard to specify — a coacervate reported in one
laboratory's buffer is not obviously the same object in another's.

### Complex Coacervation
Complex coacervation occurs when two oppositely charged polyelectrolytes (polycation and polyanion) are mixed in aqueous solution. At appropriate stoichiometries and ionic strengths, the system phase-separates into a polymer-rich coacervate phase and a polymer-dilute supernatant [@wang2014polyelectrolyte].

The earliest theoretical framework for complex coacervation was developed by Overbeek and Voorn in 1957, who estimated the total free energy of mixing as a sum of Flory-Huggins mixing entropy terms and Debye-Hückel electrostatic interactions [@overbeek1957phase; @priftis2012early]. This mean-field approach captures the essential physics: the electrostatic free energy provides the driving force, while entropic mixing favors the disordered homogeneous state.

The polymer pairs that actually appear in the literature fall into four
families, and which one a study uses says a good deal about what it is for.
Polypeptide pairs — poly(L-lysine)/poly(L-glutamate),
poly(L-arginine)/poly(L-aspartate) — are the model systems for the physics,
because sequence and charge pattern can be specified exactly. Polysaccharide
pairs such as chitosan/alginate and chitosan/hyaluronic acid are the ones with
food and pharmaceutical precedent, and are cheap. Synthetic pairs, above all
poly(diallyldimethylammonium chloride) (PDADMAC) with poly(styrene sulfonate)
(PSS), are the workhorses of the metal-uptake work below. Protein-polymer pairs
— gelatin/gum arabic, BSA with polycations — are where selectivity might come
from, and are the least characterized as materials.

Phase diagrams for coacervate systems typically show a two-phase region at intermediate ionic strengths, bounded by a single-phase region at very low salt (kinetically trapped precipitates) and at high salt (electrostatic screening suppresses coacervation) [@sing2020progress].

That window is the whole process. [](#fig-coacervate-phase-diagram) draws it
next to the loop it supports. Inside it the system splits into a dense
coacervate and a dilute supernatant at the same ionic strength — the ends of a
horizontal tie line — and the metal goes with the dense phase. Push the salt
past the critical concentration and the two ends merge: the coacervate
redissolves and gives the metal back. One variable does both jobs, which is
what makes the cycle a cycle rather than a one-way capture.

:::{figure} ../figures/08-coacervate-phase-diagram.svg
:name: fig-coacervate-phase-diagram
:width: 100%

**(a)** where a coacervate exists, and **(b)** the loop that its existence is
supposed to buy. **The phase boundary is schematic.** No measured binodal for
an REE-relevant coacervate is reported in this chapter or in the sources it
draws on, so neither axis carries values and no distance in the figure should
be read as a number. What is taken from the literature is the topology: a
two-phase region at intermediate ionic strength, closing at a critical salt
concentration above which screening suppresses coacervation, and bounded below
by a low-salt regime in which the complex is a kinetically trapped precipitate
rather than a liquid [@sing2020progress; @wang2014polyelectrolyte]. Tie
lines are horizontal because the two coexisting phases share an ionic strength.
From the chapter: that the metal partitions into the dense phase, and that
salt, temperature past a cloud point, or a pH change all move the system out of
the two-phase region and release it. Drawn for illustration only: the shape of
the dome, where the operating tie line sits on it, and how far apart the two
coexisting compositions are. Panel (b) is the flowsheet sketched in
[](#process-considerations); its return leg is the claim the whole approach
rests on, since every stream in it is water. Drawn by
`tools/figures/fig_coacervate.py`.
:::

### Simple Coacervation
Simple coacervation involves a single polyelectrolyte species that undergoes phase separation induced by salt, solvent, or temperature changes. This process is particularly relevant for intrinsically disordered proteins (IDPs), which can self-coacervate due to their unique charge patterns and low-complexity sequences [@uversky2015intrinsically].

Temperature and pH are the two handles, and they act on different things.
Temperature moves the dielectric constant of water and, separately, the
solubility of the polymer, so its effect on the phase boundary is not generally
monotonic and has to be measured for each system rather than predicted. pH sets
the ionization state of a weak polyelectrolyte and hence its effective charge
density, which is the variable the theory is written in — so for a weak
polyacid or polybase, pH and charge density are the same knob under two names.
The cloud point, at which the solution turns turbid as the coacervate appears,
is the standard experimental signature and the quantity a temperature-swing
process would be designed around.

## Coacervates for Metal Ion Separations
The dense, water-rich environment of coacervates provides a unique medium for metal ion partitioning. Unlike organic solvents used in conventional liquid-liquid extraction, coacervates maintain aqueous compatibility while offering distinct chemical environments in the polymer-rich and polymer-dilute phases [@bediako2022facile].

### Mechanism of Ion Uptake
Four mechanisms are available, and what matters is how few can discriminate
within the lanthanide series. Non-specific **electrostatic attraction** pulls
multiply charged cations toward the carboxylates, sulfonates and phosphates on
the backbone; it drives most of the reported uptake and sees the whole series
as identical +3 ions. **Ion exchange** — a metal cation displacing bound Na⁺ or
K⁺ — is the same statement in a different vocabulary and inherits the same
blindness. **Hydrophobic partitioning** of a neutral metal-ligand complex into
the less polar coacervate interior discriminates only to the extent that the
ligand does, which puts the selectivity back in the extractant rather than the
phase. That leaves **coordination chemistry**: specific donor atoms (N, O, S)
on the polymer or on an added chelator, arranged so that the fit depends on
ionic radius. Only the fourth can in principle sort a lanthanide series, and it
is the one requiring the polymer to be designed rather than merely chosen.

The demonstrations bear this out. Polyelectrolyte complex resins fabricated from PDADMAC-PSS coacervates show outstanding performance for heavy metal adsorption, with significant uptakes of Cu2+, Pb2+, and Cd2+ and easy phase separation [@bediako2022facile]. PEC capsules have demonstrated selective Au(III) recovery from multimetal mixtures containing Pt, Pd, Cu, Co, and Zn [@wang2023polyelectrolyte]. Both results are real and both rest on chemistry that separates elements from *different* parts of the periodic table — charge, softness, chlorocomplex stability. Neither says anything about Nd against Pr.

### Selectivity and Separation Factors
Three sources of selectivity are usually invoked. **Size exclusion** by the
polymer mesh rejects large ions or complexes — a real effect for bulky
metal-ligand species, irrelevant for bare aquo ions that all fit. **Charge
density** binds the more strongly polarizing cation more tightly to a
polyanionic domain, which separates +3 from +2 and not +3 from +3.
**{index}`Lanthanide contraction <lanthanide contraction>`** — the systematic
decrease in ionic radius across the series, from La³⁺ = 1.032 Å to Lu³⁺ =
0.861 Å in six-coordination [@shannon1976revised] — is the only one of the
three that can order the lanthanides, and the hardest to exploit.

The difficulty is the size of the signal. All lanthanides carry the same +3
charge, prefer the same coordination numbers (typically 8-9), and differ in
radius by roughly 0.01-0.02 Å between adjacent elements [@shannon1976revised].
A separation medium that responds to radius must therefore respond to a
one-percent difference, which is why the field is dominated by ligands with
pre-organized, rigid binding pockets rather than by flexible polymer
environments — and a coacervate interior is about as flexible an environment as
chemistry offers.

Separation factors (SF) quantify selectivity: $$SF = \frac{[M_1]_{coacervate}/[M_1]_{supernatant}}{[M_2]_{coacervate}/[M_2]_{supernatant}}$$

For adjacent lanthanides, conventional solvent extraction with organophosphorus
extractants sits in a narrow and well-established band, near 1.5 and rarely
above 3 ([](#solvent-extraction-fundamentals)). Protein-based systems are sometimes quoted at "SF \> 100", but that number is a misreading. The figure in circulation is the \>100-fold ratio of *dimerization affinities* between the La³⁺- and Dy³⁺-loaded forms of Hans-LanM [@mattocks2023enhanced] — neither a separation factor nor an adjacent pair, since La and Dy sit nine places apart on opposite sides of the light/heavy split. The separation factors the same work actually measured are Nd/Dy = 8.1 (wild type) and 12.7 (the R100K variant), and the adjacent-pair figures from protein systems are of the same order as conventional extraction: Ce/La = 3.0, Pr/Ce = 1.7 and Nd/Pr = 1.4 for an engineered LanD chaperone [@larrinaga2024modulating], and an average adjacent-element separation factor of 2.1 across the eleven elements Nd to Lu for the dimerizing lanmodulin Al-LanM [@choi2026near] --- which is among the best reported for any ligand, protein or otherwise, and is still inside the conventional band. Against Ca²⁺ and the other non-rare-earth cations in a leachate the protein discrimination genuinely is enormous; against a neighbouring lanthanide it is not. The two selectivities must be kept apart, and only the second is what a fractionation cascade is built to supply.

One caution applies to every separation factor quoted in this chapter. The
measurements behind them are made on synthetic, usually binary solutions at
micromolar to low-millimolar concentration, in a single laboratory, and in most
cases in a single publication. Such a number is a statement about one
experiment, not a material property, and it is not directly comparable with a
solvent-extraction separation factor measured on a loaded organic phase at
plant concentrations, where extractant loading, third-phase formation and acid
balance all move it.

## Biomimetic and Natural Coacervate Systems
Nature provides inspiration for REE-selective materials through the discovery of lanthanide-dependent bacteria and their associated proteins. Biological phase separation in the form of membraneless organelles also offers insights into coacervate function and design, and the in vitro coacervate models used to study those organelles are the same objects a separations chemist would want to use — regulated assembly, differential partitioning of solutes, permeability to small molecules, and a crowded interior quite unlike bulk water [@nakashima2019biomolecular].

### Intrinsically Disordered Proteins (IDPs)
IDPs are proteins that lack a fixed three-dimensional structure but remain functional, and they are abundant: a large fraction of eukaryotic proteins carry long disordered regions. IDPs undergo liquid-liquid phase separation (LLPS) to form membrane-less organelles (MLOs) that play critical roles in cellular organization [@brangwynne2015polymer], and their overwhelming abundance in those organelles is the observation that motivates treating them as the drivers of intracellular phase separation [@uversky2015intrinsically].

What makes an IDP sequence phase-separate reads better as design rules for
synthetic polymers than as biology. The sequences are low-complexity and
enriched in charged and polar residues; they interact multivalently through
repeated motifs rather than one strong site; and — the feature with the
clearest design payoff — the *pattern* of the charges matters as much as their
number, because clustering like charges into patches amplifies phase separation
relative to the same composition scattered along the chain [@wang2025role]. All
of it responds to ionic strength, pH and temperature [@lin2019intrinsically].
Computed phase diagrams confirm the pattern effect quantitatively: block-charged
sequences have larger coacervation windows than randomly patterned ones of
identical composition [@mccarty2019complete]. A wider window is a wider
operating envelope, which makes this one of the few results here that
translates directly into a process specification.

### Protein-Polyelectrolyte Coacervates
Protein-polymer coacervates pair the structural selectivity of a protein with
the processability of a synthetic polyelectrolyte. The systems that exist —
globular proteins (BSA, lysozyme, gelatin) with synthetic polyelectrolytes,
enzyme-loaded coacervates for biocatalysis, antibody-polymer assemblies for
sensing — were not built for metals. The case for extending them to rare earths
is a case about what a protein supplies that a polymer cannot: a pre-organized
binding site with defined coordination geometry, possible allosteric control
over affinity, and biodegradability. It is a good case and, at present, an
entirely prospective one. No protein-polyelectrolyte coacervate has been
reported separating rare earths.

### Peptide-Based Coacervates
Short peptides can form coacervates and offer advantages of defined sequence, scalable synthesis, and tunable properties. The sequences involved can be very short indeed: an adhesive coacervate has been built by self-assembled condensation of a *tripeptide* with polyoxometalates in aqueous solution, giving a shear-thinning fluid that gels on a change of pH or on adding metal ions [@li2019coassembly].

#### Lanthanide Binding Tags (LBTs)

{index}`Lanthanide binding tags <lanthanide binding tags>` are amphiphilic peptide sequences based on the EF-hand metal binding loops of calcium-binding proteins [@li2024lanthanide; @schmitz2022lanmodulin]. The EF-hand motif consists of two alpha helices linked by a 12-residue loop that coordinates metal ions through carboxylate-rich sidechains, with the metal held in a pentagonal bipyramidal geometry by residues at loop positions 1, 3, 5, 7, 9 and 12 (conventionally labelled X, Y, Z, -Y, -X, -Z), and the loop itself undergoing a disorder-to-order transition when the lanthanide binds. That the motif binds lanthanides at all is a consequence of their being good Ca²⁺ mimics: the trivalent charge on a similar radius makes an EF-hand site thermodynamically better suited to Ln³⁺ than to the ion it evolved for [@nikolova2023lanthanides].

Isolated tags bind far more weakly than the protein they derive from:
micromolar dissociation constants for immobilized LBTs against picomolar ones
for full-length lanmodulin (see [](#biological-and-biomimetic-separations)).
The picomolar affinity and 10⁸-fold Ca²⁺ discrimination quoted in the
literature belong to the whole protein [@cotruvo2018lanmodulin], not to the
excised loop.

Two lines of work put LBTs into an all-aqueous separation. In the first, LBTs
optimized for Tb³⁺ are used as amphiphilic extractants that carry their bound
lanthanide to an air-water interface, from which it can be skimmed. The result
that matters for process design is not a separation factor but a warning: the
selectivity *reverses* with loading. From an equimolar Tb³⁺/La³⁺ solution the
adsorbed layer is enriched in Tb³⁺ when the bulk peptide is saturated, and
selective for La³⁺ when it is undersaturated, because the La³⁺ complex is the
more surface-active of the two [@li2024lanthanide]. A separation whose sign
depends on the loading state is not a separation a cascade can be built from
until that dependence is designed out. The same paper establishes a second
design rule: the peptide's net charge must be −3, so that the metal-peptide
complex is neutral, or excess cations are recruited to the interface by
non-selective Coulombic attraction and the selectivity is destroyed.

In the second, LBT-lanthanide complexes are cross-linked with glutaraldehyde to
stabilize the interfacial film for foam-based recovery; the cross-linked layers
are measurably thicker and stiffer in dilational and shear surface rheology,
which is what the foam needs [@ortunomacias2024enhanced]. That paper reports
interfacial mechanics, not separation factors, and is evidence about foam
stability rather than about REE selectivity.

Isolated EF-hand loop peptides dimerize when saturated with lanthanide ions, reproducing the structure of native protein domains [@shaw1997isolated]; that metal-induced self-assembly could be exploited for coacervate formation. The same motif has a separate use in structural biology: a twelve-residue EF-hand grafted onto the N-terminus of a membrane protein in lipid micelles binds a lanthanide specifically and weakly aligns the protein in the magnetic field without perturbing its structure, yielding residual dipolar couplings for solution NMR [@ma2000lanthanide].

#### Lanmodulin (LanM)

Lanmodulin is a natural lanthanide-binding protein discovered in methylotrophic bacteria that use lanthanides in methanol dehydrogenase enzymes [@cotruvo2018lanmodulin; @deblonde2020selective]. LanM possesses four EF-hand motifs and undergoes a large disorder-to-order conformational change on metal binding. Two of its properties matter here, and they are different properties:

- **Ln³⁺ versus everything else.** LanM responds to picomolar concentrations of every trivalent lanthanide from La to Lu (and Y), but only to near-millimolar Ca²⁺ — a discrimination of order 10⁸ [@cotruvo2018lanmodulin]. It holds that binding down to pH ≈ 2.5, survives 95 °C and repeated acid cycling, and recovers rare earths quantitatively from coal and electronic-waste leachates containing molar amounts of Li, Na, Mg, Ca, Sr, Al, Si, Mn, Fe, Co, Ni, Cu, Zn and U [@deblonde2020selective]. This is a *group* selectivity, and it is the strongest one known for a macromolecule.
- **Ln³⁺ versus Ln³⁺.** The same property — picomolar affinity for the whole series — means the monomer barely distinguishes one lanthanide from the next. Discriminating Nd from Pr, which is what a fractionation cascade exists to do, is a different problem, and native LanM does not solve it.

The route to intra-series discrimination is not the binding site but the *quaternary* structure. A homologue from *Hansschlegelia quercus* (Hans-LanM) dimerizes in a way that is sensitive to ionic radius: the La³⁺-induced dimer is \>100-fold tighter than the Dy³⁺-induced dimer [@mattocks2023enhanced]. X-ray crystal structures reveal how picometer-scale radius differences between La³⁺ and Dy³⁺ are propagated to quaternary structure through carboxylate shifts in second-sphere hydrogen bonding networks.

As stressed above, that \>100-fold figure is a ratio of dimerization affinities and not a separation factor. The separation factors the same work measured are Nd/Dy = 8.12 ± 0.40 on a Hans-LanM column and 12.7 ± 1.3 on an R100K variant column [@mattocks2023enhanced]. An SF of that size still does real work when amplified down a column: loaded with a model electronic-waste mixture of 95% Nd and 5% Dy, the R100K column achieved baseline separation to \>98% purity and \>99% yield in a single stage. The mechanism is a modest separation factor plus many theoretical plates.

For an adjacent pair the numbers are smaller still. The same dimerization strategy applied to *Methylorubrum extorquens* LanD — a related periplasmic lanthanide chaperone, not lanmodulin — gives an engineered variant that enriches Pr³⁺ and Nd³⁺ over La³⁺ and Ce³⁺ in an all-aqueous ultrafiltration step, with SF Ce/La = 3.0 ± 0.4, Pr/Ce = 1.7 ± 0.2 and Nd/Pr = 1.4 ± 0.2 [@larrinaga2024modulating] — the best protein-based adjacent-pair figures reported, measured on micromolar solutions at bench scale.

Recent computational studies provide structural insights into REE selectivity in lanmodulin variants, which is the groundwork for rational design of engineered proteins aimed at specific separation challenges [@yao2025computationally]. Wild-type lanmodulin is meanwhile being tested as a sorbent in its own right: crude LanM from *Methylorubrum extorquens* takes up lanthanum from a synthetic acidic leachate at 70 mg La per gram of protein at a 100 mg/L feed, falling to 49.8 mg/g at 50 mg/L, with chemisorption kinetics, an equilibrium time of 90 minutes and an optimum at pH 5 [@chhantyal2025lanmodulin]. That study is single-element (La only), on a synthetic leachate, and is described by its own authors as the first of its kind, so the capacity figure is a first measurement rather than a design basis.

## Stimuli-Responsive Coacervates
Stimuli-responsive coacervates undergo phase transitions in response to external triggers, which is what a separation needs if extraction and stripping are to be the same operation run forwards and backwards. This section reviews what has been demonstrated. It is important to be clear at the outset that the demonstrations are of the *switching*, on model systems, and that the metals involved — where there are metals at all — are transition metals rather than rare earths.

### Temperature-Responsive Systems
#### LCST and UCST Polymers

Poly(N-isopropylacrylamide) (PNIPAM) is the prototypical thermoresponsive polymer, exhibiting a lower critical solution temperature (LCST) around 32°C [@das2024poly]. Below the LCST, PNIPAM is water-soluble and hydrated; above the LCST, it undergoes a reversible transition to an insoluble, dehydrated state.

The LCST is not a fixed property but a formulation variable. Copolymerizing with hydrophilic monomers raises it and with hydrophobic monomers lowers it; added salts shift it according to the Hofmeister series; and binding a metal ion shifts it too, which is the effect a separation would exploit. The metal-binding case has been demonstrated with PNIPAM-*b*-poly(acrylic acid) block copolymers taking up Cu(II) [@zhong2021thermoresponsive] — a divalent transition metal, not a lanthanide. The general design, a PNIPAM copolymer carrying metal-binding groups that captures at low temperature and releases above the LCST, is the basis of a broad class of thermoresponsive adsorbents for heavy metals and dyes [@kumar2023comprehensive], and the same review is the closest thing in the literature to a systematic account of what such a thermal cycle costs and how many cycles it survives. Neither source is about rare earths.

#### Thermoseparating Coacervates

Cloud point extraction (CPE) uses temperature-induced phase separation of non-ionic surfactants for metal preconcentration. Above the cloud point a micellar solution splits into surfactant-rich and surfactant-dilute phases, and a metal complexed by a hydrophobic ligand partitions into the surfactant-rich one. This is the closest thing to a coacervate-like process with a real lanthanide track record. Favre-Réguillon and co-workers separated La(III) from Gd(III) by forming their 8-hydroxyquinoline complexes in the micellar phase of a non-ionic surfactant, and proposed CPE explicitly as an alternative to organic-solvent extraction for lanthanides [@favrerguillon2004cloud]. Water-soluble calixarenes — p-sulfonato thiacalixarene, calix[4]resorcinarene phosphonic acid — used as chelators with Triton X-100 extend the approach to La(III), Gd(III) and Yb(III) with selectivity that depends on the chelator chosen [@mustafina2006cloud]. Later work has optimized the surfactant side: CPE of La(III) with the non-ionic surfactant C13E10 has been through a formal Taguchi design of experiments, which is a level of process characterization the rest of this chapter cannot match [@ghidini2019cloud].

No representative separation factor can be given for lanthanide CPE. The
figures in circulation for the La/Gd system could not be traced to a source
that states them, and are not repeated here; the qualitative claim — that CPE
separates La from Gd via 8-HQ complexes in a micellar phase — is what the
primary source supports.

### pH-Responsive Coacervates
pH-responsive coacervates exploit the charge-switching behavior of weak polyelectrolytes above and below their pKa values. The mechanism is simple and it is the most controllable one available. A weak polyacid — poly(acrylic acid), poly(glutamic acid) — is protonated and effectively uncharged below its pKa; above it, ionization raises the charge density until the system enters the two-phase window with an oppositely charged partner. Crossing back and forth across that pKa assembles and disassembles the coacervate, and the cycle is fully reversible. The cleanest demonstration takes it inside a lipid vesicle, where a pH change nucleates a single coacervate droplet and, on reversal, dissolves it again, switching a dormant enzymatic reaction on and off [@love2020reversible]. That experiment establishes the reversibility; it is a cell-mimetic study, and no metal is being separated in it.

Complex coacervates formed from peptides and polyoxometalates undergo pH-induced phase transitions from fluid coacervate to gel state [@li2019coassembly]. Metal ions can trigger similar transitions, providing a readout for metal binding and a mechanism for metal-responsive materials.

Mapped onto a flowsheet, a pH-cycled coacervate would extract at the pH of
strongest binding, strip by moving the pH to release, and return the polymer to
service. Each step is plausible; none has been demonstrated on a rare earth
feed. The acid and base consumption such a cycle implies is unquantified, and
it is the term most likely to decide whether the idea is economic, being a
reagent cost incurred once per pass rather than once per campaign.

### Light and Redox-Responsive Systems
Azobenzene-containing polymers undergo *cis-trans* isomerization upon UV/visible light irradiation, changing their hydrophobicity and charge distribution, which in principle enables light-triggered coacervate formation or dissolution with no chemical addition at all. This is the most attractive trigger on paper — nothing is consumed and nothing accumulates — and the least developed. No REE application is reported. Light-, temperature- and pH-responsive materials for extraction more broadly are reviewed by @davidson2020application, and that review is the right place to see how thin the metals coverage is relative to the organic-analyte coverage.

Redox triggers act either on the polymer backbone, through ferrocene or disulfide groups whose charge or connectivity changes with oxidation state, or on the metal itself, through couples such as Ce³⁺/Ce⁴⁺ and Fe²⁺/Fe³⁺. Recent work quantified redox thermodynamics shifts within coacervates using temperature-dependent electrochemistry, extracting reaction entropy, enthalpy, and Gibbs energy for redox processes in the condensed phase [@wang2025quantification] — establishing that the coacervate interior shifts redox potentials measurably relative to bulk water, which is the prerequisite for any redox-driven scheme and is not itself a separation.

For {index}`cerium` specifically, the Ce3+/Ce4+ redox couple enables selective oxidation and {index}`precipitation`, and integrating that step with coacervate extraction is an obvious thing to try; no such combination has been reported, and the suggestion is this book's rather than any cited source's.

## Coacervates for Rare Earth Element Separations
The application of coacervate-based systems specifically to REE separations is an emerging field, with most work focusing on aqueous biphasic systems, cloud point extraction, and protein-based approaches rather than classical polyelectrolyte coacervates.

### Polyelectrolyte Systems for REE
While PEC coacervates have been extensively studied for heavy metal removal [@bediako2022facile; @wang2023polyelectrolyte] their application to REE separation is limited. The similar chemistry of lanthanides means that non-specific electrostatic binding provides poor selectivity.

The design responses follow from the mechanism analysis above: put the
selectivity in a ligand rather than in the phase. That means grafting
phosphonate or aminocarboxylate groups onto the coacervate-forming polymer, or
leaving the polymer non-selective and adding a water-soluble holdback reagent
such as DTPA or EDTA to the dilute phase so that selectivity comes from the
*difference* between two competing complexations — the standard trick in
aqueous biphasic work, discussed below. Neither has been reported for a
polyelectrolyte coacervate on a rare earth pair.

### Aqueous Biphasic Systems (ABS)
Aqueous biphasic systems form when two water-soluble polymers (PEG/dextran) or a polymer and kosmotropic salt (PEG/ammonium sulfate) are mixed above critical concentrations [@neves2022liquid; @kee2020development]. Unlike organic-aqueous extraction, both ABS phases are aqueous, reducing environmental and safety concerns.

#### Polymer-Salt ABS

PEG-salt systems have been applied to lanthanides with added extractants, and the qualitative behaviour is well established: partitioning responds to PEG molecular weight, to the identity and concentration of the salting-out salt, and to pH, and adding DTPA to the salt-rich phase shifts selectivity by holding the more strongly complexed lanthanides back. No representative separation factor is quoted here because the reported values are specific to the extractant and the feed used in each study, and no source verified for this chapter offers a figure that generalizes.

#### Ionic Liquid-Based ABS

Ionic liquid ABS replace the polymer with an IL, which brings the tunability of the cation and anion into the phase behaviour. The best-characterized rare earth example is the tributyltetradecylphosphonium chloride ([P444,14]Cl) system, and it repays close reading because of what it does and does not separate. The pairs studied were Sm/Co, Nd/Fe, Eu/Zn and La/Ni — in every case a rare earth against a *transition metal* [@kumar2022separation]. Fe(III) and Zn(II) transfer essentially quantitatively into the IL phase as their chlorometallate complexes, with the zinc distribution ratio exceeding 2600, while the rare earths stay behind at low chloride concentration; Ni(II) behaves oppositely and, at 8 mol/kg LiCl, is taken up over La with a selectivity of 288. The distribution ratios of Nd and Eu rise with chloride concentration through the salting-out effect, which is why the recommendation is to operate at the *lowest* chloride concentration that gives phase separation. These are large numbers and they are large for a reason: they separate elements with different chlorocomplex chemistry. The same system reports no rare-earth-against-rare-earth separation, and the measurements are at 0.05-0.10 mol/kg metal, 23 °C, in synthetic chloride solutions.

The one demonstration on a real feed follows the same pattern. A one-pot leaching-extraction process using [P44414]Cl-HCl ABS selectively extracts Fe (\>99%) from dissolved {index}`NdFeB` magnet while leaving the REEs in the aqueous phase (\<10% extracted) [@liu2022one]. That is a genuinely useful unit operation — iron rejection is a real problem in magnet recycling — and it is an REE/Fe separation, which is to say a group separation that leaves the hard part untouched.

#### Three-Liquid-Phase Systems (TLPS)

TLPS consisting of salt-rich bottom aqueous phase, polymer-rich middle phase, and organic top phase provide gradients of hydrophobicity for enhanced selectivity [@wang2021strategy]. The {index}`Cyanex272 <Cyanex 272>`/PEG 2000/(NH4)2SO4-H2O system was developed for *stripping* heavy rare earths from a loaded organic phase rather than for extracting them from a leachate, with the separation adjustable through polymer concentration, salt concentration, pH and DTPA addition. It is worth noting that this system is only two-thirds aqueous: the organic top phase is Cyanex 272, so the environmental argument that motivates the rest of the chapter applies to it only partially.

### Coordination-Enhanced Coacervates
If selectivity has to come from a ligand, the obvious move is to attach a known
REE extractant to the phase-forming polymer. Three ligand families are
candidates.

**Phosphonates** are the basis of the industrial extractants
({index}`HDEHP`, {index}`PC88A`, Cyanex 272) and the family with the most
process precedent. Polymer-supported phosphonate extractants \[D201\]\[DEHP\] and \[D201\]\[C272\] show pronounced {index}`scandium` selectivity, with adsorption maximizing near pH 0.78 and, in a nickel-laterite leach liquor, little competition from the base metals present [@cui2016high]. The paper reports no separation factor against the lanthanides, so it demonstrates that the immobilization strategy works, not that it fractionates a series.

**Aminocarboxylates** — DTPA, EDTA and relatives — bind lanthanides strongly with modest size-based selectivity. Their role is usually as holdback reagents in the aqueous phase of an ABS rather than as the primary extractant, precisely because their selectivity is weak but their affinity is high, which is what a competing complexation needs.

**{index}`Diglycolamides <diglycolamide>`** (DGA) show size-dependent lanthanide binding that tracks the lanthanide contraction, making them the most interesting of the three for intra-series work and the least explored in a coacervate context. Polymer-supported extracting materials of all these kinds are reviewed by @croft2024polymer, whose framing is worth borrowing: their advantage is using the *same* extractants as commercial solvent extraction with far less of them, an incremental improvement on a proven chemistry rather than a new one.

### Case Studies: Specific REE Pair Separations
#### Light REE: La/Ce and Ce/Pr Separations
Cerium is the one lanthanide whose +4 state is stable enough in aqueous
solution to separate on, which makes the oxidative route available: Ce⁴⁺ can be
selectively precipitated as CeO₂, or extracted with a partition coefficient
quite unlike Ce³⁺'s.

The ionic radius differences are small --- La³⁺ = 1.032 Å, Ce³⁺ = 1.01 Å, Pr³⁺ = 0.99 Å in six-coordination [@shannon1976revised] --- and both conventional extractants and proteins find them hard. The protein result that does fractionate this stretch of the series is the engineered LanD chaperone described above, at SF Ce/La = 3.0, Pr/Ce = 1.7 [@larrinaga2024modulating].

#### Nd/Pr Separation
The Nd/Pr separation ("didymium" problem) is critical for permanent magnet recycling. These elements have nearly identical ionic radii (Nd³⁺ = 0.983 Å, Pr³⁺ = 0.99 Å in six-coordination [@shannon1976revised]) and similar coordination chemistry, making separation extremely difficult [@zhang2024remarkably].

Four recent results bound what is possible, and they are not commensurable with
one another. The largest number belongs to a process that is not a liquid-liquid
extraction at all: selective dissolution of Nd₂O₃ from a solid Nd/Pr *oxide
mixture* into an ionic liquid containing the β-diketone
2-thenoyltrifluoroacetone gives β(Nd/Pr) \> 500, which the authors report as
277 times the previously published values [@zhang2024remarkably]. That is a
striking result on a binary oxide feed, and a separation factor measured on
solid dissolution cannot be compared like-for-like with one measured between
two liquid phases. Next, PC88A-impregnated surfaces separate Pr+Nd *as a group*
from the heavy rare earths — not from each other — at SF = 171, reaching 92%
Pr+Nd purity at 96% yield from a 10 mg/L all-REE feed at pH 2.5, a figure the
authors themselves describe as comparable with solvent extraction
[@zhang2023separation]. Third, kinetic rather than equilibrium separation of
Pr from Nd has been demonstrated using specific ion effects [@sui2023kinetic];
the separation factor reported in that work could not be verified from any
source available here and is therefore not quoted. Fourth, a push-and-pull
column using [A336][NO3] with DTPA as the aqueous complexant enhances Pr/Nd
separation by combining extraction kinetics in one direction with complexation
in the other [@wang2019enhanced]. Both of the kinetic results are part of a
wider programme on rate-based rather than equilibrium-based separation, which
[](#kinetics-and-mass-transfer) sets out.

No coacervate has been applied to this pair. The routes that would be worth
trying are the ones the four results above suggest: exploiting kinetic rather
than thermodynamic differences, coupling to a selective Pr³⁺/Pr⁴⁺ oxidation,
or engineering a protein interface for Nd/Pr specifically.

#### Heavy REE Separations (Dy, Ho, Er, Yb, Lu)
Heavy REEs have smaller ionic radii and typically prefer lower coordination numbers than light REEs. The ionic radius differences between adjacent heavy REEs are very small (\< 0.02 Å), making separation particularly challenging.

Three-liquid-phase systems with Cyanex272/PEG/ammonium sulfate show promise for heavy REE stripping with tunable selectivity [@wang2021strategy].

The protein work on the heavy end is the most advanced part of this chapter and
also the part where the evidence base is narrowest — three papers, one research
group, no independent replication. Hans-LanM discriminates light from heavy REEs through metal-sensitive dimerization, and an interface mutant separates an Nd/Dy mixture to \>98% purity in a single-stage column [@mattocks2023enhanced]; Nd/Dy is a light/heavy split rather than an adjacent pair. The related LanD chaperone, engineered at the same interface, fractionates *within* the light lanthanides, enriching Pr and Nd over La and Ce [@larrinaga2024modulating]. Most recently, dimerization has been engineered deliberately rather than merely exploited: tandem dimers of the dimerizing lanmodulin Al-LanM, immobilized on a column so that they self-dimerize on it, nearly double SF(Nd/Dy) relative to the immobilized monomer, and separate Y, Dy, Gd, Sm and Nd from one another to \>95% purities from a mixed rare earth leachate derived from allanite ore, using one pH step per element [@choi2026near]. This is the closest any protein system has come to fractionating the heavy end, it is the only one of the three run on an ore-derived feed, and it is where the reported adjacent-element average of 2.1 comes from.

#### Sc Separation
Scandium is geochemically associated with REEs but has distinct chemistry: a much smaller ionic radius (Sc³⁺ = 0.745 Å in six-coordination, against 0.861 Å for the smallest lanthanide [@shannon1976revised]), lower coordination number preference, and unique complexation behavior. That gap is an order of magnitude larger than the adjacent-lanthanide gap, which is why scandium separation is the one place in this chapter where large selectivities are routine and unremarkable.

Four approaches are represented in the sources verified here:

- Polymer-supported phosphonate extractants \[D201\]\[DEHP\] and \[D201\]\[C272\], which show unusual selectivity for scandium and little competition from the base metals of a nickel-laterite leach liquor; the paper reports no separation factor against the lanthanides [@cui2016high]
- Amic acid extractants (D2EHAG, D2EHAF) in solvent extraction and in {index}`polymer inclusion membranes`, giving complete Sc separation from Ni, Al, Co, Mn, Cr, Ca and Mg under strongly acidic conditions [@kim2019separation]
- Mesoporous silica with unmodified silanols for selective Sc extraction over Fe [@ramasamy2017selective]
- TRPO-modified resins for Sc and Zr in sulfuric and hydrochloric acid media [@hou2024adsorption]

A critical review of Sc/Fe separation emphasizes the importance of functional ligands and complexing agents for solid-phase extraction [@gangadari2025critical]. Every one of these separates scandium from something that is not a lanthanide.

## Computational and Modeling Approaches
Computational methods provide fundamental understanding of coacervate thermodynamics, structure, and metal ion interactions, guiding the rational design of separation systems.

### Molecular Dynamics Simulations
Molecular dynamics simulations of coacervates are mostly coarse-grained rather than atomistic, and the level of description determines what can be asked of them. The coacervation study this chapter leans on uses a coarse-grained, implicit-solvent model with thermodynamic analysis of the potential of mean force along the coacervation pathway [@chen2022driving]; solvent enters it only through the dielectric constant, so it speaks to polymer-ion interactions and free energies but not to solvation shells or water structure. An all-atom explicit-solvent treatment would be needed for those. What the two levels between them address:

- Ion solvation and coordination environments (all-atom only)
- Polymer-polymer and polymer-ion interactions
- Water structure in coacervate vs supernatant phases (all-atom only)
- Free energy profiles for ion transfer between phases

A key finding from MD simulations is that the thermodynamic driving force for coacervation is entropy-dominated under typical aqueous conditions. The temperature dependence of the dielectric constant of water contributes substantially to the entropic term in electrostatic interactions [@chen2022driving].

### Thermodynamic Modeling
#### Voorn-Overbeek Theory

The classical Voorn-Overbeek (VO) theory combines Flory-Huggins mixing entropy with Debye-Hückel electrostatics [@overbeek1957phase; @priftis2012early]. While capturing the essential physics of coacervation, VO theory treats backbone charges as disconnected free ions and neglects chain connectivity correlations.

#### Random Phase Approximation (RPA)

RPA extends mean-field theory by including correlation corrections to the electrostatic free energy, improving predictions for charge sequence effects and salt dependence.

#### PC-SAFT and Molecular Equations of State

Perturbed-chain statistical associating fluid theory (PC-SAFT) and related equations of state provide rigorous molecular thermodynamic models for polyelectrolyte solutions [@ascani2025molecular]. These approaches address strong charge correlations and the complex interplay of short-range and long-range interactions.

### Field-Theoretic Simulations
Field-theoretic simulations (FTS) using complex Langevin sampling provide approximation-free phase diagrams for coacervate systems [@lee2008complex; @delaney2017theory]. The point of the method is that it makes no mean-field approximation and samples the fluctuations of the electrostatic and composition fields properly, which is what lets it locate spinodal and binodal boundaries rather than merely bracket them, and what lets it be extended to multicomponent and multiphase systems [@chen2022multiphase]. Applied to IDP coacervation, it reproduces how charge patterning moves the phase boundaries [@mccarty2019complete] — the same result quoted above from a different direction, and one of the few places in this chapter where theory and measurement meet on a specific number.

### Machine Learning Approaches
Machine learning has obvious targets here — predicting polymer properties from sequence, screening candidate coacervate formers, inverse-designing for a target selectivity — and, in this application, no published results this chapter can point to. The bottleneck is data: no body of measured coacervate-REE partition coefficients exists to train on, so generating one is the prerequisite rather than the application. Work bridging the theoretical frameworks — field theory, ion pairing, explicit simulation — into a unified account of polyelectrolyte complexation is a more productive current direction [@qin2023bridging; @li2024thermodynamic].

(process-considerations)=
## Process Considerations
Translation of coacervate-based separations from laboratory to industrial scale requires addressing process engineering challenges.

### Continuous Processing
{index}`Microfluidic <microfluidics>` platforms are the natural laboratory format for coacervate work, because what they control is what coacervation is sensitive to: mixing of the two polymer streams, residence time and flow rate, and in-situ observation of the phase separation. Droplet operation additionally gives the high surface-to-volume ratio that fast mass transfer needs. What microfluidics does not give is throughput, and that gap is discussed at length in [](#process-intensification-the-numbers).

Integrated into an existing hydrometallurgical flowsheet, a coacervate step would sit as follows:

- Leaching: acidic dissolution of REE-bearing minerals
- Coacervate extraction: selective partitioning into polymer-rich phase
- Back-extraction: stimuli-triggered release to stripping solution
- Polymer recovery: regeneration for reuse

These four steps are panel (b) of [](#fig-coacervate-phase-diagram), and the
middle two are the same move on the phase diagram read in opposite directions:
into the two-phase window to load, back out of it to strip.

### Environmental and Economic Factors
The case for aqueous coacervate systems over organic solvent extraction is
mostly a case about the diluent. Removing kerosene removes the VOC emissions,
the fire and explosion hazard, and the solvent inventory that dominates the
environmental footprint of a conventional circuit, and it permits biological
components that an organic diluent would denature. Milder operating conditions
follow. None of these advantages is in dispute, and none of them is a
separation.

The objections are substantial. Metal loading per unit volume is lower than an
organic extractant achieves, which means more equipment for the same duty. The
polymer is a consumable unless it can be recovered quantitatively, and its cost
is poorly characterized because nobody has bought any at scale for this
purpose. And there is no industrial experience of any kind.

That last point has a directly relevant cautionary precedent. Ionic liquids
arrived in extractive metallurgy twenty years ago with an argument structurally
identical to the one made for coacervates: a novel solvent, tunable, greener,
promising selectivities in academic papers. After two decades,
@binnemans2023ionic — pioneers of the field, and the senior authors of the
IL-ABS work cited above — concluded that no IL or DES process is being
seriously considered for industrial implementation, and listed why: viscosity
two to three orders of magnitude above water, limited chemical stability under
process conditions, difficulty of recycling, absence of pilot-scale flowsheets,
missing engineering property data, regulatory burden, prohibitive cost at
scale, and minimal added value over state-of-the-art hydrometallurgy. Their
summary judgement — that water is a wonderful solvent, that there is none
cheaper, and that a novel solvent merely *as good as* a conventional one gives
no reason to switch — is the test any coacervate proposal has to pass.
Coacervates have one advantage ionic liquids did not, in that their continuous
phase *is* water. They share the polymer-cost, recycling and
missing-property-data problems entirely.

A rigorous {index}`techno-economic <techno-economic analysis (TEA)>` analysis would have to price the polymer inventory and the equipment against a conventional circuit, price the operating cost of energy, reagents and polymer replacement, put a number on the achievable separation efficiency and purity, and account for waste and emissions on both sides. No such analysis exists for a coacervate REE process, which is unsurprising given that the separation efficiency term would have to be assumed rather than measured. The biodegradability and recyclability of the polymer components are the terms most likely to decide the outcome and are the least characterized.

(challenges-and-future-directions)=
## Challenges and Future Directions
### Selectivity for Adjacent Lanthanides

A coacervate has to generate intra-series selectivity from one of four things:
a pre-organized binding site that discriminates on size, a coordination-number
preference that shifts across the series, a kinetic rather than thermodynamic
difference in binding or release, or brute-force staging that multiplies a
small factor into a large purity. The first three are chemistry that has not
been done for a coacervate. The fourth is available immediately, and is how the
one successful protein column works [@mattocks2023enhanced]: a separation factor
of 8 amplified over many plates, not a separation factor of 100.

### Polymer Design, Integration and the Barriers to Translation

The polymer development agenda follows: incorporate genuinely selective ligands
(lanmodulin-inspired binding pockets, diglycolamides), build in a response that
gives controlled capture and release, and make the result cheap enough to buy
and durable enough to cycle. Recyclability and stability over cycling are the
properties nobody currently reports, and the ones a process engineer would ask
for first.

Hybrid approaches are the most likely near-term route, because they let a
coacervate contribute the property it actually has — an aqueous, mild,
ligand-compatible phase — while something else supplies the staging. Polymer
inclusion membranes containing coacervate-forming polymers or selective
extractants offer continuous separation with a reduced solvent inventory
[@kim2019separation], and the wider family of polymer-supported extracting
materials is reviewed by @croft2024polymer. Coacervate-coated chromatographic
stationary phases, redox-driven electrochemical separations, and
coacervate-assisted crystallization are all plausible and none is demonstrated
on rare earths.

The barriers to commercialization are the ordinary ones, and none is close to
being addressed: polymer synthesis has to scale, the process has to be robust
in a way no bench demonstration tests, REE products face regulatory
qualification, the incumbent solvent-extraction infrastructure is built and
depreciated, and no pilot-scale demonstration on a real feedstock has been run.
The last would move the field most: a single kilogram-scale campaign on an
actual leachate would settle more questions than another decade of binary model
systems.

## Conclusions
Coacervate-based separation offers a genuinely attractive premise — a
liquid-liquid separation in which both liquids are water — and, at present,
very little evidence that the premise can be cashed. The physics of
coacervation is solid and the mechanisms of metal partitioning are understood;
the applications to rare earths are mostly proposals, or results on adjacent
problems.

1.  **Biomimetic approaches show the highest *group* selectivity**: lanmodulin discriminates rare earths from calcium and the common leachate cations by roughly eight orders of magnitude, and does so at pH 2.5 in real coal and e-waste liquors [@cotruvo2018lanmodulin; @deblonde2020selective]. Its intra-series discrimination is far weaker. Engineered dimer-interface variants have delivered a light/heavy split (Nd/Dy, \>98% purity, single-stage column) [@mattocks2023enhanced], a light-lanthanide enrichment (Pr,Nd over La,Ce) [@larrinaga2024modulating], and near-adjacent heavy separations from an ore-derived leachate [@choi2026near], but no adjacent-pair separation factor comparable to a solvent-extraction cascade has been reported. The right place for these ligands in a flowsheet is upstream concentration and group separation, not adjacent-pair fractionation. All of this work comes from one research group and has not been independently replicated.

2.  **Aqueous biphasic systems are the most developed, on the wrong problem**: IL-based ABS and polymer-salt systems have demonstrated practical separations of rare earths from *transition metals* — Sm/Co, Nd/Fe, Eu/Zn, La/Ni [@kumar2022separation], and Fe rejection from NdFeB magnet leachate [@liu2022one] — and cloud point extraction has a lanthanide track record going back two decades [@neves2022liquid; @favrerguillon2004cloud]. The separation of one rare earth from another by an ABS remains undemonstrated.

3.  **Stimuli-responsive coacervates are demonstrated as switches, not as separations**: pH-triggered assembly and disassembly is fully reversible in a model system [@love2020reversible], the coacervate interior demonstrably shifts redox thermodynamics [@wang2025quantification], and thermoresponsive polymers cycle metal uptake and release for divalent transition metals [@kumar2023comprehensive; @zhong2021thermoresponsive]. No published work closes the loop on a rare earth in a coacervate.

4.  **Computational methods are ahead of the experiments**: field-theoretic simulation gives approximation-free phase diagrams [@lee2008complex; @delaney2017theory], MD settles the driving-force question [@chen2022driving], and charge-pattern effects on the coacervation window are quantitative [@mccarty2019complete]. What is missing is the measured partition data that would let any of it be applied to rare earths.

5.  **The unmet needs are specific**: an adjacent-lanthanide separation factor measured in a coacervate; a measured binodal for an REE-relevant system; polymer cost and cycle life; and a demonstration at more than bench scale on a real feedstock.

The most useful next experiments are correspondingly concrete: peptide-based
coacervates carrying lanthanide-selective motifs; a stimuli-responsive system
run through a full extract-strip-regenerate cycle with a lanthanide in it; a
hybrid in which a membrane or electrochemical stage supplies the staging; and a
campaign on a real leachate at more than bench scale. Until at least the first
and last of those exist, the fair summary is that coacervates are a promising
solvent looking for a selectivity, and that the selectivity is the hard part.
