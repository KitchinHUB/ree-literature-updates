# Phase 2 conversion manifest

Mechanical pandoc conversion of the ree-literature-review sources to
MyST Markdown. Nothing here is restructured yet -- Phase 3 splits and
merges these into `src/`. Citations are still in their original four
styles; Phase 4 converts them to `[@key]`.

Total: **57,193 words** across 13 files.

| Converted file | Source | Words | Headings | org `cite:` | `[n]` cites | Destination |
|---|---|---|---|---|---|---|
| `leaching.md` | `leaching/ree-ore-leaching-review.org` | 5,968 | 102 | 83 | 0 | Ch. 5 Hydrometallurgical Leaching |
| `clay-ion-exchange.md` | `clay-ion-exchange/readme.org` | 2,948 | 21 | 0 | 0 | Ch. 6 Ion-Adsorption Clays |
| `coacervates.md` | `coacervate-ree-separations-review.org` | 3,627 | 60 | 73 | 0 | Ch. 8 Coacervates |
| `crystallization.md` | `molecular-crystallization-separation.org` | 1,139 | 14 | 0 | 0 | Ch. 10 Selective Crystallization |
| `thermodynamic-cycle.md` | `thermodynamic-cycle-to-kex.org` | 2,078 | 35 | 0 | 0 | Ch. 13 Thermodynamics (strip the SOW section in Phase 3) |
| `chemistry-fundamentals.md` | `ree-chemistry-fundamentals-review.org` | 4,423 | 69 | 70 | 0 | Ch. 2 + Ch. 3 (split at section 2) |
| `high-throughput.md` | `high-throughput-ree-separations-review.org` | 2,194 | 54 | 23 | 0 | Ch. 14, sections 1-5 only; 6-7 are lab planning, drop |
| `microfluidic-report.md` | `Microfluidic_REE_Separation_Report.org` | 3,045 | 14 | 0 | 49 | Ch. 9 merge source (industrial/pilot framing) |
| `microfluidic-colorimetric.md` | `colorimetric-microfluidic-separation.org` | 1,311 | 34 | 38 | 0 | Ch. 9 merge source (detection + computer vision) |
| `broad-review.md` | `rare_earth_separation_literature_review.md` | 17,610 | 254 | 0 | 0 | Ch. 1, 4, 11, 12, 15, 16, 17, 18, 19 (split by section) |
| `carbochlorination-report.md` | `carbochlorination/Carbochlorination_Rare_Earth_Processing_Report.docx` | 7,418 | 37 | 0 | 166 | Ch. 7 merge source |
| `carbohalogenation-review.md` | `carbochlorination/Carbohalogenation_Comprehensive_Review.docx` | 4,882 | 34 | 0 | 51 | Ch. 7 merge source |
| `bastnasite-framework.md` | `leaching/Bastnasite_Dissolution_to_Acidic_Phosphate_Extraction_Framework.docx` | 550 | 8 | 0 | 0 | Ch. 5 sidebar or Ch. 13 (short, 568 words) |

## Excluded from the book

- `notes.org` — mostly tungsten alloys, HEAs, crack detection; off-topic.
- `litdb-ree-findings.org` — a database search log, not prose.
- `ideas.org` — brainstorming; the stimuli-responsive nanoparticle idea
  may seed Ch. 19 Research Directions.
- `nnl.bib` — disjoint general materials-science library (see Phase 1).
- `papers/`, `microfluidic-ree-papers/` — PDFs with no written prose;
  they become Appendix B further reading.
