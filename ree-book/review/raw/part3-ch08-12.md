# Review — Part III, "Separation Technologies" (ch. 8–12)

Read in full: `src/08-coacervates.md`, `src/09-microfluidic-separations.md`, `src/10-selective-crystallization.md`, `src/11-biological-biomimetic.md`, `src/12-membranes-mofs-emerging.md`. Cross-checked against `src/04-technology-landscape.md`, `src/90-glossary.md`, `src/93-appendix-provenance.md`, and every citation key in the five chapters against `src/references-cited.bib`.

No chapter in this slice is clean. Chapter 10's second half and chapter 9's numbers tables are the worst-affected. The most consequential single problem is a conceptual one that runs through ch. 8, 11, and 12 and reaches the glossary: **lanmodulin's 10⁸-fold Ln/Ca discrimination is repeatedly presented as if it were intra-lanthanide selectivity, and the Hans-LanM dimer's ">100-fold tighter" affinity ratio is repeatedly quoted as a "separation factor >100 for adjacent lanthanides."** Neither is true, and a new graduate student will take away a badly wrong idea of what biology has actually solved.

---

## Cross-cutting findings (affect several files)

### C1. Lanmodulin: Ln/Ca selectivity presented as Ln/Ln selectivity — BLOCKER

`src/11-biological-biomimetic.md:8-14`:
> "binds them with roughly a hundred-million-fold preference over calcium — a discrimination no synthetic extractant approaches. That single result reframes the separation problem: the reason conventional processes need hundreds of stages is not that the underlying differences are too small to exploit, but that the ligands in use are the wrong shape to exploit them."

This is a non-sequitur, and it is the thesis paragraph of the chapter. Discriminating Ln³⁺ from Ca²⁺ is a charge-and-radius problem that DTPA and oxalate also solve; it says nothing about discriminating Nd from Pr, which is what "hundreds of stages" is about. The chapter's own data contradicts the inference: `11:40` gives LanM's Kd as "0.4-10 pM across lanthanide series" — a spread of only ~25× across all fifteen elements, i.e. *worse* intra-series discrimination than a good extractant compounds over a cascade.

**Fix:** rewrite the opening to say what is actually remarkable — LanM's affinity, its acid tolerance (pH ~2.5), and the *dimerization* mechanism, which is the only part that gives genuine intra-Ln discrimination. Add one sentence stating explicitly that Ln/Ca selectivity and Ln/Ln selectivity are different quantities and that LanM's monomer affinity varies only ~25-fold across the series.

### C2. ">100-fold tighter dimer" quoted as "separation factor >100 for adjacent lanthanides" — BLOCKER

Correctly stated at `src/11-biological-biomimetic.md:62` and `src/08-coacervates.md:149` ("La(III)-induced dimer: >100-fold tighter than Dy(III)-induced dimer" — this is a dimerization affinity ratio for La vs Dy, which are not adjacent). It is then miscast as a separation factor in at least four places:

- `src/08-coacervates.md:24-27`: "reach separation factors above 100 for *adjacent* lanthanides [@cotruvo2023enhanced] — a figure that should be read against the single-digit factors typical of conventional extractants."
- `src/08-coacervates.md:95`: "conventional solvent extraction achieves SF = 1.5-3.0, while protein-based systems can achieve SF > 100 [@cotruvo2023enhanced]"
- `src/08-coacervates.md:452`: "achieve separation factors >100 for adjacent lanthanides, approaching the theoretical limits of protein-based recognition"
- `src/04-technology-landscape.md:177` gives Lanmodulin "Separation Factor: High" — vague, but fed by the same claim.

Two errors compounded: an affinity ratio is not a separation factor, and La/Dy is the widest pair in the light/heavy split, not an adjacent pair. "Approaching the theoretical limits of protein-based recognition" (`08:452`) is unsupportable — no such limit is defined anywhere in the book.

**Fix:** replace every instance with the measured quantity and its pair, e.g. "the La³⁺-induced Hans-LanM dimer is >100× more stable than the Dy³⁺-induced dimer, which the authors convert into a single-column Nd/Dy separation at >98% purity." Delete "adjacent" and "approaching theoretical limits."

### C3. Two lanmodulin papers swapped — MAJOR

`src/08-coacervates.md:151` and `src/11-biological-biomimetic.md:291` both attribute **Nd/Dy** separation to `@park2024modulating`. That paper's own title in `references-cited.bib` is *"Modulating metal-centered dimerization of a lanthanide chaperone protein for separation of **light lanthanides**"*. Meanwhile `src/09-microfluidic-separations.md:155` attributes the Nd/Dy single-stage result to `@cotruvo2023enhanced`, which is right. The two results have been crossed.

**Fix:** attribute Nd/Dy to `@cotruvo2023enhanced` and the light-lanthanide (La/Nd, Nd/Pr) result to `@park2024modulating`, and say which pair each achieved.

### C4. `{index}` role inserted mid-word — MAJOR (mechanical, systematic)

- `src/09-microfluidic-separations.md:136`: "employs cat{index}\`ion exchange\` extraction"
- `src/12-membranes-mofs-emerging.md:54`: "using adjacent an{index}\`ion exchange\` membranes"
- (also `src/13-extraction-thermodynamics.md:674`, outside this slice)

An automated indexer split "cation exchange" and "anion exchange". The index entry is wrong and the rendered text may break.

**Fix:** `cation exchange` / `anion exchange` with the index role attached to the whole term or removed.

### C5. HDEHP / D2EHPA / PC88A / HEHEHP / P507 / EHEHPA used as if six reagents — MAJOR (clarity)

Within this slice: `08:251` "HDEHP, PC88A, Cyanex 272"; `09:142,147,149,153` D2EHPA and HDEHP in the same chapter; `09:144` "HEHEHP/P507"; `09:359` "EHEHPA"; `11:69` "HDEHP". HDEHP and D2EHPA are the same compound; PC88A, HEHEHP, P507 and EHEHPA are the same compound. `src/04-technology-landscape.md:39-40` gives two of the aliases but not the identity, and there is no glossary entry for any of them. A new group member reading ch. 9 will believe the chapter compares four extractants when it compares two.

