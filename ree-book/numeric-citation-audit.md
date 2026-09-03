# Numeric citation audit (Phase 4)

Two chapters came from documents that cite by number against a hand-typed
reference list: `07-pyrometallurgical-halogenation.md` (from
`converted/carbochlorination-report.md`, 85 references) and
`09-microfluidic-separations.md` (from `converted/microfluidic-report.md`, 53
references). `tools/convert_numeric_citations.py` rewrites `[7]`, `[11,12]` and
`[5-7]` into MyST citations, but it can only do that once every cited number
resolves to a `references.bib` key.

112 numbers are cited between the two chapters. 46 resolved straight away
against the bibliography assembled in Phase 1. The remaining 66 were checked
one by one against CrossRef, and that check is the point of this document: the
reference lists in these two documents contain **DOIs that resolve to a
completely unrelated paper**, the same failure repaired at scale in
`doi-mismatch-repair.md`. A DOI that resolves is not evidence. The title it
resolves to has to be read.

## What the audit found

| Outcome | Count |
|---|---|
| DOI resolves and the title agrees | 18 |
| DOI resolves to a **different paper**; the real paper was found by title | 9 |
| DOI resolves to a different paper and no such paper exists | 8 |
| No DOI; grey literature (agency, standards body, company, encyclopaedia, book) | 22 |
| No DOI and the described paper does not exist | 9 |

## DOIs that resolve to the wrong paper

Nine references named a real paper but printed a DOI belonging to something
else — usually one character off. Each was recovered by searching CrossRef for
the printed title and confirming the returned record.

| Ref | Printed DOI resolves to | Real paper |
|---|---|---|
| 07 [11] | *(unresolved)* | Xue et al., *Miner. Eng.* 233, 109623 (2025) |
| 07 [18] | Trace elements in indium by GDMS | Anderson et al., *J. Sustain. Metall.* 1, 33 (2015) |
| 07 [29] | Environmental impact of urban consumption | Gorman & Dzombak, *Resour. Conserv. Recycl.* 137, 281 (2018) |
| 07 [49] | Electro-oxidation of sphalerite | Banda et al., *J. Ind. Eng. Chem.* 21, 1290 (2015) |
| 07 [82] | Ta/Nb from tin slags by chlorination | Gupta & Suri, *Int. Mater. Rev.* 29, 405 (1984) |
| 09 [10] | Rheology of waxy crude oils | *Chem. Eng. Sci.* 207, 115223 (2019) |
| 09 [15] | Extractive distillation of an azeotrope | *Chin. J. Chem. Eng.* 42, 1 (2022) |
| 09 [25] | A Cd(II) metal-organic framework | *Polyhedron* 152, 267 (2018) |
| 09 [33] | Hydrogenation of phenol | Kashid et al., *Chem. Eng. J.* 131, 1 (2007) |

Two more named a real paper under the wrong author and year — 07 [20]
("Gaballah & Djona 1994") is Gaviría & Bohé, *Thermochim. Acta* 509, 100 (2010),
and 09 [32] ("Quantitative criteria for solvent extraction in microchannels",
*Chem. Eng. Technol.* 2007) is Dessimoz et al., *Chem. Eng. J.* 160, 882 (2010).
The paper is right, the citation was not.

## References that do not describe any existing paper

Nine references survived neither DOI resolution nor a title search. Under the
Phase 1 rule — a claim resting solely on a deleted citation must be removed or
rewritten, not left unsupported — each was handled individually.

