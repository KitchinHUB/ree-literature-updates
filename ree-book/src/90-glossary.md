---
title: Glossary
---

(glossary)=
# Glossary

Terms used throughout the book. Definitions are written for the sense the term
carries *in rare earth separation*, which is sometimes narrower than its
general chemical-engineering meaning.

:::{glossary}
activity coefficient
: The correction factor relating a species' effective thermodynamic
  concentration to its analytical concentration. Rare earth extraction runs at
  ionic strengths where activity coefficients are far from unity, so
  equilibrium constants fitted to concentrations rather than activities are
  conditional on the medium they were measured in.

aqueous biphasic system
: A two-phase system formed from two water-soluble components — typically a
  polymer and a salt — rather than from water and an organic solvent. It
  offers a separation without a volatile organic phase, at the cost of a much
  smaller operating window.

bastnäsite
: A rare-earth fluorocarbonate, (Ce,La)CO₃F, and the dominant light-rare-earth
  ore mineral. Mountain Pass and Bayan Obo are bastnäsite deposits. It is
  low in thorium relative to monazite, which simplifies waste handling.

beneficiation
: Physical upgrading of run-of-mine ore into a mineral concentrate — crushing,
  grinding, flotation, magnetic and gravity separation — before any chemistry
  happens. Everything downstream inherits whatever the concentrate contains.

bioleaching
: Mobilization of metals from a solid by microbial action — organic acids,
  siderophores, or the regeneration of a chemical oxidant — as distinct from
  {term}`biosorption`, which is passive uptake onto biomass. Reported REE
  recoveries are real, but the leach is usually the rate-limiting step by
  orders of magnitude.

biosorption
: Uptake of metal ions onto biological material — cell walls, biomass,
  biopolymers — by surface complexation rather than by metabolism. It is
  passive and works on dead biomass, which distinguishes it from bioleaching.

