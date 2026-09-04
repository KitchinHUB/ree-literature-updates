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
| `bastnäsite-framework.md` | `leaching/Bastnäsite_Dissolution_to_Acidic_Phosphate_Extraction_Framework.docx` |

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
| 13. Thermodynamics of Extraction | `thermodynamic-cycle.md` 3–441 and 462–end + `broad-review.md` 2733–2897 (§16 Microcalorimetry) + `bastnäsite-framework.md` |
| 14. High-Throughput and Computational Methods | `high-throughput.md` 13–256 + `broad-review.md` 2514–2714 (§14 Computational) |
| 15. Process Modeling and Optimization | **No source document**; written from the primary literature for this edition. See the note below |
| 16. Characterization Methods | `broad-review.md` 1791–2236 (§11) |
| 17. Recycling and Urban Mining | `broad-review.md` 1110–1148 (§5) |
| 18. Environment, Techno-Economics, and Life Cycle | `broad-review.md` 1150–1186 (§6), 2238–2367 (§12 TEA), 2369–2512 (§13 LCA) |
| 19. The Industrial Landscape | `broad-review.md` 1188–1215 (§7) |
| 20. Research Directions and Open Questions | `broad-review.md` 1233–1259 (§9), 2716–2732 (§15 Conclusions) + `high-throughput.md` 349–357 (critical gaps); synthesis newly written |

### The one chapter with no source document

Every other chapter here is a rewrite of material the group had already
written. Chapter 15 is not. The sources touch process modeling twice — a
four-row table of software names in `high-throughput.md`, and a paragraph of
geochemical speciation packages in the characterization section — and neither
is an account of how a rare-earth flowsheet is modeled or optimized. The
chapter was written from the published literature instead, and its citations
were located and checked for this edition rather than inherited from a source
document.

That difference changes what an error in it would look like. Elsewhere in this
book the likeliest error is something a source document asserted and the
verification pass failed to catch. In Chapter 15 the likeliest error is a paper
whose abstract supports less than the sentence citing it claims. Every number
that chapter attributes to a specific study — stage counts, recoveries,
profitability signs — was read out of that study's own abstract during
drafting; where only a title was available, the sentence was written to claim
no more than a title can support.

## Material deliberately dropped

- **Project-internal content.** Statement-of-work sections, staffing and
  location notes, meeting framing, and direct second-person address to a
  collaborator were removed from the leaching, thermodynamics, clay, and
  high-throughput sources. What survived was rewritten into third person.
- **Lab-planning sections.** `high-throughput.md` §6–7 planned specific
  equipment purchases and a collaboration; only the technical gap analysis
  was kept, in Ch. 20.
- **Duplicated coverage.** `chemistry-fundamentals.md` §7 and
  `high-throughput.md` §1.1 and §3.1–3.2 both describe the same automated
  platform and machine-learning work. The fuller high-throughput treatment
  was kept and the duplicate dropped.
