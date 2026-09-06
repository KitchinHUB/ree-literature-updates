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
| 21. Critical Minerals from Pennsylvania Produced Water | **No source document**; written from the primary literature for this edition. See the note below |
| 22. Uranium and Plutonium Separations | **No source document**; written from the primary literature for this edition. See the note below |
| 23. Environment, Techno-Economics, and Life Cycle | `broad-review.md` 1150–1186 (§6), 2238–2367 (§12 TEA), 2369–2512 (§13 LCA) |
| 24. The Industrial Landscape | `broad-review.md` 1188–1215 (§7) |
| 25. Research Directions and Open Questions | `broad-review.md` 1233–1259 (§9), 2716–2732 (§15 Conclusions) + `high-throughput.md` 349–357 (critical gaps); synthesis newly written |

### The six chapters with no source document

Most chapters here are a rewrite of material the group had already
written. Chapters 12, 15, 17, 18, 21 and 22 are not. The sources touch process modeling twice — a
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
that position are named in the text and listed in `needs-journal-access.md`.

One number in this chapter has a longer history than the chapter does. The
comparison table in Chapter 04 had carried a separation factor of 125 for Dy/Nd
by electrodialysis since the first draft, taken from a paper whose text no
interface reachable from this project would return. The PDF was retrieved by
hand after the chapter was drafted, and it showed the pair was wrong: the
paper's separation factor is dysprosium over praseodymium **and** neodymium
together, and it is a batch transfer ratio rather than an equilibrium β. The
value 125 is correct at the stated operating point. Chapter 12 now sets out the
whole result, including the paper's own finding that praseodymium and neodymium
cannot be separated by this method even by cascading, and the four places that
said Dy/Nd were corrected.

Chapter 21 is the fifth and the newest, added because the book's only treatment
of oilfield and geothermal water was a single section of Chapter 20 that
considered rare earths alone. It has no source document, and its exposure is
lower than the other four rather than comparable, because every number in it was
read out of a full text or a retrieved abstract during drafting rather than
inferred from a title. Full texts were obtained for @mackey2024estimates,
@smith2024critical, @phan2018role, @chapman2012geochemical, @noack2015rare,
@donmoyer2023effect, @peng2024extreme, @wenzlick2020techno and
@knierim2024evaluation; @warner2013impacts and @blondes2020utica are cited only
for figures that appear verbatim in their abstracts. One source,
@duchanois2023prospects, is cited for existence alone and no number is taken
from it.

Two things in that chapter are worth flagging as provenance rather than as
content. @mackey2024estimates is internally inconsistent about one figure: its
abstract and Table 1 give the northeastern per-well ten-year lithium yield as
1.96 mt while the Results text prints 1.86, evidently by duplicating the
confidence-interval lower bound. The chapter uses 1.96, which is the value two
of the three appearances agree on. And the rare earth row in the chapter's
national inventory rests, at the Marcellus, on **two samples** — a fact the
chapter states in the text rather than in a footnote, because the conclusion
drawn from it is a negative one and a reader is entitled to know how thin the
evidence for it is.

Chapter 22 is the sixth and was added at a reader's request for a treatment of
uranium separation, including from seawater, with plutonium included where the
literature supported it. It has no source document. Its 43 new sources were
found by OpenAlex search and every one was verified against its CrossRef record
for title, authors, journal and year before it was cited; none duplicated an
entry already in the bibliography. The chapter's exposure is the same as
Chapters 12 and 15's and is handled the same way — where no abstract was
reachable, no number was taken. Five sources fell in that category at first
drafting — @lindner2015review, @das2016novel, @seredkin2016situ,
@kim2016potential and @campbell2015biogeochemical — and were cited for what
their titles and metadata assert and for nothing numerical. That constraint has
since been lifted for all five; the paragraph below on the full-text pass
records what happened when they were read.

One deliberate omission shapes a section, and it changed shape when the source
was finally read. @lindner2015review is a review of cost estimates for uranium
from seawater, and while it was unreachable the chapter declined to quote any
dollar figure at all — a refusal resting on our own lack of access rather than
on anything about the literature. With the paper in hand that refusal was no
longer honest, so the chapter now quotes the review's own range (\$400–\$1,000/kg
U for the most recent estimates it covers, \$210 to \$3,400 across the full fifty
years in 2010 dollars) together with its verdict that none of the reviewed
systems is economically competitive with terrestrial mining. What the chapter
still declines to do is endorse a point inside that range, and the reason is now
a stated property of the sources: the spread is the propagated effect of
capacity and reuse assumptions that no field measurement constrains. The
physical arithmetic of @guidez2016extraction is quoted beside it, with the
distinction the paper itself draws between the 2 g/kg laboratory input to those
cost models and the under-1 g/kg/month its marine campaigns actually averaged.

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

