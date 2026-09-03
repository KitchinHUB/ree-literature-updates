# Review: Parts IV–V and back matter

Scope: `src/13`–`src/19`, `src/90-glossary.md`, `src/93-appendix-provenance.md`, `src/94-appendix-further-reading.md`. Read-only. Line numbers are from `cat -n` on the current files.

Two provenance facts that shape the findings below:

- `myst.yml` loads the root `references.bib`, which contains every key cited in this slice (including `gupta2025accelerating` and the four Appendix B papers), so no citation in this slice is broken. `src/references-cited.bib` is a stale subset; ignore it.
- I diffed the chapters against the `converted/` line ranges Appendix A maps them to. The uncited quantitative claims in ch. 15–18 were **already uncited in the source review** (which used hyperlinks, not `cite:` keys). They are not casualties of the verification pass; they were never sourced. The one exception is in ch. 17 (the "MDPI 2022" ionic-clay GWP row, see below).

---

## src/13-extraction-thermodynamics.md

Verdict: the microcalorimetry section is sound and well cited. The thermodynamic-cycle section, which is the pedagogical heart of Part IV, has an unbalanced cycle, a wrong hydration-energy magnitude, a sign error in its final working equation, and a "reality check" that blames the wrong cause for a 700-log-unit discrepancy. A new student who works through it carefully will conclude either that they have misunderstood or that the book has, and the second is correct.

**13:71, 13:119–121, 13:139 — BLOCKER — unbalanced thermodynamic cycle.**
> `REE³⁺(gas) + 3 HL(gas) → REEL₃(gas)` ... `ΔG₂ ≈ E[REEL₃] - E[REE³⁺] - 3×E[HL]`

The left side carries charge +3 and three acidic protons; the right side is neutral. The three H⁺ that ΔG₅ later hydrates (13:230) never appear on the ΔG₂ step, so the cycle does not close. As written, ΔG₂ omits the gas-phase deprotonation of 3 HL, roughly +1,300–1,400 kJ/mol per dialkyl phosphoric acid, i.e. about **+4,000 kJ/mol** in total. That is exactly the size of the discrepancy the chapter then fails to explain (13:330, 13:340–352). Fix: write ΔG₂ as `REE³⁺(g) + 3HL(g) → REEL₃(g) + 3H⁺(g)` (or as `REE³⁺(g) + 3L⁻(g) → REEL₃(g)` plus an explicit 3× gas-phase acidity term), redraw the ASCII cycle with the proton path on it, and state which of the two reactions the DFT/ML "binding energy" of ch. 14 actually refers to. Re-run the worked table (13:273–280, 13:309–316) with the corrected sum.

**13:97, 13:113–114 — BLOCKER — hydration free energy off by a factor of ~2.5.**
> `~1200-1500 kJ/mol for +3 ions` ... `La³⁺: ΔG₁ ≈ 1250 kJ/mol; Gd³⁺: ΔG₁ ≈ 1400 kJ/mol`

Experimental Ln³⁺ hydration free energies (Marcus) are −3,100 to −3,500 kJ/mol (La ≈ −3,145; Gd ≈ −3,375; Lu ≈ −3,515). The chapter's own Born formula at 13:107 with z = 3, r = 1.0–1.2 Å gives ≈ −5,000 to −6,000 kJ/mol, so the quoted numbers agree with neither theory nor experiment. Fix: use the Marcus values, cite them, and note that Born overestimates by ~1.7× for trivalent ions.

**13:688 — BLOCKER — wrong sign in the working equation.**
> `log D ≈ log K_ex + 3 log[HA] − 3 pH + Δγ`

From K_ex at 13:680, `D = K_ex·a_HA³/a_H⁺³`, so `log D = log K_ex + 3 log a_HA − 3 log a_H⁺ = ... + 3 pH`. The earlier section gets this right at 13:450 and 13:483 ("+3 slope"). Fix: `+ 3 pH`.

**Cross-chapter (outside my slice, but blocking): `src/03-solvent-extraction-fundamentals.md:17, :261, :264–266, :420–422, :820`** write the slope as −3 and `log D = log K_ex + 3 log[(HL)₂] − 3 pH`, which contradicts ch. 3's own table at 3:275–280 (log D rises with pH), ch. 13, and the glossary's "pH swing" entry. The book currently states the sign of its single most important equation three different ways.

**13:324–330, 13:436–454 — MAJOR — pH-dependent "K_ex" and thinking-aloud derivation.**
> `log K_ex(pH) = log K°_ex + 3 pH` ... `Wait, the pH cancels!` ... `Actually, the correct formulation is:`

K_ex is a constant; pH enters through D, not K. Defining a pH-dependent K_ex is what causes the double-counting at 13:436–442, and the section then corrects itself in place. A textbook should show the correct derivation once. Fix: delete 13:322–330 and 13:436–444; go from K°_ex to D via the mass-action expression at 13:446–450.

**13:32 vs 13:436, 13:446 — MAJOR — monomer/dimer stoichiometry switches mid-derivation.** The cycle is built for 3 HL; Step 5 suddenly uses `[(HL)₂]³`. Both are defensible but not in the same derivation; the extractant order differs. Pick one (ch. 3 uses the dimer) and say why.

**13:340–352 — MAJOR — the reality check misdiagnoses the failure.**
> `These uncertainties add up to ±150-200 kJ/mol ... ±35 log units!`

