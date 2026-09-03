---
title: Ion-Adsorption Clays
---

(ion-adsorption-clays)=
# Ion-Adsorption Clays

{index}`Ion-adsorption clays <ion-adsorption clay>` are the odd deposit type in rare earth processing, and the
questions they raise are as much chemical-engineering questions as geological
ones: where are these clays mined, how are they processed, can they be bought on
the open market, what chemistry makes them work, and are they recyclable? This
chapter answers those in turn, then assesses the state of the art, the research
opportunities, and the environmental implications.

It draws on the thermodynamic-screening work of
@mohamadsobri2025enhancing and on the broader ion-adsorption-clay literature
[@borst2020adsorption; @zhou2020genesis; @moldoveanu2016overview; @luo2022development; @wu2023rare; @alshameri2019understanding]. Leaching
of these ores is also treated from the flowsheet side in
[](#ion-adsorption-clay-leaching-the-gentle-approach); this chapter takes the
deposit and the {index}`ion-exchange <ion exchange>` chemistry as its subject.

## Summary

- Ion-adsorption clays (IAC) -- also "ion-adsorption deposits," "regolith-hosted REE deposits," or "weathered-crust elution-deposited ores" -- are the dominant global source of the **heavy** rare earths (Dy, Tb, Y). Their value is that the REE are held as loosely bound, hydrated, **exchangeable** ions on clay surfaces, so they can be recovered by a simple salt solution at room temperature -- no roasting or strong-acid cracking [@borst2020adsorption].
- The clay is **not** an open-market commodity: it is low-grade, processed near-source, and supply is dominated by China and Myanmar. The host minerals (kaolinite, halloysite) are cheap industrial clays, but those are sold **without** the adsorbed REE.
- The chemical-engineering pain is dilute, high-volume hydrometallurgy with impurity co-extraction (Al, Fe), speciation/{index}`precipitation` yield losses, and reagent-driven pollution. Thermodynamic screening is one response to it: compute the aqueous stability fields and pick a reagent (MgSO4) and conditions (ambient, acidic) that keep the freed REE soluble [@mohamadsobri2025enhancing].
- The most interesting forward direction is to use **clay/ion exchange itself as a separation technology** -- as a preconcentrator ahead of {index}`solvent extraction`, and (with imported selectivity) as a partial replacement for it.
- The headline environmental issue is ammonia-nitrogen pollution from in-situ ammonium-sulfate leaching, plus landscape destruction and a large spent-clay residue stream whose fate (reuse vs landfill) is unresolved.

## What the clays are and the chemistry that makes them work

REEs in these ores sit primarily in the **ion-exchangeable** phase, typically \~60-90% of total REE content, adsorbed on clay minerals -- chiefly kaolinite and halloysite, with contributions from illite, smectite, and Fe-oxyhydroxides. Synchrotron spectroscopy shows the REE are held as 8- to 9-coordinated **outer-sphere hydrated complexes** on kaolinite: weak, electrostatic, with the hydration shell intact and not bound into a mineral lattice [@borst2020adsorption].

The clay surface carries net negative charge (isomorphic substitution plus pH-dependent broken-edge silanol/aluminol sites). Recovery is therefore **cation exchange** driven by mass action -- a more concentrated electrolyte cation displaces the loosely held REE3+:

``` example
2 Clay-REE + 3 M2SO4  ->  2 Clay-M3 + REE2(SO4)3      (M = NH4+, ½ Mg2+, ...)
```

Because the REE is exchangeable and hydrated, a salt solution at ambient temperature liberates it with fast kinetics and no acid attack on the mineral [@borst2020adsorption; @moldoveanu2016overview]. This is the entire economic basis of the deposit type, and what distinguishes it from hard-rock bastnaesite/{index}`monazite`.

A crucial subtlety for everything downstream: REE attach to clay by **two mechanisms with opposite consequences** [@wu2023rare]:

- **Ion exchange** (outer-sphere) -- dominant, but **cannot fractionate** the REE; it grabs the whole REE block without discriminating among adjacent lanthanides.
- **Surface complexation** (inner-sphere, at edge sites) -- **does** fractionate, enriching HREE over LREE.

## Where they are mined, how they are processed, and market availability

### Formation and geography

IAC form by deep chemical weathering of REE-bearing parent rocks (mostly felsic granites; some mafic-ultramafic for Sc) in warm, humid, subtropical climates. REE liberated from primary minerals migrate down the regolith and re-adsorb onto clays; as weathering advances, kaolinite converts to halloysite, lowering adsorption capacity and producing vertical zonation [@zhou2020genesis].

- **Southern China** (Jiangxi/Ganzhou-Longnan, Guangdong, Fujian, Hunan, Guangxi): historic and dominant producer.
- **Myanmar**: now a very large supplier of HREE-bearing ore/concentrate feeding Chinese separation plants.
- **Emerging/exploration**: Madagascar (mineralogically genuine analogues of the Chinese ores [@borst2020adsorption]), plus Brazil, Malaysia, Laos, Vietnam, Tanzania.

Regolith-hosted deposits supply **over 90% of global heavy-REE production** despite low grade (commonly \~0.03-0.3 wt% total REO); the economics come from the cheap extraction and from geologic pre-concentration, not from grade [@zhou2020genesis].

### Processing chain

1.  **Leaching**: historically heap/tank leaching of excavated ore; now predominantly **in-situ leaching** -- ammonium sulfate (or magnesium sulfate) solution injected into the orebody, pregnant leach solution collected.
2.  **Purification**: impurity removal (Al, Fe) from the pregnant solution.
3.  **Precipitation**: REE recovered as carbonate or oxalate, then calcined to mixed oxide.
4.  **Separation**: individual elements separated downstream, conventionally by solvent extraction.

The general envelope -- ambient temperature, fast kinetics, salt-driven -- holds across ores of varying origin [@moldoveanu2016overview].

### Can they be procured on the open market?

Largely **no**. The ore is low-grade, processed near-source, and subject to Chinese export and technology restrictions, with Myanmar ore feeding Chinese supply chains. What trades openly are the downstream **separated REE oxides**. A common point of confusion: kaolinite and halloysite are cheap, widely sold industrial clays, but the commercial product is purified clay **without** adsorbed REE -- not a substitute for the ore.

## State of the art

### Reagent and condition selection by thermodynamic screening

One route to choosing a lixiviant is to screen candidates thermodynamically before touching an ore. @mohamadsobri2025enhancing is a purely **thermodynamic** (Eh-pH / Pourbaix) study of exactly this kind, not an experimental one. Using HSC Chemistry 10.0 it computes the stability fields of La, Nd, and Y in three sulfate leaching solutions over 0.05-0.6 M and 25-80 degrees C, asking which conditions keep the freed REE soluble as REE3+ rather than precipitating or complexing.

| Leaching solution | Behavior across concentration | Verdict |
|----|----|----|
| (NH4)2SO4 | Good when dilute; \>\~0.25-0.3 M, nitrate from nitrification forms LaNO3(2+)/NdNO3(2+) | Degrades |
| MgSO4 | Maximum stability for La, Nd, Y at **all** 0.05-0.6 M; no unwanted species | **Best** |
| Al2(SO4)3 | SO4(2-) forms LaSO4+ and hydrated Nd2(SO4)3.8H2O | Degrades |

Stability falls as temperature rises (25 -\> 80 degrees C), so ambient leaching is optimal; the REE3+ stability order is La \> Nd \> Y, with acidic windows La (pH 0-5.8), Nd (0-5), Y (0-4.2). The modeled MgSO4-at-ambient conclusion agrees with experiment [@pan2024insights; @shi2022column] which is what lends the screening credibility. **Limitation**: single element, single solvent, no impurities, no kinetics -- a prediction tool, not validation.

### Reagent substitution and impurity control

The field is actively moving off ammonium sulfate. Magnesium sulfate gives comparable recovery with far less nitrogen pollution [@pan2024insights]; low-ammonium column leaching keeps recovery \>90% at much reduced reagent loads [@shi2022column]; and selective inhibitors (e.g., HMTA) suppress aluminum co-dissolution to cut the downstream impurity burden [@he2025stepwise]. "Ammonium-free extraction" and whole-process precipitation are explicit research directions for "green efficient development" [@luo2022development].

### Clay ion exchange as a separation technology

Beyond primary leaching, clay/IX can act as a **separation** unit operation. Its competitiveness depends entirely on the job:

- **Group separation / preconcentration** (pull REE-as-a-block out of a dilute, dirty stream; reject Na/K/Ca/Mg/Al/Fe): driven by **charge** selectivity -- strong. Natural clays are explicitly proposed as adsorbents/recovery media for REE from solution [@alshameri2019understanding].
- **Individual-element separation** (resolve adjacent lanthanides): bare clay is intrinsically weak (adjacent {index}`separation factors <separation factor>` \~1.0-1.3 vs \~1.5-4 per stage for tailored solvent-extraction reagents). Adjacent selectivity must be **imported** -- from surface-complexation sites [@wu2023rare] a complexing eluent, or a grafted ligand.

The proof-of-concept is the orebody itself: the regolith is vertically fractionated (LREE/HREE zonation, Ce anomalies) by clay loading plus carbonate-complexing groundwater acting as a mobile phase -- clay ion-exchange {index}`chromatography` run over geologic time [@zhou2020genesis]. Feasibility is settled; throughput and control are the engineering questions.

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

(clay-research-opportunities)=
## Research opportunities

1.  **Clay as a preconcentrator ahead of SX (strongest near-term).** Load dilute leachate, reject monovalent/divalent matrix ions by charge selectivity, strip a 10-100x concentrated, de-salted REE eluate into a much smaller SX plant or direct precipitation. Directly attacks the dilute, high-volume penalty [@alshameri2019understanding; @moldoveanu2016overview].
2.  **LREE/HREE rough cut.** Exploit the surface-complexation HREE-over-LREE enrichment [@wu2023rare] for a binary roughing split -- apt because IAC feeds are already HREE-enriched.
3.  **Functionalized clay = extraction chromatography on a cheap support.** Graft an SX-grade ligand (phosphonic acid; a {index}`diglycolamide` such as {index}`TODGA`/DMDODGA) onto clay to combine "the selectivity of SX with the convenience of column IX." This is demonstrated on porous supports with diglycolamide extractants as a cleaner alternative to liquid-liquid SX [@momen2019extraction]; clay is the cheap, benign support variant.
4.  **Continuous chromatography (simulated moving bed).** Batch single-column operation is what costs chromatography its throughput; SMB makes it {index}`counter-current <countercurrent cascade>` and continuous (as it is industrially for sugars and enantiomers). A title search of the REE literature for "simulated moving bed" returns essentially nothing -- a genuine white space.
5.  **Synthetic / engineered clay analogues.** Technically feasible (synthetic smectites, pillared clays, LDHs have high exchange capacity), but the value of a natural **deposit** is the geologic pre-concentration onto already-mined regolith [@zhou2020genesis]; synthesizing and then loading from a dilute stream inverts that economy. The realistic role is selective **polishing/concentration** of leachates and effluents, not a synthetic orebody.
6.  **Experimental validation of thermodynamic screening.** Extend Pourbaix-style models to multi-element, impurity-bearing systems with kinetics, and validate against column data [@mohamadsobri2025enhancing].
7.  **Measured separation factors** on smectite/vermiculite vs kaolinite, and how far edge-site density, pH, and ionic strength can push adjacent-REE selectivity [@wu2023rare].

## Environmental implications

### Ammonia-nitrogen pollution (the headline issue)

In-situ ammonium-sulfate leaching discharges ammonia-nitrogen into groundwater and surface water -- the dominant environmental liability of Chinese IAC mining. This is the principal driver of the move to magnesium-sulfate and ammonium-free leaching [@pan2024insights; @shi2022column; @luo2022development]. Reduced-concentration leaching cuts the nitrogen load but needs longer times and larger solution volumes [@shi2022column].

#### Precedent: ammonia at the Moab UMTRA site

A sobering precedent for what residual process ammonia costs comes from uranium, not rare earths. The Moab uranium mill tailings pile near Moab, Utah -- roughly 16 million tons of tailings on the bank of the Colorado River, left by the former Atlas Minerals mill -- is being remediated by the U.S. Department of Energy under the Uranium Mill Tailings Radiation Control Act [@doe2025moaboverview]. Its two main **groundwater** contaminants of concern are **ammonia and uranium**, and ammonia is the driver of the active groundwater remediation: elevated ammonia in the backwater channels beside the pile is toxic to young-of-year endangered fish [@doe2025moaboverview], among them the razorback sucker and Colorado pikeminnow, for which measured chronic values for un-ionized ammonia lie below the concentrations found in those backwaters [@fairchild2005chronic]. Since 2003 DOE has run a groundwater interim action -- currently eight extraction wells plus more than thirty freshwater injection wells that dilute what still reaches the river -- and reports that it has kept roughly **1.0 million pounds of ammonia** and about **5,800 pounds of uranium** out of the Colorado, ammonia outweighing uranium by some **170-fold** [@doe2025moabgroundwater; @doe2025moaboverview].

The ammonia is **process** ammonia: the tailings pile and the former mill area are DOE's identified sources of ammonia to soil and groundwater, and it has leached from the pile into the aquifer for decades [@doe2025moaboverview] -- the same root cause as ammonium-sulfate REE leaching, differing only in unit operation (milling vs leaching). If anything the REE case is harder to contain: Moab is a **point source** (one pile) that can be ringed with extraction wells, whereas in-situ REE leaching injects ammonium **directly into a hillside aquifer over large areas** with no engineered liner. Moab is thus the multi-decade, million-pound, still-pumping illustration of the bill that ammonium hydrometallurgy can incur, and a concrete argument for the magnesium-sulfate / ammonium-free direction [@pan2024insights; @luo2022development; @mohamadsobri2025enhancing].

### Landscape destruction and slope failure

Excavation and in-situ leaching of weathered regolith cause deforestation, soil loss, and landslide risk; in-situ operations suffer uneven contacting and seepage/mass-transfer limits in low-permeability regolith, leaving REE behind and solution uncontrolled [@luo2022development].

### Reagent, energy, and yield footprint

Dilute, high-volume hydrometallurgy means large reagent and water inventories. Choosing reagent/pH/temperature to keep REE soluble (MgSO4, ambient, acidic) reduces precipitation yield losses and avoids the energy of external heating [@mohamadsobri2025enhancing]. Reagent recovery/recycle (ammonium or magnesium sulfate) and leachate recirculation onto fresh ore are central to both cost and pollution [@moldoveanu2016overview; @luo2022development].

### Spent clay residue: reuse vs landfill (the recyclability question)

After leaching, the kaolinite/halloysite substrate survives intact (REE merely desorbs) -- it becomes depleted regolith, not a closed-loop recycled material. Its fate splits between **landfill** and **beneficial reuse** (land reclamation/ revegetation, construction fill, geopolymer/ceramic feedstock), and residue valorization is part of the green-development agenda [@luo2022development]. **If landfill dominates, the environmental case weakens markedly**, and which fate prevails in practice is poorly documented -- the most decision-relevant open question about these deposits, and the one with the thinnest published evidence behind it. By contrast, true REE **circularity** comes from end-products ({index}`NdFeB` magnets, phosphors, e-waste) via urban mining, a separate stream.

### Spent-clay valorization routes

Because the spent clay is essentially a depleted aluminosilicate (kaolinite/ halloysite plus quartz), it is chemically similar to ordinary construction-clay feedstocks, and several beneficial-reuse routes have been demonstrated at lab/ pilot scale:

- **Geopolymer / alkali-activated binder (cement-like)** -- the best-developed route. Ion-adsorption REE tailings have been alkali-activated into geopolymer binders [@zhang2022ion; @hu2020synthesis]. Notably, the motivation is as much **heavy-metal immobilization** as construction: the geopolymer locks contaminants into the matrix, so it doubles as waste stabilization. (This is effectively the metakaolin/pozzolan chemistry -- calcined kaolinite as a supplementary cementitious material.)
- **Glass-ceramics** -- tailings crystallized into diopside/anorthite glass-ceramic for building/decorative use [@zhao2010utilization].
- **Zeolite synthesis** -- the aluminosilicate residue converted to high-crystallinity Zeolite A, which then adsorbs pollutants in the mine's own water -- a closed-loop, treat-your-own-waste reuse [@cheng2024synthesis].

Two routes that **do not** fit, despite the obvious analogy:

- **Asphalt**: clays are generally avoided as asphalt filler -- they are moisture-sensitive and promote stripping (binder-aggregate debonding).
- **Drywall**: drywall is gypsum (CaSO4.2H2O); the only link is the gypsum **byproduct** of sulfate leaching, not the clay residue itself.

The decisive practical caveat: the dominant modern method is **in-situ** leaching, in which the clay is never excavated -- so for those operations there is no solid residue stream to send to a kiln, and the real residue question is in-place **land reclamation and revegetation** [@liu2022biogeochemical]. Reusable tailings exist mainly for older heap/tank (excavated) operations, and even then residual reagent, Al, and occasional radioactivity must be managed, while low-value bulk materials do not travel far from remote mining regions. Net: valorization is real and locally attractive (especially for waste stabilization), but it is not yet a mainstream fate, and in-situ mining structurally limits how much residue is ever collectable.

### Net assessment

IAC are environmentally double-edged: extraction chemistry is mild (no roasting, no strong acid, low radioactivity), but the **process** footprint -- nitrogen pollution, landscape damage, dilute effluents, and a large residue stream -- is substantial. The research frontier (MgSO4/ammonium-free leaching, impurity control, preconcentration, residue valorization) is largely an effort to keep the mild chemistry while shrinking that footprint.
