---
title: Pyrometallurgical and Halogenation Routes
---

(pyrometallurgical-and-halogenation-routes)=
# Pyrometallurgical and Halogenation Routes

Everything else in this book dissolves the ore. Halogenation does not. Instead
of leaching a mineral into an aqueous liquor and then separating ions in
solution, {index}`carbochlorination` converts rare earth oxides directly to volatile or
low-melting chlorides in the solid state, and separates them by boiling point.
It is a different physics of separation — vapour pressure rather than
{index}`distribution ratio` — and it therefore has a different set of strengths and a
different set of problems.

The strengths are real: no aqueous waste stream, no solvent inventory, no acid
consumption, and a route that handles refractory minerals which resist acid
attack. The problems are equally real: chlorine gas at 800–1200 °C, materials of
construction that survive it, and the fact that adjacent lanthanide chlorides
have boiling points nearly as close together as their distribution ratios.

What makes this chapter worth reading even if halogenation never separates a
single rare earth is the industrial precedent. Titanium, zirconium, aluminium,
magnesium, and niobium-tantalum are all produced or purified at large scale by
exactly this chemistry today. The Kroll process is a century-old
carbochlorination. The zirconium industry separates Zr from Hf — a pair at least
as similar as any lanthanide pair — by extractive distillation of their
chlorides in a molten salt. Those industries have already solved most of the
materials and containment problems that a rare earth carbochlorination plant
would face, and the second half of this chapter reads them for transferable
lessons.

This chapter merges two source documents on halogenation with the
pyrometallurgical and electrochemical material from the broad review.

## The Halogenation Family

### Fundamental Thermodynamics of Halogenation
Halogenation of metal oxides to form metal halides is governed by fundamental thermodynamic principles. The general reaction for direct halogenation is:

> MₓOᵧ + γX₂ → xMX₂ᵧ/ₓ + γ/2 O₂

For most rare earth oxides, direct halogenation is thermodynamically unfavorable without a reducing agent. Carbon serves as an effective reductant, lowering the reaction temperature and driving the reaction toward products through the formation of CO or CO₂:

> MₓOᵧ + γC + γX₂ → xMX₂ᵧ/ₓ + γCO (carbohalogenation)

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

> Bromine:

Bromination of rare earths is primarily used for synthesis of rare earth bromides for specialized applications rather than large-scale extraction. Bromine can selectively dissolve metals in organic solvents, enabling separation from oxides. Lanthanide tribromides (LnBr₃) form various complex compounds with alkali metal halides.

> Iodine:

Iodination is the mildest halogenation route, producing rare earth iodides at relatively low temperatures (250-500°C). Direct reaction of lanthanide metals with iodine in THF produces triiodides LnI₃(THF)ₙ in good yields. Rare earth iodides are hygroscopic and prone to hydrolysis, limiting industrial applications.

## Carbochlorination Chemistry

### Fundamental Chemistry
The carbochlorination process converts metal oxides to chlorides through the synergistic action of carbon (reducing agent) and chlorine gas (chlorinating agent) at elevated temperatures [@anderson2015investigation]. The presence of carbon is essential because direct {index}`chlorination` of many metal oxides, including rare earth oxides, is thermodynamically unfavorable at accessible temperatures without a reducing agent [@hua2014selective].

For rare earth oxides, the primary reactions are:

- RE₂O₃ + 3C + 3Cl₂ → 2RECl₃ + 3CO (at higher temperatures)

- RE₂O₃ + 1.5C + 3Cl₂ → 2RECl₃ + 1.5CO₂ (at lower temperatures)

- CeO₂ + 2C + 2Cl₂ → CeCl₃ + 2CO (for tetravalent {index}`cerium`)

Research has shown that direct contact between metal oxides and carbon is not necessary for effective chlorination [@gavira2010carbochlorination]. The reaction proceeds through gaseous intermediates, with carbon providing catalytic activity sites for the formation of highly reactive species. Proposed intermediates include phosgene (COCl₂), monatomic chlorine, and carbon tetrachloride (CCl₄) [@murase1995recovery].

### Thermodynamic Considerations
Thermodynamic analysis using Gibbs free energy calculations demonstrates that carbochlorination of rare earth oxides is spontaneous (ΔG \< 0) over a wide temperature range of 500-1000°C [@xue2025carbochlorination; @xu2024rare]. The Gibbs free energy becomes increasingly negative with rising temperature, indicating enhanced thermodynamic driving force.

Key thermodynamic findings include:

- Operating temperatures of 600-900°C are typical, significantly lower than the \>1200°C required for traditional roasting processes [@zheng2019mechanism].

- Above 700°C, the primary carbon product switches from CO₂ to CO, requiring more carbon for complete conversion but providing better energy efficiency [@borra2016recovery].

- Phase stability diagrams (RE-O-Cl systems) reveal element-specific reaction pathways that influence process design [@xue2025carbochlorination].

- The carbochlorination process provides substantially lower activation energy compared to direct chlorination or oxide reduction routes [@xia2024experimental].

### Reaction Mechanisms and Kinetics
The carbochlorination reaction proceeds through distinct mechanisms depending on the specific rare earth element. For cerium oxide (CeO₂), phase stability diagrams show a direct boundary between the CeO₂ and CeCl₃ phases, indicating that the oxide can convert directly to the chloride without intermediate phases [@roine2019hsc].

In contrast, {index}`neodymium` oxide (Nd₂O₃) must convert through an intermediate oxychloride (NdOCl) phase before complete conversion to NdCl₃ [@anderson2015investigation]. This difference has important implications for process optimization, as the oxychloride plays a larger role in neodymium processing than in cerium processing.

Kinetic studies reveal that the carbochlorination reaction proceeds in two stages, both controlled by chemical reactions rather than diffusion [@yang2017ree]. Key kinetic parameters include:

- First stage activation energy: 12.54 kJ/mol

- Second stage activation energy: 11.22 kJ/mol

- Optimal temperature: 700°C

- Optimal chlorination time: 60 minutes

- Carbon ratio: 12% by weight

- Chlorine gas flow rate: 10 L/min (laboratory scale)

