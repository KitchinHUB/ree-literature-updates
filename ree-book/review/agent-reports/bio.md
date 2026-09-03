# Agent report: `bio` — FIXPLAN B8

**Scope:** `src/08-coacervates.md`, `src/11-biological-biomimetic.md`.
**Also written:** `review/bib-additions/bio.bib`, this file.
**Not touched:** `references.bib`, `myst.yml`, `review/FIXPLAN.md`, and every file
owned by another worker. No build run, no `git add`, no `git commit`.

## 1. The core finding

The book conflated two different selectivities under one word. Both are now
separated everywhere in my two files, and the separating language is explicit:

- **Ln/non-Ln (group).** Real and enormous. LanM responds to *picomolar* Ln³⁺
  (La–Lu and Y) but only to *near-millimolar* Ca²⁺ — of order 10⁸-fold. Source:
  Cotruvo et al., *JACS* 140:15056 (2018), verified via CrossRef + PubMed
  (PMID 30351021); the abstract states this directly. The book had been citing
  this figure to `@cotruvo2023enhanced`, a different paper that does not contain it.
- **Ln/Ln (intra-group).** Weak. Mex-LanM's preference across the whole series is
  **about fivefold**, light over heavy, and every lanthanide plus Y³⁺ induces
  essentially the same conformational change. Source: the Hans-LanM Nature 2023
  paper's own full text (Europe PMC).

Seven orders of magnitude separate those two numbers, and only the second is the
quantity a fractionation cascade consumes. That sentence, in some form, now
appears in both chapters.

## 2. The ">100-fold" number

`>100-fold` is the ratio of **dimerization affinities** between the La³⁺- and
Dy³⁺-loaded forms of Hans-LanM. It is not a separation factor, and La/Dy is not
an adjacent pair — nine places apart, on opposite sides of the light/heavy split.
Every site that presented it as a separation factor now names the pair and says
what it does and does not imply.

I went to the primary full texts and recovered the numbers the book should have
been quoting all along. **All of these are now in the book with their pair type
labelled:**

| System | Pair | SF | Pair type |
| --- | --- | --- | --- |
| Hans-LanM column | Nd/Dy | 8.12 ± 0.40 | light/heavy split |
| Hans-LanM(R100K) column | Nd/Dy | 12.7 ± 1.3 | light/heavy split |
| LanD–E75Q/E78A | Ce/La | 3.0 ± 0.4 | **adjacent** |
| LanD–E75Q/E78A | Pr/Ce | 1.7 ± 0.2 | **adjacent** |
| LanD–E75Q/E78A | Nd/Pr | 1.4 ± 0.2 | **adjacent** |
| LanD–E75Q/E78A | Nd/La | 7.3 ± 0.9 | three apart |

The best adjacent-pair separation factor any protein system has produced is
therefore **1.4 to 3.0** — inside the same band as conventional acidic
organophosphorus extractants (1.5–3.0), not a hundred times better. The
single-stage Nd/Dy column result is genuine, but its mechanism is a modest SF
amplified over many theoretical plates, not a large SF.

## 3. Citation swap — verified, then fixed

Verified independently against CrossRef and PubMed before touching anything:

- `@cotruvo2023enhanced` — Hans-LanM, metal-sensitive **dimerization**, the
  **Nd/Dy** column separation. (Note: its true first author is **Mattocks**, not
  Cotruvo; the key is misleading but the key is not mine to rename.)
- `@park2024modulating` — **LanD**, a periplasmic lanthanide chaperone that is
  *not* lanmodulin, engineered at the dimer interface to enrich Pr/Nd over La/Ce
  among the **light lanthanides**. True authors: Larrinaga, Jung, Lin, Boal,
  Cotruvo.

The two were swapped in ch. 8 at both Nd/Dy sites. Fixed. I also added the fact
that `@park2024modulating` is about LanD and not LanM — the book nowhere said so,
which is part of why the numbers drifted between proteins.