Compounding this, `src/08-coacervates.md:251` is wrong chemistry: "Phosphonate ligands are the basis of industrial REE extractants (HDEHP, PC88A, Cyanex 272)." HDEHP is a phosph**oric** acid diester, PC88A a phosph**onic** acid monoester, Cyanex 272 a phosph**inic** acid. Only PC88A is a phosphonate. The distinction is the whole basis of the acidic-extractant selectivity trend.

**Fix:** add a glossary entry mapping the aliases, and correct `08:251` to "organophosphorus acid extractants (phosphoric HDEHP/D2EHPA, phosphonic PC88A, phosphinic Cyanex 272)."

### C6. Ch. 4's comparison table does not do what ch. 4 promises — MAJOR

`src/04-technology-landscape.md:10`: "places **every** approach in this book on a single comparison." The table at `04:171-180` has eight rows and omits precipitation, selective crystallization, coacervates/ABS, microfluidics, biosorption, phytomining, electrodialysis, and supercritical CO₂ — i.e. most of Part III. Chapters 8, 9, 10 have no line in the frame the reader was told to read them against.

**Fix:** either extend the table to cover Part III (preferred; see issue G1) or soften the promise to "the technologies that have an established comparison basis."

---

## `src/08-coacervates.md`

**08:263 — BLOCKER (rendering).** Markdown corruption from the pandoc conversion:
> "Cerium is unique among lanthanides in exhibiting stable ~~4 oxidation state, enabling oxidative separation. Ce4~~ can be selectively precipitated as CeO2"

The `+` superscripts were eaten and the surviving `~~` pairs render as strikethrough. It should read "a stable +4 oxidation state … Ce⁴⁺ can be selectively precipitated." Grep the whole book for `~~` before shipping.

**08:59 — MAJOR (physics).**
> "bounded by a single-phase region at very low salt (kinetically trapped precipitates) and at high salt (electrostatic screening suppresses coacervation)"

Mis-assigns the phase count. At low salt the system is *two*-phase — a solid-like precipitate plus solution; the single homogeneous phase occurs only at high salt. As written a student learns the phase diagram backwards. Fix: "bounded by a solid precipitate regime at very low salt and a homogeneous single-phase regime at high salt."

**08:273 — MAJOR (citation does not support the sentence).** Under the heading `#### Nd/Pr Separation`:
> "PC88A-impregnated surfaces achieve SF = 171 with 92% Pr+Nd purity [@gao2023separation]"

The bib title is *"Separation of Praseodymium and Neodymium **from Heavy Rare Earth Elements** Using Extractant-Impregnated Surfaces."* That is a (Pr+Nd) vs HREE **group** separation — confirmed by the book's own "Pr+Nd purity". SF = 171 for Nd/Pr would be a landmark; presenting it under a Nd/Pr heading is a serious misreading. Fix: move to a group-separation context and state the pair as (Pr,Nd)/HREE.

**08:272 — MAJOR (citation mismatch).**
> "Ionic liquid extraction with β-diketones achieves unprecedented separation factor >500 [@zhang2024remarkably]"

Bib title: *"Remarkably High Separation of Neodymium from Praseodymium by **Selective Dissolution from their Oxide Mixture**."* That is not liquid–liquid IL/β-diketone extraction. Either the description or the citation is wrong. Also drop "unprecedented."

**08:274 — MAJOR (implausible number, no conditions).** "Kinetic separation strategies with specific ion effects achieve SF > 8 [@sui2023kinetic]." A thermodynamic Nd/Pr SF of 8 is roughly 5× anything reported; this is almost certainly a kinetic selectivity or enhancement factor, not an equilibrium SF. State which, with the contact time it was measured at.

**08:136 — MAJOR.** Under `#### Lanthanide Binding Tags (LBTs)`: "Picomolar affinity for Ln3+ with 10^8-fold selectivity over Ca2+ [@cotruvo2023enhanced]". Those are full-protein LanM numbers. `src/11-biological-biomimetic.md:117` states the correct LBT figure — "LBT Kd range: 0.9-1.8 μM (immobilized) vs. 0.4-10 pM (full LanM protein)" — a six-order-of-magnitude contradiction between the two chapters.

**08:280 — MAJOR (chemistry).** "Integration with selective oxidation for Pr (Pr3+/Pr4+)". Pr(IV) is not accessible in aqueous solution (it exists only in solid oxides/fluorides and superacidic fluoride melts); E° is far beyond the water window. Proposing it as a coacervate process route is not chemically viable. Either delete or state explicitly that it is solid-state-only and why that matters.

**08:89 vs 08:91 — MAJOR (unstated coordination number).** "La3+ = 1.03 Å to Lu3+ = 0.86 Å" are Shannon radii for **CN = 6**, but the very next paragraph says lanthanide coordination preferences are "typically 8-9". The same CN-6 values reappear at `08:265` and `08:268`. Radii for CN = 8/9 are ~0.13 Å larger and the *differences* scale too. Fix: state "Shannon six-coordinate radii" once, and note that the values shift with coordination number.

**08:8-15 vs 08:212-215 — MAJOR (over-claim in the framing).** The opening asserts "A coacervate system does the job of a solvent extraction circuit without kerosene." The chapter's own body says the opposite: `08:212` "most work focusing on aqueous biphasic systems, cloud point extraction, and protein-based approaches **rather than classical polyelectrolyte coacervates**"; `08:215` "their application to REE separation is limited. The similar chemistry of lanthanides means that non-specific electrostatic binding provides **poor selectivity**." No coacervate REE separation with numbers appears anywhere in the chapter. Fix: the intro must say that polyelectrolyte coacervates have not yet been demonstrated on REE, and that the chapter's REE content is ABS and CPE.

**08:388 — MAJOR (limitation stated but not quantified).** "Lower metal loading capacity than organic extractants" is the single most important barrier for an aqueous two-phase process and gets one unquantified bullet. Organic extractant circuits run at 0.1–0.3 M metal in the organic; give the coacervate figure, or say it is unmeasured.

