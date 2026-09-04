---
title: Pyrometallurgical and Halogenation Routes
---

(pyrometallurgical-and-halogenation-routes)=
# Pyrometallurgical and Halogenation Routes

Everything else in this book dissolves the ore. Halogenation does not. Instead
of leaching a mineral into an aqueous liquor and then separating ions in
solution, {index}`carbochlorination` converts a mineral concentrate into a bed of
anhydrous chlorides in the solid state, and lets the volatility difference
between those chlorides do the sorting. It is a different physics of separation
— vapour pressure rather than {index}`distribution ratio` — and it therefore has a
different set of strengths and a different set of problems.

It is worth being precise about which way the separation runs, because the
obvious guess is wrong. The rare earth trichlorides are not the volatile
products. They melt between roughly 580 and 930 °C and do not reach one
atmosphere of vapour pressure until well above 1,500 °C [@seifert2005melting;
@brunetti2000vaporization]. What leaves the reactor is everything else: the
silicon, phosphorus, iron, aluminium, titanium, zirconium and thorium in the
concentrate all form chlorides that boil or sublime below about 340 °C, with
ThCl₄ the only laggard at 921 °C. Run a chlorinator at 600–900 °C and the
impurities walk out as vapour while the rare earths stay behind as a molten or
solid chloride cake that dissolves in plain water. That asymmetry — the
impurities leave, the rare earths stay — is what makes chloride volatility a
separation at all.

| Chloride | Melting point (°C) | Boiling or sublimation point (°C) | Fate at 600–900 °C |
|----|----|----|----|
| SiCl₄ | −69 | 58 (b) | vapour |
| POCl₃ | 1 | 106 (b) | vapour |
| TiCl₄ | −24 | 136 (b) | vapour |
| AlCl₃ | 193 (under pressure) | 181 (s) | vapour |
| FeCl₃ | 308 | 316 (b, dec.) | vapour |
| ZrCl₄ | 437 (under pressure) | 331 (s) | vapour |
| ThCl₄ | 770 | 921 (b) | volatile only at the top of the window |
| CaCl₂ | 775 | 1,935 (b) | stays in the cake |
| LnCl₃ (La–Lu, Y) | ≈580 (Tb) to 930 (Lu) | ≳1,550 (b, est.) | stays in the cake |

: Melting and boiling (b) or sublimation (s) points of the chlorides that matter
in a rare earth chlorinator. Impurity- and alkaline-earth-chloride values are
from the CRC Handbook [@haynes2016crc]. The LnCl₃ melting range is from Seifert's
critical review, which also documents the minimum near Tb [@seifert2005melting];
the boiling estimate is extrapolated from the liquid-LaCl₃ vapour-pressure
equation of Brunetti and co-workers, log(p/kPa) = 9.65 − 13,989 K/T, which
reaches 1 atm at about 1,830 K [@brunetti2000vaporization]. Extrapolation that
far beyond the measured range (1,137–1,188 K) is uncertain by well over 100 K;
the point is the order of magnitude of the gap, not the digits.