## 4. Changes made

### `src/08-coacervates.md` (6 sites)

1. **Headline bullet (~24–32).** Rewrote to claim group separation only, with the
   10⁸ Ca²⁺ figure correctly sourced, an explicit statement that neighbour
   discrimination is weak, and a forward reference to the ch. 11 section.
2. **SF comparison paragraph (100).** Replaced the bare `"SF > 100"` claim with the
   explanation of what that number actually is, plus the six measured SFs above.
3. **LBT section (~140–148).** Deleted a bullet asserting picomolar affinity and
   10⁸ Ca²⁺ selectivity *for lanthanide-binding tags* citing `@cotruvo2023enhanced`
   — wrong paper and wrong molecule. Replaced with a sourced statement that LBTs
   are micromolar and LanM picomolar, six orders of magnitude apart.
4. **Lanmodulin subsection (154–165).** Rewritten as two explicitly labelled
   properties (Ln³⁺ vs everything else / Ln³⁺ vs Ln³⁺), then the ">100-fold is not
   an SF" paragraph, then the LanD paragraph with the adjacent-pair numbers.
5. **Heavy-REE bullets (302–303).** Unswapped the two citations; added that Nd/Dy
   is a light/heavy split and that no protein system has fractionated an adjacent
   heavy pair such as Dy/Ho.
6. **Conclusion item 1 (464).** Now says "highest ***group*** selectivity" and
   places these ligands at upstream concentration and group separation rather than
   adjacent-pair fractionation.

### `src/11-biological-biomimetic.md` (5 sites)

1. **Opening (8–40).** Rewritten around "biology solved one half of the problem
   and left the other untouched," with the two selectivities defined as terms of
   art before any number is quoted.
2. **Binding-properties table (59–70).** Added a **Source** column so every row
   carries its citation; split the single "selectivity" row into Ln/Ca and Ln/Ln
   rows; added two interpretive paragraphs tying the rows to the pregnant leach
   solution of `[](#hydrometallurgical-leaching)`.
3. **Metal-Sensitive Dimerization (101–176).** Rewritten. Removed two unsupported
   bullets — "achieves higher separation factors than standard lanmodulins" and
   "comparable or better than common industrial extractants (e.g. HDEHP)" — the
   second of which was the false claim in compact form. Added the sourced SF table
   with a **pair-type column**, and a paragraph reading the 0.043 → 88 mol%
   result as the *purity/concentration* figure it is.
4. **New `#### Where Lanmodulin Belongs in a Flowsheet`.** The constructive half of
   the fix: upstream group separation from PLS is where LanM is strong and where
   the water/acid/reagent burden actually sits; the adjacent-pair cascade is where
   it is weak. Cross-references `[](#hydrometallurgical-leaching)`,
   `[](#solvent-extraction-fundamentals)`,
   `[](#environment-techno-economics-and-life-cycle)`,
   `[](#the-landscape-of-separation-technologies)`.
5. **Final comparison table (~745).** Split the Selectivity column into **Group**
   and **Intra-group**; added a LanD row; added a "Not demonstrated" footnote.

### `review/bib-additions/bio.bib`

One entry, `cotruvo2018lanmodulin` (JACS 140:15056, DOI 10.1021/jacs.8b09842),
CrossRef- and PubMed-verified, with the verifying abstract quotation in a comment.
It is the correct primary source for the 10⁸ Ln/Ca figure and the
picomolar-across-the-series Kd, both of which the book had attributed elsewhere.

## 5. Changes needed in files I do not own

**`src/04-technology-landscape.md:177`** — the technology table row
`Lanmodulin | Separation Factor: High` is the same error in its most compressed
form. It needs the Selectivity/SF column split into group and intra-group, or at
minimum the element pair named. Correct entries: group ~10⁸ vs Ca²⁺; intra-group
SF 8–13 (Nd/Dy, light/heavy split, dimerizing-variant column) and 1.4–3.0 for
adjacent pairs (LanD). My ch. 11 flowsheet section explicitly cross-references
this table on the point that a separation factor without its pair is meaningless,
so the two should be reconciled.

