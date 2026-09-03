# Book review — consolidated findings

Date: 2026-09-03. Reviewers: four independent agents, one per slice, each reading
its chapters in full plus the glossary and appendices, with no knowledge of the
others' findings. Raw reports in `review/raw/`.

| Slice | Files |
|---|---|
| Front matter + Part I | prologue, preface, ch. 1-4 |
| Part II | ch. 5-7 (+ ch. 2, glossary) |
| Part III | ch. 8-12 |
| Parts IV-V + back matter | ch. 13-19, glossary, appendices A and B |

Structural counts below are mine, measured across `src/` rather than read.

The book is well organised and much of it is well written — ch. 8, ch. 19, the
introductions to ch. 13 and ch. 17, and ch. 6 were all praised on their merits by
reviewers who had every incentive to complain. What follows is what needs work.

---

## The five findings that matter most

**1. The sign of the book's central equation is written three ways.**
`03:261` and `03:420` give `log D = log K_ex + 3 log[(HL)₂] − 3 pH`, and `03:17`
and `03:264` call the slope −3. `13:450` and `13:483` give `+3 pH`. `13:688`
reverts to `−3`. From `K_ex = [REL₃][H⁺]³ / ([RE³⁺][(HL)₂]³)` the slope of
log D against pH is **+3**, which is also what ch. 3's own table at `03:275-280`
shows numerically. The pH swing is the operating principle of the entire
industry and the book states it incorrectly in the chapter that teaches it.

**2. Ch. 1's founding fact contradicts itself in one file.**
`01:14` "roughly 0.01 Å per element"; `01:48` "only decreasing by ~0.01 Å across
the lanthanide series". These differ by 15×. The first is right and the whole
book's premise rests on it.

**3. The prologue's cautionary example is itself an instance of the error it warns about.**
`00:226` cites `10.1016/j.mineng.2023.108234` as the model of a well-formed issue.
That DOI resolves through CrossRef to "Effect of pyrite textures and composition
on flotation performance: A review" — a resolving-but-unrelated DOI, which is
precisely the failure mode the prologue exists to teach.

**4. Ch. 3's worked examples are wrong in ways a student will act on.**
`03:749` has La extracting preferentially with D2EHPA (inverted: D rises La→Lu),
with the raffinate and loaded-organic assignments swapped. `03:638` gives 97%
recovery for D = 10 at O/A = 1/3, where E = D·(O/A) = 3.33 and one stage gives
77%. The phase-ratio/concentration-factor section at `03:631-645` contains three
wrong equations. There is no extraction factor, no Kremser equation, and no
minimum-stage estimate anywhere in the book, so ch. 1's "hundreds of stages" is
asserted rather than derived.

**5. Ch. 13's thermodynamic cycle does not close.**
`13:71` writes `REE³⁺(g) + 3HL(g) → REEL₃(g)`: charge +3 and three protons on the
left, neutral on the right. The omitted gas-phase deprotonation is ~+4,000 kJ/mol,
which is the size of the unexplained discrepancy the chapter then blames on
solvation noise (`13:340-352`, "±35 log units" against a result of 10⁷⁸⁸).
Separately, `13:113` gives Ln³⁺ hydration free energies of 1,250-1,400 kJ/mol
where Marcus gives 3,100-3,500, and `14:316` inverts the La/Y ordering entirely
(Y³⁺, the smaller ion, is listed as less hydrated) from a Research Square preprint.

---

## Correctness, by theme

### Reaction equations
Unbalanced or chemically wrong: `05:251` (no H on the left; dry calcination gives
REOF, not HF), `05:279`, `05:299`, `05:302`, `05:319`, `05:787`, `05:788`,
`05:1019`, `07:86` (`CeO₂ + 2C + 2Cl₂ → CeCl₃ + 2CO`, Cl 4 vs 3, in the chapter
about that reaction), `07:515-517` (garbled cathode half-reaction; the anode
consumes carbon to CO/CO₂, F₂ evolution is a fault condition), `02:98`,
`13:665`, `13:695` (dimerization mass balance missing the factor of 2).
Thorium is written into trivalent formulas throughout ch. 5 (`(REE,Th)₂(SO₄)₃`
etc.), hiding the Th(IV) chemistry that makes it separable.