- Achievable conversion rate: \>93%

For {index}`yttrium` oxide (Y₂O₃), the reaction mechanism involves the initial formation of YOCl through nucleation and growth. At temperatures above 715°C, the final product is liquid YCl₃, which can evaporate from the reaction zone [@gavira2010carbochlorination].

### Kinetics and Mechanism
Research has revealed element-specific reaction mechanisms. For cerium oxide (CeO₂), phase stability diagrams show a direct boundary between CeO₂ and CeCl₃ phases, indicating direct conversion without intermediate phases. In contrast, neodymium oxide (Nd₂O₃) converts through an intermediate oxychloride (NdOCl) phase before complete conversion to NdCl₃.

Key kinetic parameters from literature:

- First stage activation energy: 12.54 kJ/mol

- Second stage activation energy: 11.22 kJ/mol

- Optimal temperature: 700°C

- Optimal chlorination time: 60 minutes

- Carbon ratio: 12% by weight

- Achievable conversion rate: \>93%

The carbochlorination reaction proceeds through gaseous intermediates. Proposed reactive species include phosgene (COCl₂), monatomic chlorine, and carbon tetrachloride (CCl₄). Direct contact between metal oxides and carbon is not necessary for effective chlorination.

### Industrial Applications
Carbochlorination has been demonstrated for multiple feedstocks:

> Primary Ore Processing:

Bastnaesite \[(Ce,La)(CO₃)F\] processing requires special consideration of fluorine content. Silicon tetrachloride (SiCl₄) serves as a defluorinating agent, preventing formation of volatile fluorides. Process parameters for bastnaesite: 700°C, 12% carbon by weight, recovery rate 93-97% of rare earths.

> {index}`NdFeB` Magnet Recycling:

Chlorination roasting at 300-500°C with subsequent water leaching enables REE recovery from end-of-life permanent magnets. The selective chlorination of REEs to RECl₃ enables separation from iron, which remains as oxide under appropriate conditions.

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

### Processing of Mixed Bastnaesite-Monazite Concentrates
The SC-CVT process is particularly effective for mixed bastnaesite (REFCO₃) and monazite (REPO₄) concentrates:

**Optimized Conditions:**

| Parameter | Value |
| ----------- | ------- |
| Chlorination temperature | 500-800°C |
| Atmosphere | Cl₂ + SiCl₄ |
| REE chloride yield | 92-99 mol% |

**Two-Stage CVT Separation:**

1.  **Stage 1** (800°C, 0.5 h): Cl₂ + SiCl₄ + AlCl₃ atmosphere
2.  **Stage 2** (1000°C, 6 h): Cl₂ + AlCl₃ atmosphere with temperature gradients

This approach operates at temperatures as low as 500°C, compared to the conventional Goldschmidt process at 1000-1200°C.

### One-Step Clean Process (2025)
A recent breakthrough proposes a one-step carbochlorination-washing process achieving "zero discharge" of acidic wastewater:

**Optimized Parameters:**

| Parameter | Optimal Value |
| ----------- | --------------- |
| Chlorination temperature | 800°C |
| Reaction time | 60 min |
| Chlorine flow rate | 10 L/min |
| C:RE₂O₃ molar ratio | 4.2:1 |
| Particle size | 250 mesh |

**Chlorination Rates Achieved:**

| Element | Chlorination Rate |
| --------- | ------------------ |
| Rare earths | 93% |
| Calcium | 99% |
| Barium | 95% |
| Iron | 99% |

**Environmental Advantages:**

- No acid or alkali reagents required
- Emissions recyclable within the system
- Short-process characteristic avoids wastewater generation
- Significantly reduced equipment costs due to lower operating temperatures

## Application Across the Rare Earth Series

Carbochlorination has been investigated for various rare earth elements with thermodynamic and experimental evidence supporting its applicability across the entire lanthanide series plus {index}`scandium` and yttrium.

### Light Rare Earth Elements
The light rare earth elements (LREEs) comprise {index}`lanthanum` (La), cerium (Ce), {index}`praseodymium` (Pr), neodymium (Nd), promethium (Pm), and {index}`samarium` (Sm). These elements are more abundant in the principal REE minerals bastnaesite and monazite, making them the primary targets for industrial carbochlorination [@gupta1992extractive].

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

The HREEs follow similar carbochlorination chemistry to the LREEs, with thermodynamic calculations indicating spontaneous reaction at temperatures above 500°C [@jyothi2020rare]. Europium and ytterbium present special cases as they can form divalent chlorides (EuCl₂, YbCl₂) under strongly reducing conditions, which may affect separation strategies [@kumari2015process].

### Scandium and Yttrium
Scandium (Sc) and yttrium (Y), while not lanthanides, are classified as rare earth elements due to their similar chemical properties and occurrence with lanthanides in mineral deposits [@energy2011critical].

Yttrium oxide (Y₂O₃) carbochlorination has been studied in detail. Key findings include [@habashi2013extractive]:

- The reaction proceeds via nucleation and growth of YOCl intermediate

- At temperatures above 715°C, the final product is liquid YCl₃

- Evaporation of YCl₃ is observed in thermogravimetric analysis at high temperatures

- Complete conversion to anhydrous YCl₃ is achievable under optimized conditions

Scandium, though less studied for carbochlorination specifically, is expected to follow similar thermodynamic and kinetic patterns given its chemical similarity to yttrium and the lanthanides [@gorman2018sustainable].

## Primary Ore Processing

### Bastnaesite Processing
Bastnaesite \[(Ce,La)(CO₃)F\] is a fluorocarbonate mineral containing approximately 70 wt% rare earth oxides, primarily light rare earths [@chi2008weathered]. The {index}`Bayan Obo` deposit in China and the {index}`Mountain Pass` deposit in the United States represent the world's largest bastnaesite resources [@castor2006rare].

Carbochlorination of bastnaesite requires special consideration of the fluorine content. Zhang et al. developed a carbochlorination process using carbon as the reducing agent, chlorine as the chlorinating agent, and silicon tetrachloride (SiCl₄) as a defluorinating agent [@zhang2015occurrence]. The defluorination reaction prevents formation of volatile fluorides and allows recovery of fluorine as valuable byproduct.

