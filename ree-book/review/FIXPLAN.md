# Fix plan — 2026-09-03 review

30 work items from `review/proposed-issues.md`. Detail behind each lives in
`review/raw/`. One commit per item. Check off as completed.

Severity: **B** wrong and load-bearing · **M** wrong or unsupported but contained
· **G** missing content · **P** production/consistency.

Rule inherited from PLAN.md: 67 citations were deleted during verification. Any
claim resting solely on one of those must be removed or rewritten, never left
standing unsupported. Corollary from this review: a citation that *resolves* is
not thereby *correct* — check that the cited work contains the claim.

---

## B1 — Fix the sign of the pH slope book-wide
`src/03-solvent-extraction-fundamentals.md:17,261,264-266,420-422,820`, `src/13-extraction-thermodynamics.md:688`

From `K_ex = [REL₃][H⁺]³ / ([RE³⁺][(HL)₂]³)`, `D = K_ex[(HL)₂]³/[H⁺]³`, so
`log D = log K_ex + 3 log[(HL)₂] + 3 pH`. Slope of log D vs pH is **+3**;
slope vs log[H⁺] is −3. Ch. 3 currently writes the equation itself with −3 pH,
which is wrong; `03:275-280`'s table (log D rising with pH) is right.
Fix every occurrence, keep one convention, and say explicitly which variable the
slope is taken against.

- [x] B1

## B2 — Ch. 1 states the lanthanide contraction two ways
`src/01-why-separation-is-hard.md:14` "roughly 0.01 Å per element" vs `:48`
"only decreasing by ~0.01 Å across the lanthanide series". 15× apart. `:14` is
right (La³⁺ 1.032 Å → Lu³⁺ 0.861 Å, CN 6: 0.171 Å over 14 steps ≈ 0.012 Å/step).
Fix `:48` and make the two statements quote the same number.

- [x] B2

## B3 — The prologue's exemplar DOI resolves to an unrelated paper
`src/00-prologue.md:226`. `10.1016/j.mineng.2023.108234` → "Effect of pyrite
textures and composition on flotation performance: A review". The prologue's
whole lesson is that a resolving-but-wrong DOI is the most dangerous failure
mode, so the example must be a real, checked DOI (or explicitly labelled as the
pyrite paper to make the point).

- [x] B3

## B4 — Ch. 3: inverted extraction order and two wrong worked examples
- `03:749` "La extracts preferentially (higher K_ex)" — inverted for D2EHPA
  (D rises La→Lu); raffinate and loaded-organic assignments are swapped.
- `03:638` D = 10 at O/A = 1/3 → E = D(O/A) = 3.33 → one stage gives 77%, not 97%.
- `03:631-645` phase-ratio / concentration-factor section: three wrong equations.
Fix the chemistry, then state the series trend explicitly (D rises La→Lu for
acidic organophosphorus extractants; Y falls near Ho/Er).

- [x] B4

## B5 — Ch. 13: close the thermodynamic cycle, fix the hydration energies
- `13:71,119-121,139` ΔG₂ written `REE³⁺(g) + 3HL(g) → REEL₃(g)`: charge and
  protons unbalanced. Missing gas-phase deprotonation ≈ +4,000 kJ/mol.
- `13:97,113-114` ΔG₁ ≈ 1,250-1,400 kJ/mol; Marcus gives 3,145 (La) to 3,515 (Lu).
- `13:340-352` "reality check" blames ±35 log units of solvation noise for a
  10⁷⁸⁸ discrepancy; the cause is the missing term.
- `13:324-330,428-444` pH-dependent "K_ex" and a self-correcting derivation
  ("Wait, the pH cancels!"). Delete; derive once, correctly.
- `13:401-402` `ΔH = ∂ΔG/∂T` — wrong identity (`ΔS = −∂ΔG/∂T`).
- `14:316-322` La/Y hydration energies inverted and 2-5× too small, from a
  Research Square preprint (`@alizadeh2023deep`).
- `13:143-146,345` UMA/Allegro conflated; the 6.1 kcal/mol MAE is Gupta's Allegro.

- [x] B5

## B6 — Balance every reaction equation in Parts II and IV
`02:98`; `05:251,279,299,302,319,787,788,1019`; `07:41-45,86,515-517`;
`13:665,695`. Write Th(IV) chemistry separately from REE(III) throughout ch. 5
(`05:452,482,521,552`). `05:251` also has the wrong chemistry: dry calcination of
bastnäsite gives REOF + CO₂; HF evolves only on steam hydrolysis.

- [x] B6