| Ref | Printed as | Disposition |
|---|---|---|
| 07 [9] | Gaballah et al., *Metall. Mater. Trans. B* 26, 711 (1995) | Re-sourced to Gaviría & Bohé on the carbochlorination mechanism |
| 07 [15] | Anderson, *JOM* 68, 3126 (2016) | Re-sourced to Xue et al. (2025), which reports the thermodynamic analysis |
| 07 [23] | Wang et al., *J. Rare Earths* 37, 198 (2019) | Re-sourced to Anderson et al. (2015), the actual source of the >93% Ce/Nd conversion |
| 07 [43] | Zhan & Xu, *Miner. Eng.* 58, 20 (2014) | Re-sourced to Deng et al., *Sci. Adv.* 8 (2022) — the flash Joule heating work the sentence describes |
| 07 [47] | Schreiber et al., *ES&T* 55, 5196 (2021) | Citation dropped: an LCA does not support a list of process limitations, and the parallel advantages list is uncited |
| 07 [59] | Bordbar et al., *Polyolefins J.* 4, 149 (2017) | **Claim corrected.** The sentence asserted TiCl₄ production "exceeding 280 million metric tonnes annually"; world TiO₂ pigment output is single-digit millions of tonnes. The figure was removed and the chloride-route share sourced to the USGS minerals yearbook |
| 07 [69] | Delons et al., *J. Nucl. Mater.* 360, 29 (2007) | Re-sourced to Chen et al., *Sep. Purif. Technol.* (2025) on molten-salt ZrCl₄/HfCl₄ distillation |
| 07 [72] | Nagaiyar & Kishore, *Miner. Process. Extr. Metall. Rev.* 37, 249 (2016) | Citation dropped: the sentence is the chapter's own extrapolation ("could potentially be adapted") |
| 07 [73] | Nell, *J. S. Afr. Inst. Min. Metall.* 112, 13 (2012) | Citation dropped: likewise an extrapolation from the titanium precedent |

Three more in chapter 9: 09 [31] (Sen et al., "CFD simulation of two-phase flow
in microchannels") was dropped from a `[31-33]` group that the two surviving
references carry on their own; 09 [35] did not exist and the sentence resting on
it — a 5-50× kLa enhancement from gas injection — was deleted; 09 [49] was
re-sourced to Yadav et al., *Sep. Purif. Technol.* 194, 265 (2018), which does
report non-dispersive Dy recovery from NdFeB leachates by hollow-fibre supported
liquid membrane.

## The company section in chapter 9

`09-microfluidic-separations.md` closed with four company bullets sourced to
press material — references [39] to [43], none of which carried a title or a
URL that could be checked. Two of them made claims that no public record
supports (a scale-up to 90,000 t/y by 2028, and 99.999% separation in a single
pass), and one identified REEgen, the Cornell spinout working with
*Gluconobacter oxydans*, as "REEtec", an unrelated Norwegian company.

The section was rewritten: the unverifiable numbers are gone, the company is
named correctly, and the remaining statements are explicitly marked as company
announcements rather than measurements.

## Grey literature

22 references are agency reports, standards, encyclopaedia entries, company
disclosures or books rather than journal articles: USGS, IAEA, the US EPA and
DOE, CSIRO, the European Parliament's STOA, the Tantalum-Niobium International
Study Center, India's Nuclear Fuel Complex, Britannica, Wikipedia, and the
Gupta, Habashi, Chi & Tian and Castor & Hedrick volumes. These are legitimate
sources for the background and industrial-practice claims that cite them, and
each was entered in `references.bib` by hand with its URL.

## Guard added to the tool

`tools/convert_numeric_citations.py` now checks that a reference resolved by DOI
or URL lands on an entry whose title matches the one printed in the reference
list, and refuses to rewrite a chapter if it does not. A printed title that is a
prefix of the entry's title is a truncated subtitle, not a mismatch, and is
allowed; four resolutions that legitimately disagree — a reference naming a
database rather than the software holding it, one naming a company rather than
its project, one naming a commodity summary rather than the yearbook chapter,
and one paraphrasing its own title — are listed explicitly in the tool.

Re-running the audit on the 46 references that had already resolved found no
further mismatches. All 112 numeric citations now convert, and the book builds
with 582 citation nodes and no unresolved keys.
