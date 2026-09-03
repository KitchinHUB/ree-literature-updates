# Review: Prologue, Preface, Chapters 1–4

Scope: `src/00-prologue.md`, `src/00-preface.md`, `src/01-why-separation-is-hard.md`, `src/02-ore-to-feed-solution.md`, `src/03-solvent-extraction-fundamentals.md`, `src/04-technology-landscape.md`, with `src/90-glossary.md`, `myst.yml`, `converted/`, `citation-repairs.md`, and `tools/convert_link_citations.py` consulted for provenance. All line numbers are from `cat -n` on the current working tree.

Overall: the prologue and preface are clean and well written. Chapter 3 — described in its own first line as "the core teaching chapter" — is the problem. It was lifted nearly verbatim from `converted/chemistry-fundamentals.md` (an AI-drafted outline), and it contains several quantitative errors a student would copy into a proposal, plus one chemistry error (which REE extracts first) that inverts the industrial flowsheet. Chapters 1 and 4 have internal contradictions with each other and with Chapter 3 on the single most important number in the book (the per-stage separation factor and hence the stage count).

---

## src/00-prologue.md

Clean, with two items.

**L226 — MAJOR — `**DOIs:** 10.1016/j.mineng.2023.108234`**
The model issue offered as the template for "a good issue" carries a DOI that resolves (CrossRef) to *"Effect of pyrite textures and composition on flotation performance: A review"* (Minerals Engineering) — not the magnesium-sulfate ion-adsorption-clay leaching paper the example describes. In a prologue whose central lesson is "a DOI that resolves but points at the wrong paper is the most dangerous failure mode," the example exhibits that exact failure. Fix: either label the example explicitly as fictional (`**DOIs:** 10.xxxx/example`), or use the real MgSO₄-leaching paper the repo already verified, `pan2024` = `10.1016/j.jre.2024.04.025` (see `citation-repairs.md` L30), and adjust the "82%, Table 3" details to what that paper actually reports.

**L102–103 — MINOR — `| | |` / `|---|---|`**
Empty table header row; MyST renders a blank header band. Give it headers (`| Step | Count |`) or convert to a definition list.

## src/00-preface.md

Clean. Two consistency notes that are really findings against other files:

**L26 — MINOR — "why a separation factor of 1.5 is considered good"**
Chapter 4 L173 says solvent extraction has separation factor "2-10 (per stage)" and Chapter 3 L459–466 tabulates 4–32. The preface's framing is the correct one; the other two need to be brought into line (see below).

**L73 — MINOR — "Every citation resolves to an entry in a single verified bibliography."**
Chapter 1 L62 cites a CSIS web page as a bare Markdown hyperlink, outside the bibliography. Either add it as a `@misc` with URL (verified by the live-URL route the prologue describes) or soften this sentence.

## src/01-why-separation-is-hard.md

**L48 — MAJOR — "Similar ionic radii (only decreasing by ~0.01 Å across the lanthanide series)"**
Wrong, and it contradicts L14 of the same chapter, which correctly says ~0.01 Å *per element*. The total contraction La³⁺→Lu³⁺ is ~0.18 Å (CN 8: 1.160 → 0.977 Å), about 16%. Fix: "decreasing by only ~0.01 Å between neighbours (~0.18 Å across the whole series)".

**L13 — MINOR — "They share a +3 oxidation state."**
True as a generalization, but the two exceptions (Ce⁴⁺, Eu²⁺) are the only *cheap* REE separations in industry, and Chapter 3 L735–740 relies on the cerium one without ever having introduced it. Add one sentence: the exceptions are Ce (oxidizable to +4) and Eu (reducible to +2), and both are exploited industrially before solvent extraction ever starts.

**L19–21 — MINOR — "a per-stage separation factor near 1.5 needs a hundred stages to reach the 99.99% purity"**
This is the thesis of the book and it is asserted, not shown. A Fenske-type count (N_min = ln[(x_P/(1−x_P))·(x_R/(1−x_R))] / ln β ≈ 45 stages at total reflux for β = 1.5 and 99.99% at both ends; 2–3× that in practice) takes three lines and would make the claim checkable. Suggested home: Chapter 3, countercurrent cascade section, with a back-reference here. Also, "the 99.99% purity a magnet alloy demands" overstates: magnet-grade Nd/Pr oxide is typically 99–99.5%; 4N–6N is phosphor/optical grade. Say "99.9–99.99%" or "high-purity applications".