±35 log units cannot explain a result of 10⁷⁸⁸. The discrepancy is the missing ~4,000 kJ/mol above, not solvation uncertainty. Once the cycle is balanced, this section becomes true and useful; as it stands it teaches the student that the method is merely noisy when it is actually mis-specified.

**13:143–146, 13:345 — MAJOR — UMA and Allegro conflated; MAE misattributed.**
> `Use Fairchem UMA model ... Following Gupta et al. 2025: MAE ≈ 6.1 kcal/mol` / `(this is why UMA has MAE ≈ 25 kJ/mol)`

Ch. 14:279–281 correctly says the 6.1 kcal/mol MAE is Gupta et al.'s Allegro model trained on 5,356 complexes. UMA is a different (Fairchem universal) model with no REE–extractant benchmark cited anywhere in the book. Fix: attribute the number to Gupta/Allegro; if UMA is what the group plans to use, say its accuracy on this task is untested.

**13:401–402 — MAJOR — wrong thermodynamic identity.**
> `Temperature dependence (via ΔH = ∂ΔG/∂T)`

`ΔS = −∂ΔG/∂T`; ΔH comes from Gibbs–Helmholtz, `∂(ΔG/T)/∂(1/T) = ΔH`, which is what the van't Hoff analysis at 13:505 uses. Fix the identity.

**13:97, 13:125, 13:168, 13:206 — MINOR — "endothermic/exothermic" applied to ΔG.** Sign of ΔG is spontaneity, not heat. Say "positive/negative ΔG".

**13:217 — MINOR — `ΔG₄ ≈ 3 × ΔH_vap (neglecting entropy)`.** Vaporization of pure liquid HL is not desolvation from kerosene, and TΔS_vap is ~25–30 kJ/mol per molecule, i.e. ~40% of the term. Say this is an order-of-magnitude placeholder only.

**Missing, MAJOR — the selectivity target is never quantified.** The chapter says relative predictions are "more robust" (13:369–385) but never states what accuracy selectivity needs. At 298 K, `ΔΔG = RT ln β`, so an adjacent-pair β of 1.5–3 corresponds to **1–2.7 kJ/mol**, against a surrogate MAE of 25 kJ/mol and DFT errors of 50–100 kJ/mol (13:345). The whole Part IV argument rests on error cancellation reaching ~1 kJ/mol, and the book never says so. This one sentence belongs in the Key Takeaways (13:469–483) and again in ch. 14 and ch. 19. It is also the best candidate for a worked example (Nd/Pr with D2EHPA).

**13:525 vs 13:636 — MINOR — TOPO ΔH sign missing.** `Constant ~29 kJ/mol` in the section, `Exothermic (~29 kJ/mol)` in the summary. Write −29.

**13:534–537 vs 13:637 — MINOR — DGA entropy contradicts itself.** "Enthalpy-driven for Am(III)" and "negative ΔH with positive ΔS — driven by both factors" in adjacent bullets; summary table says entropy "Unfavorable". Reconcile against @ansari2011chemistry / @sharov2024specific.

**13:536 — MINOR — `ΔH = −64.94 kJ/mol, ΔS = −144.42 J/(mol·K)`** for an unnamed "novel unsymmetrical DGA" with two-decimal precision and three references, one of which is a bare IAEA URL. Name the ligand and attach the one paper.

**13:547 — MINOR — `Bumim·Tf₂N`** is nonstandard; use [C₄mim][Tf₂N] and expand it once.

**13:529, 13:543, 13:607, 13:615 — MINOR — raw URLs as "References"** (OSTI, IAEA, Nash group page, INL PDF) after the book converted everything else to verified citations.

**13:600–615 — MINOR — "Key Research Groups & Resources"** is literature-review scaffolding, not book content. Cut, or fold Nash/INL into a sentence with a real citation.

**13:640, 13:645 — MINOR — crown ethers appear in the summary table and the "recent developments" list with no citation anywhere in the chapter.** This reads like a claim that lost its source. Cite or drop.

**13:131, 13:141 — MINOR — "Phase 1 (DFT approach)", "Phase 2 (UMA approach)"** and 13:395, 13:458 "an experimental validation dataset" are leftovers from the internal project plan Appendix A says was removed.

**13:660 — MINOR — "This document presents"** (docx leftover).

**13:663 — MINOR — bastnäsite `REE = Y, La, Ce, Pr, Nd, Sm, Gd`.** Bastnäsite is a light-REE mineral, (Ce,La)CO₃F per the glossary; Y belongs to xenotime. Misleading list.

**13:665 — MAJOR — unbalanced dissolution reaction.**
> `REECO3F(s) + 3H+ ⇌ REE3+ + CO2(g) + HF(aq)`

Oxygen: 3 on the left, 2 on the right. Correct: `RECO₃F + 3H⁺ → RE³⁺ + CO₂ + HF + H₂O`.

**13:695 — MAJOR — dimerization "model" is not the mass balance.**
> `[HA]_free = [HA]_tot / (1 + K_d [HA]_tot)`

For `2HA ⇌ (HA)₂` with `K_d = [(HA)₂]/[HA]²`, mass balance is `[HA]_tot = [HA] + 2K_d[HA]²`, a quadratic in the free monomer. The given form has neither the factor 2 nor the free concentration in the denominator. Either derive the quadratic or label this an ad hoc interpolation.

