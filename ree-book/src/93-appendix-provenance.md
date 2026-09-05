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
| 12. Electrochemical Separations | **No source document**; written from the primary literature for this edition. The electrodialysis section was moved here from Chapter 13 rather than rewritten — see the note below |
| 13. Membranes, MOFs, and Emerging Approaches | `broad-review.md` 484–584, 753–929 (§3, less the microfluidics subsection) |
| 14. Thermodynamics of Extraction | `thermodynamic-cycle.md` 3–441 and 462–end + `broad-review.md` 2733–2897 (§16 Microcalorimetry) + `bastnäsite-framework.md` |
| 15. Kinetics and Mass Transfer | **No source document**; written from the primary literature for this edition. See the note below |
| 16. High-Throughput and Computational Methods | `high-throughput.md` 13–256 + `broad-review.md` 2514–2714 (§14 Computational) |
| 17. Process Modeling and Optimization | **No source document**; written from the primary literature for this edition. See the note below |
| 18. Machine Learning in Rare Earth Separations | **No source document**; written from the primary literature for this edition. Two sections were moved here from Chapter 16 rather than rewritten — see the note below |
| 19. Characterization Methods | `broad-review.md` 1791–2236 (§11) |
| 20. Recycling and Urban Mining | `broad-review.md` 1110–1148 (§5) |
| 21. Environment, Techno-Economics, and Life Cycle | `broad-review.md` 1150–1186 (§6), 2238–2367 (§12 TEA), 2369–2512 (§13 LCA) |
| 22. The Industrial Landscape | `broad-review.md` 1188–1215 (§7) |
| 23. Research Directions and Open Questions | `broad-review.md` 1233–1259 (§9), 2716–2732 (§15 Conclusions) + `high-throughput.md` 349–357 (critical gaps); synthesis newly written |

### The four chapters with no source document

Most chapters here are a rewrite of material the group had already
written. Chapters 12, 15, 17 and 18 are not. The sources touch process modeling twice — a
four-row table of software names in `high-throughput.md`, and a paragraph of
geochemical speciation packages in the characterization section — and neither
is an account of how a rare-earth flowsheet is modeled or optimized. The
chapter was written from the published literature instead, and its citations
were located and checked for this edition rather than inherited from a source
document.

That difference changes what an error in it would look like. Elsewhere in this
book the likeliest error is something a source document asserted and the
verification pass failed to catch. In Chapter 17 the likeliest error is a paper
whose abstract supports less than the sentence citing it claims. Every number
that chapter attributes to a specific study — stage counts, recoveries,
profitability signs — was read out of that study's own abstract during
drafting; where only a title was available, the sentence was written to claim
no more than a title can support.

Chapter 18 was written the same way and with the same exposure. Two of its
sections — the deep-learning distribution-ratio work and the learned binding
energies — were moved out of Chapter 16, where they were originally assembled
from `high-throughput.md`, and were not rewritten in the move; their labels
travelled with them so that existing cross-references still resolve. Everything
else in the chapter was written from CrossRef, OpenAlex and Semantic Scholar
metadata and from publisher abstracts. Five of its sources had no abstract
reachable through any of those routes and no open-access copy:
@zhang2026predicting, @liu2026machine, @zhang2026design,
@jorjani2008prediction and @gomezflores2022critical. Each is cited for no more
than its title asserts, and the two that bear most directly on the chapter's
subject are named in the text as papers this book takes no numbers from.

Chapter 15 has no source document either, and its exposure is
different again and smaller. It exists because the sources — and, until it was
written, this book — treated separation almost entirely as an equilibrium
problem, so there was nothing to rewrite. Every claim in it was checked against
a CrossRef or OpenAlex record while it was being drafted, and the rule it works
to was made explicit rather than assumed: where no abstract was reachable, no
number was taken. Five sources fall in that category and are listed by name in
`needs-journal-access.md` alongside what reading them would add. Four more — the
aqueous kinetic-separation work of the Huang group — report separation factors
that could not be verified, and the chapter's own comparison table carries "not
quoted here" in those cells rather than a number.

Chapter 12 is the fourth and was added in a 2026 pass that compared the book
against the recent literature and found electrically driven separations treated
in one paragraph inside the membranes chapter and nowhere else. It has no source
document. Its electrodialysis section was moved out of Chapter 13 and re-voiced
rather than rewritten from scratch; Chapter 13 keeps a pointer in its place. The
chapter's exposure is the same as Chapter 15's and is handled the same way:
where no abstract was reachable, no number was taken, and the four sources in
that position are named in the text and listed in `needs-journal-access.md`. One
of them matters more than the others. The separation factor of 125 for Dy/Nd
that the chapter 04 comparison table has carried since the first draft comes
from a paper whose text no interface reachable from this project would return,
and chapter 12 says so rather than repeating the number as established.

## Material deliberately dropped