**L55–60 — MAJOR — "~70% of global rare earth mining / ~90% of separation and processing / ~93% of magnet manufacturing / ~92% of NdFeB magnet production"**
Four quantitative market-share claims, no citation, and the last two are near-duplicates of each other with different numbers (magnet manufacturing ≈ NdFeB magnet production). These read like a source was once attached. Cite (USGS Mineral Commodity Summaries and/or IEA Critical Minerals) and collapse the two magnet lines into one.

**L62 — MINOR — "([CSIS](https://www.csis.org/...))"**
Bare hyperlink citation; see preface note. Also, the seven elements should be named (Sm, Gd, Tb, Dy, Lu, Sc, Y) so the reader sees they are the medium/heavy ones — which is the point.

**L8–33 vs L35–51 — MINOR (structure) — seam**
The newly written essay opening (L8–33) and the pasted broad-review bullets (L35–51) say the same thing twice in two registers. "The Separation Challenge" (L45–51) repeats L10–17 almost bullet for bullet. Either delete L45–51 or fold its one new item (purity requirement) into the essay.

**L29 — MINOR (clarity) — "coordination geometry that changes abruptly partway along the series"**
This is the gadolinium break (CN 9 → 8 near Gd). Name it; it is not in the glossary and Chapter 10 presumably depends on it.

## src/02-ore-to-feed-solution.md

**L36 — MAJOR — "Enriched in middle REEs and heavy REEs" (monazite)**
Wrong. Monazite is light-REE dominated (Ce > La > Nd > Pr; typically >90% LREE by mass), only modestly richer in mid/heavy REE than bastnäsite. Xenotime (item 3) and the clays (item 4) are the HREE sources. Fix: "Light-REE dominated like bastnäsite, but with somewhat more Nd, Sm, Gd and a few percent HREE; the thorium is the distinguishing feature."

**L30 — MINOR — "Bastnasite (REE·FCO₃)"**
Non-standard formula. Use RE(CO₃)F, matching the glossary's (Ce,La)CO₃F. Also spell it consistently — text uses "Bastnasite", glossary and index use "bastnäsite".

**L33, L37, L40 — MINOR — "Typical composition: 60-70% REO"**
These are *flotation concentrate* grades, not mineral or ore compositions (Mountain Pass ore is ~7–8% REO; pure bastnäsite is ~75% REO). Say "concentrate".

