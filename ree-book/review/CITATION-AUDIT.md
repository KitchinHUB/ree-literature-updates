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