- **Project-internal content.** Statement-of-work sections, staffing and
  location notes, meeting framing, and direct second-person address to a
  collaborator were removed from the leaching, thermodynamics, clay, and
  high-throughput sources. What survived was rewritten into third person.
- **Lab-planning sections.** `high-throughput.md` §6–7 planned specific
  equipment purchases and a collaboration; only the technical gap analysis
  was kept, in Ch. 23.
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
  produced headings like "3.2.1" inside chapter 13.
- Per-technology research opportunities stayed in their own chapters rather
  than being collected into Ch. 23, which cross-references them instead.
  Judging an opportunity requires the surrounding technical context.
- Flash Joule heating with chlorination is treated in full in Ch. 7, because
  the chemistry is chlorination. Ch. 13 keeps a pointer and the reported
  performance numbers for comparison.
- The bastnäsite dissolution framework moved to Ch. 14 rather than Ch. 5: it
  is a thermodynamic argument, and it reads better next to the extraction
  thermodynamic cycle it connects to.

(bibliography-verification)=
## How the bibliography was checked

The bibliography was not inherited from the source documents. It was rebuilt
and then verified entry by entry, because the source documents' own citations
could not be trusted: an early pass found references whose DOIs resolved to
unrelated papers, hand-typed entries with wrong volumes and page ranges, and at
least one paper attributed to the wrong authors.

Verification ran in four stages.

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
survived acquired real sources, and shrunk again as sources that could not carry
their claims were removed. On the last full re-run, on 2026-09-04, it held 637
entries, all 637 verified — 586 by resolving a DOI in CrossRef, two by resolving
a DOI in DataCite, 46 by fetching a live URL, and three books by ISBN. Nothing
was rejected in that run, no title disagreed with the registry, and ninety
entries sit in `references-rejected.bib` from earlier ones.

That date matters more than the count. The checker is re-run whenever
`references.bib` changes, and `verification-report.md` carries the date of the
run that produced it, so a reader who finds this paragraph disagreeing with the
bibliography is looking at a stale sentence rather than at an unchecked entry —
and can tell which by comparing the two dates.

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

Citation keys were left as they were at this stage. A key like
`moyer2011overview` is a label, not a claim; the author and year the book prints
come from the entry's fields, and those are now right. Seven were eventually
renamed anyway --- `spruijt2014polyelectrolyte` became `wang2014polyelectrolyte`,
`gao2023separation` became `zhang2023separation`, and five more --- not because
anything rendered wrongly, but because a key that names the wrong person misleads
whoever opens the `.bib`, and renaming is cheap. The full audit, including the
table of every entry whose authorship was corrected, is in
`review/CITATION-AUDIT.md`.

**Stage 3 — does the reference say what the text claims?** A resolving DOI
proves a paper exists; it proves nothing about whether that paper supports the
sentence citing it. A chapter-by-chapter review checked cited claims against
the cited work. It found the two failure modes that matter: citations attached
to the wrong paper, and numbers that appear in no paper at all. Both were
corrected in place — either by substituting what the source actually reports,
or, where nothing in the literature supported the claim, by deleting it. More
than a dozen data tables were deleted outright during this pass, because their
entries could not be traced to any source.

The last part of that review to be done was the hardest to automate. Forty-four
entries have no DOI — agency reports, standards, company pages, a handful of
books — and for those, stage 1 could only fetch the URL. A URL that returns 200
proves a page exists. It says nothing about what is on it, and that gap is
exactly where a fabricated citation survives longest: the identifier is live,
the checker is satisfied, and no one has read the page. All twenty-one such
entries that the book actually cites were therefore opened and read against the
sentence citing them.

Six could not carry their claim. A market-research preview page was supporting
a fluidized-bed reactor temperature it does not mention; a corporate key-facts
page was supporting a sentence about seven decades of safe operation that it
does not contain; a blog post attributed to "Engell, K." in 2023 turned out to
be by Bjarte Øye in 2019 and to be about aluminium, with no mention of rare
earths, while it propped up a claim about rare earth co-recycling; a
membership-gated page was supporting a distillation cascade nobody outside the
membership can check; an OSTI identifier attributed to a Department of Energy
report on coal-based resources belongs to Zhang and Honaker's paper on acid
mine leachate and contains none of the fly ash grades cited to it; and a CSIRO
assessment was cited for chlorination being an established industrial route in
China when what it says is that chlorination roasting is being investigated at
laboratory scale.

Where the claim was sound and only the citation was bad, a real source replaced
it — Taggart and co-workers in *Environmental Science & Technology* for the fly
ash grades, Morris and Jensen and Zhou and Sohn for the fluidized-bed
chlorinator, the USGS Minerals Yearbook for the chloride process and its
operators. Where the claim was the problem, the claim went, or was rewritten to
say plainly that it is a conjecture of ours. Two encyclopaedia citations were
replaced by technical ones, and seventeen uncited vendor pages, blogs and
encyclopaedia articles were removed from the bibliography as well: none of them
reached the book, but a bibliography that carries them invites the reader to
wonder what else is in it. The full account is in `review/CITATION-AUDIT.md`.

