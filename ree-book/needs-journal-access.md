# Claims that could not be verified without journal access

This file is the standing to-do list for the one category of correctness
problem this project could not close on its own.

The book's rule is that a citation which resolves is not thereby correct: the
cited work has to actually contain the claim. Verifying that means reading the
paper. For most of the bibliography that was possible — abstracts and full text
came from CrossRef, OpenAlex, Europe PMC, Semantic Scholar and OSTI, and where a
publisher's own site refused (Springer, RSC and Elsevier all block automated
access) OpenAlex usually still returned an abstract.

The entries below are the residue: cases where the specific number in the book
sits in a table, a figure, or a methods section that no open interface exposes.
None of them is known to be wrong. Each is a claim standing on an abstract or on
a secondary description rather than on the passage that contains it.

**What to do with each one:** pull the PDF, find the number, and either confirm
it, correct it, or delete the sentence and say plainly that the figure is not
established. Do not resolve one by finding a different paper that happens to
report a similar number.

**Where the PDFs go:** `fulltexts/`, which is gitignored — publisher PDFs are
not redistributable and must never be committed. Name each file by its citation
key, e.g. `huang2002rare.pdf`. Issue #1 lists every entry in this file with
its DOI and what specifically to look for, in a suggested retrieval order.

## Flagged claims

| Chapter | Citation key | What rests on it |
|----|----|----|
| 07 Pyrometallurgical and halogenation routes (also cited in 04) | `huang2002rare` | The selective chlorination / vacuum-thermal purity, yield and thorium-partitioning figures. The abstract does not carry them. |
| 08 Coacervates and aqueous two-phase systems | `favrerguillon2004cloud` | Cloud-point extraction performance figures. |
| 08 Coacervates and aqueous two-phase systems (also 14) | `sui2023kinetic` | The kinetically enhanced Pr/Nd separation factor. Chapter 08 already declines to quote it. |
| 11 Biological and biomimetic separations | `zhou2018leaching` | Bioleaching recovery figures. |
| 11 Biological and biomimetic separations | `zhang2018bioleaching` | Bioleaching recovery figures. |
| 11 Biological and biomimetic separations | `deng2025application` | Application-scale claims. |
| 11 Biological and biomimetic separations | `kore2024application` | Application-scale claims. |
| 14 Kinetics and mass transfer | `cao2021extraction` | The extraction rate constants and kinetic separation factors for La/Gd/Ho/Lu with HEHEHP. |
| 14 Kinetics and mass transfer (also 08) | `wang2019enhanced` | The Pr/Nd separation factor from the push-and-pull column. |
| 14 Kinetics and mass transfer | `sui2024nonequilibrium` | The Tm/Y/Er separation performance on rising oil droplets. |
| 15 High-throughput and computational screening | `an2024agile` | Synthesis details of the automated platform. |
| 17 Machine learning in rare earth separations | `zhang2026predicting` | Reported model performance. |
| 17 Machine learning in rare earth separations | `liu2026machine` | Reported model performance. |
| 04 Technology landscape, 06 Ion-adsorption clays, 21 Environment/TEA/LCA | `wang2022electrokinetic` | The electrokinetic mining performance figures: ~2.6× recovery efficiency, ~80 % less leaching agent, ~70 % fewer metallic impurities, and the "autonomous purification" mechanism. |
| 04, 06, 21 | `wang2025industrial` | 95 % REE recovery on a 5,000 t ore body, the 95 % ammonia-emission reduction, and the comparative technoeconomic analysis, whose values the abstract does not give at all. |
| 10 Precipitation and selective crystallization | `li2018photochemical` | Cited alongside the Van den Bogaert work; no value is taken from it, but its scope is known only from the abstract. |
| 12 Electrochemical separations | `zhao2022selectively` | 9.55 at.% pyrrolic-N doping, 128.98 F/g capacitance, 23.66 mg/g La in 25 min, and the La/Fe/Ca/Na selectivity. |
| 12 Electrochemical separations | `zhan2024regulating` | The "essentially complete" recovery from low-concentration feed, and the chemisorption-electrosorption coupling mechanism on O-doped MoS₂. |
| 12 Electrochemical separations | `aziman2021rapid` | 8.4 mg Th per g of carbon, and the isotherm and kinetic model fits. |
| 13 Membranes, MOFs and emerging | `behera2025supramolecular` | The transport selectivities — ~140 Tb/La, 72 Tb/Yb, 58 Tb/Nd, \>40 Eu/La, ~30 Eu/Yb, ~17 Eu/Nd — and the \>18:1 Ln/K⁺ figure. These are the largest membrane numbers in the book and rest entirely on the abstract. |
| 13 Membranes, MOFs and emerging | `wang2023graphene` | The actinide/lanthanide separation factor of up to ~400 and the interlayer-spacing mechanism. |
| 13 Membranes, MOFs and emerging | `bao2025mxene` | 892.8 mg/g Eu(III) and 649.2 mg/g Ho(III) at pH 2.0, and 99.1 % Eu removal by the PES-supported membrane at pH 5.0. |
| 13 Membranes, MOFs and emerging (also 04) | `xiao2022highly` | β = 15.34 Eu/Yb, 14.70 Eu/Tm, 10.78 Eu/La for the deep-eutectic-solvent TpPa COFs. |
| 13 Membranes, MOFs and emerging | `chatterjee2024efficient` | The \>40× uptake over the pristine imine COF and \>4× over the next-best DGA support. |
| 19 Characterization | `sun2025nanopore` | The three-level current transitions, the claim that the periodicity tracks the lanthanide contraction, and the identification of all sixteen natural rare earths. |
| 05 Hydrometallurgical leaching | `liu2023mechanochemical` | 98.2 % YF₃-to-Y(OH)₃ conversion at room temperature and 96.2 % yttrium leaching from calciothermic slag. |
| 20 Recycling and urban mining | `mukaba2021rare` | The \>2000 mg/kg total REE in phosphogypsum against a normal \<0.1 wt %, and the assessment that recrystallization is the most promising route. |
| 20 Recycling and urban mining | `virolainen2019recovering` | The resin-in-leach loading of 19.2 g/kg at up to 20 % purity over four cross-current stages, against 3 % for the strong-acid resin. |
| 20 Recycling and urban mining | `brewer2019recovery` | Biosorption tolerance to 165,000 ppm TDS, the pH 5-6 optimum and ~65 % capacity loss at pH 2, and the improvement to ~70 °C. |
| 20 Recycling and urban mining | `tian2020rare` | The 4.5-118.3 µg/L total REE and 0.92-79.62 µg/L Eu in Sichuan flowback water, and the 4.2 t → 16.8-111.7 t Eu₂O₃ projection. |