## B7 — Audit citations attached to claims their source cannot support
~30 in ch. 7 (tabulated in `review/raw/part2-ch05-07.md`), 5 in ch. 5, 3 in
ch. 14. Each key resolves; the paper does not contain the claim. Rule: the
citation must be to a work containing the claim, or the claim goes.
Also: FJH-Cl₂ cited to `@deng2022rare` in ch. 7 and `@tour2025sustainable` in
ch. 12 — reconcile.

- [ ] B7

## B8 — Rewrite the lanmodulin story around what it actually discriminates
`04:177`, `08:24-27,95,136,151,452`, `11:8-14,37-43,66-70,291`, `12:86`, glossary.
Separate Ln/Ca (10⁸-fold, real) from Ln/Ln (LanM monomer Kd varies ~25× across
the series). Stop quoting the Hans-LanM ">100-fold tighter dimer" affinity ratio
as a separation factor for adjacent lanthanides — La/Dy is not an adjacent pair.
Unswap `@park2024modulating` (light lanthanides) and `@cotruvo2023enhanced` (Nd/Dy).

- [ ] B8

## M9 — Rewrite the Mountain Pass and monazite-digestion descriptions
`05:410-433,478-497,520-533,1053-1080`, `07:304-308`. Mountain Pass was oxidative
roast + HCl leach, not a 70 wt% (or 4 M) H₂SO₄ leach, and "evaporate H₂SO₄" out
of HCl is impossible. Monazite NaOH digestion is 140-150 °C in 60-70 % NaOH at
atmospheric pressure — one number, owned by ch. 5, cross-referenced elsewhere.
`05:583,1006` Alamine 336 is tertiary, not primary.
`05:478-497` direct HCl digestion of monazite: delete or label laboratory-only.

- [ ] M9

## M10 — Ch. 15: four analytical errors
`15:61` ng/g is ppb, not ppt. `15:80` the ¹⁴²Ce/¹⁴²Nd isobar needs R ≈ 10⁵ and
cannot be resolved by any commercial instrument — use another Nd isotope or
correct from ¹⁴⁰Ce. `15:101` "5-10%" is not a detection limit. `15:193-199`
"pKa values of REE-MGDA complexes" mislabels the quantity. `15:239` "decreasing
atomic number ... (Gd → Tm)" is self-contradictory. `15:460-467` non-monotonic
separation factors, uncited.

- [ ] M10

## M11 — Ch. 9: recompute the intensification table
`09:167` kLa 20-400×, printed 100-1000×, propagating to `09:10` and `09:425`.
`09:169` S/V corresponds to a 700 µm channel against "tens of µm" at `09:52` and
"2× over bulk" at `09:76`. Extraction-time enhancement 10-100× (`09:168`) vs
150× (`09:66`). `09:170` "2-6× higher separation factor" cited to two flow-pattern
papers containing no separation factors.

- [ ] M11

## M12 — Ch. 5's waste table is wrong by >10× and mixes bases
`05:1280-1286`. At the chapter's own 0.05-0.3 % grade, one ton REO needs
300-2,000 t of ion-adsorption ore, not 20-50. The bastnäsite row is evidently
concentrate, not ore. Recompute from grade and recovery, label the basis, and
drop the `@jha2016hydrometallurgical` attribution unless the numbers are his.

- [ ] M12

## M13 — Source or delete ch. 7's uncited numerical sections
`07:199-227` (one-step clean process), `365-404` (fluorination), `406-433`
(bromination/iodination — also consider deleting as out of scope), `436-470`
(FJH), `474-567` (MSE, one citation in 90 lines).

- [ ] M13

## M14 — Source or delete ch. 5's uncited flowsheet, energy and cost tables
`05:1042-1170` (three flowsheets, 130 lines, recoveries and energies),
`1337-1353` (energy/CO₂), `1439-1449` (cost), `892-896` (bioleaching recoveries
an order of magnitude above what `@brisson2015bioleaching` reports).

- [ ] M14

## M15 — Source or delete ch. 17's unsourced tables
`17:67-88` (CAPEX/OPEX shares), `106-112` (cost basis undefined, inconsistent by
10-50×), `188-195` (rival TRL table), `259-264` (hotspot shares summing to
75-120 %), `278-284` (water by stage), `316-322` (qualitative LCA-by-method table
for which no comparable study exists), `346-354` (energy intensity).
Resolve the in-table "MDPI 2022" pseudo-citation at `17:241-247`.

- [ ] M15

