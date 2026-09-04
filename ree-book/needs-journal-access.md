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
| 08 Coacervates and aqueous two-phase systems | `sui2023kinetic` | Crystallization kinetic parameters. |
| 11 Biological and biomimetic separations | `zhou2018leaching` | Bioleaching recovery figures. |
| 11 Biological and biomimetic separations | `zhang2018bioleaching` | Bioleaching recovery figures. |
| 11 Biological and biomimetic separations | `deng2025application` | Application-scale claims. |
| 11 Biological and biomimetic separations | `kore2024application` | Application-scale claims. |
| 14 High-throughput and computational screening | `an2024agile` | Synthesis details of the automated platform. |
| 16 Machine learning in rare earth separations | `zhang2026predicting` | Reported model performance. |
| 16 Machine learning in rare earth separations | `liu2026machine` | Reported model performance. |

## A gap, not a flag

Chapter 05, Hydrometallurgical leaching, states no overall rare earth recovery figure
for any leaching route, anywhere in the chapter. That is deliberate: no source
consulted for this book gives one that survives the check, and inventing a
plausible range would be exactly the failure mode the whole project is built to
avoid. Restoring a number here needs journal access to the primary
process-metallurgy literature. Until then the absence is the honest answer, and
the chapter says so rather than leaving a reader to assume an omission.