## A gap, not a flag

Chapter 05, Hydrometallurgical leaching, states no overall rare earth recovery figure
for any leaching route, anywhere in the chapter. That is deliberate: no source
consulted for this book gives one that survives the check, and inventing a
plausible range would be exactly the failure mode the whole project is built to
avoid. Restoring a number here needs journal access to the primary
process-metallurgy literature. Until then the absence is the honest answer, and
the chapter says so rather than leaving a reader to assume an omission.

## Cited for existence, with no number taken

A second and milder category, introduced with chapter 14, Kinetics and Mass
Transfer, and extended by the 2026 literature-gap pass. These are sources whose
abstracts are not exposed by any interface reachable from here — some are
pre-2000 Elsevier and ACS papers that predate structured abstracts in the
aggregators, others are recent papers behind publishers that block automated
access. The book cites them for what their titles establish (that a measurement
was made, of what, by what method) and quotes no value from any of them; the
prose says so at each point. Nothing in the text depends on their contents, so
none of these is a correctness risk in the way the table above is. They are
listed because reading them would let the chapters say more than they currently
do.

| Citation key | What the chapter would gain |
|----|----|
| `geist1999kinetics` | Measured rate constants for rare earth extraction into D2EHPA, and which step controls. |
| `cossy1988oxygen` | Water-exchange rate constants across the Ln(III) aqua ions, and how much of the series ¹⁷O NMR could actually reach. |
| `gabelman1999hollow` | Mass-transfer correlations for hollow-fibre contactors; currently cited only as the standard review. |
| `tian2010kinetics` | Rate law and activation energy for ammonium sulfate leaching of weathered-crust ore. |
| `he2016kinetics` | The same for column leaching, including the aluminium co-extraction behaviour. |
| `xu2024comparative` | A comparison of leaching agents for electrokinetic mining; would let chapter 06 say which reagent the field method actually favours. |
| `mosadeghsedghi2023chelation` | Chelation-assisted electrodialysis; would let chapter 12 say what selectivity the chelator supplies. |
| `akcaguler2025comprehensive` | A comprehensive treatment of electrochemical rare earth recovery; would let chapter 12 check its own taxonomy against a review. |
| `leblebici2017efficiency` | Photochemical reactor efficiency; would let chapter 10 say whether the Eu photoreduction's illumination times can be engineered away. |
| `zhang2022construction` | Nitrogen-rich COFs for La(III) uptake; would add a second COF data point to chapter 13. |
| `cai2024lithium` | Lithium-intercalated Ti₃C₂Tₓ for Nd adsorption; would add a second MXene data point to chapter 13. |
| `liu2025advances` | A review of reticular materials for rare earth capture; would let chapter 13 place its two examples in a field. |
| `zhang2023mechanochemical` | A second mechanochemical study; would let chapter 05 say whether the approach generalises beyond fluoride conversion. |
| `rychkov2018recovery` | Recovery of rare earths from a secondary source; cited in chapter 20 for existence only. |
| `canovas2019leaching` | Leaching of phosphogypsum; would let chapter 20 state what fraction of the contained rare earths is actually accessible and under what conditions. |