### Industrial descriptions
- **Mountain Pass** is given as a 70 wt% H₂SO₄ leach at `05:422` and 4 M at
  `05:1059`, with "evaporate H₂SO₄" (bp 337 °C) out of an HCl solution at
  `05:1067`. The plant was oxidative roast + HCl leach; sulfuric bake is Bayan Obo.
- **Monazite NaOH digestion** appears as 300-400 °C (`05:520`), 140-200 °C
  autogenous (`05:533`), and 140-150 °C in an autoclave (`07:308`). It is
  atmospheric, 140-150 °C, in 60-70% NaOH.
- **Alamine 336** is called a primary amine at `05:583`; it is tertiary.
  Primary-amine Th extraction uses Primene JM-T from sulfate, not HCl.
- `05:478-497` describes direct HCl digestion of monazite, which is essentially
  insoluble in HCl, uncited.
- `07:969` gives global TiCl₄ as 280 Mt/yr; world TiO₂ pigment is ~7-8 Mt/yr.

### Biology
Lanmodulin's 10⁸-fold **Ln/Ca** discrimination is presented as intra-lanthanide
selectivity at `08:24-27`, `08:95`, `11:8-14`, `12:86` and in the glossary, and
the Hans-LanM ">100-fold tighter dimer" affinity ratio is quoted in four places
as "a separation factor >100 for adjacent lanthanides" — La/Dy is not an adjacent
pair and an affinity ratio is not a separation factor. `11:40` gives LanM's own
Kd spread as ~25× across all fifteen elements. `@park2024modulating` and
`@cotruvo2023enhanced` are swapped.

### Analytical chemistry (ch. 15)
`15:61` "2-11 ng/g (ppt range)" — ng/g is ppb. `15:80` proposes resolving the
¹⁴²Ce/¹⁴²Nd isobar by mass resolution, which needs R ≈ 10⁵ (use another Nd
isotope). `15:101` gives an XRF detection limit of "5-10%". `15:193` labels a
table of numbers "pKa values of REE-MGDA complexes". `15:239` has frequencies
decreasing "with decreasing atomic number ... (Gd → Tm)". `15:460-467` lists
non-monotonic separation factors (β(Pr/La) > β(Nd/La)) with no source.

### Arithmetic
`09:167` kLa enhancement is 20-400×, printed as 100-1000×, and the error
propagates to `09:10` and `09:425`. `05:1280-1286` says 20-50 t of ion-adsorption
ore per t REO; at the chapter's own 0.05-0.3% grade it is 300-2,000 t.
`12:207-209` reports "101% extraction". `14:67-69` gives 63% and 74% and
339/1,296 for the same result. `17:259-264` has GWP hotspot shares summing to
75-120%.

---

## Sourcing

**Citations attached to claims their source cannot support.** Ch. 7 has roughly
30 (tabulated in the Part II report), ch. 5 five, ch. 14 three. These look like
keys swapped in during the DOI-repair pass: `@roine2019hsc` (a software manual)
carries a phase-stability finding, `@zhang2015occurrence` (REE in coal) carries
SiCl₄ defluorination, `@wikipedia2024aluminium` carries Oersted 1825, and the
FJH-Cl₂ results are cited to `@deng2022rare` in ch. 7 and `@tour2025sustainable`
in ch. 12. **This is the largest single defect in the book** and the one the
verification pass was not designed to catch: every one of these keys resolves.

