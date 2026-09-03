# Motivating question (Don)

I think the use of clays initiates these responses: \"where are these clays mined, how are they processed, can they be procured in the open market place, what are their basic chemistries that lead to their function, are they recyclable... etc\"?? Apparently, their use introduce production yield and other ChE issues.

This report answers those questions, then assesses the state of the art, research opportunities, and environmental implications. It is grounded in the thermodynamic-screening paper that prompted the discussion citep:mohamadsobri2025 and in the broader ion-adsorption-clay literature citep:borst2020,zhou2020,moldoveanu2016,luo2022,wu2023,alshameri2019. Sources are also distilled in the project Crucible knowledge base (`concepts/ion-adsorption-clays.org`{.verbatim}, `concepts/clay-ion-exchange-separation.org`{.verbatim}).

# Executive summary

- Ion-adsorption clays (IAC) -- also \"ion-adsorption deposits,\" \"regolith-hosted REE deposits,\" or \"weathered-crust elution-deposited ores\" -- are the dominant global source of the **heavy** rare earths (Dy, Tb, Y). Their value is that the REE are held as loosely bound, hydrated, **exchangeable** ions on clay surfaces, so they can be recovered by a simple salt solution at room temperature -- no roasting or strong-acid cracking citep:borst2020.
- The clay is **not** an open-market commodity: it is low-grade, processed near-source, and supply is dominated by China and Myanmar. The host minerals (kaolinite, halloysite) are cheap industrial clays, but those are sold **without** the adsorbed REE.
- The chemical-engineering pain is dilute, high-volume hydrometallurgy with impurity co-extraction (Al, Fe), speciation/precipitation yield losses, and reagent-driven pollution. The Sobri paper is one response: use thermodynamics to pick a reagent (MgSO4) and conditions (ambient, acidic) that keep REE soluble citep:mohamadsobri2025.
- The most interesting forward direction is to use **clay/ion exchange itself as a separation technology** -- as a preconcentrator ahead of solvent extraction, and (with imported selectivity) as a partial replacement for it.
- The headline environmental issue is ammonia-nitrogen pollution from in-situ ammonium-sulfate leaching, plus landscape destruction and a large spent-clay residue stream whose fate (reuse vs landfill) is unresolved.

# What the clays are and the chemistry that makes them work

REEs in these ores sit primarily in the **ion-exchangeable** phase, typically \~60-90% of total REE content, adsorbed on clay minerals -- chiefly kaolinite and halloysite, with contributions from illite, smectite, and Fe-oxyhydroxides. Synchrotron spectroscopy shows the REE are held as 8- to 9-coordinated **outer-sphere hydrated complexes** on kaolinite: weak, electrostatic, with the hydration shell intact and not bound into a mineral lattice citep:borst2020.

The clay surface carries net negative charge (isomorphic substitution plus pH-dependent broken-edge silanol/aluminol sites). Recovery is therefore **cation exchange** driven by mass action -- a more concentrated electrolyte cation displaces the loosely held REE3+:

``` example
2 Clay-REE + 3 M2SO4  ->  2 Clay-M3 + REE2(SO4)3      (M = NH4+, ½ Mg2+, ...)
```

Because the REE is exchangeable and hydrated, a salt solution at ambient temperature liberates it with fast kinetics and no acid attack on the mineral citep:borst2020,moldoveanu2016. This is the entire economic basis of the deposit type, and what distinguishes it from hard-rock bastnaesite/monazite.

A crucial subtlety for everything downstream: REE attach to clay by **two mechanisms with opposite consequences** citep:wu2023:

- **Ion exchange** (outer-sphere) -- dominant, but **cannot fractionate** the REE; it grabs the whole REE block without discriminating among adjacent lanthanides.
- **Surface complexation** (inner-sphere, at edge sites) -- **does** fractionate, enriching HREE over LREE.

# Where they are mined, how they are processed, and market availability

## Formation and geography

IAC form by deep chemical weathering of REE-bearing parent rocks (mostly felsic granites; some mafic-ultramafic for Sc) in warm, humid, subtropical climates. REE liberated from primary minerals migrate down the regolith and re-adsorb onto clays; as weathering advances, kaolinite converts to halloysite, lowering adsorption capacity and producing vertical zonation citep:zhou2020.