- **Hand-written reference lists.** Several sources ended with a manually
  maintained list of references. These were dropped in favour of the single
  verified bibliography; see the [](#bibliography). This was not a stylistic
  choice: when the hand-written entries in one source were checked against
  CrossRef, only one of twelve was correct as printed, and one was attributed
  to the wrong authors entirely.
- **Off-topic documents.** `notes.org` (tungsten alloys, high-entropy alloys,
  crack detection), `litdb-ree-findings.org` (a search log), and `ideas.org`
  (brainstorming) were excluded from the book.

## Structural decisions worth knowing

- Section numbers were stripped from all headings. The source documents
  numbered their own sections; MyST numbers chapters, and keeping both
  produced headings like "3.2.1" inside chapter 12.
- Per-technology research opportunities stayed in their own chapters rather
  than being collected into Ch. 20, which cross-references them instead.
  Judging an opportunity requires the surrounding technical context.
- Flash Joule heating with chlorination is treated in full in Ch. 7, because
  the chemistry is chlorination. Ch. 12 keeps a pointer and the reported
  performance numbers for comparison.
- The bastnäsite dissolution framework moved to Ch. 13 rather than Ch. 5: it
  is a thermodynamic argument, and it reads better next to the extraction
  thermodynamic cycle it connects to.

(bibliography-verification)=
## How the bibliography was checked

The bibliography was not inherited from the source documents. It was rebuilt
and then verified entry by entry, because the source documents' own citations
could not be trusted: an early pass found references whose DOIs resolved to
unrelated papers, hand-typed entries with wrong volumes and page ranges, and at
least one paper attributed to the wrong authors.

Verification ran in three stages.

**Stage 1 — does the reference exist?** Every entry was checked against
CrossRef by DOI, or, for a DOI CrossRef does not know, against DataCite —
software and dataset records are minted there rather than in CrossRef, and
which registry issued a DOI says nothing about the source — or, for entries
with no DOI at all (reports, standards, agency web pages), by fetching the
URL. Entries that could not be resolved either way were
removed to `references-rejected.bib` rather than left in place. Sixty-seven
entries were removed this way. The rule that followed from that removal governs
the rest of the book: any claim resting solely on a rejected citation had to be
removed or rewritten, not left standing without support.

The bibliography has grown since, as chapters were repaired and the claims that
survived acquired real sources. It now holds 577 entries, all 577 verified — 506
by resolving a DOI in CrossRef, one by resolving a DOI in DataCite, 67 by
fetching a live URL, and three books by ISBN.

That last group taught the tool something. An earlier version of the checker
rejected all three, which looked like a verdict on the books and was in fact a
verdict on the network: it reported "ISBN not found" when the truth was that
nothing had answered. Silence from a lookup service is not evidence. The
checker now distinguishes a service that says *no* from a service that says
nothing, keeps an entry in the second case, and lists it in
`verification-report.md` so it can be checked by hand. On the run that produced
the current report every lookup answered and nothing needed that exemption, but
the distinction is the difference between a check and a coin toss.

No title now diverges from the registry's record. Two appeared to: CrossRef
files a monograph's subtitle in a field of its own, so `gupta2003chemical`
(*Chemical Metallurgy: Principles and Practice*) and `biegler2010nonlinear`
(*Nonlinear Programming: Concepts, Algorithms, and Applications to Chemical
Processes*) were being compared against a bare *Chemical Metallurgy* and a bare
*Nonlinear Programming*. The checker now compares against title and subtitle
together, which is the honest comparison; checking the second of those by hand
also caught a real error, a title that had been transcribed with its last words
missing. The full record, including the sixty-seven rejected entries, is in
`verification-report.md` at the root of the book source.

**Stage 2 — does the entry describe the work it points at?** A DOI that
resolves to a paper with the right title still says nothing about the rest of
the entry, and the rest of the entry is most of what a reader uses to find the
work. Every entry with a DOI was therefore compared field by field against its
registry record: first author against the whole author list, year, container
title against every container the registry returns — a proceedings paper
returns both its series and its volume title, and either may be the right one —
volume, and pages.

One hundred and fifty entries disagreed, and the pattern was consistent: the
DOI was right, the title was right, and the bibliographic apparatus around them
was invented. Eighty-five had wrong page ranges, fifty-eight a wrong year,
fifty-one credited authors who had nothing to do with the paper.
`moyer2011overview` is by Tachimori and Morita, not Moyer and Jansone-Popova;
*Minerals* **10**(2) 178 is by Han alone, not Kim and Osseo-Asare; the 2022
*PNAS* coacervation paper is by Chen and Wang, not by Zhang and three
co-authors. All 150 were rewritten from the registry record. Only three titles
were touched, and only to restore a subtitle the entry had dropped. The prose
was checked separately for passages that name one of the wrong surnames beside
its citation; none does, so the error never reached the text.

Two entries pointed at a preprint while naming a journal. Both published
versions were found and substituted: @afonin2024extraction is *Compounds*
**4**(1) 172–181, not *Minerals*, and @yang2024investigation is *Materials*
**18**, 1538, not "PMC" — which is a repository, not a journal.

Citation keys were left as they were. A key like `moyer2011overview` is a
label, not a claim; the author and year the book prints come from the entry's
fields, and those are now right. The full audit, including the table of every
entry whose authorship was corrected, is in `review/CITATION-AUDIT.md`.

**Stage 3 — does the reference say what the text claims?** A resolving DOI
proves a paper exists; it proves nothing about whether that paper supports the
sentence citing it. A chapter-by-chapter review checked cited claims against
the cited work. It found the two failure modes that matter: citations attached
to the wrong paper, and numbers that appear in no paper at all. Both were
corrected in place — either by substituting what the source actually reports,
or, where nothing in the literature supported the claim, by deleting it. More
than a dozen data tables were deleted outright during this pass, because their
entries could not be traced to any source.

Claims that survive as numbers in this book should therefore be traceable. That
is a lower standard than *correct*, and it is the standard this book can
honestly claim.

(sources-not-synthesized)=
## Sources collected but not synthesized

Six papers were collected during the literature review as full PDFs but never
written up in prose, so no chapter was built from them. They are recorded here
because a paper nobody synthesized is not the same as a paper nobody thought
was important, and the gap is better visible than silent.

Three are nonetheless cited elsewhere in the book, from summaries written at
the time rather than from the PDFs: @augustine2024advancing (eleven times),
@an2024agile (five), and @gupta2025accelerating (three). The other three are in
the bibliography but are cited nowhere in the text.

**Automated and machine-learning separations.** @augustine2024advancing is the
Los Alamos platform that anchors
[](#automated-high-throughput-platforms-for-f-element-separations), and the
first thing to read if the automated-screening chapter is why you are here.
@an2024agile couples ligand synthesis to screening in one loop; its life-cycle
comparison against the prior synthetic route is the part usually missing from
papers of this kind, and it is discussed in
[](#high-throughput-extractant-synthesis-and-screening).
@gupta2025accelerating is the equivariant-network surrogate for DFT binding
energies weighed in [](#learned-binding-energies-as-a-dft-surrogate).
@nelson2020high is an earlier and more modest screening campaign than the LANL
work, and useful for exactly that reason: it shows what the approach looks like
without a robotics budget. It is cited nowhere in the text.

**Microfluidic extraction.** @chen2024continuous addresses phase separation at
the viscosities typical of loaded organic phases — the step that most often
defeats microfluidic extraction in practice, and one
[](#microfluidic-separations) does not treat, since that chapter is about
contacting. @maurice2021first demonstrates in-line X-ray fluorescence
measurement of both phases during extraction, which is the kind of real-time
analytics [](#gaps-in-automation-and-computation) identifies as the binding
constraint on automated screening throughput. Neither is cited in the text.

The review also accumulated a presentation deck and a docx duplicate of one of
the microfluidics reports; both were judged redundant with sources already
used. The Crucible knowledge base referenced by the ion-adsorption clay source
(`.crucible/wiki/concepts/`) has not been surveyed and may hold further
material.