Process parameters for bastnaesite carbochlorination [@suli2017rare]:

- Temperature: 700°C (optimal)

- Carbon ratio: 12% by weight

- Chlorine flow: \~2× theoretical requirement

- Recovery rate: 93-97% of rare earths

- Energy consumption: 1.44-2.16 GJ/tonne REE chlorides

- Theoretical heat requirement: 0.94-1.21 GJ/tonne RE contained

### Monazite Processing
Monazite \[(Ce,La,Nd,Th)PO₄\] is a phosphate mineral containing 55-65% REO along with thorium (4-12%) [@battsengel2018recovery]. The radioactive thorium content presents unique processing challenges that must be addressed regardless of extraction method.

Carbochlorination of monazite offers advantages for thorium management. The phosphorus content can be converted to volatile POCl₃, which can be separately recovered. Thorium chloride (ThCl₄) can be separated based on its different volatility characteristics compared to REE chlorides [@weng2015detailed].

Conventional monazite processing involves either [@jordens2013beneficiation]:

- Acid process: H₂SO₄ digestion at 150-200°C producing soluble sulfates

- Alkaline process: NaOH treatment at 140-150°C in autoclave

Carbochlorination may provide a cleaner alternative by avoiding the generation of large volumes of acidic or alkaline waste streams while enabling more straightforward thorium separation [@tsamis2015recovery].

### Xenotime Processing
{index}`Xenotime <xenotime>` \[YPO₄\] is the primary mineral source for heavy rare earths and yttrium. The mineral contains 52-62% REO with a composition heavily weighted toward HREEs and Y [@kaya2016recovery].

The carbochlorination of xenotime follows similar principles to monazite, with the phosphate matrix being converted to volatile chloride products while the REE chlorides are retained. Given the higher value of HREEs, carbochlorination may offer economic advantages through reduced reagent costs and simplified product recovery [@lorenz2023recovery].

## Recycling Applications

### NdFeB Magnet Recycling
NdFeB permanent magnets represent the largest application of neodymium and contain significant amounts of praseodymium, dysprosium, and terbium. End-of-life magnets from electric vehicles, wind turbines, and consumer electronics offer an important secondary resource [@onal2015recycling].

Multiple chlorination approaches have been investigated for NdFeB recycling [@liu2014solvent]:

- Chlorination roasting at 300-500°C with subsequent water leaching

- High-temperature chlorination at 1173-1273 K with distillation separation

- Solid-state chlorination with NH₄Cl, FeCl₂, or MgCl₂-KCl

- {index}`Flash Joule heating <flash Joule heating>` combined with chlorination (FJH-Cl₂)

The chlorination roasting method offers lower roasting temperatures and shorter times compared to oxidation roasting, yielding RE₂O₃ (\>99% pure) and iron oxide (\>96% pure) as valuable products [@dutta2016global]. The selective chlorination of REEs to RECls enables separation from iron, which remains as oxide under appropriate conditions.

A particularly promising development is the flash Joule heating with chlorination (FJH-Cl₂) method, which achieves [@deng2022rare]:

- High purity: \>90% REE

- High yield: \>90% recovery

- Energy reduction: 87% compared to conventional hydrometallurgy

- GHG emission reduction: 84%

- Operating cost reduction: 54%

- Complete elimination of water and acid usage

### Other Secondary Sources
Carbochlorination has also been investigated for REE recovery from [@binnemans2017solvometallurgy]:

- Fluorescent lamp phosphors (primarily Y, Eu, Tb)

- Nickel-metal hydride batteries (La, Ce, Nd, Pr)

- Catalytic converters (La, Ce)

- {index}`Coal fly ash <coal fly ash>` and coal by-products

- Electronic waste (various REEs)

- Mining tailings and processing residues

The carbochlorination approach is particularly suitable for secondary sources with complex compositions, as the process does not require high-quality feedstock and can handle wide variations in composition [@tanaka2013recycling]. The cascade condensation system enables separation of different chlorides based on boiling point differences.

## Fluorination

### Direct Fluorination with HF
The conversion of rare earth oxides to fluorides is essential for molten salt electrolysis metal production. Direct fluorination with anhydrous hydrogen fluoride (AHF) is the industrial standard:

> RE₂O₃ + 6HF → 2REF₃ + 3H₂O

Process parameters for dry fluorination:

- Temperature: 600-700°C

- HF gas flow: 3-4 kg/h

- Theoretical HF amount: 100%

- Fluorination rate: \>99%

- Maximum temperature: 1223 K (950°C) for gas-phase fluorination

Neodymium trifluoride (NdF₃) production from neodymium carbonate monohydrate using AHF has been studied in Carberry spinning-basket reactors at 100-250°C. However, AHF is extremely dangerous, requiring extensive safety precautions and custom AHF-safe facilities.

### Solid-State Fluorination (NH₄HF₂, ZnF₂, NaBF₄)
Alternative solid fluorinating agents offer safer handling compared to HF gas:

> Ammonium Bifluoride (NH₄HF₂):

NH₄HF₂ overcomes the hygroscopic disadvantages of NH₄F and is preferred for direct fluorination of RE oxides to obtain anhydrous oxygen-free fluorides. Additional fluorination at 600°C with argon and HF gas can produce rare earth fluorides with lower oxygen content. This method has been used for Nd₂O₃ and Y₂O₃ fluorination.

> ZnF₂ Fluorination:

Thermodynamic calculations demonstrate feasibility of fluorinating rare earths in NdFeB waste using ZnF₂. At 850°C, 90 minutes reaction time, and 100% ZnF₂ addition, the fluorination rate reaches 95.69%. ZnF₂, along with AlF₃ and FeF₃, acts as a strong fluorinating agent giving complete conversion of neodymium oxide to neodymium fluoride.

> NaBF₄ Fluorination:

Due to its high fluorine ratio, NaBF₄ has been selected for recovery of rare earth elements from NdFeB waste. When roasted at 600°C for 30 minutes with 65% NaBF₄, the fluorination rate reaches 95.83%. After acid leaching, the purity of mixed fluorinated rare earth products reaches 99.39%.