**13:708 — MAJOR — `Mason-style atomistic dissolution thermodynamics`.** "Mason" is never identified or cited, here or anywhere in the book. An attributive claim with no source. Cite the paper or remove the eponym.

**13:669, 13:706 — MINOR — undefined symbols and mixed standard states.** `μ_REE(solid)` is undefined; 13:706 adds `3RT ln a_H⁺` to a ΔG that was just defined as `−RT ln K_ex` (standard). Define, and separate standard from actual.

**Undefined jargon (MINOR):** SMD (13:101), COSMO-RS (13:180; also 14:340), UMA (13:143), B3LYP-D4 (13:131), ITC c-value protocols (13:622). Define once each.

---

## src/14-high-throughput-computational.md

Verdict: the Augustine / An / Liu / Gupta material is the best-sourced writing in the slice. The problems are structural (three ML sections, two Bayesian-optimization sections, two closed-loop sections, and a DFT/COSMO-RS section that duplicates ch. 13) and a handful of numbers that contradict each other or their citation.

**14:67–69 — MAJOR — contradictory efficiency numbers.**
> `using only 63% of experiments` ... `74% reduction in experimental effort` ... `339 total measurements vs. 1,296`

339/1296 = 26%, which is a 74% reduction; "63%" is inconsistent with both. Check @augustine2024advancing and keep one figure.

**14:292–297 — MAJOR — lab platform cited as industrial practice.**
> `Modern plants incorporate [@augustine2024advancing]: Real-time ICP-MS analysis ... Active learning algorithms ... "self-driving" separation plants`

Augustine describes a bench robot, and no commercial REE plant runs active-learning control. This is both a miscitation and an overclaim that contradicts ch. 19:105–107 ("Most automated platforms still depend on offline ICP"). Rewrite as aspiration or delete.

**14:316–322 — MAJOR — hydration energies physically wrong; source is an unreviewed preprint.**
> `Hydration energy: La(III) −383.7 kcal/mol; Y(III) −171.8 kcal/mol`

Y³⁺ is the smaller ion and has the more negative hydration energy (≈ −825 kcal/mol vs ≈ −750 for La³⁺). The ordering is inverted and the magnitudes are off by 2–5×. `alizadeh2023deep` resolves to a Research Square preprint (`10.21203/rs.3.rs-2525701/v1`). "Born–Haber thermodynamics" is also the wrong name for a solvation cycle. Fix: drop the table; if the D2EHPA Y/La point is wanted, cite a peer-reviewed DFT study and quote the Marcus values.

**14:327 vs 14:371 — MAJOR — the same finding attributed to two different ligands and papers.**
> `Binding pocket shrinks from La to Nd to Eu [@liu2021theoretical]` (DGA) / `Binding pocket contraction along La → Nd → Eu series` (BLPhen, @chapleski2020molecular)

One of these is a copy. Keep the one the cited paper actually supports.

**14:368 — MAJOR — probable miscitation.** `chapleski2020molecular` resolves to "A Molecular-Scale Approach to Rare-Earth Beneficiation: Thinking Small to Avoid Large Losses" (iScience), which is about flotation-collector chemistry, not BLPhen extraction MD. The source review linked a PMC ID for this claim; confirm the PMC article is the same paper, and if not, replace with the BLPhen MD paper (Jansone-Popova / Bryantsev group).

**14:213 — MAJOR — unsupported specific claim.**
> `Recent work (2025) developed explainable AI systems to predict REE leaching efficiency ... trained on 572 experimental datasets.`

A dated, numbered claim with no citation. This reads exactly like a sentence that once had a source. Cite or cut.

**14:237 — MINOR — `Polymer solar cells: 75% reduction in discovery time`** uncited.

**14:105–116 — MINOR — vendor product copy.** "FAST Automated Systems" and "SimPrep" are Elemental Scientific products; the bullet lists are catalogue text with no citation. Cite the vendor note explicitly as such, or cut.

**14:197 — MINOR — `D > 1: More than 50% of lanthanide extracted`** is true only at phase ratio A/O = 1. Say so; the phase-ratio dependence is exactly what a new student gets wrong.

**14:178 vs 14:407 — MINOR — `1,202 log D values` vs `Thousands of experimental D values`** for the same Liu 2022 model. And 14:409 `Millions of compounds/day` is uncited.

**14:450 — MINOR — Architector attributed to @summers2024importance.** Summers 2024 uses it; the package paper is Taylor et al., Nat. Commun. 2023. Cite the package.

**14:36 — MINOR — `Unchained Laboratories Inc.`** is Unchained Labs.

**14:279 — MINOR — Gupta year.** `references.bib` says 2025, Digital Discovery vol. 5; Appendix B (94:36) says 2026. Vol. 5 is the 2026 volume; fix the bib year or the appendix.

**Structure — MAJOR — duplication.** ML for D prediction appears at 14:170–199 and again at 14:383–417; Bayesian optimization at 14:54–70 and 14:201–210; closed-loop discovery at 14:217–241 and 14:530–551; implicit-solvation/COSMO-RS at 13:172–184 and 14:339–356; the active-learning gap at 14:234–241 and 19:101–104. Appendix A (93:79–82) says the duplicate high-throughput material was dropped; the computational half was not. Consolidate to one section per topic.