## M16 — Verify and convert ch. 10's hand-written Sources list
`10:449-473` is the only such list left in the book and contradicts the policy in
`93-appendix-provenance.md`; item 7 misattributes a Hatanaka paper to
"Marsh, M. L."; three items have no author. Meanwhile `10:331-448` — 118 lines
carrying every quantitative claim about borate crystallization, M₄L₄ cages,
H₂PDA and macrophosphi — has zero inline citations. Run the twelve through the
CrossRef pipeline, convert survivors to `[@key]`, delete the list.

- [ ] M16

## M17 — Restore or remove three dangling footnotes
`06:132` (`[^1][^2]`, carrying seven-significant-figure ammonia/uranium tonnages
and the razorback sucker claim) and `09:79` (`[^1]`, carrying "enrichment factors
of 200-450"). No definitions exist anywhere in either file.

- [ ] M17

## M18 — Replace four placeholder-author bib entries
`others2019characterization`, `anon2024efficienta`, `yang2022pilot`,
`tour2025sustainable` — each carries a load-bearing number. Re-key from CrossRef
first authors as in Phase 6. Then grep `author = {[^}]*Authors}` and
`author = {(others|anon)` again.

- [ ] M18

## G19 — Ch. 3: the missing quantitative core
Add: extraction order across the series with the pH₁/₂ trend; the extraction
factor `E = D(O/A)` and single-stage fraction `E/(1+E)`; the Kremser equation;
a Fenske-type `N_min = ln[(x_P/(1−x_P))(x_R/(1−x_R))]/ln β` showing that β = 1.5
and 99.99 % at both ends needs ~45 stages (making ch. 1's "hundreds of stages"
derivable); fractional extraction cascades with REE-on-REE scrubbing (Xu
Guangxian); and saponification of the extractant, which is the origin of the
ammonia effluent problem ch. 6 and ch. 17 discuss.

- [ ] G19

## G20 — Ch. 4: write the promised ion-exchange section
`04:13-18` says IX has no chapter of its own and is covered here; the section
never describes displacement chromatography (EDTA eluent, retaining ion,
self-sharpening bands) or why throughput is limited. ~200 words plus a band
schematic. Add the glossary entry.

- [ ] G20

## G21 — Rebuild the technology comparison table, retire the rivals
`04:171-182` is the canonical one. `07:645-654` and `17:188-195` duplicate it
with different TRLs (FJH 3-4 vs 5-6; membranes 5-7 vs 4-6). One row per Part
II-III chapter with: best reported separation factor **and the element pair**,
feed (synthetic or real), concentration, T/pH, demonstrated scale, TRL with a
one-line justification, and a cross-reference. Delete the other two.

- [ ] G21

## G22 — Ch. 15: how to measure D, and an interference table
The most-used measurement in the group is absent: aqueous-by-difference vs direct
organic analysis, matrix matching, error amplification when D ≫ 1 or ≪ 1, phase-
ratio bookkeeping, equilibration-time checks. Plus a table of REE isotopes and
their principal oxide interferents (¹³⁵Ba¹⁶O→¹⁵¹Eu, ¹⁴¹Pr¹⁶O→¹⁵⁷Gd,
¹⁴³Nd¹⁶O→¹⁵⁹Tb, ¹⁴⁷Sm¹⁶O→¹⁶³Dy, ¹⁴⁹Sm¹⁶O→¹⁶⁵Ho, ¹⁵⁰Nd¹⁶O→¹⁶⁶Er,
¹⁵³Eu¹⁶O→¹⁶⁹Tm, ¹⁵⁹Tb¹⁶O→¹⁷⁵Lu).

- [ ] G22

## G23 — State Part IV's accuracy target and carry it through
`ΔΔG = RT ln β`: an adjacent-pair β of 1.5-3 is **1-2.7 kJ/mol** at 298 K,
against a surrogate MAE of 25 and DFT error of 50-100. The whole computational
programme rests on error cancellation reaching ~1 kJ/mol and the book never says
so. Add to ch. 13 Key Takeaways, ch. 14, and ch. 19's research directions, with
a worked Nd/Pr example.

- [x] G23

## G24 — Ch. 7: the LnCl₃/LnF₃ property table
The intro (`07:8-11,19-20`) promises separation by boiling point; LnCl₃ boil at
1,600-1,750 °C and are the non-volatile products. What volatilises is the
impurity chlorides. Add a table of LnCl₃ mp/bp alongside FeCl₃, AlCl₃, SiCl₄,
POCl₃, ThCl₄, ZrCl₄, TiCl₄, and rewrite the intro to make that the argument.

- [ ] G24

## G25 — Ch. 12: a real membranes section
26 uncited lines for membranes against 215 for scCO₂, in the chapter that names
membranes first. Move the 8 m² HFSLM pilot (`09:149`) and the NdFeB Dy HFSLM
result (`09:359`) out of microfluidics; add NF/UF rejection and flux; state the
limitations the glossary knows and the chapter does not — carrier loss, membrane
lifetime, fouling, and why SLMs have not displaced cascades.

- [ ] G25

## G26 — Expand ch. 16 (recycling) from a 334-word stub
Keep `16:8-24`. Add feedstock inventory with REE contents (NdFeB ~30 wt%,
phosphors, NiMH, FCC catalysts), the standard magnet routes (hydrogen
decrepitation / direct re-sinter; oxidative roast + acid leach + oxalate;
selective leaching; molten-salt and electrochemical), recoveries with citations,
the <1 % global rate with its source (UNEP 2011; Binnemans 2013), and the
copper-salt acid-free route (Prodius 2020) now sitting uncited at `16:56`.
Remove "rivaling ores" (`16:48`) and "50 % since 2015" (`16:44`).

- [ ] G26

## G27 — Ch. 18: expand as a dated snapshot, or cut
208 words, 2022 data, zero citations, "expected to begin in late 2025" in a book
being read in 2026, and not one Chinese producer named despite the premise.
Expand only if someone will own an annual update: a "data as of" line and one
sourced table (operator, site, feed, product, nameplate, status). Otherwise cut
and move the 90 % fact into ch. 1.

- [ ] G27

## G28 — Glossary: ~50 missing terms, four wrong entries
Wrong: `90:48-52` chelator ("nearly every selective REE extractant is a chelator"
— D2EHPA, PC88A, Cyanex 272 and TBP are not); `90:155-159` ionic radius as "the
only property that reliably distinguishes adjacent rare earths" (redox is used
industrially, ch. 10); `90:143-147` a research result asserted as a definition;
`90:109-112` vs `165-167` Gd in both LREE and HREE.
Missing and load-bearing: EF-hand (~15 uses), Damköhler number, enrichment /
concentration / decontamination factor (three distinct quantities), PLS,
bioleaching, precipitation, diluent, modifier, third phase, phase ratio, loading,
McCabe-Thiele, K_ex vs D, pH₁/₂, TRL, plus the synonym map
HDEHP = D2EHPA and PC88A = HEHEHP = P507 = EHEHPA (currently read as six reagents).