### Fluoride Molten Salt Systems
Fluoride molten salts serve dual purposes: as fluorinating media for oxide-to-fluoride conversion and as electrolytes for metal production. Fluoride additives including AlF₃, ZnF₂, and FeF₃ convert rare earth oxides to fluorides in molten salt systems, enabling subsequent electrochemical extraction.

Key advantages of fluoride systems include higher current efficiency compared to chloride systems. However, they require more energy due to higher decomposition potentials and produce perfluorocarbon (PFC) emissions when the "anode effect" occurs.

## Bromination and Iodination

### Rare Earth Bromide Synthesis
Lanthanide tribromides (LnBr₃) are typically synthesized through direct combination of rare earth metals with bromine or through ammonium bromide routes. The compounds are important precursors for organometallic synthesis and specialized applications.

Lanthanide tribromides form various complex compounds with alkali metals including M₃LnBr₆ (Ln = La, Pr, Nd, Sm, Gd, Tb, Ho, Tm; M = alkali metal), MLn₂Br₇ (Ln = Pr, Nd, Sm, Gd, Ho; M = Cs), and MLnBr₄ (Ln = Nd, M = Tl⁺). Heavier lanthanides produce more complex compositions in the melt.

Bromine in organic solvents (e.g., Br₂-EtOAc) can selectively separate metals from their oxides. This approach has been used for uranium separation and may have applications for REE recovery from mixed oxide sources.

### Rare Earth Iodide Preparation
Rare earth iodides are prepared through several methods:

- Direct combination of rare earth metals with iodine (most common)

- Reaction of rare earth metals with mercury iodide

- Direct reaction of lanthanide metal powders with 1.5 equiv iodine in THF at room temperature

- High-temperature synthesis (e.g., ScI₃ at 250°C in sealed silica ampoule)

Lanthanide triiodides LnI₃(THF)ₙ can be obtained by Soxhlet extraction of crude solids with THF. Crystal structures vary: early, larger lanthanides (La, Pr) form LnI₃(THF)₄ with pentagonal bipyramidal structure, while smaller lanthanides (Nd, Gd, Y) form LnI₃(THF)₃.₅ as solvent-separated ion pairs.

Europium uniquely forms the stable diiodide EuI₂ regardless of Eu:I ratio; EuI₃ is unknown. Rare earth iodides are hygroscopic and prone to hydrolysis, making direct preparation of anhydrous forms challenging.

### Metal Halide Exchange Reactions
To overcome disadvantages of traditional acid-based extraction, exchange reactions using alkali metal halides or magnesium halides have emerged as effective, simple, and eco-friendly processes for REE recovery.

Research on NdFeB magnet scrap recycling using magnesium halide salts shows the fluoride system is more efficient than the chloride system, achieving 98.64% extraction of Nd compared to 84.59% with chloride. The selective halogenation approach enables separation of REEs from transition metals based on reactivity differences.

(flash-joule-heating-with-chlorination)=
## Flash Joule Heating with Chlorination

Flash Joule heating (FJH) combined with chlorination (FJH-Cl₂) represents a breakthrough technology for rare earth recovery from end-of-life magnets, developed at Rice University and published in PNAS in September 2025.

Process mechanism:

- FJH rapidly raises material temperatures to thousands of degrees within milliseconds

- At \~1000°C, transition metals (Fe, Co) chlorinate and vaporize as FeCl₃, CoCl₂

- Rare earth oxides require \>1350°C to react with chlorine

- Temperature difference enables selective separation of non-REE elements

- REE oxides remain as \>90% pure product

Performance results compared to conventional hydrometallurgy:

- REE purity: \>90%

- REE yield: \>90%

- Energy reduction: 87%

- GHG emission reduction: 84%

- Operating cost reduction: 54%

- Water and acid elimination: 100%

- Processing time: Seconds vs hours for traditional methods

- By-products: Commercially valuable CoCl₂, FeCl₃

The technology has been licensed to Flash Metals USA, with commercial production planned for Q1 2026. The modular design enables small or large recycling units near electronic waste collection points, reducing shipping costs.

## Molten Salt Electrolysis and Electrowinning

### Molten Salt Electrolysis (MSE)
MSE is the dominant method for rare earth metal and alloy production in China [@yang2021recovery].

#### Advantages over Other Reduction Processes

- Lower temperature requirement: **427-870°C**
- Lower energy intensity
- Flexibility for batch or continuous processing
- Low water consumption
- Reduced hazardous waste

#### Electrolyte Systems

- **LiCl-LiF-GdF₃**: Optimal for gadolinium electro-purification
- **LiF-NaF-KF**: Evaluated for REE recovery
- **LiCl-KCl-RECl₃**: Common for electrodeposition studies

#### Challenges

- High energy consumption
- Corrosive environment
- Requires toxic HF for fluoride preparation
- Environmental impact from fluoride systems

### FFC Cambridge Process
A direct electrochemical reduction of solid metal oxides in molten salts:

- Developed by Chen et al.
- Applied to Gd, Tb, Dy, Er, and Ce
- Avoids the need for fluoride intermediates

### Room Temperature Ionic Liquid Electrochemistry
An alternative to high-temperature molten salt processes:

- Lower environmental impact
- Reduced energy consumption
- Still under development for industrial scale

### Fluoride-Based Electrolysis
Molten salt electrolysis is the most widely used method for producing light rare earth metals (La, Ce, Pr, Nd) and alloys in China. The process uses rare earth fluorides dissolved in fluoride-based electrolytes:

> REF₃ → RE³⁺ + 3e⁻ → RE(metal) at cathode
>
> Fluoride ions oxidized to F₂ gas at carbon anode

Optimal process parameters for Pr-Nd alloy production (25 kA cell):

- Molten salt composition: 90.91 wt% NdF₃, 9.09 wt% LiF, REO (25% Pr, 75% Nd)

- Electrolysis temperature: 1323 K (1050°C)

- Cathode current density: 7-12 A/cm²

- Product purity: Non-RE impurities \<0.05 wt%, carbon \<0.04 wt%

- Current efficiencies: Up to 83%