The table also shows why {index}`carbochlorination` is a bulk-impurity separation
rather than an inter-lanthanide one. Nothing in a 600–900 °C chlorinator
distinguishes NdCl₃ from PrCl₃; their vapour pressures are as close together as
their distribution ratios. Separating rare earths from each other by volatility
requires a second trick — the AlCl₃ vapour complexes described below, which have
reached about 80 % purity for La and Ce — or handing the water-soluble chloride
cake to the solvent extraction plant of [](#solvent-extraction-fundamentals).

The strengths of the route are real: no aqueous waste stream, no solvent
inventory, no acid consumption, and a tolerance for refractory minerals that
resist acid attack. The problems are equally real: chlorine gas at temperature,
materials of construction that survive it, and a product that still needs
conventional separation if individual elements are the goal.

What makes this chapter worth reading even if halogenation never separates a
single rare earth is the industrial precedent. Titanium, zirconium, aluminium,
magnesium, and niobium-tantalum are all produced or purified at large scale by
exactly this chemistry today. The zirconium industry separates Zr from Hf — a
pair at least as similar as any lanthanide pair — by extractive distillation of
their chlorides in a molten salt. Those industries have already solved most of
the materials and containment problems that a rare earth carbochlorination plant
would face, and the second half of this chapter reads them for transferable
lessons.

## The Halogenation Family

### Fundamental Thermodynamics of Halogenation
Halogenation of metal oxides to form metal halides is governed by fundamental thermodynamic principles. The general reaction for direct halogenation is:

> $\mathrm{M}_x\mathrm{O}_y + y\,\mathrm{X}_2 \rightarrow x\,\mathrm{MX}_{2y/x} + \tfrac{y}{2}\,\mathrm{O}_2$

Whether that reaction needs help depends on the oxide. For the sesquioxides it is
already downhill: from the standard free energies of formation of La₂O₃ and
LaCl₃, La₂O₃ + 3 Cl₂ → 2 LaCl₃ + 1.5 O₂ has ΔG° ≈ −290 kJ at 298 K and stays
negative to about 1,000 K. It is CeO₂ — tetravalent, and the most abundant rare
earth in bastnäsite — together with the gangue oxides TiO₂, ZrO₂ and Al₂O₃ for
which direct chlorination is uphill at accessible temperatures. Carbon fixes all
of them at once. It converts the liberated oxygen to CO or CO₂, which removes the
product-side penalty, and for the rare earths it also drives the reaction past
the oxychloride intermediate that otherwise stalls conversion
[@pomiro2021panoramic]:

> $\mathrm{M}_x\mathrm{O}_y + y\,\mathrm{C} + y\,\mathrm{X}_2 \rightarrow x\,\mathrm{MX}_{2y/x} + y\,\mathrm{CO}$ (carbohalogenation)

The thermodynamic favorability of carbohalogenation varies with the halogen used. The bond energies and electronegativity of the halogens influence reaction thermodynamics:

| **Halogen** | **Electronegativity** | **X-X Bond Energy (kJ/mol)** | **M-X Bond Strength** | **Typical Temp (°C)** | **Industrial Status** |
|----|----|----|----|----|----|
| Fluorine (F) | 3.98 | 155 | Very Strong | 500-700 | Commercial (metal production) |
| Chlorine (Cl) | 3.16 | 243 | Strong | 600-900 | Commercial (Ti, Zr, REE pilot) |
| Bromine (Br) | 2.96 | 193 | Moderate | 400-700 | Laboratory scale |
| Iodine (I) | 2.66 | 151 | Weak | 250-500 | Laboratory scale |

### Comparison of Halogens (F, Cl, Br, I)
Each halogen offers distinct advantages and limitations for rare earth processing:

> Fluorine/HF:

Fluorination produces rare earth fluorides essential for {index}`molten salt electrolysis`. The strong RE-F bond provides high thermodynamic stability. However, fluorine and HF are highly corrosive and toxic, requiring specialized equipment and safety protocols. Anhydrous HF (AHF) is particularly hazardous, necessitating custom AHF-safe laboratories.

> Chlorine:

Carbochlorination is the most industrially mature halogenation process for REEs. Chlorine is less reactive than fluorine, allowing easier handling, and rare earth chlorides are highly water-soluble, enabling simple downstream processing. The process operates at moderate temperatures (600-900°C) and has been demonstrated at pilot and commercial scale in China.

> Bromine and iodine:

Neither halogen has a separations role. Lanthanide bromides and iodides are made
by direct combination of the metal with the halogen, or from ammonium halides,
and are used as precursors in organometallic and molten-salt chemistry rather
than as a route out of an ore. They are also strongly hygroscopic and hydrolyse
readily, which makes anhydrous handling harder than for the chlorides with no
compensating selectivity. The rest of this chapter is therefore about chlorine,
with a section on fluorine because rare earth fluorides are the feed to molten
salt electrolysis.

## Carbochlorination Chemistry

### Fundamental Chemistry
The carbochlorination process converts metal oxides to chlorides through the synergistic action of carbon (reducing agent) and chlorine gas (chlorinating agent) at elevated temperatures [@anderson2015investigation]. Carbon is what makes direct {index}`chlorination` of the more refractory oxides — CeO₂, TiO₂, ZrO₂, Al₂O₃ — thermodynamically accessible, and what carries the rare earth sesquioxides past their oxychloride intermediates to complete conversion [@pomiro2021panoramic].

For rare earth oxides, the primary reactions are:

- RE₂O₃ + 3C + 3Cl₂ → 2RECl₃ + 3CO (at higher temperatures)

- RE₂O₃ + 1.5C + 3Cl₂ → 2RECl₃ + 1.5CO₂ (at lower temperatures)

- 2CeO₂ + 4C + 3Cl₂ → 2CeCl₃ + 4CO (for tetravalent {index}`cerium`; the extra carbon supplies the electrons for Ce(IV) → Ce(III))

Research has shown that direct contact between metal oxides and carbon is not necessary for effective chlorination [@gavira2010carbochlorination]. The reaction proceeds through gaseous intermediates, with carbon providing catalytic activity sites for the formation of highly reactive species. Proposed intermediates include phosgene (COCl₂), monatomic chlorine, and carbon tetrachloride (CCl₄) [@murase1995recovery].

### Thermodynamic Considerations
Thermodynamic analysis using Gibbs free energy calculations demonstrates that carbochlorination of rare earth oxides is spontaneous (ΔG \< 0) over a wide temperature range of 500-1000°C [@xue2025carbochlorination; @pomiro2021panoramic]. The Gibbs free energy becomes increasingly negative with rising temperature, indicating enhanced thermodynamic driving force.

Key thermodynamic findings include:

- Operating temperatures of 600-900°C are typical. This window is set by kinetics and by the melting point of the chloride product, not by any comparison with roasting: oxidative roasting of bastnäsite runs at 500-700 °C and sulfuric acid baking at 200-500 °C (see [](#hydrometallurgical-leaching)), so carbochlorination is not the lower-temperature option.

- Above about 700°C the Boudouard equilibrium C + CO₂ ⇌ 2 CO moves to the right, so the primary carbon product switches from CO₂ to CO. This doubles the carbon demand per mole of oxygen removed but makes the chlorination itself more favourable.

- Phase stability diagrams (RE-O-Cl systems) reveal element-specific reaction pathways that influence process design [@xue2025carbochlorination; @pomiro2021panoramic].

- Pelletizing the concentrate with the reductant before chlorination improves gas-solid contact and prevents the fine feed from being entrained out of the bed [@xia2024experimental].

### Reaction Mechanisms and Kinetics
The carbochlorination reaction proceeds through distinct mechanisms depending on the specific rare earth element. For cerium oxide (CeO₂), phase stability diagrams show a direct boundary between the CeO₂ and CeCl₃ phases, indicating that the oxide can convert directly to the chloride without intermediate phases; {index}`neodymium` oxide (Nd₂O₃) must instead pass through an intermediate oxychloride (NdOCl) before complete conversion to NdCl₃ [@anderson2015investigation]. The difference matters for process design, because the oxychloride is the slow step and it is more important in neodymium processing than in cerium processing. {index}`Europium <europium>` is a third case again: its carbochlorination proceeds in resolvable stages through EuOCl and can terminate at the divalent chloride EuCl₂ under reducing conditions [@pomiro2014study].

For {index}`yttrium` oxide (Y₂O₃), the reaction mechanism involves the initial formation of YOCl through nucleation and growth. At temperatures above 715°C, the final product is liquid YCl₃, which can evaporate from the reaction zone [@gavira2010carbochlorination].

Kinetics for a real bastnäsite feed, measured between 600 and 800 °C, resolve
two successive stages with apparent activation energies of 12.54 kJ/mol and
11.22 kJ/mol; the authors assign both stages to chemical-reaction control
[@xue2025carbochlorination]. That assignment deserves a caution, because
activation energies of 10-15 kJ/mol are in the range normally taken as
diagnostic of diffusion control — the same criterion this book applies in
[](#hydrometallurgical-leaching). Either the rate-limiting step is gas-phase
transport into the pellet rather than surface reaction, or the two-stage fit is
absorbing a change in reactive surface area. It is a discrepancy in the primary
literature, not a settled result, and any scale-up model should treat the
control regime as an open question.

Under the same study's optimum — 800 °C, 60 min, 10 % fluorine-fixing agent and
10 L/min of chlorine at laboratory scale — the chlorination rates reached 96 %
for the rare earths and 98-99 % for the Ca, Ba and Fe in the concentrate
[@xue2025carbochlorination].

Mechanistically the reaction runs through the gas phase. Direct contact between oxide and carbon particles is not required [@gavira2010carbochlorination]; the carbon generates reactive intermediates — phosgene (COCl₂), monatomic chlorine, and carbon tetrachloride (CCl₄) have all been proposed — which then attack the oxide [@murase1995recovery].

### Industrial Applications
Carbochlorination has been demonstrated for multiple feedstocks. Bastnäsite \[(Ce,La)(CO₃)F\] requires special consideration of its fluorine content, and silicon tetrachloride (SiCl₄) is used as a defluorinating agent to prevent the loss of fluorine as volatile rare earth fluorides [@huang2002rare]. End-of-life {index}`NdFeB` magnets are handled by chlorination roasting followed by water leaching, exploiting the fact that the rare earths chlorinate while iron can be held as the oxide [@hua2014selective]. Both are treated in detail below.

### Stepwise Carbochlorination-Chemical Vapor Transport (SC-CVT)
A breakthrough process combining carbochlorination with chemical vapor transport (CVT) enables both extraction and separation of individual REEs [@huang2002rare].

**Process Components:**

- **Carbon**: Reducing agent
- **Cl₂ gas**: Primary chlorinating agent
- **SiCl₄**: Defluorination agent for fluorocarbonate minerals
- **AlCl₃**: Vapor complex former for transport

**Mechanism:**

REE chlorides form vapor complexes with aluminum chloride: RAlₙCl₃₊₃ₙ (where R = rare earth). These complexes transport along temperature gradients, with selective condensation enabling separation:

| Species       | Condensation Temperature |
|---------------|--------------------------|
| REE chlorides | 1220-730 K               |
| AlCl₃, FeCl₃  | \< 400 K                 |

**Performance:**

- **LaCl₃ and CeCl₃ purity**: \~80% achieved through selective condensation
- **{index}`Thorium <thorium>` removal**: Complete (critical for {index}`monazite` processing)
- **REE recovery**: 92-99 mol% with SiCl₄ addition (vs. 56-88% without)

### Processing of Mixed Bastnäsite-Monazite Concentrates
The SC-CVT process is particularly effective for mixed bastnäsite (REFCO₃) and monazite (REPO₄) concentrates:

**Optimized Conditions:**

| Parameter | Value |
| ----------- | ------- |
| Chlorination temperature | 500-800°C |
| Atmosphere | Cl₂ + SiCl₄ |
| REE chloride yield | 92-99 mol% |

**Two-Stage CVT Separation:**

1.  **Stage 1** (800°C, 0.5 h): Cl₂ + SiCl₄ + AlCl₃ atmosphere
2.  **Stage 2** (1000°C, 6 h): Cl₂ + AlCl₃ atmosphere with temperature gradients

This approach operates at temperatures as low as 500°C, against 1000-1200°C for the older Goldschmidt carbochlorination route to anhydrous RECl₃ [@huang2002rare].

### One-Step Carbochlorination-Washing
The most recent line of work collapses chlorination and product recovery into a
single operation: chlorinate the concentrate in a chlorine-rich atmosphere, then
wash the cake with water to take the rare earth chlorides into solution
[@xue2025onestep; @xue2026clean]. The claim on the process is not a higher
recovery — the chlorination rates are the 96 % rare earth and 98-99 % Ca, Ba and
Fe figures quoted above — but the absence of an acidic effluent. There is no
sulfuric acid bake and no caustic digestion, the only liquid input is wash water,
and the off-gas (excess Cl₂, CO/CO₂, and the volatile impurity chlorides) is
recycled or condensed rather than scrubbed into a waste stream. Its authors
describe this as "zero discharge" of acidic wastewater [@xue2026clean].

Two cautions attach. First, "zero discharge" is a claim about the acid circuit,
not about the whole flowsheet: the volatile chlorides that leave the reactor —
FeCl₃, AlCl₃, SiCl₄, POCl₃ and any ThCl₄ — are still a waste or by-product
stream that has to be condensed, separated and sold or disposed of, and the
thorium fraction is radioactive. Second, the process has been demonstrated on
laboratory quantities of concentrate; the reduced equipment cost claimed for it
rests on a flowsheet comparison, not on an operating plant.

## Application Across the Rare Earth Series

Carbochlorination has been investigated for various rare earth elements with thermodynamic and experimental evidence supporting its applicability across the entire lanthanide series plus {index}`scandium` and yttrium.

### Light Rare Earth Elements
The light rare earth elements (LREEs) comprise {index}`lanthanum` (La), cerium (Ce), {index}`praseodymium` (Pr), neodymium (Nd), promethium (Pm), and {index}`samarium` (Sm). These elements are more abundant in the principal REE minerals bastnäsite and monazite, making them the primary targets for industrial carbochlorination [@gupta1992extractive].

| **Element** | **Oxide** | **Chloride** | **Carbochlorination Feasibility** |
|----|----|----|----|
| Lanthanum (La) | La₂O₃ | LaCl₃ | Excellent - Demonstrated at lab and pilot scale |
| Cerium (Ce) | CeO₂ | CeCl₃ | Excellent - Direct conversion, no intermediate phases |
| Praseodymium (Pr) | Pr₆O₁₁ | PrCl₃ | Good - Thermodynamically favorable |
| Neodymium (Nd) | Nd₂O₃ | NdCl₃ | Excellent - Proceeds via NdOCl intermediate |
| Promethium (Pm) | Pm₂O₃ | PmCl₃ | Theoretical - Radioactive, limited studies |
| Samarium (Sm) | Sm₂O₃ | SmCl₃ | Good - Follows LREE pattern |

Cerium and neodymium have received the most research attention due to their industrial importance. Cerium is the most abundant REE and is used in catalysts and glass polishing, while neodymium is critical for NdFeB permanent magnets [@long2010principal]. Studies have confirmed that both oxides can be efficiently converted to anhydrous chlorides via carbochlorination at 700°C with \>93% conversion rates [@anderson2015investigation].

### Heavy Rare Earth Elements
The heavy rare earth elements (HREEs) include {index}`europium` (Eu), gadolinium (Gd), {index}`terbium` (Tb), {index}`dysprosium` (Dy), holmium (Ho), erbium (Er), thulium (Tm), ytterbium (Yb), and lutetium (Lu). These elements are generally less abundant but often more valuable than LREEs [@tunsu2016hydrometallurgical].

| **Element** | **Oxide** | **Chloride** | **Carbochlorination Feasibility** |
|----|----|----|----|
| Europium (Eu) | Eu₂O₃ | EuCl₃/EuCl₂ | Good - May reduce to Eu(II) |
| Gadolinium (Gd) | Gd₂O₃ | GdCl₃ | Good - Follows lanthanide pattern |
| Terbium (Tb) | Tb₄O₇ | TbCl₃ | Good - Critical element for magnets |
| Dysprosium (Dy) | Dy₂O₃ | DyCl₃ | Good - Important for high-temp magnets |
| Holmium (Ho) | Ho₂O₃ | HoCl₃ | Good - Limited specific studies |
| Erbium (Er) | Er₂O₃ | ErCl₃ | Good - Thermodynamically favorable |
| Thulium (Tm) | Tm₂O₃ | TmCl₃ | Theoretical - Rarest stable lanthanide |
| Ytterbium (Yb) | Yb₂O₃ | YbCl₃/YbCl₂ | Good - May reduce to Yb(II) |
| Lutetium (Lu) | Lu₂O₃ | LuCl₃ | Good - Highest melting point REE |

The HREEs follow similar carbochlorination chemistry to the LREEs, with thermodynamic calculations indicating spontaneous reaction over the 500-1000 °C window [@xue2025carbochlorination]. Europium and ytterbium are the special cases: both can be reduced to the divalent chlorides (EuCl₂, YbCl₂) under strongly reducing conditions, and the europium reaction has been resolved stage by stage [@pomiro2014study]. Note that the table above lists europium with the heavies for continuity with the source literature; the boundary used in this book's glossary places Eu on the light side of Gd.

### Scandium and Yttrium
Scandium (Sc) and yttrium (Y) are not lanthanides, but both are counted among the rare earths because their chemistry resembles that of the lanthanides and they occur alongside them in the ore minerals; see the [](#glossary) entry.

Yttrium oxide (Y₂O₃) carbochlorination has been studied in detail by thermogravimetry [@gavira2010carbochlorination]:

- The reaction proceeds via nucleation and growth of YOCl intermediate

- At temperatures above 715°C, the final product is liquid YCl₃

- Evaporation of YCl₃ is observed in thermogravimetric analysis at high temperatures

- Complete conversion to anhydrous YCl₃ is achievable under optimized conditions

Scandium has not been studied for carbochlorination in comparable detail. Its chemical similarity to yttrium makes similar behaviour plausible, but that is an expectation, not a measurement.

## Primary Ore Processing

### Bastnäsite Processing
Bastnäsite \[(Ce,La)(CO₃)F\] is a fluorocarbonate mineral, dominated by the light rare earths; the pure end-member is about 75 wt% rare earth oxide by stoichiometry and commercial concentrates run lower. The {index}`Bayan Obo` deposit in China and the {index}`Mountain Pass` deposit in the United States are the world's largest bastnäsite resources [@castor2006rare].

Carbochlorination of bastnäsite requires special consideration of the fluorine content. Wang and co-workers developed the carbochlorination route that uses carbon as the reducing agent, chlorine as the chlorinating agent, and silicon tetrachloride (SiCl₄) as a defluorinating agent [@huang2002rare]. Fixing the fluorine as SiF₄ stops it leaving as rare earth fluoride and makes it recoverable as a by-product.

Operating parameters for bastnäsite carbochlorination are given above under
Reaction Mechanisms and Kinetics; the chlorine feed is typically run at roughly
twice the stoichiometric requirement to keep the bed in a chlorine-rich regime
[@suli2017rare].


### Monazite Processing
Monazite \[(Ce,La,Nd,Th)PO₄\] is a phosphate mineral containing 55-65% REO along with several per cent thorium [@kumari2015process]. The radioactive thorium content presents unique processing challenges that must be addressed regardless of extraction method.

Carbochlorination of monazite offers advantages for thorium management. The phosphorus content can be converted to volatile POCl₃, which can be separately recovered. Thorium chloride (ThCl₄) boils at 921 °C, far below the rare earth chlorides, and in stepwise carbochlorination with chemical vapour transport thorium removal from a mixed bastnäsite-monazite concentrate was complete [@huang2002rare].

Conventional monazite processing goes by either sulfuric acid digestion or caustic decomposition; both are described, with their operating conditions, in [](#hydrometallurgical-leaching), which owns those numbers for this book.

Carbochlorination may provide a cleaner alternative by avoiding the generation of large volumes of acidic or alkaline waste streams while concentrating thorium into a small volatile stream rather than dispersing it. The thorium still has to be managed; see [](#thorium-management).

### Xenotime Processing
{index}`Xenotime <xenotime>` \[YPO₄\] is the primary mineral source for heavy rare earths and yttrium. The mineral contains roughly 55-65 % REO with a composition heavily weighted toward HREEs and Y [@castor2006rare].

The carbochlorination of xenotime follows similar principles to monazite, with the phosphate matrix being converted to volatile chloride products while the REE chlorides are retained. Given the higher value of HREEs, carbochlorination might offer economic advantages through reduced reagent costs and simplified product recovery, but no study in the open literature has costed it for xenotime.

## Recycling Applications

### NdFeB Magnet Recycling
NdFeB permanent magnets represent the largest application of neodymium and contain significant amounts of praseodymium, dysprosium, and terbium. End-of-life magnets from electric vehicles, wind turbines, and consumer electronics offer an important secondary resource [@onal2015recycling].

Multiple chlorination approaches have been investigated for NdFeB recycling [@yang2017ree]:

- Chlorination roasting at 300-500°C with subsequent water leaching

- High-temperature chlorination at 1173-1273 K with distillation separation

- Solid-state chlorination with NH₄Cl, FeCl₂, or MgCl₂-KCl

- {index}`Flash Joule heating <flash Joule heating>` combined with chlorination (FJH-Cl₂)

Chlorination roasting runs cooler and faster than oxidation roasting, and the selective chlorination of the rare earths to RECl₃ separates them from iron, which is held as the oxide under appropriate conditions [@hua2014selective]. Chlorination followed by distillation of the rare earth chlorides has also been demonstrated on magnet scrap [@lorenz2023recovery]. The flash Joule heating variant is the newest of these and is treated separately in [](#flash-joule-heating-with-chlorination).

### Other Secondary Sources
Carbochlorination has also been investigated for REE recovery from [@binnemans2017solvometallurgy]:

- Fluorescent lamp phosphors (primarily Y, Eu, Tb)

- Nickel-metal hydride batteries (La, Ce, Nd, Pr)

- Catalytic converters (La, Ce)

- {index}`Coal fly ash <coal fly ash>` and coal by-products

- Electronic waste (various REEs)

- Mining tailings and processing residues

The carbochlorination approach suits secondary sources with complex compositions, because it does not require a high-grade feedstock and tolerates wide variation in composition [@tanaka2013recycling]. A cascade condensation train downstream of the reactor sorts the resulting chlorides by boiling point, which is where the volatility spread in the table at the head of this chapter earns its keep.

## Fluorination

### Direct Fluorination with HF
The conversion of rare earth oxides to fluorides is essential for molten salt electrolysis metal production. Direct fluorination with anhydrous hydrogen fluoride (AHF) is the industrial standard:

> RE₂O₃ + 6HF → 2REF₃ + 3H₂O

The reaction is run dry, on the oxide or on a carbonate precursor, at a few
hundred degrees; conversion is essentially quantitative because the RE-F bond is
so much stronger than RE-O. The engineering problem is not the chemistry but the
reagent. Anhydrous HF is acutely toxic, attacks glass and most metals, and
demands a dedicated facility, which is why the alternatives below exist. We give
no operating parameters here: the process conditions circulating in review
articles for this step could not be traced to a primary source.

### Solid-State Fluorination (NH₄HF₂, ZnF₂, NaBF₄)
Solid fluorinating agents avoid the anhydrous-HF handling problem by carrying
their fluorine in a condensed phase that decomposes only on heating.

Ammonium bifluoride, NH₄HF₂, is the mildest of them. It is preferred over NH₄F
because it is not hygroscopic, and it converts rare earth oxides to anhydrous
fluorides at modest temperature; a finishing step under argon with a little HF
is used when residual oxygen must be driven out. It has been applied to both
Nd₂O₃ and Y₂O₃.

Zinc fluoride is the more interesting reagent for recycling, because its
thermodynamics are favourable against the oxides present in oxidised NdFeB
swarf. Roasting the waste with a stoichiometric excess of ZnF₂ at 850 °C for
90 minutes fluorinates about 96 % of the rare earth content, and the volatile
zinc species leave the residue; AlF₃ and FeF₃ behave similarly
[@liu2024mechanism]. Sodium tetrafluoroborate, NaBF₄, has been studied by the
same group as a higher fluorine-density alternative on the same feed
[@liu2025mechanism]. The reported fluorination and purity figures for the NaBF₄
route could not be traced beyond the abstract and are omitted here.

The general point is that all three reagents convert the rare earth fraction
without touching the {index}`iron` — iron fluoride is not the stable product at
these conditions — so the fluorination is itself a separation step, not merely a
compound conversion.

### Halide Exchange with Magnesium Salts
A related route replaces the fluorinating solid with a molten halide bath. An
exchange reaction between a magnesium halide melt and NdFeB scrap converts the
neodymium to NdF₃ or NdCl₃ while the iron stays metallic. Run in a LiF-NaF-MgF₂
melt at 1,073 K, the reaction extracted 98.6 % of the neodymium; the
corresponding LiCl-NaCl-MgCl₂ melt at 873 K reached 84.6 % [@heo2025extraction].
The fluoride system wins because MgF₂ is the weaker fluoride donor of the two
relative to NdF₃ — the same free-energy ordering that makes fluorination
selective in the solid-state routes above.

### Fluoride Molten Salt Systems
Fluoride molten salts serve two purposes at once: they are the medium in which
oxide-to-fluoride conversion happens, and they are the electrolyte for the metal
reduction that follows. Fluoride additives including AlF₃, ZnF₂ and FeF₃ convert
rare earth oxides to fluorides in situ, so a single vessel can take oxide in and
give metal out.

Fluoride electrolytes give higher current efficiency than chloride electrolytes,
but they cost more energy because their decomposition potentials are higher, and
they emit perfluorocarbons when the cell goes into anode effect. That trade-off
is quantified in [](#molten-salt-electrolysis).

(flash-joule-heating-with-chlorination)=
## Flash Joule Heating with Chlorination

Flash Joule heating passes a large capacitive discharge through a conductive
charge, raising it to thousands of degrees in milliseconds and cooling it almost
as fast. Combined with chlorination (FJH-Cl₂), it has been applied to
end-of-life magnets and to other rare-earth-bearing waste
[@xu2025sustainable].

The separation rests on a temperature window rather than on a reagent. Iron and
cobalt chlorinate and volatilise as FeCl₃ and CoCl₂ around 1,000 °C, while the
rare earth oxides do not react appreciably with chlorine until well above that.
Holding the charge in between, for the fraction of a second the pulse lasts,
strips the transition metals and leaves a rare earth oxide residue reported at
better than 90 % purity and better than 90 % recovery. Against a conventional
hydrometallurgical baseline the authors report roughly 87 % lower energy use,
84 % lower greenhouse gas emissions and 54 % lower operating cost, with water
and acid consumption eliminated; the volatilised chlorides are recovered as
saleable CoCl₂ and FeCl₃ [@xu2025sustainable].

Two cautions belong with those numbers. They are the developers' own
life-cycle and cost comparison against a modelled hydrometallurgical baseline,
not an independent audit, and the demonstrations are bench scale — grams to tens
of grams per pulse. The modular, batch character of the process is genuinely
attractive for distributed electronic-waste processing, where feed volumes are
small and shipping dominates cost, but the scaling behaviour of the electrode
and reactor at tonne-per-day rates has not been shown.

(molten-salt-electrolysis)=
## Molten Salt Electrolysis and Electrowinning

Everything so far in this chapter produces a rare earth *compound*. Turning that
compound into metal is a separate unit operation, and in practice it is
electrolysis in a molten salt. It belongs in this chapter because the choice of
halide made upstream — fluoride or chloride — largely determines what the
electrolysis cell looks like, what it costs to run, and what comes out of its
stack.

### The Two Cell Chemistries

Molten salt electrolysis is the dominant route to rare earth metals and alloys
in China, and the great majority of that capacity is the oxide-fluoride cell
[@yang2021recovery]. Rare earth oxide is dissolved in a molten
{index}`fluoride` electrolyte — an REF₃-LiF melt — and reduced on the cathode
while a consumable carbon anode burns:

> Cathode:  RE³⁺ + 3 e⁻ → RE(metal)
>
> Anode:    2 O²⁻ + C → CO₂ + 4 e⁻
>
> Overall:  2 REO₁.₅ + 3 C → 2 RE + 3 CO₂

The fluorides are the solvent, not the reagent: the reducible species is the
dissolved oxide, and the carbon anode burns to CO/CO₂ exactly as in aluminium
electrolysis. F₂ and CF₄ evolve only when the melt is depleted of oxide and the
cell goes into anode effect. Cells of this type run near 1,050 °C in closed
steel pots under argon, with carbon ring anodes and tungsten or molybdenum
cathodes, and they are the reason light rare earth metal is a commodity rather
than a laboratory curiosity.

The chloride cell is the alternative, and it is a genuinely different machine:

> Cathode:  RE³⁺ + 3 e⁻ → RE(metal)
>
> Anode:    2 Cl⁻ → Cl₂(g) + 2 e⁻
>
> Overall:  2 RECl₃ (in LiCl-KCl eutectic) → 2 RE(metal) + 3 Cl₂(g)

Here the rare earth chloride is the reagent, the anode is inert rather than
consumable, and the anode product is chlorine, which goes back to the
chlorinator at the front of this chapter. Electrolysis of NdCl₃ at 1.65 M in a
45:55 wt % LiCl-KCl eutectic against an RuO₂-coated dimensionally stable anode
has been demonstrated at better than 80 % coulombic efficiency and 2.3 kWh per
kilogram of neodymium, giving metal of better than 97 wt % purity; a life-cycle
assessment of that cell puts its global warming potential at 5 kg CO₂-eq per
kilogram against 9-16 for the conventional oxide-fluoride route, a 44-69 %
reduction [@holcombe2024sustainable]. The eutectic melts below 400 °C, so the
cell runs several hundred degrees cooler than the fluoride pot and can be built
from cheaper materials.

The chloride cell is not free of problems. Chlorine at temperature is corrosive
to everything, RECl₃ salts are hygroscopic enough that moisture ingress
hydrolyses the melt to oxychloride, and the demonstrated cells are laboratory
scale — the 2.3 kWh/kg figure is a cell measurement, not a plant number.

### Why the Fluoride Cell's Emissions Matter

The perfluorocarbons released during anode effect are the strongest argument
against the incumbent process. Using the IPCC's Sixth Assessment values, CF₄ has
a 100-year global warming potential of about 7,400 times that of CO₂, and C₂F₆
over 12,000 times [@ipcc2021physical]. These are not trace concerns: PFCs also
disrupt the current distribution in the cell and interrupt metal production, so
suppressing the anode effect is an operating priority quite apart from its
climate cost. A cell that evolves chlorine into a recycle loop avoids the
problem entirely rather than managing it.

### Other Electrochemical Routes

Two research directions sit alongside the two production cells. The FFC
Cambridge process reduces solid rare earth oxide directly in a molten calcium
chloride bath, with the oxide as the cathode itself, and has been demonstrated
for Gd, Tb, Dy, Er and Ce; its attraction is that it skips the fluoride
intermediate and therefore the HF plant needed to make it. Room-temperature
ionic liquids have been explored as a low-temperature electrolyte for the same
purpose. Neither has been shown at a scale that bears on industrial rare earth
metal supply, and both face the same difficulty: the rare earths are reduced at
potentials so negative that most solvents decompose first.

## Comparison with Conventional Methods

### Technical Performance
| **Parameter** | **Carbochlorination** | **Conventional Hydrometallurgy** |
|----|----|----|
| Operating Temperature | 600-900°C | 150-200°C (acid); 140-150°C (alkali) |
| REE Recovery Rate | \>93-97% | 90-98% |
| Product Form | Anhydrous RECl₃ (water soluble) | REE sulfates/hydroxides |
| Process Steps | Single step + water wash | Multiple steps (roasting, leaching, precipitation) |
| Reagent Consumption | Cl₂ + C only | H₂SO₄, NaOH, HCl, organics |
| Process Time | 60 minutes (chlorination) | Several hours to days |
| Selectivity | Moderate (based on volatility) | High (via solvent extraction) |

The advantages that follow from the chemistry of the preceding sections are
these: the product is an anhydrous chloride, which is what a molten salt cell
wants, so the dehydration step that plagues aqueous routes disappears; the
volatility spread between the rare earth chlorides and the impurity chlorides
does real separation work inside the reactor; and the reagents and equipment are
those of an existing chlorometallurgical industry.

The limitations are the mirror image. Chlorine at 900 °C must be contained,
distributed and recycled, which is a materials problem before it is a chemistry
problem. The operating temperature is several hundred degrees above an
autoclave. And, decisively for this book, carbochlorination does not separate
one rare earth from another: the mixed chloride still goes to a solvent
extraction plant.

### Environmental Impact
| **Environmental Factor** | **Carbochlorination** | **Conventional Methods** |
|----|----|----|
| Wastewater Generation | Minimal (water wash only) | Significant (acid/alkali effluents) |
| Acid/Alkali Consumption | None | High (recycling possible) |
| Gaseous Emissions | CO/CO₂, excess Cl₂ (recyclable) | HF, SO₂, NOx from roasting |
| Solid Waste | Reduced (chlorides are soluble) | Precipitation sludges |
| Energy Intensity | Not established in the open literature | Variable (process dependent) |
| Radioactive Waste | Concentrated ThCl₄ stream | Dispersed in waste streams |

Its proponents describe carbochlorination as a "clean metallurgical
technology," on the grounds that it eliminates the acid and alkali wastewater
streams, recycles chlorine within the system, and recovers by-products such as
HF from bastnäsite and phosphorus values from monazite
[@xue2026clean; @xue2025onestep]. The description is fair as far as the
liquid effluent goes, and it should be read with the qualification made earlier
in this chapter: a chlorinator has no aqueous effluent because it has no aqueous
phase, and the acid burden simply moves downstream to whichever solvent
extraction plant separates the resulting mixed chloride.

The comparison it is being made against is real enough. Conventional rare earth
processing generates large quantities of hazardous waste, consumes water at
scale, and disperses naturally occurring radioactive residues through the
{index}`tailings <tailings management>` rather than concentrating them
[@weber2012rare].

### Economic Considerations
An honest economic comparison has to weigh four things against each other:
the capital cost of chlorine-resistant equipment against a simpler flowsheet;
the saving on acid and alkali against the cost of heating to 900 °C; the value
of recycling chlorine within the plant; and whatever premium an anhydrous
chloride commands over an oxide for electrolytic feed.

We do not put numbers on any of them. No published {index}`techno-economic
<techno-economic analysis (TEA)>` analysis compares an industrial-scale rare
earth carbochlorination plant with an established hydrometallurgical one, and
the minimum-economic-scale figures that circulate for this route could not be
traced to a primary source. The "short-process" argument — one chlorination step
followed by a water wash — is plausible on flowsheet grounds and unquantified in
the open literature.

A side-by-side comparison of carbochlorination against the other extraction and
processing technologies in this book — readiness, recovery, energy intensity,
environmental burden and demonstrated scale — is given once, for all of them, in
[](#technology-comparison); it is not repeated here.

## Industrial Implementation

### Technology Readiness Level
Readiness for rare earth carbochlorination is lower than its long history
suggests. CSIRO's 2024 assessment of mid-stream processing places chlorination
roasting at laboratory scale: the chemistry is "generally well understood", but
the processes "are being investigated at lab scale", some of them on the Baotou
mixed bastnäsite-monazite concentrate, and corrosion of the equipment and the
energy intensity of the route are named as the obstacles to commercial use
[@csiro2024minerals]. The industrially established routes for the same
concentrates are the ones treated in [](#hydrometallurgical-leaching) --
oxidation roasting followed by acid leaching, the sulfuric acid bake, and
caustic decomposition. The recycling variants of carbochlorination are likewise
at laboratory and pilot scale. We give no TRL numbers for the route, because
the specific ratings that circulate for it are not traceable to a published
assessment.

### Scale-Up Challenges
Key challenges for industrial-scale implementation include:

- Fluidized Bed Reactor Design: Complex gas-solid interactions require careful modeling and control. Dead zones and non-uniform fluidization can affect conversion efficiency.

- Material Handling: Prevention of raw material splashing through pelletization with binders and reducing agents.

- Chlorine Management: Safe handling, distribution, and recycling of chlorine gas at industrial scale.

- Corrosion Control: Development of materials resistant to high-temperature chlorine environments.

- Heat Integration: Efficient recovery and utilization of reaction heat.

- Product Separation: Design of cascade condensation systems for separating different chloride products.

- Expertise Gap: Limited technical know-how for rare earth chlorination outside China after decades of offshoring.

Reference to the titanium industry provides valuable lessons, as carbochlorination of rutile/ilmenite to produce TiCl₄ has been practiced commercially for decades (see [](#industrial-precedents)). The Kroll process for titanium uses similar principles, and development of analogous compact distillation apparatus for REE separation has been proposed.

### Equipment and Safety Considerations
Industrial implementation requires:

- Chlorination Reactor: Fluidized bed or packed bed reactor with temperature control (600-900°C)

- Gas Distribution System: For controlled chlorine introduction

- Condensation Train: Cascade system for separating products by boiling point

- Off-Gas Treatment: For capturing excess chlorine and volatile byproducts

- Water Leaching System: For dissolving water-soluble REE chlorides

- Corrosion-Resistant Materials: Refractory linings, special alloys for chlorine service

- Safety Systems: Chlorine detection, emergency scrubbing, personnel protection

Operating temperatures of 600-900 °C are elevated relative to an autoclave but modest relative to the carbochlorination of titanium or zirconium, which runs at 1,000-1,200 °C. They are not lower than conventional rare earth roasting, which as noted earlier runs at 500-700 °C; the equipment burden here comes from the chlorine, not from the temperature.

(industrial-precedents)=
## Industrial Precedents: Titanium, Zirconium, Aluminium, Magnesium, and Niobium-Tantalum

Carbochlorination has been practiced at massive industrial scale for decades in the production of titanium and nuclear-grade zirconium. These established industries provide invaluable precedent, proven technology, and potential synergies for rare earth element processing. The infrastructure, expertise, and equipment developed for Ti and Zr chloride production represent a foundation upon which REE carbochlorination could be built.

### Titanium Production via Carbochlorination
The titanium industry represents the largest and most mature application of
carbochlorination. TiO₂ pigment is made by either the chloride process or the
sulfate process, and it is the chloride process that begins with a
carbochlorination step; the USGS expects the split between chloride- and
sulfate-process pigment capacity to reach parity, driven mainly by the
expansion of chloride capacity in China [@usgs2020titanium]. The route and its
place in titanium metallurgy are reviewed by Zhang and co-workers
[@zhang2011literature].

> The Chloride Process for TiO₂/Ti Metal:

In the chloride process, natural rutile, synthetic rutile, chloride-grade
ilmenite or titanium slag is converted to TiCl₄ by chlorination in the presence
of petroleum coke; the TiCl₄ is then oxidized with air or oxygen at about
1000 °C and the resulting TiO₂ is calcined to strip residual chlorine
[@usgs2020titanium]:

> TiO₂ + 2C + 2Cl₂ → TiCl₄ + 2CO

The chlorinator is a fluidized bed. Morris and Jensen measured chlorination
rates of Australian rutile in a fluidized bed with CO and with coke as the
reductant over 1143--1311 K, that is roughly 870--1040 °C
[@morris1976fluidized], and Zhou and Sohn built a bubble-assemblage model of
the same reactor that reproduces both the reaction rate and the evolving
particle size distribution [@zhou1996mathematical]. Those two papers are the
closest analogue in the open literature to what an REE chlorinator would have
to be designed as.

Feedstock grades run from rutile (\>95 % TiO₂) through synthetic rutile and
upgraded ilmenite slag; the reductant is petroleum coke; and the product is
liquid TiCl₄, boiling at 136 °C.

> Purification and Metal Production:

The crude TiCl₄ contains impurities including FeCl₃, AlCl₃, VOCl₃, SnCl₄, and SiCl₄. These are removed through a combination of [@habashi1997handbook]:

- Selective condensation, exploiting the boiling-point spread among FeCl₃, AlCl₃ and TiCl₄

- Chemical treatment — classically with H₂S or mineral oil — which reduces VOCl₃ to solid VOCl₂ and drops it out of the liquid; vanadium is removed as a solid, not converted to a higher-boiling chloride

- Multi-stage fractional distillation to achieve \>99.9% purity

- The purified TiCl₄ is reduced to titanium metal via the Kroll process (Mg reduction) or Hunter process (Na reduction)

> Major Global Producers:

The chloride process is run by a small number of large firms. The USGS lists
the U.S. chloride-process pigment producers as Chemours, INEOS Pigments,
Louisiana Pigment (a Kronos-Venator joint venture) and Tronox, with no domestic
sulfate-process producer at all [@usgs2020titanium]. The largest single
chloride operator outside the United States is Lomon Billions in China, which
reports roughly 660 kt/y of chloride-process capacity within about 1,510 kt/y
of total TiO₂ capacity [@lomon2024titanium].

What the titanium industry establishes for our purposes is narrower than it is
often made to sound. It shows that a carbochlorination step can be run
continuously at the scale of hundreds of kilotonnes a year on an oxide
feedstock, in a fluidized bed, with coke as the reductant and chlorine
recovered downstream --- commercial Kroll-process production dates from 1948
[@usgs2020titanium]. It does not show that the same is true for a mixed rare
earth concentrate, whose chlorides are far less volatile and far more
hygroscopic than TiCl₄, and which has to be separated after chlorination rather
than simply purified.

### The Zr/Hf Separation Challenge
Zirconium is an ideal material for nuclear reactor fuel cladding due to its exceptionally low thermal neutron absorption cross-section. However, zirconium ores (primarily zircon sand, ZrSiO₄) naturally contain 1-3 wt% hafnium, which has a very high neutron absorption cross-section [@xu2015production]. For nuclear applications, the hafnium content must be reduced to less than 100 ppm---a challenging separation given the remarkable chemical similarity between Zr and Hf (same group, nearly identical ionic radii).

This separation challenge parallels the difficulties in separating individual rare earth elements, which also exhibit very similar chemical properties across the lanthanide series. The industrial solutions developed for Zr/Hf separation therefore offer instructive lessons for REE processing [@xu2015production].

### Industrial Zr Carbochlorination Process
The production of nuclear-grade zirconium begins with carbochlorination of zircon sand. The process is conducted in fluidized bed reactors at temperatures of 1000-1200°C [@xu2015production; @yin2024preparation]:

> ZrSiO₄ + 4C + 4Cl₂ → ZrCl₄ + SiCl₄ + 4CO

Key process characteristics include:

- Temperature: 1000-1200°C in fluidized bed reactors

- Feedstock: Zircon sand mixed with petroleum coke or graphite

- Products: Mixed ZrCl₄/HfCl₄ vapor (sublimation point \~331°C) plus volatile SiCl₄

- Scale: Industrial plants produce several tonnes of crude ZrCl₄ per day

- The ZrCl₄/HfCl₄ mixture is condensed as a solid powder for subsequent separation

This carbochlorination step has been optimized over decades of industrial operation, with well-established practices for reactor design, chlorine distribution, heat management, and product recovery [@yang2016separation].

### Molten Salt Extractive Distillation for Zr/Hf
Following carbochlorination, the separation of ZrCl₄ from HfCl₄ is accomplished through molten salt extractive distillation---the only pyrometallurgical Zr/Hf separation method operating at industrial scale [@chen2025process]. This technology, developed by Cezus (now Framatome) in France during the 1980s, exploits the slight difference in vapor pressure between ZrCl₄ and HfCl₄.

The process uses a distillation column with multiple plates, each containing a layer of molten salt (typically KAlCl₄). The mixed ZrCl₄/HfCl₄ vapor from carbochlorination is introduced into the column, and selective absorption/desorption in the molten salt achieves separation [@chen2025process]. Key parameters include:

- Molten salt system: KAlCl₄ or similar alkali metal chloroaluminates

- Column design: 12+ stage sieve plate columns

- Separation efficiency: Produces ZrCl₄ with \<100 ppm Hf and HfCl₄ with \>96% purity

- The purified ZrCl₄ is then reduced to zirconium metal via the Kroll process (magnesiothermic reduction)

### Lessons and Synergies for REE Processing
The established Ti and Zr/Hf carbochlorination industries offer several important lessons and potential synergies for rare earth element processing:

> Technology Transfer Opportunities:

- Fluidized bed reactor design and operation at 1000°C+ with chlorine atmospheres

- Materials of construction resistant to high-temperature chlorine corrosion

- Chloride condensation and handling systems for subliming metal chlorides

- Chlorine recycling and off-gas treatment systems

- Safety protocols for large-scale chlorine operations

> Potential for Integrated Operations:

Facilities already operating carbochlorination for titanium (TiCl₄ production) or zirconium could potentially integrate rare earth chloride production with relatively modest additional investment. Shared infrastructure would include:

- Chlorine supply and distribution systems

- High-temperature reactor expertise and maintenance capabilities

- Chloride product handling and packaging

- Environmental control and chlorine scrubbing systems

- Trained workforce familiar with chlorometallurgical operations

> Adaptation of Separation Technologies:

The molten salt extractive distillation technology used for Zr/Hf separation could potentially be adapted for REE chloride separation, exploiting differences in vapor pressure and molten salt solubility among the various REE chlorides. While REE separation is more complex (17 elements vs. 2), the fundamental principles are analogous.

| **Parameter** | **Zr/Hf Processing** | **REE Processing (Potential)** |
|----|----|----|
| Carbochlorination Temp. | 1000-1200°C | 600-900°C (lower) |
| Number of Elements | 2 (Zr, Hf) | 17 (lanthanides + Sc, Y) |
| Separation Method | Molten salt distillation | Distillation, selective condensation |
| Industrial Status | Commercial (decades) | Pilot/demo scale |
| Primary Driver | Nuclear industry | Clean energy, electronics |

The successful industrial implementation of carbochlorination for titanium pigment production and nuclear-grade zirconium demonstrates that the fundamental process challenges---high-temperature chlorine handling, chloride separation, and product purification---can be solved at commercial scale. This precedent significantly de-risks the development of carbochlorination for rare earth elements.

### Aluminum Chloride Production from Alumina
Anhydrous aluminum chloride (AlCl₃) production via carbochlorination represents another important industrial precedent. First demonstrated by Hans Christian Oersted in 1825, it is today a routine industrial operation for making the anhydrous chloride as a chemical commodity — though not, as discussed below, as a route to aluminium metal. The carbochlorination of alumina follows the reaction:

> Al₂O₃ + 3C + 3Cl₂ → 2AlCl₃ + 3CO

Key process characteristics include:

- Temperature: 500-700°C in fluidized bed reactors

- Mildly exothermic — of order a few tens of kJ per mole of AlCl₃ when CO is the carbon product, and several times that if the carbon burns through to CO₂ — so a well-insulated fluidized bed can approach thermal self-sufficiency once started

- Little external heating required at steady state

- Feedstock: γ-alumina with finely divided carbon (petroleum coke)

- Product: AlCl₃ vapor condensed as solid (sublimation point \~180°C)

> Industrial Applications:

The aluminum chloride process has garnered renewed interest as a potential alternative to the Hall-Héroult process for primary aluminum production. Work on the bauxite chloride route has shown [@namboothiri2017bauxite]:

- Bauxite can be carbochlorinated directly, producing mixed chlorides (AlCl₃, FeCl₃, SiCl₄, TiCl₄)

- A claimed energy saving relative to Hall-Héroult electrolysis; note that Alcoa operated a chloride smelter on this principle from 1976 and closed it in 1985, so the route is a demonstrated failure at commercial scale, not merely an undeveloped one

- Easier CO₂ capture and sequestration potential

- Biocarbon can replace petroleum coke (no mechanical strength requirements)

- AlCl₃ is subsequently electrolyzed to produce aluminum metal

> Relevance to REE Recycling:

Øye's account of the chloride route is concerned with aluminium alone and says
nothing about rare earths [@oye2019chloride]. The extension is ours, and it is
a conjecture rather than a result: end-of-life materials that carry both
aluminium and rare earths --- spent {index}`FCC catalyst <FCC catalyst>`,
some electronic scrap --- present both metals as oxides to the same chlorinating
atmosphere, so a single carbochlorination step would in principle chloridize
both. Whether the resulting AlCl₃/REECl₃ mixture is easier or harder to work up
than the separate streams is unstudied, and the volatility gap between AlCl₃,
which sublimes at 180 °C, and the rare earth chlorides, which do not boil below
about 1500 °C, is the obvious place to start.

### Magnesium Production via Chlorination
Magnesium production via the chloride route has a long industrial history, with carbochlorination serving as an important alternative to the seawater route for producing anhydrous MgCl₂ feedstock for electrolysis [@gaballah1999chlorination]. The carbochlorination reaction is:

> MgO + C + Cl₂ → MgCl₂ + CO

Thermogravimetric studies have characterized the carbochlorination of MgO [@gaballah1999chlorination]:

- Optimal temperature range: 500-675°C (conversion decreases above 700°C due to MgCl₂ melting)

- Activation energy: 49 kJ/mol (between 425-600°C)

- Optimal Cl₂/CO molar ratio: approximately 0.6

- Maximum conversion: 82% at 675°C

- Carbon presence enhances MgO conversion by up to 49%

> Historical Industrial Implementation:

Carbochlorination of magnesium oxide from magnesite, silicates, or hydroxides was practiced industrially at several facilities [@gupta2003chemical]:

- IG Farben process (Germany, pre-WWII)

- Basic Magnesium plant (Henderson, Nevada, WWII era)

- Norsk Hydro (Porsgrunn, Norway), which ran a chlorination route from the early 1950s until the plant closed in 2002

- The Dow seawater process at Freeport, Texas, which took a different route through Mg(OH)₂ and closed in 1998

> Integration with Titanium/Zirconium Production:

Magnesium and chlorine are intimately linked with titanium and zirconium production through the Kroll process, which uses magnesium to reduce TiCl₄ and ZrCl₄ to metals, producing MgCl₂ as a byproduct [@usgs2020titanium]. That MgCl₂ is electrolyzed to regenerate magnesium and chlorine, closing the loop [@habashi1997handbook]. A rare earth chlorinator sited next to such a plant would have a chlorine supply and a magnesium supply already in place; we know of no attempt to do it.

### Niobium and Tantalum Separation via Chlorination
The separation of niobium and tantalum by chlorination and distillation represents one of the most successful applications of chloride-based separation for chemically similar elements---directly analogous to the REE separation challenge [@habashi1997handbook]. The carbochlorination reactions are:

> Nb₂O₅ + 5C + 5Cl₂ → 2NbCl₅ + 5CO
>
> Ta₂O₅ + 5C + 5Cl₂ → 2TaCl₅ + 5CO
>
> Process Characteristics:

Research on tin slag processing has demonstrated the effectiveness of carbochlorination for Nb/Ta recovery [@gupta1984extractive]:

- Temperature: 500-1000°C depending on concentrate grade

- Activation energy: 103-166 kJ/mol (carbochlorination is 116 kJ/mol for low-grade concentrate)

- High-grade concentrate carbochlorination at 500°C achieves complete extraction

- Recovery rates: up to 95% of Nb and Ta at 1000°C

- Carbochlorination significantly more effective than direct chlorination

> Separation by Distillation:

The key advantage of the chloride route for Nb/Ta is the ability to separate these very similar elements by fractional distillation [@yang1999carbochlorination]:

- NbCl₅ boiling point: 248°C

- TaCl₅ boiling point: 236°C

- Distillation produces NbCl₅ with tantalum reduced to the low-ppm level, and other metallic impurities similarly low

- Chlorides can be hydrolyzed to hydroxides and calcined to high-purity oxides

> Lessons for REE Processing:

The Nb/Ta separation precedent is particularly instructive for REE processing because it demonstrates successful industrial separation of chemically similar elements via chloride distillation. While REE separation is more complex (17 elements vs. 2), the fundamental principle of exploiting vapor pressure differences among chlorides is directly applicable. Whether a cascade of distillation stages could be made to do the same for the rare earth chlorides is an open question and not one the Nb/Ta precedent settles. The analogy should not be pressed too far, though: most Nb/Ta separation practised today is not chloride distillation but MIBK solvent extraction from HF media, and the reason is the same one that keeps the rare earths in solvent extraction — a liquid-liquid contactor buys many more theoretical stages per unit of capital than a high-temperature column does.

> Summary of Industrial Carbochlorination Precedents:

| **Parameter** | **Titanium** | **Zirconium** | **Aluminum** | **Magnesium** | **Nb/Ta** | **REE (Potential)** |
|----|----|----|----|----|----|----|
| Global Scale | Millions t/yr TiCl₄ | Thousands t/yr | Large scale | Historical | Specialty | To be developed |
| Temperature | 900-1050°C | 1000-1200°C | 500-700°C | 500-675°C | 500-1000°C | 600-900°C |
| Status | Commercial | Commercial | Commercial (chemical AlCl₃); abandoned for metal | Historical | Commercial, specialty | Pilot and laboratory |
| Key Driver | Pigments, aerospace | Nuclear | Alt. Al route | Metal production | Electronics | Clean energy |
| Separation | Distillation | Molten salt | Condensation | Electrolysis | Distillation | Multiple |

(outlook)=
## Outlook

Carbochlorination converts rare earth oxides to anhydrous chlorides at 600-900 °C,
and it does so for every element in the series. The thermodynamics are
favourable across the lanthanides plus scandium and yttrium, laboratory and
pilot work reports better than 93 % conversion on light rare earth oxides, and
the route works on primary concentrates — bastnäsite, monazite, xenotime — as
well as on magnet scrap and phosphor waste. The reaction is practised
industrially in China and has been proven at enormous scale in the neighbouring
titanium and zirconium industries, which is the strongest argument for its
feasibility anywhere else.

What it does not do is separate one rare earth from another. That point has been
made repeatedly in this chapter and it deserves to be the last word on the
route. Nothing in a chlorinator distinguishes NdCl₃ from PrCl₃; the volatility
window that does the work separates the rare earths *collectively* from iron,
calcium, silicon, aluminium, phosphorus and thorium. Carbochlorination is
therefore a decomposition and dissolution step — a competitor to acid baking and
caustic cracking, not to solvent extraction — and the mixed chloride it produces
still goes to the plant described in [](#solvent-extraction-fundamentals).

Its case rests on three genuine advantages. The product is anhydrous, which is
what a molten salt cell wants and what an aqueous route cannot deliver without
an expensive dehydration step. There is no acid or alkali effluent from the
chlorinator itself, and the chlorine can be recycled — including, in the
chloride electrolysis cell of [](#molten-salt-electrolysis), from the metal
production step at the far end of the flowsheet. And thorium reports to a small
concentrated volatile stream rather than being dispersed through the tailings,
which makes it easier to manage even though it does not make it go away.

The case against is equally concrete. Chlorine at 900 °C is a materials problem
that has to be engineered rather than argued away; the energy to reach that
temperature is real; and no published techno-economic analysis compares an
industrial-scale rare earth carbochlorination plant with the hydrometallurgical
route it would replace. Several of the performance claims that circulate for
this technology — energy intensities, minimum economic scales, technology
readiness levels — could not be traced to primary sources while this chapter was
being written, and they have been left out rather than repeated.

The developments most worth watching are the ones that change the economics
rather than the chemistry: chloride-based molten salt electrolysis, which closes
the chlorine loop and removes the perfluorocarbon emissions of the incumbent
fluoride cell; flash Joule heating, which attacks magnet recycling at a scale
and capital cost that suits distributed feedstock; and the reconstruction of
chlorometallurgical expertise outside China, which is a workforce problem before
it is a technical one.