**Stage 4 — does the cited paper actually say it?** Stage 3 read the
forty-four entries that have no DOI, because those were the ones no automated
check could reach. That left the larger and more comfortable assumption
untested: that the 883 citation instances resting on a resolving DOI say what
the sentences citing them say. They were read too, one claim at a time, across
388 distinct entries. The reading was fanned out over thirteen parallel agents,
one or two chapters each; every finding that would change the book was then
re-verified by hand against a primary source before a word was changed, because
an agent's report is a lead and not a verdict, and several of those leads did
not survive the check.

Fifty-nine claims did not survive it, in four kinds. Most often the claim is
simply not in the paper — a table, a number, or a mechanism attributed to a
work that contains no such thing. Sometimes the paper is about something else
entirely: @murase1995recovery is chemical vapour transport with AlCl₃ rather
than a carbochlorination intermediate, @hua2014selective is a molten
MgCl₂–KCl study rather than chlorination roasting, and @suli2017rare — the one
case where a full PDF could be read rather than an abstract — has no
chlorination content whatever, though a stoichiometric chlorine feed had been
cited to it. Twice the paper says the opposite of the sentence citing it:
@chen2022driving argues *against* counterion release as the driving force, and
@dessimoz2008liquid's headline finding is that slug and parallel flow give the
*same* mass-transfer coefficient, where the book had used it to distinguish
them. And once a real number was wearing the wrong unit — the "49 % conversion"
in the MgO carbochlorination passage is that paper's 49 kJ/mol activation
energy, which is the kind of error no identifier check will ever find.

Where the cited work was real and useful but attached to the wrong sentence, it
was re-homed onto a claim it does support rather than dropped. Where nothing
supported the claim, the claim went, or the text now says in plain words that
the figure is not available and why. Ten claims rest on papers that no route
available could reach — Elsevier and Springer serve nothing to automated
requests and are excluded from the Internet Archive, and several institutional
repositories return 404 on their own handles — and each of those is either
softened to what its metadata guarantees or explicitly flagged in the text as
unquoted.

One finding was of a different kind. The book had said that no protein system
had been shown to fractionate an adjacent *heavy* lanthanide pair. That was
true when it was written and is no longer: @choi2026near report an average
adjacent-element separation factor of 2.1 across Nd–Lu for dimerizing
lanmodulins, and on-column tandem dimers that separate Y, Dy, Gd, Sm and Nd to
above 95 % purity from an allanite-derived leachate. Both passages making the
claim were rewritten. A synthesis has a shelf life, and this is what its
expiry looks like.

The method has a blind spot worth naming, since naming it is cheaper than
pretending it does not exist: a claim-by-claim audit keyed on citations walks
straight past any sentence that carries no citation at all. Chapters 10 and 18
each contain specific numeric figures of exactly that kind. Finding their
sources needs a different question — start from the numbers, not from the
bibliography — and it has not been asked yet.

Claims that survive as numbers in this book should therefore be traceable. That
is a lower standard than *correct*, and it is the standard this book can
honestly claim.

**A later batch, and what checking it turned up.** A reading list of thirteen
references supplied after the chapters were written was checked the same way
before any of it was used. Eight were already in the bibliography. Of the
remaining five, three needed correcting against the record before they could be
cited. The Lyon thesis was supplied as a 2016 Ph.D. thesis and the bibliography
already held it as a 2015 Master's thesis by "Kyle" Lyon; the title page of the
deposited copy settles it as a Master of Science thesis by *Kevin* L. Lyon,
accepted May 2016, so the entry now carries the right name, the right year and
the right degree, and its key changed with them. The IUPAC *Nomenclature of
Inorganic Chemistry* was supplied with DOI `10.1515/pac-2014-0718`, which
belongs not to the book but to a 2015 *Pure and Applied Chemistry* technical
report summarising it, by a different set of authors; both are now in the
bibliography as separate entries, the book by ISBN and the report by its DOI,
and the definition quoted in [](#why-rare-earths-are-hard-to-separate) was read
out of section IR-3.5 of the book itself. The DOE final report was supplied as
"Keim, S.; Hans, N."; the second author's name is Hans Naumann.

@guo2026acidic is the one source in that batch whose abstract no route could
reach, so it is cited for no more than its title asserts, as the recent review
of solvent extraction from acidic media.

(sources-not-synthesized)=
## Sources collected but not synthesized

Six papers were collected during the literature review as full PDFs but never
written up in prose, so no chapter was built from them. They are recorded here
because a paper nobody synthesized is not the same as a paper nobody thought
was important, and the gap is better visible than silent.

Three are nonetheless cited elsewhere in the book, from summaries written at
the time rather than from the PDFs: @augustine2024advancing (eleven times),
@an2024agile (five), and @gupta2025accelerating (four). The other three are in
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
