# Review: Part II "Upstream: Ore to Purified Feed" (chapters 5, 6, 7; plus ch. 2 and glossary)

Scope read in full: `src/05-hydrometallurgical-leaching.md` (1535 lines), `src/06-ion-adsorption-clays.md` (165), `src/07-pyrometallurgical-halogenation.md` (1044), `src/02-ore-to-feed-solution.md` (125), `src/90-glossary.md` (288); spot-checked `src/04-technology-landscape.md`, `src/11-biological-biomimetic.md`, `src/12-membranes-mofs-emerging.md`, `src/13-extraction-thermodynamics.md`, `src/93-appendix-provenance.md`, and `src/references-cited.bib` (every key cited in these chapters exists; the problem is what the keys are attached to, not whether they resolve).

Headline: none of the three chapters is clean. Ch. 7 has the worst citation integrity I have seen in the book so far (roughly 30 citations attached to sentences the cited work cannot support, plus two whole sections with zero citations and a double conclusion). Ch. 5 has several unbalanced equations, an industrial description of Mountain Pass that is wrong, a waste table off by 1-2 orders of magnitude, and heavy duplication with ch. 6/11/16/17. Ch. 6 is the best written but is still a memo organised around one minor paper, with its Moab numbers now sourced to footnotes that no longer exist.

---

## `src/05-hydrometallurgical-leaching.md`

### Correctness

