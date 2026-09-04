---
title: Citation Audit
---

# Citation Audit

Every identifier in `references.bib` was resolved against an authoritative
registry -- CrossRef for journal articles, book chapters, proceedings and OSTI
reports, DataCite for DOE software DOIs -- and then the record that came back
was compared field by field with the entry that cites it. The second half is
the part that had never been done. An earlier pass checked that each DOI
resolved and that the title of the work it resolved to matched the title in the
entry; it did not check who wrote that work, when, or where it appeared.

## Summary

| Status | Before | After | Meaning |
|---|---|---|---|
| Agrees with the registry | 351 | 501 | every compared field matches |
| Divergence documented in the entry | 6 | 6 | a `note` field already explains why |
| **Disagrees with the registry** | **150** | **0** | DOI and title right, other fields wrong |
| No DOI (web page, report, book) | 70 | 70 | checked by live URL or ISBN instead |
| Total | 577 | 577 | |

Of the 150 divergent entries, 93 were cited somewhere in the book and 57 were
carried in the bibliography but not cited. All 150 were rewritten from the
registry record; the check was then re-run over all 577 entries and every one
now agrees, apart from the six whose divergence is deliberate and documented.

The tool that performs this comparison is `tools/check_bib_metadata.py`, and it
is worth re-running whenever entries are added:

    python3 tools/check_bib_metadata.py

## What is wrong, by field

| Field | Entries |
|---|---|
| pages | 85 |
| year | 58 |
| first author | 52 |
| volume | 34 |
| journal | 17 |
| title | 3 |

Titles are almost entirely sound -- three entries record a title that the
registry extends with a subtitle, and nothing else. The damage is concentrated
in the fields that were never checked.

## The serious class: 51 entries credit the wrong authors

In each of these the DOI is right and the title is right, so the entry points
at a real and relevant paper. The author list attached to it belongs to no one.
Three checked by hand:

- `moyer2011overview` -- "Overview of Solvent Extraction Chemistry for
  Reprocessing" is chapter 1 of *Ion Exchange and Solvent Extraction* vol. 19
  (2009) by **Tachimori and Morita**. The entry credits Moyer and
  Jansone-Popova, and names a different book.
- `kim2020characteristics` -- *Minerals* **10**(2) 178 is by **Han**, a single
  author. The entry credits Kim and Osseo-Asare.
- `zhang2022driving` -- *PNAS* **119**(35) is by **Chen and Wang**. The entry
  credits Zhang, Alsaifi, Wu and Wang.

No passage in the book names any of these wrong surnames in its prose next to
the citation -- that was checked across all of `src/` -- so the error is
confined to the bibliography and to the author-year label the site renders.

