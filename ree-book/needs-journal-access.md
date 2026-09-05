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
not redistributable and must never be committed. Files are named by citation key
(`huang2002rare.pdf`) inside `tier-2/`, `tier-3/` and `tier-4/` subdirectories
matching the tiers of issue #1. Every file's title was checked against the
bibliography entry before it was read, so a PDF named for a key is that key's
paper. Issue #1 lists every entry in this file with its DOI and what
specifically to look for, in a suggested retrieval order.

## Resolved

**Tier 1 (1 source).** `ding2023separation` — retrieved and read. The claim was
**wrong**: the paper's separation factor of 125 is dysprosium over praseodymium
*and* neodymium combined, not Dy/Nd, and it is a batch transfer ratio rather
than an equilibrium β. Corrected in ch04, ch09, ch12 and the provenance
appendix; see `RELEASE-PLAN.md`.

**Tier 2 (15 sources).** All retrieved and read. **Every flagged number was
confirmed exactly as the book states it** — 9.55 at.% N and 128.98 F/g and
23.66 mg/g La; β = 15.34 / 14.70 / 10.78 for Eu/Yb, Eu/Tm, Eu/La; 19.2 g/kg
resin loading at 20 % purity against 3 %; 8.4 mg Th/g carbon; 165,000 ppm TDS
and the pH 5-6 optimum and 65 % loss at pH 2 and the ~70 °C improvement; >40×
and >4× for the DGA COF; >2000 mg/kg REE in phosphogypsum; ~100 % recovery on
O-doped MoS₂; ~140 / 72 / 58 for Tb/La, Tb/Yb, Tb/Nd; ~400 An/Ln on the graphene
oxide membrane; the three-level transitions and periodicity and all sixteen
elements; 2.6× recovery and ~80 % less leaching agent and ~70 % fewer impurities;
95 % recovery on 5,000 t and 95 % ammonia reduction; 98.2 % and 96.2 % for the
mechanochemical yttrium route.

Reading them nonetheless changed the book in four places, because the full texts
carry things no abstract did:

- **`behera2025supramolecular`** reports a near-pair the abstract omits.
  **Tb/Eu is ~3**, against ~140 for Tb/La. The book had said no near-neighbour
  figure was given; it now gives this one, which reshapes the claim.
- **`wang2025industrial`** contains the technoeconomic numbers ch21 said were
  unobtainable, and they cut against the abstract's framing: US$7,078 per tonne
  REO for electrokinetic mining against US$6,214 conventional — 14 % *more*
  expensive — reversed only by US$16,477/t of remediation cost the conventional
  route does not internalise.
- **`zhao2022selectively`** gives the size of a selectivity the book had only
  named: 19.66 mg/g La against 12.25 Fe in the quaternary batch, and 450 s
  against 90 s to breakthrough in flow.
- **`virolainen2019recovering`** gives the calcium loadings that explain the
  resin comparison: 14.7 g Ca/kg on the chelating resin against 67.0 on the
  strong cation exchanger.

Tier 3 and Tier 4 PDFs have been retrieved and are in `fulltexts/`; they have
not yet been read against their claims.

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
| 13 Membranes, MOFs and emerging | `bao2025mxene` | 892.8 mg/g Eu(III) and 649.2 mg/g Ho(III) at pH 2.0, and 99.1 % Eu removal by the PES-supported membrane at pH 5.0. |
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