| Ref | Sev | Quote | Problem | Fix |
|---|---|---|---|---|
| `src/05-hydrometallurgical-leaching.md:251` | BLOCKER | `2 REE·FCO₃ → REE₂O₂CO₃ + 2 HF↑` | No hydrogen on the left, C and O do not balance (C₂O₆ → C₁O₅ + F₂H₂). Chemically, dry calcination gives the oxyfluoride (REOF + CO₂); HF only evolves on hydrolysis with steam. | `2 REEFCO₃ → 2 REEOF + 2 CO₂` then `2 REEOF + H₂O → REE₂O₃ + 2 HF` (steam roast), and say that fluorine is retained as REOF in a dry roast. |
| `:279` | MINOR | `2 REE·FCO₃ + Na₂CO₃ → REE₂O₂CO₃ + 2 NaF + CO₂↑` | C 3 vs 2, O 9 vs 7. | `… + 2 CO₂↑` |
| `:291-294` | MAJOR | "NaREEO₂ … Water soluble!" | NaLnO₂ is not water-soluble; it hydrolyses to NaOH + Ln(OH)₃/LnOOH, which the chapter itself writes at :298. The "soluble" bullet contradicts :298 and the "double sulfate" motivation. | Replace with "hydrolyses in water to NaOH and REE hydroxide; the hydroxide is then acid-dissolved". |
| `:299` | MINOR | `REEO(OH) + 2 HCl → REECl₃ + H₂O` | Cl 2 vs 3. | `REEO(OH) + 3 HCl → REECl₃ + 2 H₂O` |
| `:302` | MINOR | `2 NaREEO₂ + 3 H₂SO₄ → REE₂(SO₄)₃ + Na₂SO₄ + 3 H₂O` | S 3 vs 4. | `… + 4 H₂SO₄ → … + 4 H₂O` |
| `:319` | MAJOR | `REE·FCO₃ + 3 NH₄Cl → REECl₃ + NH₃↑ + NH₄F + CO₂↑ + H₂O` | N 3 vs 2, H 12 vs 9. Also NH₄F does not survive 400-600 °C (it decomposes to NH₃ + HF near 100 °C), so "fluorine captured as NH₄F byproduct" (:325) is implausible; the "fluorine deactivation" in @chi2004 is a solid additive step. | `… → REECl₃ + 2 NH₃ + NH₄F + CO₂ + H₂O` for balance; re-read @chi2004 for what actually fixes the fluorine. |
| `:346-349` | MINOR | "After alkaline roasting … `REE₂O₃ + 3 H₂SO₄`" | The alkaline roast (previous section) produces NaREEO₂, not REE₂O₃; this equation belongs to the oxidative roast. Heading/content mismatch. | Say "after oxidative roasting"; for the alkaline product use the :302 equation. |
| `:352` | MINOR | "2-6 M (20-60 wt%)" | 2 M H₂SO₄ is ~18 wt%; 6 M is ~45 wt%. | "2-6 M (18-45 wt%)" |
| `:410-433` and `:1053-1067` | MAJOR | "70% H₂SO₄ at 90°C" (:422) vs "4 M H₂SO₄, 90°C, 3 h" (:1059) vs "Conversion to chloride (add HCl, evaporate H₂SO₄)" (:1067) | Two different acid strengths for the same plant (70 wt% is ~10.6 M); and you cannot "evaporate H₂SO₄" (bp 337 °C) out of an HCl solution. The historical Molycorp route was oxidative roast (~620 °C, Ce to Ce(IV)) followed by HCl leach (Ce stays in the residue), and the 2012-15 plant was HCl leach with chlor-alkali regeneration; sulfuric bake is Chinese Bayan Obo practice. As written, the "Industrial Example" describes neither. | Rewrite Mountain Pass as roast + HCl leach, with a citation (Gupta & Krishnamurthy or @castor2006rare); keep the H₂SO₄ bake as the Bayan Obo example. Delete "evaporate H₂SO₄"; sulfate-to-chloride conversion goes via hydroxide/carbonate precipitation and HCl redissolution. |
| `:452`, `:482`, `:521`, `:552` | MINOR | `(REE,Th)₂(SO₄)₃`, `(REE,Th)Cl₃`, `(REE,Th)(OH)₃`, `(REE,Th)₂O₃` | Thorium is tetravalent; writing it into trivalent formulas is wrong and hides exactly the chemistry (Th(SO₄)₂, ThO₂, Th(OH)₄) that makes Th separable. | Write REE and Th equations separately. |
| `:478-497` | MAJOR | "HCl leaching … 140-180°C … Autoclave required" | Monazite is essentially insoluble in HCl; direct HCl digestion is not an industrial or well-documented route and the paragraph carries no citation. | Delete or cite a specific study and label it "laboratory only". |
| `:520` vs `:533` | MAJOR | "Alkaline digestion (300-400°C)" then "Temperature: 140-200°C (autogenous pressure)" | Direct contradiction within one subsection. Industrial NaOH digestion is 140-150 °C in 60-70 % NaOH at atmospheric pressure (the boiling-point elevation of concentrated caustic makes the autoclave unnecessary), which is also what ch. 7 :308 and ch. 2 say. | Use 140-150 °C, delete "autogenous pressure" and "300-400°C" (or label the latter as caustic fusion, a different process). |
| `:566` | MINOR | "Preferentially dissolves thorium (5-15% Th extraction)" | "Preferential" and "5-15 %" cannot both describe the same step. | State what @borai2016modified actually reports (fraction of Th vs REE dissolved). |
| `:583-585`, `:1006` | MAJOR | "**Primary amine extraction** … Alamine 336 (trioctylamine)" | Alamine 336 is a tertiary amine (tri-C₈/C₁₀). Primary-amine Th extraction (@amaral2010thorium) uses Primene JM-T, from sulfate liquor, not "HCl medium … pH 1-2". | Two correct options: "primary amine (Primene JM-T) from sulfate liquor" or "tertiary amine (Alamine 336)". Fix both places. |
| `:635` | MAJOR | "50% of world's heavy REE supply" | Ch. 6 :57 says "over 90 %" (cited to @zhou2020regolith). Ch. 5's figure is uncited. | Use ">90 %" and cite @zhou2020regolith. |
| `:690-691` | MINOR | "Helps mobilize Ce (can oxidize to Ce⁴⁺ and precipitate)" | Backwards. Ce in IAC ores sits as cerianite (Ce(IV) oxide) and is *not* exchangeable; reductive leaching mobilises it by reducing Ce(IV) to Ce(III). | Rewrite accordingly. |
| `:735-741` | MINOR | "0.2 % (NH₄)₂SO₄: 93 % … 1.0 %: 85 %"; "Lower concentration reduces competitive adsorption" | Suspiciously precise; and the mechanism explanation is not how ion exchange works (lower lixiviant concentration needs more pore volumes, which is what ch. 6 :80 says citing the same @shi2022column). The two chapters draw opposite lessons from one paper. | Reconcile with ch. 6; keep only what @shi2022column reports. |
| `:787` | MINOR | `REE³⁺ + 1.5 H₂C₂O₄ → REE₂(C₂O₄)₃↓` | 1 REE → 2 REE; no H⁺. | `2 REE³⁺ + 3 H₂C₂O₄ → REE₂(C₂O₄)₃↓ + 6 H⁺` |
| `:788` | MINOR | `REE³⁺ + 3 NH₄HCO₃ → REE(OH)CO₃↓ + 3 NH₄⁺` | C 3 vs 1. | `… → REE(OH)CO₃↓ + 3 NH₄⁺ + 2 CO₂ + H₂O` |
| `:892-896` | MAJOR | Bioleaching table: monazite 65-92 % with *Penicillium tricolor* [@brisson2015bioleaching] | Brisson et al. leached a few percent of the REE from monazite (tens of mg/L), not 65-92 %; and *P. tricolor* is from the red-mud bioleaching literature (Qu & Lian), not Brisson. Same concern for :937-938 "80 % in 14 days" [@corbett2017incorporation]. | Re-read both papers; replace with their actual numbers (which will make the "Research potential" framing at :938 harder to sustain). |
| `:868`, `:911` | MINOR | "Requires sterile conditions"; "Carbon-neutral process" | Heap bioleaching is not sterile; heterotrophic fungi fed glucose are not carbon-neutral. Both uncited. | Delete. |
| `:1019` | MINOR | `Ca²⁺ + SO₄²⁻ + PO₄³⁻ → CaSO₄·xH₂O↓ (traps phosphate)` | Not an equation (charge and P do not balance). | Prose, or write Ca₃(PO₄)₂ / REEPO₄ precipitation. |
| `:1176-1178` | MAJOR | "Typical E~a~: 40-80 kJ/mol (diffusion-controlled)"; "Doubling temperature → 2-5× faster" | 40-80 kJ/mol signals chemical control; diffusion control is typically <20 kJ/mol (this is also the criterion used at :1250-1256). "Doubling temperature" is meaningless in °C. Also pandoc `~a~` subscript markup leaked through conversion here and at :1250. | Swap the labels; replace with "roughly 2× per 10 °C"; fix markup (`E_a` in math). |
| `:1186` | MINOR | "Monazite: 6-12 M H₂SO₄" | :455 says 93-98 wt% (~18 M). | Reconcile. |
| `:1224` | MINOR | "Reducing for selective Ce oxidation" | Self-contradictory. | "Oxidizing (air) for selective Ce oxidation". |
| `:1280-1286` | BLOCKER | Waste table "Per ton REO [@jha2016hydrometallurgical]": "Ion-adsorption 20-50 tons ore" | At the chapter's own grade (0.05-0.3 % REO, :618) one ton of REO needs 300-2000 t of ore, not 20-50. The bastnäsite row (1.5-2 t) is evidently *concentrate*, not ore, so the table mixes bases. I doubt Jha tabulates any of this. | Recompute from grade and recovery and label the basis; drop the Jha citation unless the numbers are actually his. |
| `:1337-1353` | MAJOR | Energy table and "CO₂ footprint 10-15 t/t REO" attributed to @jha2016hydrometallurgical | These numbers do not read like Jha's review; the 15 GJ/t and 2 GJ/t figures at :1078 and :1168 are uncited and inconsistent with the table. Ch. 17 owns LCA. | Either source them (Vahidi & Zhao, Koltun & Tharumarajah, Weng et al.) or cut and point to ch. 17. |