- [x] G28

## G29 — Add figures; the book has none
Nine that carry arguments prose cannot: (a) the corrected thermodynamic cycle,
ch. 13; (b) log D vs pH at slope +3, ch. 3; (c) a fractional cascade with
extract, scrub and strip sections, ch. 3; (d) a coacervate phase diagram, ch. 8;
(e) approach to equilibrium vs contact time with the kinetic window marked,
ch. 9; (f) the four flow regimes, ch. 9; (g) precipitation pH and solubility
curves across the series, ch. 10; (h) the LanM EF-hand coordination sphere,
ch. 11; (i) one drawn flowsheet replacing ch. 5's three ASCII ones.

- [ ] G29

## P30 — Sweep conversion damage, duplication, seams and cross-chapter numbers
- Conversion: 41 pandoc `~sub~` markers; `~~` strikethrough at `08:263`; 543
  Unicode sub/superscripts across 14 files; 56 indented code blocks standing in
  for equations; `####` under `##` in ch. 9; raw URLs as references in ch. 13.
- Duplication: ch. 7's two conclusions (`978`, `1008`) and doubled kinetics
  section; ch. 5 re-deriving chs. 6/11/16/17; ch. 14's doubled ML, BO and
  closed-loop sections; ch. 9's doubled numbering-up.
- Seams: "the Sobri paper" and "this report" (`06:74-84,26,146`), "This chapter
  merges two source documents" (`07:33`), "the chemistry fundamentals review"
  (`05:1040`), "This document presents" (`13:660`), "Phase 1 (DFT approach)"
  (`13:131`), "the source reviews" unnamed (`19:18`).
- Numbers: China share (3 values), SX feed spec, extraction pH, Fe removal pH,
  IAC share of HREE supply (50 % vs >90 %), monazite REE profile, HREE boundary,
  bastnäsite spelling (4) and formula notation (3), carbochlorination window (5).
- Appendices: add the citation-verification record to A; B's premise is false for
  two of its six papers — fold into A and write a real further-reading list.

- [ ] P30
