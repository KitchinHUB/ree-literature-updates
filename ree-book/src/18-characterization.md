---
title: Characterization Methods
---

(characterization-methods)=
# Characterization Methods

A separation is only as good as the analysis that measures it. This chapter
covers the techniques used to quantify rare earths in process streams and to
understand what is happening at the molecular level in an extraction system —
two rather different jobs with different instruments.

The analytical side is dominated by ICP-MS and ICP-OES, and the difficulties are
mostly interference problems: rare earth oxides and doubly-charged ions land on
the masses of their neighbours, so the very similarity that makes the separation
hard also makes the measurement hard. The speciation side — X-ray absorption
spectroscopy, NMR, vibrational spectroscopy and calorimetry — is where the
mechanistic picture in [](#thermodynamics-of-extraction) comes from.

Throughput matters as much as accuracy for the work described in
[](#high-throughput-and-computational-methods): a screening campaign that
generates a thousand extraction conditions a week needs an analysis that keeps
up with it.

## Choosing an Instrument by Choosing a Question

A list of analytical techniques is not useful on its own. What makes one useful
is knowing which question it answers, because the questions a separations
laboratory actually asks are few and the instruments sort cleanly among them.

*How much of each element is in this sample?* This is the routine question, the
one asked of every raffinate and every strip liquor, and it is answered by the
plasma-source methods — ICP-OES, ICP-MS and their laser-ablation and
chromatographically coupled variants — with X-ray fluorescence and neutron
activation analysis filling specific niches that the plasma methods handle
badly. The technical content of this group is almost entirely about
interferences and about matrix.

*What is bound to what?* This is the mechanistic question, and it is the one that
matters most for developing an extractant, because it is how an extraction
mechanism is established rather than inferred. UV-visible and luminescence
spectroscopy report on the metal, vibrational spectroscopy and NMR on the
ligand, X-ray absorption spectroscopy on the coordination shell, and
electrospray mass spectrometry on the stoichiometry of the complex that
survives into the gas phase. No one of them settles a mechanism; a convergent
answer from three or four of them usually does. A representative example is the
characterization of the rare earth–P507 system in a microfluidic contactor,
where FTIR, UV-Vis, NMR and mass spectrometry were run on the same extracts and
together established that lactic acid, present as a complexant in the aqueous
phase, does not enter the extracted species at all, and that the complex forms
by cation exchange at the P–O–H group together with coordination at the P=O
oxygen [@chen2019characterization]. Any one of those measurements alone would
have left the lactic acid question open.

*How strong is the binding, and why?* Isothermal titration calorimetry and
potentiometric titration answer this, and they are complementary rather than
alternative: potentiometry returns equilibrium constants, calorimetry returns
the enthalpy and entropy that those constants are made of.

*What does the material look like, and where are the rare earths in it?*
Electron microscopy and the porosity methods answer this for solids — ores,
adsorbents, precipitates — and the answer usually determines whether a
hydrometallurgical route is viable before any leaching is attempted.

The chapter is organised in that order, and closes with the two calculations —
distribution coefficient and separation factor — that turn analytical numbers
into the quantities the rest of the book uses.

## How Much of Each Element Is Present?

### Inductively Coupled Plasma Optical Emission Spectrometry (ICP-OES)

ICP-OES is the workhorse of a separations laboratory, and it earns that position
by tolerance rather than by sensitivity. An argon plasma at atmospheric pressure
is a forgiving sample introduction system: it accepts high acid concentrations
and high total dissolved solids without the signal suppression that the sampling
interface of a mass spectrometer suffers, it measures every rare earth
simultaneously from a single aspiration, and its consumables and service costs
are a fraction of an ICP-MS. For process solutions — where concentrations are in
the milligram-per-litre to gram-per-litre range and the matrix is a
several-molar acid loaded with base metals — it is very often the correct
instrument, and reaching for ICP-MS instead buys sensitivity that the sample
does not need while inviting matrix problems it does not have.

What it buys with that robustness is a spectral interference problem. The
lanthanides have partially filled 4f shells and correspondingly rich emission
spectra: each element contributes hundreds of usable lines, and in a solution
containing all of them the lines overlap extensively. The consequence is that
line selection is not a one-time instrument setup but part of method
development, and it has to be redone when the matrix changes, because a line
that is clean in a nitric acid standard may sit under an iron or calcium line in
a real leach liquor. This is the routine reason a reported ICP-OES rare earth
analysis is wrong, and it is why matrix-matched calibration standards are not
optional.

Where the matrix is dominated by a single heavy element the practical remedy is
to remove it before the plasma rather than to fight it spectrally. In the
determination of trace rare earths in uranium materials, extracting the uranium
into tri(2-ethylhexyl)phosphate reduced the uranium concentration in the
raffinate from roughly 40,000 mg/L to under 10 mg/L, after which the raffinate
could be analysed directly by either ICP-OES or ICP-MS, with spike recoveries in
U₃O₈ and UO₂ falling between 94% and 106% across both instruments
[@cheng2020determination]. That is a general pattern worth noticing: a
separation problem upstream of the instrument is usually cheaper to solve than
the interference it would otherwise create inside it.

### Inductively Coupled Plasma Mass Spectrometry (ICP-MS)

ICP-MS trades the tolerance of ICP-OES for three to four orders of magnitude of
sensitivity, and it is the reference method whenever the question involves trace
concentrations — environmental samples, raffinates that are supposed to be
clean, or the low-concentration tail of a loading curve. Detection limits are
quoted for it more freely than for any other technique in this book and almost
always without the two things that determine them, namely the matrix and the
sample introduction system. A figure worth quoting is one measured under stated
conditions: in a fully automatic online system that strips the salt matrix on an
iminodiacetic/ethylenediaminetriacetic resin column before the plasma, 3σ
detection limits for the rare earths in a 3.5% NaCl matrix ranged from 0.002
ng/L for Dy to 0.097 ng/L for La, validated against the NASS-6 seawater
reference material [@li2022development]. Sub-nanogram-per-litre performance of
that kind is real, but it is the performance of the *whole method*, matrix
elimination included. Aspirating an undiluted process liquor with percent-level
dissolved solids gives detection limits orders of magnitude worse, and quoting
the seawater figure for that sample would be a straightforward misrepresentation.

Instrument architecture matters as much as the nominal detection limit. A
single-quadrupole instrument is the routine choice and the cheapest. A
triple-quadrupole adds a reaction cell between two mass filters, which allows an
analyte to be chemically mass-shifted away from an interference rather than
merely discriminated against — the most effective available answer to the oxide
problem described below. A multi-collector instrument gives up scanning speed
and dynamic range to measure several isotopes simultaneously on separate
detectors, which is what isotope dilution and geochronology require; rapid and
highly reproducible rare earth determination by MC-ICP-MS is well established
for exactly these applications [@baker2002rapid]. A separations laboratory
rarely needs the third of these, but it is the instrument behind most of the
reference values its standards are traceable to.

#### The interference problem, and what actually works

The interferences fall into four kinds, and they are not equally tractable.

| Interference type | Example | What works |
|-------------------|---------|------------|
| Oxide formation | BaO⁺ on Eu | Tune the oxide rate down, correct mathematically, or remove the parent |
| Hydroxide | REEOH⁺ on the heavier REEs | Collision/reaction cell; desolvating sample introduction |
| Isobaric | ¹⁴²Ce on ¹⁴²Nd | A different analyte isotope, or correction from a Ce-only mass |
| Matrix effects | High dissolved solids | Dilution, matrix matching, internal standard, matrix removal |

**Why the ¹⁴²Ce/¹⁴²Nd isobar cannot be resolved by mass resolution.** The two
nuclides differ by about 0.0015 u, so separating them requires a mass resolving
power near 10⁵. Commercial sector-field ICP-MS tops out an order of magnitude
below that, and multi-collector instruments are operated at lower resolution
still, so no available instrument resolves this pair. There are two workable
alternatives. The first is simply to quantify Nd on a mass Ce does not reach —
¹⁴³Nd, ¹⁴⁵Nd or ¹⁴⁶Nd — which is what most laboratories do. The second is to
measure ¹⁴⁰Ce, which is free of Nd, and subtract the Ce contribution to mass 142
using the natural ¹⁴²Ce/¹⁴⁰Ce abundance ratio (≈0.126). The mathematical
correction is only as good as the assumption of natural Ce isotopic composition
and degrades once the Ce/Nd ratio in the sample is large, so the alternative
isotope is preferred whenever sensitivity allows.

**Kinetic energy discrimination (KED)** supplies non-reactive helium that
collides with polyatomic ions, lowering their kinetic energy so that a downstream
potential barrier rejects them preferentially over the atomic analyte ion. It is
the standard defence against argide and other polyatomic interferences, and it
allows higher dissolved solids to be run without extreme dilution. It is much
less effective against metal monoxides, for the reason given below.

**Oxide interferences, element by element.** The general statement "BaO⁺ on Eu"
is not enough to choose isotopes. Because the monoxide MO⁺ appears 16 mass units
above its parent, and because the REEs span a contiguous block of masses, a light
REE almost always has a monoxide sitting on a heavy REE. The table below lists
the principal MO⁺ overlaps a separations laboratory will meet, with the
mitigation that actually works for each [@dulski1994interferences; @balaram2019rare].

| Analyte | Oxide interferent | Mitigation |
|---------|-------------------|------------|
| ¹⁵¹Eu | ¹³⁵Ba¹⁶O⁺ | Ba is usually the largest single problem; ¹⁵³Eu is no escape (¹³⁷Ba¹⁶O⁺ lands there). Remove Ba chromatographically, or correct mathematically from ¹³⁷Ba and a measured BaO⁺/Ba⁺ ratio |
| ¹⁵⁷Gd | ¹⁴¹Pr¹⁶O⁺ | Mathematical correction from ¹⁴¹Pr (monoisotopic, so the correction is clean); every other Gd isotope carries a LaO⁺, CeO⁺ or NdO⁺ overlap |
| ¹⁵⁹Tb | ¹⁴³Nd¹⁶O⁺ | Tb is monoisotopic — no alternative mass. Minimize oxide formation, then correct from ¹⁴³Nd |
| ¹⁶³Dy | ¹⁴⁷Sm¹⁶O⁺ | Correct from ¹⁴⁷Sm; ¹⁶¹Dy and ¹⁶²Dy trade this for ¹⁴⁵Nd¹⁶O⁺ and ¹⁴⁶Nd¹⁶O⁺ |
| ¹⁶⁵Ho | ¹⁴⁹Sm¹⁶O⁺ | Ho is monoisotopic — correct from ¹⁴⁹Sm |
| ¹⁶⁶Er | ¹⁵⁰Nd¹⁶O⁺ (and ¹⁵⁰Sm¹⁶O⁺) | Two parents contribute at mass 166; correct from both, or use ¹⁶⁷Er and correct for ¹⁵¹Eu¹⁶O⁺ |
| ¹⁶⁹Tm | ¹⁵³Eu¹⁶O⁺ | Tm is monoisotopic — correct from ¹⁵³Eu |
| ¹⁷⁵Lu | ¹⁵⁹Tb¹⁶O⁺ | Correct from ¹⁵⁹Tb; ¹⁷⁶Lu is worse, carrying isobaric ¹⁷⁶Yb and ¹⁷⁶Hf |

Three general remedies apply across the table. First, **tune the oxide rate
down**: the standard figure of merit is CeO⁺/Ce⁺, measured on a Ce solution
during setup, because Ce forms one of the most stable REE monoxides and so
represents a near-worst case for the rest. Routine tuning targets a percent or
two; a desolvating nebulizer or a cooled spray chamber pushes it substantially
lower, and the correction
residuals fall with it. Second, **correct mathematically**: aspirate a
single-element solution of each interfering parent, measure its MO⁺/M⁺ ratio at
the same tune, and subtract that fraction of the parent's signal from the
analyte mass. This is reliable only while the correction is a small part of the
analyte signal — a correction larger than the signal it corrects is not a
measurement. Third, **remove the interferent**, either by chromatographic
separation of the REEs upstream of the plasma (which is what the HPLC-ICP-MS and
online-separation methods below are for) or, on a triple-quadrupole instrument,
by reaction-cell chemistry that mass-shifts analyte and interferent to different
product masses. Collision-cell helium with KED helps far less here than it does
for argide interferences, because MO⁺ and M⁺ have similar collision cross
sections. Note also that the samples most likely to defeat all of this are the
ones a separations laboratory actually generates: a raffinate from a Nd/Sm
system is, by construction, enormously enriched in one REE relative to its
neighbours, which is precisely the condition that makes an oxide correction
large.

### Separating Before Detecting: HPLC, IC, and Online Systems

The most general answer to the interference problem is to present the elements
to the detector one at a time. High-performance liquid chromatography and ion
chromatography separate the rare earths on a column and quantify them as they
elute, and they have been used for this since long before ICP-MS was routine;
they remain attractive because they are comparatively cheap, and because the
chromatographic step removes the matrix as a side effect [@verma2007high].

The separation chemistry is the same weak-complexation chemistry that the rest
of this book is about. Cation-exchange separations elute the lanthanides with a
gradient of a complexing eluent such as α-hydroxyisobutyric acid, exploiting the
same monotonic trend in complex stability across the series that drives solvent
extraction. Ion-interaction chromatography instead forms an anionic complex in
the mobile phase and retains it on a reversed-phase column coated with a
lipophilic counter-ion, which produces an elution order that is not monotonic at
all: with diglycolic acid as the complexant on a C18 column, the predicted and
observed order of elution runs
Sc < La < Ce < Lu < Pr < Yb < Nd < Tm < Sm < Eu < Er ≈ Y < Gd < Ho < Tb ≈ Dy,
because retention rises from La towards the Tb–Dy–Ho region and then falls again
[@dybczynski2021separation]. An unfamiliar elution order is a genuine practical
hazard here: peaks assigned by assumed order rather than by standards will be
assigned wrongly.

Detection after the column is by UV-visible absorbance following post-column
derivatization with a chromogenic reagent such as chlorophosphonazo III, or by
feeding the eluent directly into an ICP-MS. The second option is the more
powerful, since it combines chromatographic removal of interferences with
mass-spectrometric sensitivity, and it is the basis of the automated online
systems that make ultra-trace work in difficult matrices possible at all
[@li2022development]. Coupling the separation to the detector also removes the
sample-handling step that limits throughput, which is why online sequential
extraction feeding directly into a mass spectrometer has been pursued as a
high-throughput route for rare earth determination [@zhang2021high] — the
throughput argument of [](#high-throughput-and-computational-methods) applies to
the analysis as much as to the experiment.

Ion {index}`chromatography` with chelating stationary phases — iminodiacetate,
nitrilotriacetate and carboxyl-functionalized silicas — serves the related
purpose of separating the rare earths as a group from base metals in geological
and process materials [@ahmed2020chromatographic].

### X-Ray Fluorescence (XRF)

XRF is the only technique in this group that requires no dissolution. A pressed
powder pellet or a fused lithium borate bead is measured directly, which makes
XRF the natural choice for solid feed materials, for process control on ores and
concentrates, and for any sample too precious to destroy. It has been applied to
rare earths since about 1970, in both energy-dispersive and wavelength-dispersive
forms, and reliable results depend above all on careful optimization of the
measurement — in particular on the choice of spectral lines — with quantification
resting on calibration against reference materials of similar composition
[@schramm2016use]. That last point is the practical constraint: XRF is a
comparative method, and without matrix-matched standards a rare earth
determination by XRF is a semi-quantitative one.

The spectroscopic difficulty is line overlap in the L-line region where the
lanthanides are measured. Neighbouring rare earth L-lines can be separated by
only a few electron-volts, which an energy-dispersive detector cannot resolve,
particularly in the presence of transition-metal K-lines from the gangue. This
is what wavelength dispersion is for. A recent instrument that disperses the
L-lines between 4.5 and 7 keV with a fixed Ge(111) crystal onto an
energy-dispersive pnCCD detector achieves 12 eV resolution at the Ti Kα line and
a sensitivity down to 0.50 ppm for rare earth L-lines, which is enough to
analyse inclusions in diamonds non-destructively [@depauw2020highly]. That is a
specific instrument on a specific sample geometry, not a general XRF
specification; handheld energy-dispersive instruments used for field screening
are several orders of magnitude less sensitive and should be treated as
prospecting tools rather than analytical ones.

### Neutron Activation Analysis (NAA)

NAA irradiates the sample with neutrons, producing artificial radionuclides
whose gamma emissions are counted on a high-resolution germanium detector. It
was the method of choice for rare earth analysis from the early 1960s through
the 1980s, and the reason it mattered is worth stating precisely: after
high-resolution gamma detectors arrived in the mid-1960s, most applications no
longer required chemical separation of the rare earths from the matrix at all
[@stosch2016neutron]. The measurement is nuclear rather than chemical, so it is
essentially matrix-independent, and in its instrumental form it is
non-destructive.

Two things bound its usefulness. The first is chemical: instrumental NAA is
sensitive for only about half the rare earths — La, Ce, Nd, Sm, Eu, Tb, Yb and
Lu — because the others lack a convenient combination of neutron capture cross
section, product half-life and gamma yield, and reaching them requires
radiochemical separation after irradiation. The second is precision: NAA is less
precise than isotope-dilution mass spectrometry, and modern practice compensates
with internal-standard methods rather than by improving the counting statistics
[@silachyov2016rare]. Together with the decommissioning of research reactors
across Europe and North America and the arrival of ICP-MS, these limits explain
why NAA has declined from the standard method to a specialist one
[@stosch2016neutron]. It survives where its distinguishing properties are
decisive: samples that must not be destroyed, samples whose matrix defeats
dissolution, and situations where an entirely independent method is needed to
validate a chemical one.

### LA-ICP-MS: How Much, and Where

Laser ablation replaces the nebulizer with a pulsed laser that samples a small
spot on a solid surface and carries the aerosol into the plasma. The
consequence is spatial resolution: with spot sizes on the order of tens of
micrometres, individual mineral grains and zones within grains can be analysed
separately, and elemental maps can be built by rastering. For rare earth work
this matters because the elements are almost never uniformly distributed. A
bulk digestion of an ore reports an average that may correspond to no phase
actually present, whereas LA-ICP-MS reports which mineral carries the rare
earths — the question that determines whether a beneficiation step will work.
Coupled to a multi-collector instrument it also supports in situ Sm–Nd and Lu–Hf
isotope analysis and U–Pb geochronology on {index}`monazite`, apatite and
titanite [@lin2024situ]. The trade is calibration: without a matrix-matched
solid standard, laser ablation quantification carries systematic errors that
solution nebulization does not.

## What Is Bound to What? Speciation and Structure

### UV-Visible Absorption Spectroscopy

The f–f transitions of the trivalent lanthanides are formally forbidden, which
makes them weak, but they are also narrow and largely insensitive to the
surroundings, because the 4f orbitals are shielded by the filled 5s and 5p
shells. Both properties follow from the same shielding, and both are useful. The
narrowness means the band positions are characteristic of the ion and are
transferable enough between compounds that reference libraries covering the
whole series are worth compiling — one such library records the UV-visible
absorption spectra of the orthophosphates LnPO₄ from La to Lu
[@sharma2020library] — so that individual lanthanides can be identified and
quantified in a mixture rather than separated first. The weakness means the
technique is limited to the concentrations a process stream actually carries
rather than to trace analysis.
The residual sensitivity of certain "hypersensitive" transitions to the
coordination environment is what allows UV-Vis to report on complexation at all.

The property that makes UV-Vis genuinely valuable in separations is that it
requires no sample removal. An absorbance probe can sit in a flowing stream and
report continuously, which turns a laboratory measurement into process
instrumentation. In a simulated TALSPEAK process, Nd³⁺ was monitored
simultaneously at up to six locations on a single centrifugal contactor — the
aqueous and organic inlets and outlets — using a multi-track visible absorbance
detector with chemometric models to convert spectra to concentrations; the
integrated moles of Nd³⁺ entering and leaving agreed to near zero, closing the
mass balance in real time [@tse2024spectroscopic]. Real-time material
accountancy of that kind is a different capability from off-line analysis: it
detects a drifting contactor while it is drifting, rather than after the
campaign.

### Luminescence and Fluorescence Spectroscopy

Several lanthanides emit sharp, characteristic line spectra when excited,
arising from the same shielded 4f manifold, and the emission is far easier to
detect against a dark background than a weak absorbance is against a bright one
[@khan2019rare]. The most-used emitters and their diagnostic transitions are

| Ion | Colour | Transition | Approximate wavelength |
|------|--------|------------|------------|
| Eu³⁺ | Red | ⁵D₀ → ⁷F₂ | 615 nm |
| Tb³⁺ | Green | ⁵D₄ → ⁷F₅ | 545 nm |
| Dy³⁺ | Yellow | ⁴F₉/₂ → ⁶H₁₃/₂ | 573 nm |
| Sm³⁺ | Orange | ⁴G₅/₂ → ⁶H₇/₂ | 600 nm |

Direct excitation of a forbidden f–f transition is inefficient, and the standard
remedy is the antenna effect: an aromatic ligand absorbs strongly in the
ultraviolet and transfers the energy to the metal, so that the observed emission
intensity depends on the ligand as much as on the metal. For a separations
chemist this cuts both ways. It gives a sensitive readout of whether a designed
ligand is coordinating — the emission appears when the complex forms — and it
means luminescence intensity cannot be read as a concentration unless the
speciation is already known and fixed. Europium is the most informative case,
because the intensity ratio between its ⁵D₀ → ⁷F₂ and ⁵D₀ → ⁷F₁ bands responds
to the symmetry of the coordination site, making the ion a structural reporter
rather than merely a label.

### FTIR and Raman Spectroscopy

Vibrational spectroscopy looks at the ligand rather than the metal, and answers
the questions the metal-centred methods cannot: which functional group is
coordinated, whether the coordination is inner- or outer-sphere, and whether a
ligand is bound at all. The signature is a frequency shift in the coordinating
group on complexation — the P=O stretch of an organophosphorus extractant, the
carbonyl of an amide, the carboxylate asymmetric/symmetric splitting that
distinguishes monodentate from bidentate binding. In a solvent extraction
context this is often the cleanest evidence available that a proposed extraction
reaction is the one occurring [@fieser2016raman; @chen2019characterization].

Sensitivity to the metal across the series follows from the same mechanism.
Vibrational frequencies of a coordinated ligand track the Lewis acidity of the
metal centre, which rises across the series as the ionic radius contracts. In
rare earth dinitrogen complexes, for example, the N–N Raman stretching frequency
changes regularly from Gd to Tm — that is, with *increasing* atomic number,
decreasing ionic radius, and increasing Lewis acidity [@fieser2016raman]. That
regularity is the point: a vibrational frequency that varies smoothly with
lanthanide identity is a probe of the small energetic differences a separation
has to exploit, and one that can in principle be measured in situ.

### NMR Spectroscopy

Paramagnetic lanthanides shift the resonances of nuclei near them, sometimes
enormously, and the shift carries structural information [@cockerill1973lanthanide].
Two mechanisms contribute. The contact (Fermi) shift arises from unpaired
electron spin density delocalized onto the observed nucleus through bonds, and
matters most for nuclei directly bonded to the metal. The pseudocontact
(dipolar) shift arises through space from the magnetic anisotropy of the metal
centre and depends on the position of the nucleus relative to the magnetic axes.
For the 4f lanthanides the pseudocontact term usually dominates, which is what
makes the shifts geometrically interpretable: they encode distances and angles
rather than merely connectivity.

The historical application, lanthanide shift reagents, exploited this to spread
out crowded proton spectra of organic molecules by adding a europium or
praseodymium β-diketonate. That use has largely been displaced by
high-field instruments and multidimensional experiments, and for a reason worth
understanding rather than merely noting: the same unpaired electrons that shift
the resonances also relax them, and the resulting line broadening scales
unfavourably with field strength, so the technique gained least from exactly the
hardware improvement that transformed the rest of NMR. Where the object of study
*is* the lanthanide complex, however — and in extraction chemistry it usually is
— the paramagnetic shift is signal rather than nuisance, and the practical
strategies are to choose a less strongly shifting and less strongly relaxing ion
where the chemistry allows a substitution, and to work at elevated temperature to
narrow the lines.

### X-Ray Absorption Spectroscopy (XANES and EXAFS)

X-ray absorption spectroscopy is element-specific by construction: the
measurement is made at the absorption edge of the element of interest, so a
dilute rare earth in a complicated matrix can be interrogated without separating
it. For the lanthanides the L-edges are used, the K-edges lying at
inconveniently high energy. The technique divides into two regimes of the same
spectrum. The near-edge region (XANES) reports oxidation state and, more
qualitatively, coordination geometry; it is the standard way to distinguish
Ce(III) from Ce(IV), which matters directly to the cerium oxidation separations
used industrially. The extended fine structure (EXAFS) oscillations above the
edge encode the radial distribution of neighbouring atoms, and fitting them
returns coordination numbers, the identity of the neighbours, and interatomic
distances to within a few hundredths of an ångström.

The characteristic application is determining the mode of occurrence of rare
earths in a material that resists every other approach. In coal and coal
combustion byproducts, XANES linear-combination fitting identified silicate and
phosphate minerals as the dominant yttrium-bearing phases, and EXAFS curve
fitting showed that the host phase undergoes minimal transformation during
combustion — the rare earths are transferred essentially in bulk from the coal
to the ash [@bishop2024rare]. That is a result with direct process consequences:
it says the leaching chemistry that works on the coal is the leaching chemistry
that will be needed on the ash.

The cost is access. XAS on dilute samples requires a synchrotron, which means
beamtime proposals and campaigns rather than routine measurement, and this
constrains it to questions important enough to justify the overhead. Laboratory
X-ray absorption spectrometers have improved considerably and can now handle
more concentrated samples, but they do not replace synchrotron access for
process-relevant concentrations.

### Electrospray Ionization Mass Spectrometry (ESI-MS)

Electrospray transfers ions from solution to the gas phase gently enough that
weakly bound metal–ligand complexes survive, which makes it the most direct
available measurement of complex stoichiometry: the mass spectrum shows which
ML, ML₂ and ML₃ species are present, in what relative abundance, and how those
abundances change with metal-to-ligand ratio and pH
[@indelicato2021approaches; @geue2024modern]. Isotope patterns identify the
metal unambiguously, and ternary systems can be probed for competitive binding
in a single experiment.

The caveat is fundamental rather than technical. What is measured is the ion
population that survives desolvation and transmission to the detector, not the
solution population, and the mapping between them is not one-to-one: ionization
efficiencies differ between species, adducts form, and labile complexes can
dissociate or rearrange in the source. An ESI-MS peak is therefore good evidence
that a species *can* exist and poor evidence for its solution concentration.
Used alongside potentiometry or optical spectroscopy, which measure solution
equilibria but do not identify stoichiometry directly, it is a strong
combination; used alone to assign a speciation model, it is not.

## What Are the Binding Thermodynamics?

### Isothermal Titration Calorimetry (ITC)

ITC measures the heat evolved as ligand is titrated into a metal solution, and
from a single titration returns the association constant, the binding enthalpy,
the stoichiometry, and — from ΔG = −RT ln K and ΔG = ΔH − TΔS — the entropy
[@bastos2023isothermal]. That last point is the reason the technique matters
here. Every other method in this chapter returns an equilibrium constant, which
is a free energy; ITC is the only one that decomposes the free energy into its
enthalpic and entropic parts without assuming a temperature dependence.

The decomposition is not a formality for lanthanide chemistry, because the
dominant term is usually not the metal–ligand bond at all but the dehydration
that precedes it. A trivalent lanthanide in water carries a tightly held inner
hydration shell; forming an inner-sphere complex means displacing part of it,
which costs enthalpy and releases entropy, while the new metal–ligand bonds
return enthalpy and cost entropy. The measured ΔH and ΔS are differences between
large opposing terms, and whether a given complexation appears enthalpy- or
entropy-driven depends on how much water is displaced. This is precisely what
cannot be inferred from a stability constant, and it is why two ligands with
nearly identical log K can behave quite differently as the temperature or the
solvent changes. Non-aqueous and mixed solvents change the balance substantially,
because they change what has to be displaced [@desbouis2012thermodynamics], and
the thermodynamics of lanthanide complexation with the polydentate N,O-donor
ligands used in separations has been characterized this way alongside structural
determination of the coordination mode [@chen2019complexation].

ITC also works directly on biphasic systems, which is not obvious: the heat
measured on contacting an aqueous metal solution with an organic extractant
phase is the enthalpy of extraction ΔH_extr, the quantity a thermodynamic cycle
of the kind built in [](#thermodynamics-of-extraction) is trying to predict.
This has been done for Eu(NO₃)₃ with a tripodal {index}`diglycolamide` extractant
in a {index}`solvent extraction <solvent extraction>` system, giving a directly
measured enthalpy of extraction rather than one inferred from the temperature
dependence of a distribution ratio [@ansari2016thermodynamics].

### Potentiometric Titration

Potentiometry is the oldest of these methods and remains the reference source
for stability constants. It is also the cheapest, which is why it is worth being
clear about what it does and does not return.

**What the titration actually yields.** A potentiometric titration of a
ligand alone returns the ligand's own protonation constants — for an
aminopolycarboxylate such as {index}`MGDA <methylglycinediacetic acid>`
(methylglycinediacetic acid) these are the pKa values of its carboxylate and
amine groups. Repeating the titration with metal present, and fitting the
displaced titration curve, returns the metal-ligand stability constants
log K(ML), log K(ML₂) and, where relevant, the conditional (pH-dependent)
constant log K′ at the working pH. A metal complex does not have a "pKa" in
this sense; the only pKa a complex can be said to have belongs to a coordinated
water molecule or to a protonatable site left free on the bound ligand, and
either must be identified explicitly. Reported numbers should therefore say
which quantity they are, at what ionic strength and temperature, because
conditional constants are not comparable across pH and stability constants are
not comparable across background electrolyte.

Two practical points recur. First, the technique is indirect: it detects the
metal only through the protons the metal displaces from the ligand, so it works
well for ligands with protonatable donors and poorly for neutral extractants
that release none. Second, trivalent rare earths hydrolyse, and a hydrolysing
metal acts as a Brønsted acid, contributing to the measured pH change and
biasing the fitted constants if it is not accounted for. The remedies are to
work at pH low enough that hydrolysis is negligible, to include hydrolysis
constants explicitly in the fitted model, or to add a competing complexant such
as oxalate that holds the metal in a known form during the titration. The same
apparatus, used more prosaically, measures free acid concentration in process
liquors and checks the purity of a synthesized extractant through its
protonation curve — routine work, and the reason a potentiometric titrator is
present in laboratories that never determine a stability constant.

## What Does the Material Look Like?

### SEM-EDS

Scanning electron microscopy with energy-dispersive X-ray spectroscopy is the
first measurement made on almost any solid rare earth material, and its role is
to establish mineralogy rather than composition. Backscattered electron contrast
scales steeply with mean atomic number, so rare earth phases appear bright
against a silicate gangue before any spectrum is collected, and EDS mapping then
assigns them. The automated forms of this — SEM-based automated mineralogy,
mineral liberation analysis, QEMSCAN — turn it into a quantitative modal
analysis over thousands of particles, which is what a beneficiation flowsheet is
designed from [@ali2023mineral].

The limits are worth stating plainly, because SEM-EDS is often asked to do work
it cannot. Its elemental detection floor is far above that of any solution
method: EDS sees an element when it is a constituent of a phase, not when it is
an impurity in one, so rare earths dispersed at trace level through a gangue
mineral are invisible to it even when they dominate the bulk assay. Its spatial
resolution for composition is set by the electron interaction volume rather than
by the probe, and is therefore on the micrometre scale regardless of how finely
the beam is focused — a submicrometre inclusion analysed by EDS returns a
mixture of the inclusion and its host. And rare earth L-line overlaps in the EDS
spectrum are severe at the modest energy resolution of a silicon drift detector,
which is where multivariate methods enter: principal component analysis to
denoise a phase map, and blind source separation — with non-negative matrix
factorization outperforming independent component analysis for this problem — to
unmix overlapping spectral components into physically interpretable phases
[@teng2020multivariate].

### TEM

Transmission electron microscopy, with electron energy loss spectroscopy or
EDS on the same instrument, extends the same questions below the resolution
where SEM-EDS stops mattering. The case for doing so is that rare earth
occurrence in weathered and processed materials is often nanoscale, and a
micrometre-resolution technique averages over exactly the association that
controls the chemistry. Combining SEM-EDS, TEM and EELS on acid sulfate soils
and adjacent estuarine sediments resolved a recurring nanoscale association
between iron phases and lanthanum-bearing particles that bulk chemical
extractions could not have distinguished from a distinct mineral phase
[@xu2018micro]. For a separations audience the transferable lesson is about
adsorbed versus mineral-bound rare earths: the two require different recovery
chemistry and are indistinguishable in a bulk assay.

### Thermal Analysis

Thermogravimetry follows mass as a function of temperature and differential
scanning calorimetry or differential thermal analysis follows heat flow;
run simultaneously they identify both what is lost and whether losing it absorbs
or releases heat. In rare earth processing the recurring applications are the
calcination of precipitated oxalates and carbonates to the oxide — where the
mass-loss steps define the temperature schedule an industrial calciner needs —
the dehydration of hydrated phosphates and sulfates, and the thermal stability
of loaded organic extractants and adsorbents, which sets an upper bound on
regeneration temperature. A transition that appears in the heat-flow trace with
no accompanying mass loss is a phase change rather than a decomposition, and
distinguishing the two is the reason the combined measurement is preferred to
either alone.

### Surface Area and Porosity

Adsorbent-based separations, treated at length elsewhere in this book, depend on
accessible surface area and on pore dimensions comparable to the hydrated ion
being adsorbed, and gas physisorption measures both. Nitrogen adsorption at 77 K
analysed by the BET method returns a specific surface area; the shape of the
full isotherm classifies the material as microporous, mesoporous or
macroporous; and a pore size distribution is extracted from the isotherm by
model. The choice of model is not a detail: BJH is adequate for mesopores but
systematically misestimates micropore sizes, and non-local density functional
theory methods should be used below about 2 nm.

Reported surface areas for a given class of material — mesoporous silicas,
metal–organic frameworks, activated carbons, biochars — span more than an order
of magnitude within the class, depending on synthesis and activation, so a
class-level figure is not a meaningful specification and none is quoted here.
The number that matters for a separation is the surface area of the specific
material as synthesized, measured on the same batch used in the uptake
experiment, together with evidence that the pores are accessible to a solvated
trivalent ion rather than merely to nitrogen [@oztug2024overview].

## From Measurement to Number

### Speciation Calculation

"Process modeling" in an analytical context means aqueous speciation — what
species exist in a solution and which solids can precipitate from it. It is the
input to a flowsheet model rather than the model itself;
[](#process-modeling-and-optimization) treats the flowsheet scale, where these
speciation calculations supply the equilibrium closure that stage-wise cascade
balances need.

Several mature codes do this. PHREEQC from the USGS is open-source and the most
widely used; the Geochemist's Workbench is the commercial equivalent with
integrated graphics and Pitzer activity models for concentrated solutions; EQ3/6
from LLNL targets high-temperature systems; MINTEQA2 remains common in
environmental work.

The essential caution is that a code is not a model. A calculation requires
three things — the executable, the input file, and a thermodynamic data file —
and it is the data file that supplies every equilibrium constant the answer
depends on. Speciation, mineral solubilities and gas concentrations calculated
for the same input with different data files can differ substantially, and the
practice of reporting "the PHREEQC model" or "the MINTEQ model" of a system
without stating which thermodynamic data were used has been criticised
directly, and named, as flying blind [@zhu2022flying]. For rare earths the
concern is sharper than for the major ions the general-purpose databases were
built around: lanthanide complexation constants are sparser, less internally
consistent, and more often extrapolated. Specialised compilations exist —
THEREDA for nuclear waste systems, the OECD Nuclear Energy Agency database for
the f-elements — and choosing among them is a decision the modeller owns, not
one the software makes.

### Measuring the Distribution Coefficient

The distribution coefficient

$$
D = \frac{[\mathrm{REE}]_\mathrm{org}}{[\mathrm{REE}]_\mathrm{aq}}
$$

is defined in [](#solvent-extraction-fundamentals) and reported in almost
every extraction paper, yet it is the measurement most often made badly. The
definition involves two concentrations, and the practical question is which of
them you actually measure.

**By difference, or directly.** The cheapest protocol measures the feed and the
raffinate — both aqueous, both compatible with the same ICP calibration — and
infers the organic loading from the depletion:
`[REE]_org = ([REE]_feed − [REE]_aq) × (V_aq/V_org)`. The alternative is to
analyse the organic phase itself, either by back-extracting it into a strong
acid or by digesting an aliquot. Direct analysis costs an extra step and an
extra calibration; by difference costs nothing and is defensible over a
surprisingly narrow range.

**Where by difference fails.** The rule is that you must never obtain by
difference the phase holding most of the metal. Take D = 0.01 at a phase ratio
O/A = 1: the aqueous retains 99.0% of the feed, and the whole organic loading is
carried by a 1.0% depletion. Propagate a 2% relative uncertainty on the feed and
on the raffinate — optimistic for routine ICP-OES — and that 1.0% difference
arrives with roughly 280% relative uncertainty. The reported D is
indistinguishable from zero. Direct analysis of the organic phase turns the same
experiment into a few-percent measurement, because the small quantity is then
measured rather than inferred. The mirror-image failure is measuring only the
organic and taking the raffinate by difference when D = 100, where the aqueous
holds under 1% and the same arithmetic applies with the phases exchanged. As a
working rule, by difference is acceptable while the depletion exceeds roughly a
quarter of the feed, i.e. while `D × (O/A)` is of order 0.3 or larger; outside
that window, analyse the minority phase directly. At D ≫ 1 there is a second,
harder limit: once the raffinate approaches the detection limit, or once a
percent of entrained organic droplets in the aqueous aliquot puts a floor under
the apparent aqueous concentration, the experiment can only report a lower bound
on D. Say so rather than quoting a number.

**Matrix matching.** Standards must match the solution that is actually
aspirated. Aqueous samples should be calibrated in the same acid at the same
molarity, with the same background salt, because acid strength and total
dissolved solids both change transport efficiency and plasma loading. Organic
samples are the harder case: a kerosene or dodecane phase cannot be quantified
against aqueous standards. Either back-extract quantitatively into acid and
calibrate as an aqueous sample — the usual choice, and the one that keeps a
single calibration — or aspirate the organic with organometallic standards in
the same diluent, oxygen addition to the plasma, and a cooled spray chamber. An
internal standard (In or Rh) should be present in every solution either way.

**Mass balance is the check that catches the mistakes.** Measure both phases,
not one, and close the balance:
`[REE]_feed × V_aq = [REE]_aq × V_aq + [REE]_org × V_org`. Closure within a few
percent is the evidence that D means what you think it means. Poor closure is
diagnostic rather than merely annoying: metal missing from both phases points to
third-phase formation, precipitation at the interface, or sorption on the vessel
walls, while apparent excess usually means a dilution factor or a phase volume
was recorded wrongly. Record the volumes actually used, not the volumes intended
— mutual solubility and entrainment change them — since every D computed by
difference and every mass balance depends on V_aq/V_org. Where the contactor
allows it, the online spectroscopic monitoring described above closes the same
balance continuously rather than at the end [@tse2024spectroscopic].

**Do not assume equilibrium.** Contact times quoted in the literature are
frequently inherited rather than measured. Establish the equilibration time once
for each new system by sampling a time series — for example 1, 2, 5, 10, 30 and
60 minutes at fixed temperature and agitation — and plotting D against time to
confirm a plateau. Chelating and macrocyclic extractants, systems near their
loading limit, and low-pH conditions where the extraction is slowest are the
cases where an assumed contact time silently returns a kinetic rather than an
equilibrium D. Report the contact time, the temperature, and the phase ratio
alongside the value.

### Separation Factor

The {index}`separation factor <separation factor>` is a ratio of distribution
coefficients,

$$
\beta_\mathrm{REE1/REE2} = \frac{D_\mathrm{REE1}}{D_\mathrm{REE2}}
$$

and inherits every uncertainty in both. In a multicomponent mixture two
conventions are in use: an *effective* separation factor built from the
adjacent-element factors weighted by the component fractions, and an
*equivalent* separation factor that lumps the mixture into a pseudo-binary
system. Which is intended should always be stated, since they do not agree.

A useful internal check on any table of separation factors: for a single
extractant, β against a common reference element should vary monotonically with
atomic number, because D itself varies monotonically. A tabulated set in which
β(Pr/La) exceeds β(Nd/La) — Pr sits between Ce and Nd — is either a
transcription error or the result of mixing systems, and should not be used.
Representative measured separation factors for named extractant systems are
given in [](#solvent-extraction-fundamentals).

Machine learning enters here as a way of extrapolating from measured
distribution coefficients to unmeasured ligands: neural networks trained on
experimental extraction data have been used to predict distribution coefficients
for high-throughput ligand screening [@liu2022advancing], an approach developed
further in [](#machine-learning-in-rare-earth-separations). The models are only
as good as the D values they are trained on, which returns the argument to the
measurement practice above.

## Choosing Among Them

The table below is a qualitative orientation, not a set of specifications.
Detection limits in particular are properties of a whole method — instrument,
sample introduction, matrix and sample preparation together — and the entries
give only the order of magnitude a well-set-up method reaches on a favourable
sample. Any figure that will be quoted needs to come from a source that states
its conditions.

| Technique | Reaches roughly | Sample | Answers |
|-----------|-----------------|--------|---------|
| ICP-OES | µg/L in solution | Liquid | How much, routinely, in a difficult matrix |
| ICP-MS | ng/L and below in clean matrices | Liquid | How much, at trace level |
| MC-ICP-MS | ng/L, with isotope-ratio precision | Liquid | Isotope ratios, isotope dilution, geochronology |
| LA-ICP-MS | Trace, on a tens-of-µm spot | Solid | How much, and in which grain |
| XRF | ppm (WDXRF) to percent (handheld) | Solid | How much, without dissolution |
| NAA | Trace, matrix-independent, ~8 REEs by INAA | Solid | How much, non-destructively and independently |
| HPLC / IC | µg/L to mg/L | Liquid | How much, with the interferences separated away |
| UV-Vis | Process concentrations | Liquid, in situ | How much, continuously, in a running contactor |
| Luminescence | Trace, for the emissive ions | Liquid, solid | Whether a complex formed; site symmetry |
| FTIR / Raman | — | Liquid, solid | Which group is coordinated |
| NMR | — | Liquid | Coordination geometry, ligand exchange |
| ESI-MS | — | Liquid | Complex stoichiometry |
| ITC | — | Liquid | ΔH and ΔS of binding |
| Potentiometry | — | Liquid | Stability and protonation constants |
| XAS | Dilute, with a synchrotron | Solid, liquid | Oxidation state, coordination shell |
| SEM-EDS | Minor-constituent level | Solid | Which mineral, and how liberated |
| TEM-EELS | Minor-constituent level, nanoscale | Solid | Nanoscale associations |

Read down the last column rather than across the second. The instrument that
answers the question being asked is almost always the right one, and the
sensitivity comparison only decides between instruments that answer the same
question.
