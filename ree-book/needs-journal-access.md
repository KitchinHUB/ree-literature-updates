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

## A gap, not a flag

Chapter 05, Hydrometallurgical leaching, states no overall rare earth recovery figure
for any leaching route, anywhere in the chapter. That is deliberate: no source
consulted for this book gives one that survives the check, and inventing a
plausible range would be exactly the failure mode the whole project is built to
avoid. Restoring a number here needs journal access to the primary
process-metallurgy literature. Until then the absence is the honest answer, and
the chapter says so rather than leaving a reader to assume an omission.

## Cited for existence, with no number taken

A second and milder category, introduced with chapter 14, Kinetics and
Mass Transfer. These are sources whose abstracts are not
exposed by any interface reachable from here — several are pre-2000 Elsevier and
ACS papers that predate structured abstracts in the aggregators. The book cites
them for what their titles establish (that a measurement was made, of what, by
what method) and quotes no value from any of them. Nothing in the text depends
on their contents, so none of these is a correctness risk in the way the table
above is. They are listed because reading them would let the chapter say more
than it currently does.

| Citation key | What the chapter would gain |
|----|----|
| `geist1999kinetics` | Measured rate constants for rare earth extraction into D2EHPA, and which step controls. |
| `cossy1988oxygen` | Water-exchange rate constants across the Ln(III) aqua ions, and how much of the series ¹⁷O NMR could actually reach. |
| `gabelman1999hollow` | Mass-transfer correlations for hollow-fibre contactors; currently cited only as the standard review. |
| `tian2010kinetics` | Rate law and activation energy for ammonium sulfate leaching of weathered-crust ore. |
| `he2016kinetics` | The same for column leaching, including the aluminium co-extraction behaviour. |