- **Southern China** (Jiangxi/Ganzhou-Longnan, Guangdong, Fujian, Hunan, Guangxi): historic and dominant producer.
- **Myanmar**: now a very large supplier of HREE-bearing ore/concentrate feeding Chinese separation plants.
- **Emerging/exploration**: Madagascar (mineralogically genuine analogues of the Chinese ores citep:borst2020), plus Brazil, Malaysia, Laos, Vietnam, Tanzania.

Regolith-hosted deposits supply **over 90% of global heavy-REE production** despite low grade (commonly \~0.03-0.3 wt% total REO); the economics come from the cheap extraction and from geologic pre-concentration, not from grade citep:zhou2020.

## Processing chain

1.  **Leaching**: historically heap/tank leaching of excavated ore; now predominantly **in-situ leaching** -- ammonium sulfate (or magnesium sulfate) solution injected into the orebody, pregnant leach solution collected.
2.  **Purification**: impurity removal (Al, Fe) from the pregnant solution.
3.  **Precipitation**: REE recovered as carbonate or oxalate, then calcined to mixed oxide.
4.  **Separation**: individual elements separated downstream, conventionally by solvent extraction.

The general envelope -- ambient temperature, fast kinetics, salt-driven -- holds across ores of varying origin citep:moldoveanu2016.

## Can they be procured on the open market?

Largely **no**. The ore is low-grade, processed near-source, and subject to Chinese export and technology restrictions, with Myanmar ore feeding Chinese supply chains. What trades openly are the downstream **separated REE oxides**. A common point of confusion: kaolinite and halloysite are cheap, widely sold industrial clays, but the commercial product is purified clay **without** adsorbed REE -- not a substitute for the ore.

# State of the art

## Reagent and condition selection (the Sobri paper in context)

The paper that prompted this report is a purely **thermodynamic** (Eh-pH / Pourbaix) screening study, not an experimental one citep:mohamadsobri2025. Using HSC Chemistry 10.0 it computes the stability fields of La, Nd, and Y in three sulfate leaching solutions over 0.05-0.6 M and 25-80 degrees C, asking which conditions keep the freed REE soluble as REE3+ rather than precipitating or complexing.

| Leaching solution | Behavior across concentration | Verdict |
|----|----|----|
| (NH4)2SO4 | Good when dilute; \>\~0.25-0.3 M, nitrate from nitrification forms LaNO3(2+)/NdNO3(2+) | Degrades |
| MgSO4 | Maximum stability for La, Nd, Y at **all** 0.05-0.6 M; no unwanted species | **Best** |
| Al2(SO4)3 | SO4(2-) forms LaSO4+ and hydrated Nd2(SO4)3.8H2O | Degrades |

Stability falls as temperature rises (25 -\> 80 degrees C), so ambient leaching is optimal; the REE3+ stability order is La \> Nd \> Y, with acidic windows La (pH 0-5.8), Nd (0-5), Y (0-4.2). The modeled MgSO4-at-ambient conclusion agrees with experiment citep:pan2024,shi2022, which is what lends the screening credibility. **Limitation**: single element, single solvent, no impurities, no kinetics -- a prediction tool, not validation.

## Reagent substitution and impurity control

The field is actively moving off ammonium sulfate. Magnesium sulfate gives comparable recovery with far less nitrogen pollution citep:pan2024; low-ammonium column leaching keeps recovery \>90% at much reduced reagent loads citep:shi2022; and selective inhibitors (e.g., HMTA) suppress aluminum co-dissolution to cut the downstream impurity burden citep:he2025. \"Ammonium-free extraction\" and whole-process precipitation are explicit research directions for \"green efficient development\" citep:luo2022.

## Clay ion exchange as a separation technology

Beyond primary leaching, clay/IX can act as a **separation** unit operation. Its competitiveness depends entirely on the job:

- **Group separation / preconcentration** (pull REE-as-a-block out of a dilute, dirty stream; reject Na/K/Ca/Mg/Al/Fe): driven by **charge** selectivity -- strong. Natural clays are explicitly proposed as adsorbents/recovery media for REE from solution citep:alshameri2019.
- **Individual-element separation** (resolve adjacent lanthanides): bare clay is intrinsically weak (adjacent separation factors \~1.0-1.3 vs \~1.5-4 per stage for tailored solvent-extraction reagents). Adjacent selectivity must be **imported** -- from surface-complexation sites citep:wu2023, a complexing eluent, or a grafted ligand.

The proof-of-concept is the orebody itself: the regolith is vertically fractionated (LREE/HREE zonation, Ce anomalies) by clay loading plus carbonate-complexing groundwater acting as a mobile phase -- clay ion-exchange chromatography run over geologic time citep:zhou2020. Feasibility is settled; throughput and control are the engineering questions.