### Unsupported / once-sourced claims
- `:113`, `:152`, `:176`: "Jaw crusher (1 m → 10 cm)", "χ ≈ 500-900 × 10⁻⁶ CGS", "500-2000 g/ton" — engineering numbers with no source; the citations nearby (@chen2023various is a magnetic-fluid paper, @zhou2024gravity is an Nb/Zr ore paper) do not carry them.
- `:614`: "~3000 tons/year REO (historical)" for IREL.
- `:696`: NaCl "60-75 %".
- `:1042-1170` (three "Complete Process Flowsheets"): zero citations across 130 lines, including "Overall REE recovery 65-75 %", "Energy ~15 GJ/ton", "Thorium recovery 95 %", "PLS 200-500 ppm" (vs :717 "200-1000 mg/L").
- `:1260`: "Ultrasound reduces leaching time 30-50 %" [@stojkovic2024recovery] — a coal-ash ultrasonic *roasting* paper.
- `:1357`: "DES REE extraction from waste 60-80 %" [@ni2023sustainable] — a Th DES paper.
- `:1402`, `:1439-1449`, `:1458`: ML "Demonstrated for ion-adsorption leaching"; the whole cost table; "acid 20-40 % of operating cost" — all uncited.
- `:644-649`: @xiao2015leaching (MgSO₄ paper) cited for the *traditional* (NH₄)₂SO₄ process; the Further Reading entry at :1530 describes it correctly.

### Clarity / seams
- `:1040` MAJOR: "described in the chemistry fundamentals review" — dangling reference to a source document; should be `[](#solvent-extraction-fundamentals)`.
- `:1176`, `:1250`: `k = A exp(-E~a~/RT)`, `k~s~, k~d~` — pandoc subscript syntax, renders literally in MyST.
- `:1435`: "Xenotime | Alkali roast preferred" — the text (:816-819) says alkaline *decomposition*; "alkali roast" is never defined anywhere. Glossary defines "cracking" but ch. 5 never uses the word (only ch. 6 :24 does).
- `:1494-1501`: "pH 0.5-2.0" then "adjusting the pH into the extraction range (2.5-4.0)" — ch. 2 :120 gives 0.5-4.0. Feed spec "0.5-2.0 M" (:1494) vs ch. 2 :125 "0.1-1.0 M". A student handed both chapters cannot tell what the SX feed is.

### Structure
- MAJOR: the ion-adsorption section (:616-797, ~180 lines) re-derives ch. 6 (formation, in-situ vs heap, MgSO₄, ammonia pollution, HMTA). Cut to the leach chemistry plus a pointer.
- MAJOR: bioleaching (:829-938) duplicates ch. 11 (`src/11-biological-biomimetic.md:268` "Siderophore-Mediated Bioleaching", *A. niger*, *G. oxydans*); urban mining (:1410-1426) belongs to ch. 16; LCA/energy (:1336-1353) to ch. 17.
- MINOR: each industrial process is told twice (Mountain Pass :410-433 and :1053-1080; IREL :603-614 and :1085-1123; in-situ :700-741 and :1128-1168), and the purified-solution spec is given twice (:1026-1038 and :1489-1503). The "Conclusions and Recommendations / Key Findings / Research Gaps" (:1462-1487) is memo voice.

---

## `src/06-ion-adsorption-clays.md`