**08:261-303 — MAJOR (structure).** The four subsections `#### Light REE: La/Ce and Ce/Pr`, `#### Nd/Pr Separation`, `#### Heavy REE Separations`, `#### Sc Separation` (43 lines) describe IL/β-diketone extraction, extractant-impregnated surfaces, polymer-supported phosphonates, mesoporous silica and TRPO resins — none of which are coacervates, as `08:277` admits ("Coacervate-based approaches remain to be developed"). This is generic REE separation content that belongs in ch. 4 or 12.

**08:176 — MINOR.** "decontamination factors of 50" — DF is never defined and is not in the glossary; it is a different quantity from separation factor and from enrichment factor, both of which also appear in this slice.

**08:454 — MINOR (over-claim).** "Aqueous biphasic systems are most mature: IL-based ABS and polymer-salt systems have demonstrated practical REE separations with good efficiency." No TRL, scale, or number. The one ABS result actually cited (`@liu2022one`, `08:238`) is an Fe/REE separation, not an intra-REE separation.

**Undefined on first use, not in glossary:** LLPS (`08:36`), IDP (`08:100`), LCST/UCST and cloud point (`08:159-176`), kosmotropic (`08:225`), Hofmeister series (`08:167`), holdback reagent (`08:221`), didymium (`08:267`), EF-hand (`08:130` — used ~15 times across ch. 8 and 11 and never defined).

---

## `src/09-microfluidic-separations.md`

The framing (`09:8-45`) is the best writing in the slice — the kinetic-vs-thermodynamic argument, the honest "the science is demonstrated and the engineering economics are not," and the citation-reliability warning box. The numbers tables underneath it do not live up to it.

**09:79 — BLOCKER (dangling footnote).** "achieve enrichment factors of **200-450** at phase ratios exceeding 200:1---far beyond conventional capabilities [^1]". There is **no `[^1]` definition anywhere in the file** (verified by grep). This is a build-breaking dangling reference *and* it means the chapter's most extreme quantitative claim has no source at all — exactly the "claim that once had a source and now has none" signature. Either restore the source or delete the sentence.

**09:167 — MAJOR (arithmetic).**
> "| Mass transfer coefficient (kLa) | 0.19-0.41 s⁻¹ | 10⁻³-10⁻² s⁻¹ | **100-1000×** |"

0.19/10⁻² = 19 and 0.41/10⁻³ = 410. The enhancement from the table's own numbers is ~20–400×, not 100–1000×. The wrong figure is then repeated in the chapter's closing summary (`09:425`, "100-1000× mass transfer enhancement") and in the opening (`09:10`, "mass transfer coefficients rise by two or three [orders]"). Separately, a conventional mixer-settler kLa of 10⁻³–10⁻² s⁻¹ is at the low end for a stirred contactor and flatters the comparison; give the source and the agitation condition.

**09:169 vs 09:52 — MAJOR (physics inconsistency).** The table gives "Surface-to-volume ratio 49-61 cm²/cm³" while `09:52` says channels are "typically tens of µm cross-section." For a square channel S/V ≈ 4/d, so 50 µm gives ~800 cm⁻¹; 49–61 cm⁻¹ corresponds to d ≈ 700 µm — a *mini*-channel. And `09:76` claims co-laminar systems achieve "surface-to-volume ratios **double** those in bulk extraction," against the table's "~10×" and the intro's "order of magnitude." Three mutually inconsistent statements about the chapter's foundational quantity. Fix: pick one channel scale, compute S/V from it, and state which geometry each literature number came from.

**09:168 and 09:66 — MAJOR (inconsistent, arithmetic).** Table 2 gives "3-60 seconds vs 10-25 minutes → 10-100×" (the true range from those numbers is 10–500×); the earlier table at `09:66` gives "<10 seconds vs ~25 minutes" (150×). Reconcile.

**09:170 — MAJOR (unsupported, attributed to the wrong papers).** "| Separation factor | Up to 6× higher | Baseline | **2-6×** |", sourced from `[@dessimoz2010quantitative; @kashid2007hydrodynamics]` at `09:161`. Those are *"Quantitative criteria to define flow patterns in micro-capillaries"* and *"Hydrodynamics of liquid–liquid slug flow capillary microreactor"* — flow-pattern and pressure-drop papers with no REE separation factors in them. The chapter's headline selectivity claim, repeated at `09:425`, rests on citations that cannot support it.

**09:136 — MAJOR (citation mismatch).** "involves each REE ion extracted in a complex with six extractant molecules arranged as dimers [@jensen2002comparison]". That paper is *"Comparison of Covalency in the Complexes of Trivalent Actinide and Lanthanide Cations"* — about covalency, not extractant stoichiometry. Likely a citation swapped in during repair.

**09:178-182 — MAJOR (over-claim, propagated to the glossary).**
> "ITP can separate up to **14 lanthanides** from a homogeneous sample into elementally pure bands [@pesavento2021versatile]" … "Eight lanthanides concentrated within ~6 minutes"

14 in one bullet, 8 four lines later. The stronger version has migrated into `src/90-glossary.md:143-148` as settled fact: "On-chip, it has resolved all fourteen lanthanides into elementally pure bands." Fix both; state which is the demonstrated number, at what sample loading, and note that this is analytical scale (µL, ng) — the chapter never says so.