The technology is similar to aluminum electrolysis but operates at higher temperatures (\~1050°C) in closed steel cells under inert argon atmosphere with carbon ring anodes and tungsten or molybdenum cathodes.

### Chloride-Based Electrolysis
An alternative chloride-based molten salt electrolysis process has been developed that eliminates greenhouse gas emissions associated with conventional fluoride systems:

> RECl₃ (in LiCl-KCl eutectic) → RE(metal) + Cl₂(gas)

Technical performance of chloride-based process:

- Electrolyte: NdCl₃ (1.65 M) in LiCl-KCl eutectic (45:55 wt%)

- Anode: RuO₂-coated dimensionally stable anode (DSA)

- Coulombic efficiency: \>80%

- Specific energy consumption: 2.3 kWh/kg-Nd

- Product purity: \>97 wt%

- GWP reduction: 44-69% compared to conventional process (5 vs 9-16 kg CO₂-eq)

The chloride process produces reusable chlorine gas rather than CO₂ and eliminates perfluorocarbon (PFC) emissions entirely. The lower operating temperature also enables use of less expensive materials of construction.

### Environmental Considerations
Conventional neodymium electrowinning in oxyfluoride molten salts using consumable graphite anodes generates significant greenhouse gases:

- Carbon dioxide from anode consumption

- Perfluorocarbons (CF₄, C₂F₆) during "anode effect"

- CF₄ has global warming potential 6,500× CO₂

- C₂F₆ has global warming potential 9,200× CO₂

- PFC production disrupts current density and metal production

Life cycle analysis shows the chloride-based approach significantly reduces environmental impact. The chloride process represents a sustainable pathway for rare earth metal production aligned with decarbonization goals.

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

Technical advantages of carbochlorination include [@paulick2017global]:

- Production of anhydrous REE chlorides directly suitable for molten salt electrolysis

- Elimination of dehydration steps required when using aqueous methods

- Lower activation energies enabling faster reaction kinetics

- Potential for selective volatilization and separation of certain elements

- Compatibility with integrated chlorometallurgical operations (Ti, Zr production)

Technical limitations include:

- Less established separation methods compared to {index}`solvent extraction`

- Chlorine gas handling requirements

- Higher temperature operation than aqueous methods

- Limited selectivity for individual REE separation without additional processing

### Environmental Impact
| **Environmental Factor** | **Carbochlorination** | **Conventional Methods** |
|----|----|----|
| Wastewater Generation | Minimal (water wash only) | Significant (acid/alkali effluents) |
| Acid/Alkali Consumption | None | High (recycling possible) |
| Gaseous Emissions | CO/CO₂, excess Cl₂ (recyclable) | HF, SO₂, NOx from roasting |
| Solid Waste | Reduced (chlorides are soluble) | Precipitation sludges |
| Energy Intensity | Moderate (1.4-2.2 GJ/t RECl) | Variable (process dependent) |
| Radioactive Waste | Concentrated ThCl₄ stream | Dispersed in waste streams |

Carbochlorination is characterized as a "clean metallurgical technology" due to [@weber2012rare]:

- Elimination of acid/alkali wastewater streams

- Ability to recycle excess chlorine within the system

- Reduced pollutant discharge compared to conventional processes

- Short-process characteristic avoiding generation of secondary waste

- Potential for recovery of byproducts (HF from bastnaesite, P₂O₅ from phosphates)

However, conventional rare earth processing has significant environmental impacts that carbochlorination could help mitigate. Traditional processes generate large quantities of hazardous waste, require extensive water resources, and produce radioactive residues that pose health and environmental risks [@banda2015separation].

### Economic Considerations
Economic comparison between carbochlorination and conventional methods must consider [@bailey2017sustainability]:

- Capital Costs: Carbochlorination requires specialized chlorine-resistant equipment but potentially simpler overall flowsheets compared to multi-stage hydrometallurgical plants

- Operating Costs: Reduced reagent costs (no acids/alkalis) but higher energy costs for heating

- Reagent Recycling: Chlorine can be recovered and recycled, reducing ongoing chemical costs

- Product Value: Anhydrous chlorides may command premium prices for certain applications

- Scale Dependencies: Minimum economic scale estimated at 5,000-10,000 tonnes/year REO for concentrate production; 10,000-20,000 tonnes/year for full processing

The "short-process" characteristic of carbochlorination---single chlorination step followed by water washing---offers potential for reduced capital investment compared to conventional multi-stage processing. However, detailed {index}`techno-economic <techno-economic analysis (TEA)>` analyses comparing industrial-scale carbochlorination to established hydrometallurgical routes remain limited in the open literature [@peck2015critical].

Comparison of REE extraction and processing technologies:

| **Technology** | **TRL** | **Recovery (%)** | **Energy Intensity** | **Environmental Impact** | **Scale** |
|----|----|----|----|----|----|
| Hydrometallurgy | 9 | 90-99 | Moderate | High (acid waste) | Industrial |
| Carbochlorination | 7-8 | \>93 | Moderate | Low (dry process) | Pilot-Demo |
| Fluoride MSE | 9 | 80-90 | High | Moderate (PFCs) | Industrial |
| Chloride MSE | 6-7 | \>80 | Low | Low (no PFCs) | Demo |
| FJH-Cl₂ | 5-6 | \>90 | Very Low | Very Low | Pilot |
| Supercritical CO₂ | 5-6 | 70-98 | Moderate | Very Low | Lab-Pilot |
| Bioleaching | 4-5 | \>80 | Very Low | Very Low | Lab |
| DES/Ionic Liquids | 4-5 | High | Low | Low | Lab |

Key observations from comparative analysis:

- Hydrometallurgy remains the dominant industrial technology despite environmental concerns

- Carbochlorination offers a cleaner alternative with proven industrial precedent (Ti, Zr)

- Fluoride molten salt electrolysis is mature but faces PFC emission challenges

- Chloride-based electrolysis shows promise for sustainable metal production

- Emerging technologies (FJH, scCO₂, {index}`bioleaching`) offer significant sustainability benefits

- Technology selection depends on feedstock, scale, environmental regulations, and economics