| Ref | Sev | Quote | Problem | Fix |
|---|---|---|---|---|
| `src/06-ion-adsorption-clays.md:132` | BLOCKER | "1,002,109 lb of ammonia versus 5,816 lb of uranium … `[^1][^2]`" | Footnote markers with no footnote definitions anywhere in the file (grep finds only this line). The sources were deleted, leaving seven-significant-figure numbers, "42 wells", and the "razorback sucker" claim standing on nothing. | Restore the DOE Moab UMTRA annual report / EA citations as proper `[@…]` entries, or round and mark as approximate. |
| `:51` | MAJOR | "kaolinite converts to halloysite, lowering adsorption capacity" | Reversed. In regolith profiles the weathering sequence is feldspar → halloysite → kaolinite, and it is the halloysite-to-kaolinite transformation in the upper pedolith that lowers capacity (Li & Zhou, and @zhou2020regolith which is cited next to the sentence). | "halloysite converts to kaolinite". |
| `:37` | MINOR | `2 Clay-REE + 3 M2SO4 -> 2 Clay-M3 + REE2(SO4)3 (M = NH4+, ½ Mg2+ …)` | Plain-ASCII, "½ Mg²⁺" hack, "Clay-M3". | Two equations, one per lixiviant, in math mode; the ch. 5 :641/:681 forms are fine. |
| `:74-84` | MAJOR (structure) | "the Sobri paper"; "The paper that prompted this report" | The chapter is organised as a response to one Jurnal Teknologi HSC calculation. A new student will read it as the field's anchor. Also "this report" is a seam. | Reframe: present Eh-pH screening in general (with @sobri2025thermodynamic as one example), delete "this report". |
| `:80` | MINOR | "nitrate from nitrification forms LaNO3(2+)"; "SO4(2-) forms LaSO4+" only for Al₂(SO₄)₃ | Both are artifacts of an equilibrium calculation: NH₄⁺ "nitrifies" only because the diagram spans high Eh, and sulfate complexation is the same in (NH₄)₂SO₄ and MgSO₄ at equal sulfate. The text notes HSC's limits later but presents these as findings. | One sentence saying so. |
| `:84` | MINOR | "La (pH 0-5.8), Nd (0-5), Y (0-4.2)" | Over-precise windows from one database calculation. | "roughly pH <4-6, narrowing toward the heavies". |
| `:95` | MINOR | "~1.0-1.3 vs ~1.5-4 per stage" | Uncited; ch. 4 and the glossary give different SX numbers. | Cite or delete. |
| `:114`, `:117` | MINOR | "10-100x concentrated"; "A title search … returns essentially nothing" | The first is uncited; the second is a lab-notebook observation, not a checkable statement (there is SMB/continuous-IX lanthanide literature). | Cite; replace the search claim with what was searched and when, or drop. |
| `:25` vs `:70`, `:158-159`, `:146` | MINOR | Summary repeats body ("kaolinite sold without REE"); asphalt/drywall paragraph reads like a chat answer; "weakest-sourced" self-assessment | Memo residue. | Trim the Summary to what the body did not say; cut :158-159 or cite; drop :146. |

Gap specific to this chapter: it promises "the chemistry that makes them work" but gives no exchange-affinity series (why NH₄⁺/Mg²⁺ displace REE³⁺ at all), no pH dependence of exchange, no L/S or concentration numbers (those are in ch. 5), and no mention beyond one clause (:97) that Ce is locked in cerianite and Al is the main co-leached impurity.

---

## `src/07-pyrometallurgical-halogenation.md`

### Correctness