**Undefined jargon (MINOR):** Kriging Believer (14:61), Matérn kernel (14:62), ECFP (14:184), equivariant / Allegro (14:280), GFN2-xTB (14:457), σ-profile (14:346), 12-6-4 LJ (14:380). A student who knows extraction chemistry will not know these.

**Missing (MAJOR):** the chapter never states what reaction the learned "binding energy" is for (see 13:119 blocker) nor how its 25 kJ/mol MAE compares to the 1–3 kJ/mol selectivity target. Without that, "screening at the scale of a ligand library" (14:284) sounds like a solved problem.

---

## src/15-characterization.md

Verdict: broad and mostly correct as a catalogue, but it contains three outright errors in the ICP/XRF sections, which are the sections a separation lab actually uses, and it omits the one procedure every reader will need: how to measure a distribution ratio correctly.

**15:61 — MAJOR — unit error.**
> `Detection limits | 2-11 ng/g (ppt range)`

ng/g is ppb. ppt is pg/g. One of the two is wrong; quadrupole ICP-MS REE limits in clean matrices are typically low-ppt to sub-ppb, so probably "ng/L".

**15:80 — MAJOR — true isobar cannot be resolved by mass resolution.**
> `Isobaric | ¹⁴²Ce on ¹⁴²Nd | High-resolution or MC-ICP-MS`

¹⁴²Ce and ¹⁴²Nd differ by 0.0015 u, needing R ≈ 10⁵; commercial sector-field ICP-MS tops out near 10⁴ and MC-ICP-MS is lower. The mitigation is to use a different Nd isotope (¹⁴³, ¹⁴⁵, ¹⁴⁶) or a mathematical correction from ¹⁴⁰Ce. Fix the row.

**15:101 — MAJOR — nonsense detection limit.**
> `Detection limits: ~5-10% for laboratory instruments (lower for trace analysis)`

The table two lines up (15:92) says "ppm level" and the comparison table (15:477) says ppm. 5–10 wt% is not a detection limit for anything. Delete or replace with a ppm figure.

**15:193–199 — MAJOR — mislabelled quantity.**
> `Example pKa Values (REE-MGDA Complexes): La 3.81, Nd 3.25, Eu 2.96`

Complexes do not have "pKa values" in this sense; these are presumably pKa of a coordinated water or a log K of something. MGDA is never expanded (methylglycinediacetic acid). Source is a master's thesis URL (15:183). Label the quantity correctly or cut.

**15:239 — MAJOR — self-contradiction.**
> `frequencies decrease regularly with decreasing atomic number and increasing Lewis acidity of the metal (Gd → Tm)`

Gd → Tm is increasing atomic number, and Lewis acidity increases with decreasing radius, i.e. with increasing Z. Also, Raman of organometallic dinitrogen complexes (@fieser2016raman) has nothing to do with separations; the citation was chosen for the word "Raman". Replace with a vibrational-spectroscopy example of extractant coordination (P=O shift on complexation).

**15:460–467 — MAJOR — uncited, non-monotonic separation factors.**
> `Ce/La 12 | Nd/La 87 | Pr/La 127 | Sm/La 3191`

Pr sits between Ce and Nd, so β(Pr/La) > β(Nd/La) is impossible for any single extractant with a monotonic series trend. The "optimized system" is never named and no paper is cited. Remove or source.

**15:112–114, 15:121 — MINOR — NAA detection limits too pessimistic and too precise.** INAA reaches sub-ppm for La, Sm, Eu, Lu in rocks (Stosch); "10¹–10² ppm" for light REE is wrong by 10–100×. "10⁻⁷ to 10⁻¹⁵ g/g" implies fg/g, which no routine INAA reaches.

**15:13–16 — MINOR — intro promises "doubly-charged ions" interfering on REE masses**, but the body has no doubly-charged entry, and in practice REE²⁺ interfere on As/Se, not REE-on-REE. Either drop the phrase or add the actual mechanism.

**15:177 — MINOR — `stability follows PC > AN > MeOH > DMF > DMSO`** — abbreviations undefined, claim uncited.

**15:191 — MINOR — `adding 1 M potassium oxalate (5 mL)`** is a thesis recipe; volume without sample size is meaningless.

**15:203, 15:209–211 — MINOR — UV-Vis section cites a solid-state LnPO₄ spectral library (@sharma2020library) but the substantive claim, online multi-track Nd monitoring for material accountancy, is uncited** (this is PNNL/INL work; it should be cited).

**15:225 — MINOR — `fluorite containing 226-867 ppm total REEs ... Ar-ion laser`** uncited and off-topic.

**15:269 — MINOR — XANES `Bond angles`** overclaims; say "sensitive to coordination geometry".

**15:294 — MINOR — `L-edge XANES primarily used for lanthanides (K-edge at very high energies)`.** Ln K-edges (39–63 keV) are routinely used for EXAFS precisely because the L-edges are close together and truncate the EXAFS range; L₃ is preferred for XANES. Half-true as written.

**15:29, 15:55, 15:86, 15:106, 15:183, 15:324, 15:354, 15:412, 15:435 — MINOR — vendor application notes and web pages as the sole source** for instrument sections. Acceptable for detection limits, but mark them as vendor sources rather than presenting them like literature.

**15:434–469 — MINOR — duplicates ch. 3's definitions of D and β**; the "effective/equivalent separation factor" bullets (15:457–458) are introduced and never explained.

