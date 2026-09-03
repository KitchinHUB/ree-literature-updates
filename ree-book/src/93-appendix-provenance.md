---
title: "Appendix A: Source Provenance"
---

(appendix-a-source-provenance)=
# Appendix A: Source Provenance

Nothing in this book was written from scratch. Every chapter was assembled from
documents the group produced over roughly a year of literature review, held in
the `ree-literature-review/` repository. This appendix records which document
each chapter came from, so that any passage can be traced back to the review it
was written for and read in its original context.

The pipeline had two mechanical steps before any editing. First,
`tools/convert_sources.py` ran pandoc over the thirteen source documents (org,
Markdown, and docx) to produce MyST Markdown in `converted/`; the conversion
manifest, including word counts and citation-style counts, is in
`converted/MANIFEST.md`. Second, chapters were assembled by extracting line
ranges from `converted/`, demoting or promoting headings to fit the chapter
structure, and stripping the source documents' own section numbers so that
MyST owns numbering.

Line ranges below refer to the files in `converted/` **as produced by the
current version of `convert_sources.py`**. They are recorded for traceability,
not as a reproducible build step: re-running the converter after a source
document changes will shift them.

## Source documents

| Converted file | Original |
|---|---|
| `broad-review.md` | `rare_earth_separation_literature_review.md` |
| `leaching.md` | `leaching/ree-ore-leaching-review.org` |
| `clay-ion-exchange.md` | `clay-ion-exchange/readme.org` |
| `coacervates.md` | `coacervate-ree-separations-review.org` |
| `crystallization.md` | `molecular-crystallization-separation.org` |
| `thermodynamic-cycle.md` | `thermodynamic-cycle-to-kex.org` |
| `chemistry-fundamentals.md` | `ree-chemistry-fundamentals-review.org` |
| `high-throughput.md` | `high-throughput-ree-separations-review.org` |
| `microfluidic-report.md` | `Microfluidic_REE_Separation_Report.org` |
| `microfluidic-colorimetric.md` | `colorimetric-microfluidic-separation.org` |
| `carbochlorination-report.md` | `carbochlorination/Carbochlorination_Rare_Earth_Processing_Report.docx` |
| `carbohalogenation-review.md` | `carbohalogenation/Carbohalogenation_Comprehensive_Review.docx` |
| `bastnasite-framework.md` | `leaching/Bastnasite_Dissolution_to_Acidic_Phosphate_Extraction_Framework.docx` |

## Chapter map

| Chapter | Assembled from |
|---|---|
| 1. Why Rare Earths Are Hard to Separate | `broad-review.md` 10–38 (§1 Introduction); opening section newly written |
| 2. From Ore to Feed Solution | `chemistry-fundamentals.md` 13–113 |
| 3. Solvent Extraction Fundamentals | `chemistry-fundamentals.md` 114–866, 899–955 |
| 4. The Landscape of Separation Technologies | `broad-review.md` 41–183 (§2 Conventional), 1217–1231 (§8 Comparison) |
| 5. Hydrometallurgical Leaching | `leaching.md` 13–1469; closing "Feed Handed to Solvent Extraction" and "Further Reading" sections re-voiced from the source's memo-style conclusion |
| 6. Ion-Adsorption Clays | `clay-ion-exchange.md` 7–150 |
| 7. Pyrometallurgical and Halogenation Routes | Merge of `carbohalogenation-review.md` and `carbochlorination-report.md` (both docx tables of contents dropped; the hydrometallurgy section dropped as duplicated in Ch. 5) with `broad-review.md` §4 (930–1108) |
| 8. Coacervates and Aqueous Biphasic Systems | `coacervates.md` 14–450 |
| 9. Microfluidic Separations | Merge of `microfluidic-report.md`, `microfluidic-colorimetric.md`, and `broad-review.md` §3.9 (585–752) |
| 10. Precipitation and Selective Crystallization | `broad-review.md` 185–482 (§2.3 Precipitation) + `crystallization.md` 7–122 |
| 11. Biological and Biomimetic Separations | `broad-review.md` 1261–1789 (§10) |
| 12. Membranes, MOFs, and Emerging Approaches | `broad-review.md` 484–584, 753–929 (§3, less the microfluidics subsection) |
| 13. Thermodynamics of Extraction | `thermodynamic-cycle.md` 3–441 and 462–end + `broad-review.md` 2733–2897 (§16 Microcalorimetry) + `bastnasite-framework.md` |
| 14. High-Throughput and Computational Methods | `high-throughput.md` 13–256 + `broad-review.md` 2514–2714 (§14 Computational) |
| 15. Characterization Methods | `broad-review.md` 1791–2236 (§11) |
| 16. Recycling and Urban Mining | `broad-review.md` 1110–1148 (§5) |
| 17. Environment, Techno-Economics, and Life Cycle | `broad-review.md` 1150–1186 (§6), 2238–2367 (§12 TEA), 2369–2512 (§13 LCA) |
| 18. The Industrial Landscape | `broad-review.md` 1188–1215 (§7) |
| 19. Research Directions and Open Questions | `broad-review.md` 1233–1259 (§9), 2716–2732 (§15 Conclusions) + `high-throughput.md` 349–357 (critical gaps); synthesis newly written |

## Material deliberately dropped

- **Project-internal content.** Statement-of-work sections, staffing and
  location notes, meeting framing, and direct second-person address to a
  collaborator were removed from the leaching, thermodynamics, clay, and
  high-throughput sources. What survived was rewritten into third person.
- **Lab-planning sections.** `high-throughput.md` §6–7 planned specific
  equipment purchases and a collaboration; only the technical gap analysis
  was kept, in Ch. 19.
- **Duplicated coverage.** `chemistry-fundamentals.md` §7 and
  `high-throughput.md` §1.1 and §3.1–3.2 both describe the same automated
  platform and machine-learning work. The fuller high-throughput treatment
  was kept and the duplicate dropped.
- **Hand-written reference lists.** Several sources ended with a manually
  maintained list of references. These were dropped in favour of the single
  verified bibliography; see the [](#bibliography).
- **Off-topic documents.** `notes.org` (tungsten alloys, high-entropy alloys,
  crack detection), `litdb-ree-findings.org` (a search log), and `ideas.org`
  (brainstorming) were excluded from the book.

## Structural decisions worth knowing

- Section numbers were stripped from all headings. The source documents
  numbered their own sections; MyST numbers chapters, and keeping both
  produced headings like "3.2.1" inside chapter 12.
- Per-technology research opportunities stayed in their own chapters rather
  than being collected into Ch. 19, which cross-references them instead.
  Judging an opportunity requires the surrounding technical context.
- Flash Joule heating with chlorination is treated in full in Ch. 7, because
  the chemistry is chlorination. Ch. 12 keeps a pointer and the reported
  performance numbers for comparison.
- The bastnäsite dissolution framework moved to Ch. 13 rather than Ch. 5: it
  is a thermodynamic argument, and it reads better next to the extraction
  thermodynamic cycle it connects to.