**Sections with no citations at all.** Ch. 7: fluorination (`365-404`),
bromination/iodination (`406-433`), FJH (`436-470`), MSE (`474-567`, one citation
in 90 lines), one-step clean process (`199-227`). Ch. 5: three flowsheets
(`1042-1170`, 130 lines including recoveries and energy intensities), energy/CO₂
tables, cost table. Ch. 10: `331-448`, 118 lines carrying every quantitative claim
about borate crystallization. Ch. 17: CAPEX/OPEX shares, hotspot shares,
water-by-stage, energy intensity, and a qualitative LCA-by-method table for which
no comparable study exists. Ch. 16 and ch. 18 have zero `@` keys in the file.

**Structural counts:** 121 tables book-wide, **72 with no citation in or near
them**; worst are ch. 15 (12/17), ch. 17 (10/20), ch. 10 (9/11), ch. 07 (8/12).
Zero-citation chapters: ch. 16 (334 w), ch. 18 (208 w), ch. 19 (1,198 w).
Lowest density: ch. 10 at 2.3 citations per 1,000 words against ch. 8 at 24.6.

**Residue of the source documents.** `10:449-473` is the only hand-written
`## Sources` list left in the book, contradicting the policy stated in Appendix A;
item 7 misattributes a Hatanaka paper to "Marsh, M. L." and three items have no
author. Dangling footnote markers with no definitions at `06:132` (which carries
seven-significant-figure ammonia/uranium tonnages), `06:[^2]`, and `09:79`. Four
bib entries still have placeholder authors and each carries a load-bearing
number: `others2019characterization`, `anon2024efficienta`, `yang2022pilot`,
`tour2025sustainable`.

---

## Gaps — content the book promises or needs and does not have

- **Ch. 3** has no extraction order across the series, no extraction factor or
  Kremser equation, no fractional-cascade/scrubbing treatment (Xu Guangxian), and
  no saponification — the industrial practice behind the ammonia effluent problem
  ch. 6 and ch. 17 discuss.
- **Ch. 4** promises an ion-exchange section at `04:13-18` and never writes it;
  displacement chromatography is never described. Its comparison table omits
  eight Part III technologies and disagrees with the rival tables in ch. 7 and
  ch. 17.
- **Ch. 15** has no procedure for measuring D — the most-used measurement in the
  group — and no ICP-MS oxide-interference table.
- **Ch. 7** promises a volatility-based separation argument and never gives
  LnCl₃ melting or boiling points.
- **Ch. 12** gives membranes 26 uncited lines and scCO₂ 215, while two membrane
  pilot results sit misfiled in ch. 9.
- **Ch. 16** (recycling, 334 words) and **ch. 18** (industrial landscape, 208
  words, 2022 data, "expected to begin in late 2025") are stubs.
- **Part IV never states its own target.** `ΔΔG = RT ln β` puts an adjacent-pair
  β of 1.5-3 at **1-2.7 kJ/mol**, against surrogate MAE of 25 and DFT error of
  50-100. The whole computational programme rests on error cancellation reaching
  ~1 kJ/mol and the book never says so.
- **Ch. 17** has no worked TEA — throughput × price − OPEX, annualized CAPEX,
  payback, one sensitivity.
- **Glossary**: ~50 load-bearing terms undefined at first use, including EF-hand
  (~15 uses), Damköhler number, PLS, bioleaching, precipitation, diluent,
  modifier, third phase, phase ratio, McCabe-Thiele, K_ex, TRL. Four entries are
  wrong: chelator ("nearly every selective REE extractant is a chelator" — D2EHPA,
  PC88A, Cyanex 272 and TBP are not), ionic radius as "the only property that
  reliably distinguishes adjacent rare earths" (redox is used industrially and
  ch. 10 covers it), a research result asserted as a definition, and Gd placed in
  both LREE and HREE. The book presents HDEHP/D2EHPA and PC88A/HEHEHP/P507/EHEHPA
  as six reagents.
- **Appendix A** records the pandoc conversion but not the citation-verification
  pass, so a reader who hits an uncited number cannot tell whether it was ever
  sourced. **Appendix B**'s premise ("no chapter was built from them") is false
  for two of its six papers, which supply ~1,150 words of ch. 14.