- Integrated process chains combining multiple technologies may be optimal

## Industrial Implementation

### Technology Readiness Level
The technology readiness level (TRL) for rare earth carbochlorination varies by region and application [@nassar2015criticality]:

- China: TRL 7-8 (Demonstrated in operational environment, pilot-to-commercial scale at Baotou and other facilities)

- Rest of World: TRL 6-7 (Pilot plant demonstration, not yet commercially deployed)

- Recycling applications: TRL 5-6 (Technology validated in relevant environment)

Chinese industrial processes for bastnaesite include the chlorination process as one of several established methods, alongside oxidation roasting-acid leaching, sulfuric acid bake-water leaching, and caustic soda decomposition [@csiro2024minerals]. At the Baotou processing facilities, chlorides are produced alongside oxides, carbonates, and alloy products.

### Scale-Up Challenges
Key challenges for industrial-scale implementation include [@vital2023nechalacho]:

- Fluidized Bed Reactor Design: Complex gas-solid interactions require careful modeling and control. Dead zones and non-uniform fluidization can affect conversion efficiency.

- Material Handling: Prevention of raw material splashing through pelletization with binders and reducing agents.

- Chlorine Management: Safe handling, distribution, and recycling of chlorine gas at industrial scale.

- Corrosion Control: Development of materials resistant to high-temperature chlorine environments.

- Heat Integration: Efficient recovery and utilization of reaction heat.

- Product Separation: Design of cascade condensation systems for separating different chloride products.

- Expertise Gap: Limited technical know-how for rare earth chlorination outside China after decades of offshoring.

Reference to the titanium industry provides valuable lessons, as carbochlorination of rutile/ilmenite to produce TiCl₄ has been practiced commercially for decades [@doe2022report]. The Kroll process for titanium uses similar principles, and development of analogous compact distillation apparatus for REE separation has been proposed.

### Equipment and Safety Considerations
Industrial implementation requires [@habib2014exploring]:

- Chlorination Reactor: Fluidized bed or packed bed reactor with temperature control (600-900°C)

- Gas Distribution System: For controlled chlorine introduction

- Condensation Train: Cascade system for separating products by boiling point

- Off-Gas Treatment: For capturing excess chlorine and volatile byproducts

- Water Leaching System: For dissolving water-soluble REE chlorides

- Corrosion-Resistant Materials: Refractory linings, special alloys for chlorine service

- Safety Systems: Chlorine detection, emergency scrubbing, personnel protection

Operating temperatures of 600-900°C, while elevated, are significantly lower than the \>1200°C required for traditional high-temperature roasting, reducing equipment wear and energy consumption [@iaea2011radiation]. This also expands the range of materials suitable for reactor construction.

## Industrial Precedents: Titanium, Zirconium, Aluminium, Magnesium, and Niobium-Tantalum

Carbochlorination has been practiced at massive industrial scale for decades in the production of titanium and nuclear-grade zirconium. These established industries provide invaluable precedent, proven technology, and potential synergies for rare earth element processing. The infrastructure, expertise, and equipment developed for Ti and Zr chloride production represent a foundation upon which REE carbochlorination could be built [@commission2020critical].

### Titanium Production via Carbochlorination
The titanium industry represents the largest and most mature application of carbochlorination. Roughly half of global TiO₂ pigment production goes through the chloride process, which relies on carbochlorination as its first step [@usgs2020titanium].

> The Chloride Process for TiO₂/Ti Metal:

The process begins with carbochlorination of titanium ores (rutile or upgraded ilmenite) in fluidized bed reactors at 900-1050°C [@fmi2024titanium]:

> TiO₂ + 2C + 2Cl₂ → TiCl₄ + 2CO

Key industrial parameters include:

- Temperature: 900-1050°C in fluidized bed reactors

- Feedstock: Rutile (\>95% TiO₂) or synthetic rutile/upgraded ilmenite slag (\>90% TiO₂)

- Reductant: Petroleum coke or anthracite coal

- Product: TiCl₄ (liquid, boiling point 136°C)

- Scale: Major plants produce hundreds of thousands of tonnes of TiCl₄ annually

- Energy efficiency: Optimized to \~500 × 10³ kcal per tonne TiCl₄ (down from 1,560 × 10³ kcal historically)

> Purification and Metal Production:

The crude TiCl₄ contains impurities including FeCl₃, AlCl₃, VOCl₃, SnCl₄, and SiCl₄. These are removed through a combination of [@roine2019hsc]:

- Selective condensation (FeCl₃, AlCl₃ have different boiling points)

- Chemical treatment with H₂S to convert VOCl₃ to higher-boiling VCl₄

- Multi-stage fractional distillation to achieve \>99.98% purity

- The purified TiCl₄ is reduced to titanium metal via the Kroll process (Mg reduction) or Hunter process (Na reduction)

> Major Global Producers:

The titanium chloride industry is dominated by major multinational corporations with decades of operational experience [@britannica2024titanium]:

- Chemours (USA) - Major TiO₂ and TiCl₄ producer

- Tronox (USA/Global) - Vertically integrated Ti operations

- Lomon Billions (China) - \~660 kt/year chloride TiO₂ capacity

- Venator Materials (Global) - Significant chloride process capacity

- Kronos Worldwide (Global) - Major TiO₂ producer

The titanium industry demonstrates that carbochlorination can be operated safely and economically at very large scale, with continuous improvements in energy efficiency, chlorine recycling, and environmental performance over seven decades of industrial operation [@lomon2024titanium].

### The Zr/Hf Separation Challenge
Zirconium is an ideal material for nuclear reactor fuel cladding due to its exceptionally low thermal neutron absorption cross-section. However, zirconium ores (primarily zircon sand, ZrSiO₄) naturally contain 1-3 wt% hafnium, which has a very high neutron absorption cross-section [@usgs2020titanium]. For nuclear applications, the hafnium content must be reduced to less than 100 ppm---a challenging separation given the remarkable chemical similarity between Zr and Hf (same group, nearly identical ionic radii).

This separation challenge parallels the difficulties in separating individual rare earth elements, which also exhibit very similar chemical properties across the lanthanide series. The industrial solutions developed for Zr/Hf separation therefore offer instructive lessons for REE processing [@xu2015production].