A scorecard versus solvent extraction (SX):

| Task | Clay / ion exchange | Solvent extraction |
|----|----|----|
| Adjacent-element purity at scale | weak (needs ligand) | **incumbent** |
| Group / matrix separation | **strong** | moderate |
| Dilute feeds (mine water, recycle, ash) | **strong** | weak |
| Preconcentration | **strong** | weak |
| HSE footprint (no diluent/crud/VOC) | **strong** | weak |
| Throughput, bulk individual separation | weak (unless SMB) | **strong** |
| Capacity / kinetics | clay-dependent | strong |

# Research opportunities

1.  **Clay as a preconcentrator ahead of SX (strongest near-term).** Load dilute leachate, reject monovalent/divalent matrix ions by charge selectivity, strip a 10-100x concentrated, de-salted REE eluate into a much smaller SX plant or direct precipitation. Directly attacks the dilute, high-volume penalty citep:alshameri2019,moldoveanu2016.
2.  **LREE/HREE rough cut.** Exploit the surface-complexation HREE-over-LREE enrichment citep:wu2023 for a binary roughing split -- apt because IAC feeds are already HREE-enriched.
3.  **Functionalized clay = extraction chromatography on a cheap support.** Graft an SX-grade ligand (phosphonic acid; a diglycolamide such as TODGA/DMDODGA) onto clay to combine \"the selectivity of SX with the convenience of column IX.\" This is demonstrated on porous supports with diglycolamide extractants as a cleaner alternative to liquid-liquid SX citep:momen2019; clay is the cheap, benign support variant.
4.  **Continuous chromatography (simulated moving bed).** Batch single-column operation is what costs chromatography its throughput; SMB makes it counter-current and continuous (as it is industrially for sugars and enantiomers). A title search of the REE literature for \"simulated moving bed\" returns essentially nothing -- a genuine white space.
5.  **Synthetic / engineered clay analogues.** Technically feasible (synthetic smectites, pillared clays, LDHs have high exchange capacity), but the value of a natural **deposit** is the geologic pre-concentration onto already-mined regolith citep:zhou2020; synthesizing and then loading from a dilute stream inverts that economy. The realistic role is selective **polishing/concentration** of leachates and effluents, not a synthetic orebody.
6.  **Experimental validation of thermodynamic screening.** Extend Pourbaix-style models to multi-element, impurity-bearing systems with kinetics, and validate against column data citep:mohamadsobri2025.
7.  **Measured separation factors** on smectite/vermiculite vs kaolinite, and how far edge-site density, pH, and ionic strength can push adjacent-REE selectivity citep:wu2023.

# Environmental implications

## Ammonia-nitrogen pollution (the headline issue)

In-situ ammonium-sulfate leaching discharges ammonia-nitrogen into groundwater and surface water -- the dominant environmental liability of Chinese IAC mining. This is the principal driver of the move to magnesium-sulfate and ammonium-free leaching citep:pan2024,shi2022,luo2022. Reduced-concentration leaching cuts the nitrogen load but needs longer times and larger solution volumes citep:shi2022.

### Precedent: ammonia at the Moab UMTRA site

A sobering precedent for what residual process ammonia costs comes from uranium, not rare earths. The Moab uranium mill tailings pile near Moab, Utah -- a \~16-million-ton pile on the bank of the Colorado River from the former Atlas Minerals mill -- is remediated by the U.S. Department of Energy under the Uranium Mill Tailings Radiation Control Act (a DOE UMTRA project, **not** a CERCLA Superfund site). Its two main **groundwater** contaminants of concern are **ammonia and uranium**, and ammonia is the dominant driver of the active groundwater remediation: it is acutely toxic to young-of-year endangered fish (razorback sucker, Colorado pikeminnow) in Colorado River backwaters. Since 2003 DOE has run a groundwater interim action (now 42 wells) that extracts contaminated groundwater and injects diverted river water to dilute the discharge; over the project life it has kept an estimated **1,002,109 lb of ammonia** versus **5,816 lb of uranium** out of the river -- ammonia outweighing uranium by \~170x

[^1][^2].

