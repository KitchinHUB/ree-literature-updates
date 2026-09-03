# Citation repairs (Phase 4)

Converting the chapters to MyST citations meant every inherited key had to
resolve to a verified bibliography entry first. `tools/map_citation_keys.py`
reported 131 distinct keys, of which 113 resolved immediately. This records what
happened to the other 18, so the reasoning survives the commit.

Final state: **128 of 128 keys resolve**, three claims removed or re-sourced.

## Thirteen keys the Crucible knowledge base supplied

The ion-adsorption-clay chapter was written against
`nnl-rare-earth/.crucible/references.bib`, which the mapper did not read. Those
records are weak `@misc` entries that store the DOI in the `url` field and
prefix the title with "Surname YEAR - ", so even after adding the file as a
mapping source, nothing matched. The mapper now recovers a DOI from `url` and
strips that title prefix, and all thirteen resolve on DOI: `alshameri2019`,
`borst2020`, `cheng2024`, `hu2020`, `liu2022`, `luo2022`, `mohamadsobri2025`,
`moldoveanu2016`, `momen2019`, `wu2023`, `zhang2022`, `zhao2010`, `zhou2020`.

## Three keys identified by hand

`pan2024`, `shi2022` and `he2025` appear in no `.bib` file at all — the clay
source cited its own hand-typed reference list. Each was identified from that
list and confirmed against CrossRef, and the mapping is recorded explicitly in
`tools/map_citation_keys.py` because it cannot be derived mechanically:

| Key | Paper | DOI |
|---|---|---|
| `pan2024` | Insights into selective leaching of rare earths … using magnesium sulfate | `10.1016/j.jre.2024.04.025` |
| `shi2022` | Column leaching of ion adsorption rare earth ore at low ammonium concentration | `10.1016/j.jmrt.2022.05.199` |
| `he2025` | Stepwise leaching … inhibition leaching of aluminum with HMTA | `10.1007/s11356-025-36598-8` |

## Ten papers restored from fabricated DOIs

Twelve keys pointed at entries Phase 1 had rejected. Re-checking them showed the
*papers* are real; what was wrong was the recorded DOI. Eight carried DOIs that
look entirely plausible and resolve to nothing — the signature of a fabricated
identifier rather than a typo — and two carried a dead URL and no DOI. A CrossRef
title search found each one at a similarity of 1.00 (0.86 for the one whose title
the source recorded truncated), so they were re-fetched from CrossRef and added
through `tools/add_refs.py`, which takes the metadata from CrossRef rather than
from the source document.

The first author is wrong in six of the ten, which is why matching by key would
have been worthless here and why the recorded metadata could not be trusted even
where the title was right.

| Old key | Recorded DOI | Real DOI | New key |
|---|---|---|---|
| `castiho2003cpe` | `10.1016/S0039-9140(03)00387-2` | `10.1016/j.talanta.2003.12.033` | `favrerguillon2004cloud` |
| `chen2021abs` | `10.1007/s11426-021-1014-6` | `10.1016/j.cclet.2021.07.026` | `liu2022one` |
| `chen2023multiphase` | none (dead URL) | `10.1021/acs.macromol.2c01205` | `chen2022multiphase` |
| `chen2023ndpr` | `10.1016/j.seppur.2023.123076` | `10.1016/j.seppur.2023.123157` | `sui2023kinetic` |
| `li2019peptide` | `10.1021/acsami.8b21764` | `10.1021/acs.langmuir.9b00273` | `li2019coassembly` |
| `li2020abs` | `10.1039/D0GC01065K` | `10.1080/07388551.2020.1747388` | `kee2020development` |
| `li2025sc` | `10.1016/j.hydromet.2025.106234` | `10.1016/j.hydromet.2025.106514` | `gangadari2025critical` |
| `nitz2000lbt` | `10.1021/ja001609v` | `10.1006/jmre.2000.2172` | `ma2000lanthanide` |
| `shen2024thermodynamics` | `10.1016/j.fluid.2024.114135` | `10.1016/j.fluid.2024.114304` | `ascani2025molecular` |
| `rydberg2004solvent` | none | `10.1201/9780203021460` | `rydberg2004solvent` |

`rydberg2004solvent` is the standard *Solvent Extraction Principles and
Practice* (CRC Press, 2nd ed.). Phase 1 rejected it under a rule written for
journal articles — no DOI and no URL means unverifiable — which is the wrong
test for a book. CRC has since registered a DOI for it, and the entry is now a
`@book` with editors and ISBN.

## Three claims that could not be supported

- **`huang2006development`** (`src/05-hydrometallurgical-leaching.md`) —
  "Development Status and Research Progress in Rare Earth Hydrometallurgy in
  China", no DOI and no URL, and no CrossRef record resembles it (best match
  0.66, a different paper). The clause naming it was removed; the sentence keeps
  `[@gupta2004extractive]` as the standard textbook.
- **`unc2024smart`** (`src/08-coacervates.md`) — a UNC news release whose URL no
  longer responds. Searches for the underlying paper returned nothing
  identifiable, and a press release is not a citable primary source, so the
  sentence resting on it was deleted rather than re-pointed.
- **`sun2018nature`** (`src/03-solvent-extraction-fundamentals.md`) — cited three
  times and present in no bibliography anywhere, including the source
  document's own. Two of the three uses support general salting-out theory
  (salts compete for water of hydration; the equilibrium shifts toward the
  organic phase), which is exactly what *Solvent Extraction Principles and
  Practice* covers, so those now cite `rydberg2004solvent`. The third — ionic
  liquids being at the research stage for REE separations — supports nothing in
  particular and lost its citation.

## Conversion

`tools/convert_citations.py` then rewrote 19 org-cite, 247 parenthetical and 6
narrative citations across 7 chapters, renaming keys through
`citation-key-map.json` in the same pass. The build resolves all of them: the
ten "Could not link citation" warnings in the microfluidics chapter are gone and
the project builds clean.