- **The book has zero figures.** Nine were nominated as carrying arguments prose
  cannot: the corrected thermodynamic cycle; log D vs pH at slope +3; a fractional
  cascade with extract, scrub and strip sections; a coacervate phase diagram;
  approach-to-equilibrium vs contact time with the kinetic window marked; the
  four flow regimes; precipitation pH/solubility curves across the series; the
  LanM EF-hand coordination sphere; and one drawn flowsheet replacing ch. 5's
  three ASCII ones.

---

## Consistency across chapters

| Quantity | Values found |
|---|---|
| China share of separation | ~90% (`01:58`), >95% (`17:36`), ~90% (`18:12`) |
| China share of mining | ~70% (`01:58`), >70% (`17:36`) |
| SX feed REE concentration | 0.1-1.0 M (`02:125`), 0.5-2.0 M (`05:1494`), 1-2 M (`02:56`) |
| Extraction pH | 0.5-4.0 (`02:120`), 2.5-4.0 (`05:1501`) |
| Fe³⁺ removal pH | 3-4 (`02:116`), 3.5-4.5 (`05:962`), 4 (`05:1065`) |
| IAC share of HREE supply | 50% (`05:635`), >90% (`06:57`) |
| Monazite REE profile | LREE (`05:45`), "middle and heavy" (`02:36`) |
| Monazite H₂SO₄ | 93-98 wt% (`05:455`), 6-12 M (`05:1186`) |
| Halloysite/kaolinite | `06:51` has the weathering sequence backwards |
| HREE boundary | Gd-Lu+Y (glossary), Eu-Lu (ch. 7 tables) |
| Carbochlorination window | five ranges in ch. 7 alone |
| TRL tables | ch. 4, ch. 7 and ch. 17 disagree (FJH 3-4 vs 5-6; membranes 5-7 vs 4-6) |
| Bastnäsite | four spellings; three formula notations |

---

## Structure and production

**Duplication.** Ch. 7 has two conclusions (`07:978` and `07:1008`), the second
concluding about a solvent-extraction section that Appendix A says was dropped
from the chapter; its kinetics section appears twice near-verbatim
(`07:103-124`, `07:126-143`) and one parameter set appears three times. Ch. 5
re-derives ch. 6 (180 lines on ion-adsorption clays), ch. 11 (bioleaching),
ch. 16 (urban mining) and ch. 17 (LCA). Ch. 14 has ML-for-D twice, Bayesian
optimization twice, closed-loop discovery twice, and implicit solvation shared
with ch. 13. Ch. 9 duplicates its numbering-up section.

**Seams from the source documents.** "the Sobri paper" and "the paper that
prompted this report" (`06:74-84`), "This chapter merges two source documents"
in the body (`07:33`), "described in the chemistry fundamentals review"
(`05:1040`), "This document presents" (`13:660`), "Phase 1 (DFT approach)"
project-plan leftovers (`13:131`), "the source reviews" unnamed (`19:18`),
and Conclusions/Key Findings/Research Gaps memo blocks in ch. 5 and ch. 6.

**Conversion damage.** 41 pandoc `~sub~` markers rendering literally as `K~ex~`
(10 in ch. 3 alone, confirmed in the served HTML); `~~` strikethrough corruption
at `08:263` (`~~4 oxidation state ... Ce4~~`); 543 Unicode sub/superscript
characters across 14 files; 56 indented code blocks standing in for equations
and essentially no real LaTeX math anywhere; `####` headings under `##` with no
`###` in ch. 9; missing terminal periods; raw URLs as references in ch. 13.

*(One conversion defect found by this review — `{index}` roles written mid-word,
producing `cat{index}`ion exchange`` at three sites — was a regression in
`tools/tag_index.py` from Phase 5 and has been fixed in `bd47008`.)*
