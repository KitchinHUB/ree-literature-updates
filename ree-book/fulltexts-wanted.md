# Full texts still to collect

Generated 2026-09-06 by `tools/fulltext_inventory.py`. Regenerate it rather than
editing it by hand — it is a report, not a record.

## What this is

The book's rule is that a citation which resolves is not thereby correct:
the cited work has to actually contain the claim, and checking that means
reading it. This is the list of cited sources with no PDF in `fulltexts/`,
batched fifty at a time so they can be collected in sittings.

| | |
|---|---:|
| Entries the book cites | 656 |
| Full text on hand | 183 |
| **Still wanted** | **473** |
| — with a DOI to fetch | 452 |
| — no DOI; see the last section | 21 |

The 99 uncited entries in `references.bib` are out of scope — nothing in
the book rests on them. `orphan-references.md` lists those.

## How to use it

Work a batch at a time, in order. **Save each PDF as `<key>.pdf`**, the key
in the second column exactly as written, anywhere under `fulltexts/`. That
name is what lets a verification pass find the paper without a lookup table,
and it is what the next run of this report reads to decide the source is no
longer wanted.

Every batch ends with a plain block of DOI links and no markup, for pasting
into a downloader in one go.

## How the batches are ordered

1. **⚑ first.** Sources carrying a claim that `needs-journal-access.md`
   records as unverified, or that a chapter states outright it cannot
   source. Reading one of these changes the text.
2. **Then by how often the book cites the source**, most first. A source the
   book leans on in twenty places is worth more than one cited once.
3. Then alphabetically, so the order is stable between runs.

Batch 1 is therefore the highest-value fifty and the last batches are the
long tail of single citations. If the effort stops partway, it stops in the
right place.

**Cites** is how many times the book cites the source; **Ch** is which
chapters do.

## Batch 1 of 10