carbochlorination
: Chlorination of an oxide in the presence of a carbon source, which consumes
  the liberated oxygen as CO/CO₂ and makes the reaction thermodynamically
  favourable at temperatures where direct chlorination is not. The first step
  of the chloride route to titanium, and the basis of the halogenation
  approaches in [](#pyrometallurgical-and-halogenation-routes).

chelating agent
: A ligand that binds a metal ion through two or more donor atoms at once,
  forming a ring. The chelate effect makes the resulting complex far more
  stable than the equivalent set of separate monodentate bonds. Note that the
  industrially dominant REE extractants are *not* chelators: D2EHPA, PC88A and
  Cyanex 272 are acidic cation exchangers and TBP is a neutral solvating
  extractant. Chelation matters on the other side of the interface — in the
  aqueous complexants (EDTA, DTPA, citrate) used to shift selectivity and in
  {term}`displacement chromatography`, and in the EF-hand sites of lanmodulin.

coacervate
: A dense, solute-rich liquid phase that separates from a dilute phase without
  a conventional organic solvent. Coacervate systems are pursued as a
  lower-volatility alternative to solvent extraction.

concentration factor
: The ratio of product concentration to feed concentration for the element of
  interest. It measures how much a step concentrates and says nothing about
  purity. Distinguish it from {term}`enrichment factor` and
  {term}`decontamination factor`; the three are routinely conflated in the
  literature and are not interchangeable.

countercurrent cascade
: An arrangement in which the aqueous and organic streams flow in opposite
  directions through a series of stages, so each stage sees a feed already
  enriched by the one before it. This is how a per-stage separation factor
  near 1.5 is compounded into a 99.99% product.

cracking
: The chemical breakdown of a refractory ore mineral into acid- or
  water-soluble species — typically concentrated sulfuric acid bake or caustic
  digestion for monazite and bastnäsite. It is the step that makes the rare
  earths leachable at all.

crud
: The stable emulsion of solids, degraded organic, and aqueous that
  accumulates at the phase interface in a solvent extraction circuit.
  Operationally it is the difference between a flowsheet and a plant: it does
  not appear in the equilibrium chemistry and it dominates maintenance.

D2EHPA
: Di-(2-ethylhexyl)phosphoric acid, the archetypal acidic organophosphorus
  extractant, also written **HDEHP** and sold as **P204**. It exists as a
  hydrogen-bonded dimer in aliphatic diluents, which is why the extraction
  stoichiometry is written in (HL)₂. Strong extraction, hard stripping.

Damköhler number
: The ratio of a characteristic reaction or mass-transfer time to a
  characteristic residence time. In a contactor it answers whether the phases
  reach equilibrium before they leave: a large value means the stage is
  equilibrium-limited, a small one that it is kinetics-limited — the
  distinction microfluidic contactors exploit
  ([](#microfluidic-and-flow-separations)).

decontamination factor
: The factor by which a named impurity is reduced from feed to product at
  fixed product recovery. It is the quantity that matters for radiological
  contaminants such as thorium in monazite circuits, where the specification
  is written on the impurity rather than on the product.

deep eutectic solvent
: A liquid formed by mixing two solids whose eutectic melting point is far
  below either component's, most often a quaternary ammonium salt with a
  hydrogen-bond donor. Investigated as a lixiviant and as an extraction
  medium.

diglycolamide
: A class of tridentate extractants (TODGA is the best known) built around a
  diglycolamide backbone with two amide arms and an ether oxygen. They give
  high loading of trivalent lanthanides and actinides from nitric acid.

diluent
: The bulk organic liquid — kerosene, Isopar, Escaid — in which the extractant
  is dissolved. It is not inert: it sets viscosity, density difference, flash
  point and phase-disengagement time, and its aromatic content changes both
  extractant aggregation and the onset of a {term}`third phase`.

displacement chromatography
: The ion-exchange mode used for rare earths: a loaded bed is developed with a
  complexant eluent (EDTA, HEDTA, DTPA) against a retaining ion such as Cu²⁺ or
  Zn²⁺, and the elements emerge as contiguous, self-sharpening bands of nearly
  pure single elements rather than as separated peaks. It gives far sharper
  separation than solvent extraction and far less throughput, which is why it
  survives only for high-value, low-tonnage product.

distribution ratio (D)
: The ratio of the total analytical concentration of an element in the organic
  phase to that in the aqueous phase at equilibrium. It is not an equilibrium
  constant: it depends on pH, extractant concentration and loading. See
  {term}`extraction constant (K_ex)`.

EF-hand
: A helix-loop-helix metal-binding motif found throughout calcium biology, in
  which a twelve-residue loop supplies the metal's oxygen donors. Lanmodulin's
  EF-hands carry substitutions that convert a calcium site into a lanthanide
  site, which is the structural origin of its Ln/Ca selectivity.

enrichment factor
: The ratio of the target element's mass fraction *within the rare earth
  fraction* between product and feed. Unlike {term}`concentration factor` it is
  a purity measure, and unlike {term}`separation factor` it is defined against
  the whole feed rather than against one named competitor.

extractant
: The species in the organic phase that actually complexes the metal —
  D2EHPA, PC88A, Cyanex 272, TBP, a diglycolamide. It is distinct from the
  diluent, which is the bulk organic carrying it, and from any modifier added
  to suppress third-phase formation.

extraction constant (K_ex)
: The equilibrium constant for the cation-exchange extraction reaction,
  REE³⁺(aq) + 3 (HL)₂(org) ⇌ REEL₃·3HL(org) + 3 H⁺(aq). Unlike the
  {term}`distribution ratio (D)` it does not depend on pH; the pH dependence
  appears only when the mass-action expression is rearranged for D, giving
  log D = log K_ex + 3 log[(HL)₂] + 3 pH.

extraction factor (E)
: The product of the distribution ratio and the phase ratio, E = D·(O/A). It,
  not D alone, determines what a stage achieves: a single equilibrium stage
  extracts a fraction E/(1+E), and E is the parameter the Kremser equation is
  written in.

flash Joule heating
: Resistive heating of a conductive feedstock by a capacitor discharge,
  reaching thousands of kelvin in under a second. Applied to REE recovery it
  converts feed to a leachable form on a timescale short enough to avoid the
  reactions a furnace hold would allow.

flotation
: Separation of mineral particles by selective attachment to air bubbles after
  surface conditioning with collectors. The main beneficiation route for
  bastnäsite.

heavy rare earth elements (HREE)
: Gadolinium through lutetium, plus yttrium. Scarcer, more valuable and
  harder to separate than the light rare earths, and the reason ion-adsorption
  clays matter out of proportion to their grade. The Gd boundary is a
  convention, not a chemical fact, and commerce is inconsistent: some
  classifications place Gd with the lights, and a middle group (Sm-Gd, "MREE")
  is also in use. This book puts Gd with the heavies throughout.

hydrometallurgy
: Metal extraction through aqueous solution chemistry — leaching, solvent
  extraction, ion exchange, precipitation. Contrast pyrometallurgy.

inner-sphere complex
: A complex in which the ligand is bonded directly to the metal ion, having
  displaced a water molecule from its first coordination shell. In an
  outer-sphere complex the ligand is held beyond that shell by electrostatics
  and hydrogen bonding, and the metal keeps its hydration. The distinction
  governs whether an extractant can discriminate on anything but charge.

ion exchange
: Separation by reversible exchange of ions between a solution and a solid
  resin. It gives sharper separations than solvent extraction and was the
  pre-1960s industrial route; it is now reserved for ultra-high-purity
  product because of its throughput.

ion-adsorption clay
: A weathered granite regolith in which rare earths sit as exchangeable
  hydrated cations on clay surfaces rather than in a mineral lattice. Grades
  are low, but the rare earths are recovered by simple salt-solution ion
  exchange and the deposits are unusually rich in heavy rare earths.

ion-imprinted polymer
: A polymer crosslinked around a template ion, which is then removed to leave
  cavities matched to that ion's size and coordination geometry. An attempt to
  build threshold selectivity into a material where the underlying chemistry
  offers only a gradient.

isotachophoresis
: An electrophoretic technique in which analytes migrate between a leading and
  a trailing electrolyte and self-sharpen into contiguous bands of constant
  velocity. The self-sharpening is what makes it interesting here: band edges
  stay sharp instead of diffusing, so resolution does not decay along the
  channel. What has actually been separated this way, and at what scale, is in
  [](#microfluidic-and-flow-separations).

lanmodulin
: A bacterial protein whose EF-hand sites bind trivalent lanthanides with
  picomolar affinity, roughly 10⁸-fold more tightly than calcium. That
  Ln-versus-everything-else selectivity is what makes it useful, and it is
  enormous. Its selectivity *within* the series is not: the monomer's
  dissociation constant varies only about 25-fold from La to Lu, so lanmodulin
  is a group-capture agent rather than an adjacent-pair separating agent. See
  [](#biological-and-biomimetic-separations).

lanthanide-binding tag (LBT)
: A short peptide derived from the calcium-binding loop of an EF-hand,
  engineered to bind trivalent lanthanides. LBTs are the fragment, lanmodulin
  the whole protein, and the difference costs affinity: immobilized LBTs bind
  in the micromolar range against picomolar for the intact protein. Like
  {term}`lanmodulin` they capture the group; they do not resolve adjacent
  pairs.

lanthanide contraction
: The steady decrease in ionic radius across the lanthanide series, roughly
  0.012 Å per element (0.171 Å in total, La³⁺ 1.032 Å to Lu³⁺ 0.861 Å at
  six-coordination [@shannon1976revised]), caused by poor shielding of the
  nuclear charge by 4f electrons. It is the property most separations exploit,
  and its smallness is why they are hard. It is not the only handle: cerium and
  europium have accessible Ce(IV) and Eu(II) states, and the redox separations
  built on them ([](#precipitation-and-selective-crystallization)) are the
  sharpest in industrial use precisely because they do not depend on radius.

leaching
: Dissolution of a target metal out of a solid into a solution. The solution
  used is the lixiviant.

light rare earth elements (LREE)
: Lanthanum through europium. Abundant relative to the heavies, and the bulk
  of what bastnäsite deposits produce. See
  {term}`heavy rare earth elements (HREE)` for the boundary convention.

lixiviant
: The solution used to leach a target metal out of an ore or residue.

loaded organic
: The organic phase after extraction, carrying the metal. It is scrubbed to
  remove co-extracted impurities and then stripped to recover the metal into a
  fresh aqueous phase.

loading
: The fraction of the extractant's capacity occupied by metal. As loading
  rises D falls, selectivity generally degrades, and the organic phase
  approaches its viscosity and {term}`third phase` limits. A separation factor
  quoted without a loading was measured near infinite dilution and will not be
  reproduced in a plant.

McCabe-Thiele diagram
: A graphical stage construction: the equilibrium curve, organic against
  aqueous concentration, with an operating line whose slope is the phase ratio,
  stepped off to count stages. It is the standard way to size a rare earth
  extraction section and to see at once whether a pinch exists.

metal-organic framework (MOF)
: A crystalline solid built from metal nodes bridged by organic linkers, with
  permanent porosity and pore dimensions tunable by linker choice. The REE
  results in this book do not come from a pore sieving one ion and rejecting
  the next: they come from binding sites built into the framework — free
  carboxyl groups, triazole nitrogens — whose response to ionic radius is
  sharper than a dissolved ligand's. The pore holds the site in place; it is
  not itself the discriminator. See [](#metal-organic-framework-mof-nanotraps).

mixer-settler
: The workhorse solvent extraction contactor: a stirred chamber where the
  phases are dispersed and equilibrated, followed by a quiescent chamber where
  they separate under gravity. Hundreds are staged in series in a commercial
  REE plant.

modifier
: An additive to the organic phase — a long-chain alcohol such as isodecanol,
  or TBP — used to raise the solubility of the metal-extractant complex and
  suppress {term}`third phase` formation. It buys phase stability at some cost
  in selectivity.

monazite
: A rare-earth phosphate, (Ce,La,Nd,Th)PO₄, and the second major ore mineral.
  It carries thorium in the lattice, which makes its residues NORM and drives
  much of the cost and permitting difficulty of monazite processing.

NdFeB
: The neodymium–iron–boron magnet alloy, Nd₂Fe₁₄B, usually with dysprosium or
  terbium substituted in for coercivity at temperature. It is the single
  largest driver of rare earth demand and the feedstock for magnet recycling.

NORM
: Naturally occurring radioactive material. Rare earth ores concentrate
  thorium and uranium, so residues are regulated as NORM — a waste-management
  and licensing problem, not a chemistry problem, but often the binding
  constraint on a flowsheet.

numbering-up
: Increasing throughput by running many identical small units in parallel
  rather than by building a larger one. It is how microfluidic separations
  propose to scale, and it trades a scale-up risk for a manifolding and
  fouling problem.

outer-sphere complex
: See {term}`inner-sphere complex`.

PC88A
: 2-ethylhexyl phosphonic acid mono-2-ethylhexyl ester, the workhorse of modern
  rare earth fractionation. The same compound appears in the literature as
  **HEHEHP**, **EHEHPA**, **P507** and **Ionquest 801**; these are one reagent,
  not five. It strips more easily than {term}`D2EHPA` and gives slightly higher
  adjacent-pair separation factors, which is why it displaced it industrially.

pH₁/₂
: The aqueous pH at which half the metal is extracted, D = 1. It is the
  standard way to compare extractants and elements on one axis: because log D
  rises with slope 3 against pH, the separation factor between two elements is
  β = 10^(3 ΔpH₁/₂), so a gap of 0.1 pH units is a factor of two.

pH swing
: The operating principle of acidic-extractant solvent extraction: metal
  transfers to the organic phase at higher pH and is stripped back into the
  aqueous phase at lower pH.

phase ratio (O/A)
: The volumetric ratio of organic to aqueous flow through a stage. It is a free
  design variable that moves the {term}`extraction factor (E)` without changing
  the chemistry, and it is the first thing to check when a reported recovery
  cannot be reproduced.

precipitation
: Recovery of a metal as an insoluble solid — oxalate, carbonate, hydroxide,
  double sulfate — by adding a reagent or shifting pH. It is the standard
  finishing step after solvent extraction and, exploited selectively, a
  separation in its own right
  ([](#precipitation-and-selective-crystallization)).

pregnant leach solution (PLS)
: The metal-bearing solution leaving a leach circuit, before purification. Its
  free acid, iron, aluminium, calcium, phosphate and total dissolved solids
  determine what the solvent extraction circuit downstream has to survive, as
  much as its rare earth content does.

pyrometallurgy
: Metal extraction at high temperature without a bulk aqueous phase — roasting,
  chlorination, molten-salt electrolysis. It avoids the water and acid
  inventories of hydrometallurgy and pays for it in energy and materials of
  construction.

raffinate
: The aqueous phase leaving an extraction stage, depleted in the extracted
  metal. In a cascade it is the feed to the next stage; at the end of the
  circuit it is a waste or a recycle stream.

rare earth elements (REE)
: The fifteen lanthanides plus scandium and yttrium. Yttrium is included
  because its ionic radius places it among the heavy lanthanides
  chemically, and it separates alongside them.

roasting
: Heating an ore or concentrate in a controlled atmosphere to convert minerals
  to a more tractable form — oxidizing carbonate to oxide, converting cerium
  to Ce(IV), or sulfating for a subsequent water leach.

saponification
: Pre-neutralization of an acidic extractant with NaOH, ammonia, or a magnesium
  or calcium salt before it contacts the feed. Extraction releases three protons
  per RE³⁺ and would otherwise drive the aqueous pH out of the operating window
  within a stage or two. Ammonia saponification is the origin of the
  ammonium-nitrogen effluent that dominates the environmental burden of rare
  earth separation plants.

scrubbing
: Contacting the loaded organic with a clean aqueous phase to strip
  co-extracted impurities back out before the product is stripped. It buys
  purity at the cost of some product recirculation.

separation factor
: The ratio of the distribution ratios of two elements, quantifying how well a
  system discriminates between them. For adjacent lanthanides it is typically
  small, which is why REE separation needs many stages.

solvent extraction
: Transfer of a metal between an aqueous phase and an immiscible organic phase
  containing an extractant. It is the dominant industrial REE separation
  because it is continuous, scalable, and stageable — not because any single
  stage separates well.

speciation
: The distribution of an element among its actual chemical forms in solution —
  free ion, hydroxide, sulfate, chloride, and organic complexes. Two liquors
  of identical elemental assay can behave completely differently, and
  speciation is why.

stripping
: Recovering the metal from the loaded organic into a fresh aqueous phase,
  regenerating the extractant for recycle. The reverse of extraction, driven
  by a change in acidity or by a competing complexant.

supported liquid membrane (SLM)
: A porous support whose pores are filled with an organic extractant phase, so
  extraction and stripping happen across a single thin barrier instead of in
  separate contactors. It collapses a cascade into one unit; membrane
  stability is the reason it has not displaced one.

synergistic extraction
: Extraction by a mixture of two extractants that exceeds the sum of their
  separate performance, usually because one satisfies the metal's charge and
  the other displaces its remaining water. Synergism can also shift
  selectivity, not just capacity.

techno-economic analysis (TEA)
: A costed process model — capital, operating, and revenue — used to compare
  flowsheets on economics rather than on recovery. Paired in this book with
  life cycle assessment (LCA), which does the same for environmental burden.

technology readiness level (TRL)
: A nine-point scale for how far a technology has been demonstrated, from basic
  principles (1) through laboratory validation (4) and relevant-environment
  demonstration (6) to a proven operating system (9). Assignments in this book
  are justified from demonstrated scale, not from claimed potential: a bench
  result on a synthetic feed is not a pilot.

third phase
: A third liquid layer that separates between the aqueous and organic phases
  when the metal-extractant complex exceeds its solubility in the diluent. It
  is an operational failure, not a curiosity — it holds up metal and destroys
  interface control — and it is fought with a {term}`modifier`, a more aromatic
  {term}`diluent`, higher temperature, or lower {term}`loading`.

xenotime
: A rare-earth phosphate, YPO₄, chemically similar to monazite but strongly
  enriched in yttrium and the heavy rare earths. A minor ore by tonnage and a
  significant one by value.
:::