| Ref | Sev | Quote | Problem | Fix |
|---|---|---|---|---|
| `src/07-pyrometallurgical-halogenation.md:86` | BLOCKER | `CeO₂ + 2C + 2Cl₂ → CeCl₃ + 2CO` | Cl 4 vs 3. In the one chapter that is about this reaction. | `CeO₂ + 2C + 1.5Cl₂ → CeCl₃ + 2CO` (or double it). |
| `:515-517` | BLOCKER | "REF₃ → RE³⁺ + 3e⁻ → RE(metal) at cathode"; "Fluoride ions oxidized to F₂ gas at carbon anode" | Garbled half-reaction, and the anode chemistry is wrong: industrial oxide-fluoride electrolysis feeds RE₂O₃ into REF₃-LiF and the carbon anode is consumed to CO/CO₂ (which :555-557 says correctly). F₂/PFC evolution is the *anode effect*, a fault condition. | `RE³⁺ + 3e⁻ → RE` at cathode; `2 O²⁻ + C → CO₂ + 4e⁻` at anode; delete "F₂ gas". |
| `:969` | BLOCKER | "Global Scale: 280 Mt TiCl₄/yr" | World TiO₂ pigment is ~7-8 Mt/yr; chloride-route TiCl₄ is a few Mt/yr. Off by ~50-100×. | Recompute from @usgs2020titanium. |
| `:8-11`, `:19-20` | MAJOR | "converts rare earth oxides directly to volatile or low-melting chlorides … separates them by boiling point" | LnCl₃ boil at ~1600-1750 °C; they are the *non-volatile* products. What volatilises is the impurity chlorides (FeCl₃, AlCl₃, SiCl₄, POCl₃, ThCl₄), which is the actual win. Inter-REE separation by volatility is only demonstrated via AlCl₃ vapour complexes at ~80 % purity (:177). The intro sets up the wrong expectation for the whole chapter, and no LnCl₃ mp/bp data ever appears to back the "boiling points nearly as close together" line. | Rewrite the intro; add an LnCl₃ mp/bp table (see Gaps). |
| `:43` | MINOR | "direct halogenation is thermodynamically unfavorable without a reducing agent" | Overstated for Ln₂O₃: La₂O₃ + 3Cl₂ → 2LaCl₃ + 1.5O₂ has ΔG° ≈ -290 kJ at 298 K (ΔGf: LaCl₃ -998, La₂O₃ -1706) and stays negative to ~1000 K; it is true for CeO₂ (ΔG ≈ +40 kJ) and for TiO₂/Al₂O₃. Carbon's job for REE is to drive it to completion past REOCl and to scavenge O₂. | Say that, with the numbers. |
| `:95`, `:721` | MAJOR | "the >1200°C required for traditional roasting processes" | Bastnäsite roast is 500-700 °C (ch. 5 :259), acid bake 200-500 °C. The comparison is false and contradicts ch. 5. Cited to @zheng2019mechanism and @iaea2011radiation (a NORM guidance document). | Delete or compare with the actual roast temperature (which makes carbochlorination *not* lower). |
| `:108-122` | MAJOR | "12.54 kJ/mol … 11.22 kJ/mol … both stages controlled by chemical reactions" | Activation energies of 11-12 kJ/mol indicate diffusion control, not chemical control (ch. 5 :1250 uses the same criterion). Attributed to @yang2017ree, an NdFeB recycling review. | Cite the primary kinetics paper and state its own control assignment. |
| `:114` vs `:206` | MINOR | "Optimal temperature: 700°C" vs "Chlorination temperature 800°C" with otherwise identical parameters (12 % C, 60 min, 10 L/min, >93 %) | Same study, two temperatures. | Pick one. |
| `:283` | MAJOR | "Zhang et al. developed … SiCl₄ … [@zhang2015occurrence]" | @zhang2015occurrence is a review of REE in coal. The SiCl₄-defluorination / SC-CVT work is @huang2002rare (cited at :157). Wrong attribution by name. | Fix author and key. Also verify @huang2002rare's author list — the MMTB 2002 SC-CVT paper is by Wang et al., not "Huang, Li, Xue, Dong". |
| `:304-308`, `:572-580` | MAJOR | "H₂SO₄ digestion at 150-200°C; NaOH at 140-150°C in autoclave" | Contradicts ch. 5 (:455 200-250 °C; :520/:533 300-400 / 140-200 °C). Three chapters, three sets of numbers for one industrial process. NaOH digestion is atmospheric, not autoclave. | Own the numbers in ch. 5 and cross-reference from here. |
| `:334-346` vs `:438`, `:452-468` | MAJOR | FJH-Cl₂ numbers (87 %, 84 %, 54 %) cited to @deng2022rare; later "published in PNAS in September 2025" with no citation | @deng2022rare is *Science Advances* 2022 "Rare earth elements from waste" (FJH activation + acid leach). The FJH-Cl₂ paper is @tour2025sustainable (PNAS 2025), which is what ch. 12 :93 cites. The same three numbers appear twice in this chapter (:334-346 and :452-468). | Cite @tour2025sustainable, delete one of the two lists, and check ch. 12 for the same duplication. |
| `:446` vs `:444` | MINOR | "Rare earth oxides require >1350°C to react with chlorine" | Uncited, and contradicts the chapter's own 600-900 °C carbochlorination without explaining that FJH runs *without carbon*. | Explain, cite. |
| `:470` | MINOR | "licensed to Flash Metals USA, commercial production planned for Q1 2026" | Uncited press-release claim, now past its date (today is 2026-09). | Cite or cut. |
| `:479` vs `:523` | MAJOR | "Lower temperature requirement: 427-870°C" (fluoride MSE) vs "1323 K (1050°C)" | Internal contradiction; 427-870 °C is the chloride-eutectic range. | Fix. |
| `:546` | MAJOR | "Specific energy consumption: 2.3 kWh/kg-Nd" | Theoretical minimum for NdCl₃ decomposition at ~3 V is ~1.7 kWh/kg at 100 % CE; at the quoted "up to 83 %" CE the floor is ~2.1. A cell at 2.3 is at the thermodynamic limit, far below any real cell (industrial fluoride cells are ~10 V). Uncited. | Cite the primary paper and its cell voltage, or delete. |
| `:561-563` | MINOR | "CF₄ GWP 6,500× … C₂F₆ 9,200×" | These are IPCC SAR (1995) values; AR6 gives 7,380 and 12,400. Uncited. | Update and cite. |
| `:756` | MINOR | "H₂S to convert VOCl₃ to higher-boiling VCl₄" | VOCl₃ is removed by *reduction to solid VOCl₂* (H₂S, Cu, or organics); VCl₄ is not the target. | Fix. |
| `:867` | MAJOR | "Exothermic (~300 kJ/mol AlCl₃)" | From ΔHf: with CO the reaction (:861) is ~-32 kJ/mol AlCl₃; with CO₂ ~-160. Not 300 under either. | Recompute and say which carbon product. |
| `:916-920` | MINOR | "Norsk Hydro (1950-1987)"; "The Dow process (still operational)" | Norsk Hydro Porsgrunn ran ~1951-2002; Dow Freeport closed in 1998. | Fix dates; drop "still operational". |
| `:955` | MINOR | "<5 mg/L Ta" | Solid product; mg/kg or ppm. | Fix units. |
| `:963` | MINOR | "successful industrial separation … via chloride distillation" (Nb/Ta) | Industrial Nb/Ta separation today is MIBK/HF solvent extraction; distillation is historical. | Qualify. |
| `:971` vs `:859` | MINOR | "Aluminum TRL 7-8 (Demo)" vs "mature industrial technology" | Contradiction; AlCl₃ carbochlorination is commercial for AlCl₃ product, abandoned (Alcoa, 1985) for Al metal. | Say which. |
| `:978` | MINOR | "all 17 rare earth element oxides … at industrial scale" | The chapter's own tables mark Pm and Tm "Theoretical". | Soften. |
| `:18` vs `:52`, `:91`, `:261`, `:980` | MINOR | "800-1200 °C" / "600-900" / "500-1000" / ">500" / "600-900" | Notation drift for the operating window. | One range, stated once. |
| `:233-259` | MINOR | HREE table starts with Eu | Glossary :109 defines HREE as Gd-Lu + Y; ch. 7 puts Sm in LREE and Eu in HREE. | Match glossary. |
| `:41`, `:45` | MINOR | `MₓOᵧ + γX₂ → xMX₂ᵧ/ₓ + γ/2 O₂` | Balances, but uses Greek γ as the coefficient for a subscript written y; unreadable. | `M_xO_y + yX_2 → xMX_{2y/x} + (y/2)O_2` in math mode. |