**09:203 — MAJOR (apples-to-oranges in the chapter's headline number).**
> "Industrial REE separation typically processes 50,000-100,000 tons of concentrates annually. The best microfluidic demonstration at 1 L/h equals approximately 8.76 m³/year---requiring 10,000-100,000× additional scale-up through massive parallelization"

8.76 m³/yr of *liquid* is compared to 50,000–100,000 t/yr of *solid concentrate*. The gap is real and probably much larger than stated once the concentrate is converted to leach liquor at plant tenor. Also: sentence has no terminal period; "tons" here vs "tonnes" at `09:30` and `09:372`. Fix: convert both sides to m³/yr of process liquor at a stated g/L, then quote the ratio.

**09:361 vs 12:224 — MAJOR (unreconciled cross-chapter disagreement).** Ch. 9: coal fly ash "containing 250-800 ppm total REE (Appalachian sources average 591 ppm)". Ch. 12: "Coal ash contains 270-1480 ppm REEs". Ch. 9's own preamble (`09:35-36`) promises "Where they disagree on a number, the disagreement is noted rather than averaged" — the promise is not kept across chapters.

**09:98, 09:103 — MAJOR (undefined metric, false precision).** "Higher mass transfer efficiency: 86.9-94.8%" and "Highest mass transfer efficiency: 92.9-97.4%". "Mass transfer efficiency" as a percentage is undefined — fraction of equilibrium approached? extraction yield? Three significant figures on an undefined quantity, uncited.

**09:82 — MINOR.** "separation factors of **1,289 for Zn/Mn** in 45 seconds … versus 233 in 25 minutes". The arithmetic checks (5.5×, 33×) but Zn/Mn is a transition-metal pair with a large intrinsic SF; presenting it as the lead evidence in an REE chapter, without saying it is not an REE separation, invites the reader to transfer the number.

**09:280-334 — MAJOR (structure, visible conversion seam).** The sections `## Detection: Colorimetry, Fluorescence, and Spectroscopy` and `## Computer Vision and Machine Learning` (55 lines, 12% of the chapter) cover Hg/Pb/Cd/Cr/Ni/Cu/Fe colorimetry, smartphone pH/nitrite determination, and droplet image segmentation. None of it involves rare earths. It exists only to provide "Precedent" bullets for `### Research Opportunities` at `09:432`. Fix: compress to a short paragraph inside the Research Opportunities section.

**09:51, 84, 114, 175, 205, 229 — MINOR (heading hierarchy).** Six `####` headings sit directly under `##` headings with no `###` between them (verified against the full heading list). Content under `#### Scale-Up: Numbering-Up Approach` (`09:205`) also duplicates `## Scale-Up by Numbering-Up` (`09:197`) almost point for point — the same 100-fold / 1 L/h / counter-current facts twice in nine lines. Same duplication between `09:117-124` and `09:155` (flow-focusing, SF 279, pH 1, 3-60 s).

**09:429 — MINOR.** "Phoenix Tailings, **RETi**, and IBC Advanced Technologies" — RETi appears nowhere else in the book and is absent from the `## Industrial Status and Key Players` list at `09:366-374`. Also "true microfluidic processing at scale remains 5-10 years away" is an unsourced forecast in a chapter that elsewhere carefully labels company claims as claims.

**09:225 — MINOR.** "Nd(III) equilibrium achieved within **1.5 seconds** in microreactor" — no citation.

**09:377 — MINOR.** "Prof. Yundong Wang's team focuses on continuous REE recovery from wastewater" — sentence ends without a period (conversion seam).

**Undefined, not in glossary:** Damköhler number (`09:157`) — load-bearing for the chapter's entire kinetic-control thesis; TALSPEAK (`09:265`); enrichment factor / concentration factor (`09:79`, `09:361`) as distinct from separation factor; co-laminar / slug / segmented flow; red mud (`09:363`); coal fly ash. Also `09:149`: "complete separation of **14 lanthanides**" — a reader who just read the glossary's "fifteen lanthanides" will want one clause explaining that Pm is excluded.

---

## `src/10-selective-crystallization.md`

This chapter has the most serious provenance problem in the slice.

**10:449-473 — BLOCKER (violates the book's own citation policy).** The chapter ends with a hand-written `## Sources` list of 12 numbered references with raw URLs. It is the **only** such list left in the book (verified by grep across `src/`), and `src/93-appendix-provenance.md` states these were deliberately removed: *"Hand-written reference lists … were dropped in favour of the single verified bibliography."* Worse, the entire second half of the chapter (`10:331-448`, 118 lines covering borate crystallization, M₄L₄ cages, H₂PDA, cyclic peptides, macrocyclic chelators, macropa/macrophosphi) contains **zero inline citations** — the chapter has six `[@...]` keys total, all in the first half. Every quantitative claim in the molecular-design half rests on this unverified list.

Concrete evidence the list is unreliable: **item 7** (`10:463`) attributes *"Rationally designed mineralization for selective recovery of the rare earth elements,"* Nat. Commun. 8, 15670 (2017), to **"Marsh, M. L. et al."** The verified bibliography has the same paper under `hatanaka2017rationally` with authors *Hatanaka, Matsugami et al.* — and the chapter body at `10:396-409` discusses exactly this Hatanaka Lamp work. Three entries (items 5, 6, 11) have no author at all. This list needs the same CrossRef verification the rest of the book got, and the surviving entries need to be converted to inline `[@key]` citations against `references-cited.bib`.

**10:175 — MAJOR (sign convention).**
> `Ce³⁺ → Ce⁴⁺ + e⁻     E° = 1.74 V`

Written as an oxidation half-reaction with a positive E°. By IUPAC convention E° is quoted for the reduction: Ce⁴⁺ + e⁻ → Ce³⁺, E° = +1.72 V. As printed, a student learns the convention wrong. The value is also strongly medium-dependent (+1.72 V in HClO₄, +1.61 V in HNO₃, +1.44 V in H₂SO₄) and must be quoted with its medium — particularly since the very next line, `10:176` (`Ce⁴⁺ + 4OH⁻ → Ce(OH)₄`), implies alkaline conditions while the performance table at `10:192` specifies pH 3-5.

**10:66 vs 10:287 — MAJOR (contradiction, wrong mechanism).**
> `10:66`: "Oxalate forms soluble REE complexes at low pH and precipitates as pH increases."
> `10:287`: "| Oxalate at pH 1.5 | High | Low (stays in solution) | Low |"

Industrial oxalate precipitation runs at pH 1–2, as the chapter's own table says. The pH dependence is oxalate *protonation* (H₂C₂O₄ pKa₁ 1.25, pKa₂ 4.27), not the formation of soluble REE-oxalate complexes.

**10:66-72 — MAJOR (stated mechanism contradicts the table).** The text says "The saturation index of REE-oxalate decreases at higher pH **due to competition with hydroxide precipitation**," but the table shows La-hydroxide SI = −3.81 at pH 7 and −1.99 at pH 8 — undersaturated at both, i.e. hydroxide is not precipitating and cannot be competing. Table is also uncited.

**10:102 vs 10:107 and 10:244 — MAJOR (unreconciled contradiction).** "Over **99% REE precipitation** achieved at pH 6.5" (`10:102`) against "Only **~70% REE recovery** at circumneutral pH using NaOH alone" (`10:107`) and "| OH⁻ | ~70% recovery at neutral pH |" (`10:244`). Same reagent, same pH, 30 points apart, five lines apart.

**10:341 and 10:361 — MAJOR (wrong chemistry).** "Soft/hard donor selectivity - **Soft donors (e.g., Cl⁻)** preferentially bind early lanthanides", repeated as "Soft ligand coordination selectivity". Cl⁻ is a borderline/hard donor in HSAB terms, not soft; soft donors are S, Se, and soft N. As stated the sentence teaches HSAB backwards. Fix to "harder vs. softer donor sets" with a correct example (S- or N-donor vs O-donor), or cite the borate paper's actual argument.

**10:26 — MINOR (number).** "Ionic radius varies by only about **0.15 Å** across the whole lanthanide series." From the book's own CN-6 values (`08:89`: La 1.03 → Lu 0.86) the span is 0.17 Å. Use one number consistently.

**10:237 — MINOR/MAJOR (garbled reagent name).** "CEPPA (3-hydroxyphenylphosphoryl propionic acid)". CEPPA is 2-carboxyethyl(phenyl)phosphinic acid. Also "90.5% RE³⁺ extraction, only 9.5% Al³⁺" summing to exactly 100 looks like a transcription artifact; uncited.

**10:300 — MINOR (unsupported, no conditions).** "Phosphine oxide modified adsorbents achieve separation factors **>15,000**" — no pair named (presumably Th/REE), no conditions, no citation. An SF of 15,000 needs all three.

**10:73 — MINOR (unclear, unsupported).** "efficient extraction even at low initial REE concentrations (<5%) from processed magnet wastes" — 5% of what basis? Uncited. This section also duplicates `src/12-membranes-mofs-emerging.md:120-126` almost verbatim.

**10:250-277 — MINOR (internal tension, undated chemistry).** "remains relevant for high-purity production" (`10:251`) is contradicted by "Largely superseded by solvent extraction for bulk separation" (`10:277`) and "Multiple (often hundreds of) crystallization stages required" (`10:275`). The table at `10:260-264` presents bromates and ethyl sulfates as "Optimal Double Salt" recommendations without noting these are pre-1950s practice.

**10:425 — MINOR (extraordinary claim, uncited).** "Binding affinity of macrophosphi for La³⁺ is over **5 orders of magnitude** higher than for Gd³⁺." Sits oddly beside the very modest "Separation factors of up to 45 achieved for the Ce/La pair" two lines later. Needs the conditions and the primary citation (Sources item 10).

**10:438 — MINOR (over-strong).** "the 4f orbitals are shielded, **preventing** bonding with ligand orbitals." 4f covalency is small but demonstrably non-zero — and the book cites a covalency paper elsewhere (`@jensen2002comparison`). Fix to "so bonding is overwhelmingly electrostatic, and selectivity tracks charge and radius rather than orbital overlap."

**10:56, 175-176 — MINOR (formatting seam).** Chemical equations are in four-space code blocks rather than math, so they render in monospace with the rest of the book's equations in MyST math.

**10:62 — MINOR (non-sequitur).** "Avoids co-precipitation of nickel (5× less water for washing vs. hydroxide route)" — two unrelated claims in one bullet; nickel is relevant only for NiMH feeds, unexplained at this point.

**10:198 — MINOR.** "bastnaesite" here; the book uses "bastnäsite" (glossary, ch. 12), "bastnasite" (ch. 5), and "bastnaesite" (ch. 6, 7, 10, 11). Pick one.

**Undefined, not in glossary:** saturation index (`10:66`), supersaturation (`10:344`), concomitant polymorphism (`10:346`), Stranski–Totomanow conjecture (`10:351`, also transliteration-inconsistent), macropa/macrophosphi (`10:423`), CSEREOX (`10:73`).

**GAP — europium.** The chapter's best idea is at `10:20-23`: cerium works "because oxidation state, unlike ionic radius, is a **threshold property**." Europium is the second genuine redox exception and is separated industrially by Eu(II) reduction and sulfate precipitation. Its complete absence from a chapter organised around threshold properties is a real hole. (Sm(II)/Yb(II) deserve a sentence too.)

---

## `src/11-biological-biomimetic.md`

See C1–C3 above, which are this chapter's central problems. Additionally:

**11:191-202 — MAJOR (citation contradicts the sentences it supports).** The passage states "Lanthanides can replace Ca²⁺ in EF-hand proteins **isomorphously** [@edington2018coordination]", then "**X-ray crystallography** shows lanthanides bind more strongly than calcium", "Same degree of conformational changes as with Ca²⁺", and "Though coordination distorts structure slightly, **perturbations are small**". The cited paper is titled *"Coordination to Lanthanide Ions **Distorts Binding Site Conformation** in Calmodulin"* (PNAS) — its conclusion is the opposite of "isomorphous" and "perturbations are small", and it is a 2D-IR spectroscopy study, not crystallography. Either the citation is a repair swap or the claims are inverted.

**11:33 — MAJOR (over-strong).** "*Methylobacterium extorquens*, a methylotrophic bacterium that **requires** lanthanides for methanol metabolism." AM1 carries both the Ca-dependent MxaFI and the Ln-dependent XoxF methanol dehydrogenases and grows without lanthanides; the lanthanide switch is regulatory, not obligate. (Genus is now *Methylorubrum* — worth a parenthetical.)

**11:37-43 — MAJOR (numbers without conditions, missing the key caveat).** The binding-property table gives "Selectivity Ln³⁺/Ca²⁺ 100,000,000-fold", "Kd 0.4-10 pM across lanthanide series", "pH stability … pH ≈ 2.5", "Temperature stability up to 95°C" with no buffer, ionic strength, method, or citation per row, and — critically — no statement that a 25× Kd spread across fifteen elements means **weak intra-lanthanide discrimination**. That omission is what makes C1 possible.

**11:66-70 — MAJOR (the chapter's anchor claim has no number).**
> "Achieves higher separation factors than standard lanmodulins / Comparable or better than common industrial extractants (e.g., HDEHP)"

Not one separation factor appears anywhere in this 610-line chapter. "Comparable or better than HDEHP" is precisely the kind of claim that needs the pair, the SF, the pH, and the scale.

**11:388-399 — MAJOR (internally inconsistent numbers).**
> "Up to **0.7 wt% REEs** in above-ground tissues / Total REE concentrations: **2-3 mg/g** in fronds" … "**92.3%** weight reduction after incineration … REEs enriched to **30,000 mg/kg** in ash … **~11-fold** concentration vs. original **woody biomass**"

0.7 wt% = 7,000 mg/kg but 2-3 mg/g = 2,000-3,000 mg/kg — a 2-3× internal disagreement. 92.3% weight loss is a 13× concentration factor, not 11×. And 30,000 mg/kg ÷ 13 = 2,300 mg/kg, consistent with the 2-3 mg/g figure but not with 0.7 wt%. Also *Dicranopteris* is a fern, not "woody biomass" — a conversion seam.

**11:402-416 — MAJOR (single 2025 paper, over-claimed).** The "biological monazite" section states as advantages: "**Pure and non-radioactive** (unlike natural monazite containing U/Th) / Strong potential for green extraction / **No mining-associated radioactive waste concerns**." A discovery of nanoscale dendritic crystals in fern tissue establishes none of this — purity depends on what the plant took up from the substrate, no extraction route was demonstrated, and no mass balance was reported. Fix: state what was observed (nanoscale monazite crystals in extracellular tissue, ambient formation) and label the rest explicitly as speculation.

**11:530-539 — MAJOR (unsupported).** The `### High-Purity REE Biomanufacturing` section carries **no citation at all** and reports "Eu recovery 99.9% / La recovery 97.1% / Dy recovery 92.7%" under a column headed "Element Pair" that contains single elements. "Outstanding separation achieved" is content-free. This reads exactly like a passage whose source was deleted in the verification pass.

**11:217-228 — MAJOR (suspicious precision pattern).** The rhamnolipid log β table gives exact values only for the endpoints (UO₂²⁺ 9.82, Lu³⁺ 8.20) and "~" values for every REE in between, which are non-monotonic (peak at Eu). This is the signature of interpolated rather than reported numbers. Also, a 1.3-log-unit spread across the series means *poor* intra-REE selectivity, which the section's "**Key Finding**" (`11:230`) elides by talking about recovery from soil cations instead.

**11:236 — MINOR (garbled).** "Reduces surface tension more effectively than chemical surfactants **at same CMC**" — CMC is a measured property of a surfactant, not a condition you can hold equal. Probably meant "at the same concentration" or "reaches a lower surface tension at its CMC."

**11:270 — MAJOR (broken bib entry, cited in text).** `[@others2019characterization]` — the bibliography entry's author field is literally **"Others"**. This will render as "Others (2019)". Same class of problem: `@anon2024efficienta` (`09:79`, `09:377`, author blank, key "anon"), `@yang2022pilot` ("Yang, Yiming and others"), `@tour2025sustainable` ("Tour, James M. and others"). These four are the highest-risk entries in the slice and each carries a load-bearing number.

**11:293 — MINOR.** "*Streptomyces* strains FXJ1.172 and FXJ1.532 produced 200 and 9.3 µmol/L siderophores" — no citation, and a 20× difference between two strains is presented without comment.

**11:307-311 — MINOR (table garbled).** In `### Mineral Source Selectivity` the "Mechanism" column contains "**Sc extraction**", which is a target, not a mechanism.

**11:430, 439-445, 451-453 — MAJOR (units error, false precision, off-topic).**
- `11:430`: "High adsorption capacity (**85-100%**)" — a percentage is a removal efficiency, not a capacity.
- `11:441`, `11:453`: "353.28 mg/g", "**661.21 mg/g**" Nd, "436.55 mg/g" Ce — five significant figures on Langmuir fits, with no equilibrium concentration, pH, or temperature. 661 mg/g Nd = 4.6 mmol/g, at the very top of anything credible for a GO-cellulose composite and presented without comment.
- `11:472`: "EDTA-Fe₃O₄-chitosan-CMC nanocomposite: 432.34 mg/g for **Pb²⁺**" — a lead capacity in an REE chapter; conversion seam.

**11:490, 496 — MINOR (no baseline).** "Up to **73% improvement** in REE extraction" and "18% increase in bioleaching rates" — improvement over what absolute extraction? Without the baseline these are uninterpretable.

**11:501 — MINOR.** "**Scalable** to 10 L with consistent metal yields." 10 L is a bench fermenter. Say "demonstrated at 10 L."

**11:598-608 — MAJOR (unsupported comparison table).** The nine-row Selectivity/Scalability/Cost/Environmental Impact/TRL table has no citations and no criteria. Every row scores "Very Low" or "Low" environmental impact — including phytomining (land use, multi-year cycles) and engineered microbes (media, sterilization, protein expression). "Chitosan Adsorbents | **Industrial** | TRL 6-7" is not supported by anything in the chapter. "Selectivity: Exceptional / High / Moderate" is undefined and, given C1, likely conflates Ln/Ca with Ln/Ln discrimination.

**Undefined, not in glossary:** EF-hand, lanthanide binding tag (LBT), bioleaching (used repeatedly and referenced *inside* the `biosorption` glossary entry, but has no headword of its own), siderophore, phytomining, hyperaccumulator, TRL (a column in three tables book-wide, expanded only in a footnote).

---

## `src/12-membranes-mofs-emerging.md`

The chapter opening (`12:8-21`) is honest and well-judged — "measured on synthetic feeds at milligram scale" is exactly the right caveat. The body does not maintain it.

**12:28-54 vs 12:128-342 — MAJOR (uneven depth; the title technology is a stub).** "Membranes" is the first word of the chapter title and gets 26 lines: a bulleted taxonomy with no citation, a three-bullet NF/UF section with no rejection figures, and four lines on electrodialysis. Supercritical CO₂ — not in the chapter title — gets 215 lines with a TEA, a scale-up section, and an advantages/limitations table. Meanwhile the only membrane *pilot* result in the book, "**8 m² pilot-scale testing** with D2EHPA", sits in the microfluidics chapter at `09:149`, and the Dy/NdFeB HFSLM result at `09:359` is likewise misfiled.

Critically, the glossary itself (`90-glossary.md:267-271`) names the field's central membrane limitation — "membrane stability is the reason it has not displaced [a cascade]" — and **chapter 12 never mentions it**. No flux, no lifetime, no carrier loss, no fouling.

**12:174-176 — MAJOR (actinide data in a column headed "REE Recovery").**
> "| TBP + TTA (2.7:3.2 mol%) | 65°C, 20 MPa | **88% Am, 69% Pu** |"
> "| TBP + HFA (5.3:6.8 mol%) | 95°C, 26 MPa | **95% Am, 83% Pu** |"

Americium and plutonium recoveries reported under "REE Recovery" in a section headed "Chelating Agents and Extractant Systems" for REE. Relabel the column and say these are actinide surrogates.

**12:207-209 — MAJOR (impossible values).** The NaOH-digested bastnäsite table reports Nd extraction of "**101%**" at 90 and 120 min and Ce/Pr of "100%". Extraction efficiencies above 100% are analytical artifacts and must be presented as such (">99%, within analytical uncertainty"), not tabulated as data.

**12:249-253 — MAJOR (unsupported, and conflates kinetics with selectivity).**
> "Higher extraction rates are observed for heavier REEs due to smaller ionic radii: **Nd extraction 30-100% faster than La** / This trend enables some inherent fractionation / **Heavy REEs preferentially extracted**"

No citation. A *rate* difference is used to assert an *equilibrium* preference — the same conflation the book correctly warns against in ch. 9. The direction is also contested: TBP/nitrate systems frequently show the opposite trend. Fix: cite, state whether the measurement is kinetic or equilibrium, and give the system.

**12:104-110 — MAJOR (whole section sourced to a trade-news URL).** `## Water-Based Recycling (2025)` cites only a Metal Tech News story and claims "**Achieves separation factors comparable to industrial solvent extraction**" — with no number, no pair, no conditions, and no primary reference. This is the strongest possible claim in the chapter carried by the weakest possible source.

**12:112-118 — MAJOR (press release presented as result).** `## DGA Ligand Technology` cites an ORNL news page and claims "Reduces chemical consumption and waste production / **Fewer separation stages required, reducing capital costs**" with no quantitative basis whatsoever.

**12:92-102 — MAJOR (modeled LCA/TEA outputs presented as measurements).** The FJH-Cl₂ list — ">90% purity, >90% yield, **87%** energy reduction, **84%** GHG reduction, **54%** operating cost reduction, **100% elimination** of water and acid" — reads as measured plant data. These are comparative model estimates from a lab-scale demonstration, and the downstream chloride separation that must follow is not accounted for in "100% elimination of water and acid." Note also this block is the *third* appearance of FJH in the book (ch. 7 in full, ch. 12 here, ch. 9 at `09:361` with a different set of numbers) and the `@tour2025sustainable` bib entry has a placeholder author list.

**12:295-303 — MAJOR (TEA table with no production rate).** "Reactor volume 4000 L | CAPEX $13.7-14.6 million | Year 1 OPEX ~$3 million | REE recovery >95% | **Purity: Battery-grade**". Without an annual tonnage the CAPEX is uninterpretable — no $/kg REO can be derived, which is the only number a reader wants. And "battery-grade" is not an REE product specification (it is a Li/Ni term); REE products are specified as %REO and %TREO. Give the throughput and the actual purity spec.

**12:57-70 — MAJOR (headline result with no limitations).** The MOF section reports "Pr/Lu separation factor: **796**", "Nd/Er: **273**", "high separation in a **single step**" with no feed concentration, no capacity (mg/g), no regeneration cycles, no stability in acid, and no scale. The chapter intro supplies the caveat once; the section itself must carry it, since the numbers travel (to `09:155`, to `04:176`, to the ch. 12 intro). Note also that Pr/Lu is the widest pair in the series — the informative comparison is the adjacent-pair SF, which is never given.

**Glossary mismatch — MINOR.** `90-glossary.md:177-181` says MOFs are pursued "on the hope that a **pore** can discriminate between **hydrated radii**." NCU-1's described mechanism (`12:62`) is chelation by uncoordinated carboxyl groups and triazole N inside the framework — a binding-site mechanism, not size-sieving of hydrated ions. Align the glossary with the chemistry the chapter actually describes.

**12:71-81 and 12:120-126 — MINOR (duplication with ch. 10).** The triamidoarene platform and M₄L₄ cages duplicate `10:211-221` and `10:372-382`; CSEREOX duplicates `10:73`. With a discrepancy: `12:77` claims "Near-quantitative recovery of **Nd/Pr directly from magnet scrap** without pH adjustment" while `10:211-215` describes the same system as precipitating *light REE nitratometalates* with no mention of magnet scrap.

**12:274 — MINOR (limitation omitted).** "**42% extraction efficiency** achieved / Preferential extraction of critical REEs / No hazardous reagents required" — 42% recovery is poor and the text does not say so.

**12:224 — MINOR (context missing).** "Coal ash contains 270-1480 ppm REEs and represents a **significant secondary resource**", followed by "Concentration factor increased to 3.23 ± 0.30". 3.23 × ~500 ppm = ~1,600 ppm, against bastnäsite ore at 50,000-100,000 ppm TREO. The comparison is needed for the reader to judge "significant."

---

# GAPS WORTH FILING AS ISSUES

**G1. Build the Part III comparison table ch. 4 promises, with conditions and scale per row.**
`04:10` claims the chapter "places every approach in this book on a single comparison," but the table at `04:171-180` omits precipitation, crystallization, coacervates/ABS, microfluidics, biosorption, phytomining, electrodialysis and scCO₂. Extend it to one row per Part III technology with columns: best reported separation factor, **the element pair**, feed (synthetic or real), concentration, temperature/pH, demonstrated scale (mg / g / L·h⁻¹ / t·y⁻¹), and TRL with a one-line justification. Every SF in this slice is currently quoted without its pair or its conditions; this table is the single highest-value fix in the review.

**G2. Rewrite the lanmodulin story around what it actually discriminates.**
Fix C1–C3 together: separate Ln/Ca selectivity from Ln/Ln selectivity everywhere; replace ">100-fold" affinity ratios used as separation factors with the measured single-column purity and yield, naming the pair; unswap `@cotruvo2023enhanced` (Nd/Dy) and `@park2024modulating` (light lanthanides); add the caveat that LanM monomer Kd varies only ~25× across the series. Touches `08:24-27`, `08:95`, `08:136`, `08:151`, `08:452`, `11:8-14`, `11:37-43`, `11:66-70`, `11:291`, `12:86`, `04:177`.

**G3. Verify or delete chapter 10's `## Sources` list and re-cite the molecular-design half.**
`10:449-473` is the only hand-written reference list left in the book and contradicts the stated policy in `93-appendix-provenance.md`; item 7 misattributes a Hatanaka paper to "Marsh, M. L.", and three items have no author. Meanwhile `10:331-448` — 118 lines including every quantitative claim about borate crystallization, M₄L₄ cages, H₂PDA and macrophosphi — has zero inline citations. Run these twelve through the CrossRef pipeline, add survivors to `references-cited.bib`, convert to inline `[@key]`, and delete the list.

**G4. Fix chapter 9's intensification numbers and make them mutually consistent.**
The kLa enhancement (`09:167`) is arithmetically wrong (20-400×, printed as 100-1000×) and the error propagates to `09:10` and `09:425`; the S/V figure (`09:169`) corresponds to a 700 µm channel while the text says "tens of µm" (`09:52`) and elsewhere claims only 2× over bulk (`09:76`); the extraction-time enhancement is given as 10-100× (`09:168`) and 150× (`09:66`); the "2-6× higher separation factor" row (`09:170`) is cited to two flow-pattern papers that contain no separation factors. Recompute every row of Table 2 from stated primary sources, and restore or delete the dangling `[^1]` footnote at `09:79`.

**G5. Give chapter 12 a real membranes section, and move the misfiled membrane results into it.**
Membranes get 26 uncited lines in the chapter that names them first, while scCO₂ gets 215. Pull the 8 m² HFSLM pilot (`09:149`) and the NdFeB Dy HFSLM result (`09:359`) out of the microfluidics chapter, add NF/UF rejection figures and flux, and write the limitations the glossary already knows about but the chapter never states: carrier loss, membrane lifetime, fouling, and why SLMs have not displaced cascades despite collapsing one into a single unit.

**G6. Add six figures — the book currently has none, and these six carry arguments prose cannot.**
(a) A coacervate phase diagram, salt vs polymer composition, showing precipitate / coacervate / single-phase regions — this would also fix the error at `08:59`. (b) Fractional approach to equilibrium vs contact time for two lanthanides, with the optimum kinetic-separation window marked — this is chapter 9's entire thesis (`09:15-24`, `09:157`) and is unintelligible in prose. (c) A four-panel flow-regime schematic (co-laminar / slug / droplet / pore-throat), without which the comparison table at `09:399` is unreadable. (d) Precipitation pH and solubility curves across the series for hydroxide and oxalate, ch. 10. (e) The LanM EF-hand coordination sphere plus the carboxylate-shift dimerization mechanism, ch. 11 (`11:46-64` describes a 3D mechanism in bullet points). (f) The NCU-1 pore with its carboxyl/triazole sites against Ln radius, ch. 12.

**G7. Add the ~25 missing glossary entries this slice depends on.**
Highest priority because they are load-bearing and undefined at first use: **EF-hand** (used ~15× in ch. 8 and 11), **Damköhler number** (ch. 9's kinetic-control argument rests on it), **enrichment factor / concentration factor / decontamination factor** (three distinct quantities, all confusable with separation factor, all used), **bioleaching** (referenced inside the `biosorption` entry but has no headword), and an entry mapping **HDEHP = D2EHPA** and **PC88A = HEHEHP = P507 = EHEHPA**, which the book currently presents as six reagents. Then: LLPS, IDP, LCST/UCST, cloud point extraction, kosmotropic, Hofmeister series, holdback reagent, didymium, TALSPEAK, saturation index, supersaturation, concomitant polymorphism, siderophore, phytomining, hyperaccumulator, red mud, coal fly ash, nanotrap, TRL.

**G8. Sweep the conversion seams.**
The strikethrough corruption at `08:263` (`~~4 … Ce4~~`) — grep the whole book for `~~`. The mid-word `{index}` insertions at `09:136`, `12:54`, `13:674`. Six `####` headings under `##` with no `###` in ch. 9 (`09:51, 84, 114, 175, 205, 229`) and the duplicated numbering-up section (`09:197` vs `09:205`). Missing terminal periods at `09:203` and `09:377`. Four spellings of bastnäsite across the book (`bastnäsite` / `bastnasite` / `bastnaesite`). "tons" vs "tonnes" within ch. 9. Equations in code blocks rather than MyST math at `10:56` and `10:175-176`. Four bibliography entries with placeholder authors — `others2019characterization`, `anon2024efficienta`, `yang2022pilot`, `tour2025sustainable` — each of which carries a load-bearing number.