**L45 — MINOR (clarity) — "Recent work by [@han2024efficient] focuses on this feedstock"**
Citation-driven prose that tells the reader nothing. Replace with the claim the paper supports (HPOAc extraction from sulfate clay leachate) or cross-reference [](#ion-adsorption-clays) and drop the sentence.

**L95–110 — MAJOR (gap/misleading) — "Sulfate Solutions (Ion-Adsorption Ores)"**
Two problems. (a) The chapter treats "sulfate liquor" as arising only from clay leaching. The largest sulfate liquors in the industry come from *sulfuric acid baking* of Bayan Obo mixed bastnäsite–monazite concentrate — the dominant Chinese route — and that route is absent from the "Dissolution" section entirely, even though the glossary's `cracking` entry describes it. (b) Clay leachates (~1 g/L REO) are not fed to solvent extraction directly; they are precipitated (oxalate/carbonate/ammonium bicarbonate), calcined or redissolved in HCl, and *then* extracted. The "Challenges" list (L108–110) implies direct SX of the leachate. Add a paragraph on H₂SO₄ bake → water leach → double-sulfate/oxalate precipitation → HCl redissolution, and state explicitly that precipitation-and-redissolution is the standard way any dirty liquor becomes an SX feed.

**L98 — MINOR — "Clay-REE³⁺ + (NH₄)₂SO₄ → REE₂(SO₄)₃ + NH₄⁺-Clay"**
Unbalanced. Write as an ion exchange: 2 Clay–RE + 3 (NH₄)₂SO₄ → RE₂(SO₄)₃ + 6 Clay–NH₄ (or use the per-ion form).

**L109 — MINOR — "Sulfate can precipitate with some extractants"**
Not the actual issue. Sulfate complexes RE³⁺ in the aqueous phase (RESO₄⁺), lowering D for cation-exchange extractants; the precipitation problem is Ca/Na RE double sulfates at high loading. Restate.

**L57, L85, L87 — MINOR (unsupported) — "Lower viscosity than nitrate solutions" / "Lower maximum REE concentration (viscosity limits)" / "Decomposition risk at high temperatures"**
Uncited, vague, and the first two are questionable (concentrated RE nitrate liquors of >1 M are routinely used in TBP circuits). Cut or cite.

**L112–125 — MINOR (gap) — Feed purification**
No cross-reference to [](#thorium-management), which the preface uses as its example of a link worth following. "Buffer if needed (acetate, citrate buffers)" (L121) is not industrial practice for RE chloride feeds and will mislead; qualify as laboratory-scale. Add one line that Fe³⁺ must be *fully* removed upstream because it loads onto D2EHPA/PC88A irreversibly (see Chapter 3 L311 finding).

## src/03-solvent-extraction-fundamentals.md

### Correctness — blockers

**L749 — BLOCKER — "La extracts preferentially (higher K~ex~)"**
Inverted. For every acidic organophosphorus extractant (D2EHPA, PC88A, Cyanex 272) the distribution ratio *increases* with atomic number: D(La) < D(Ce) < D(Pr) < D(Nd) < … < D(Lu). Lanthanum is the *least* extracted light REE; in a La/(Pr,Nd) split, Pr and Nd load onto the organic and La is recovered from the raffinate. L750–751 and L757 ("Product: 1.8 M La in HCl") propagate the error. This is the single fact a student most needs from this chapter and the chapter never states it anywhere. Fix the example and add an explicit paragraph on extraction order (and the pH₁/₂ trend) near L415.

**L638–639 — BLOCKER — "D = 10, O/A = 1/3 → 97% extraction per stage" / "D = 0.1, A/O = 1/5 → 95% stripping per stage"**
Arithmetic is wrong. Single-stage extraction fraction = E/(1+E) with extraction factor E = D·(O/A) = 10/3 → 77%, not 97%. Stripping with D = 0.1 and A/O = 1/5 (i.e. O/A = 5): fraction remaining in organic = 0.5/1.5, so 67% stripped, not 95% (if A/O = 5 was intended, 98%). The equation on L634 ("(O/A)_ext × D = (A/O)_strip × (1/D_strip)") is not a design relation found anywhere; it is an invented identity. Replace with the extraction-factor definition and the Kremser equation, and redo the example.

**L643–645 — BLOCKER — "CF = (O/A)_extraction × (A/O)_stripping … (1/3) × (5/1) = 5/3"**
Formula is inverted and the example contradicts the ratios just given. Metal in aqueous volume A moves into organic volume O (concentration ×A/O = 3), then into strip volume A′ (× O/A′ = 5): CF = (A/O)_ext × (O/A)_strip = 15, not 1.7. As written, (1/3)×(1/5) = 1/15.

**L264, L747, L757 — BLOCKER — "REE³⁺ = 1.0 M … 30% D2EHPA … O/A = 1/3 … Product: 1.8 M La"**
The worked example violates extractant capacity by more than an order of magnitude. 30 vol% D2EHPA ≈ 0.9 M HL = 0.45 M dimer; the tris-complex RE(HL₂)₃ consumes 3 dimers per RE, so the ceiling is ~0.15 M RE (~25 g/L REO), and L388 itself says operate at 30–40% of that. Feeding 1.0 M RE at O/A = 1/3 asks the organic to carry 3 M. Real plants run ~1–1.5 M saponified P507, O/A ≥ 1, and loaded organics of ~0.2 M RE. Rebuild the example with consistent numbers.

**L737 — BLOCKER — "Oxidize Ce³⁺ to Ce⁴⁺ (add NaOCl at pH 9) — Ce(OH)₄ precipitates — Result: La-Pr-Nd mixture"**
At pH 9 every RE(OH)₃ precipitates (RE hydroxides come down at pH ≈ 6.5–8), so this step would precipitate the whole feed. Industrial practice is either oxidative roasting (Ce → CeO₂, insoluble in dilute HCl, stays in the residue — which is what the L725 roast actually does) or NaOCl/KMnO₄ oxidation at pH ≈ 3–5 followed by Ce(OH)₄ precipitation. Fix and reconcile with L725.

### Correctness — major

**L459–466 — MAJOR — separation factor table: "Ce-Pr 8 / Pr-Nd 4 / Nd-Sm 16 / Gd-Tb 32" attributed to [@tanaka2021revaluating] under "Δ pH₁/₂ (D2EHPA)"**
The table is internally consistent (β = 10^(3ΔpH₁/₂)) but the values are 3–10× above measured ones and contradict L21 ("near 1.5 is normal") and Chapter 1. Adjacent-pair β for D2EHPA/PC88A in chloride are roughly Ce/La 2–4, Pr/Ce ~1.5–2, Nd/Pr 1.3–1.5, Sm/Nd 5–7, Tb/Gd 3–6, Y/Ho ~1.2–1.5. Pr/Nd at β = 4 would make the industry's hardest split easy. Also the cited paper is a PC-88A (not D2EHPA) study. Replace with the tabulated values in [@xie2014critical] (which gives them by extractant) and label the extractant correctly.

**L52 — MAJOR — "DGA (amides) | 0.5-3.0 | 0.1-0.5" in the pH table**
Backwards. Diglycolamides (TODGA etc.) are neutral, solvating extractants that load from *concentrated* nitric acid (1–4 M, i.e. pH < 0) and are stripped with *dilute* acid or water. Putting them in a "high pH extracts / low pH strips" table with the acidic extractants inverts their chemistry. Move them to a separate row with "extraction: 1–4 M HNO₃; stripping: 0.01–0.1 M HNO₃" or drop the row and point to Chapter 13.

**L55–79, L792 — MAJOR — salting-out section: "NaCl (0.5-3 M) … Moderate salting-out effect … Can provide 1-2 orders of magnitude improvement in distribution ratio"**
Conflates two mechanisms. Nitrate salting agents raise D for *neutral* extractants (TBP) by mass action on RE(NO₃)₃·3TBP. For the *cation-exchange* extractants the chapter is mostly about (D2EHPA, PC88A), adding NaCl generally *lowers* D (chloro-complexation, lower RE³⁺ activity coefficient, Na⁺ competition). The "1-2 orders of magnitude" applies to TBP/nitrate only. Note also that this passage is where the fabricated `sun2018nature` was replaced by `rydberg2004solvent` (`citation-repairs.md` L79–86); the substitute supports the textbook mechanism but not the NaCl/acidic-extractant claim. Split the section: neutral extractants (salting-out works), acidic extractants (ionic strength usually hurts).

**L126–128 — MAJOR — "High ionic strength (I > 1 M): Salting-out effect dominates / Low ionic strength (I < 0.1 M): Activity coefficient corrections needed"**
Backwards as a statement about activity coefficients: at I < 0.1 M Debye–Hückel corrections are small and calculable; it is at I > 1 M that they are large and require Pitzer/SIT treatment — which is what the glossary's `activity coefficient` entry correctly says. Rewrite.

**L311–323 — MAJOR — Scrubbing: "Remove co-extracted impurities (Fe³⁺, Al³⁺, Ca²⁺) … Impurities with lower K~ex~ values strip preferentially"**
Fe³⁺ has a *higher* affinity for D2EHPA/PC88A than any RE and is notoriously hard to strip (needs concentrated HCl, oxalic acid, or reduction to Fe²⁺). It cannot be scrubbed off at pH 2–3 while RE stays. This is exactly why Chapter 2 says iron is removed upstream. More importantly, the section misses what scrubbing is *for* in REE plants: removing the less-extractable REE from the loaded organic (e.g. scrubbing Pr off a Nd-loaded organic with a portion of the Nd strip liquor) — the mechanism by which a fractional cascade achieves purity on both ends. Rewrite around REE-on-REE scrubbing; treat Fe/Al as an upstream problem.

**L446–458, L790 — MAJOR — "Extraction is typically exothermic [@khoshoei2025crown] … ΔH ≈ -20 to -40 kJ/mol (for D2EHPA systems)" / "Stripping: 40-60°C (elevated T favors endothermic reverse reaction)"**
Overstated and mis-cited. The citation is a crown-ether review, not a D2EHPA calorimetry source. Enthalpies for RE extraction by HDEHP/PC88A are small and of *either* sign depending on element and medium (extraction by PC88A is reported endothermic for several REE), and industrial stripping is done at ambient temperature, not 40–60°C. Replace with a hedged statement and cite the calorimetric literature that Chapter 13 already covers (the two-phase calorimetry entry mapped in `tools/convert_link_citations.py` L67–69 is the right source). Fix units on L790: "ΔH = -30 kJ" → kJ/mol.

**L159 — MAJOR — "Flash point 60-80°C (vs. 40°C for hexane)"**
n-Hexane's flash point is about −22°C. As written it understates the hazard difference by 60 K. Also, generic kerosene (Jet A) has a flash point ≥38°C; the 60–80°C figures belong to the dearomatized SX diluents (Escaid 110, Shellsol D70). Correct hexane and say which product the 60–80°C refers to.

**L131 — MAJOR — "Kerosene is a mixture of C₉-C₁₆ alkanes … with some aromatic content (10-20%)"**
Industrial SX diluents are *dearomatized* (<1% aromatics, e.g. Escaid 110, Shellsol D70/D80, Isopar) precisely because aromatics change extractant aggregation and phase disengagement. L178–182 then describes Isopar as "used in pharmaceutical/food applications" when it is one of the most common SX diluents. Fix both.

**L569 vs L676–678 — MAJOR — "Very high interfacial area (500-2000 m²/m³)" (membrane contactors) vs "Mixer-settlers: a = 50-200 cm²/cm³; Pulsed columns 100-500; Centrifugal 500-2000 cm²/cm³"**
Unit mix-up. 50–200 cm²/cm³ = 5,000–20,000 m²/m³, which would make a mixer-settler 10–40× *higher* in area than the membrane contactor the text calls "very high". Agitated dispersions are typically ~500–3,000 m²/m³ (a = 6φ/d). The cm²/cm³ numbers are almost certainly m²/m³ values mislabelled. Correct units and reconcile the two passages.

**L497, L612, L628, L763, L795 — MAJOR — "Number of stages: 4-8 extraction, 2-4 stripping" / "Total stages: 8-15" / "Pr/Nd … Typically requires 8-12 stages"**
Contradicts Chapter 1 L19 ("hundreds of … stages"), Chapter 4 L47, and the chapter's own L21–25. 4–8 stages is right for *bulk recovery* of REE from an impure liquor (one solute, high D). An adjacent-pair *separation* at β ≈ 1.4 (Pr/Nd) needs 60–100+ stages in fractional configuration. The chapter never draws this distinction, and a reader will leave believing a Pr/Nd plant has a dozen stages. Add the distinction explicitly and correct L763.

**L336, L755 — MINOR — "4 M HCl, pH ≈ 0"**
4 M HCl is pH ≈ −0.6 on concentration alone (lower on activity). Say "4 M HCl" and drop the pH, or use 1 M.

**L733 — MINOR — "Adjust pH to 3.5 with NaOH … Result: Clean 1.0 M REE solution in 0.01 M HCl"**
pH 3.5 is [H⁺] ≈ 3×10⁻⁴ M, not 0.01 M (pH 2).

**L36 vs L246 — MINOR (clarity) — two different extraction equations**
L36 writes the monomer form (3 HL → REL₃), L246 the dimer form (3 (HL)₂ → RE(HL₂)₃), with no sentence saying the first is the simplified version of the second. State it once.

**L360–361 vs L396, L828 — MINOR — "Organic phase loss: <0.01% per cycle" vs "Makeup rate: 0.1-1% per cycle"**
Off by 10–100× from each other; neither is cited. Pick one, cite it, and note that entrainment and crud losses dominate over solubility loss.

**L413 — MINOR — "Rate-limiting step: usually aqueous diffusion"**
Overconfident. For PC88A with heavy REE, interfacial reaction kinetics are slow enough to matter (minutes), which is why L331 gives 5–15 min stripping. Hedge.

**L511 — MINOR — "Better stage efficiency than mixer-settlers"**
Mixer-settlers approach ~95–100% of one theoretical stage per unit; columns are characterized by HETS precisely because a unit height is *less* than a stage. Say "higher throughput per unit volume" and drop the efficiency claim.

**L537 — MINOR — "Robatel CINC extractors"**
Two different manufacturers (Rousselet-Robatel; CINC Industries). Separate them.

**L715–717 — MINOR (verify) — "LANL Super Separator uses automated sampling and ICP-AES analysis / Closed-loop control with Bayesian optimization" [@augustine2024advancing]**
Verify that the cited paper describes a device by that name and Bayesian closed-loop control; the title is about ML-guided high-throughput screening. The same citation is also attached to L696 ("Key control variables") which lists in-line pH meters and mass-flow controllers — generic process-control content the paper does not cover.

### Unsupported claims

**L765–783 — MAJOR — "Material and Energy Balance (Approximate) — For 1000 kg/day REO production: Concentrate 1700 kg/day; HCl (37%) 3000 kg/day; NaOH (50%) 2500 kg/day; … Roasting 1.5 GJ/day; … Total ~2000 kWh/day + 4.5 GJ thermal"**
Nineteen lines of specific plant numbers, no citation, no basis shown. The reagent stoichiometry is roughly defensible (I checked: ~1.8 t of 37% HCl for dissolution alone) but the energy figures are unsourced. This is the kind of passage the prologue warns about. Either derive it visibly from the stoichiometry with the assumptions stated, cite a TEA (and cross-reference Chapter 17), or delete.

**L275–280 — MINOR — "Example with D2EHPA [@agarwal2020comparative]" with log D = −1.5, 0.0, 1.5, 3.0**
These are idealized slope-3 values, not measurements, yet they are presented as data from a specific paper. Label as "illustrative, assuming slope −3 and pH₁/₂ = 2".

**L346–350 — MINOR — "Stripping efficiency [@agarwal2020comparative]: pH 0.5 ~95%, pH 1.0 ~85%, pH 1.5 ~60%"**
Same pattern; stripping efficiency depends on which REE (heavy REE loaded on D2EHPA need 4–6 M HCl). Label as illustrative or quote the actual numbers from the paper.

**L482, L493–497, L520–525, L542 — MINOR — "demonstrated up to 100 m³ units", "Mixer: 1-5 m³; Settler: 5-20 m³", "Pulse frequency 60-120 cycles/min …", "10-100× smaller"**
Equipment figures with no citation. Cite Rydberg (it has these) or a vendor datasheet.

### Clarity / structure

**L8–30 vs L32 onward — MINOR (seam)**
The essay-voice introduction stops at L30 and the rest is an unmodified bullet outline (`**Purpose**:`, `**Advantages**:`, numbered lists). Readable, but the chapter would benefit from at least one prose paragraph per H2 tying the bullets together — especially before L460 (contactors) and L587 (cascades).

**L785–840 — MINOR (structure) — "Summary and Key Takeaways"**
Fifty-five lines that repeat L107–212 ("Why Kerosene?" appears as a heading twice: L136 and L797; "pH Swing Mechanism" at L213 and L809). Cut to the Critical Parameters table (L787–795) and the seven-item Practical Implementation list, and fix the tolerance inconsistency between L834 ("±0.1 units") and L98 ("0.2-0.5 pH units drift acceptable").

**L63, L322–323, L360, L420, L422, L595, L670, L749 — MINOR (formatting) — `c~i~`, `K~ex~`, `P~HL~`, `[HL]~org~`, `K~overall~`**
Pandoc `~subscript~` syntax survived conversion and MyST does not render it; they will appear literally as tildes. Same for the Unicode math-script subscripts at L226–232 (`ₒᵣ𝓰`, `ₐ𝓆`). Convert all equations in the chapter to `$...$` math.

**L240 — MINOR — "DEHPA"** — the chapter otherwise says D2EHPA. Pick one and add a synonym line (D2EHPA = HDEHP = DEHPA = P204; PC88A = P507 = HEH[EHP] = EHEHPA — the Tanaka citation title uses the last form).

**L194, L211, L390 — MINOR (clarity) — "third-phase formation"**
Used three times, never defined, absent from the glossary.

**L590–603 — MINOR (clarity) — McCabe–Thiele section**
Describes a single-solute recovery construction and does not say so; a reader expecting to learn how *separation* between two REE is designed gets nothing here. See the gap below.

**L605–612 — MINOR (clarity) — "Feed enters at intermediate point / Fresh organic enters at bottom / Loaded organic exits at top / Raffinate exits at bottom"**
"Top/bottom" is column vocabulary applied to a mixer-settler train, and "feed at an intermediate point" is only meaningful in the fractional (extraction + scrub) configuration the text never names. Without a figure this is unfollowable.

## src/04-technology-landscape.md

**L23–24 — MINOR — "Two technologies in that table are at TRL 9 and everything else is at 3–7."**
The table (L171–180) has three rows at TRL 9 (solvent extraction, ion exchange, molten salt electrolysis).

**L173 — MAJOR — "Solvent Extraction | 2-10 (per stage) | 95-99.9%"**
Both cells contradict the rest of Part I. Per-stage β for adjacent pairs is ~1.3–2 (Chapter 1 L20, Chapter 3 L21, preface L26); 2–10 is the range for *non-adjacent* or group splits. Purity of 95–99.9% understates industrial SX, which routinely delivers 99.9–99.99% Nd₂O₃ and 5N for some oxides; L48 repeats the same understatement. Reconcile with L16–17 (IX needed only above ~99.99%).

**L44 — MAJOR (unsupported) — "Cyanex® 572 - emerging alternative that reduces acid consumption by >30% compared to PC88A"**
Vendor claim, no citation. Cite Solvay/Cytec's published comparison or a peer-reviewed study, or soften to "marketed as requiring less acid to strip heavy REE than PC88A".

**L40 — MINOR (gap) — "PC88A/HEHEHP … industrial standard"**
States the fact without the reason, which is a one-liner worth having: D2EHPA binds heavy REE so strongly that stripping needs ~6 M HCl; PC88A is weaker, so it strips at ~1–2 M and became the Chinese industry's workhorse (P507).

**L54–56 — MINOR — "Medium REEs: Sm, Eu, Gd / Heavy REEs: Tb, Dy, …"**
Glossary (L109–112, L165–167) defines HREE as Gd–Lu + Y and LREE as La–Eu/Gd. Both conventions exist; the book should state one and note the other. Also, the industrial three-group split is usually La–Nd / Sm–Gd / Tb–Lu+Y — which matches L54–56 — so the glossary is the one to amend.

**L66 — MINOR — "Can achieve purities >99.99999% (7 nines)"**
Overclaim; 5N–6N is what is routinely reported for displacement IX. L16 says ≥99.9999% — make them agree.

**L13–18 — MAJOR (gap) — "it does so by displacement chromatography rather than by staging"**
The chapter says IX "has no chapter of its own" and then never explains it. "Displacement chromatography" is undefined (and not in the glossary), and the actual mechanism — RE loaded on a cation resin, eluted with EDTA (or HEDTA/citrate) against a retaining ion such as Cu²⁺ or Zn²⁺, so the RE band self-sharpens into contiguous pure zones in order of complex stability — is the one thing a reader needs. Add ~150 words on the Spedding/Powell process and why its throughput is limited (band length scales with resin bed, cycle times of days–weeks, dilute product). The resin-type table (L77–82) does not substitute for this.

**L106 — MINOR (unsupported) — "Demonstrated for heavy metal removal (Cu²⁺, Pb²⁺) with translation to REE recovery"**
Uncited. The original source citation here (`tools/convert_link_citations.py` L49–52) was a chitosan drug-delivery paper — i.e. fabricated — and was replaced by `molinacaldern2022advances`, which supports L85 but not this sentence.

**L109–116 — MINOR (verify) — µPIBs: "Magnetic responsiveness for easy recovery"**
The citation was swapped from a fabricated Sep. Purif. Technol. URL to `croft2024online` (Minerals Engineering). Verify the µPIBs in that paper are magnetically responsive; Kolev-group polymer inclusion beads are generally not. If not, delete the bullet.

**L140–147 — MINOR (unsupported) — IIP performance table "Selectivity coefficient 10-100× … Adsorption capacity 20-100 mg/g … >10 cycles … 30-120 minutes"**
Generic ranges with no source; the only citation in the section (`zhao2025ultra`, itself a swap-in for a fabricated Chem. Eng. J. link) is a single Tm-IIP paper and cannot support a "typical value" table. Cite a review or drop the table.

**L149–167 — MINOR — "Advanced Chelating Resins … Bis-picolinic Acid Resins: Exceptionally high selectivity for Am/Cm over lanthanides"**
Uncited throughout, and the Am/Cm item is minor-actinide chemistry with no bearing on REE separation. Cut it; cite the aminophosphonic and diglycolamic resin statements.

**L169–182 — MAJOR (structure + unsupported) — Comparison table**
L10 promises the chapter "places every approach in this book on a single comparison". The table omits coacervates, microfluidics, selective crystallization, and hydrometallurgical/pyrometallurgical routes (four of the book's Part II–III chapters) while including two rows that are not separations at all: Flash Joule Heating (a feed-activation/leaching aid) and Molten Salt Electrolysis (a reduction to metal). "MOF Nanotraps 270-800" is a specific paper's number with no citation; "Lanmodulin … Pilot … TRL 4-5" overstates (bench-scale columns). No row has a source. Rebuild the table with one row per Part II/III chapter, cite each row's β and TRL to the chapter that discusses it, and drop the two non-separation rows or move them to Chapter 7.

**L30–34 — MINOR (seam) — "The phases separate (like oil and vinegar)"**
Tonal drop from L8–24; also, a reader who has just finished 840 lines on the same subject in Chapter 3 does not need a three-step "principle of operation". Replace L26–35 with a two-sentence back-reference to [](#solvent-extraction-fundamentals).

**L8–11 — MINOR (gap)** — No forward links to the Part III chapters the comparison table is meant to index. Add cross-references per row.

## src/90-glossary.md — terms used in the slice and not defined

Missing: **third phase / phase modifier** (Ch3 L194, L211, L390), **diluent** (defined only inside `extractant`), **salting-out** (Ch3 L54), **pH₁/₂** (Ch3 L416), **extraction factor** (needed for the corrected L638 example), **HETS** (Ch3 L525), **TRL** (Ch4 L22, L182), **McCabe–Thiele** (Ch3 L590), **entrainment** (Ch3 L680), **saponification** (not in the text either — see gaps), **displacement chromatography** and **chromatography** (Ch1 L9, Ch4 L16), **REO** (Ch2 L33), **gadolinium break** (Ch1 L29), **fractional extraction** (needed by Ch3 L605), **polymer inclusion bead/membrane** (Ch4 L109; the index tag points to a glossary entry that does not exist), **magnetic adsorbent** (Ch4 L84), and an extractant synonym table (D2EHPA/HDEHP/P204; PC88A/P507/HEH[EHP]/EHEHPA; Cyanex 272/572; TBP; Aliquat 336; Versatic 10), none of which are glossary entries despite being the chapter's main actors.

Also: `heavy rare earth elements` (L109) and `light rare earth elements` (L165) conflict with Ch4 L54–56; see above.

---

## GAPS WORTH FILING AS ISSUES

1. **Chapter 3: state the extraction order across the lanthanide series and fix the inverted La/Pr/Nd worked example.**
   The chapter never says that D rises monotonically La → Lu for acidic organophosphorus extractants (with Y falling near Ho/Er), and its industrial example (L742–757) has La loading first. Add a paragraph with the pH₁/₂ trend, a corrected example in which Pr/Nd load and La reports to raffinate, and consistent numbers (feed ≤0.3 M RE or O/A ≥ 1, product concentration derived from the correct CF formula).

2. **Chapter 3: replace the phase-ratio/concentration-factor section with the extraction factor, Kremser equation, and a Fenske-type minimum-stage estimate.**
   L631–645 contains three wrong equations/examples. Replace with E = D·(O/A), single-stage fraction E/(1+E), the Kremser expression for N stages, and N_min = ln[(x_P/(1−x_P))(x_R/(1−x_R))]/ln β, then show that β = 1.5 and 99.99% at both ends gives ~45 stages minimum — which makes Chapter 1's "a hundred stages" claim derivable rather than asserted.

3. **Chapter 3: add a section on fractional extraction cascades and REE-on-REE scrubbing (Xu Guangxian's countercurrent extraction theory), with a flowsheet figure.**
   The book's one cascade diagram request (preface L85) should be this: extraction + scrub sections, feed in the middle, two products, strip liquor recycled as scrub. Currently scrubbing is described as impurity removal (L310–323) and "feed enters at intermediate point" (L607) is unexplained. Include the 4–8 vs 60–100 stage distinction (bulk recovery vs adjacent-pair split).

4. **Chapter 3: add saponification of the extractant.**
   Industrial P507/P204 circuits pre-neutralize the extractant with NaOH or NH₃ (typically 30–50%) so that extraction does not crash the pH; this is the origin of the ammonia-nitrogen effluent problem that Chapters 6 and 17 presumably discuss. The chapter's "add NaOH to maintain pH" (L267) is a laboratory description of an industrial practice it never names.

5. **Chapter 2: add the sulfuric acid bake / caustic crack routes and the precipitate-and-redissolve step.**
   The dissolution section only covers oxide + HCl and oxide + HNO₃. Add H₂SO₄ baking of Bayan Obo concentrate (the largest single REE flowsheet in the world), NaOH digestion of monazite, and the oxalate/carbonate precipitation → HCl redissolution step that turns any leachate (including clay sulfate liquor) into an SX feed. Cross-reference [](#thorium-management).

6. **Chapter 4: write the ion-exchange section the chapter promises.**
   L13–18 says IX has no chapter of its own and is covered here; the section never describes displacement chromatography (EDTA eluent, retaining ion, self-sharpening bands) or why throughput is limited. ~200 words plus a schematic of the band structure. Define "displacement chromatography" in the glossary.

7. **Chapter 4: rebuild the technology comparison table so it indexes Part II–III.**
   One row per chapter (leaching routes, clays, pyro/halogenation, coacervates, microfluidics, crystallization, biological, membranes/MOFs) with β, purity, feed type, TRL, and a cross-reference; every number cited to the chapter or paper it came from; drop Flash Joule Heating and molten-salt electrolysis as non-separations. Bring the SX row into line with β ≈ 1.5 and 99.9–99.99% purity.

8. **Chapter 1: cite the supply-chain figures and add the Ce/Eu redox exceptions.**
   L55–60 has four uncited market-share numbers (two of them near-duplicates). Cite USGS/IEA and merge the magnet lines. Add one paragraph on Ce(IV)/Eu(II) as the two redox separations that are done before any cascade, since Chapter 3's example depends on the cerium one.