The ammonia is **process-reagent** ammonia: the mill precipitated uranium as ammonium diuranate (\"yellowcake\") using ammonia reagents, and residual ammonia held in tailings pore water has leached into the aquifer for decades -- the same root cause as ammonium-sulfate REE leaching, differing only in unit operation (milling vs leaching). If anything the REE case is harder to contain: Moab is a **point source** (one pile) that can be ringed with extraction wells, whereas in-situ REE leaching injects ammonium **directly into a hillside aquifer over large areas** with no engineered liner. Moab is thus the multi-decade, multi-million- pound, still-pumping illustration of the bill that ammonium hydrometallurgy can incur, and a concrete argument for the magnesium-sulfate / ammonium-free direction citep:pan2024,luo2022,mohamadsobri2025.

## Landscape destruction and slope failure

Excavation and in-situ leaching of weathered regolith cause deforestation, soil loss, and landslide risk; in-situ operations suffer uneven contacting and seepage/mass-transfer limits in low-permeability regolith, leaving REE behind and solution uncontrolled citep:luo2022.

## Reagent, energy, and yield footprint

Dilute, high-volume hydrometallurgy means large reagent and water inventories. Choosing reagent/pH/temperature to keep REE soluble (MgSO4, ambient, acidic) reduces precipitation yield losses and avoids the energy of external heating citep:mohamadsobri2025. Reagent recovery/recycle (ammonium or magnesium sulfate) and leachate recirculation onto fresh ore are central to both cost and pollution citep:moldoveanu2016,luo2022.

## Spent clay residue: reuse vs landfill (the recyclability question)

After leaching, the kaolinite/halloysite substrate survives intact (REE merely desorbs) -- it becomes depleted regolith, not a closed-loop recycled material. Its fate splits between **landfill** and **beneficial reuse** (land reclamation/ revegetation, construction fill, geopolymer/ceramic feedstock), and residue valorization is part of the green-development agenda citep:luo2022. **If landfill dominates, the environmental case weakens markedly** -- this is the weakest-sourced and most decision-relevant open question. By contrast, true REE **circularity** comes from end-products (NdFeB magnets, phosphors, e-waste) via urban mining, a separate stream.

## Spent-clay valorization routes

Because the spent clay is essentially a depleted aluminosilicate (kaolinite/ halloysite plus quartz), it is chemically similar to ordinary construction-clay feedstocks, and several beneficial-reuse routes have been demonstrated at lab/ pilot scale:

- **Geopolymer / alkali-activated binder (cement-like)** -- the best-developed route. Ion-adsorption REE tailings have been alkali-activated into geopolymer binders citep:zhang2022,hu2020. Notably, the motivation is as much **heavy-metal immobilization** as construction: the geopolymer locks contaminants into the matrix, so it doubles as waste stabilization. (This is effectively the metakaolin/pozzolan chemistry -- calcined kaolinite as a supplementary cementitious material.)
- **Glass-ceramics** -- tailings crystallized into diopside/anorthite glass-ceramic for building/decorative use citep:zhao2010.
- **Zeolite synthesis** -- the aluminosilicate residue converted to high- crystallinity Zeolite A, which then adsorbs pollutants in the mine\'s own water -- a closed-loop, treat-your-own-waste reuse citep:cheng2024.

Two routes that **do not** fit, despite the obvious analogy:

- **Asphalt**: clays are generally avoided as asphalt filler -- they are moisture-sensitive and promote stripping (binder-aggregate debonding).
- **Drywall**: drywall is gypsum (CaSO4.2H2O); the only link is the gypsum **byproduct** of sulfate leaching, not the clay residue itself.

The decisive practical caveat: the dominant modern method is **in-situ** leaching, in which the clay is never excavated -- so for those operations there is no solid residue stream to send to a kiln, and the real residue question is in-place **land reclamation and revegetation** citep:liu2022. Reusable tailings exist mainly for older heap/tank (excavated) operations, and even then residual reagent, Al, and occasional radioactivity must be managed, while low-value bulk materials do not travel far from remote mining regions. Net: valorization is real and locally attractive (especially for waste stabilization), but it is not yet a mainstream fate, and in-situ mining structurally limits how much residue is ever collectable.

## Net assessment

IAC are environmentally double-edged: extraction chemistry is mild (no roasting, no strong acid, low radioactivity), but the **process** footprint -- nitrogen pollution, landscape damage, dilute effluents, and a large residue stream -- is substantial. The research frontier (MgSO4/ammonium-free leaching, impurity control, preconcentration, residue valorization) is largely an effort to keep the mild chemistry while shrinking that footprint.

# References

Crucible cite keys in brackets; DOIs given for retrieval.

- \[borst2020\] Borst, Smith, Finch, et al. (2020). Adsorption of rare earth elements in regolith-hosted clay deposits. *Nature Communications*. <doi:10.1038/s41467-020-17801-5>
- \[moldoveanu2016\] Moldoveanu & Papangelakis (2016). An overview of rare-earth recovery by ion-exchange leaching from ion-adsorption clays of various origins. *Mineralogical Magazine*. <doi:10.1180/minmag.2016.080.051>
- \[zhou2020\] Zhou, Li, Wang, et al. (2020). The genesis of regolith-hosted REE and scandium deposits. *Chinese Science Bulletin*. <doi:10.1360/tb-2020-0350>
- \[luo2022\] Luo, Zhang, Zhou, et al. (2022). Review on the development and utilization of ionic rare earth ore. *Minerals*. <doi:10.3390/min12050554>
- \[wu2023\] Wu, Chen, Wang, et al. (2023). Review of REE adsorption on and desorption from clay minerals. *Ore Geology Reviews*. <doi:10.1016/j.oregeorev.2023.105446>
- \[alshameri2019\] Alshameri, He, Xin, et al. (2019). Understanding the role of natural clay minerals as effective adsorbents and alternative source of rare earth elements. *Hydrometallurgy*. <doi:10.1016/j.hydromet.2019.02.016>
- \[momen2019\] Momen, Healy, Tsouris, et al. (2019). Extraction chromatographic materials for clean hydrometallurgical separation of REE using diglycolamide extractants. *Industrial & Engineering Chemistry Research*. <doi:10.1021/acs.iecr.9b04528>
- \[mohamadsobri2025\] Mohamad Sobri, Harun & Mohd Yunus (2026). Enhancing rare earth elements stability in ion adsorption clays during ion-exchange leaching with salt solutions: a thermodynamic approach through Pourbaix diagrams. *Jurnal Teknologi* 88(1):41-51. <doi:10.11113/jurnalteknologi.v88.23169>
- \[pan2024\] Pan, Jiaxin, et al. (2025). Insights into selective leaching of rare earths from weathered crust elution-deposited rare earth ore using magnesium sulfate. *Journal of Rare Earths*. <doi:10.1016/j.jre.2024.04.025>
- \[shi2022\] Shi, Qiyuan, et al. (2022). Column leaching of ion adsorption rare earth ore at low ammonium concentration. *Journal of Materials Research and Technology*. <doi:10.1016/j.jmrt.2022.05.199>
- \[he2025\] He, Zhengyan, et al. (2025). Stepwise leaching rare earth from weathered crust elution-deposited rare earth ores by the inhibition leaching of aluminum with HMTA. *Environmental Science and Pollution Research* 32(25):15274-15286. <doi:10.1007/s11356-025-36598-8>
- \[zhang2022\] Zhang, Baifa, et al. (2022). Ion-adsorption type rare earth tailings for preparation of alkali-based geopolymer with capacity for heavy metals immobilization. *Cement and Concrete Composites*. <doi:10.1016/j.cemconcomp.2022.104768>
- \[hu2020\] Hu, Sixian, et al. (2020). Synthesis of rare earth tailing-based geopolymer for efficiently immobilizing heavy metals. *Construction and Building Materials*. <doi:10.1016/j.conbuildmat.2020.119273>
- \[zhao2010\] Zhao, Tuan, et al. (2010). The utilization of rare earth tailing for the production of glass-ceramics. *Materials Science and Engineering: B*. <doi:10.1016/j.mseb.2010.02.019>
- \[cheng2024\] Cheng, Jiancheng, et al. (2024). Synthesis of high-crystallinity Zeolite A from rare earth tailings: investigating adsorption performance on typical pollutants in rare earth mines. *Journal of Hazardous Materials*. <doi:10.1016/j.jhazmat.2024.133730>
- \[liu2022\] Liu, Chang, et al. (2022). Biogeochemical cycles of nutrients, rare earth elements (REEs) and Al in soil-plant system in ion-adsorption REE mine tailings remediated with amendment and ramie (Boehmeria nivea L.). *Science of the Total Environment*. <doi:10.1016/j.scitotenv.2021.152075>

[^1]: U.S. DOE, Office of Environmental Management, \"Groundwater Interim Action,\" Moab UMTRA Project. <https://www.energy.gov/em/moab/groundwater-interim-action-0>

[^2]: U.S. DOE, Office of Environmental Management, \"Overview of the Moab UMTRA Project.\" <https://www.energy.gov/em/moab/overview-moab-umtra-project>