| Key | Entry credits | Registry credits | Cited |
|---|---|---|---|
| `anderson2016chlorination` | Anderson | Gaede, Ruffier, Downey et al. | — |
| `boronski2020rationally` | Boronski | Prodius, Klocke, Smetana et al. | — |
| `chen2025lanmodulin` | Chen | Chhantyal, Pugazhenthi, Pakshirajan | yes |
| `cheng2020determination` | Cheng | Baghaliannejad, Aghahoseini, Amini | — |
| `cheng2021theoretical` | Cheng | Olea, Rosales, Quintriqueo et al. | yes |
| `davidson2020application` | Davidson | González-Sálamo, Ortega-Zamora, Carrillo et al. | — |
| `depierro2008cloud` | De Pierro | Mustafina, Elistratova, Burilov et al. | yes |
| `desbouis2012thermodynamics` | Desbouis | Di Bernardo, Melchior, Tolazzi et al. | — |
| `elizalde2019oxidative` | Elizalde | McNeice, Kim, Ghahreman | — |
| `gao2023separation` | Gao | Zhang, Azimi | yes |
| `ghidini2019cloud` | Ghidini | Sefrou, Belkhouche | — |
| `hou2024adsorption` | Hou | Xu, Yin, Ning et al. | yes |
| `huang2002rare` | Huang | Wang, Lei, Chi et al. | yes |
| `huang2004rare` | Huang | Zhang, Wang, Tong et al. | — |
| `kim2019separation` | Kim | Yoshida, Kubota, Baba et al. | yes |
| `kim2020characteristics` | Kim | Han | yes |
| `kim2022facile` | Kim | Bediako, Kang, Yun et al. | yes |
| `kumar2022separation` | Kumar | Li, van de Ven, Li et al. | yes |
| `kumar2023comprehensive` | Kumar | Khamis, Hegab, Banat et al. | yes |
| `li2024thermodynamic` | Li | Ghosh | yes |
| `liu2019selective` | Liu | Silva, Morais, Oliveira | — |
| `liu2021theoretical` | Liu | Peng, Su, Li et al. | yes |
| `lorenz2023recovery` | Lorenz | Böhm, Czerski, Gottlieb et al. | yes |
| `meng2024efficient` | Meng | Ghaly, Youssef, Borai | — |
| `moyer2011overview` | Moyer | Tachimori, Morita | yes |
| `murase1999extraction` | Murase | Ozaki, Machida, Adachi | — |
| `oztug2024overview` | Oztug | Peng, Zhu, Zou et al. | yes |
| `pak2020progress` | Pak | Judge, Azimi | — |
| `pal2019complete` | Pal | McCarty, Delaney, Danielsen et al. | yes |
| `pesavento2021versatile` | Pesavento | Lackey, Bottenus, Liezers et al. | yes |
| `priftis2012early` | Priftis | Veis | yes |
| `ram2020separation` | Ram | Talan, Huang | — |
| `ramasamy2017selective` | Ramasamy | Giret, Hu, Masoumifard et al. | yes |
| `schmitz2022lanmodulin` | Schmitz | Gutenthaler, Tsushima, Steudtner et al. | yes |
| `shaw1997isolated` | Shaw | Wójcik, Góral, Pawłowski et al. | yes |
| `sing2025polyelectrolyte` | Sing | Li, Li, Brink et al. | yes |
| `spruijt2014polyelectrolyte` | Spruijt | Wang, Schlenoff | yes |
| `szczesniak2021alkyl` | Szcześniak | Virtanen, Perämäki, Helttunen et al. | — |
| `wang2021strategy` | Wang | Sui, Huang | yes |
| `wang2023polyelectrolyte` | Wang | Bediako, Lim, Repo et al. | yes |
| `wang2025quantification` | Wang | Rodriguez, Watkins, Faraji et al. | yes |
| `wang2025role` | Wang | Sathyavageeswaran, Pandey, Holmlund et al. | yes |
| `xia2024experimental` | Xia | Xue, Lv, Wang et al. | yes |
| `yang2021recovery` | Yang | Yin, Xue, Yan et al. | yes |
| `yao2025computationally` | Yao | Sajeevan, Acharya, Ferdous et al. | yes |
| `zhang2021high` | Zhang | Xu, Li, Xia et al. | — |
| `zhang2022driving` | Zhang | Chen, Wang | yes |
| `zhang2024remarkably` | Zhang | Sengupta, Goyal, Prava Mantry et al. | yes |
| `zhao2022selective` | Zhao | Vaziri Hassas, Rezaee | — |
| `zheng2019mechanism` | Zheng | Xing, Cheng, Yang et al. | yes |
| `zhong2021thermoresponsive` | Zhong | Kafetzi, Borchert, Steinbach et al. | yes |

One apparent author mismatch is not one: `lopez2018application` records
`L\'opez` in LaTeX and the registry writes `López`. Same person.

## Two DOIs pointed at preprints (fixed)

`afonin2024extraction` and `yang2024investigation` carried preprint DOIs
(`10.20944/preprints…`) while naming a journal. Both published versions were
located and the DOIs replaced:

- `afonin2024extraction` -> `10.3390/compounds4010008`, *Compounds* **4**(1)
  172--181 (2024). The entry had named *Minerals*.
- `yang2024investigation` -> `10.3390/ma18071538`, *Materials* **18**(7) 1538
  (2025). The entry had named "PMC", which is a repository, not a journal.