**Missing (MAJOR):** no treatment of **how to measure D**. Aqueous-phase-only measurement by difference vs direct organic-phase analysis (digestion or back-extraction), matrix-matching, the error amplification when D ≫ 1 or ≪ 1, phase-ratio bookkeeping, and equilibration-time checks. This is the single most-used procedure in the group and the thing ch. 19:89–93 complains the literature does badly.

**Missing (MAJOR, table needed):** a table of REE isotopes and their principal oxide/hydroxide interferents (¹³⁵Ba¹⁶O→¹⁵¹Eu, ¹⁴¹Pr¹⁶O→¹⁵⁷Gd, ¹⁴³Nd¹⁶O→¹⁵⁹Tb, ¹⁴⁷Sm¹⁶O→¹⁶³Dy, ¹⁴⁹Sm¹⁶O→¹⁶⁵Ho, ¹⁵⁰Nd¹⁶O→¹⁶⁶Er, ¹⁵³Eu¹⁶O→¹⁶⁹Tm, ¹⁵⁹Tb¹⁶O→¹⁷⁵Lu). The chapter's one-line "BaO⁺ on Eu" does not let a student choose isotopes.

---

## src/16-recycling-urban-mining.md

Verdict: **a stub**. 334 words, one news-page link, zero MyST citations, and the three paragraphs of body text are inconsistent with the (good) two-paragraph introduction. Recommendation: **expand**, not merge. The preface (00-preface.md:55–57) names recycling as a Part V topic; ch. 17:324–332 quotes 64–96% GWP reductions for recycling; ch. 19:138, 19:143 list recycling as medium- and long-term priorities; and magnet recycling is the feedstock for three of the Part III technologies (16:20–24). The book therefore needs a chapter that says what the recycling flowsheets are. Target ~1,500–2,000 words: feedstock inventory with REE contents (NdFeB ~30 wt% REE; phosphors; NiMH; FCC catalysts), the standard magnet routes (hydrogen decrepitation / direct re-sintering; oxidative roast + acid leach + oxalate precipitation; selective leaching; molten-salt and electrochemical), reported recoveries with citations, why global rates are <1% (collection, dispersion, economics; UNEP 2011; Binnemans et al. 2013), and pointers into ch. 7/10/12. Keep 16:8–24 verbatim; it is the right framing.

**16:17–18 vs 16:27 — MAJOR — internal contradiction.**
> `recycling rates for rare earths sit in the single digits` / `The global REE recycling rate remains below 1%`

Both uncited. The <1% figure (UNEP 2011; Binnemans 2013) is the standard one.

**16:44 — MAJOR — meaningless uncited statistic.**
> `Recycling innovations have increased recovery rates from e-waste by up to 50% since 2015`

50% of what, measured how? Cut or replace with a sourced number.

**16:48 — MAJOR — overclaim.**
> `Certain coal and coal ash samples contain REE concentrations rivaling traditional ores`

Ch. 12:224 and ch. 9:361 put coal ash at 270–1,480 ppm; bastnäsite ores run 1–10% REO, i.e. 10–100× higher. Coal ash is interesting for tonnage and existing handling, not grade. Say that instead, and cite ch. 12. "Nature-based solutions" (16:50) is a buzzword with no meaning here.

**16:56–61 — MAJOR — uncited process.** The copper-salt acid-free dissolution is Prodius et al. (Ames / Critical Materials Institute, ACS Sustain. Chem. Eng. 2020). It is not cited anywhere in the book. This reads as a claim that once had a link.

**16:53–54 — MINOR — ETH news page as the sole source** for a start-up's claims.

---

## src/17-environment-tea-lca.md

Verdict: the introduction (17:8–23) is excellent and makes exactly the right argument. The body is a stack of tables of which roughly half are unsourced, several are qualitative rankings that no LCA supports, and the cost figures span three orders of magnitude without a stated basis. There is no worked example, which for a TEA chapter is the gap that matters.

**17:36 — MAJOR — market share numbers contradict ch. 1 and ch. 18; uncited.**
> `China, where >70% is mined and >95% is refined`

Ch. 1:58 says ~90% of separation/processing; ch. 18:12 says roughly 90%. USGS MCS 2025: ~69% of mine production, ~90% of separation. Use one set of numbers, cite USGS, and date them.

**17:53 — MAJOR — uncited and odd.**
> `Recovery efficiencies of 80-95% for Y, Ce, Nd, and Th`

Bioleaching "recovering" thorium is not a selling point, and no source is given.

**17:58, 17:130–137, 17:193 — MAJOR — vendor claims stated as findings.**
> `Separates all individual REEs at >99% recovery and >99% purity`

The only source for MRT anywhere in the book is IBC's marketing page (also ch. 9:370). Yet 17:193 assigns it TRL 7-8 "Demonstration" with "Low" OPEX. Either find independent evidence or label every MRT statement as a vendor claim.

**17:67–88 — MAJOR — CAPEX/OPEX share tables are unsourced.** The citation at 17:67 (@obrien2024simplified) was attached to the intro sentence in the source review; the two tables were never sourced. The percentages are textbook chemical-plant rules of thumb, not REE data. Cite Peters & Timmerhaus (or equivalent) or say "generic process-plant shares".

**17:106–112 — MAJOR — cost basis undefined; inconsistent by 10–50×.**
> `Acid roast + SX | $1,430 /ton REO` vs 17:100 `OPEX US$12/kg REO` vs 17:162 `Break-even ~$70/kg blended REO`