### Citations that cannot support their sentence (MAJOR, as a class)

Each of these is a real bib entry attached to a claim its title/venue cannot contain. Given the provenance note, these look like keys swapped in during DOI repair. Line, key, and what the paper actually is:

| Line | Key | Paper is actually | Attached to |
|---|---|---|---|
| :97 | @borra2016recovery | red-mud REE review | Boudouard CO₂→CO crossover |
| :104, :752 | @roine2019hsc | HSC software manual | CeO₂ phase-stability finding; TiCl₄ purification |
| :108 | @yang2017ree | NdFeB recycling review | carbochlorination Ea values |
| :244 | @long2010principal | USGS deposit report | Ce applications (acceptable) |
| :261 | @jyothi2020rare, @kumari2015process | secondary-resources review; monazite review | "spontaneous above 500 °C"; Eu(II) chloride |
| :266 | @habashi2013extractive | textbook | Gaviría & Bohé Y₂O₃ results (the real key @gavira2010carbochlorination is at :124) |
| :281 | @chi2008weathered | book on weathered-crust (IAC) ores | bastnäsite 70 wt% REO |
| :283 | @zhang2015occurrence | REE in coal | SiCl₄ defluorination |
| :300 | @battsengel2018recovery | apatite ore | monazite Th 4-12 % |
| :302 | @weng2015detailed | resource assessment (Econ. Geol.) | POCl₃/ThCl₄ volatility |
| :310 | @tsamis2015recovery | EU Parliament e-waste report | monazite carbochlorination "cleanliness" |
| :313, :315 | @kaya2016recovery, @lorenz2023recovery | e-waste; NdFeB chlorination | xenotime REO grade; xenotime economics |
| :322, :332 | @liu2014solvent, @dutta2016global | Cyanex/Alamine SX; global REE review | NdFeB chlorination roasting (also "RECls" typo at :332) |
| :334 | @deng2022rare | Sci. Adv. 2022 FJH+acid | FJH-Cl₂ (should be @tour2025sustainable) |
| :582 | @paulick2017global | exploration boom | technical advantages |
| :614 | @weber2012rare | EPA review | "clean metallurgical technology" |
| :626, :629, :641 | @banda2015separation, @bailey2017sustainability, @peck2015critical | Pr/Nd SX; magnet motors; product design | environmental impacts; economics; policy |
| :675 | @nassar2015criticality | criticality methodology | China TRL 7-8 |
| :686 | @vital2023nechalacho | company web page | scale-up challenges |
| :702, :705, :725 | @doe2022report, @habib2014exploring, @commission2020critical | coal REE report; supply constraints; EU list | Ti industry precedent; equipment list |
| :721 | @iaea2011radiation | NORM guidance | roasting temperature |
| :779, :784 | @usgs2020titanium, @konings2010thermodynamic | Ti commodity summary; f-element thermo | Zr/Hf content; ZrSiO₄ chlorination temp |
| :803 | @yin2024preparation | crude ZrCl₄ prep | "only pyrometallurgical Zr/Hf method at industrial scale" (@chen2025process at :805 fits better) |
| :832 | @nfc2023nuclear | nuclear fuel page | shared infrastructure |
| :859, :877 | @wikipedia2024aluminium | Wikipedia | Oersted 1825; Alcoa process |
| :894 | @namboothiri2017bauxite | bauxite/Al | Mg chlorination "alternative to Dow" |
| :898 vs :912 | @gupta2003chemical / @gaballah1999chlorination | swapped: the TGA MgO study is Gaballah, cited instead for "historical plants" | |