**`src/12-membranes-mofs-emerging.md`** — the MOF figures **Pr/Lu = 796** and
**Nd/Er = 273** are widest-pair or wide-split numbers presented in the same
position a reader expects an adjacent-pair SF. Same error class as B8, different
material. Each needs its pair type named. (I understand another worker is on ch. 12.)

**`src/90-glossary.md`** —
- Add an **EF-hand** headword; the term is used ~15 times across the book and is
  never defined.
- Add **lanmodulin** and **lanthanide binding tag** entries that state the group /
  intra-group distinction, so the distinction survives outside ch. 8 and 11.
- `90:143–147` states a specific research result as though it were a definition;
  it should be a definition, with the result left to the chapter.
- `90:177–181` gives a hydrated-radius mechanism for the MOF entry that does not
  match how the mechanism is described in the chapter.
- **Separation factor**, **enrichment factor**, **concentration factor** and
  **decontamination factor** are used interchangeably in places. They are four
  different quantities and B8 is largely a consequence of blurring the first
  with the others. Worth four distinct entries.

**`src/09-microfluidic-separations.md:155`** — checked, attributes Nd/Dy correctly.
**No change needed.**

## 6. Bibliography defects found (I cannot edit `references.bib`)

- `park2024modulating` — wrong authors; correct: Larrinaga, Jung, Lin, Boal,
  Cotruvo. Subject is **LanD**, not lanmodulin.
- `cotruvo2023enhanced` — first author is **Mattocks**, not Cotruvo.
- `mattocks2019structural` — wrong authors; correct: Cook, Featherston, Showalter,
  Cotruvo. Pages should be 120–125.
- `deblonde2021natural` — actually Daumann, L. J. (sole author), *ACS Central
  Science* 7:1780–1782; the entry gives the journal as *Chemical Science*. **This
  key is now orphaned book-wide**: it supported a claim I removed as unsupported,
  and no other file cites it.
- `deblonde2020selective` — author list partly wrong.
- `li2019coassembly` — appears in **both** `references.bib` (line 2997) and
  `references-rejected.bib` (line 473). It survives in the live bib, so I left the
  pre-existing citation in ch. 8 (~131) alone; flagging it because a key on both
  lists is a bookkeeping hazard. Not mine, not part of B8.

## 7. Honest caveats

- **The "~25-fold Kd variation" framing in FIXPLAN could not be verified.** The
  underlying "0.4–10 pM across the series" range does not appear in any primary
  abstract or open-access full text I could reach. Rather than state an
  unverifiable number as the load-bearing claim, I rested the argument on two
  figures I did verify — picomolar for all of La–Lu and Y (JACS 2018), and the
  **~fivefold** light-over-heavy preference (Nature 2023 full text) — and demoted
  the 0.4–10 pM range to a parenthetical. The qualitative conclusion is unchanged
  and in fact stronger: fivefold across the *entire series* is a weaker
  intra-group selectivity than 25×, so the book's corrected claim is more
  conservative than FIXPLAN assumed.
- **FIXPLAN site `11:291` does not exist.** `git show HEAD:./src/11-...` finds no
  `park2024` or `Nd/Dy` text there. The `@park2024modulating` Nd/Dy misattribution
  lived only in ch. 8, at two sites, both fixed.
- **One cross-reference dropped.** I initially wrote an intra-file link to a
  heading that carries no `(slug)=` label; rather than emit a broken reference I
  rewrote it as prose. If the orchestrator wants that link, the heading needs a
  label first.
- Every `[@key]` in both my files resolves against `references.bib` plus my one
  addition. No key I introduced is on the rejected list.
- No Kd, separation factor, recovery, purity or TRL in either file is unsourced.
  Where I could not source a number, I deleted the claim rather than soften it.