### Industrial Zr Carbochlorination Process
The production of nuclear-grade zirconium begins with carbochlorination of zircon sand. The process is conducted in fluidized bed reactors at temperatures of 1000-1200°C [@konings2010thermodynamic]:

> ZrSiO₄ + 4C + 4Cl₂ → ZrCl₄ + SiCl₄ + 4CO

Key process characteristics include:

- Temperature: 1000-1200°C in fluidized bed reactors

- Feedstock: Zircon sand mixed with petroleum coke or graphite

- Products: Mixed ZrCl₄/HfCl₄ vapor (sublimation point \~331°C) plus volatile SiCl₄

- Scale: Industrial plants produce several tonnes of crude ZrCl₄ per day

- The ZrCl₄/HfCl₄ mixture is condensed as a solid powder for subsequent separation

This carbochlorination step has been optimized over decades of industrial operation, with well-established practices for reactor design, chlorine distribution, heat management, and product recovery [@yang2016separation].

### Molten Salt Extractive Distillation for Zr/Hf
Following carbochlorination, the separation of ZrCl₄ from HfCl₄ is accomplished through molten salt extractive distillation---the only pyrometallurgical Zr/Hf separation method operating at industrial scale [@yin2024preparation]. This technology, developed by Cezus (now Framatome) in France during the 1980s, exploits the slight difference in vapor pressure between ZrCl₄ and HfCl₄.

The process uses a distillation column with multiple plates, each containing a layer of molten salt (typically KAlCl₄). The mixed ZrCl₄/HfCl₄ vapor from carbochlorination is introduced into the column, and selective absorption/desorption in the molten salt achieves separation [@chen2025process]. Key parameters include:

- Molten salt system: KAlCl₄ or similar alkali metal chloroaluminates

- Column design: 12+ stage sieve plate columns

- Separation efficiency: Produces ZrCl₄ with \<100 ppm Hf and HfCl₄ with \>96% purity

- The purified ZrCl₄ is then reduced to zirconium metal via the Kroll process (magnesiothermic reduction)

### Lessons and Synergies for REE Processing
The established Ti and Zr/Hf carbochlorination industries offer several important lessons and potential synergies for rare earth element processing [@chen2025process]:

> Technology Transfer Opportunities:

- Fluidized bed reactor design and operation at 1000°C+ with chlorine atmospheres

- Materials of construction resistant to high-temperature chlorine corrosion

- Chloride condensation and handling systems for subliming metal chlorides

- Chlorine recycling and off-gas treatment systems

- Safety protocols for large-scale chlorine operations

> Potential for Integrated Operations:

Facilities already operating carbochlorination for titanium (TiCl₄ production) or zirconium could potentially integrate rare earth chloride production with relatively modest additional investment. Shared infrastructure would include [@nfc2023nuclear]:

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
Anhydrous aluminum chloride (AlCl₃) production via carbochlorination represents another important industrial precedent. First demonstrated by Hans Christian Oersted in 1825, the process has been refined into a mature industrial technology [@wikipedia2024aluminium]. The carbochlorination of alumina follows the reaction:

> Al₂O₃ + 3C + 3Cl₂ → 2AlCl₃ + 3CO

Key process characteristics include:

- Temperature: 500-700°C in fluidized bed reactors

- Exothermic reaction (\~300 kJ/mol AlCl₃) enabling self-sustaining operation

- No external heating required once reaction is initiated

- Feedstock: γ-alumina with finely divided carbon (petroleum coke)

- Product: AlCl₃ vapor condensed as solid (sublimation point \~180°C)

> Industrial Applications:

The aluminum chloride process has garnered renewed interest as a potential alternative to the Hall-Héroult process for primary aluminum production. Research by SINTEF (Norway) and the Gharda Scientific Research Foundation (India) has demonstrated [@wikipedia2024aluminium]:

- Bauxite can be carbochlorinated directly, producing mixed chlorides (AlCl₃, FeCl₃, SiCl₄, TiCl₄)

- Energy savings of 25-30% compared to Hall-Héroult electrolysis

- Easier CO₂ capture and sequestration potential

- Biocarbon can replace petroleum coke (no mechanical strength requirements)

- AlCl₃ is subsequently electrolyzed to produce aluminum metal

> Relevance to REE Recycling:

The aluminum chloride process is particularly relevant to REE recycling from aluminum-containing secondary sources. End-of-life materials containing both aluminum and rare earths (e.g., certain catalysts, electronics) could potentially be processed through integrated carbochlorination, enabling simultaneous recovery of both Al and REE values [@engell2023could].

### Magnesium Production via Chlorination
Magnesium production via the chloride route has a long industrial history, with carbochlorination serving as an important alternative to the Dow process for producing anhydrous MgCl₂ feedstock for electrolysis [@namboothiri2017bauxite]. The carbochlorination reaction is:

> MgO + C + Cl₂ → MgCl₂ + CO

Thermogravimetric studies have characterized the carbochlorination of MgO [@gupta2003chemical]:

- Optimal temperature range: 500-675°C (conversion decreases above 700°C due to MgCl₂ melting)

- Activation energy: 49 kJ/mol (between 425-600°C)

- Optimal Cl₂/CO molar ratio: approximately 0.6

- Maximum conversion: 82% at 675°C

- Carbon presence enhances MgO conversion by up to 49%

> Historical Industrial Implementation:

Carbochlorination of magnesium oxide from magnesite, silicates, or hydroxides was practiced industrially at several facilities [@gaballah1999chlorination]:

- IG Farben process (Germany, pre-WWII)

- Basic Magnesium plant (Henderson, Nevada, WWII era)

- Norsk Hydro (Norway, 1950-1987)

- The Dow process (still operational) uses a different approach with seawater-derived Mg(OH)₂

> Integration with Titanium/Zirconium Production:

Magnesium and chlorine are intimately linked with titanium and zirconium production through the Kroll process, which uses magnesium to reduce TiCl₄ and ZrCl₄ to metals, producing MgCl₂ as a byproduct. This MgCl₂ is electrolyzed to regenerate magnesium and chlorine, creating a closed-loop system. REE carbochlorination could potentially integrate into this existing infrastructure [@britannica2024magnesium].

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