| # | Key | Cites | Ch | Source | DOI |
|---:|---|---:|---|---|---|
| 1 | `an2024agile` | 8 | 16 | ⚑ An 2024 — *Agile synthesis and automated, high-throughput evaluation of diglyc…* | [10.1039/D4GC01146E](https://doi.org/10.1039/D4GC01146E) |
| 2 | `augustine2026coupling` | 6 | 16,18 | ⚑ Augustine 2026 — *Coupling High-Throughput Density Functional Theory, Automated Exper…* | [10.1021/jacs.6c04301](https://doi.org/10.1021/jacs.6c04301) |
| 3 | `nichols2011mechanistic` | 5 | 9,15 | ⚑ Nichols 2011 — *Toward Mechanistic Understanding of Nuclear Reprocessing Chemistrie…* | [10.1021/ja206020u](https://doi.org/10.1021/ja206020u) |
| 4 | `bao2025mxene` | 4 | 4,13 | ⚑ Bao 2025 — *Functionalized 2D multilayered MXene for selective and continuous r…* | [10.1016/j.jhazmat.2025.137277](https://doi.org/10.1016/j.jhazmat.2025.137277) |
| 5 | `yang2022pilot` | 4 | 4,9 | ⚑ Yang 2022 — *Pilot-Scale Microfluidic Solvent Extraction of High-Value Metals* | [10.1016/j.mineng.2022.107536](https://doi.org/10.1016/j.mineng.2022.107536) |
| 6 | `duchanois2023prospects` | 2 | 21 | ⚑ DuChanois 2023 — *Prospects of metal recovery from wastewater and brine* | [10.1038/s44221-022-00006-z](https://doi.org/10.1038/s44221-022-00006-z) |
| 7 | `elmaangar2020microfluidic` | 2 | 9 | ⚑ El Maangar 2020 — *A microfluidic study of synergic liquid--liquid extraction of rare…* | [10.1039/c9cp06569e](https://doi.org/10.1039/c9cp06569e) |
| 8 | `he2024intensifying` | 2 | 9 | ⚑ He 2024 — *Intensifying the Extraction of Rare Earth Elements by a Mini-Channe…* | [10.1016/j.seppur.2023.125930](https://doi.org/10.1016/j.seppur.2023.125930) |
| 9 | `leite2025creation` | 2 | 16 | ⚑ da Silva Garcia Leite 2025 — *Creation of the Separation Archive for Elements (SAFE) Database* | [10.1080/07366299.2025.2564381](https://doi.org/10.1080/07366299.2025.2564381) |
| 10 | `yu2026progress` | 2 | 3 | ⚑ Yu 2026 — *Progress in pulsed extraction column for spent nuclear fuel reproce…* | [10.1016/j.energy.2026.141605](https://doi.org/10.1016/j.energy.2026.141605) |
| 11 | `deng2025application` | 1 | 11 | ⚑ Deng 2025 — *Application of Ionic Liquids and Deep Eutectic Solvents as Green So…* | [10.1007/s40831-025-01289-8](https://doi.org/10.1007/s40831-025-01289-8) |
| 12 | `tian2020rare` | 1 | 20 | ⚑ Tian 2020 — *Rare Earth Elements Occurrence and Economical Recovery Strategy fro…* | [10.1021/acssuschemeng.0c04971](https://doi.org/10.1021/acssuschemeng.0c04971) |
| 13 | `mattocks2023enhanced` | 20 | 4,8,9,11 | Mattocks 2023 — *Enhanced rare-earth separation with a metal-sensitive lanmodulin di…* | [10.1038/s41586-023-05945-5](https://doi.org/10.1038/s41586-023-05945-5) |
| 14 | `larrinaga2024modulating` | 12 | 8,11 | Larrinaga 2024 — *Modulating metal-centered dimerization of a lanthanide chaperone pr…* | [10.1073/pnas.2410926121](https://doi.org/10.1073/pnas.2410926121) |
| 15 | `cotruvo2018lanmodulin` | 11 | 4,8,11 | Cotruvo 2018 — *Lanmodulin: A Highly Selective Lanthanide-Binding Protein from a La…* | [10.1021/jacs.8b09842](https://doi.org/10.1021/jacs.8b09842) |
| 16 | `usgs2026mineral` | 10 | 1,20,23,24 | U.S. Geological Survey 2026 — *Mineral Commodity Summaries 2026* | [10.3133/mcs2026](https://doi.org/10.3133/mcs2026) |
| 17 | `deblonde2020selective` | 9 | 8,11 | Deblonde 2020 — *Selective and Efficient Biomacromolecular Extraction of Rare-Earth…* | [10.1021/acs.inorgchem.0c01303](https://doi.org/10.1021/acs.inorgchem.0c01303) |
| 18 | `hu2024rationally` | 9 | 4,9,13 | Hu 2024 — *Rationally Designed Nanotrap Structures for Efficient Separation of…* | [10.1038/s41467-024-45810-1](https://doi.org/10.1038/s41467-024-45810-1) |
| 19 | `mackey2024estimates` | 9 | 21 | Mackey 2024 — *Estimates of lithium mass yields from produced water sourced from t…* | [10.1038/s41598-024-58887-x](https://doi.org/10.1038/s41598-024-58887-x) |
| 20 | `shi2022column` | 9 | 5 | Shi 2022 — *Column leaching of ion adsorption rare earth ore at low ammonium co…* | [10.1016/j.jmrt.2022.05.199](https://doi.org/10.1016/j.jmrt.2022.05.199) |
| 21 | `sinclair2017rare` | 9 | 4,5,13 | Sinclair 2017 — *Rare earth element extraction from pretreated bastnäsite in supercr…* | [10.1016/j.supflu.2017.01.005](https://doi.org/10.1016/j.supflu.2017.01.005) |
| 22 | `vandenbogaert2015photochemical` | 9 | 10,12 | Van den Bogaert 2015 — *Photochemical recycling of europium from Eu/Y mixtures in red lamp…* | [10.1039/c4gc02140a](https://doi.org/10.1039/c4gc02140a) |
| 23 | `dong2021bridging` | 8 | 4,11,20 | Dong 2021 — *Bridging Hydrometallurgy and Biochemistry: A Protein-Based Process…* | [10.1021/acscentsci.1c00724](https://doi.org/10.1021/acscentsci.1c00724) |
| 24 | `xue2025onestep` | 8 | 4,7 | Xue 2025 — *Study on the Process and Mechanism of One-Step Carbochlorination-Wa…* | [10.1021/acs.iecr.5c02156](https://doi.org/10.1021/acs.iecr.5c02156) |
| 25 | `xue2026clean` | 8 | 7 | Xue 2026 — *A clean and efficient one-step process for rare earth extraction: C…* | [10.1016/j.ces.2025.122244](https://doi.org/10.1016/j.ces.2025.122244) |
| 26 | `choi2026near` | 7 | 8,11 | Choi 2026 — *Near-Adjacent Heavy Lanthanide Separation and Sensing Using Dimeriz…* | [10.1021/jacs.6c08525](https://doi.org/10.1021/jacs.6c08525) |
| 27 | `gupta2025accelerating` | 7 | 14,18 | Gupta 2026 — *Toward accelerating rare-earth metal extraction using equivariant n…* | [10.1039/d5dd00286a](https://doi.org/10.1039/d5dd00286a) |
| 28 | `rydberg2004solvent` | 7 | 3 | 2004 — *Solvent Extraction Principles and Practice, Revised and Expanded* | [10.1201/9780203021460](https://doi.org/10.1201/9780203021460) |
| 29 | `smith2024critical` | 7 | 21 | Smith 2024 — *Critical mineral source potential from oil \& gas produced waters i…* | [10.1016/j.scitotenv.2024.172573](https://doi.org/10.1016/j.scitotenv.2024.172573) |
| 30 | `zhang2018rare` | 7 | 4,10 | Zhang 2018 — *Rare earth elements recovery using staged precipitation from a leac…* | [10.1016/j.coal.2018.06.008](https://doi.org/10.1016/j.coal.2018.06.008) |
| 31 | `brisson2015bioleaching` | 6 | 5 | Brisson 2015 — *Bioleaching of rare earth elements from monazite sand* | [10.1002/bit.25823](https://doi.org/10.1002/bit.25823) |
| 32 | `browning2017life` | 6 | 23 | Browning 2016 — *Life Cycle Assessment of Rare Earth Production from Monazite* | [10.1007/978-3-319-48768-7_12](https://doi.org/10.1007/978-3-319-48768-7_12) |
| 33 | `chelgani2015rare` | 6 | 2,5 | Chelgani 2015 — *A review of rare earth minerals flotation: Monazite and xenotime* | [10.1016/j.ijmst.2015.09.002](https://doi.org/10.1016/j.ijmst.2015.09.002) |
| 34 | `jordens2013beneficiation` | 6 | 2,5 | Jordens 2013 — *A review of the beneficiation of rare earth element bearing minerals* | [10.1016/j.mineng.2012.10.017](https://doi.org/10.1016/j.mineng.2012.10.017) |
| 35 | `kaczorowska2023latest` | 6 | 13 | Kaczorowska 2023 — *The Latest Achievements of Liquid Membranes for Rare Earth Elements…* | [10.3390/membranes13100839](https://doi.org/10.3390/membranes13100839) |
| 36 | `laskar2025conversion` | 6 | 10 | Laskar 2025 — *Conversion of Sodium-Rare Earth Double Sulfate Salts Prepared from…* | [10.1007/s40831-025-01173-5](https://doi.org/10.1007/s40831-025-01173-5) |
| 37 | `liu2019selective` | 6 | 10 | Silva 2019 — *Selective Precipitation of Rare Earth from Non-Purified and Purifie…* | [10.1016/j.mineng.2019.02.028](https://doi.org/10.1016/j.mineng.2019.02.028) |
| 38 | `nawab2022parametric` | 6 | 4,10 | Nawab 2022 — *Parametric study and speciation analysis of rare earth precipitatio…* | [10.1016/j.mineng.2021.107352](https://doi.org/10.1016/j.mineng.2021.107352) |
| 39 | `zahariev2024prediction` | 6 | 18,25 | Zahariev 2024 — *Prediction of stability constants of metal–ligand complexes by mach…* | [10.1063/5.0176000](https://doi.org/10.1063/5.0176000) |
| 40 | `brunetti2000vaporization` | 5 | 7 | Brunetti 2000 — *Vaporization Studies of Lanthanum Trichloride, Tribromide, and Trii…* | [10.1021/je9902037](https://doi.org/10.1021/je9902037) |
| 41 | `chen2022driving` | 5 | 8 | Chen 2022 — *Driving force and pathway in polyelectrolyte complex coacervation* | [10.1073/pnas.2209975119](https://doi.org/10.1073/pnas.2209975119) |
| 42 | `chen2025process` | 5 | 7 | Ma 2025 — *Process design of molten salt distillation separation of ZrCl4 and…* | [10.1016/j.seppur.2025.132620](https://doi.org/10.1016/j.seppur.2025.132620) |
| 43 | `feng2026selective` | 5 | 4,13 | Feng 2026 — *Selective Separation of Rare Earth Elements by Nanofiltration Membr…* | [10.3390/membranes16080268](https://doi.org/10.3390/membranes16080268) |
| 44 | `gupta2004extractive` | 5 | 5,10 | Gupta 2004 — *Extractive Metallurgy of Rare Earths* | [10.1201/9780203413029](https://doi.org/10.1201/9780203413029) |
| 45 | `liu2022advancing` | 5 | 16,18,19 | Liu 2022 — *Advancing Rare-Earth Separation by Machine Learning* | [10.1021/jacsau.2c00122](https://doi.org/10.1021/jacsau.2c00122) |
| 46 | `pomiro2021panoramic` | 5 | 7 | Pomiro 2021 — *A Panoramic Overview of Chlorination and Carbochlorination of Light…* | [10.1007/s42461-021-00490-z](https://doi.org/10.1007/s42461-021-00490-z) |
| 47 | `rasoulnia2020critical` | 5 | 5,23 | Rasoulnia 2020 — *A critical review of bioleaching of rare earth elements: The mechan…* | [10.1080/10643389.2020.1727718](https://doi.org/10.1080/10643389.2020.1727718) |
| 48 | `seifert2005melting` | 5 | 7 | Seifert 2005 — *Melting points of lanthanide trichlorides* | [10.1007/s10973-005-0936-7](https://doi.org/10.1007/s10973-005-0936-7) |
| 49 | `smith2019selective` | 5 | 15 | Smith 2019 — *Selective Recovery of Rare Earth Elements from Coal Fly Ash Leachat…* | [10.1021/acs.est.9b00539](https://doi.org/10.1021/acs.est.9b00539) |
| 50 | `summers2024importance` | 5 | 16,18 | Summers 2024 — *On the Importance of Configuration Search to the Predictivity of La…* | [10.1021/jacsau.4c00770](https://doi.org/10.1021/jacsau.4c00770) |

```text
https://doi.org/10.1039/D4GC01146E
https://doi.org/10.1021/jacs.6c04301
https://doi.org/10.1021/ja206020u
https://doi.org/10.1016/j.jhazmat.2025.137277
https://doi.org/10.1016/j.mineng.2022.107536
https://doi.org/10.1038/s44221-022-00006-z
https://doi.org/10.1039/c9cp06569e
https://doi.org/10.1016/j.seppur.2023.125930
https://doi.org/10.1080/07366299.2025.2564381
https://doi.org/10.1016/j.energy.2026.141605
https://doi.org/10.1007/s40831-025-01289-8
https://doi.org/10.1021/acssuschemeng.0c04971
https://doi.org/10.1038/s41586-023-05945-5
https://doi.org/10.1073/pnas.2410926121
https://doi.org/10.1021/jacs.8b09842
https://doi.org/10.3133/mcs2026
https://doi.org/10.1021/acs.inorgchem.0c01303
https://doi.org/10.1038/s41467-024-45810-1
https://doi.org/10.1038/s41598-024-58887-x
https://doi.org/10.1016/j.jmrt.2022.05.199
https://doi.org/10.1016/j.supflu.2017.01.005
https://doi.org/10.1039/c4gc02140a
https://doi.org/10.1021/acscentsci.1c00724
https://doi.org/10.1021/acs.iecr.5c02156
https://doi.org/10.1016/j.ces.2025.122244
https://doi.org/10.1021/jacs.6c08525
https://doi.org/10.1039/d5dd00286a
https://doi.org/10.1201/9780203021460
https://doi.org/10.1016/j.scitotenv.2024.172573
https://doi.org/10.1016/j.coal.2018.06.008
https://doi.org/10.1002/bit.25823
https://doi.org/10.1007/978-3-319-48768-7_12
https://doi.org/10.1016/j.ijmst.2015.09.002
https://doi.org/10.1016/j.mineng.2012.10.017
https://doi.org/10.3390/membranes13100839
https://doi.org/10.1007/s40831-025-01173-5
https://doi.org/10.1016/j.mineng.2019.02.028
https://doi.org/10.1016/j.mineng.2021.107352
https://doi.org/10.1063/5.0176000
https://doi.org/10.1021/je9902037
https://doi.org/10.1073/pnas.2209975119
https://doi.org/10.1016/j.seppur.2025.132620
https://doi.org/10.3390/membranes16080268
https://doi.org/10.1201/9780203413029
https://doi.org/10.1021/jacsau.2c00122
https://doi.org/10.1007/s42461-021-00490-z
https://doi.org/10.1080/10643389.2020.1727718
https://doi.org/10.1007/s10973-005-0936-7
https://doi.org/10.1021/acs.est.9b00539
https://doi.org/10.1021/jacsau.4c00770
```

## Batch 2 of 10

| # | Key | Cites | Ch | Source | DOI |
|---:|---|---:|---|---|---|
| 51 | `tan2016innovative` | 5 | 20 | Tan 2016 — *Innovative Application of Mechanical Activation for Rare Earth Elem…* | [10.1038/srep19961](https://doi.org/10.1038/srep19961) |
| 52 | `wenzlick2020techno` | 5 | 21,23 | Wenzlick 2020 — *Techno-economic analysis of converting oil \& gas produced water in…* | [10.1016/j.desal.2020.114381](https://doi.org/10.1016/j.desal.2020.114381) |
| 53 | `xu2025sustainable` | 5 | 7,13 | Xu 2025 — *Sustainable separation of rare earth elements from wastes* | [10.1073/pnas.2507819122](https://doi.org/10.1073/pnas.2507819122) |
| 54 | `yang2017ree` | 5 | 7,20 | Yang 2016 — *REE recovery from end-of-life NdFeB permanent magnet scrap: A criti…* | [10.1007/s40831-016-0090-4](https://doi.org/10.1007/s40831-016-0090-4) |
| 55 | `azimi2025technoeconomic` | 4 | 4,13,23 | Azimi 2025 — *Technoeconomic Analysis of the Supercritical Fluid Extraction Proce…* | [10.1021/acs.iecr.5c00324](https://doi.org/10.1021/acs.iecr.5c00324) |
| 56 | `bashiri2022rare` | 4 | 13 | Bashiri 2022 — *Rare Earth Elements Recovery Using Selective Membranes via Extracti…* | [10.3390/membranes12010080](https://doi.org/10.3390/membranes12010080) |
| 57 | `borai2016modified` | 4 | 5 | Borai 2016 — *Modified acidic leaching for selective separation of thorium, phosp…* | [10.1016/j.minpro.2016.02.003](https://doi.org/10.1016/j.minpro.2016.02.003) |
| 58 | `fang2017electrokinetic` | 4 | 15 | Fang 2017 — *Electro-kinetic Separation of Rare Earth Elements Using a Redox-Act…* | [10.1002/anie.201706894](https://doi.org/10.1002/anie.201706894) |
| 59 | `gavira2010carbochlorination` | 4 | 7 | Gaviría 2010 — *Carbochlorination of yttrium oxide* | [10.1016/j.tca.2010.06.009](https://doi.org/10.1016/j.tca.2010.06.009) |
| 60 | `good2024scalable` | 4 | 4,11 | Good 2023 — *Scalable and Consolidated Microbial Platform for Rare Earth Element…* | [10.1021/acs.est.3c06775](https://doi.org/10.1021/acs.est.3c06775) |
| 61 | `gupta1984extractive` | 4 | 7 | Gupta 1984 — *Extractive metallurgy of niobium, tantalum, and vanadium* | [10.1179/imr.1984.29.1.405](https://doi.org/10.1179/imr.1984.29.1.405) |
| 62 | `gupta2003chemical` | 4 | 7 | Gupta 2003 — *Chemical Metallurgy: Principles and Practice* | [10.1002/3527602003](https://doi.org/10.1002/3527602003) |
| 63 | `hatanaka2017rationally` | 4 | 10,11 | Hatanaka 2017 — *Rationally Designed Mineralization for Selective Recovery of the Ra…* | [10.1038/ncomms15670](https://doi.org/10.1038/ncomms15670) |
| 64 | `jones2025macrocyclic` | 4 | 10,13 | Jones 2025 — *Macrocyclic Chelators for Aqueous Lanthanide Separations via Precip…* | [10.1021/jacs.5c04150](https://doi.org/10.1021/jacs.5c04150) |
| 65 | `knierim2024evaluation` | 4 | 21 | Knierim 2024 — *Evaluation of the lithium resource in the Smackover Formation brine…* | [10.1126/sciadv.adp8149](https://doi.org/10.1126/sciadv.adp8149) |
| 66 | `mohamadsobri2025enhancing` | 4 | 4,6 | Mohamad Sobri 2025 — *ENHANCING RARE EARTH ELEMENTS STABILITY IN ION ADSORPTION CLAYS DUR…* | [10.11113/jurnalteknologi.v88.23169](https://doi.org/10.11113/jurnalteknologi.v88.23169) |
| 67 | `nash2012kinetics` | 4 | 15 | Nash 2012 — *The kinetics of lanthanide complexation by EDTA and DTPA in lactate…* | [10.1039/c2dt31851b](https://doi.org/10.1039/c2dt31851b) |
| 68 | `neves2022liquid` | 4 | 8 | Neves 2022 — *Liquid-liquid extraction of rare earth elements using systems that…* | [10.1016/j.seppur.2021.120064](https://doi.org/10.1016/j.seppur.2021.120064) |
| 69 | `obrien2024simplified` | 4 | 23 | O’Brien 2024 — *A Simplified Rare Earth Element Mining Project Cost Estimator - A N…* | [10.1007/s13563-024-00467-6](https://doi.org/10.1007/s13563-024-00467-6) |
| 70 | `oztug2024overview` | 4 | 13,19 | Peng 2024 — *Overview of Functionalized Porous Materials for Rare-Earth Element…* | [10.3390/molecules29122824](https://doi.org/10.3390/molecules29122824) |
| 71 | `peng2024extreme` | 4 | 21 | Peng 2024 — *Extreme Li-Mg selectivity via precise ion size differentiation of p…* | [10.1038/s41467-024-46887-4](https://doi.org/10.1038/s41467-024-46887-4) |
| 72 | `pomiro2014study` | 4 | 7 | Pomiro 2014 — *Study of the Reaction Stages and Kinetics of the Europium Oxide Car…* | [10.1007/s11663-014-0196-7](https://doi.org/10.1007/s11663-014-0196-7) |
| 73 | `prodius2019sustainable` | 4 | 20 | Prodius 2019 — *Sustainable Urban Mining of Critical Elements from Magnet and Elect…* | [10.1021/acssuschemeng.9b05741](https://doi.org/10.1021/acssuschemeng.9b05741) |
| 74 | `xu2015production` | 4 | 7 | Xu 2015 — *Production of nuclear grade zirconium: A review* | [10.1016/j.jnucmat.2015.07.010](https://doi.org/10.1016/j.jnucmat.2015.07.010) |
| 75 | `xue2025carbochlorination` | 4 | 7 | Xue 2025 — *Carbochlorination extraction of rare earth Elements: Thermodynamics…* | [10.1016/j.mineng.2025.109623](https://doi.org/10.1016/j.mineng.2025.109623) |
| 76 | `yao2025computationally` | 4 | 8,11 | Sajeevan 2025 — *Computationally derived structural insights into Rare Earth selecti…* | [10.1016/j.csbj.2025.02.005](https://doi.org/10.1016/j.csbj.2025.02.005) |
| 77 | `yin2017rare` | 4 | 10 | Yin 2017 — *Rare Earth Separations by Selective Borate Crystallization* | [10.1038/ncomms14438](https://doi.org/10.1038/ncomms14438) |
| 78 | `yin2025selective` | 4 | 4,10 | Yin 2025 — *Selective Crystallization Separation Driven by Structural Divergenc…* | [10.1021/acs.inorgchem.5c00183](https://doi.org/10.1021/acs.inorgchem.5c00183) |
| 79 | `zaimes2015environmental` | 4 | 23 | Zaimes 2015 — *Environmental Life Cycle Perspective on Rare Earth Oxide Production* | [10.1021/sc500573b](https://doi.org/10.1021/sc500573b) |
| 80 | `zhang2026augmenting` | 4 | 18 | Zhang 2026 — *Augmenting Large Language Models for Automated Discovery of F-Eleme…* | [10.1021/jacs.5c19738](https://doi.org/10.1021/jacs.5c19738) |
| 81 | `abbasalizadeh2017electrochemical` | 3 | 10,12,20 | Abbasalizadeh 2017 — *Electrochemical Extraction of Rare Earth Metals in Molten Fluorides…* | [10.1007/s40831-017-0120-x](https://doi.org/10.1007/s40831-017-0120-x) |
| 82 | `anderson2015investigation` | 3 | 7 | Anderson 2015 — *Investigation of the Carbochlorination Process for Conversion of Ce…* | [10.1007/s40831-015-0023-7](https://doi.org/10.1007/s40831-015-0023-7) |
| 83 | `bediako2022facile` | 3 | 8 | Bediako 2022 — *Facile Processing of Polyelectrolyte Complexes for Immobilization o…* | [10.1021/acsapm.1c01634](https://doi.org/10.1021/acsapm.1c01634) |
| 84 | `blondes2020utica` | 3 | 21 | Blondes 2020 — *Utica Shale Play Oil and Gas Brines: Geochemistry and Factors Influ…* | [10.1021/acs.est.0c02461](https://doi.org/10.1021/acs.est.0c02461) |
| 85 | `borst2020adsorption` | 3 | 6 | Borst 2020 — *Adsorption of rare earth elements in regolith-hosted clay deposits* | [10.1038/s41467-020-17801-5](https://doi.org/10.1038/s41467-020-17801-5) |
| 86 | `chen2018overview` | 3 | 13 | Chen 2018 — *An Overview on Membrane Strategies for Rare Earths Extraction and S…* | [10.1016/j.seppur.2017.12.053](https://doi.org/10.1016/j.seppur.2017.12.053) |
| 87 | `chen2025selective` | 3 | 10 | Chen 2025 — *Selective Crystallization Strategies for Lanthanide--Lanthanide and…* | [10.1039/D5CC03636D](https://doi.org/10.1039/D5CC03636D) |
| 88 | `cook2019structural` | 3 | 11 | Cook 2018 — *Structural Basis for Rare Earth Element Recognition by Methylobacte…* | [10.1021/acs.biochem.8b01019](https://doi.org/10.1021/acs.biochem.8b01019) |
| 89 | `elizalde2019oxidative` | 3 | 10 | McNeice 2019 — *Oxidative Precipitation of Cerium in Acidic Chloride Solutions: Par…* | [10.1016/j.hydromet.2018.12.018](https://doi.org/10.1016/j.hydromet.2018.12.018) |
| 90 | `forsberg2024separation` | 3 | 10 | Forsberg 2024 — *Separation of Rare Earth Elements by Crystallization* | [10.1002/9781119515005.ch6](https://doi.org/10.1002/9781119515005.ch6) |
| 91 | `gaballah1999chlorination` | 3 | 7 | Kanari 1999 — *Chlorination and carbochlorination of magnesium oxide* | [10.1007/s11663-999-0070-1](https://doi.org/10.1007/s11663-999-0070-1) |
| 92 | `he2025stepwise` | 3 | 5 | He 2025 — *Stepwise leaching rare earth from weathered crust elution-deposited…* | [10.1007/s11356-025-36598-8](https://doi.org/10.1007/s11356-025-36598-8) |
| 93 | `hua2014selective` | 3 | 7 | Hua 2014 — *Selective extraction of rare earth elements from NdFeB scrap by mol…* | [10.1021/sc5004456](https://doi.org/10.1021/sc5004456) |
| 94 | `kim2020characteristics` | 3 | 10 | Han 2020 — *Characteristics of Precipitation of Rare Earth Elements with Variou…* | [10.3390/min10020178](https://doi.org/10.3390/min10020178) |
| 95 | `kosemutlu2018application` | 3 | 4,13 | Kose Mutlu 2018 — *Application of Nanofiltration for Rare Earth Elements Recovery from…* | [10.1016/j.cej.2018.05.080](https://doi.org/10.1016/j.cej.2018.05.080) |
| 96 | `kumar2022separation` | 3 | 8 | Li 2022 — *Separation of Rare Earths and Transition Metals Using Ionic-Liquid-…* | [10.1021/acs.iecr.1c04470](https://doi.org/10.1021/acs.iecr.1c04470) |
| 97 | `larochelle2021fundamental` | 3 | 23 | Larochelle 2021 — *A Fundamental Economic Assessment of Recovering Rare Earth Elements…* | [10.3390/min11111298](https://doi.org/10.3390/min11111298) |
| 98 | `li2018supramolecular` | 3 | 10,13 | Li 2018 — *A Supramolecular Lanthanide Separation Approach Based on Multivalen…* | [10.1038/s41467-018-02940-7](https://doi.org/10.1038/s41467-018-02940-7) |
| 99 | `liu2017enrichment` | 3 | 5,6 | Liu 2017 — *Enrichment of Low Concentration Rare Earths from Leach Solutions of…* | [10.1021/acssuschemeng.7b01682](https://doi.org/10.1021/acssuschemeng.7b01682) |
| 100 | `liu2022one` | 3 | 4,8 | Liu 2022 — *A one-pot process based on P44414Cl-HCl aqueous biphasic system for…* | [10.1016/j.cclet.2021.07.026](https://doi.org/10.1016/j.cclet.2021.07.026) |

```text
https://doi.org/10.1038/srep19961
https://doi.org/10.1016/j.desal.2020.114381
https://doi.org/10.1073/pnas.2507819122
https://doi.org/10.1007/s40831-016-0090-4
https://doi.org/10.1021/acs.iecr.5c00324
https://doi.org/10.3390/membranes12010080
https://doi.org/10.1016/j.minpro.2016.02.003
https://doi.org/10.1002/anie.201706894
https://doi.org/10.1016/j.tca.2010.06.009
https://doi.org/10.1021/acs.est.3c06775
https://doi.org/10.1179/imr.1984.29.1.405
https://doi.org/10.1002/3527602003
https://doi.org/10.1038/ncomms15670
https://doi.org/10.1021/jacs.5c04150
https://doi.org/10.1126/sciadv.adp8149
https://doi.org/10.11113/jurnalteknologi.v88.23169
https://doi.org/10.1039/c2dt31851b
https://doi.org/10.1016/j.seppur.2021.120064
https://doi.org/10.1007/s13563-024-00467-6
https://doi.org/10.3390/molecules29122824
https://doi.org/10.1038/s41467-024-46887-4
https://doi.org/10.1007/s11663-014-0196-7
https://doi.org/10.1021/acssuschemeng.9b05741
https://doi.org/10.1016/j.jnucmat.2015.07.010
https://doi.org/10.1016/j.mineng.2025.109623
https://doi.org/10.1016/j.csbj.2025.02.005
https://doi.org/10.1038/ncomms14438
https://doi.org/10.1021/acs.inorgchem.5c00183
https://doi.org/10.1021/sc500573b
https://doi.org/10.1021/jacs.5c19738
https://doi.org/10.1007/s40831-017-0120-x
https://doi.org/10.1007/s40831-015-0023-7
https://doi.org/10.1021/acsapm.1c01634
https://doi.org/10.1021/acs.est.0c02461
https://doi.org/10.1038/s41467-020-17801-5
https://doi.org/10.1016/j.seppur.2017.12.053
https://doi.org/10.1039/D5CC03636D
https://doi.org/10.1021/acs.biochem.8b01019
https://doi.org/10.1016/j.hydromet.2018.12.018
https://doi.org/10.1002/9781119515005.ch6
https://doi.org/10.1007/s11663-999-0070-1
https://doi.org/10.1007/s11356-025-36598-8
https://doi.org/10.1021/sc5004456
https://doi.org/10.3390/min10020178
https://doi.org/10.1016/j.cej.2018.05.080
https://doi.org/10.1021/acs.iecr.1c04470
https://doi.org/10.3390/min11111298
https://doi.org/10.1038/s41467-018-02940-7
https://doi.org/10.1021/acssuschemeng.7b01682
https://doi.org/10.1016/j.cclet.2021.07.026
```

## Batch 3 of 10

| # | Key | Cites | Ch | Source | DOI |
|---:|---|---:|---|---|---|
| 101 | `long2019kinetics` | 3 | 5 | Long 2020 — *Kinetics model for leaching of ion-adsorption type rare earth ores* | [10.1016/j.jre.2019.11.011](https://doi.org/10.1016/j.jre.2019.11.011) |
| 102 | `love2020reversible` | 3 | 8 | Love 2020 — *Reversible pH-Responsive Coacervate Formation in Lipid Vesicles Act…* | [10.1002/anie.201914893](https://doi.org/10.1002/anie.201914893) |
| 103 | `marcus1991thermodynamics` | 3 | 14,16 | Marcus 1991 — *Thermodynamics of solvation of ions. Part 5.---Gibbs free energy of…* | [10.1039/FT9918702995](https://doi.org/10.1039/FT9918702995) |
| 104 | `mccarty2019complete` | 3 | 8 | McCarty 2019 — *Complete Phase Diagram for Liquid-Liquid Phase Separation of Intrin…* | [10.1021/acs.jpclett.9b00099](https://doi.org/10.1021/acs.jpclett.9b00099) |
| 105 | `moyer2011overview` | 3 | 22 | Tachimori 2009 — *Overview of solvent extraction chemistry for reprocessing* | [10.1201/9781420059700-c1](https://doi.org/10.1201/9781420059700-c1) |
| 106 | `muratov2020qsar` | 3 | 18 | Muratov 2020 — *QSAR without borders* | [10.1039/d0cs00098a](https://doi.org/10.1039/d0cs00098a) |
| 107 | `nash2015chemistry` | 3 | 15 | Nash 2015 — *The Chemistry of TALSPEAK: A Review of the Science* | [10.1080/07366299.2014.985912](https://doi.org/10.1080/07366299.2014.985912) |
| 108 | `navarro2014life` | 3 | 23 | Navarro 2014 — *Life-Cycle Assessment of the Production of Rare-Earth Elements for…* | [10.3389/fenrg.2014.00045](https://doi.org/10.3389/fenrg.2014.00045) |
| 109 | `noack2015rare` | 3 | 21 | Noack 2015 — *Rare earth element geochemistry of outcrop and core samples from th…* | [10.1186/s12932-015-0022-4](https://doi.org/10.1186/s12932-015-0022-4) |
| 110 | `pan2024insights` | 3 | 5,6 | Pan 2025 — *Insights into selective leaching of rare earths from weathered crus…* | [10.1016/j.jre.2024.04.025](https://doi.org/10.1016/j.jre.2024.04.025) |
| 111 | `phan2018role` | 3 | 21 | Phan 2018 — *Role of water-rock interaction in the geochemical evolution of Marc…* | [10.1016/j.coal.2018.02.014](https://doi.org/10.1016/j.coal.2018.02.014) |
| 112 | `powell1956basic` | 3 | 4,10 | Powell 1956 — *Basic Principles Involved in the Macro-Separation of Adjacent Rare…* | [10.2172/4289324](https://doi.org/10.2172/4289324) |
| 113 | `safarzadeh2018insights` | 3 | 4,9 | Safarzadeh 2018 — *New insights into the separation of Nd from Pr in hydrochloric and…* | [10.1016/j.poly.2018.06.050](https://doi.org/10.1016/j.poly.2018.06.050) |
| 114 | `sposato2021towards` | 3 | 20 | Sposato 2021 — *Towards the Circular Economy of Rare Earth Elements: Lanthanum Leac…* | [10.3390/pr9081369](https://doi.org/10.3390/pr9081369) |
| 115 | `taggart2016trends` | 3 | 4,9,13 | Taggart 2016 — *Trends in the Rare Earth Element Content of U.S.-Based Coal Combust…* | [10.1021/acs.est.6b00085](https://doi.org/10.1021/acs.est.6b00085) |
| 116 | `uysal2022economic` | 3 | 23 | Uysal 2022 — *Economic Analysis of Rare Earth Element Processing Methods for Moun…* | [10.17159/2411-9717/1989/2022](https://doi.org/10.17159/2411-9717/1989/2022) |
| 117 | `wan2022lca` | 3 | 23 | Wan 2022 — *LCA-Based Carbon Footprint Accounting of Mixed Rare Earth Oxides Pr…* | [10.3390/pr10071354](https://doi.org/10.3390/pr10071354) |
| 118 | `wang2014polyelectrolyte` | 3 | 8 | Wang 2014 — *The Polyelectrolyte Complex/Coacervate Continuum* | [10.1021/ma500500q](https://doi.org/10.1021/ma500500q) |
| 119 | `wang2025quantification` | 3 | 8 | Rodriguez 2025 — *Quantification of redox thermodynamics shifts within coacervates* | [10.1073/pnas.2521526122](https://doi.org/10.1073/pnas.2521526122) |
| 120 | `wang2025rare` | 3 | 5 | Wang 2025 — *Rare Earth Element Extraction from Ionic Rare Earth Ores by Two Typ…* | [10.3390/ijms26051986](https://doi.org/10.3390/ijms26051986) |
| 121 | `warner2013impacts` | 3 | 21 | Warner 2013 — *Impacts of Shale Gas Wastewater Disposal on Water Quality in Wester…* | [10.1021/es402165b](https://doi.org/10.1021/es402165b) |
| 122 | `weshahy2022efficient` | 3 | 20 | Weshahy 2022 — *Efficient Recovery of Rare Earth Elements and Zinc from Spent Ni--M…* | [10.3390/nano12132305](https://doi.org/10.3390/nano12132305) |
| 123 | `xu1985theory` | 3 | 3,17 | Xu 1985 — *Theory of Countercurrent Extraction and Its Applications in Rare Ea…* | [10.1016/b978-0-12-767661-6.50109-0](https://doi.org/10.1016/b978-0-12-767661-6.50109-0) |
| 124 | `yin2024preparation` | 3 | 7 | Yang 2024 — *Study on Preparation of Crude ZrCl4 by Industrial Desiliconization…* | [10.1007/s11837-024-06756-3](https://doi.org/10.1007/s11837-024-06756-3) |
| 125 | `zapp2022environmental` | 3 | 23 | Zapp 2022 — *Environmental Impacts of Rare Earth Production* | [10.1557/s43577-022-00286-6](https://doi.org/10.1557/s43577-022-00286-6) |
| 126 | `ali2023mineral` | 2 | 19 | Ali 2023 — *Mineral Characterization Using Scanning Electron Microscopy (SEM):…* | [10.3390/app132312600](https://doi.org/10.3390/app132312600) |
| 127 | `alshameri2019understanding` | 2 | 6 | Alshameri 2019 — *Understanding the role of natural clay minerals as effective adsorb…* | [10.1016/j.hydromet.2019.02.016](https://doi.org/10.1016/j.hydromet.2019.02.016) |
| 128 | `ansari2006extraction` | 2 | 14 | Ansari 2006 — *Extraction of Actinides Using N,N,N',N'-tetraoctyl Diglycolamide (T…* | [10.1524/ract.2006.94.6.307](https://doi.org/10.1524/ract.2006.94.6.307) |
| 129 | `bashiri2024artificial` | 2 | 18 | Bashiri 2024 — *Artificial Intelligence Models for Efficiency Estimation of Adsorbe…* | [10.1021/acs.iecr.4c01935](https://doi.org/10.1021/acs.iecr.4c01935) |
| 130 | `binnemans2013recycling` | 2 | 20 | Binnemans 2013 — *Recycling of rare earths: A critical review* | [10.1016/j.jclepro.2012.12.037](https://doi.org/10.1016/j.jclepro.2012.12.037) |
| 131 | `binnemans2023ionic` | 2 | 8,11 | Binnemans 2023 — *Ionic Liquids and Deep-Eutectic Solvents in Extractive Metallurgy:…* | [10.1007/s40831-023-00681-6](https://doi.org/10.1007/s40831-023-00681-6) |
| 132 | `boronski2020rationally` | 2 | 10,13 | Prodius 2020 — *Rationally Designed Rare Earth Separation by Selective Oxalate Solu…* | [10.1039/d0cc02270e](https://doi.org/10.1039/d0cc02270e) |
| 133 | `braley2012alternatives` | 2 | 15 | Braley 2012 — *Alternatives to HDEHP and DTPA for Simplified TALSPEAK Separations* | [10.1021/ie200285r](https://doi.org/10.1021/ie200285r) |
| 134 | `chapman2012geochemical` | 2 | 21 | Chapman 2012 — *Geochemical and Strontium Isotope Characterization of Produced Wate…* | [10.1021/es204005g](https://doi.org/10.1021/es204005g) |
| 135 | `chen2019characterization` | 2 | 19 | Chen 2019 — *Characterization of the Interaction of Rare Earth Elements with P50…* | [10.1016/j.cej.2018.09.039](https://doi.org/10.1016/j.cej.2018.09.039) |
| 136 | `cheng2021theoretical` | 2 | 16 | Olea 2021 — *Theoretical Prediction of Selectivity in Solvent Extraction of La(I…* | [10.1016/j.molliq.2020.114655](https://doi.org/10.1016/j.molliq.2020.114655) |
| 137 | `cole2020redox` | 2 | 15 | Cole 2020 — *Redox-Driven Chelation and Kinetic Separation of Select Rare Earths…* | [10.1021/acs.inorgchem.9b00975](https://doi.org/10.1021/acs.inorgchem.9b00975) |
| 138 | `cui2016high` | 2 | 8 | Cui 2016 — *High-performance polymer-supported extractants with phosphonate lig…* | [10.1002/aic.15236](https://doi.org/10.1002/aic.15236) |
| 139 | `das2016alternative` | 2 | 22 | Das 2016 — *Alternative Alkaline Conditioning of Amidoxime Based Adsorbent for…* | [10.1021/acs.iecr.5b03210](https://doi.org/10.1021/acs.iecr.5b03210) |
| 140 | `delaney2017theory` | 2 | 8 | Delaney 2017 — *Theory of polyelectrolyte complexation - Complex coacervates are se…* | [10.1063/1.4985568](https://doi.org/10.1063/1.4985568) |
| 141 | `diazgomez2023synthesis` | 2 | 18 | Diaz Gomez 2023 — *Synthesis and evaluation of new modified diglycolamides with differ…* | [10.1039/d2nj05663a](https://doi.org/10.1039/d2nj05663a) |
| 142 | `dobbelaere2021machine` | 2 | 18 | Dobbelaere 2021 — *Machine Learning in Chemical Engineering: Strengths, Weaknesses, Op…* | [10.1016/j.eng.2021.03.019](https://doi.org/10.1016/j.eng.2021.03.019) |
| 143 | `donmoyer2023effect` | 2 | 21 | Donmoyer 2023 — *Effect of oxidative breakers on organic matter degradation, contami…* | [10.1016/j.fuel.2022.125678](https://doi.org/10.1016/j.fuel.2022.125678) |
| 144 | `estay2023challenges` | 2 | 18 | Estay 2023 — *On the Challenges of Applying Machine Learning in Mineral Processin…* | [10.3390/min13060788](https://doi.org/10.3390/min13060788) |
| 145 | `fieser2016raman` | 2 | 19 | Fieser 2016 — *Raman Spectroscopy of the N–N Bond in Rare Earth Dinitrogen Complex…* | [10.1039/C5DT04547A](https://doi.org/10.1039/C5DT04547A) |
| 146 | `gomezflores2022critical` | 2 | 18 | Gomez-Flores 2022 — *A critical review of artificial intelligence in mineral concentrati…* | [10.1016/j.mineng.2022.107884](https://doi.org/10.1016/j.mineng.2022.107884) |
| 147 | `han2021thermodynamic` | 2 | 10 | Han 2021 — *Thermodynamic Analysis of Precipitation Characteristics of Rare Ear…* | [10.3390/min11070670](https://doi.org/10.3390/min11070670) |
| 148 | `hassas2021effect` | 2 | 10 | Hassas 2021 — *Effect of Various Ligands on the Selective Precipitation of Critica…* | [10.1016/j.chemosphere.2021.130684](https://doi.org/10.1016/j.chemosphere.2021.130684) |
| 149 | `hogan2017rhamnolipid` | 2 | 11 | Hogan 2017 — *Rhamnolipid Biosurfactant Complexation of Rare Earth Elements* | [10.1016/j.jhazmat.2017.06.056](https://doi.org/10.1016/j.jhazmat.2017.06.056) |
| 150 | `hosokawa2022improved` | 2 | 10 | Hosokawa 2022 — *Improved Recovery and Selectivity of Lanthanide-Ion-Binding Cyclic…* | [10.3390/min12020148](https://doi.org/10.3390/min12020148) |

```text
https://doi.org/10.1016/j.jre.2019.11.011
https://doi.org/10.1002/anie.201914893
https://doi.org/10.1039/FT9918702995
https://doi.org/10.1021/acs.jpclett.9b00099
https://doi.org/10.1201/9781420059700-c1
https://doi.org/10.1039/d0cs00098a
https://doi.org/10.1080/07366299.2014.985912
https://doi.org/10.3389/fenrg.2014.00045
https://doi.org/10.1186/s12932-015-0022-4
https://doi.org/10.1016/j.jre.2024.04.025
https://doi.org/10.1016/j.coal.2018.02.014
https://doi.org/10.2172/4289324
https://doi.org/10.1016/j.poly.2018.06.050
https://doi.org/10.3390/pr9081369
https://doi.org/10.1021/acs.est.6b00085
https://doi.org/10.17159/2411-9717/1989/2022
https://doi.org/10.3390/pr10071354
https://doi.org/10.1021/ma500500q
https://doi.org/10.1073/pnas.2521526122
https://doi.org/10.3390/ijms26051986
https://doi.org/10.1021/es402165b
https://doi.org/10.3390/nano12132305
https://doi.org/10.1016/b978-0-12-767661-6.50109-0
https://doi.org/10.1007/s11837-024-06756-3
https://doi.org/10.1557/s43577-022-00286-6
https://doi.org/10.3390/app132312600
https://doi.org/10.1016/j.hydromet.2019.02.016
https://doi.org/10.1524/ract.2006.94.6.307
https://doi.org/10.1021/acs.iecr.4c01935
https://doi.org/10.1016/j.jclepro.2012.12.037
https://doi.org/10.1007/s40831-023-00681-6
https://doi.org/10.1039/d0cc02270e
https://doi.org/10.1021/ie200285r
https://doi.org/10.1021/es204005g
https://doi.org/10.1016/j.cej.2018.09.039
https://doi.org/10.1016/j.molliq.2020.114655
https://doi.org/10.1021/acs.inorgchem.9b00975
https://doi.org/10.1002/aic.15236
https://doi.org/10.1021/acs.iecr.5b03210
https://doi.org/10.1063/1.4985568
https://doi.org/10.1039/d2nj05663a
https://doi.org/10.1016/j.eng.2021.03.019
https://doi.org/10.1016/j.fuel.2022.125678
https://doi.org/10.3390/min13060788
https://doi.org/10.1039/C5DT04547A
https://doi.org/10.1016/j.mineng.2022.107884
https://doi.org/10.3390/min11070670
https://doi.org/10.1016/j.chemosphere.2021.130684
https://doi.org/10.1016/j.jhazmat.2017.06.056
https://doi.org/10.3390/min12020148
```

## Batch 4 of 10

| # | Key | Cites | Ch | Source | DOI |
|---:|---|---:|---|---|---|
| 151 | `jally2021method` | 2 | 11 | Jally 2021 — *A New Method for Recovering Rare Earth Elements from the Hyperaccum…* | [10.1016/j.mineng.2021.106879](https://doi.org/10.1016/j.mineng.2021.106879) |
| 152 | `jorjani2008prediction` | 2 | 18 | Jorjani 2008 — *Prediction of yttrium, lanthanum, cerium, and neodymium leaching re…* | [10.1016/s1005-8850(08)60070-5](https://doi.org/10.1016/s1005-8850(08)60070-5) |
| 153 | `kanahashi2022machine` | 2 | 18 | Kanahashi 2022 — *Machine learning-based analysis of overall stability constants of m…* | [10.1038/s41598-022-15300-9](https://doi.org/10.1038/s41598-022-15300-9) |
| 154 | `kashid2007hydrodynamics` | 2 | 9 | Kashid 2007 — *Hydrodynamics of liquid–liquid slug flow capillary microreactor: Fl…* | [10.1016/j.cej.2006.11.020](https://doi.org/10.1016/j.cej.2006.11.020) |
| 155 | `kim2019separation` | 2 | 8 | Yoshida 2019 — *Separation and Recovery of Scandium from Sulfate Media by Solvent E…* | [10.1021/acsomega.9b02540](https://doi.org/10.1021/acsomega.9b02540) |
| 156 | `kosemutlu2020separation` | 2 | 4,13 | Kose-Mutlu 2020 — *Separation of Rare Earth Elements from Mixed-Metal Feedstocks by Mi…* | [10.1080/09593330.2020.1812732](https://doi.org/10.1080/09593330.2020.1812732) |
| 157 | `kumar2023comprehensive` | 2 | 8 | Khamis 2024 — *Comprehensive review on pH and temperature-responsive polymeric ads…* | [10.1016/j.chemosphere.2023.140801](https://doi.org/10.1016/j.chemosphere.2023.140801) |
| 158 | `lee2008complex` | 2 | 8 | Lee 2008 — *Complex coacervation: A field theoretic simulation study of polyele…* | [10.1063/1.2936834](https://doi.org/10.1063/1.2936834) |
| 159 | `lee2021idaes` | 2 | 17 | Lee 2021 — *The IDAES process modeling framework and model library—Flexibility…* | [10.1002/amp2.10095](https://doi.org/10.1002/amp2.10095) |
| 160 | `lee2025data` | 2 | 18 | Lee 2025 — *Data-Driven Kinetic Reaction Networks for Separation Chemistry* | [10.1021/acs.jctc.4c01783](https://doi.org/10.1021/acs.jctc.4c01783) |
| 161 | `lee2025polyelectrolyte` | 2 | 8 | Lee 2025 — *Polyelectrolyte Complex Coacervates: Structural Insights, Rheologic…* | [10.1007/s12221-025-00975-4](https://doi.org/10.1007/s12221-025-00975-4) |
| 162 | `leoncini2017ligands` | 2 | 22 | Leoncini 2017 — *Ligands for f-element extraction used in the nuclear fuel cycle* | [10.1039/c7cs00574a](https://doi.org/10.1039/c7cs00574a) |
| 163 | `li2019coassembly` | 2 | 8 | Li 2019 — *Coassembly of Short Peptide and Polyoxometalate into Complex Coacer…* | [10.1021/acs.langmuir.9b00273](https://doi.org/10.1021/acs.langmuir.9b00273) |
| 164 | `li2022development` | 2 | 19 | Li 2022 — *Development of a Fully Automatic Separation System Coupled with Onl…* | [10.1039/D2RA02833F](https://doi.org/10.1039/D2RA02833F) |
| 165 | `li2022high` | 2 | 11,23 | Li 2023 — *High Toxicity of Amino Acid-Based Deep Eutectic Solvents* | [10.1016/j.molliq.2022.121044](https://doi.org/10.1016/j.molliq.2022.121044) |
| 166 | `liang2019nanoscale` | 2 | 15 | Liang 2019 — *Nanoscale view of assisted ion transport across the liquid-liquid i…* | [10.1073/pnas.1701389115](https://doi.org/10.1073/pnas.1701389115) |
| 167 | `lin1994supercritical` | 2 | 13 | Lin 1993 — *Supercritical Fluid Extraction of Lanthanides and Actinides from So…* | [10.1021/ac00066a027](https://doi.org/10.1021/ac00066a027) |
| 168 | `lopez2018application` | 2 | 13 | López 2018 — *Application of Nanofiltration for Acidic Waters Containing Rare Ear…* | [10.1016/j.desal.2017.12.033](https://doi.org/10.1016/j.desal.2017.12.033) |
| 169 | `lyon2017dynamic` | 2 | 17 | Lyon 2017 — *Dynamic Modeling for the Separation of Rare Earth Elements Using So…* | [10.1021/acs.iecr.6b04009](https://doi.org/10.1021/acs.iecr.6b04009) |
| 170 | `meng2023heap` | 2 | 6 | Meng 2023 — *Heap leaching of ion adsorption rare earth ores and REEs recovery f…* | [10.1016/j.scitotenv.2023.165417](https://doi.org/10.1016/j.scitotenv.2023.165417) |
| 171 | `morris1976fluidized` | 2 | 7 | Morris 1976 — *Fluidized-bed chlorination rates of Australian rutile* | [10.1007/bf02652823](https://doi.org/10.1007/bf02652823) |
| 172 | `mugion2025systematic` | 2 | 23 | Mugion 2025 — *A Systematic Literature Review of Selected Aspects of Life Cycle As…* | [10.3390/su17135825](https://doi.org/10.3390/su17135825) |
| 173 | `murase1995recovery` | 2 | 7 | Murase 1995 — *Recovery of rare metals from scrap of rare earth intermetallic mate…* | [10.1016/0925-8388(94)01316-A](https://doi.org/10.1016/0925-8388(94)01316-A) |
| 174 | `murthy2011application` | 2 | 4,13 | Murthy 2011 — *Application of Nanofiltration to Treat Rare Earth Element (Neodymiu…* | [10.1016/S1002-0721(10)60581-9](https://doi.org/10.1016/S1002-0721(10)60581-9) |
| 175 | `namboothiri2017bauxite` | 2 | 7 | Namboothiri 2017 — *Bauxite Processing via Chloride Route to Produce Chloride Products…* | [10.1007/978-3-319-51541-0_79](https://doi.org/10.1007/978-3-319-51541-0_79) |
| 176 | `nguyen2025explainable` | 2 | 18 | Nguyen 2025 — *Explainable Artificial Intelligence for Predicting Rare Earth Eleme…* | [10.1016/j.jhazmat.2025.139479](https://doi.org/10.1016/j.jhazmat.2025.139479) |
| 177 | `nikolova2023lanthanides` | 2 | 8,11 | Nikolova 2023 — *Lanthanides as Calcium Mimetic Species in Calcium-Signaling/Bufferi…* | [10.3390/ijms24076297](https://doi.org/10.3390/ijms24076297) |
| 178 | `oconnelldanes2022selective` | 2 | 10,13 | O'Connell-Danes 2022 — *Selective Separation of Light Rare-Earth Elements by Supramolecular…* | [10.1038/s41467-022-32178-3](https://doi.org/10.1038/s41467-022-32178-3) |
| 179 | `onal2015recycling` | 2 | 7,20 | Önal 2015 — *Recycling of NdFeB magnets using sulfation, selective roasting, and…* | [10.1007/s40831-015-0021-9](https://doi.org/10.1007/s40831-015-0021-9) |
| 180 | `ortunomacias2024enhanced` | 2 | 8,11 | Ortuno Macias 2025 — *Enhanced Rare Earth Element Recovery with Cross-Linked Glutaraldehy…* | [10.1016/j.jcis.2024.08.225](https://doi.org/10.1016/j.jcis.2024.08.225) |
| 181 | `overbeek1957phase` | 2 | 8 | Overbeek 1957 — *Phase separation in polyelectrolyte solutions. Theory of complex co…* | [10.1002/jcp.1030490404](https://doi.org/10.1002/jcp.1030490404) |
| 182 | `priftis2012early` | 2 | 8 | Veis 2011 — *A Review of the Early Development of the Thermodynamics of the Comp…* | [10.1016/j.cis.2011.01.007](https://doi.org/10.1016/j.cis.2011.01.007) |
| 183 | `qi2018equipment` | 2 | 3,17 | Qi 2018 — *Equipment in Rare-Earth Solvent Extraction-Separation Process: Mixe…* | [10.1016/b978-0-12-813920-2.00005-2](https://doi.org/10.1016/b978-0-12-813920-2.00005-2) |
| 184 | `salehi2025tailored` | 2 | 4,10 | Salehi 2025 — *Tailored Separation of Light Rare-Earth Elements Using Combined Oxi…* | [10.1016/j.seppur.2025.132566](https://doi.org/10.1016/j.seppur.2025.132566) |
| 185 | `simonnet2021study` | 2 | 18 | Simonnet 2021 — *Study on Phenanthroline Carboxamide for Lanthanide Separation: Infl…* | [10.1021/acs.inorgchem.1c01729](https://doi.org/10.1021/acs.inorgchem.1c01729) |
| 186 | `sing2020progress` | 2 | 8 | Sing 2020 — *Recent progress in the science of complex coacervation* | [10.1039/D0SM00001A](https://doi.org/10.1039/D0SM00001A) |
| 187 | `sing2025polyelectrolyte` | 2 | 8 | Li 2025 — *Polyelectrolyte complex-based materials for separations: progress,…* | [10.1039/D4MH01840K](https://doi.org/10.1039/D4MH01840K) |
| 188 | `slack2020fooling` | 2 | 18 | Slack 2020 — *Fooling LIME and SHAP* | [10.1145/3375627.3375830](https://doi.org/10.1145/3375627.3375830) |
| 189 | `srivastava2021modeling` | 2 | 17 | Srivastava 2021 — *Modeling of Rare Earth Solvent Extraction Process for Flowsheet Des…* | [10.13023/etd.2021.220](https://doi.org/10.13023/etd.2021.220) |
| 190 | `stamberga2020structure` | 2 | 13,18 | Stamberga 2020 — *Structure Activity Relationship Approach toward the Improved Separa…* | [10.1021/acs.inorgchem.0c02861](https://doi.org/10.1021/acs.inorgchem.0c02861) |
| 191 | `stops2022flowsheet` | 2 | 18 | Stops 2022 — *Flowsheet generation through hierarchical reinforcement learning an…* | [10.1002/aic.17938](https://doi.org/10.1002/aic.17938) |
| 192 | `stosch2016neutron` | 2 | 19 | Stosch 2016 — *Neutron Activation Analysis of the Rare Earth Elements (REE) – With…* | [10.1515/psr-2016-0062](https://doi.org/10.1515/psr-2016-0062) |
| 193 | `su2020electrochemical` | 2 | 12 | Su 2020 — *Electrochemical Separations for Metal Recycling* | [10.1149/2.f08203if](https://doi.org/10.1149/2.f08203if) |
| 194 | `taylor2023architector` | 2 | 16 | Taylor 2023 — *Architector for High-Throughput Cross-Periodic Table Three-Dimensio…* | [10.1038/s41467-023-38169-2](https://doi.org/10.1038/s41467-023-38169-2) |
| 195 | `thebelt2022maximizing` | 2 | 18 | Thebelt 2022 — *Maximizing information from chemical engineering data sets: Applica…* | [10.1016/j.ces.2022.117469](https://doi.org/10.1016/j.ces.2022.117469) |
| 196 | `tian2024leaching` | 2 | 6 | Tian 2024 — *Leaching characteristics and environmental impact of heavy metals i…* | [10.1016/j.ecoenv.2024.116642](https://doi.org/10.1016/j.ecoenv.2024.116642) |
| 197 | `tissandier1998proton` | 2 | 14 | Tissandier 1998 — *The Proton's Absolute Aqueous Enthalpy and Gibbs Free Energy of Sol…* | [10.1021/jp982638r](https://doi.org/10.1021/jp982638r) |
| 198 | `tse2024spectroscopic` | 2 | 19 | Tse 2025 — *Spectroscopic Online Monitoring: Using a Multi-Track Visible Spectr…* | [10.1021/acsomega.4c07704](https://doi.org/10.1021/acsomega.4c07704) |
| 199 | `uversky2015intrinsically` | 2 | 8 | Uversky 2014 — *Intrinsically disordered proteins as crucial constituents of cellul…* | [10.1016/j.febslet.2014.11.028](https://doi.org/10.1016/j.febslet.2014.11.028) |
| 200 | `vogel2023learning` | 2 | 18 | Vogel 2023 — *Learning from flowsheets: A generative transformer model for autoco…* | [10.1016/j.compchemeng.2023.108162](https://doi.org/10.1016/j.compchemeng.2023.108162) |

```text
https://doi.org/10.1016/j.mineng.2021.106879
https://doi.org/10.1016/s1005-8850(08)60070-5
https://doi.org/10.1038/s41598-022-15300-9
https://doi.org/10.1016/j.cej.2006.11.020
https://doi.org/10.1021/acsomega.9b02540
https://doi.org/10.1080/09593330.2020.1812732
https://doi.org/10.1016/j.chemosphere.2023.140801
https://doi.org/10.1063/1.2936834
https://doi.org/10.1002/amp2.10095
https://doi.org/10.1021/acs.jctc.4c01783
https://doi.org/10.1007/s12221-025-00975-4
https://doi.org/10.1039/c7cs00574a
https://doi.org/10.1021/acs.langmuir.9b00273
https://doi.org/10.1039/D2RA02833F
https://doi.org/10.1016/j.molliq.2022.121044
https://doi.org/10.1073/pnas.1701389115
https://doi.org/10.1021/ac00066a027
https://doi.org/10.1016/j.desal.2017.12.033
https://doi.org/10.1021/acs.iecr.6b04009
https://doi.org/10.1016/j.scitotenv.2023.165417
https://doi.org/10.1007/bf02652823
https://doi.org/10.3390/su17135825
https://doi.org/10.1016/0925-8388(94)01316-A
https://doi.org/10.1016/S1002-0721(10)60581-9
https://doi.org/10.1007/978-3-319-51541-0_79
https://doi.org/10.1016/j.jhazmat.2025.139479
https://doi.org/10.3390/ijms24076297
https://doi.org/10.1038/s41467-022-32178-3
https://doi.org/10.1007/s40831-015-0021-9
https://doi.org/10.1016/j.jcis.2024.08.225
https://doi.org/10.1002/jcp.1030490404
https://doi.org/10.1016/j.cis.2011.01.007
https://doi.org/10.1016/b978-0-12-813920-2.00005-2
https://doi.org/10.1016/j.seppur.2025.132566
https://doi.org/10.1021/acs.inorgchem.1c01729
https://doi.org/10.1039/D0SM00001A
https://doi.org/10.1039/D4MH01840K
https://doi.org/10.1145/3375627.3375830
https://doi.org/10.13023/etd.2021.220
https://doi.org/10.1021/acs.inorgchem.0c02861
https://doi.org/10.1002/aic.17938
https://doi.org/10.1515/psr-2016-0062
https://doi.org/10.1149/2.f08203if
https://doi.org/10.1038/s41467-023-38169-2
https://doi.org/10.1016/j.ces.2022.117469
https://doi.org/10.1016/j.ecoenv.2024.116642
https://doi.org/10.1021/jp982638r
https://doi.org/10.1021/acsomega.4c07704
https://doi.org/10.1016/j.febslet.2014.11.028
https://doi.org/10.1016/j.compchemeng.2023.108162
```

## Batch 5 of 10

| # | Key | Cites | Ch | Source | DOI |
|---:|---|---:|---|---|---|
| 201 | `wang2020machine` | 2 | 18 | Wang 2020 — *Machine Learning for Materials Scientists: An Introductory Guide to…* | [10.1021/acs.chemmater.0c01907](https://doi.org/10.1021/acs.chemmater.0c01907) |
| 202 | `wang2021strategy` | 2 | 8 | Sui 2020 — *A new strategy of three-liquid-phase partitioning for stripping of…* | [10.1016/j.seppur.2020.117386](https://doi.org/10.1016/j.seppur.2020.117386) |
| 203 | `wang2023polyelectrolyte` | 2 | 8 | Bediako 2023 — *Polyelectrolyte complex-derived adsorbent capsules capable of selec…* | [10.1016/j.ces.2023.118688](https://doi.org/10.1016/j.ces.2023.118688) |
| 204 | `wang2025selective` | 2 | 10 | Wang 2025 — *Selective-Crystallization Strategy for the Separation of Rare Earth…* | [10.1016/j.ccr.2025.216686](https://doi.org/10.1016/j.ccr.2025.216686) |
| 205 | `wigh2022review` | 2 | 18 | Wigh 2022 — *A review of molecular representation in the age of machine learning* | [10.1002/wcms.1603](https://doi.org/10.1002/wcms.1603) |
| 206 | `xian2016glutarimidedioxime` | 2 | 22 | Xian 2016 — *Glutarimidedioxime: A Complexing and Reducing Reagent for Plutonium…* | [10.1002/anie.201510712](https://doi.org/10.1002/anie.201510712) |
| 207 | `yadav2018ndfeb` | 2 | 4,13 | Yadav 2018 — *NdFeB magnet recycling: Dysprosium recovery by non-dispersive solve…* | [10.1016/j.seppur.2017.11.025](https://doi.org/10.1016/j.seppur.2017.11.025) |
| 208 | `yang1999carbochlorination` | 2 | 7 | Yang 1999 — *Carbochlorination of tantalum and niobium oxides: Thermodynamic sim…* | [10.1002/aic.690450315](https://doi.org/10.1002/aic.690450315) |
| 209 | `yang2024investigation` | 2 | 10 | Yang 2025 — *Investigation on the Recovery of Rare Earth Fluorides from Spent Ra…* | [10.3390/ma18071538](https://doi.org/10.3390/ma18071538) |
| 210 | `yang2025emerging` | 2 | 11 | Yang 2025 — *Emerging role of rare earth elements in biomolecular functions* | [10.1093/ismejo/wrae241](https://doi.org/10.1093/ismejo/wrae241) |
| 211 | `zahakifar2025solvent` | 2 | 14,22 | Zahakifar 2025 — *The solvent extraction and stripping process using Alamine 336 with…* | [10.1038/s41598-025-96421-9](https://doi.org/10.1038/s41598-025-96421-9) |
| 212 | `zalupski2008two` | 2 | 14 | Zalupski 2008 — *Two‐Phase Calorimetry. I. Studies on the Thermodynamics of Lanthani…* | [10.1080/07366290802301374](https://doi.org/10.1080/07366290802301374) |
| 213 | `zhang2024remarkably` | 2 | 8 | Sengupta 2024 — *Remarkably High Separation of Neodymium from Praseodymium by Select…* | [10.1002/chem.202303923](https://doi.org/10.1002/chem.202303923) |
| 214 | `zhang2026design` | 2 | 18 | Zhang 2026 — *Design of monopyridine amine extractant for selective heavy rare ea…* | [10.1016/j.jece.2026.121221](https://doi.org/10.1016/j.jece.2026.121221) |
| 215 | `zhong2021thermoresponsive` | 2 | 8 | Kafetzi 2021 — *Thermoresponsive PNIPAM-b-PAA block copolymers as smart adsorbents…* | [10.1016/j.colsurfa.2020.126049](https://doi.org/10.1016/j.colsurfa.2020.126049) |
| 216 | `abolhasani2023rise` | 1 | 18 | Abolhasani 2023 — *The rise of self-driving labs in chemical and materials sciences* | [10.1038/s44160-022-00231-0](https://doi.org/10.1038/s44160-022-00231-0) |
| 217 | `ahmed2020chromatographic` | 1 | 19 | Ahmed 2020 — *Chromatographic separation and determination of some heavy metals a…* | [10.1007/s11696-020-01182-6](https://doi.org/10.1007/s11696-020-01182-6) |
| 218 | `ahn2020valorization` | 1 | 20 | Ahn 2020 — *Valorization of waste NiMH battery through recovery of critical rar…* | [10.1016/j.wasman.2020.01.014](https://doi.org/10.1016/j.wasman.2020.01.014) |
| 219 | `alguacil2023work` | 1 | 11 | Alguacil 2023 — *Recent Work on the Recovery of Rare Earths Using Ionic Liquids and…* | [10.3390/min13101288](https://doi.org/10.3390/min13101288) |
| 220 | `alizadeh2023deep` | 1 | 16 | Alizadeh 2023 — *A Deep Insight into the Selectivity Difference Between Y(III) and L…* | [10.21203/rs.3.rs-2525701/v1](https://doi.org/10.21203/rs.3.rs-2525701/v1) |
| 221 | `ansari2016thermodynamics` | 1 | 19 | Ansari 2016 — *Thermodynamics of Biphasic Lanthanide Extraction by Tripodal Diglyc…* | [10.1039/C6DT03380F](https://doi.org/10.1039/C6DT03380F) |
| 222 | `ascani2025molecular` | 1 | 8 | Ascani 2025 — *Molecular thermodynamics of complex coacervate systems. Part I: Mod…* | [10.1016/j.fluid.2024.114304](https://doi.org/10.1016/j.fluid.2024.114304) |
| 223 | `bai2025harnessing` | 1 | 11 | Bai 2025 — *Harnessing Synthetic Biology for Sustainable Recovery of Critical M…* | [10.1002/adfm.202509900](https://doi.org/10.1002/adfm.202509900) |
| 224 | `baker2002rapid` | 1 | 19 | Baker 2002 — *Rapid and Highly Reproducible Analysis of Rare Earth Elements by Mu…* | [10.1016/S0016-7037(02)00921-3](https://doi.org/10.1016/S0016-7037(02)00921-3) |
| 225 | `bastos2023isothermal` | 1 | 19 | Bastos 2023 — *Isothermal Titration Calorimetry* | [10.1038/s43586-023-00199-x](https://doi.org/10.1038/s43586-023-00199-x) |
| 226 | `batzner2022equivariant` | 1 | 18 | Batzner 2022 — *E(3)-equivariant graph neural networks for data-efficient and accur…* | [10.1038/s41467-022-29939-5](https://doi.org/10.1038/s41467-022-29939-5) |
| 227 | `benetollo2003structural` | 1 | 15 | Benetollo 2003 — *Structural Variations Across the Lanthanide Series of Macrocyclic D…* | [10.1021/ic025790n](https://doi.org/10.1021/ic025790n) |
| 228 | `benjamin1993mechanism` | 1 | 14 | Benjamin 1993 — *Mechanism and Dynamics of Ion Transfer Across a Liquid-Liquid Inter…* | [10.1126/science.261.5128.1558](https://doi.org/10.1126/science.261.5128.1558) |
| 229 | `biegler2010nonlinear` | 1 | 17 | Biegler 2010 — *Nonlinear Programming: Concepts, Algorithms, and Applications to Ch…* | [10.1137/1.9780898719383](https://doi.org/10.1137/1.9780898719383) |
| 230 | `biegler2022dont` | 1 | 17 | Biegler 2022 — *Don’t search—Solve! Process optimization modeling with IDAES* | [10.1016/b978-0-323-85043-8.00005-2](https://doi.org/10.1016/b978-0-323-85043-8.00005-2) |
| 231 | `bishop2024rare` | 1 | 19 | Bishop 2024 — *Rare Earth Element Speciation in Coal and Coal Combustion Byproduct…* | [10.1021/acs.est.4c04256](https://doi.org/10.1021/acs.est.4c04256) |
| 232 | `boiko2023autonomous` | 1 | 18 | Boiko 2023 — *Autonomous chemical research with large language models* | [10.1038/s41586-023-06792-0](https://doi.org/10.1038/s41586-023-06792-0) |
| 233 | `bonificio2016rare` | 1 | 11 | Bonificio 2016 — *Rare-Earth Separation Using Bacteria* | [10.1021/acs.estlett.6b00064](https://doi.org/10.1021/acs.estlett.6b00064) |
| 234 | `bradley1966vaterite` | 1 | 10 | Bradley 1966 — *The Vaterite-Type ABO$_3$ Rare-Earth Borates* | [10.1107/S0365110X66000549](https://doi.org/10.1107/S0365110X66000549) |
| 235 | `bran2024augmenting` | 1 | 18 | M. Bran 2024 — *Augmenting large language models with chemistry tools* | [10.1038/s42256-024-00832-8](https://doi.org/10.1038/s42256-024-00832-8) |
| 236 | `brangwynne2015polymer` | 1 | 8 | Brangwynne 2015 — *Polymer physics of intracellular phase transitions* | [10.1038/nphys3532](https://doi.org/10.1038/nphys3532) |
| 237 | `breuker2020biosorption` | 1 | 11 | Breuker 2020 — *Biosorption of Rare Earth Elements by Different Microorganisms in A…* | [10.3390/met10070954](https://doi.org/10.3390/met10070954) |
| 238 | `bulin2025preparation` | 1 | 11 | Bulin 2025 — *Preparation of Ion Imprinted EDTA Modified Chitosan-Magnetic Graphe…* | [10.1016/j.scitotenv.2025.178468](https://doi.org/10.1016/j.scitotenv.2025.178468) |
| 239 | `burger2020mobile` | 1 | 18 | Burger 2020 — *A mobile robotic chemist* | [10.1038/s41586-020-2442-2](https://doi.org/10.1038/s41586-020-2442-2) |
| 240 | `butler2018machine` | 1 | 18 | Butler 2018 — *Machine learning for molecular and materials science* | [10.1038/s41586-018-0337-2](https://doi.org/10.1038/s41586-018-0337-2) |
| 241 | `carrott2008oxidation` | 1 | 22 | Carrott 2008 — *Oxidation–reduction reactions of simple hydroxamic acids and pluton…* | [10.1524/ract.2008.1502](https://doi.org/10.1524/ract.2008.1502) |
| 242 | `chapleski2020molecular` | 1 | 16 | Chapleski 2020 — *A Molecular-Scale Approach to Rare-Earth Beneficiation: Thinking Sm…* | [10.1016/j.isci.2020.101435](https://doi.org/10.1016/j.isci.2020.101435) |
| 243 | `chaube2020applied` | 1 | 18 | Chaube 2020 — *Applied machine learning for predicting the lanthanide-ligand bindi…* | [10.1038/s41598-020-71255-9](https://doi.org/10.1038/s41598-020-71255-9) |
| 244 | `chen2018flowsheet` | 1 | 17 | Chen 2018 — *Flowsheet Simulation of Cobalt–Nickel Separation by Solvent Extract…* | [10.1021/acs.iecr.7b05254](https://doi.org/10.1021/acs.iecr.7b05254) |
| 245 | `chen2018leaching` | 1 | 6 | Chen 2018 — *Leaching behaviour of rare earth elements from low-grade weathered…* | [10.1180/clm.2018.37](https://doi.org/10.1180/clm.2018.37) |
| 246 | `chen2019complexation` | 1 | 19 | Chen 2019 — *Complexation of Lanthanides with N,N,N′,N′-Tetramethylamide Derivat…* | [10.1021/acs.inorgchem.9b00545](https://doi.org/10.1021/acs.inorgchem.9b00545) |
| 247 | `chen2021advances` | 1 | — | Chen 2022 — *Recent advances in selective separation technologies of rare earth…* | [10.1016/j.jece.2021.107104](https://doi.org/10.1016/j.jece.2021.107104) |
| 248 | `chen2022multiphase` | 1 | 8 | Chen 2022 — *Multiphase Coacervation of Polyelectrolytes Driven by Asymmetry of…* | [10.1021/acs.macromol.2c01205](https://doi.org/10.1021/acs.macromol.2c01205) |
| 249 | `chen2023various` | 1 | 5 | Chen 2023 — *Various rare earth particles magnetic separation using magnetic flu…* | [10.1016/j.mineng.2023.108350](https://doi.org/10.1016/j.mineng.2023.108350) |
| 250 | `chen2024continuous` | 1 | — | Chen 2024 — *Continuous high viscosity biphasic liquid separation* | [10.1016/j.seppur.2024.127111](https://doi.org/10.1016/j.seppur.2024.127111) |

```text
https://doi.org/10.1021/acs.chemmater.0c01907
https://doi.org/10.1016/j.seppur.2020.117386
https://doi.org/10.1016/j.ces.2023.118688
https://doi.org/10.1016/j.ccr.2025.216686
https://doi.org/10.1002/wcms.1603
https://doi.org/10.1002/anie.201510712
https://doi.org/10.1016/j.seppur.2017.11.025
https://doi.org/10.1002/aic.690450315
https://doi.org/10.3390/ma18071538
https://doi.org/10.1093/ismejo/wrae241
https://doi.org/10.1038/s41598-025-96421-9
https://doi.org/10.1080/07366290802301374
https://doi.org/10.1002/chem.202303923
https://doi.org/10.1016/j.jece.2026.121221
https://doi.org/10.1016/j.colsurfa.2020.126049
https://doi.org/10.1038/s44160-022-00231-0
https://doi.org/10.1007/s11696-020-01182-6
https://doi.org/10.1016/j.wasman.2020.01.014
https://doi.org/10.3390/min13101288
https://doi.org/10.21203/rs.3.rs-2525701/v1
https://doi.org/10.1039/C6DT03380F
https://doi.org/10.1016/j.fluid.2024.114304
https://doi.org/10.1002/adfm.202509900
https://doi.org/10.1016/S0016-7037(02)00921-3
https://doi.org/10.1038/s43586-023-00199-x
https://doi.org/10.1038/s41467-022-29939-5
https://doi.org/10.1021/ic025790n
https://doi.org/10.1126/science.261.5128.1558
https://doi.org/10.1137/1.9780898719383
https://doi.org/10.1016/b978-0-323-85043-8.00005-2
https://doi.org/10.1021/acs.est.4c04256
https://doi.org/10.1038/s41586-023-06792-0
https://doi.org/10.1021/acs.estlett.6b00064
https://doi.org/10.1107/S0365110X66000549
https://doi.org/10.1038/s42256-024-00832-8
https://doi.org/10.1038/nphys3532
https://doi.org/10.3390/met10070954
https://doi.org/10.1016/j.scitotenv.2025.178468
https://doi.org/10.1038/s41586-020-2442-2
https://doi.org/10.1038/s41586-018-0337-2
https://doi.org/10.1524/ract.2008.1502
https://doi.org/10.1016/j.isci.2020.101435
https://doi.org/10.1038/s41598-020-71255-9
https://doi.org/10.1021/acs.iecr.7b05254
https://doi.org/10.1180/clm.2018.37
https://doi.org/10.1021/acs.inorgchem.9b00545
https://doi.org/10.1016/j.jece.2021.107104
https://doi.org/10.1021/acs.macromol.2c01205
https://doi.org/10.1016/j.mineng.2023.108350
https://doi.org/10.1016/j.seppur.2024.127111
```

## Batch 6 of 10

| # | Key | Cites | Ch | Source | DOI |
|---:|---|---:|---|---|---|
| 251 | `cheng2020determination` | 1 | 19 | Baghaliannejad 2021 — *Determination of Rare Earth Elements in Uranium Materials by ICP-MS…* | [10.1016/j.talanta.2020.121509](https://doi.org/10.1016/j.talanta.2020.121509) |
| 252 | `cheng2024synthesis` | 1 | 6 | Cheng 2024 — *Synthesis of high-crystallinity Zeolite A from rare earth tailings:…* | [10.1016/j.jhazmat.2024.133730](https://doi.org/10.1016/j.jhazmat.2024.133730) |
| 253 | `chhantyal2025lanmodulin` | 1 | 8 | Chhantyal 2025 — *Lanmodulin as protein-based platform for the separation of light ra…* | [10.1080/01496395.2025.2602158](https://doi.org/10.1080/01496395.2025.2602158) |
| 254 | `chinkaka2023unexpected` | 1 | 6 | Chinkaka 2023 — *Unexpected Expansion of Rare-Earth Element Mining Activities in the…* | [10.3390/rs15184597](https://doi.org/10.3390/rs15184597) |
| 255 | `chung2023recovery` | 1 | 20 | Chung 2023 — *Recovery of Rare Earth Elements from Spent NdFeB Magnets: Metal Ext…* | [10.3390/met13030559](https://doi.org/10.3390/met13030559) |
| 256 | `cockerill1973lanthanide` | 1 | 19 | Cockerill 1973 — *Lanthanide Shift Reagents for Nuclear Magnetic Resonance Spectrosco…* | [10.1021/cr60286a001](https://doi.org/10.1021/cr60286a001) |
| 257 | `coley2017prediction` | 1 | 18 | Coley 2017 — *Prediction of Organic Reaction Outcomes Using Machine Learning* | [10.1021/acscentsci.7b00064](https://doi.org/10.1021/acscentsci.7b00064) |
| 258 | `coquil2022interactions` | 1 | 14 | Coquil 2022 — *On interactions in binary mixtures used in solvent extraction: Insi…* | [10.1016/j.molliq.2021.116985](https://doi.org/10.1016/j.molliq.2021.116985) |
| 259 | `corbett2017incorporation` | 1 | 5 | Corbett 2017 — *Incorporation of Indigenous Microorganisms Increases Leaching Rates…* | [10.4028/www.scientific.net/ssp.262.294](https://doi.org/10.4028/www.scientific.net/ssp.262.294) |
| 260 | `daoutidis2024machine` | 1 | 18 | Daoutidis 2024 — *Machine learning in process systems engineering: Challenges and opp…* | [10.1016/j.compchemeng.2023.108523](https://doi.org/10.1016/j.compchemeng.2023.108523) |
| 261 | `das2024poly` | 1 | 8 | Das 2024 — *Poly(N-isopropylacrylamide) and Its Copolymers: A Review on Recent…* | [10.1002/adfm.202402432](https://doi.org/10.1002/adfm.202402432) |
| 262 | `davidson2020application` | 1 | 8 | González-Sálamo 2021 — *Application of stimuli-responsive materials for extraction purposes* | [10.1016/j.chroma.2020.461764](https://doi.org/10.1016/j.chroma.2020.461764) |
| 263 | `deng2022rare` | 1 | 9 | Deng 2022 — *Rare earth elements from waste* | [10.1126/sciadv.abm3132](https://doi.org/10.1126/sciadv.abm3132) |
| 264 | `deng2024maximized` | 1 | 13 | Deng 2024 — *Maximized Lanthanide Extraction Using Supercritical CO₂ and Fluorin…* | [10.1021/acssusresmgt.4c00122](https://doi.org/10.1021/acssusresmgt.4c00122) |
| 265 | `depauw2020highly` | 1 | 19 | De Pauw 2019 — *Highly Sensitive Nondestructive Rare Earth Element Detection by Mea…* | [10.1021/acs.analchem.9b04176](https://doi.org/10.1021/acs.analchem.9b04176) |
| 266 | `desbouis2012thermodynamics` | 1 | 19 | Di Bernardo 2012 — *Thermodynamics of Lanthanide(III) Complexation in Non-Aqueous Solve…* | [10.1016/j.ccr.2011.07.010](https://doi.org/10.1016/j.ccr.2011.07.010) |
| 267 | `devlin2022mechanisms` | 1 | 14 | Devlin 2022 — *On the mechanisms of ion adsorption to aqueous interfaces: air-wate…* | [10.1073/pnas.2210857119](https://doi.org/10.1073/pnas.2210857119) |
| 268 | `ding2024mathematical` | 1 | 12 | Ding 2024 — *Mathematical Modeling of Rare Earth Element Separation in Electrodi…* | [10.1038/s41598-024-62885-4](https://doi.org/10.1038/s41598-024-62885-4) |
| 269 | `dinh2022phytomining` | 1 | 11 | Dinh 2022 — *Phytomining of Rare Earth Elements -- A Review* | [10.1016/j.chemosphere.2022.134259](https://doi.org/10.1016/j.chemosphere.2022.134259) |
| 270 | `distler2020thermodynamic` | 1 | 14 | Distler 2020 — *Thermodynamic parameters of Am(III), Cm(III) and Eu(III) extraction…* | [10.1016/j.jct.2019.105955](https://doi.org/10.1016/j.jct.2019.105955) |
| 271 | `doyo2023advances` | 1 | 11 | Doyo 2023 — *Recent Advances in Cellulose, Chitosan, and Alginate Based Biopolym…* | [10.1016/j.jtice.2023.105095](https://doi.org/10.1016/j.jtice.2023.105095) |
| 272 | `duan2015removal` | 1 | 13 | Duan 2015 — *Removal of High-Salinity Matrices Through Polymer-Complexation--Ult…* | [10.1016/j.talanta.2015.04.071](https://doi.org/10.1016/j.talanta.2015.04.071) |
| 273 | `dulski1994interferences` | 1 | 19 | Dulski 1994 — *Interferences of oxide, hydroxide and chloride analyte species in t…* | [10.1007/BF00322470](https://doi.org/10.1007/BF00322470) |
| 274 | `dybczynski2021separation` | 1 | 19 | Dybczyński 2021 — *Separation of Rare Earth Elements (REE) by Ion Interaction Chromato…* | [10.1007/s10337-021-04025-y](https://doi.org/10.1007/s10337-021-04025-y) |
| 275 | `edaugal2025solvent` | 1 | 18 | Edaugal 2025 — *Solvent Screening for Separation Processes Using Machine Learning a…* | [10.1021/cbe.4c00170](https://doi.org/10.1021/cbe.4c00170) |
| 276 | `edington2018coordination` | 1 | 11 | Edington 2018 — *Coordination to Lanthanide Ions Distorts Binding Site Conformation…* | [10.1073/pnas.1722042115](https://doi.org/10.1073/pnas.1722042115) |
| 277 | `elsayed2023sustainable` | 1 | 11 | El-Sayed 2023 — *Sustainable Grafted Chitosan-Dialdehyde Cellulose with High Adsorpt…* | [10.1186/s13065-023-01035-9](https://doi.org/10.1186/s13065-023-01035-9) |
| 278 | `esterhuizen2022interpretable` | 1 | 18 | Esterhuizen 2022 — *Interpretable machine learning for knowledge generation in heteroge…* | [10.1038/s41929-022-00744-z](https://doi.org/10.1038/s41929-022-00744-z) |
| 279 | `evans2014modelling` | 1 | 17 | Evans 2014 — *Modelling Cobalt Solvent Extraction using Aspen Custom Modeler* | [10.1016/b978-0-444-63456-6.50085-5](https://doi.org/10.1016/b978-0-444-63456-6.50085-5) |
| 280 | `fairchild2005chronic` | 1 | 6 | Fairchild 2005 — *Chronic Toxicity of Un-ionized Ammonia to Early Life-Stages of Enda…* | [10.1007/s00244-004-0223-9](https://doi.org/10.1007/s00244-004-0223-9) |
| 281 | `fardis2025surrogate` | 1 | 17 | Fardis 2025 — *Surrogate modeling and optimization of the leaching process in a ra…* | [10.1016/j.compchemeng.2025.109061](https://doi.org/10.1016/j.compchemeng.2025.109061) |
| 282 | `firdaus2016review` | 1 | 20 | Firdaus 2016 — *Review of High-Temperature Recovery of Rare Earth (Nd/Dy) from Magn…* | [10.1007/s40831-016-0045-9](https://doi.org/10.1007/s40831-016-0045-9) |
| 283 | `gangadari2025critical` | 1 | 8 | Gangadari 2025 — *A critical review on selective separation of scandium and iron from…* | [10.1016/j.hydromet.2025.106514](https://doi.org/10.1016/j.hydromet.2025.106514) |
| 284 | `geue2024modern` | 1 | 19 | Geue 2024 — *Modern Electrospray Ionization Mass Spectrometry Techniques for the…* | [10.1021/acs.analchem.4c01028](https://doi.org/10.1021/acs.analchem.4c01028) |
| 285 | `ghidini2019cloud` | 1 | 8 | Sefrou 2020 — *Cloud point extraction of La(III) by C13E10 non-ionic surfactant: S…* | [10.1016/j.cherd.2019.11.027](https://doi.org/10.1016/j.cherd.2019.11.027) |
| 286 | `ghosh2025electrochemical` | 1 | 12 | Ghosh 2025 — *Electrochemical Separation and Clean Energy Applications of Rare Ea…* | [10.1021/acs.chemrev.5c00103](https://doi.org/10.1021/acs.chemrev.5c00103) |
| 287 | `giese2020biosorption` | 1 | 11 | Giese 2020 — *Biosorption as Green Technology for the Recovery and Separation of…* | [10.1007/s11274-020-02821-6](https://doi.org/10.1007/s11274-020-02821-6) |
| 288 | `gifford2007structures` | 1 | 11 | Gifford 2007 — *Structures and Metal-Ion-Binding Properties of the Ca2+-Binding Hel…* | [10.1042/BJ20070255](https://doi.org/10.1042/BJ20070255) |
| 289 | `graedel2011what` | 1 | 20 | Graedel 2011 — *What Do We Know About Metal Recycling Rates?* | [10.1111/j.1530-9290.2011.00342.x](https://doi.org/10.1111/j.1530-9290.2011.00342.x) |
| 290 | `gujar2023complexation` | 1 | 14 | Gujar 2023 — *Complexation thermodynamics of lanthanides with 2-thenoyltrifluoroa…* | [10.1039/d2nj05314d](https://doi.org/10.1039/d2nj05314d) |
| 291 | `gupta1992extractive` | 1 | 7 | Gupta 1992 — *Extractive metallurgy of rare earths* | [10.1179/imr.1992.37.1.197](https://doi.org/10.1179/imr.1992.37.1.197) |
| 292 | `hart2011pyomo` | 1 | 17 | Hart 2011 — *Pyomo: modeling and solving mathematical programs in Python* | [10.1007/s12532-011-0026-8](https://doi.org/10.1007/s12532-011-0026-8) |
| 293 | `hartshorn2015brief` | 1 | 1 | Hartshorn 2015 — *Brief guide to the nomenclature of inorganic chemistry* | [10.1515/pac-2014-0718](https://doi.org/10.1515/pac-2014-0718) |
| 294 | `he2025discovery` | 1 | 11 | He 2025 — *Discovery and Implications of a Nanoscale Rare Earth Mineral in a H…* | [10.1021/acs.est.5c09617](https://doi.org/10.1021/acs.est.5c09617) |
| 295 | `he2025efficiently` | 1 | 10 | He 2025 — *Efficiently Selective Removal of Radioactive Thorium and Uranium fr…* | [10.1016/j.seppur.2025.132426](https://doi.org/10.1016/j.seppur.2025.132426) |
| 296 | `heid2023chemprop` | 1 | 18 | Heid 2023 — *Chemprop: A Machine Learning Package for Chemical Property Predicti…* | [10.1021/acs.jcim.3c01250](https://doi.org/10.1021/acs.jcim.3c01250) |
| 297 | `heilmann2021rare` | 1 | 11 | Heilmann 2021 — *Towards Rare Earth Element Recovery from Wastewaters: Biosorption U…* | [10.1007/s00253-021-11386-9](https://doi.org/10.1007/s00253-021-11386-9) |
| 298 | `heo2025extraction` | 1 | 7 | Heo 2025 — *Extraction of rare earth elements from neodymium (NdFeB) magnet scr…* | [10.1016/j.jre.2024.01.012](https://doi.org/10.1016/j.jre.2024.01.012) |
| 299 | `hessel2013process` | 1 | 9 | Hessel 2013 — *Novel Process Windows for Enabling, Accelerating, and Uplifting Flo…* | [10.1002/cssc.201200766](https://doi.org/10.1002/cssc.201200766) |
| 300 | `holcombe2024sustainable` | 1 | 7 | Holcombe 2024 — *Sustainable and Energy-Efficient Production of Rare-Earth Metals vi…* | [10.1021/acssuschemeng.3c07720](https://doi.org/10.1021/acssuschemeng.3c07720) |

```text
https://doi.org/10.1016/j.talanta.2020.121509
https://doi.org/10.1016/j.jhazmat.2024.133730
https://doi.org/10.1080/01496395.2025.2602158
https://doi.org/10.3390/rs15184597
https://doi.org/10.3390/met13030559
https://doi.org/10.1021/cr60286a001
https://doi.org/10.1021/acscentsci.7b00064
https://doi.org/10.1016/j.molliq.2021.116985
https://doi.org/10.4028/www.scientific.net/ssp.262.294
https://doi.org/10.1016/j.compchemeng.2023.108523
https://doi.org/10.1002/adfm.202402432
https://doi.org/10.1016/j.chroma.2020.461764
https://doi.org/10.1126/sciadv.abm3132
https://doi.org/10.1021/acssusresmgt.4c00122
https://doi.org/10.1021/acs.analchem.9b04176
https://doi.org/10.1016/j.ccr.2011.07.010
https://doi.org/10.1073/pnas.2210857119
https://doi.org/10.1038/s41598-024-62885-4
https://doi.org/10.1016/j.chemosphere.2022.134259
https://doi.org/10.1016/j.jct.2019.105955
https://doi.org/10.1016/j.jtice.2023.105095
https://doi.org/10.1016/j.talanta.2015.04.071
https://doi.org/10.1007/BF00322470
https://doi.org/10.1007/s10337-021-04025-y
https://doi.org/10.1021/cbe.4c00170
https://doi.org/10.1073/pnas.1722042115
https://doi.org/10.1186/s13065-023-01035-9
https://doi.org/10.1038/s41929-022-00744-z
https://doi.org/10.1016/b978-0-444-63456-6.50085-5
https://doi.org/10.1007/s00244-004-0223-9
https://doi.org/10.1016/j.compchemeng.2025.109061
https://doi.org/10.1007/s40831-016-0045-9
https://doi.org/10.1016/j.hydromet.2025.106514
https://doi.org/10.1021/acs.analchem.4c01028
https://doi.org/10.1016/j.cherd.2019.11.027
https://doi.org/10.1021/acs.chemrev.5c00103
https://doi.org/10.1007/s11274-020-02821-6
https://doi.org/10.1042/BJ20070255
https://doi.org/10.1111/j.1530-9290.2011.00342.x
https://doi.org/10.1039/d2nj05314d
https://doi.org/10.1179/imr.1992.37.1.197
https://doi.org/10.1007/s12532-011-0026-8
https://doi.org/10.1515/pac-2014-0718
https://doi.org/10.1021/acs.est.5c09617
https://doi.org/10.1016/j.seppur.2025.132426
https://doi.org/10.1021/acs.jcim.3c01250
https://doi.org/10.1007/s00253-021-11386-9
https://doi.org/10.1016/j.jre.2024.01.012
https://doi.org/10.1002/cssc.201200766
https://doi.org/10.1021/acssuschemeng.3c07720
```

## Batch 7 of 10

| # | Key | Cites | Ch | Source | DOI |
|---:|---|---:|---|---|---|
| 301 | `honaker2018conception` | 1 | 17 | Honaker 2018 — *Conception of an integrated flowsheet for rare earth elements recov…* | [10.1016/j.mineng.2018.04.005](https://doi.org/10.1016/j.mineng.2018.04.005) |
| 302 | `hou2024adsorption` | 1 | 8 | Xu 2024 — *Study of the Adsorption and Separation Behavior of Scandium and Zir…* | [10.3390/toxics12050350](https://doi.org/10.3390/toxics12050350) |
| 303 | `hu2020synthesis` | 1 | 6 | Hu 2020 — *Synthesis of rare earth tailing-based geopolymer for efficiently im…* | [10.1016/j.conbuildmat.2020.119273](https://doi.org/10.1016/j.conbuildmat.2020.119273) |
| 304 | `hubbs2020deep` | 1 | 18 | Hubbs 2020 — *A deep reinforcement learning approach for chemical production sche…* | [10.1016/j.compchemeng.2020.106982](https://doi.org/10.1016/j.compchemeng.2020.106982) |
| 305 | `indelicato2021approaches` | 1 | 19 | Indelicato 2021 — *Recent Approaches for Chemical Speciation and Analysis by Electrosp…* | [10.3389/fchem.2020.625945](https://doi.org/10.3389/fchem.2020.625945) |
| 306 | `innocenzi2018treatment` | 1 | 13 | Innocenzi 2018 — *Treatment of WEEE Industrial Wastewaters: Removal of Yttrium and Zi…* | [10.1016/j.wasman.2017.12.018](https://doi.org/10.1016/j.wasman.2017.12.018) |
| 307 | `ipcc2021physical` | 1 | 7 | 2021 — *Climate Change 2021 -- The Physical Science Basis* | [10.1017/9781009157896](https://doi.org/10.1017/9781009157896) |
| 308 | `ivanov2019siderophore` | 1 | 22 | Ivanov 2019 — *Siderophore-inspired chelator hijacks uranium from aqueous medium* | [10.1038/s41467-019-08758-1](https://doi.org/10.1038/s41467-019-08758-1) |
| 309 | `jin2018life` | 1 | 20 | Jin 2018 — *Life Cycle Assessment of Neodymium-Iron-Boron Magnet-to-Magnet Recy…* | [10.1021/acs.est.7b05442](https://doi.org/10.1021/acs.est.7b05442) |
| 310 | `jindra2018developing` | 1 | 5 | Idaho National Laboratory (INL) 2016 — *Developing a Scalable System for Biorecovery of Critical Materials…* | [10.2172/1504923](https://doi.org/10.2172/1504923) |
| 311 | `johnson2023size` | 1 | 10 | Johnson 2023 — *Size Selective Ligand Tug of War Strategy to Separate Rare Earth El…* | [10.1021/jacsau.2c00671](https://doi.org/10.1021/jacsau.2c00671) |
| 312 | `jordens2013processing` | 1 | 5 | Jordens 2014 — *Processing a rare earth mineral deposit using gravity and magnetic…* | [10.1016/j.mineng.2013.09.011](https://doi.org/10.1016/j.mineng.2013.09.011) |
| 313 | `joshi2025bioleaching` | 1 | 5 | Joshi 2025 — *Bioleaching for the recovery of rare earth elements from industrial…* | [10.1016/j.resconrec.2025.108129](https://doi.org/10.1016/j.resconrec.2025.108129) |
| 314 | `karati2025rare` | 1 | 20 | Karati 2025 — *Rare earth metals production using alternative feedstock that elimi…* | [10.1038/s41467-025-59468-w](https://doi.org/10.1038/s41467-025-59468-w) |
| 315 | `karnes2016geometric` | 1 | 14 | Karnes 2016 — *Geometric and energetic considerations of surface fluctuations duri…* | [10.1063/1.4954331](https://doi.org/10.1063/1.4954331) |
| 316 | `karniadakis2021physics` | 1 | 18 | Karniadakis 2021 — *Physics-informed machine learning* | [10.1038/s42254-021-00314-5](https://doi.org/10.1038/s42254-021-00314-5) |
| 317 | `kee2020development` | 1 | 8 | Kee 2020 — *Recent development of unconventional aqueous biphasic system: chara…* | [10.1080/07388551.2020.1747388](https://doi.org/10.1080/07388551.2020.1747388) |
| 318 | `keim2019production` | 1 | 17 | Keim 2019 — *Production of Salable Rare Earths Products from Coal and Coal Bypro…* | [10.2172/1569277](https://doi.org/10.2172/1569277) |
| 319 | `kemperman1996stability` | 1 | 13 | Kemperman 1996 — *Stability of Supported Liquid Membranes: State of the Art* | [10.1080/01496399608000824](https://doi.org/10.1080/01496399608000824) |
| 320 | `khan2019rare` | 1 | 19 | Khan 2018 — *Rare Earth Luminescence: Electronic Spectroscopy and Applications* | [10.1007/978-3-319-92955-2_10](https://doi.org/10.1007/978-3-319-92955-2_10) |
| 321 | `kim2012fluorescent` | 1 | 9 | Kim 2012 — *Fluorescent and colorimetric sensors for detection of lead, cadmium…* | [10.1039/c1cs15245a](https://doi.org/10.1039/c1cs15245a) |
| 322 | `kisala1987sequential` | 1 | 17 | Kisala 1987 — *Sequential modular and simultaneous modular strategies for process…* | [10.1016/0098-1354(87)87003-5](https://doi.org/10.1016/0098-1354(87)87003-5) |
| 323 | `klise2019parmest` | 1 | 17 | Klise 2019 — *Parmest: Parameter Estimation Via Pyomo* | [10.1016/b978-0-12-818597-1.50007-2](https://doi.org/10.1016/b978-0-12-818597-1.50007-2) |
| 324 | `kubota1995extraction` | 1 | 15 | Kubota 1995 — *Extraction Kinetics of Rare Earth Metals with 2-Ethylhexyl Phosphon…* | [10.1080/01496399508013891](https://doi.org/10.1080/01496399508013891) |
| 325 | `kujawa2023membrane` | 1 | 13 | Kujawa 2023 — *On Membrane-Based Approaches for Rare Earths Separation and Extract…* | [10.1016/j.ccr.2023.215340](https://doi.org/10.1016/j.ccr.2023.215340) |
| 326 | `laliwala2024design` | 1 | 17 | Laliwala 2024 — *Design and Optimization of Processes for Recovering Rare Earth Elem…* | [10.69997/sct.123161](https://doi.org/10.69997/sct.123161) |
| 327 | `laliwala2025optimization` | 1 | 17 | Laliwala 2025 — *An Optimization-Based Law of Mass Action Precipitation/Dissolution…* | [10.69997/sct.132742](https://doi.org/10.69997/sct.132742) |
| 328 | `laliwala2026design` | 1 | 17 | Laliwala 2026 — *Design and optimization of processes for recovering rare earth elem…* | [10.1002/aic.70208](https://doi.org/10.1002/aic.70208) |
| 329 | `laub2025ligand` | 1 | 18 | Laub 2025 — *Ligand design for 227 Ac extraction by active learning and molecula…* | [10.1039/d5dd00007f](https://doi.org/10.1039/d5dd00007f) |
| 330 | `li2020role` | 1 | 6 | Li 2020 — *The role of clay minerals in formation of the regolith-hosted heavy…* | [10.2138/am-2020-7061](https://doi.org/10.2138/am-2020-7061) |
| 331 | `li2021nonaqueous` | 1 | 14 | Li 2021 — *Nonaqueous Solvent Extraction for Enhanced Metal Separations: Conce…* | [10.1021/acs.iecr.1c02287](https://doi.org/10.1021/acs.iecr.1c02287) |
| 332 | `li2023extraction` | 1 | — | Li 2023 — *A Review on the Extraction and Recovery of Critical Metals Using Mo…* | [10.1016/j.jece.2023.109746](https://doi.org/10.1016/j.jece.2023.109746) |
| 333 | `li2024thermodynamic` | 1 | 8 | Ghosh 2025 — *Thermodynamic Insights into Polyelectrolyte Complexation: A Theoret…* | [10.1063/5.0250546](https://doi.org/10.1063/5.0250546) |
| 334 | `li2025extraction` | 1 | 3 | Li 2025 — *Extraction of Rare Earths from NdFeB Acid Leachate Using Pulsed Dis…* | [10.1080/07366299.2025.2508300](https://doi.org/10.1080/07366299.2025.2508300) |
| 335 | `li2025prediction` | 1 | 18 | Li 2025 — *Prediction of Actinide–Ligand Complex Stability Constants by Machin…* | [10.1021/acs.jpca.5c01743](https://doi.org/10.1021/acs.jpca.5c01743) |
| 336 | `liao2024research` | 1 | — | Liao 2024 — *Research Status of Electrolytic Preparation of Rare Earth Metals an…* | [10.3390/met14040407](https://doi.org/10.3390/met14040407) |
| 337 | `lin1995supercritical` | 1 | 13 | Lin 1994 — *Supercritical Fluid Extraction of Lanthanides with Fluorinated β-Di…* | [10.1021/ac00085a008](https://doi.org/10.1021/ac00085a008) |
| 338 | `lin2019intrinsically` | 1 | 8 | Lin 2019 — *Intrinsically disordered proteins access a range of hysteretic phas…* | [10.1126/sciadv.aax5177](https://doi.org/10.1126/sciadv.aax5177) |
| 339 | `lin2024situ` | 1 | 19 | Lin 2023 — *Review on in situ Isotopic Analysis by LA-MC-ICP-MS* | [10.1007/s12583-023-2002-4](https://doi.org/10.1007/s12583-023-2002-4) |
| 340 | `liu2017retrosynthetic` | 1 | 18 | Liu 2017 — *Retrosynthetic Reaction Prediction Using Neural Sequence-to-Sequenc…* | [10.1021/acscentsci.7b00303](https://doi.org/10.1021/acscentsci.7b00303) |
| 341 | `liu2021theoretical` | 1 | 16 | Peng 2021 — *Theoretical Elucidation of Rare Earth Extraction and Separation by…* | [10.1016/j.jre.2020.09.013](https://doi.org/10.1016/j.jre.2020.09.013) |
| 342 | `liu2022biogeochemical` | 1 | 6 | Liu 2022 — *Biogeochemical cycles of nutrients, rare earth elements (REEs) and…* | [10.1016/j.scitotenv.2021.152075](https://doi.org/10.1016/j.scitotenv.2021.152075) |
| 343 | `liu2024mechanism` | 1 | 7 | Liu 2024 — *Mechanism and Experimental Study on the Recovery of Rare Earth Elem…* | [10.3390/ma17235807](https://doi.org/10.3390/ma17235807) |
| 344 | `liu2025mechanism` | 1 | 7 | Liu 2025 — *Mechanism and experimental study on the recovery of rare earth elem…* | [10.1016/j.ijrmhm.2024.106943](https://doi.org/10.1016/j.ijrmhm.2024.106943) |
| 345 | `long2010principal` | 1 | 7 | Long 2010 — *The principal rare earth elements deposits of the United States---A…* | [10.3133/sir20105220](https://doi.org/10.3133/sir20105220) |
| 346 | `lorenz2023recovery` | 1 | 7 | Böhm 2023 — *Recovery of rare earth elements from NdFeB magnets by chlorination…* | [10.3390/pr11020577](https://doi.org/10.3390/pr11020577) |
| 347 | `lu2025separation` | 1 | 11 | Lu 2026 — *Separation and recovery of strategic metals by solvent extraction b…* | [10.1016/j.seppur.2025.135433](https://doi.org/10.1016/j.seppur.2025.135433) |
| 348 | `luo2022development` | 1 | 6 | Luo 2022 — *Review on the Development and Utilization of Ionic Rare Earth Ore* | [10.3390/min12050554](https://doi.org/10.3390/min12050554) |
| 349 | `ma2000lanthanide` | 1 | 8 | Ma 2000 — *Lanthanide Ions Bind Specifically to an Added “EF-Hand” and Orient…* | [10.1006/jmre.2000.2172](https://doi.org/10.1006/jmre.2000.2172) |
| 350 | `ma2018neural` | 1 | 18 | Ma 2018 — *Neural Network Modeling for the Extraction of Rare Earth Elements f…* | [10.3390/met8040267](https://doi.org/10.3390/met8040267) |

```text
https://doi.org/10.1016/j.mineng.2018.04.005
https://doi.org/10.3390/toxics12050350
https://doi.org/10.1016/j.conbuildmat.2020.119273
https://doi.org/10.1016/j.compchemeng.2020.106982
https://doi.org/10.3389/fchem.2020.625945
https://doi.org/10.1016/j.wasman.2017.12.018
https://doi.org/10.1017/9781009157896
https://doi.org/10.1038/s41467-019-08758-1
https://doi.org/10.1021/acs.est.7b05442
https://doi.org/10.2172/1504923
https://doi.org/10.1021/jacsau.2c00671
https://doi.org/10.1016/j.mineng.2013.09.011
https://doi.org/10.1016/j.resconrec.2025.108129
https://doi.org/10.1038/s41467-025-59468-w
https://doi.org/10.1063/1.4954331
https://doi.org/10.1038/s42254-021-00314-5
https://doi.org/10.1080/07388551.2020.1747388
https://doi.org/10.2172/1569277
https://doi.org/10.1080/01496399608000824
https://doi.org/10.1007/978-3-319-92955-2_10
https://doi.org/10.1039/c1cs15245a
https://doi.org/10.1016/0098-1354(87)87003-5
https://doi.org/10.1016/b978-0-12-818597-1.50007-2
https://doi.org/10.1080/01496399508013891
https://doi.org/10.1016/j.ccr.2023.215340
https://doi.org/10.69997/sct.123161
https://doi.org/10.69997/sct.132742
https://doi.org/10.1002/aic.70208
https://doi.org/10.1039/d5dd00007f
https://doi.org/10.2138/am-2020-7061
https://doi.org/10.1021/acs.iecr.1c02287
https://doi.org/10.1016/j.jece.2023.109746
https://doi.org/10.1063/5.0250546
https://doi.org/10.1080/07366299.2025.2508300
https://doi.org/10.1021/acs.jpca.5c01743
https://doi.org/10.3390/met14040407
https://doi.org/10.1021/ac00085a008
https://doi.org/10.1126/sciadv.aax5177
https://doi.org/10.1007/s12583-023-2002-4
https://doi.org/10.1021/acscentsci.7b00303
https://doi.org/10.1016/j.jre.2020.09.013
https://doi.org/10.1016/j.scitotenv.2021.152075
https://doi.org/10.3390/ma17235807
https://doi.org/10.1016/j.ijrmhm.2024.106943
https://doi.org/10.3133/sir20105220
https://doi.org/10.3390/pr11020577
https://doi.org/10.1016/j.seppur.2025.135433
https://doi.org/10.3390/min12050554
https://doi.org/10.1006/jmre.2000.2172
https://doi.org/10.3390/met8040267
```

## Batch 8 of 10

| # | Key | Cites | Ch | Source | DOI |
|---:|---|---:|---|---|---|
| 351 | `maurice2021first` | 1 | — | Maurice 2021 — *First online X-ray fluorescence characterization of liquid-liquid e…* | [10.1002/nano.202100133](https://doi.org/10.1002/nano.202100133) |
| 352 | `meng2024efficient` | 1 | 10 | Ghaly 2024 — *Efficient Separation of Cerium from Rare Earth Elements and Major I…* | [10.1016/j.jece.2024.114588](https://doi.org/10.1016/j.jece.2024.114588) |
| 353 | `miller2018next` | 1 | 17 | Miller 2018 — *Next Generation Multi-Scale Process Systems Engineering Framework* | [10.1016/b978-0-444-64241-7.50363-3](https://doi.org/10.1016/b978-0-444-64241-7.50363-3) |
| 354 | `mohdee2023applicability` | 1 | 13 | Mohdee 2023 — *Applicability of HFSLM for Nd(III) Recovery via Organophosphorus Ca…* | [10.1007/s11814-022-1369-8](https://doi.org/10.1007/s11814-022-1369-8) |
| 355 | `moldoveanu2023cerium` | 1 | 10 | Moldoveanu 2023 — *Cerium Removal from a Mixed Rare Earth Sulfate Solution by Oxidatio…* | [10.1007/978-3-031-38141-6_21](https://doi.org/10.1007/978-3-031-38141-6_21) |
| 356 | `moldoveanu2025separation` | 1 | 10 | Moldoveanu 2025 — *Separation of cerium from solution by oxidative precipitation with…* | [10.1016/j.hydromet.2024.106417](https://doi.org/10.1016/j.hydromet.2024.106417) |
| 357 | `momen2019extraction` | 1 | 6 | Momen 2019 — *Extraction Chromatographic Materials for Clean Hydrometallurgical S…* | [10.1021/acs.iecr.9b04528](https://doi.org/10.1021/acs.iecr.9b04528) |
| 358 | `mustafina2006cloud` | 1 | 8 | Mustafina 2006 — *Cloud point extraction of lanthanide(III) ions via use of Triton X-…* | [10.1016/j.talanta.2005.06.011](https://doi.org/10.1016/j.talanta.2005.06.011) |
| 359 | `nakashima2019biomolecular` | 1 | 8 | Nakashima 2019 — *Biomolecular Chemistry in Liquid Phase Separated Compartments* | [10.3389/fmolb.2019.00021](https://doi.org/10.3389/fmolb.2019.00021) |
| 360 | `nelson2020high` | 1 | — | Nelson 2020 — *High-throughput screening for discovery of benchtop separations sys…* | [10.1038/s42004-019-0253-x](https://doi.org/10.1038/s42004-019-0253-x) |
| 361 | `nguyen2011characterization` | 1 | 11 | Nguyen 2011 — *Characterization and Emulsification Properties of Rhamnolipid and S…* | [10.3390/ijms12021232](https://doi.org/10.3390/ijms12021232) |
| 362 | `ni2023sustainable` | 1 | 5 | Ni 2023 — *A sustainable strategy for targeted extraction of thorium from radi…* | [10.1016/j.jhazmat.2023.132465](https://doi.org/10.1016/j.jhazmat.2023.132465) |
| 363 | `nili2025reclaiming` | 1 | 23 | Nili 2025 — *Reclaiming Value from Waste: A Techno-Economic Evaluation of Rare E…* | [10.1021/acssusresmgt.5c00353](https://doi.org/10.1021/acssusresmgt.5c00353) |
| 364 | `oconnelldanes2024simple` | 1 | 13 | O’Connell-Danes 2024 — *A Simple Supramolecular Approach to Recycling Rare Earth Elements* | [10.1021/acssuschemeng.4c03063](https://doi.org/10.1021/acssuschemeng.4c03063) |
| 365 | `ojima2018recovering` | 1 | 11 | Ojima 2019 — *Recovering Metals from Aqueous Solutions by Biosorption onto Phosph…* | [10.1038/s41598-018-36306-2](https://doi.org/10.1038/s41598-018-36306-2) |
| 366 | `okamura2020progress` | 1 | 11 | Okamura 2020 — *Recent Progress in Ionic Liquid Extraction for the Separation of Ra…* | [10.2116/analsci.20sar11](https://doi.org/10.2116/analsci.20sar11) |
| 367 | `opare2021comparative` | 1 | 18 | Opare 2021 — *A comparative state-of-technology review and future directions for…* | [10.1016/j.rser.2021.110917](https://doi.org/10.1016/j.rser.2021.110917) |
| 368 | `orefice2019selective` | 1 | 9 | Orefice 2019 — *Selective Roasting of Nd–Fe‒B Permanent Magnets as a Pretreatment S…* | [10.1007/s40831-019-00259-1](https://doi.org/10.1007/s40831-019-00259-1) |
| 369 | `oshima2025machine` | 1 | 18 | Oshima 2025 — *Machine Learning Prediction of Au(III) Extractability of Various Or…* | [10.1021/acssuschemeng.5c01941](https://doi.org/10.1021/acssuschemeng.5c01941) |
| 370 | `osman2019characterization` | 1 | 11 | Osman 2019 — *Characterization of Aspergillus niger Siderophore that Mediates Bio…* | [10.1007/s11274-019-2666-1](https://doi.org/10.1007/s11274-019-2666-1) |
| 371 | `papadopoulou2025extraction` | 1 | 14 | Papadopoulou 2025 — *Extraction of rare earth ions using thermomorphic ionic liquid: In…* | [10.1016/j.seppur.2024.129686](https://doi.org/10.1016/j.seppur.2024.129686) |
| 372 | `park2017recovery` | 1 | 11 | Park 2017 — *Recovery of Rare Earth Elements from Low-Grade Feedstock Leachates…* | [10.1021/acs.est.7b02414](https://doi.org/10.1021/acs.est.7b02414) |
| 373 | `patcharawit2022comparative` | 1 | 20 | Patcharawit 2022 — *Comparative Study of Manufacturing NdFeB Magnet Wastes Recycling: O…* | [10.3390/recycling7050068](https://doi.org/10.3390/recycling7050068) |
| 374 | `pretorius2019fluorination` | 1 | 10 | Pretorius 2019 — *Fluorination of neodymium carbonate monohydrate with anhydrous hydr…* | [10.1039/C8RE00117K](https://doi.org/10.1039/C8RE00117K) |
| 375 | `prommis2025software` | 1 | 17 | Beattie 2025 — *Process Optimization and Modeling for Minerals Sustainability (PrOM…* | [10.11578/dc.20250729.4](https://doi.org/10.11578/dc.20250729.4) |
| 376 | `qin2023bridging` | 1 | 8 | Sing 2023 — *Bridging Field Theory and Ion Pairing in the Modeling of Polyelectr…* | [10.1021/acs.macromol.3c01020](https://doi.org/10.1021/acs.macromol.3c01020) |
| 377 | `ramasamy2017selective` | 1 | 8 | Giret 2017 — *Selective Separation and Preconcentration of Scandium with Mesoporo…* | [10.1021/acsami.7b13336](https://doi.org/10.1021/acsami.7b13336) |
| 378 | `ramos2025review` | 1 | 18 | Ramos 2025 — *A review of large language models and autonomous agents in chemistry* | [10.1039/d4sc03921a](https://doi.org/10.1039/d4sc03921a) |
| 379 | `reck2012challenges` | 1 | 20 | Reck 2012 — *Challenges in Metal Recycling* | [10.1126/science.1217501](https://doi.org/10.1126/science.1217501) |
| 380 | `ross2022large` | 1 | 18 | Ross 2022 — *Large-scale chemical language representations capture molecular str…* | [10.1038/s42256-022-00580-7](https://doi.org/10.1038/s42256-022-00580-7) |
| 381 | `saldana2022mineral` | 1 | 18 | Saldaña 2022 — *Mineral Leaching Modeling Through Machine Learning Algorithms − A R…* | [10.3389/feart.2022.816751](https://doi.org/10.3389/feart.2022.816751) |
| 382 | `schmitz2021generation` | 1 | 11 | Schmitz 2021 — *Generation of a Gluconobacter oxydans knockout collection for impro…* | [10.1038/s41467-021-27047-4](https://doi.org/10.1038/s41467-021-27047-4) |
| 383 | `schmitz2022lanmodulin` | 1 | 8 | Gutenthaler 2022 — *Lanmodulin peptides - unravelling the binding of the EF-Hand loop s…* | [10.1039/D2QI00933A](https://doi.org/10.1039/D2QI00933A) |
| 384 | `schmitz2025high` | 1 | 11 | Schmitz 2025 — *High Efficiency Rare Earth Element Bioleaching with Systems Biology…* | [10.1038/s42003-025-08109-5](https://doi.org/10.1038/s42003-025-08109-5) |
| 385 | `schramm2016use` | 1 | 19 | Schramm 2016 — *Use of X-ray Fluorescence Analysis for the Determination of Rare Ea…* | [10.1515/psr-2016-0061](https://doi.org/10.1515/psr-2016-0061) |
| 386 | `schwaller2021prediction` | 1 | 18 | Schwaller 2021 — *Prediction of chemical reaction yields using deep learning* | [10.1088/2632-2153/abc81d](https://doi.org/10.1088/2632-2153/abc81d) |
| 387 | `schweidtmann2021machine` | 1 | 18 | Schweidtmann 2021 — *Machine Learning in Chemical Engineering: A Perspective* | [10.1002/cite.202100083](https://doi.org/10.1002/cite.202100083) |
| 388 | `shakiba2023application` | 1 | 11 | Shakiba 2023 — *Application of deep eutectic solvents (DESs) as a green lixiviant f…* | [10.1016/j.jece.2023.110777](https://doi.org/10.1016/j.jece.2023.110777) |
| 389 | `sharma2020library` | 1 | 19 | Sharma 2020 — *Library of UV-Visible Absorption Spectra of Rare Earth Orthophospha…* | [10.3390/cryst10070593](https://doi.org/10.3390/cryst10070593) |
| 390 | `sharov2024specific` | 1 | 14 | Sharov 2024 — *Specific features of temperature influence on the extraction of Am(…* | [10.1007/s10967-024-09902-y](https://doi.org/10.1007/s10967-024-09902-y) |
| 391 | `shaw1997isolated` | 1 | 8 | Wójcik 1997 — *Isolated Calcium-Binding Loops of EF-Hand Proteins Can Dimerize To…* | [10.1021/bi961821c](https://doi.org/10.1021/bi961821c) |
| 392 | `silachyov2016rare` | 1 | 19 | Silachyov 2016 — *Rare Earths Analysis of Rock Samples by Instrumental Neutron Activa…* | [10.1007/s10967-016-4903-5](https://doi.org/10.1007/s10967-016-4903-5) |
| 393 | `sim2024electrodialysis` | 1 | 12 | Sim 2024 — *Recent advances in electrodialysis technologies for recovering crit…* | [10.1016/j.cej.2024.154640](https://doi.org/10.1016/j.cej.2024.154640) |
| 394 | `song2021extraction` | 1 | 13 | Song 2021 — *Extraction of selected rare earth elements from anthracite acid min…* | [10.1016/j.jre.2020.02.007](https://doi.org/10.1016/j.jre.2020.02.007) |
| 395 | `sorin2005rejection` | 1 | 13 | Sorin 2005 — *Rejection of Gd(III) by Nanofiltration Assisted by Complexation on…* | [10.1016/j.memsci.2005.05.022](https://doi.org/10.1016/j.memsci.2005.05.022) |
| 396 | `spadina2019synergistic` | 1 | 14 | Špadina 2019 — *Synergistic Solvent Extraction Is Driven by Entropy* | [10.1021/acsnano.9b07605](https://doi.org/10.1021/acsnano.9b07605) |
| 397 | `sprakel2019improving` | 1 | 14 | Sprakel 2019 — *Improving understanding of solvent effects on intermolecular intera…* | [10.1016/j.jiec.2018.12.038](https://doi.org/10.1016/j.jiec.2018.12.038) |
| 398 | `sree2023gravity` | 1 | 11 | Sree 2024 — *Gravity-Driven Separation for Enrichment of Rare Earth Elements Usi…* | [10.1021/acsabm.3c01280](https://doi.org/10.1021/acsabm.3c01280) |
| 399 | `sreedhar2014evaluation` | 1 | 6 | Sreedhar 2014 — *Evaluation of tertiary pyridine resin for the separation of lanthan…* | [10.1002/jssc.201400516](https://doi.org/10.1002/jssc.201400516) |
| 400 | `sreedhar2014simulated` | 1 | 6 | Sreedhar 2014 — *Simulated moving bed chromatography designs for lanthanide and acti…* | [10.1016/j.seppur.2014.08.006](https://doi.org/10.1016/j.seppur.2014.08.006) |

```text
https://doi.org/10.1002/nano.202100133
https://doi.org/10.1016/j.jece.2024.114588
https://doi.org/10.1016/b978-0-444-64241-7.50363-3
https://doi.org/10.1007/s11814-022-1369-8
https://doi.org/10.1007/978-3-031-38141-6_21
https://doi.org/10.1016/j.hydromet.2024.106417
https://doi.org/10.1021/acs.iecr.9b04528
https://doi.org/10.1016/j.talanta.2005.06.011
https://doi.org/10.3389/fmolb.2019.00021
https://doi.org/10.1038/s42004-019-0253-x
https://doi.org/10.3390/ijms12021232
https://doi.org/10.1016/j.jhazmat.2023.132465
https://doi.org/10.1021/acssusresmgt.5c00353
https://doi.org/10.1021/acssuschemeng.4c03063
https://doi.org/10.1038/s41598-018-36306-2
https://doi.org/10.2116/analsci.20sar11
https://doi.org/10.1016/j.rser.2021.110917
https://doi.org/10.1007/s40831-019-00259-1
https://doi.org/10.1021/acssuschemeng.5c01941
https://doi.org/10.1007/s11274-019-2666-1
https://doi.org/10.1016/j.seppur.2024.129686
https://doi.org/10.1021/acs.est.7b02414
https://doi.org/10.3390/recycling7050068
https://doi.org/10.1039/C8RE00117K
https://doi.org/10.11578/dc.20250729.4
https://doi.org/10.1021/acs.macromol.3c01020
https://doi.org/10.1021/acsami.7b13336
https://doi.org/10.1039/d4sc03921a
https://doi.org/10.1126/science.1217501
https://doi.org/10.1038/s42256-022-00580-7
https://doi.org/10.3389/feart.2022.816751
https://doi.org/10.1038/s41467-021-27047-4
https://doi.org/10.1039/D2QI00933A
https://doi.org/10.1038/s42003-025-08109-5
https://doi.org/10.1515/psr-2016-0061
https://doi.org/10.1088/2632-2153/abc81d
https://doi.org/10.1002/cite.202100083
https://doi.org/10.1016/j.jece.2023.110777
https://doi.org/10.3390/cryst10070593
https://doi.org/10.1007/s10967-024-09902-y
https://doi.org/10.1021/bi961821c
https://doi.org/10.1007/s10967-016-4903-5
https://doi.org/10.1016/j.cej.2024.154640
https://doi.org/10.1016/j.jre.2020.02.007
https://doi.org/10.1016/j.memsci.2005.05.022
https://doi.org/10.1021/acsnano.9b07605
https://doi.org/10.1016/j.jiec.2018.12.038
https://doi.org/10.1021/acsabm.3c01280
https://doi.org/10.1002/jssc.201400516
https://doi.org/10.1016/j.seppur.2014.08.006
```

## Batch 9 of 10

| # | Key | Cites | Ch | Source | DOI |
|---:|---|---:|---|---|---|
| 401 | `stojkovic2024recovery` | 1 | 5 | Stojković 2024 — *Recovery of Rare Earth Elements from Coal Fly and Bottom Ashes by U…* | [10.3390/met14040371](https://doi.org/10.3390/met14040371) |
| 402 | `suli2017rare` | 1 | — | Suli 2017 — *A review of rare earth mineral processing technology* | [10.3329/cerb.v19i0.33773](https://doi.org/10.3329/cerb.v19i0.33773) |
| 403 | `szczesniak2021alkyl` | 1 | 10 | Virtanen 2021 — *Alkyl-Substituted Aminobis(phosphonates)—Efficient Precipitating Ag…* | [10.1021/acsomega.1c02982](https://doi.org/10.1021/acsomega.1c02982) |
| 404 | `tanaka2013recycling` | 1 | 7 | Tanaka 2013 — *Recycling of rare earths from scrap* | [10.1016/B978-0-444-59536-2.00002-7](https://doi.org/10.1016/B978-0-444-59536-2.00002-7) |
| 405 | `tarka2025advances` | 1 | 17 | Tarka 2025 — *Advances in Modeling Capabilities for Critical Mineral Separation T…* | [10.2172/2571193](https://doi.org/10.2172/2571193) |
| 406 | `teng2020multivariate` | 1 | 19 | Teng 2020 — *Multivariate Statistical Analysis on a SEM/EDS Phase Map of Rare Ea…* | [10.1155/2020/2134516](https://doi.org/10.1155/2020/2134516) |
| 407 | `tunsu2016hydrometallurgical` | 1 | 7 | Tunsu 2016 — *Hydrometallurgical processes for the recovery of metals from WEEE* | [10.1016/B978-0-12-803363-0.00006-7](https://doi.org/10.1016/B978-0-12-803363-0.00006-7) |
| 408 | `turgeon2023simulation` | 1 | 16 | Turgeon 2023 — *Simulation of Solvent Extraction Circuits for the Separation of Rar…* | [10.3390/min13060714](https://doi.org/10.3390/min13060714) |
| 409 | `vandenbogaert2016photochemical` | 1 | 10 | Van den Bogaert 2016 — *Photochemical recovery of europium from non-aqueous solutions* | [10.1039/c6cp06329b](https://doi.org/10.1039/c6cp06329b) |
| 410 | `vazirihassas2022selective` | 1 | 10 | Vaziri Hassas 2023 — *Selective Precipitation of Rare Earth and Critical Elements from Ac…* | [10.1016/j.resconrec.2022.106654](https://doi.org/10.1016/j.resconrec.2022.106654) |
| 411 | `veerla2025investigation` | 1 | 13 | Veerla 2025 — *Investigation of rare earth element extraction from coal byproducts…* | [10.1016/j.hydromet.2025.106550](https://doi.org/10.1016/j.hydromet.2025.106550) |
| 412 | `verma2007high` | 1 | 19 | Verma 2007 — *High-Performance Liquid and Ion Chromatography: Separation and Quan…* | [10.1111/j.1751-908X.2007.00842.x](https://doi.org/10.1111/j.1751-908X.2007.00842.x) |
| 413 | `verma2024investigation` | 1 | 11 | Verma 2024 — *Investigation of Rare Earth Element Binding to a Surface-Bound Affi…* | [10.1021/acsami.3c17565](https://doi.org/10.1021/acsami.3c17565) |
| 414 | `vitova2024microbial` | 1 | 11 | Vítová 2024 — *Microbial Recovery of Rare Earth Elements from Various Waste Source…* | [10.1007/s11274-024-03974-4](https://doi.org/10.1007/s11274-024-03974-4) |
| 415 | `wachter2006implementation` | 1 | 17 | Wächter 2006 — *On the implementation of an interior-point filter line-search algor…* | [10.1007/s10107-004-0559-y](https://doi.org/10.1007/s10107-004-0559-y) |
| 416 | `walton2015use` | 1 | 20 | Walton 2015 — *The use of hydrogen to separate and recycle neodymium--iron--boron-…* | [10.1016/j.jclepro.2015.05.033](https://doi.org/10.1016/j.jclepro.2015.05.033) |
| 417 | `wang2017effects` | 1 | 5 | Wang 2017 — *Effects of organic acids on the leaching process of ion-adsorption…* | [10.1016/j.jre.2017.07.001](https://doi.org/10.1016/j.jre.2017.07.001) |
| 418 | `wang2022bayesian` | 1 | 18 | Wang 2022 — *Bayesian optimization for chemical products and functional materials* | [10.1016/j.coche.2021.100728](https://doi.org/10.1016/j.coche.2021.100728) |
| 419 | `wang2022pyomodoe` | 1 | 17 | Wang 2022 — *Pyomo.DOE : An open‐source package for model‐based design of experi…* | [10.1002/aic.17813](https://doi.org/10.1002/aic.17813) |
| 420 | `wang2025role` | 1 | 8 | Sathyavageeswaran 2025 — *Role of Charge Patterning and Hydrophobicity in Peptide-Based Compl…* | [10.1021/acs.biomac.5c00773](https://doi.org/10.1021/acs.biomac.5c00773) |
| 421 | `wu2018moleculenet` | 1 | 18 | Wu 2018 — *MoleculeNet: a benchmark for molecular machine learning* | [10.1039/c7sc02664a](https://doi.org/10.1039/c7sc02664a) |
| 422 | `wu2020trends` | 1 | 17 | Wu 2020 — *Trends and progress of the theory of countercurrent extraction and…* | [10.1360/ssc-2020-0134](https://doi.org/10.1360/ssc-2020-0134) |
| 423 | `wu2026swat` | 1 | 6 | Wu 2026 — *SWAT-WASP coupled modeling of ammonia nitrogen in rare earth mining…* | [10.2166/wst.2025.190](https://doi.org/10.2166/wst.2025.190) |
| 424 | `xia2024experimental` | 1 | 7 | Xue 2024 — *Experimental and mechanistic analysis of bastnaesite pelletization…* | [10.1007/s42461-024-01041-y](https://doi.org/10.1007/s42461-024-01041-y) |
| 425 | `xian2021retraction` | 1 | 22 | Xian 2021 — *Retraction: Glutarimidedioxime: A Complexing and Reducing Reagent f…* | [10.1002/anie.202605305](https://doi.org/10.1002/anie.202605305) |
| 426 | `xiao2016reduction` | 1 | 5 | Xiao 2016 — *Reduction leaching of rare earth from ion-adsorption type rare eart…* | [10.1016/s1002-0721(16)60115-1](https://doi.org/10.1016/s1002-0721(16)60115-1) |
| 427 | `xu2017microfluidic` | 1 | — | Xu 2017 — *Review of Microfluidic Liquid--Liquid Extractors* | [10.1021/acs.iecr.7b01712](https://doi.org/10.1021/acs.iecr.7b01712) |
| 428 | `xu2018micro` | 1 | 19 | Xu 2018 — *Micro- and Nanoscale Identification of Rare Earth Element–Mineral A…* | [10.1021/acsearthspacechem.8b00134](https://doi.org/10.1021/acsearthspacechem.8b00134) |
| 429 | `xu2019hierarchical` | 1 | 22 | Xu 2019 — *3D hierarchical porous amidoxime fibers speed up uranium extraction…* | [10.1039/c9ee00626e](https://doi.org/10.1039/c9ee00626e) |
| 430 | `yang2015component` | 1 | 17 | Yang 2015 — *Component content distribution profile control in rare earth counte…* | [10.1016/j.cjche.2014.09.046](https://doi.org/10.1016/j.cjche.2014.09.046) |
| 431 | `yang2016multiple` | 1 | 17 | Yang 2016 — *Multiple-model predictive control for component content of CePr/Nd…* | [10.1016/j.ins.2016.04.031](https://doi.org/10.1016/j.ins.2016.04.031) |
| 432 | `yang2016separation` | 1 | 7 | Xu 2014 — *Separation of zirconium and hafnium: A review* | [10.1007/978-3-319-48765-6_53](https://doi.org/10.1007/978-3-319-48765-6_53) |
| 433 | `yang2020hybrid` | 1 | 18 | Yang 2020 — *Hybrid Modeling in the Era of Smart Manufacturing* | [10.1016/j.compchemeng.2020.106874](https://doi.org/10.1016/j.compchemeng.2020.106874) |
| 434 | `yang2021recovery` | 1 | 7 | Yin 2021 — *Recovery and Separation of Rare Earth Elements by Molten Salt Elect…* | [10.1007/s12613-020-2228-4](https://doi.org/10.1007/s12613-020-2228-4) |
| 435 | `yang2026machine` | 1 | 18 | Yang 2026 — *Machine-Learning-Guided Ligand Optimization for Americium/Europium…* | [10.1021/acs.inorgchem.6c01405](https://doi.org/10.1021/acs.inorgchem.6c01405) |
| 436 | `yuan2025analysis` | 1 | 6 | Yuan 2025 — *Analysis of Slope Stability in Ion-Adsorption Rare Earth Mine Under…* | [10.3390/app15126677](https://doi.org/10.3390/app15126677) |
| 437 | `zakotnik2009multiple` | 1 | 20 | Zakotnik 2009 — *Multiple recycling of NdFeB-type sintered magnets* | [10.1016/j.jallcom.2008.01.114](https://doi.org/10.1016/j.jallcom.2008.01.114) |
| 438 | `zhang2011literature` | 1 | 7 | Zhang 2011 — *A literature review of titanium metallurgical processes* | [10.1016/j.hydromet.2011.04.005](https://doi.org/10.1016/j.hydromet.2011.04.005) |
| 439 | `zhang2020hydrometallurgical` | 1 | — | Zhang 2020 — *Hydrometallurgical Recovery of Rare Earth Elements from NdFeB Perma…* | [10.3390/met10060841](https://doi.org/10.3390/met10060841) |
| 440 | `zhang2021high` | 1 | 19 | Xu 2021 — *High throughput online sequential extraction of natural rare earth…* | [10.1007/s11426-020-9928-6](https://doi.org/10.1007/s11426-020-9928-6) |
| 441 | `zhang2022ion` | 1 | 6 | Zhang 2022 — *Ion-adsorption type rare earth tailings for preparation of alkali-b…* | [10.1016/j.cemconcomp.2022.104768](https://doi.org/10.1016/j.cemconcomp.2022.104768) |
| 442 | `zhang2023separation` | 1 | 8 | Zhang 2023 — *Separation of Praseodymium and Neodymium from Heavy Rare Earth Elem…* | [10.1021/acs.iecr.3c01547](https://doi.org/10.1021/acs.iecr.3c01547) |
| 443 | `zhang2024variations` | 1 | 6 | Zhang 2024 — *Variations in pore structures and permeabilities of ion adsorption…* | [10.1016/j.hydromet.2024.106357](https://doi.org/10.1016/j.hydromet.2024.106357) |
| 444 | `zhao2010utilization` | 1 | 6 | Zhao 2010 — *The utilization of rare earth tailing for the production of glass–c…* | [10.1016/j.mseb.2010.02.019](https://doi.org/10.1016/j.mseb.2010.02.019) |
| 445 | `zhao2022selective` | 1 | 10 | Vaziri Hassas 2023 — *Selective Precipitation of Rare Earth and Critical Elements from Ac…* | [10.1016/j.resconrec.2022.106655](https://doi.org/10.1016/j.resconrec.2022.106655) |
| 446 | `zheng2019mechanism` | 1 | — | Xing 2020 — *Mechanism and application of the ore with chlorination treatment: A…* | [10.1016/j.mineng.2020.106404](https://doi.org/10.1016/j.mineng.2020.106404) |
| 447 | `zheng2023rare` | 1 | 11 | Zheng 2023 — *Rare Earth Elements Detoxification Mechanism in the Hyperaccumulato…* | [10.1016/j.jhazmat.2023.131254](https://doi.org/10.1016/j.jhazmat.2023.131254) |
| 448 | `zhong2022explainable` | 1 | 18 | Zhong 2022 — *Explainable machine learning in materials science* | [10.1038/s41524-022-00884-7](https://doi.org/10.1038/s41524-022-00884-7) |
| 449 | `zhou1996mathematical` | 1 | 7 | Zhou 1996 — *Mathematical modeling of fluidized-bed chlorination of rutile* | [10.1002/aic.690421110](https://doi.org/10.1002/aic.690421110) |
| 450 | `zhu2022flying` | 1 | 19 | Zhu 2022 — *Flying Blind: Geochemical Modeling and Thermodynamic Data Files* | [10.1111/gwat.13223](https://doi.org/10.1111/gwat.13223) |

```text
https://doi.org/10.3390/met14040371
https://doi.org/10.3329/cerb.v19i0.33773
https://doi.org/10.1021/acsomega.1c02982
https://doi.org/10.1016/B978-0-444-59536-2.00002-7
https://doi.org/10.2172/2571193
https://doi.org/10.1155/2020/2134516
https://doi.org/10.1016/B978-0-12-803363-0.00006-7
https://doi.org/10.3390/min13060714
https://doi.org/10.1039/c6cp06329b
https://doi.org/10.1016/j.resconrec.2022.106654
https://doi.org/10.1016/j.hydromet.2025.106550
https://doi.org/10.1111/j.1751-908X.2007.00842.x
https://doi.org/10.1021/acsami.3c17565
https://doi.org/10.1007/s11274-024-03974-4
https://doi.org/10.1007/s10107-004-0559-y
https://doi.org/10.1016/j.jclepro.2015.05.033
https://doi.org/10.1016/j.jre.2017.07.001
https://doi.org/10.1016/j.coche.2021.100728
https://doi.org/10.1002/aic.17813
https://doi.org/10.1021/acs.biomac.5c00773
https://doi.org/10.1039/c7sc02664a
https://doi.org/10.1360/ssc-2020-0134
https://doi.org/10.2166/wst.2025.190
https://doi.org/10.1007/s42461-024-01041-y
https://doi.org/10.1002/anie.202605305
https://doi.org/10.1016/s1002-0721(16)60115-1
https://doi.org/10.1021/acs.iecr.7b01712
https://doi.org/10.1021/acsearthspacechem.8b00134
https://doi.org/10.1039/c9ee00626e
https://doi.org/10.1016/j.cjche.2014.09.046
https://doi.org/10.1016/j.ins.2016.04.031
https://doi.org/10.1007/978-3-319-48765-6_53
https://doi.org/10.1016/j.compchemeng.2020.106874
https://doi.org/10.1007/s12613-020-2228-4
https://doi.org/10.1021/acs.inorgchem.6c01405
https://doi.org/10.3390/app15126677
https://doi.org/10.1016/j.jallcom.2008.01.114
https://doi.org/10.1016/j.hydromet.2011.04.005
https://doi.org/10.3390/met10060841
https://doi.org/10.1007/s11426-020-9928-6
https://doi.org/10.1016/j.cemconcomp.2022.104768
https://doi.org/10.1021/acs.iecr.3c01547
https://doi.org/10.1016/j.hydromet.2024.106357
https://doi.org/10.1016/j.mseb.2010.02.019
https://doi.org/10.1016/j.resconrec.2022.106655
https://doi.org/10.1016/j.mineng.2020.106404
https://doi.org/10.1016/j.jhazmat.2023.131254
https://doi.org/10.1038/s41524-022-00884-7
https://doi.org/10.1002/aic.690421110
https://doi.org/10.1111/gwat.13223
```

## Batch 10 of 10

| # | Key | Cites | Ch | Source | DOI |
|---:|---|---:|---|---|---|
| 451 | `zhu2023supercritical` | 1 | 13 | Zhu 2023 — *Supercritical carbon dioxide/nitrogen/air extraction with multistag…* | [10.1039/D2SU00033D](https://doi.org/10.1039/D2SU00033D) |
| 452 | `zinoveva2024extraction` | 1 | 11 | Zinov’eva 2024 — *Extraction of Rare Earth Elements from Nitrate Solutions by Hydroph…* | [10.1021/acs.iecr.4c03336](https://doi.org/10.1021/acs.iecr.4c03336) |

```text
https://doi.org/10.1039/D2SU00033D
https://doi.org/10.1021/acs.iecr.4c03336
```

## Cited, but with no DOI to fetch

These 21 cannot be collected by DOI. Most are standards, agency reports,
theses or software documentation; the rest are old enough that no DOI was
ever registered. A recorded URL is given where there is one.

| Key | Cites | Ch | Source | Where |
|---|---:|---|---|---|
| `habashi1997handbook` | 7 | 7 | Habashi 1997 — *Handbook of Extractive Metallurgy* | Wiley-VCH |
| `usgs2020titanium` | 6 | 7 | Gambogi 2020 — *Titanium* | [link](https://pubs.usgs.gov/myb/vol1/2020/myb1-2020-titanium.pdf) |
| `castor2006rare` | 4 | 5,7,10 | Castor 2006 — *Rare Earth Elements* | Industrial Minerals and Rocks |
| `connelly2005nomenclature` | 4 | 1 | Connelly 2005 — *Nomenclature of Inorganic Chemistry: IUPAC Recommendations 2005* | [link](https://iupac.org/wp-content/uploads/2016/07/Red_Book_2005.pdf) |
| `doe2025moaboverview` | 4 | 6 | U.S. Department of Energy 2025 — *Overview of the Moab UMTRA Project* | [link](https://www.energy.gov/em/moab/overview-moab-umtra-project) |
| `laboratory2021game` | 3 | 13 | Oak Ridge National Laboratory 2021 — *Game-changing rare-earth elements separation technology licensed to…* | [link](https://www.ornl.gov/news/game-changing-rare-earth-elements-separation-technology-licensed-marshallton) |
| `martin2010thermodynamics` | 3 | 14 | Martin 2010 — *Thermodynamics and Kinetics of Advanced Separations Systems -- FY 2…* | [link](https://inldigitallibrary.inl.gov/sites/sti/sti/4781579.pdf) |
| `anthony2001handbook` | 2 | 5 | Anthony 2001 — *Handbook of Mineralogy* | [link](https://handbookofmineralogy.org/) |
| `charbonnel2000thermodynamics` | 2 | 14 | Charbonnel 2000 — *Thermodynamics Properties of Complexation and Extraction of Ln(III)…* | [link](https://www.osti.gov/etdeweb/biblio/20176396) |
| `liu2024modeling` | 2 | 10 | Liu 2024 — *Modeling phase equilibria and recovery of rare earth elements with…* | [link](https://olisystems.com/resources/blog/modeling-phase-equilibria-and-recovery-of-rare-earth-elements-with-hydroxide-and-organic-ligands/) |
| `oye2019chloride` | 2 | 7 | Øye 2019 — *Could the chloride process replace the Hall-Héroult process in alum…* | [link](https://blog.sintef.com/energy/could-the-chloride-process-replace-the-hall-heroult-process-in-aluminium-production/) |
| `weber2012rare` | 2 | 7 | Weber 2012 — *Rare Earth Elements: A Review of Production, Processing, Recycling,…* | [link](https://nepis.epa.gov/Adobe/PDF/P100EUBC.pdf) |
| `chi2008weathered` | 1 | 5 | Chi 2008 — *Weathered Crust Elution-Deposited Rare Earth Ores* | [link](https://search.worldcat.org/oclc/185095748) |
| `csiro2024minerals` | 1 | 7 | Delaval 2024 — *Supplementary Report: Rare Earths* | [link](https://www.csiro.au/-/media/Science-Connect/Futures/Minerals-to-materials/CMRDD_Rare-Earths_FINAL.pdf) |
| `doe2025moabgroundwater` | 1 | 6 | U.S. Department of Energy 2025 — *Groundwater Interim Action, Moab UMTRA Project* | [link](https://www.energy.gov/em/moab/groundwater-interim-action) |
| `goodfellow2026neodymium` | 1 | 7 | 2026 — *Neodymium* | [link](https://www.goodfellow.com/usa/material/rare-earth-metals/neodymium) |
| `haynes2016crc` | 1 | 7 | 2016 — *CRC Handbook of Chemistry and Physics* | CRC Press |
| `labs2024green` | 1 | 13 | Sandia National Labs 2024 — *Green Extraction of Rare Earth Elements from Coal Waste* | [link](https://ip.sandia.gov/opportunity/green-extraction-of-rare-earth-elements-from-coal-waste/) |
| `lomon2024titanium` | 1 | 7 | Lomon Billions Group 2024 — *Key Facts: Titanium Dioxide Production Capacity* | [link](https://www.lomonbillions.global/key-facts/) |
| `rer2026technology` | 1 | 24 | Rare Element Resources 2026 — *Technology -- Rare Earth Processing and Separation* | [link](https://www.rareelementresources.com/technology/) |
| `unep2011recycling` | 1 | 20 | Graedel 2011 — *Recycling Rates of Metals: A Status Report* | [link](https://www.resourcepanel.org/reports/recycling-rates-metals) |

## What "on hand" means here

A source counts as collected when a PDF under `fulltexts/` maps to its key:
the file is named `<key>.pdf`, or a DOI printed on its first two pages
matches the entry, or it is one of the ten in the generator's override
table. Files that satisfy none of the three are invisible to this report and
will be asked for again — which is the argument for naming them after the
key when they land.

Collected does **not** mean read. `fulltexts/1-50/`, `fulltexts/u-p/` and
tiers 2 and 3 have been read against the book and their corrections are in
the git history. The rest are on disk and still owed a reading.