$1,430/t is $1.43/kg. MP Materials' reported ~$1,400–1,700/t cost is for **REO in concentrate**, not separated oxide, which would reconcile it with the other two figures. State the basis. "Higher" and "Variable" in the same table are not values.

**17:241–247 — MAJOR — pseudo-citations inside a table; one has no bib entry.**
> `Springer 2017` / `MDPI 2022` / `Multiple studies` / `Minimum observed`

"Springer 2017" is @browning2017life (cited two lines later). "MDPI 2022" for ionic-clay GWP 17.8–24.3 has no corresponding bib entry and was never resolved; this is the one row in the slice I can identify as a probable casualty of the verification pass. Cite it or remove the row.

**17:251–257 — MINOR — interpolated-looking ranges.** Eu 21.3 and Y 197.9 are exact; Sm "35–45", Nd "50–70", Pr "50–70" are round. Quote Browning's actual values or mark the middle rows as approximate.

**17:259–264 — MAJOR — hotspot shares uncited and do not sum.** 40–60 + 20–35 + 5–10 + 10–15 = 75–120%.

**17:188–195 — MAJOR — unsourced comparison table that contradicts ch. 4's.** Ch. 4:171–182 gives SX purity 95–99.9% and membrane TRL 5–7; this table gives >99.5% and 4–6, adds MRT/SFE/bioseparation rows that ch. 4 lacks, and lacks the MOF/lanmodulin/FJH rows ch. 4 has. Two TRL tables that disagree is worse than one. Merge into ch. 4 and cross-reference.

**17:316–322 — MAJOR — invented LCA rankings.**
> `Supercritical CO₂ | Medium | Low | Low | Low` etc.

No cradle-to-gate LCA of MRT, membrane, or bioseparation for REE exists at boundaries comparable to SX. This table has no source and cannot have one. Delete, or replace with the honest statement that only SX and (partially) sc-CO₂ have been assessed.

**17:158–166, 17:346–354 — MINOR — energy and CO₂ intensities from a commercial blog, then repeated uncited.** The "100+ MWh/ton" total at 17:354 is the Thunder Said figure from 17:165 re-presented as a table with per-stage splits that appear nowhere else.

**17:269–274 — MINOR — verify against @zaimes2015environmental.** Sm and Gd having the identical value 3,803 is suspicious; 11,170 kg water/kg REO deserves a sentence on what is counted.

**17:278–284, 17:365–369, 17:210, 17:114–118 — MINOR — uncited numbers** (water-by-stage shares; "GWP varies by 5×, water by 8×"; ">10× price swings", which is true for Dy/Nd in 2010–11 but needs a source; "1% recovery → ~2% NPV").

**17:93–104 — MINOR — Aclara figures from an investor-news site.** Fine as a data point but perishable; date-stamp it and cite the company's own technical report.

**17:357 — MINOR — ResearchGate URL for a paper already in the bib** (@navarro2014life). Replace.

**Missing (MAJOR, worked example needed):** a ten-line TEA: throughput × price − OPEX, CAPEX annualized at a stated discount rate, payback, and a one-parameter sensitivity (price or recovery). Without it the tables are not usable by a student; with it, the "1% recovery → 2% NPV" claim becomes something they can check.

---

## src/18-industrial-landscape.md

Verdict: **a stub that is also stale**. 208 words, four company bullets, zero citations (no `@` key in the file), 2022 production data, and "operations expected to begin in late 2025" written for a book being reviewed in September 2026. It does not name a single Chinese producer despite its premise being Chinese concentration.

Recommendation: **expand as a dated snapshot, or cut.** Expand if someone in the group will own an annual update: ~1,000–1,500 words with a "Data as of <month year>" line and one table (operator, site, feed, product, nameplate capacity, status, source) covering China Northern Rare Earth and China Rare Earth Group; Lynas (Kuantan, Kalgoorlie, Texas; first ex-China separated Dy/Tb in 2025); MP Materials (Mountain Pass SX restart, and the July 2025 US DoD equity-and-price-floor agreement, which is the most important industrial event since the export controls ch. 19:27 already cites); Solvay La Rochelle; Neo/Silmet; Energy Fuels White Mesa; Iluka Eneabba; SRC; RER; plus a paragraph on NdPr/Dy/Tb pricing and why nameplate ≠ output. Cite USGS Mineral Commodity Summaries and company filings. If nobody will maintain it, cut the chapter: the one durable fact (18:12–14) is already in ch. 1:58 and ch. 19:27–33.

**18:12 — MINOR — `roughly 90%`** vs ch. 17:36 ">95%". Pick one.

**18:17–21 — MAJOR — stale, company-website-sourced.** "Operations expected to begin in late 2025" is now a past tense. Date-stamp or update.

**18:24–27, 18:29–33 — MINOR — no source at all.** SRC's C$ figure and 400 t/y NdPr target, and Lynas's "partnership with DoD" (the Texas plant) need citations and specifics.

**18:38–39 — MINOR — `42,499 metric tons ... 2022`** is correct but is REO **in concentrate**, and 2023/2024 figures exist. Say "REO in concentrate", cite the 10-K, update.

---

## src/19-research-directions.md