- Distillation produces NbCl₅ with \<5 mg/L Ta contamination

- Other metallic impurities reduced to 1-2 mg/L

- Chlorides can be hydrolyzed to hydroxides and calcined to high-purity oxides

> Lessons for REE Processing:

The Nb/Ta separation precedent is particularly instructive for REE processing because it demonstrates successful industrial separation of chemically similar elements via chloride distillation. While REE separation is more complex (17 elements vs. 2), the fundamental principle of exploiting vapor pressure differences among chlorides is directly applicable. The development of cascade distillation systems for REE chloride separation could build on this established technology base [@tic2024processing].

> Summary of Industrial Carbochlorination Precedents:

| **Parameter** | **Titanium** | **Zirconium** | **Aluminum** | **Magnesium** | **Nb/Ta** | **REE (Potential)** |
|----|----|----|----|----|----|----|
| Global Scale | 280 Mt TiCl₄/yr | Thousands t/yr | Large scale | Historical | Specialty | To be developed |
| Temperature | 900-1050°C | 1000-1200°C | 500-700°C | 500-675°C | 500-1000°C | 600-900°C |
| TRL | 9 (Commercial) | 9 (Commercial) | 7-8 (Demo) | 7 (Historical) | 7-8 (Specialty) | 6-7 (Pilot) |
| Key Driver | Pigments, aerospace | Nuclear | Alt. Al route | Metal production | Electronics | Clean energy |
| Separation | Distillation | Molten salt | Condensation | Electrolysis | Distillation | Multiple |

(outlook)=
## Outlook

This comprehensive review demonstrates that carbochlorination is a thermodynamically viable and technically promising process for converting all 17 rare earth element oxides to their corresponding chlorides at industrial scale. Key conclusions include:

1.  Universal Applicability: The carbochlorination reaction is thermodynamically favorable for all REEs across the lanthanide series plus scandium and yttrium at temperatures of 600-900°C.

2.  Demonstrated Performance: Laboratory and pilot studies have achieved \>93% conversion rates for light rare earths (Ce, Nd) with kinetics controlled by chemical reaction rather than diffusion.

3.  Primary and Secondary Sources: The process is applicable to both primary mineral concentrates (bastnaesite, monazite, xenotime) and secondary/recycled materials (NdFeB magnets, phosphors).

4.  Environmental Advantages: Carbochlorination eliminates acid/alkali wastewater generation and enables recycling of chlorine, offering a cleaner alternative to conventional hydrometallurgy.

5.  Technology Readiness: While commercially practiced in China, broader industrial deployment requires advancement from current TRL 6-7 to full commercial scale (TRL 9).

6.  Integration Potential: The process is particularly attractive for integrated chlorometallurgical operations already handling chlorine for titanium or zirconium production.

Future research and development priorities include:

- Detailed techno-economic analysis comparing carbochlorination to established routes

- Development of selective separation methods for individual REE chlorides

- Scale-up of flash Joule heating combined with chlorination for recycling

- Optimization of fluorine management for bastnaesite processing

- Investigation of integrated carbochlorination-electrowinning processes

- Development of corrosion-resistant materials for long-term industrial operation

Carbochlorination represents an important technological option for addressing the growing global demand for rare earth elements while potentially reducing the environmental footprint of REE production. Its successful industrial implementation outside China will require sustained investment in research, development, and demonstration activities, along with rebuilding of technical expertise that has been lost during decades of REE supply chain offshoring.

This comprehensive review of carbohalogenation processes and complementary technologies for rare earth element processing reveals a diverse portfolio of options at various stages of development. Key conclusions include:

1\. Halogenation provides multiple pathways for REE processing: chlorination is most industrially mature, fluorination is essential for metal production, bromination and iodination serve specialized synthesis applications.

2\. Carbochlorination (RE₂O₃ + C + Cl₂ → RECl₃ + CO) offers significant advantages over direct halogenation: lower temperatures (600-900°C), thermodynamic favorability, and high conversion rates (\>93%). The process is validated by decades of Ti and Zr production.

3\. Fluorination processes are critical for producing anhydrous REF₃ for molten salt electrolysis. Solid fluorinating agents (NH₄HF₂, ZnF₂, NaBF₄) offer safer alternatives to hazardous HF gas.

4\. Hydrometallurgy remains the dominant industrial technology. Solvent extraction with {index}`D2EHPA`, {index}`PC88A`, and Cyanex extractants achieves \~99% recovery but generates significant acidic wastewater.

5\. Molten salt electrolysis is the primary route to REE metals. Chloride-based processes offer 44-69% reduction in global warming potential compared to conventional fluoride systems.

6\. Emerging technologies show transformative potential: Flash Joule heating with chlorination reduces energy consumption by 87%, supercritical CO₂ extraction minimizes waste generation, and bioleaching operates under ambient conditions without harsh chemicals.

7\. {index}`Ionic liquids <ionic liquids>` and {index}`deep eutectic solvents <deep eutectic solvent>` demonstrate excellent laboratory performance but face significant challenges for industrial scale-up including viscosity and stability.

> Future research priorities:

- Scale-up of carbochlorination for REE ores and recycled materials

- Development of chloride-based molten salt electrolysis at commercial scale

- Commercialization of flash Joule heating technology for magnet recycling

- Optimization of supercritical CO₂ extraction for various REE feedstocks

- Acceleration of bioleaching kinetics through synthetic biology

- Development of low-viscosity ionic liquids and DES for industrial application

- Integration of multiple technologies into optimized process chains

- Rebuilding REE processing expertise outside China

- {index}`Life cycle assessment <life cycle assessment>` comparing all available technologies

The rare earth industry stands at an inflection point, driven by clean energy demands, supply chain security concerns, and environmental sustainability requirements. The portfolio of halogenation, hydrometallurgical, and electrochemical technologies reviewed here provides multiple pathways to address these challenges. Success will require sustained investment in research, development, and demonstration, along with supportive policy frameworks for technology deployment.