@guo2026acidic was the one source in that batch whose abstract no route could
reach, and it was cited for no more than its title asserted. The full text has
since been obtained and read, and the two places that cite it in
[](#solvent-extraction-fundamentals) now carry specific claims from it: the
pK~a~ series for D2EHPA, PC88A and Cyanex 272, the stripping-versus-extraction
trade-off that ordering implies, the existence of Cyanex 572 as a blend sold to
sit between the two ends, and yttrium's movement from light to heavy behaviour
between naphthenic acid and Versatic 10.

**Chapter 9, read against the papers themselves.** The microfluidics chapter was
the one place in the book that still carried an explicit warning to the reader:
one of its three source documents came with its author's caution that references
without a URL might be fabricated. That warning has been discharged rather than
left standing. Thirty full texts --- every reference in the chapter for which a
copy could be obtained --- were retrieved, renamed by citation key, and read, and
the chapter was rewritten against them. Seventeen of its keys have no obtainable
copy and are now either hedged in the text or carry no number at all.

What the reading changed is worth recording, because most of it was not a matter
of tightening prose:

* The separation factor attributed to @fernandezmaza2024high was **279 in four
  places. The paper reports 175.9**, for Dy/La at 20 s and pH 1. Corrected
  everywhere.
* The chapter asserted that no microfluidic study cited in it reported a
  separation factor for an adjacent lanthanide pair. That was **false**:
  @zhang2022solvent reports β for Ce/Pr, and the result is the most interesting
  in the chapter --- the chip *matched* the shaken-equilibrium value at low
  throughput (2.27 against 2.28) and *lost* selectivity as throughput rose, to
  1.79. It refutes the naive form of the kinetic-selectivity argument the
  chapter had been making, and the argument was rewritten around it.
* The regime-comparison figure and its caption claimed an ordering of extraction
  efficiency by interfacial area. @feng2025microfluidic's nine measurements, all
  from one apparatus on one metal with one extractant, do not order that way ---
  the bands overlap and co-laminar flow sits between slug and droplet. Enrichment
  factor *does* order, in the opposite direction (0.99, 0.59, 0.142). The figure
  script and caption now say so.
* Two citations pointed at @dessimoz2010quantitative, which is a **gas--liquid**
  study of CO₂ and water and cannot support a liquid--liquid regime boundary.
  Both were moved to @dessimoz2008liquid, which measured the relevant systems and
  found slug and parallel flow gave the *same* kLa. Nothing in the book now rests
  on the 2010 paper; it survives in the bibliography only because this paragraph
  names it.
* "Eight lanthanides concentrated within about six minutes" was attributed to
  @pesavento2021versatile. It is that paper's description of someone else's work.
  Replaced with its own numbers.
* @idros2018triple was cited for detecting six metals. Its own table shows its
  mercury and lead detection limits sit **above** the corresponding safe limits.
  The chapter now says which four elements the device can call and which two it
  cannot.
* The "20-500×" intensification headline is now bounded by the only two studies
  that ran both sides of the comparison themselves: @kolar2016microfluidic
  measured about 2× in the chip's favour, and @nelson2018micro measured a stirred
  Lewis cell about 4× *faster* than the chip.
* A design claim resting on @he2024intensifying --- that beyond about 250 mm of
  channel a mini-channel extractor delivers more than one theoretical stage ---
  was **deleted**. No copy of that paper could be obtained through any route, and
  the chapter now states plainly that the number is not one it can source.
* @yang2022pilot is likewise unobtainable. Its hundredfold numbering-up result is
  retained only as its own authors describe it in their later open-access review,
  @yang2024industry, and the text says so.

The warning block is gone from the chapter, which is what the work was for.

**A peptide paper read in full, and a key that named the wrong author.**
@ortunomacias2024lanthanide --- lanthanide-binding peptide surfactants at the
air-aqueous interface, PNAS 121(52) e2411763121 --- was already in the
bibliography, but under the key `li2024lanthanide`, which came out of the
`coacervate.bib` merge (`bibliography-audit.md:20`) and names no author of the
paper. It was renamed to `ortunomacias2024lanthanide` and moved beside the same
group's 2025 foam-separation paper; `bib-rekey.md` records the change. Reading
the full text replaced a qualitative statement in two chapters --- that the
interfacial selectivity reverses with loading --- with the numbers behind it.
The surface Tb³⁺:La³⁺ ratio runs from about 0.25 at 50 µM total Ln³⁺ to about
2.0 at 1,000 µM; the measured bulk dissociation constants predict 24.8 for that
layer. The interfacial step therefore gives away an order of magnitude of the
discrimination the bulk chemistry already has, and what survives is a factor of
about two on a pair nine places apart in the series. Both
[](#coacervates-and-aqueous-biphasic-systems) and
[](#biological-and-biomimetic-separations) now say so, and the second says
plainly that this is a demonstration rather than a separation. The net-charge
design rule (−3, giving a neutral complex and a surface cation-to-peptide ratio
of 0.96 ± 0.09) also comes from that reading.

**Four 2025-26 machine-learning and process papers, added at the level the
sources allow.** A literature check against the current search results for
automated and learned f-element separations added @lee2025data,
@augustine2026coupling, @leite2025creation and @yu2026progress. Only the first
two have released abstracts, and neither has an obtainable full text; the other
two are cited for existence. @augustine2026coupling matters most, because it
forced two of the book's own standing claims to be corrected rather than merely
extended: the "what has not been demonstrated" list in
[](#machine-learning-in-rare-earth-separations) had said that no
computationally-guided campaign had been carried through to measured lanthanide
separations, and it now has been --- a fourfold gain in separation factor over
HDEHP alone, from an aqueous holdback agent found by screening and confirmed by
experiment. The limits are recorded with it: what was optimized is process
conditions rather than molecules, the splits are {Eu, Dy, Ho} from Nd and Eu
from {Dy, Ho}, and Dy/Ho --- the one adjacent pair in the set --- stays
together. All of that is read from the abstract, which the text states.
`needs-journal-access.md` lists all four.

**Chapter 22, read against thirty-seven full texts — and a retracted paper the
whole pipeline had missed.** The chapter was written from abstracts and
metadata. Full texts were afterwards obtained for thirty-seven of its
sources — every one for which a copy could be had — renamed by citation key,
and read against the sentences citing them. Six parallel readers each took a
group of keys and reported byte-exact proposed corrections rather than editing
the chapter, so that every change could be adjudicated in one place; the
overlapping proposals were merged by hand, and where two readers disagreed the
primary source settled it.

The errors it found fall into four kinds, and naming them is more useful than
counting them. **A number attached to the wrong paper inside a
multi-source bracket:** "elution efficiencies of 95–98.5 % over up to eight
cycles" was cited to @pan2016elution and @wang2018significantly jointly, but
@pan2016elution runs no cycling experiment at all, and the eight-cycle series
belongs entirely to the other paper — which ends that run at 83.5 %, not 98.5 %.
**Measurement conditions dropped, so that non-comparable figures sat in one
column:** the capacity-trajectory table put a 180-day equilibrium loading, a
shaken-tank batch and two flow-through column tests side by side and drew a
trend line through them. It now carries a basis column, an additional row from
@das2016novel that the abstract-level pass had missed, and a paragraph saying
which three rows are actually comparable. **Arithmetic contradicting itself
across one sentence:** the chapter printed 4.5 billion tonnes of uranium in the
sea against 17 million tonnes on land and called the ratio "more than a
thousandfold." It is 260. The thousandfold figure is real and both cited
sources use it, against a narrower reserve base than the one printed beside it;
the chapter now says so. **And one ligand misnamed outright:** three stability
constants cited to "2,6-pyridinedicarboxamidoxime-type architectures" are in
fact those of 1,10-phenanthroline-2,9-dicarboxylic acid, which is in
@lashley2016highly's title. No such amidoxime appears anywhere in that paper.
The invented name reads as 2,6-pyridinedicarboxylic acid with an amidoxime
suffix grafted on, and that acid is in the paper — as the less preorganized
foil the phenanthroline is meant to beat — so the sentence pointed at the losing
ligand while quoting the winner's numbers. Two mechanisms had likewise been swapped: in
@ladshaw2016experiments, bicarbonate competes with the sorbent for uranium in
solution while calcium and magnesium occupy the binding sites, and the chapter
had said the reverse.

The same pass exposed a gap in every stage described above. A reader pointed
out that @xian2016glutarimidedioxime — cited for a glutarimidedioxime
complexant-reductant recovering plutonium from reprocessing raffinate — had
been **retracted by *Angewandte Chemie* in 2021**. Every check in stages 1
through 4 had passed it: the DOI resolves, the metadata matches, the paper says
what the chapter said it said. None of them asks whether the paper still
stands. All 706 DOI-bearing entries were therefore queried against CrossRef's
`updated-by` relation, which is where retractions, withdrawals, removals and
expressions of concern are filed. That one entry is the only retraction in the
bibliography. Three entries carry a `correction` relation — @yin2024preparation,
@muratov2020qsar and @taylor2023architector — and each was checked by hand; none
of the three carries a number the book depends on. The chapter's paragraph on
that plutonium result now records the retraction instead of the result, the
entry carries a `note` saying it is cited only to record its own retraction, and
the retraction notice is itself a bibliography entry. Retraction status is now
part of what gets checked when `references.bib` changes.

(sources-not-synthesized)=
## Two books, read by chapter

Late in the project two full monographs entered the source pile as PDFs large
enough that they had to be split by chapter before they could be read at all.
Neither can be committed: both are publisher PDFs carrying a personal watermark,
and `fulltexts/` is gitignored for that reason. What follows records what was
read, at what depth, and what came of it, so that a later reader can tell the
difference between a book that was consulted and a book that was merely owned.

**Zhang, Zhao and Schreiner, *Separation Hydrometallurgy of Rare Earth
Elements* (Springer, 2016).** Split into eight units. **Chapter 5, "Cascade
Solvent Extracting Principles and Process Design" (book pp. 171--241), was read
in full**, including §§5.2--5.13, all three worked examples, Table 5.20 and
Table 5.22. It is the source for the closed-form design equations in
[](#solvent-extraction-fundamentals) — the stage-count relations, the optimum
extraction factor $E_B = 1/\sqrt{\beta}$ and its consequence $E_A E_B = 1$, the
reflux-ratio values, and the 45-stage worked example against a 24-stage Fenske
bound — and for three new sections in
[](#process-modeling-and-optimization): the capital objective
$\Phi = S_o(n+m)$ and its shallow minimum, the three-outlet process, and
circulating start-up. Chapters 1, 2 and 3 were not read; nothing in the book
depends on them.

Two claims from that chapter were **deliberately not carried into the book**.
The rule of thumb $W_a = 1/(\beta^k - 1)$ with $k = 0.70$, and the assertion
that the design method was "approved correct in over ten years of rare earth
production," are asserted expert practice with no dataset, no error estimate and
no external citation; the chapters say so where they use the first and decline
the second. The fuzzy-linkage claim that reagent consumption falls by 30 % is
refused outright: it is ambiguously worded in the source and rests on a
Chinese-language secondary reference not reachable from here.

**Azimi, Forsberg, Ouchi et al., eds., *Rare Metal Technology 2021* (TMS/
Springer, 2021).** Split into 36 units. Thirteen were selected as
rare-earth-, scandium- or lithium-relevant and read; the remainder — on
lithium-ion battery recycling, platinum-group metals, tungsten, indium,
chromium and vanadium — are off-topic for this book and were not read beyond
their titles. Nine of the thirteen carried a number the book did not already
have and are now cited:

| Paper | Where it landed |
|---|---|
| @sanku2021extraction | Extraction chromatography in [](#the-landscape-of-separation-technologies) |
| @lewis2021innovative | Antisolvent crystallization in [](#precipitation-and-selective-crystallization) |
| @ilyas2021solvo | Ce(IV)/Cyanex 923 and oxalate kinetics, same chapter |
| @balomenos2021scandium | Bauxite residue in [](#recycling-and-urban-mining) |
| @eriksen2021scandium | Why scandium is in bauxite at all, same chapter |
| @lister2021recovery | Selective magnet leaching from steel, same chapter |
| @sarswat2021rare | Coal refuse biooxidation, same chapter |
| @marthi2021lithium | H₂TiO₃ adsorbent capacity in [](#produced-water-critical-minerals) |
| @kumari2021recovery | Battery-effluent lithium concentrations, same chapter |

The other four of the thirteen were read at abstract level and **deliberately
not used**: papers on option trees for reactive extraction, on rethinking
mineral processing, on thermodynamic calculations for Nd/Dy/Pr recovery from
NdFeB, and on total WEEE recycling. Each is a position or modelling paper whose
quantitative content either duplicates material the book already has from a
better-documented source or could not be checked without the full text. None is
in the bibliography, because a citation this book cannot verify is one it does
not make.

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