## The 70 entries without a DOI

These are agency reports, standards, company pages, encyclopaedia articles,
theses and books -- sources that legitimately have no DOI. They are checked by
resolving their URL or their ISBN, which establishes that the page exists but
not that its content matches. Twenty-one of them are cited in the book. They
remain the weakest link in the bibliography and are the right place to look
next.

## Method

`citecheck.py` compares, for every entry with a DOI: title (against both the
bare registry title and title-plus-subtitle, since either may be the form in
common use), first-author family name against the whole registry author list,
year, container title against every `container-title` the registry returns
(proceedings return `[series, volume-title]`), volume and pages. An entry whose
`note` field already explains a divergence is reported separately rather than
as an unexamined mismatch.

## Stage three: the entries that have no DOI

A DOI check cannot touch an agency report, a company page or a book, and the
earlier passes settled for resolving the URL. That establishes that a page
exists. It does not establish that the page says what the entry claims, and for
a book that is going to be read in public it is the weaker half of the
question. Every one of the twenty-one cited entries without a DOI was therefore
opened and read against the sentence citing it.

Six failed.

| Key | What it was cited for | What the source actually is |
|---|---|---|
| `fmi2024titanium` | carbochlorination of rutile in fluidized beds at 900--1050 °C | a market-research preview page containing no carbochlorination, no fluidized bed and no temperature |
| `lomon2024titanium` | "safely and economically at very large scale ... over seven decades" | a corporate key-facts page giving capacity numbers and nothing else |
| `engell2023could` | integrated Al/REE carbochlorination of end-of-life material | a SINTEF blog post of 28 March 2019 **by Bjarte Øye**, about aluminium, with no mention of rare earths |
| `tic2024processing` | cascade distillation of REE chlorides | tanb.org: "Membership Required --- You must be a member to access this content" |
| `osti2021process` | coal fly ash at 250--800 ppm REE, Appalachian average 591 ppm | OSTI 1808739 is Zhang and Honaker on **acid mine leachate**; the entry's author, title and year were all invented and the record contains none of these figures |
| `csiro2024minerals` | chlorination "one of several established industrial options" in China | the report says the opposite: chlorination roasting "is being investigated at lab scale" |

Two more were weak rather than wrong. `energy2011critical` was cited for the
definition of the rare earths by a DOE strategy document that never mentions
scandium, and the two `britannica*` entries were encyclopaedia articles doing
the work of technical sources.

### What replaced them

Where the claim was true and only the citation was bad, a real source was
found; where the claim was the problem, the claim went.

- The fly ash grades are Taggart, Hower, Dwyer and Hsu-Kim, *Environmental
  Science & Technology* **50**(11) 5919--5926 (2016), who measured more than a
  hundred U.S. ashes and report 591 mg/kg for Appalachian, 403 for Illinois
  basin and 337 for Powder River basin [@taggart2016trends].
- The fluidized-bed chlorinator is Morris and Jensen, who measured rutile
  chlorination rates over 1143--1311 K [@morris1976fluidized], and Zhou and
  Sohn, who modelled the same reactor [@zhou1996mathematical]; the process
  context is the USGS Minerals Yearbook titanium chapter [@usgs2020titanium]
  and Zhang, Zhu and Cheng's review [@zhang2011literature].
- The list of chloride-process producers now comes from the USGS rather than
  from Britannica, and the Kroll magnesium-chlorine loop from Habashi.
- The Nb/Ta cascade-distillation sentence and the Al/REE co-processing sentence
  were rewritten to say plainly that they are conjectures of ours, which is
  what they always were.
- The UNEP figure was misquoted. The report's finding is that fewer than a
  third of some sixty metals surveyed have an end-of-life recycling rate above
  50 % and thirty-four are below 1 %; the book had said "32 of the 37 specialty
  metals" and put quotation marks around a phrase that is not in the report.

Six entries went to `references-rejected.bib`, four peer-reviewed replacements
were added, and `engell2023could` and `anon2024technology` were rewritten under
their real authorship as `oye2019chloride` and `rer2026technology`.

