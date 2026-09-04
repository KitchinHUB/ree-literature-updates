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
hard also makes the measurement hard. The speciation side — EXAFS, NMR, ITC,
and the scattering methods — is where the mechanistic picture in
[](#thermodynamics-of-extraction) comes from.

Throughput matters as much as accuracy for the work described in
[](#high-throughput-and-computational-methods): a screening campaign that
generates a thousand extraction conditions a week needs an analysis that keeps
up with it.

Accurate characterization and analysis are essential for developing, optimizing, and controlling REE separation processes. This section reviews the analytical techniques used for concentration measurement, thermodynamic characterization, structural analysis, and process monitoring.

## Concentration Measurement Techniques
### Inductively Coupled Plasma-Optical Emission Spectrometry (ICP-OES)
ICP-OES is a workhorse technique for REE analysis due to its robustness and multi-element capability ([Analytik Jena](https://www.analytik-jena.com/knowledge/applications/application-teasers/analysis-of-rare-earth-elements-by-icp-oes-and-icp-ms-potentials-and-limitations/), [Spectroscopy Online](https://www.spectroscopyonline.com/view/determination-rare-earth-elements-geological-and-agricultural-samples-icp-oes-0)).

**Characteristics:**

| Parameter | Typical Value |
| ----------- | --------------- |
| Detection limits | 0.009-0.45 mg/L (element-dependent) |
| Linear dynamic range | 5-6 orders of magnitude |
| Precision (RSD) | 1-3% |
| Sample throughput | 20-40 samples/hour |
| Matrix tolerance | High |

**Advantages:**

- Higher matrix tolerance than ICP-MS
- Lower running costs
- Robust sample introduction system
- Good for routine analysis of process solutions

**Challenges:**

- Numerous emission line overlaps between REEs
- Requires careful line selection for each element and matrix
- Lower sensitivity than ICP-MS for trace levels

### Inductively Coupled Plasma-Mass Spectrometry (ICP-MS)
ICP-MS has become the method of choice for REE analysis due to its exceptional sensitivity and multi-element capability ([Agilent](https://www.agilent.com/cs/library/applications/application-ree-icp-oes-5800-5994-4492en-agilent.pdf), [NETL](https://www.netl.doe.gov/sites/default/files/netl-file/Rare-Earth-Trace-Bulk-Elemental-Analysis-ICP-MS-Topical-Report-4-14-2016.pdf)).

**Characteristics:**

| Parameter | Typical Value |
| ----------- | --------------- |
| Detection limits | 2-11 ng/g in the digested solid (ppb; ppt-level in the aspirated solution) |
| Precision (RSD) | \~2.5% |
| Linear range | ppt to ppm |
| Sample throughput | 10-30 samples/hour |

**Instrument Types:**

| Type | Detection Limit | Precision | Applications |
|----|----|----|----|
| Quadrupole (ICP-QMS) | ppt | 1-5% | Routine analysis |
| Triple Quadrupole (ICP-QQQ) | sub-ppt | \<1% | Interference removal |
| Multi-collector (MC-ICP-MS) | ppt | 0.002% (isotope ratios) | Isotope dilution, geochronology |

**Interferences and Mitigation:**

| Interference Type | Example                | Mitigation Strategy               |
|-------------------|------------------------|-----------------------------------|
| Oxide formation   | BaO⁺ on Eu             | KED mode, mathematical correction |
| Hydroxide         | REEOH⁺ on heavier REEs | Collision/reaction cell           |
| Isobaric          | ¹⁴²Ce on ¹⁴²Nd         | Use ¹⁴³Nd, ¹⁴⁵Nd or ¹⁴⁶Nd; or correct mass 142 from ¹⁴⁰Ce |
| Matrix effects    | High TDS samples       | Dilution, matrix matching         |

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

**Kinetic Energy Discrimination (KED) Mode:** KED mode supplies non-reactive helium gas that physically collides with larger polyatomic ions, lowering their kinetic energy and decreasing detection probability. This allows analysis of higher total dissolved solids samples without large dilution factors.

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

### X-Ray Fluorescence (XRF)
XRF enables rapid, non-destructive analysis of solid samples without digestion ([Rigaku](https://rigaku.com/products/xrf-spectrometers/wdxrf/webinars/determining-the-rare-earth-elements-using-wdxrf/summary), [Evident Scientific](https://ims.evidentscientific.com/en/applications/portable-xrf-for-rare-earth-element-identification-and-exploration)).

**Instrument Comparison:**

| Type            | Resolution | Sensitivity            | Portability      | Cost     |
|-----------------|------------|------------------------|------------------|----------|
| WDXRF           | Highest    | Best (ppm level)       | Laboratory       | High     |
| EDXRF           | Moderate   | Good                   | Desktop/portable | Moderate |
| pXRF (handheld) | Lower      | Adequate for screening | Field portable   | Lower    |

**Analytical Challenges:**

- REEs have numerous K-lines (3) and L-lines (\~7) with significant overlap
- Spectral overlap with common elements (Ge, Ni)
- Careful selection of analytical lines and background positions required
- Relative uncertainty on a reported concentration: \~5-10% is typical once line
  overlaps are deconvolved, and worse without matrix-matched standards. This is a
  precision figure, not a detection limit; detection limits are at the ppm level
  for WDXRF (see the comparison table at the end of this chapter)

**TXRF (Total Reflection XRF):** For trace element and contamination analyses, TXRF offers improved sensitivity through sample presentation on optically flat reflectors. Neural network-based modeling has been applied to decode interfering L-lines for direct analysis of lanthanides in water samples.

### Neutron Activation Analysis (NAA)
NAA was the historical standard for REE analysis before ICP-MS ([@stosch2016neutron], [Missouri Archaeometry](https://archaeometry.missouri.edu/naa_technical.html)).

**Principle:** Samples are irradiated with neutrons in a nuclear reactor, creating artificial radioisotopes. Subsequent gamma-ray emission is measured by high-resolution Ge detectors.

**Elements Measurable by INAA:**

- Light REEs (La, Ce, Nd, Sm): 10¹-10² ppm detection
- Eu: High sensitivity due to favorable nuclear properties
- Heavy REEs (Tb, Yb, Lu): 10⁰ ppm detection
- Pr, Er: Require chemical separation (RNAA)

**Characteristics:**

| Parameter           | Value                                 |
|---------------------|---------------------------------------|
| Detection limits    | 10⁻⁷ to 10⁻¹⁵ g/g (element-dependent) |
| Elements detectable | Up to 74                              |
| Sample preparation  | Minimal to none                       |
| Non-destructive     | Yes (for INAA)                        |

**Limitations:**

- Requires access to nuclear reactor
- Declining availability of reactor facilities
- Largely superseded by ICP-MS for routine analysis

## Chromatographic Separation and Analysis
### High-Performance Liquid Chromatography (HPLC)
HPLC provides both separation and quantification of individual REEs [@verma2007high; @dybczynski2021separation].

**Methods:**

| Technique | Stationary Phase | Mobile Phase | Detection |
|----|----|----|----|
| Ion Exchange (IEC) | Cation/anion resin | α-HIBA, EDTA | UV-Vis, ICP-MS |
| Ion Pair RP | C18 | Ion-pairing agent + complexant | Post-column derivatization |
| Ion Interaction (IIC) | C18 | Diglycolic acid (ODA) + TBAOH | UV-Vis |

**Performance:**

- Full REE separation (16 elements except Pm): 55 minutes with α-HIBA gradient
- Detection: Post-column derivatization with chlorophosphonazo III at 660 nm
- Combined HPLC-ICP-MS enables simultaneous determination of 14 REEs in 15 minutes

### Ion Chromatography (IC)
Ion {index}`chromatography` uses specialized stationary phases for REE separation [@ahmed2020chromatographic].

**Recent Developments:**

- Nitrilotriacetate-type chelating resins as stationary phases
- Anhydride-derived carboxyl-functionalized silica (Sil-TMA)
- Analysis time: \~20 minutes for heavy metals and sum of REEs

## Thermodynamic Characterization
### Isothermal Titration Calorimetry (ITC)
ITC is the gold standard for measuring thermodynamics of REE-ligand binding in solution [@bastos2023isothermal; @ansari2016thermodynamics].

**Parameters Measured in Single Experiment:**

| Parameter            | Symbol | Information               |
|----------------------|--------|---------------------------|
| Association constant | K_A    | Binding strength          |
| Enthalpy             | ΔH     | Heat of binding           |
| Entropy              | ΔS     | Calculated from ΔG and ΔH |
| Stoichiometry        | n      | Metal:ligand ratio        |
| Gibbs free energy    | ΔG     | Overall driving force     |

**Key Findings from REE-Ligand Studies:**

- Formation of lanthanide complexes is often **enthalpy-driven** with **unfavorable entropy**
- Enthalpy-entropy compensation observed across lanthanide series
- Solvent effects critical: stability follows PC \> AN \> MeOH \> DMF \> DMSO
- Stepwise 1:1 and 1:2 complexes can be distinguished

**{index}`Solvent Extraction <solvent extraction>` Studies:** ITC has been used to measure enthalpy of extraction (ΔH_extr) of Eu(NO₃)₃ using tripodal {index}`diglycolamide` (T-DGA) in biphasic systems, providing insight into extraction thermodynamics.

### Potentiometric Titration
Potentiometric titration determines pKa values, stability constants, and extractant purity ([University of Idaho Thesis](https://objects.lib.uidaho.edu/etd/pdf/Lyon_idaho_0089N_10815.pdf)).

**Applications:**

- Determination of extractant purity and pKa
- Measurement of acid concentration in process solutions
- Determination of REE-ligand complex stability constants

**Metal Hydrolysis Mitigation:** Metal ions in acidic solution can act as Bronsted acids, causing hydrolysis and lowering pH. This is mitigated by adding 1 M potassium oxalate (5 mL) to complex metal ions before titration.

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

## Spectroscopic Characterization
### UV-Visible Absorption Spectroscopy
UV-Vis spectroscopy exploits the characteristic f-f electronic transitions of lanthanide ions [@sharma2020library].

**Applications:**

- Quantification of individual REEs based on characteristic absorption bands
- Online process monitoring (multi-track visible spectrometer)
- Determination of complex stability constants

**Process Monitoring:** Simultaneous measurement of Nd³⁺ concentration at multiple process locations (inlet/outlet of aqueous and organic phases) enables real-time mass balance and material accountancy.

### Luminescence/Fluorescence Spectroscopy
Lanthanide luminescence provides highly sensitive detection with characteristic sharp emission lines [@khan2019rare].

**Characteristic Emissions:**

| Ion  | Emission Color | Transition     | Wavelength |
|------|----------------|----------------|------------|
| Eu³⁺ | Red            | ⁵D₀ → ⁷F₂      | 615 nm     |
| Tb³⁺ | Green          | ⁵D₄ → ⁷F₅      | 545 nm     |
| Dy³⁺ | Yellow/Blue    | ⁴F₉/₂ → ⁶H₁₃/₂ | 573 nm     |
| Sm³⁺ | Orange         | ⁴G₅/₂ → ⁶H₇/₂  | 600 nm     |

**Laser-Excited Fluorescence:** Fluorescence emission spectra of fluorite containing 226-867 ppm total REEs can be excited by Ar-ion laser. Narrow emission lines (\<1 nm) due to 4f-4f transitions are observed for Pr, Nd, Sm, Eu, Tb, Dy, Ho, Er, Tm in the 400-900 nm range.

**Antenna Effect:** In REE complexes, fluorescence from the central metal ion is strongly sensitized by aromatic ligands through energy transfer, enabling enhanced detection sensitivity.

### FTIR and Raman Spectroscopy
Vibrational spectroscopy characterizes REE-ligand bonding and complex structure [@fieser2016raman].

**Applications:**

- Confirmation of ligand coordination modes
- Identification of inner-sphere vs. outer-sphere complexation
- Characterization of chloride and aqua ligand coordination
- Phase identification in solid REE compounds

**Sensitivity to the metal across the series:** vibrational frequencies of a
coordinated ligand track the Lewis acidity of the metal centre, which rises
across the series as the ionic radius contracts. In rare earth dinitrogen
complexes, for example, the N-N Raman stretching frequency changes regularly
from Gd to Tm — that is, with *increasing* atomic number, decreasing ionic
radius, and increasing Lewis acidity [@fieser2016raman]. The same logic is what
makes vibrational spectroscopy useful in extraction chemistry: the P=O
stretching band of an organophosphorus extractant shifts on complexation, and
the size of that shift reports on how strongly the ligand is bound.

### NMR Spectroscopy
Paramagnetic lanthanide ions produce characteristic shifts in NMR spectra [@cockerill1973lanthanide].

**Lanthanide Shift Reagents (LSR):** Paramagnetic lanthanide complexes (typically Eu³⁺ or Pr³⁺ with β-diketonates) cause significant increases in chemical shifts, simplifying complex absorption patterns.

**Types of Paramagnetic Shifts:**

| Shift Type | Origin | Magnitude |
|----|----|----|
| Diamagnetic | Through-space/through-bond | Small |
| Contact (Fermi) | Unpaired electron density at nucleus | Large for ¹⁷O, ¹³C |
| Pseudocontact (dipolar) | Magnetic anisotropy | Dominant for 4f lanthanides |

**Limitations:**

- Line broadening at high field strengths
- Less widely used today than historically
- Strategies: use smaller shifting ions (Sm³⁺), higher temperature

## X-Ray Absorption Spectroscopy (XAS)
Synchrotron-based XAS provides element-specific structural and electronic information [@bishop2024rare].

### XANES (X-Ray Absorption Near Edge Structure)
**Information Provided:**

- Oxidation state
- Coordination geometry
- Electronic structure
- Bond angles

**Applications:**

- Distinguishing Ce³⁺ vs. Ce⁴⁺ in separation processes
- Characterizing REE speciation in environmental samples
- Identifying mineral host phases

### EXAFS (Extended X-Ray Absorption Fine Structure)
**Information Provided:**

- Interatomic distances (±0.02 Å)
- Coordination numbers
- Debye-Waller factors (disorder)
- Identity of neighboring atoms

**REE Applications:**

- Local structure of lanthanide ions complexed with chelating ligands
- Speciation in coal and coal combustion byproducts
- Minimal transformation of REE host phase observed during combustion

**Technical Requirements:**

- Synchrotron radiation source required
- L-edge XANES primarily used for lanthanides (K-edge at very high energies)
- Recent developments enable some lab-based EXAFS (5-30 keV range)

## Electron Microscopy and Microanalysis
### SEM-EDS (Scanning Electron Microscopy with Energy Dispersive Spectroscopy)
SEM-EDS is widely used for qualitative and semi-quantitative analysis of REE minerals [@ali2023mineral; @teng2020multivariate].

**Capabilities:**

- Detection limits: ≥0.1 wt% (1000 ppm) for high-Z elements
- Spatial resolution: 1-5 μm
- Backscattered electron (BSE) imaging identifies high-Z particles
- EDS mapping for elemental distribution

**Advanced Analysis:**

- Principal Component Analysis (PCA) on EDS datasets enhances phase identification
- Non-negative Matrix Factorization (NMF) algorithms separate mixed EDS signals
- Automated mineralogy systems (AMICS) for high-throughput phase characterization

### TEM (Transmission Electron Microscopy)
TEM with EELS (Electron Energy Loss Spectroscopy) provides nanoscale characterization of REE associations in minerals and processed materials.

**Applications:**

- Nanoscale REE-mineral associations
- Crystal structure determination
- Identification of submicrometer-sized REE crystals

## Thermal Analysis
Thermal analysis techniques characterize phase transitions, decomposition, and thermal stability of REE compounds ([C-Therm](https://ctherm.com/resources/newsroom/thermal-analysis-labs/exploring-the-thermal-properties-of-materials-using-thermogravimetric-analysis-tga-differential-scanning-calorimetry-dsc-and-differential-thermal-analysis-dta/)).

### Thermogravimetric Analysis (TGA)
**Measures:**

- Mass loss as function of temperature
- Decomposition temperatures
- Hydration/dehydration
- Oxidation/reduction

**REE Applications:**

- Decomposition of REE oxalates to oxides
- Dehydration of REE phosphate hydrates
- Thermal stability of REE complexes with organic ligands

### Differential Scanning Calorimetry (DSC) / Differential Thermal Analysis (DTA)
**Measures:**

- Heat flow (DSC) or temperature difference (DTA)
- Endo/exothermic transitions
- Phase changes, melting points
- Glass transition temperatures

**Combined TG/DTA:** Simultaneous analysis provides both mass change and thermal event information:

- Identifies whether decomposition is endothermic or exothermic
- Measures phase transitions without mass loss (melting, crystallization)

## Surface Area and Porosity Analysis
BET analysis characterizes adsorbent materials used for REE separation ([Intertek](https://cdn.intertek.com/www-intertek-com/dms-legacy/IntertekWhitepaper_Surface_Area_and_Porosity_Chemicals170613.pdf), [@oztug2024overview]).

**BET Method:**

| Parameter                | Measurement         |
|--------------------------|---------------------|
| Specific surface area    | m²/g                |
| Pore volume              | cm³/g               |
| Pore size distribution   | nm                  |
| Adsorption isotherm type | I-VI classification |

**Adsorbent Materials Characterized:**

| Material          | Typical Surface Area | Pore Size   |
|-------------------|----------------------|-------------|
| Mesoporous silica | 500-1000 m²/g        | 2-50 nm     |
| MOFs              | 1000-6000 m²/g       | 0.5-3 nm    |
| Activated carbon  | 800-1500 m²/g        | Variable    |
| Diatomite         | \~150 m²/g           | Macroporous |
| Biochar           | 100-500 m²/g         | Variable    |

**Methods for Micropore Analysis:**

- BJH (Barrett-Joyner-Halenda): Adequate for mesopores
- NLDFT (Non-Local Density Functional Theory): More accurate for micropores (\<2 nm)

## Mass Spectrometry for Speciation
### Electrospray Ionization Mass Spectrometry (ESI-MS)
ESI-MS enables direct observation of REE-ligand complexes in solution [@indelicato2021approaches; @geue2024modern].

**Applications:**

- Formation and stoichiometry of metal-ligand complexes
- Changes in speciation with metal:ligand ratio and pH
- Identification of metal oxidation state
- Competitive interactions in ternary systems

**Considerations:**

- Soft ionization preserves weak metal-ligand bonds
- ESI adduct formation and fragmentation can occur
- Different ionization efficiencies among species
- Best used with corroborating techniques (potentiometry, spectroscopy)

### LA-ICP-MS (Laser Ablation ICP-MS)
LA-ICP-MS enables spatially resolved analysis of solid samples [@lin2024situ].

**Applications:**

- In situ analysis of REE-bearing minerals
- Sm-Nd and Lu-Hf isotope analysis in {index}`monazite`, apatite, titanite
- Mapping REE distribution in materials
- U-Pb geochronology

**Spatial Resolution:** 10-100 μm spot sizes typical

## Process Modeling and Speciation Calculation
### Geochemical Modeling Software
Software tools calculate REE speciation, saturation indices, and phase equilibria ([USGS PHREEQC](https://www.usgs.gov/software/phreeqc-version-3), [GWB](https://www.gwb.com/software_overview.php)).

**Major Software Packages:**

| Software | Developer | Features |
|----|----|----|
| PHREEQC | USGS | Open-source, 13 thermodynamic databases |
| Geochemist's Workbench (GWB) | Aqueous Solutions | Commercial, integrated graphics, Pitzer model |
| EQ3/6 | LLNL | High-temperature applications |
| MINTEQA2 | US EPA | Environmental applications |

**Thermodynamic Databases:**

| Database   | Source                | Applications         |
|------------|-----------------------|----------------------|
| llnl.dat   | Lawrence Livermore    | General purpose      |
| pitzer.dat | Various               | High ionic strength  |
| THEREDA    | German repository     | Nuclear waste        |
| NEA-TDB    | Nuclear Energy Agency | Radioactive elements |

**Caution:** Calculated speciation, mineral solubilities, and gas concentrations may vary substantially between different thermodynamic data files. The choice of database is the responsibility of the user.

## Distribution Coefficient and Separation Factor Calculation
Key parameters for solvent extraction process design ([@liu2022advancing], [MDPI 2023](https://www.mdpi.com/2673-6489/3/3/31)).

### Distribution Coefficient (D)
**Definition:**

$$
D = \frac{[\mathrm{REE}]_\mathrm{org}}{[\mathrm{REE}]_\mathrm{aq}}
$$

**Influencing Factors:**

- Extractant type and concentration
- pH
- Temperature
- Diluent type
- Aqueous phase composition

### Measuring D

D is defined in [](#solvent-extraction-fundamentals) and reported in almost
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
difference and every mass balance depends on V_aq/V_org.

**Do not assume equilibrium.** Contact times quoted in the literature are
frequently inherited rather than measured. Establish the equilibration time once
for each new system by sampling a time series — for example 1, 2, 5, 10, 30 and
60 minutes at fixed temperature and agitation — and plotting D against time to
confirm a plateau. Chelating and macrocyclic extractants, systems near their
loading limit, and low-pH conditions where the extraction is slowest are the
cases where an assumed contact time silently returns a kinetic rather than an
equilibrium D. Report the contact time, the temperature, and the phase ratio
alongside the value.

### Separation Factor (β)
**Definition:**

$$
\beta_\mathrm{REE1/REE2} = \frac{D_\mathrm{REE1}}{D_\mathrm{REE2}}
$$

**Multicomponent Systems:** Two approaches for calculating {index}`separation factors <separation factor>` in complex mixtures:

1.  **Effective separation factor**: Function of adjacent element separation factors and component percentages
2.  **Equivalent separation factor**: Converts all components to two-component system

A useful internal check on any table of separation factors: for a single
extractant, β against a common reference element should vary monotonically with
atomic number, because D itself varies monotonically. A tabulated set in which
β(Pr/La) exceeds β(Nd/La) — Pr sits between Ce and Nd — is either a
transcription error or the result of mixing systems, and should not be used.
Representative measured separation factors for named extractant systems are
given in [](#solvent-extraction-fundamentals).

**Machine Learning Approaches:** Deep neural networks trained on experimental data can predict distribution coefficients for high-throughput ligand screening.

## Comparison of Analytical Techniques
| Technique | Detection Limit | Precision | Sample Type  | Throughput | Cost      |
|-----------|-----------------|-----------|--------------|------------|-----------|
| ICP-OES   | ppb             | 1-3%      | Liquid       | High       | Moderate  |
| ICP-MS    | ppt             | 0.5-3%    | Liquid       | Moderate   | High      |
| MC-ICP-MS | ppt (isotope)   | 0.002%    | Liquid       | Low        | Very High |
| XRF       | ppm (WDXRF)     | 1-5%      | Solid        | High       | Moderate  |
| NAA       | ppb-ppt         | 2-5%      | Solid        | Low        | High      |
| HPLC-UV   | ppb-ppm         | 1-5%      | Liquid       | Moderate   | Moderate  |
| ITC       | N/A             | 1-5%      | Liquid       | Low        | Moderate  |
| XAS       | ppm             | 5-10%     | Solid/Liquid | Low        | Very High |
| SEM-EDS   | 0.1 wt%         | 5-10%     | Solid        | Moderate   | Moderate  |