Verdict: clean and well argued. It follows from Parts I–III and cross-references correctly (every anchor resolves). Its synthesis of the "four scales" (19:167–172) is the best paragraph in Part V. Findings are minor, with one gap.

**19:18–20, 19:120–121 — MINOR — `the source reviews' estimates` / `The source reviews group the work as follows`** never says which reviews. Name them or cite them; otherwise the horizon lists are anonymous opinion.

**19:61–62 — MINOR — `A separation factor of 1000 is worth nothing if equilibrium takes six hours`** overstates; slow kinetics is handled by residence time in columns and costs capital, not viability. Say "costs capital" (which is the sentence's own point).

**19:72–75 — MINOR — `subsidized capital and permissive disposal`** is uncited; defensible but should point at a source (e.g. the MRS Bulletin review already in the bib as @zapp2022environmental, or Packey & Kingsnorth).

**19:131–132 — MINOR — `Improved extractants with higher intrinsic separation factors` as a 1–3-year item.** That has been the field's aim for sixty years; if it belongs in "short term" it needs a reason (e.g. ML-guided screening from ch. 14).

**19:154–163 — MINOR — fragile anchors.** `#outlook`, `#research-gaps`, `#limitations-and-outlook`, `#challenges-and-future-directions`, `#industrial-challenges` are generic names that will collide the first time another chapter adds an "Outlook" section. Rename with a chapter prefix.

**Missing (MAJOR):** ch. 19 has no Part IV row beyond "transferable K_ex models" (19:162). The concrete open problem Part IV establishes, that selectivity needs ~1 kJ/mol while the best surrogates deliver 25, is the most quantifiable research target in the book and should be stated here.

---

## src/90-glossary.md

Verdict: 51 entries confirmed; the definitions are mostly good and written in the right register. Four entries need correcting and the coverage has holes that the book's own index exposes.

**90:48–52 — MAJOR — wrong for the industrial extractants.**
> `nearly every selective REE extractant is a chelator`

D2EHPA, PC88A and Cyanex 272 extract as hydrogen-bonded dimers bridging through phosphoryl oxygens, TBP is monodentate, and the classic chelators (β-diketones) are not industrial REE extractants. Say "many" and name the diglycolamides and aminopolycarboxylates as the true chelators.

**90:155–159 — MINOR — `the only property that reliably distinguishes adjacent rare earths`.** Redox (Ce⁴⁺, Eu²⁺, Sm/Yb²⁺) is exploited industrially and the book covers it (ch. 10). Say "the only property that varies smoothly across the whole series".

**90:143–147 — MINOR — glossary asserts a research result as fact.** `has resolved all fourteen lanthanides into elementally pure bands`; ch. 9:178 says "up to 14" per @pesavento2021versatile. Soften and don't put claims in definitions.

**90:77–81 — MINOR — DES `formed by mixing two solids`.** Many hydrogen-bond donors (ethylene glycol, glycerol) are liquids.

**90:109–112 vs 90:165–167 — MINOR — Gd is in both LREE and HREE definitions.** State the convention once.

**90:88–90 — MINOR — distribution ratio.** Ch. 14 and 15 say "distribution coefficient"; add the D vs K_D distinction (total analytical concentrations vs one species) so the two words are not read as synonyms.

**90:230–233 — MINOR — Sc is included in the definition and never explained.**

**Missing terms (MAJOR as a set).** Index-tagged in the book but absent: **bioleaching** (4 uses; the glossary's own "biosorption" entry defines itself by contrast with it), **precipitation / oxalate precipitation** (10 index hits, the third most-used term in the book), **polymer inclusion membrane** (3), **red mud** (2), **molten-salt electrolysis** (2), **microfluidics** (4; "numbering-up" is defined but not the thing being numbered up). Used repeatedly and undefined anywhere: **diluent**, **modifier**, **third phase** (the "extractant" entry mentions all three), **phase ratio (A/O)**, **loading / loading capacity**, **extraction isotherm / McCabe–Thiele**, **extraction constant K_ex** (vs D), **pH₁/₂**, **ionic strength**, **salting-out agent**, **TALSPEAK**, **thermodynamic cycle**, **implicit solvation**, **polyatomic (oxide) interference**, **functional unit / cradle-to-gate / allocation**, **TRL**, **CAPEX/OPEX/NPV/IRR**.

---

## src/93-appendix-provenance.md

Verdict: earns its place for a group-maintained book, but it is a maintainer's document and should be the last appendix. It is accurate as far as I could check (thirteen sources listed, line ranges match the converted files).

**93:8–12 — MAJOR gap — the appendix promises traceability but omits the step that most affects trust.** It records the pandoc conversion and the chapter map, but not the citation-verification pass (500 entries checked against CrossRef, 171 keys rekeyed, hyperlink citations converted, and the removals). A reader who hits an uncited number in ch. 17 cannot tell from this appendix whether it was ever sourced. Add a short section: what was verified, how, what was dropped, and a pointer to `verification-report.md` / `bib-rekey.md`.

**93:23–26 — MINOR — acknowledged fragility of line ranges.** Consider recording the converter's git commit hash instead, so the ranges are reproducible.

---

## src/94-appendix-further-reading.md

Verdict: this is not a further-reading list; it is a note about six PDFs that were not synthesized, and its premise is false for two of them.

**94:8–9 — MAJOR — premise contradicts ch. 14.**
> `Six papers were collected ... but never written up in prose, so no chapter was built from them.`

Augustine 2024 has ~800 words at 14:28–119 and An 2024 ~350 words at 14:121–167. The hedge at 94:14–16 ("cited elsewhere ... from summaries written at the time") does not rescue "no chapter was built from them".

**94:36 — MINOR — `Gupta et al. (2026)`** vs `references.bib` year 2025 (see 14:279).

**94:68–74 — MINOR — internal notes** ("a presentation deck and a docx duplicate"; "the Crucible knowledge base has not been surveyed") belong in Appendix A.

**Structure — MAJOR.** Rename this content "Sources collected but not synthesized" and fold it into Appendix A. Then write an actual Further Reading appendix for the stated audience: the textbooks and reviews a new student should read first. Candidates already in the bib: @gupta2004extractive (Extractive Metallurgy of Rare Earths), @xie2014critical (Minerals Engineering review), @rydberg2004solvent (Solvent Extraction Principles and Practice), @ansari2011chemistry (Chem. Rev. on DGAs). Candidates not yet in the bib: Cheisson & Schelter, Science 2019; Binnemans et al., J. Cleaner Prod. 2013 (recycling); Nash & Jensen, Sep. Sci. Technol. 2001; Cotton, Lanthanide and Actinide Chemistry.

---

## Structure across the slice

- **Duplication:** ML/BO/closed-loop three times in ch. 14; implicit solvation in ch. 13 and 14; D/β definitions in ch. 3 and 15; TRL comparison tables in ch. 4 and 17 that disagree; MRT in ch. 9, 17 (twice); the active-learning gap in ch. 14 and 19; the China-share figure in ch. 1, 17, 18 with three different values.
- **Ch. 19 follows from the book** for Parts I–III and V; it under-represents Part IV.
- **Appendices:** A earns its place with the verification section added; B does not in its current form.
- **Figures:** the book has none. In this slice, three are genuinely necessary rather than decorative: the corrected thermodynamic cycle (ch. 13), a log D vs pH plot with slope +3 that settles the sign once and for all (ch. 3/13), and the ICP-MS interference map (ch. 15, as a table). A magnet-recycling flowsheet (ch. 16) and a closed-loop schematic (ch. 14) would help but are not blocking.

---

## GAPS WORTH FILING AS ISSUES

1. **Balance the extraction thermodynamic cycle in ch. 13 and fix the hydration energies.** Rewrite ΔG₂ as a balanced reaction (with 3 H⁺(g) or with an explicit gas-phase acidity term), redraw the cycle, replace the ~1,300 kJ/mol dehydration values with Marcus values (~3,100–3,500), re-run the worked table, and rewrite the "reality check" so it identifies the ~4,000 kJ/mol missing term rather than solvation noise. State which reaction the ch. 14 ML binding energy corresponds to.

2. **One sign convention for the pH slope, book-wide.** Ch. 3 (lines 17, 261, 264–266, 420–422, 820) says −3; ch. 13:450/483 and the glossary say +3; ch. 13:688 says −3 again. Fix all occurrences to `log D = log K_ex + 3 log[(HL)₂] + 3 pH`, and add the log D vs pH figure.

3. **State the selectivity accuracy target and carry it through ch. 13, 14 and 19.** Add `ΔΔG = RT ln β` with the numbers (β = 1.5–3 → 1–2.7 kJ/mol at 298 K) next to the surrogate/DFT error figures, as a worked Nd/Pr example, and list the gap as a research direction.

4. **Expand ch. 16 (Recycling) into a real chapter.** Keep the introduction; add feedstock inventory, the standard NdFeB/phosphor/battery routes with recoveries and citations (Binnemans 2013; Prodius 2020 for the copper-salt route now sitting uncited at 16:56), the <1% figure with its source, and cross-links to ch. 7/10/12. Remove the "rivaling ores" and "50% since 2015" claims.

5. **Decide the fate of ch. 18 (Industrial Landscape): expand as a dated snapshot with an owner, or cut.** If expanded: one table of ex-China separation capacity with sources, Chinese producers named, the 2025 DoD–MP agreement and Lynas Dy/Tb, a pricing paragraph, USGS MCS citation, and a "data as of" line. If cut: move the 90% fact into ch. 1 and delete.

6. **Source or delete the unsourced tables in ch. 17.** Specifically: CAPEX/OPEX shares (17:71–88), Mountain Pass OPEX basis (17:106–112), GWP hotspot shares (17:259–264), water-by-stage (17:278–284), energy intensity (17:346–354), the qualitative LCA-by-method table (17:316–322), and the process-comparison/TRL table (17:188–195, merge into ch. 4). Resolve the in-table "MDPI 2022" reference. Add a ten-line worked TEA example.

7. **Add a "How to measure D" section and an interference table to ch. 15; fix the three analytical errors** (ng/g ≠ ppt at 15:61; isobar mitigation at 15:80; XRF "5–10%" at 15:101) and the mislabelled "pKa" table at 15:193–199.

8. **Glossary and appendices pass.** Add the missing terms (bioleaching, precipitation, diluent, modifier, third phase, phase ratio, loading, McCabe–Thiele, K_ex, ionic strength, TRL, functional unit, polyatomic interference, PIM, red mud, molten-salt electrolysis); fix the chelator entry; fold Appendix B into Appendix A and write a genuine further-reading list; add the citation-verification record to Appendix A.