### The fifteen that hold

The rest were read and stand: the two DOE Moab pages, which the text follows
closely enough to be near-quotation (ammonia and uranium as the groundwater
contaminants of concern, young-of-year endangered fish in the backwater
channels, 1,002,109 lb of ammonia and 5,816 lb of uranium kept out of the
Colorado); the EPA rare earth review, EPA/600/R-12/572, by Reisman and Weber;
the USGS titanium chapter, by Joseph Gambogi; Castor and Hedrick in *Industrial
Minerals and Rocks*; Habashi's *Handbook of Extractive Metallurgy*; the CRC
Handbook, 97th edition; Chi and Tian's Nova monograph; the CEA Atalante paper;
and the INL FY 2010 summary report.

Four entries were corrected in passing: `usgs2020titanium` now credits Gambogi
rather than the agency, `csiro2024minerals` credits its six named authors and
carries the report's real title, and `chi2008weathered` carries an ISBN and a
library record because the publisher's own page refuses automated requests.

### Uncited web sources

Seventeen uncited entries were also removed --- two Britannica articles, a
Wikipedia page, six vendor and supplier pages, three content-marketing blogs, a
paywalled consultancy note, and one whose URL was a bare domain with no
document behind it. None of them was cited anywhere in the book, so none
reached the site, but a bibliography that carries them invites the reader to
wonder what else is in it.

## Stage four: does the cited paper say it?

The first three stages asked whether the citation is *real*. This one asks
whether it is *right*: for every sentence in the book that rests on a citation,
does the work cited actually contain the claim being made? A DOI that resolves
to the correct paper with the correct authors is still a bad citation if the
paper says something else.

Every DOI-bearing citation instance in the book was read this way --- 883 at the
start of the pass, across 388 distinct entries. The work was fanned out over
thirteen parallel agents, one or two chapters each, and each returned a report
naming the sentence, the key, the claim, and what the source says instead.
**Those reports were treated as leads, not verdicts.** Every finding that would
change the book was re-verified by hand against a primary source --- publisher
abstract, accepted manuscript, repository copy, or full PDF where one could be
reached --- before a word was changed. Several agent findings did not survive
that check and were discarded.

Fifty-nine claims did not survive it. They fall into four kinds.

**The claim is not in the paper at all.** The largest group, and the least
interesting individually: a number, a table, or a mechanism attributed to a
paper that contains no such thing. The `obrien2024simplified` CAPEX table, the
`larochelle2021fundamental` sensitivity rows, four of five
`mugion2025systematic` reduction rows, the `touma2024intensification` Zn/Mn
separation factors, `zhou2019controlled`'s "10--1000×" mass-transfer
enhancement, `cui2016high`'s "SF > 50", `orefice2019selective`'s ionic
hydrotropes, `uversky2015intrinsically`'s "30--40 % of the eukaryotic
proteome". These were deleted, or replaced by what the paper does report.

**The paper is about something else.** `murase1995recovery` is chemical vapour
transport with AlCl₃, not a carbochlorination intermediate. `hua2014selective`
is molten MgCl₂--KCl, not chlorination roasting plus water leaching.
`ma2000lanthanide` is an EF-hand grafted for magnetic alignment in solution NMR,
not EF-hand dimerization. `chen2025lanmodulin` is crude protein from a leachate,
not rational design. `suli2017rare` --- the one case where the full PDF could be
read rather than an abstract --- has no chlorination content whatever, and the
stoichiometric chlorine feed cited to it was invented. In each case the entry
was re-homed onto a claim it does support rather than dropped, since the paper
is real and usually worth citing somewhere.

**The paper says the opposite.** The most damaging kind, because the sentence
reads as though it has support. `zhang2022driving` was cited for counterion
release and argues against it. A DGA bullet in chapter 13 asserted "negative
ΔH with positive ΔS, driven by both factors" and contradicted the bullet three
lines above it, which correctly reports DGA extraction of Am(III) and U(VI) as
enthalpy-driven with entropy opposing; neither cited work contains it. `dessimoz2008liquid` was cited for a mass-transfer
coefficient specific to slug flow, and its headline finding is that slug and
parallel flow give the *same* coefficient. `csiro2024minerals`, caught in stage
three, said chlorination is at lab scale where the book had it established
industrially. The halloysite and kaolinite roles in the ch06 clay passage were
backwards in both directions.