Sections with **zero** citations: One-Step Clean Process (:199-227; presumably @xue2025carbochlorination, cited elsewhere), Fluorination (:365-404: "3-4 kg/h HF", "Carberry spinning-basket reactors", "95.69 %", "99.39 %"), Bromination/Iodination (:406-433: "98.64 % vs 84.59 %", LnI₃(THF)₄ structures — this is Izod/Liddle/Clegg synthesis chemistry and does not belong in a separations book at all), FJH (:436-470), and the MSE section has one citation in 90 lines (:474-567: "90.91 wt% NdF₃", "7-12 A/cm²", "83 %", "1.65 M", "44-69 % GWP reduction", FFC "Developed by Chen et al.").

### Structure / seams
- BLOCKER: two conclusions. `:978` "This comprehensive review demonstrates…" and `:1008` "This comprehensive review of carbohalogenation … reveals…" are the endings of the two merged docx sources, each with its own numbered list and "Future research priorities". The second (:1016-1022) concludes about SX with D2EHPA/PC88A, ionic liquids, DES, bioleaching, scCO₂ — the hydrometallurgy section that the provenance appendix says was *dropped* from this chapter. Orphaned conclusions.
- MAJOR: `:103-124` "Reaction Mechanisms and Kinetics" and `:126-143` "Kinetics and Mechanism" are near-verbatim duplicates. The 700 °C / 12 % C / 60 min / 10 L/min / >93 % parameter set appears three times (:114-122, :204-219, :285-297); SiCl₄ defluorination twice (:150, :283); NdFeB chlorination three times (:154, :324, :332); FJH results twice (see above); "17 elements vs 2" twice (:846, :963).
- MAJOR: `:645-654` technology-comparison table (hydrometallurgy, bioleaching, DES, scCO₂ …) duplicates `src/04-technology-landscape.md:169-182` with different TRLs (FJH 5-6 here vs 3-4 in ch. 4).
- MINOR: `:33-34` "This chapter merges two source documents…" is an editorial note in the body; belongs in `src/93-appendix-provenance.md`.
- MINOR: `:197` "conventional Goldschmidt process" is undefined (Th. Goldschmidt AG's carbochlorination for anhydrous RECl₃), and not in the glossary; `:26-28` "The zirconium industry separates Zr from Hf … by extractive distillation" overgeneralises (Cezus does; the US uses MIBK SX).
- MINOR: filler rows in the element tables (:241 Pm; :253 "Critical element for magnets"; :259 "Highest melting point REE") and the "Feasibility" column is unsourced opinion.

---

## `src/02-ore-to-feed-solution.md`

| Ref | Sev | Quote | Problem | Fix |
|---|---|---|---|---|
| `src/02-ore-to-feed-solution.md:36` | MAJOR | "Monazite … Enriched in middle REEs and heavy REEs" | Monazite is LREE-enriched (Ce, La, Nd); ch. 5 :45 says "light and middle". Wrong in the introductory chapter. | "Enriched in light REEs, with more Nd/Sm than bastnäsite". |
| `:98` | MINOR | `Clay-REE³⁺ + (NH₄)₂SO₄ → REE₂(SO₄)₃ + NH₄⁺-Clay` | Unbalanced (1 REE → 2). | Use the ch. 5 :641 form. |
| `:125` vs ch. 5 :1494; `:120` vs ch. 5 :1501; `:56` vs `:68` | MAJOR | "Target: 0.1-1.0 M"; "extraction pH (typically 0.5-4.0)"; "1-2 M" vs "0.5-2.0 M" | The feed specification handed to Part III differs between ch. 2 and ch. 5, and within ch. 2. | Pick one spec, state it in ch. 5 "The Feed Handed to Solvent Extraction", and quote it here. |
| `:30` | MINOR | "REE·FCO₃" | Three notations across the book: REE·FCO₃ (ch. 2, 5), REFCO₃/(Ce,La)(CO₃)F (ch. 7), (Ce,La)CO₃F (glossary). | Standardise on the glossary form. |
| `:45` | MINOR | "Recent work by [@han2024efficient] focuses on this feedstock" | Group-internal aside in a general intro. | Delete. |
| `:109` | MINOR | "Sulfate can precipitate with some extractants" | Vague and unsupported. | Say what is meant (Ca/REE double sulfates; low D in sulfate media) or delete. |
| `:116` | MINOR | "Fe³⁺ removal … pH 3-4" | ch. 5 :962 "3.5-4.5", :1065 "pH 4". | Harmonise. |

No conflict with ch. 5 beyond the numbers above; the chapter is otherwise a fair condensation.

---

## `src/90-glossary.md`

Well written; the problem is coverage. Terms used in Part II with no entry (grep count 0 in the glossary): pregnant leach solution / PLS, heap leaching, in-situ leaching, shrinking core model, digestion (only inside "cracking"), calcination, gangue, rougher/scavenger/cleaner, HGMS, oxychloride, oxyfluoride, chemical vapor transport, extractive distillation, Kroll process, Goldschmidt process, anode effect, molten salt electrolysis / electrowinning, FFC Cambridge, HMTA, Pourbaix / Eh-pH diagram, simulated moving bed, kaolinite/halloysite/regolith (regolith appears only inside the IAC entry), Alamine 336 / Primene (extractants named in ch. 5 but only D2EHPA/PC88A/Cyanex/TBP in the "extractant" entry), TRL, ammonium bifluoride, oxalate precipitation. Also `:65` defines "cracking", a word ch. 5 never uses (it says decomposition/digestion), and `:109`/`:165` HREE/LREE boundaries disagree with ch. 7's tables.

---

## GAPS WORTH FILING AS ISSUES

1. **Balance and correct every reaction equation in Part II.** Ch. 5 :251, :279, :299, :302, :319, :787, :788, :1019; ch. 7 :41/:45 (notation), :86, :515-517; ch. 2 :98. Write Th chemistry separately from REE (Th(IV)). Put equations in MyST math rather than indented code so they can be checked mechanically. Fix the two pandoc `~a~` subscripts at ch. 5 :1176/:1250.

2. **Rewrite the Mountain Pass and monazite industrial descriptions from primary sources.** Ch. 5 currently gives Mountain Pass as a 70 wt% (or 4 M) H₂SO₄ leach with "evaporate H₂SO₄" conversion; the plant was roast + HCl. Monazite NaOH digestion is given as 300-400 °C, 140-200 °C autogenous, and 140-150 °C autoclave in three places. One authoritative paragraph per process (Gupta & Krishnamurthy; @castor2006rare) owned by ch. 5, cross-referenced from ch. 2 and ch. 7.

3. **Add an LnCl₃/LnF₃ property table and one real flowsheet figure.** Ch. 7's intro promises a volatility argument and never gives melting/boiling points; a table of LnCl₃ mp/bp (and the impurity chlorides FeCl₃, AlCl₃, SiCl₄, POCl₃, ThCl₄, ZrCl₄, TiCl₄) would make the actual selectivity of carbochlorination obvious. Ch. 5's three ASCII flowsheets (:1042-1170) should become one drawn figure (bastnäsite / monazite / IAC in parallel) with a mass balance, replacing the waste table at :1280-1286 whose "20-50 t ore per t REO" is wrong by >10×.

4. **Deduplicate ch. 7 and remove the double conclusion.** Merge :103-143 into one kinetics section; keep one copy of the 700 °C parameter set, the SiCl₄ story, the NdFeB chlorination story, and the FJH numbers; delete the second conclusions block (:1008-1044) whose subject matter is not in the chapter; move the :645-654 TRL table to ch. 4 and reconcile TRLs. Target roughly 5,000 words.

5. **Citation-support audit of ch. 7 and ch. 5.** ~30 citations in ch. 7 (table above) and 5 in ch. 5 (@chen2023various, @zhou2024gravity, @stojkovic2024recovery, @ni2023sustainable, @xiao2015leaching-for-(NH₄)₂SO₄) are attached to sentences the cited work cannot support; the FJH-Cl₂ results are cited to @deng2022rare here and @tour2025sustainable in ch. 12; @huang2002rare's author list should be checked. Rule for the fix: each citation must be to a paper that contains the claim, or the claim goes.

6. **Source or cut the uncited numerical sections.** Ch. 7 Fluorination (:365-404), Bromination/Iodination (:406-433, and consider deleting as out of scope), FJH (:436-470), MSE (:474-567), One-Step Clean Process (:199-227); ch. 5 flowsheet recoveries/energies (:1042-1170), energy/CO₂ tables (:1337-1353), cost table (:1439-1449), and the bioleaching table (:892-896) whose monazite recoveries are an order of magnitude above what @brisson2015bioleaching reports.

7. **Reconcile the cross-chapter numbers for the SX feed and IAC.** Feed REE concentration (0.1-1.0 vs 0.5-2.0 M), extraction pH (0.5-4.0 vs 2.5-4.0), Fe removal pH (3-4 / 3.5-4.5 / 4), IAC share of HREE supply (50 % vs >90 %), the halloysite/kaolinite direction (ch. 6 :51), Alamine 336 primary vs tertiary. Then cut ch. 5's IAC section (:616-797) to leach chemistry plus a pointer to ch. 6, and move bioleaching/urban mining/LCA to chs. 11/16/17.

8. **Restore the Moab sources and strip memo residue from ch. 6; extend the glossary.** Ch. 6 :132's `[^1][^2]` have no definitions — restore the DOE UMTRA citations or round the numbers. Remove "the Sobri paper" / "this report" framing (:26, :74-76, :146), the ch. 5 :1040 "chemistry fundamentals review" pointer, and the ch. 7 :33-34 merge note. Add the ~28 missing glossary terms listed above and align the HREE/LREE boundary between glossary and ch. 7.