**A real number wearing the wrong unit.** Worth naming separately because no
resolve-the-DOI check will ever catch it: the "49 % conversion" attributed to
the MgO carbochlorination work is that paper's **49 kJ/mol activation energy**,
migrated into a percentage. The number is real and the paper is right; only the
quantity is wrong.

One finding was neither --- it was a claim the book made that has since been
**falsified by new work**. The book said no protein system had been shown to
fractionate an adjacent heavy pair. Choi et al., *JACS* 148(34) 36817--36831
(2026), report an average adjacent-element separation factor of 2.1 across
Nd--Lu for Al-LanM and its variants, and on-column tandem dimers that nearly
double SF(Nd/Dy) and separate Y, Dy, Gd, Sm and Nd to >95 % purities from an
allanite-derived leachate. Both places the claim appeared were rewritten, and
the paper added to the bibliography.

### What could not be verified

Ten claims rest on papers that no route available to this pass could reach ---
Elsevier and Springer serve nothing to automated requests and are excluded from
the Wayback Machine, and several institutional repositories 404 on their own
handles. They are `heo2025extraction`, `gupta1984extractive`, `chen2025process`,
`xue2025carbochlorination`, `marcus1991thermodynamics`, `amaral2010thorium`,
`hung2020separation`, the Mountain Pass block in `kim2025rare`,
`yang2022pilot`'s throughput and `chen2017fast`'s enrichment factor. None is
asserted on faith: each is either softened to what its title and metadata
guarantee, or the text says in so many words that the figure is not available.
The two that most deserve a look by someone with a subscription are
`amaral2010thorium` (the amine class, in a passage whose whole purpose is to
police the misreporting of amine class) and the `kim2025rare` Mountain Pass
figures, which the chapter now leans on as its internally consistent chain.

### What this method cannot reach

A claim-by-claim audit keyed on `[@citation]` walks straight past any sentence
that carries no citation at all, and chapters 10 and 16 each contain specific
numeric figures of exactly that kind. They are the obvious next thing to check,
and they need a different query --- find the numbers, then find their sources ---
rather than another pass over the bibliography.

### Seven keys renamed

Separately, seven entry keys had a stem naming someone who is not the paper's
first author --- artefacts of an earlier draft, invisible in the rendered book
but misleading to anyone reading `references.bib`. The entries themselves were
correct; only the labels were wrong. All seven were renamed, in
`references.bib`, in `src/08-coacervates.md`, in `src/93-appendix-provenance.md`
and in `tools/figures/fig_coacervate.py`:

| Old key | New key | Registry first author |
|---|---|---|
| `spruijt2014polyelectrolyte` | `wang2014polyelectrolyte` | Wang & Schlenoff |
| `kim2022facile` | `bediako2022facile` | Bediako |
| `depierro2008cloud` | `mustafina2006cloud` | Mustafina |
| `pal2019complete` | `mccarty2019complete` | McCarty |
| `zhang2022driving` | `chen2022driving` | Chen & Wang |
| `gao2023separation` | `zhang2023separation` | Zhang & Azimi |
| `chen2025lanmodulin` | `chhantyal2025lanmodulin` | Chhantyal |

`depierro2008cloud` carried a wrong year as well as a wrong name --- the paper
is 2006 --- so the new key corrects both.

### Nine `&amp;` leaks in journal names

Fixing the keys turned up a second cosmetic defect from the same source. Nine
entries whose journal name contains an ampersand had it stored as `\&amp;` ---
the HTML entity CrossRef returns, escaped for BibTeX --- and it was rendering
in the public bibliography as *Environmental Science &amp; Technology*, *ACS
Applied Materials &amp; Interfaces*, and so on, in seven of the visible
entries. All nine now hold `\&`.
