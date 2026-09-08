# Claims that could not be verified without journal access

This file is the standing to-do list for the one category of correctness
problem this project could not close on its own.

The book's rule is that a citation which resolves is not thereby correct: the
cited work has to actually contain the claim. Verifying that means reading the
paper. For most of the bibliography that was possible — abstracts and full text
came from CrossRef, OpenAlex, Europe PMC, Semantic Scholar and OSTI, and where a
publisher's own site refused (Springer, RSC and Elsevier all block automated
access) OpenAlex usually still returned an abstract.

The entries below are the residue: cases where the specific number in the book
sits in a table, a figure, or a methods section that no open interface exposes.
None of them is known to be wrong. Each is a claim standing on an abstract or on
a secondary description rather than on the passage that contains it.

**What to do with each one:** pull the PDF, find the number, and either confirm
it, correct it, or delete the sentence and say plainly that the figure is not
established. Do not resolve one by finding a different paper that happens to
report a similar number.

**Where the PDFs go:** `fulltexts/`, which is gitignored — publisher PDFs are
not redistributable and must never be committed. Files are named by citation key
(`huang2002rare.pdf`) inside `tier-2/`, `tier-3/` and `tier-4/` subdirectories
matching the tiers of issue #1. Every file's title was checked against the
bibliography entry before it was read, so a PDF named for a key is that key's
paper. Issue #1 lists every entry in this file with its DOI and what
specifically to look for, in a suggested retrieval order.

## Resolved

**Tier 1 (1 source).** `ding2023separation` — retrieved and read. The claim was
**wrong**: the paper's separation factor of 125 is dysprosium over praseodymium
*and* neodymium combined, not Dy/Nd, and it is a batch transfer ratio rather
than an equilibrium β. Corrected in ch04, ch09, ch12 and the provenance
appendix; see `RELEASE-PLAN.md`.

**Tier 2 (15 sources).** All retrieved and read. **Every flagged number was
confirmed exactly as the book states it** — 9.55 at.% N and 128.98 F/g and
23.66 mg/g La; β = 15.34 / 14.70 / 10.78 for Eu/Yb, Eu/Tm, Eu/La; 19.2 g/kg
resin loading at 20 % purity against 3 %; 8.4 mg Th/g carbon; 165,000 ppm TDS
and the pH 5-6 optimum and 65 % loss at pH 2 and the ~70 °C improvement; >40×
and >4× for the DGA COF; >2000 mg/kg REE in phosphogypsum; ~100 % recovery on
O-doped MoS₂; ~140 / 72 / 58 for Tb/La, Tb/Yb, Tb/Nd; ~400 An/Ln on the graphene
oxide membrane; the three-level transitions and periodicity and all sixteen
elements; 2.6× recovery and ~80 % less leaching agent and ~70 % fewer impurities;
95 % recovery on 5,000 t and 95 % ammonia reduction; 98.2 % and 96.2 % for the
mechanochemical yttrium route.

Reading them nonetheless changed the book in four places, because the full texts
carry things no abstract did:

- **`behera2025supramolecular`** reports a near-pair the abstract omits.
  **Tb/Eu is ~3**, against ~140 for Tb/La. The book had said no near-neighbour
  figure was given; it now gives this one, which reshapes the claim.
- **`wang2025industrial`** contains the technoeconomic numbers ch21 said were
  unobtainable, and they cut against the abstract's framing: US$7,078 per tonne
  REO for electrokinetic mining against US$6,214 conventional — 14 % *more*
  expensive — reversed only by US$16,477/t of remediation cost the conventional
  route does not internalise.
- **`zhao2022selectively`** gives the size of a selectivity the book had only
  named: 19.66 mg/g La against 12.25 Fe in the quaternary batch, and 450 s
  against 90 s to breakthrough in flow.
- **`virolainen2019recovering`** gives the calcium loadings that explain the
  resin comparison: 14.7 g Ca/kg on the chelating resin against 67.0 on the
  strong cation exchanger.

**Tiers 3 and 4 (19 sources).** All retrieved and read. Unlike Tier 2, reading
these *changed* the book in several places, because three of the flagged claims
were wrong and two more had been deleted when they should not have been.

- **`huang2002rare` was misread twice over.** Chapter 04 attributed
  `xue2025onestep`'s carbochlorination conditions to it, and both chapters had
  the rationale for the SiCl₄ additive backwards. The paper does report
  adjacent-pair separation factors, which the book had said it did not: the best
  is about **2.3** (Ce/La) and several pairs come out **below 1**. Yields, the
  three-stage sequence, activation energies and the thorium condensation
  mechanism are now in chapter 07.
- **Chapter 11 had deleted two sets of figures that are in fact in their
  papers.** `zhou2018leaching`'s 26-35 % saponin leaching recoveries and
  `zhang2018bioleaching`'s 200 µmol/L siderophore titre are both restored, each
  with the qualification that makes it honest — the soil is *spiked*, not
  contaminated; the titre is from rock-free growth medium and was not detected
  at all in the presence of rock.
- **`leblebici2017efficiency` undercuts a remedy chapter 10 reports.** The same
  group's photonic efficiency is flat at 0.66 ± 0.04 from 5 to 30 mm with no
  366 nm absorbance observed, so the back reaction the monochromatic-light
  remedy is meant to suppress does not appear to operate.
- **The kinetics numbers chapter 15 declined to quote all exist**, and are
  better arguments than the chapter's headline: β(Pr/Nd) = 21.7 against 1.6-1.8
  for the extractant alone [@wang2019enhanced], 8.3 against 1.53 conventional
  [@sui2023kinetic], 2.89 Tm/Er against ~1.5 [@sui2024nonequilibrium].
  `cao2021extraction` is the counterexample and is now presented as one: it
  reports no separation factor at all, and its rate spread across the whole
  series is 6.3, *smaller* than the equilibrium spread.
- **`canovas2019leaching` and `rychkov2018recovery` disagree with each other**,
  46-58 % against 14-18 % recovery from the same acid, and the disagreement is
  the useful part — it is a host-phase difference, and it scopes
  `virolainen2019recovering`'s conclusion that breaking up the gypsum structure
  is unnecessary to one feedstock rather than to phosphogypsum in general.

The recurring pattern across all nineteen is the book's own thesis arriving from
a new direction. The 2025 reticular-materials review has no separation-factor
column and exactly one lanthanide-over-lanthanide number in 231 references
(4.5); the 2025 electrochemistry review reports none at all across ~30 tabulated
studies; two MXene papers report no lanthanide pair between them; a COF paper
promises a separation factor in its methods and never delivers one;
mechanochemical leaching co-dissolves four lanthanides at 89.7-97.6 %. Large
selectivities are for distant pairs or for rare-earth-over-base-metal, and they
collapse or vanish for adjacent lanthanides.

`deng2025application` could not be obtained and remains flagged below.

**Batch 3 (42 sources).** Retrieved and read as a block from the general
collection list in `fulltexts-wanted.md` rather than from the flagged table, so
most were expected to be routine confirmations, and most were: the fly ash
grades, the NiMH black-mass assay, the acid-mine-drainage precipitant
comparison, the Marcellus shale and produced-water numbers, the Nd/Pr separation
factor of 2.72, the eight reasons ionic liquids never reached a plant, and the
whole machine-learning cluster all check out exactly as the chapters state them.
Nine did not, and four of those were the chapters reading a paper backwards or
past its own conclusion:

- **`boronski2020rationally` was inverted.** Chapters 10 and 13 both said CSEREOX
  separates *within* rare earth subgroups. It separates *between* them — the
  light oxalates (La-Sm) stay solid while an organic base carries the heavy ones
  (Gd-Lu) into solution — and the demonstration is dysprosium out of didymium,
  4.68 to 1.49 wt % in one 15-minute cycle at 68 % efficiency, with a
  solubility-based comparative extraction factor of 38 for Nd against Dy. The
  paper's own phrase, "separation within two subgroups", means partitioning the
  series into two, and was read as its opposite. The "below 5 %" the chapters
  quoted is the dysprosium content, not a total rare earth concentration.
- **`powell1956basic` was misread twice, in the same way as `huang2002rare`.**
  Chapter 04 gave the retaining-ion rationale backwards: copper works *because*
  its EDTA complexes have very large formation constants, combined with the
  resin's greater affinity for RE³⁺ than for Cu²⁺, not because its complex is
  weaker than any lanthanide's. Zn²⁺ is not named as a retaining ion by this
  source at all; Fe³⁺ is, and is reported inferior. Separately, the technology
  table said ion exchange is "not expressed as β" — the paper tabulates
  adjacent-pair exchange constants for the entire series, 1.02 (Gd/Eu) to 4.8
  (Tb/Gd) with EDTA, **Nd/Pr = 2.0**, and a second set for HEDTA. That is the
  oldest adjacent-pair number in the book and it belongs next to the 2.72 from
  `safarzadeh2018insights`.
- **`fieser2016raman`'s conclusion cuts against the use chapter 19 made of it.**
  The Gd-Tm N-N frequency trend is real (1447 to 1413 cm⁻¹), but the authors
  found it in one ligand set and not in the others, call the result unexpected,
  and warn that "extrapolating based on a few Raman spectra should be done with
  caution". The chapter had taken the regularity as the point; it now carries the
  caution too.
- **`wang2025rare` does report recoveries**, which chapter 05 said should not be
  quoted from it: 94.03 % for *A. ferrooxidans* and 83.48 % for *A. niger* on
  ion-adsorption ore. It was also miscited for *A. niger* working on monazite; it
  is an ionic-clay study and mentions monazite only in passing.

The remaining five are narrower. `noack2015rare`'s calcite effect is a 54-400 %
interval, not "roughly 400 %". `cheng2021theoretical` validates COSMO-RS on one
binary at one temperature, so chapter 16's "temperature dependence" and
"multi-component" bullets had no basis. `yin2024preparation` carbochlorinates
*desiliconized zirconia*, not zircon sand, and supports neither the feedstock nor
the 1000-1200 °C range chapter 07 cited it for — it is now used for what it does
report, a 3 t/day industrial fluidized bed with full operating parameters.
`diazgomez2023synthesis` does not show that stereochemistry alone sets affinity
and selectivity; every diastereomer converges on the same Am/Cm factor of ~1.5,
and substitution matters more than its orientation. `das2016alternative` compares
alkaline conditioning reagents, not graft chemistries.

Reading them also added four things the chapters were missing. `cole2020redox`'s
β = 26 comes with **19 % yttrium recovery** — the separation factor is real and
the conversion is not, and their own model predicts >1800 for a reaction that
went to completion. `alshameri2019understanding` measured La³⁺ and Yb³⁺ on four
clays and got the same capacity ordering and near-identical extraction
efficiencies for both, which is the most direct evidence in the book that bare
clay does not fractionate. `pan2024insights` gives **~94.6 % rare earth leaching
efficiency** for staged magnesium-sulfate column leaching of weathered-crust ore,
with 16.9 % less aluminium and 67.1 % less reagent than the constant-concentration
control. And `bashiri2024artificial`'s R² = 0.928 rests on 225 points from 60
papers, predicting adsorption capacity rather than selectivity.

**Batch 4 (46 sources).** The largest batch so far, and the one with the highest
confirmation rate: the coacervate physics (Voorn-Overbeek, field-theoretic
simulation, the polyelectrolyte-complex continuum), the whole machine-learning
and process-modelling cluster, the produced-water and characterization figures,
the proton hydration enthalpy, the TALSPEAK re-engineering, and the heap-leaching
trial all check out exactly. Six claims did not.

- **Chapter 07's bauxite chloride-route list contained two claims that are not in
  the cited paper.** @namboothiri2017bauxite says nothing about CO₂ capture and
  sequestration, and nothing about biocarbon replacing petroleum coke. Both have
  been deleted rather than re-attributed. What the paper does give, and the
  chapter now carries, is better: calcination at 750 °C, carbochlorination with
  petroleum coke at **650 °C** (not the 500-700 °C the chapter's table asserted),
  reductive distillation, electrolysis in a 50 L cell, a measured **9-10 kWh/kg
  Al** against 13-14 for Hall-Héroult, and a scale-up ladder ending in an
  operating demonstration plant.
- **@lopez2018application filtered synthetic solutions, not real acid mine
  drainage.** Both the chapter 13 table and the chapter 04 feed column said or
  implied a real AMD feed. The paper's own words are "synthetic solutions
  simulating the supernatant of a pre-treated AMD". Corrected in both places.
- **@murthy2011application's two enhancement figures were transposed.** 99.45 %
  is the surfactant result and 99.36 % the EDTA complexation result; chapter 04
  attributed the larger number to complexation. The feed is also a single-element
  synthetic NdCl₃ solution, and without either additive pH alone swings rejection
  from 46.22 % to 90.12 % — a spread the tables did not show.
- **@ortunomacias2024enhanced was credited with the wrong method.** Chapter 11
  said pendant-drop tensiometry and X-ray reflectivity; the reflectivity is in
  the group's *earlier* paper. This one is dilational and shear surface rheology
  with pendant-drop tensiometry.
- **@nikolova2023lanthanides' result is conditional and chapter 08 stated it
  unconditionally.** An EF-hand site is thermodynamically better suited to Ln³⁺
  than to Ca²⁺ when it is buried and carries net charge −3 or −4; at −1 calcium
  still wins. Chapter 11 already had this right.
- **@onal2015recycling was undersold to the point of being misleading.** Chapter
  20 cited it as achieving "the same separation of iron from rare earths through
  a different intermediate". It reports 95-100 % extraction of Nd, Dy, Pr, Gd, Tb
  and Eu, iron left as a marketable hematite residue, and a leachate at ≥98 %
  rare earth purity — better than either arm of the comparison the paragraph
  leads with.

Reading the batch also supplied five sets of numbers the chapters had described
only qualitatively, three of them adjacent-pair separation factors, which this
book collects:

- **@stamberga2020structure reports SF(Nd/Pr) = 3.2** for the best of its twelve
  designed diglycolamides against 2.5 for TODGA, with 2.2 Eu/Sm, 1.9 Tb/Gd and
  2.0 Er/Ho elsewhere in the series. Chapters 13 and 18 had the paper's
  qualitative conclusion and none of its numbers, and chapter 13 was quoting a
  laboratory press release for a selectivity range instead.
- **@wang2021strategy reaches 2.2 Tm/Er, 1.80 Yb/Tm and 2.05 Lu/Yb** in the
  three-liquid-phase system, and strips with 25 % ammonium sulfate instead of
  concentrated acid.
- **@oconnelldanes2022selective's pseudo separation factors are the book's own
  thesis in miniature**: 63 for La/Sm and 248 for La/Eu, Nd/Dy "effectively
  infinite" only because dysprosium does not precipitate at all, and La/Ce,
  La/Pr and La/Nd — in the authors' own words — no better than the phosphorus
  acids already in use.
- **@murase1995recovery fractionates kinetically.** Chemical vapour transport
  gives >99 % purity for each recovered chloride from real magnet sludge, but
  after six hours the rare earth yields are La 27 %, Sm 39 %, Nd 59 %, Dy 68 %
  against >99 % for nickel and cobalt — a factor of 2.5 across the series from a
  single fixed-duration run.
- **@meng2023heap's control run** explains why its 7.4 % aluminium figure
  matters: the conventional ammonium-sulfate route recovers 97.3 % of the rare
  earths but 98.7 % of the aluminium with them, and loses about 10 % of the rare
  earths in the aluminium-removal step that follows.

**Batch 5 (43 sources).** Confirmation rate higher again — the coacervate
thermodynamics, the LLM-agent and machine-learning cluster, the NiMH and
biosorption results, the Myanmar-border remote sensing, the XANES coal
speciation, the DOTA structures and the uranium matrix separation all check out
exactly as stated. Four claims did not, and one of those was a straightforward
miscitation.

- **@chen2023various was cited for the opposite of what it does.** Chapter 05
  used it for the claim that magnetic separation is a *dry* operation placed
  after a wet gravity circuit. The paper is a *wet* method: rare earth particles
  suspended in a water-based ferrofluid or paramagnetic liquid magnetized more
  strongly than the particles themselves, which inverts the capture logic and
  lets particles sort by degree of paramagnetism rather than all reporting to the
  magnetics. The dry-circuit sentence now stands on its own and the paper is
  described for what it is — including the qualification that the feed is
  artificial rare earth particles, not ore.
- **@ahmed2020chromatographic does not use the stationary phases attributed to
  it.** Chapter 19 named iminodiacetate, nitrilotriacetate and
  carboxyl-functionalized silicas; the paper uses a mixed-bed anion/cation
  exchange column with a chelating eluent, and determines the rare earth sum plus
  individual heavy metals in about twenty minutes.
- **@yadav2018ndfeb's 97 % purity takes two cycles.** Chapter 13 reported
  ">97 % purity and about 94 % recovery" as a single result. The paper's own
  sequence is 20 % → 83 % dysprosium in the first cycle, past 97 % in the second.
- **@alizadeh2023deep is a two-element comparison.** Chapter 16 cited it for
  "the heavy-REE preference of D2EHPA" across the series; the paper computes
  Y(III) against La(III).

Reading the batch also supplied four things the chapters were missing, two of
them adjacent-pair separation factors:

- **@zhang2026design reports β(Tm/Er) = 4.18**, with 4.04 and 3.90 for the other
  two isomers and β(Lu/La) from 1688 to 3736. That is among the largest genuinely
  adjacent-pair figures in this book, and the paper had been cited at title level
  only because no abstract or open copy could be reached. Its design rationale —
  a computed Wiberg bond index rising La < Eu < Lu, tracking extraction
  efficiency — is a covalency argument, not a size argument.
- **@zhang2024remarkably's β(Nd/Pr) > 500 needs a qualification the chapter did
  not have.** The feed is a physical mixture of Nd₂O₃ and **Pr₆O₁₁**: the two
  elements arrive as oxides of different average oxidation state, so part of what
  is exploited is a valence difference rather than the lanthanide contraction. It
  also takes seventeen hours, against a solvent-extraction baseline the authors
  themselves put at 1.29-2.5.
- **@yang2024investigation shows vacuum distillation of electrolytic slag mostly
  fails on its own.** Oxygen impurities convert REF₃ to non-volatile REOF, and
  direct distillation recovers only 42.04 %; a fluorination step first raises it
  to 86.23 %. Chapter 10 had the route but neither number.
- **@chaube2020applied's dataset is 5,266 log K₁ values**, which is the concrete
  size of the compiled-potentiometry advantage chapter 18 keeps contrasting
  against the ~1,200 distribution ratios.

**Batch 6 (48 sources).** Mostly method and review citations, and mostly exact:
the coacervate and thermoresponsive polymer physics, the ICP-MS interference
tables, the chromatographic elution orders, the machine-learning and process-systems
cluster, the Moab ammonia toxicology, the flash-Joule-heating figures and the
biosorption capacities all check out. Three claims did not, and two sources the
book had explicitly given up on turned out to be readable.

- **@heo2025extraction's mechanism was stated backwards.** Chapter 07 said the
  fluoride melt beats the chloride melt "because MgF₂ is the weaker fluoride
  donor relative to NdF₃ — the same free-energy ordering that makes fluorination
  selective in the solid-state routes". On the paper's own thermodynamics the
  *chloride* exchange is the more favourable: MgCl₂ and NdCl₃ differ by about
  11 kJ/mol, while MgF₂ and NdF₃ are indistinguishable below 573 K and differ by
  only 0.16-2.8 kJ/mol above it. The authors' explanation for the fourteen-point
  gap is that above 473 K the calculated Nd-metal-to-NdCl₃ ratio rises, so part
  of the neodymium never converts. Corrected, with the melt compositions and each
  route's downstream penalty.
- **@duan2015removal was described with the wrong conditions and the wrong kind
  of result.** Chapter 13's table gave "pH 8-9" and ">90 % REE retention"; the
  paper optimises at **pH 7.5** and reports standard-addition recoveries of
  **89.2 % (La) to 95.8 % (Sm)**. It is also an analytical pretreatment for
  ICP-MS determination in seawater, not a process recovery step, and the table
  now says so.
- **@hartshorn2015brief does not contain the definitions it is pointed at.**
  Chapter 01 offered it as "a short free summary of the recommendations" after
  stating IUPAC's collective names for the lanthanoids and rare earth metals.
  The technical report is a summary of nomenclature *rules* and mentions neither
  term anywhere in its 5,200 words; the collective names are in the Red Book,
  which the chapter already cites separately.

Two sources the text had flagged as unverifiable are now read:

- **@gujar2023complexation is confirmed in full.** Chapter 14 carried its table
  of stepwise enthalpies and entropies with a note saying the individual values
  had not been checked because the full text could not be reached. Every value
  matches. The note is replaced with two things the table could not carry: the
  ionic liquid is a *reagent* rather than a diluent, with charge balance
  maintained by a Tf₂N⁻ anion transferring into the aqueous phase, and of the
  42.5 kJ/mol overall extraction enthalpy only 4.6 kJ/mol is the phase transfer
  itself.
- **@deng2024maximized's numbers exist and are large.** Chapter 13 said its
  solubility values "could not be verified for this chapter and are not quoted
  here". The C8 fluorinated phosphonate extracts lanthanum from a solid matrix
  at **97 ± 2 %** in pure scCO₂ with no cosolvent, against under 10 % for
  TBP-HNO₃, 56 % with added water and 86 % with 5 mol % methanol. It is a single
  element from a solid, so it says nothing about intra-lanthanide separation, and
  the authors themselves caution that CO₂-philicity is necessary rather than
  sufficient.

Three smaller additions: @fairchild2005chronic's actual numbers (backwater
ammonia above 1.00 mg/L against chronic values of 0.40-0.70 mg/L for the
endangered species, and more than ten times Utah's 0.07 mg/L criterion);
@ding2024mathematical's separation is *chelation-assisted*, with Na₂EDTA making
the anionic complexes that migrate, so the selectivity is the chelate's rather
than the membrane's; and @coley2017prediction ranks the true major product first
in 71.8 % of cases, which is the figure that decides whether it can sit inside a
design loop.

**Batch 7 (44 sources).** The process-modelling, machine-learning and
characterization citations came through clean, as did the DOE demonstration-plant
report, the magnet life-cycle figures and the membrane-transport numbers. Three
claims were wrong, two of them in the same sentence.

- **Chapter 07's zinc-fluoride sentence had two errors.** It said "the volatile
  zinc species leave the residue" — they do not; the reaction is
  3ZnF₂ + Ln₂O₃ → 2LnF₃ + 3ZnO, the zinc reports to the residue as solid oxide,
  and unreacted ZnF₂ is filtered off before leaching. It also said "AlF₃ and FeF₃
  behave similarly", which inverts the paper's finding: ΔG for
  3ZnF₂ + Fe₂O₃ → 2FeF₃ + 3ZnO is positive at every temperature, so **iron cannot
  be fluorinated at all**, and that is precisely where the selectivity comes
  from. AlF₃ appears in the paper only as a citation to other groups' melt work.
- **@karnes2016geometric's free-energy minimum has no published depth.** The
  chapter quoted "~−5.9 kJ/mol"; the paper calls the minimum "shallow" and gives
  no number for it. The figure has been withdrawn. The ion is also chloride
  rather than a rare earth, which the bullet did not say.
- **@innocenzi2018treatment filtered synthetic solutions.** The chapter 13 table
  listed "WEEE effluent"; the paper's own words are "synthetic industrial liquid
  wastes", simulating a hydrometallurgical residue. Same correction as
  @lopez2018application in batch 4.

Two sources the text had written off are now read, and both change what the book
can say:

- **@liu2025mechanism's NaBF₄ figures are traceable after all.** Chapter 07 said
  they "could not be traced beyond the abstract and are omitted here". They are
  95.83 % fluorination at 600 °C in 30 minutes with 65 % NaBF₄, a modelled
  optimum of 98.63 %, and 99.39 % purity after a 9 M HCl leach. That is roughly
  250 °C cooler and three times faster than the zinc fluoride route, which makes
  NaBF₄ the better reagent on operating envelope rather than merely a
  "higher fluorine-density alternative". Both papers also report the same
  counterintuitive limit: a hotter roast *lowers* recovery, because oxygen enters
  the fluoride lattice and is stripped out during leaching.
- **@kim2012fluorescent is retrieved, and the hedge it was cited under was
  right.** Chapter 09 said no copy could be obtained and cited it only for the
  class of chemistry. Across the whole review, lanthanides and rare earths are
  not mentioned once.

Three additions. **@johnson2023size reports SF(Tb/Gd) = 5.8 and SF(Sm/Nd) = 15.6**
in a single stage from its two-ligand "tug of war" — the largest adjacent-pair
separation factor anywhere in this book, ahead of @zhang2026design's Tm/Er 4.18
and @stamberga2020structure's Nd/Pr 3.2 — and chapter 10 had been describing the
strategy with no numbers at all. @keim2019production's techno-economic chapter
says in its own words that process costs exceed revenue in every year and the
circuitry is "too costly to be economically viable without government subsidy".
And @li2025prediction's actinide model rests on 454 log K₁ values, an order of
magnitude fewer than the lanthanide compilation, which is worth knowing before
its R² is read as performance.

One bibliography error was fixed rather than flagged: @lin2019intrinsically
carried an author list ("Lin, Currie, Bhattacharjee") that belongs to no version
of the paper. The correct authors are Quiroz, Li, Roberts, Weber, Dzuricky,
Weitzhandler, Yingling and Chilkoti.

**Batch 8 (46 sources).** The cleanest batch of the eight. The magnet-roasting
and recycling numbers, the biosorption and protein-display results, the
*Gluconobacter* genetics, the machine-learning surveys, the analytical-method
citations and the nanofiltration table all check out, several of them word for
word. Three claims needed correcting, and none was a misreading of a mechanism.

- **@sorin2005rejection gives 5 %, not "<10 %".** The chapter 13 table said
  rejection was "<10 % without DTPA"; the paper states that Gd(III) rejection
  "reaches 5 % in absence of complexation". The row now also records why the
  low-pH behaviour departs from speciation — the membrane's isoelectric point is
  3.4, so below that its own surface charge governs.
- **@schmitz2025high's 73 % is a 1 % pulp-density figure.** Chapter 11 quoted it
  as "up to 73 %", which is true but omits that the same strain gives 53 % at
  10 % pulp density. The gain shrinks as the reactor is loaded, which is the
  direction a process has to move, so the pulp density belongs with the number.
- **@sharma2020library covers La-Lu except promethium.** Stated as "from La to
  Lu", which implies all fifteen.

The batch's most useful addition is a corrective one. **@szczesniak2021alkyl was
summarised in a single generous sentence** — that its ligands "improve separation
factors between adjacent lanthanides relative to conventional oxalate
precipitation". True, but the shape of the improvement is the book's own thesis
in miniature and was being left out: the gain is concentrated at the heavy end,
with SF(Tm/Yb) = 4.33 and SF(Yb/Lu) = 2.32 against 1.12-2.12 and 1.03-1.44 for
DEHPA and EHEHPA, and Ce/La at 3.81; but across Nd through Er the factors run
**1 to 1.7**, which the authors themselves call "rather low". Chapter 10 now says
so.

Two smaller additions: @nili2025reclaiming's headline NPV is a base case, and the
reagent recycling that makes the economics work is itself a capital and operating
cost — the 74 %/143 % improvement the paper also reports assumes 99 % recovery,
by-product sales, solvent-extraction tolling and favourable markets together. And
@spadina2019synergistic's entropy is specifically *configurational* entropy,
arising from a polydispersity of aggregates close in free energy but different in
composition, which is a sharper claim than "entropy".

Finally, one earlier finding was re-verified now that the PDF is in hand:
@suli2017rare contains the word "chlorination" zero times, exactly as the
provenance appendix records.

**Batch 9 (45 sources).** Heavy on process-modelling, characterization and
ion-adsorption-clay citations, and almost all exact — the photochemical europium
numbers, the hydrogen-decrepitation recovery, the permeability and slope-stability
modelling, the catchment ammonia figures, the lanmodulin-peptide constants and
the whole machine-learning and optimization stack check out, several word for
word. Two claims did not.

- **@xia2024experimental describes a packed bed, not a fluidized one.** Chapter 07
  said pelletizing "improves gas-solid contact and prevents the fine feed from
  being entrained out of the bed". The paper's stated reason for pelletizing is
  to stop the fine feed *spattering* in a **packed** bed, and it is a
  binder-selection and pellet-strength study — nine binders screened on a Sichuan
  bastnäsite, three carried into carbochlorination trials with AlCl₃. Entrainment
  is a fluidized-bed problem and does not arise here, which matters because the
  surrounding text draws the titanium and zirconium fluidized-bed analogues.
- **@yang2021recovery does not support a capacity claim.** Chapter 07 had molten
  salt electrolysis as "the dominant route to rare earth metals and alloys **in
  China**, and the great majority of that **capacity** is the oxide-fluoride
  cell". The review says neither. What it does say is technical and now stands in
  its place: fluoride is preferred over chloride for metal production because
  chloride melts give low current efficiencies, evolve chlorine at the anode, and
  yield metals at inconveniently low melting points. The capacity split is not
  asserted, and the chapter says so.

One addition, from a paper the chapter had used for only its dissociation
constants. **@verma2024investigation's immobilized LanM1 peptide shows no
measurable affinity for calcium or copper** — which sits directly against
@park2017recovery two paragraphs earlier in the same chapter, where copper was
the single non-rare-earth the displayed tag could not reject. The paper also
supplies the sequence-specificity control the section wanted: a scrambled version
of the same residues binds Ce³⁺ five times more weakly, at 20.59 ± 5.84 µM.

Two filing corrections rather than factual ones. The PDF that matched
@xian2016glutarimidedioxime by DOI is in fact the *retraction notice*, which the
bibliography carries separately as @xian2021retraction; it is filed under the
latter. And the 546 MB *Energy Materials 2014* proceedings volume arrived twice;
one copy was deleted and the other named for the chapter the book cites from it,
@yang2016separation.

## Flagged claims

| Chapter | Citation key | What rests on it |
|----|----|----|
| 11 Biological and biomimetic separations | `deng2025application` | Application-scale claims. The one source from issue #1 that could not be obtained. |
| 16 High-throughput and computational screening | `an2024agile` | Synthesis details of the automated platform. |
| 18 Machine learning in rare earth separations | `zhang2026predicting` | Reported model performance. **PDF retrieved, not yet read.** |
| 18 Machine learning in rare earth separations | `liu2026machine` | Reported model performance. **PDF retrieved, not yet read.** |
| 13 Membranes, MOFs and emerging | `bao2025mxene` | 892.8 mg/g Eu(III) and 649.2 mg/g Ho(III) at pH 2.0, and 99.1 % Eu removal by the PES-supported membrane at pH 5.0. |
| 20 Recycling and urban mining | `tian2020rare` | The 4.5-118.3 µg/L total REE and 0.92-79.62 µg/L Eu in Sichuan flowback water, and the 4.2 t → 16.8-111.7 t Eu₂O₃ projection. |
| 09 Microfluidic separations | `yang2022pilot` | The three-stage counter-current microSX numbered up 100-fold without loss of efficiency. No open copy, no released abstract. The chapter now carries the claim only as the authors summarize it in their own later open-access review, `yang2024industry`, and says so. Reading the paper would supply the throughput it actually reached, which the chapter currently cannot state. |
| 09 Microfluidic separations | `he2024intensifying` | Design results for mini-channel (4-6 mm) counter-current extractors. CrossRef, OpenAlex and Semantic Scholar return no abstract and Semantic Scholar reports the open-access PDF closed. The claim that beyond ~250 mm of channel the extractor exceeds one theoretical stage **has been deleted** rather than left standing; the chapter states that the number is not one it can source. |
| 09 Microfluidic separations | `elmaangar2020microfluidic` | Gibbs free energies of transfer for five REEs by synergic extraction, measured with online XRF. No copy obtainable. The chapter describes the study from its abstract and quotes no quantity from it. |
| 16 High-throughput and computational screening | `augustine2026coupling` | The fourfold separation-factor gain, the pH ≈ 2.0 and pH ≈ 0.5 operating points, and the identification of oxaloacetic acid as the holdback agent. Read from the abstract only; JACS blocks automated access. The chapter states in the text that it is an abstract-level reading. |
| 09 Microfluidic separations | `nichols2011mechanistic` | Absolute interfacial mass transfer rate constants for the whole lanthanide series under TALSPEAK conditions. No copy obtainable. The chapter names the measurement but tabulates only the P507 constants from `zhang2019enabling`. |

## A gap, not a flag

Chapter 05, Hydrometallurgical leaching, stated no rare earth recovery figure for
any leaching route, anywhere in the chapter. That was deliberate: no source
consulted for this book gave one that survived the check, and inventing a
plausible range would be exactly the failure mode the whole project is built to
avoid. The batch-3 pass closed part of it. `pan2024insights` reports **~94.6 %**
rare earth leaching efficiency for staged magnesium-sulfate column leaching of
weathered-crust elution-deposited ore, against a constant-concentration control
that reaches the same figure with 16.9 % more aluminium and three times the
reagent, and `wang2025rare` reports 94.03 % and 83.48 % for bioleaching the same
ore type. The chapter now carries the first of these, with the qualification that
makes it honest: it is a leaching-stage efficiency on a column, for the one ore
type whose rare earths sit on exchange sites rather than in a mineral lattice.

The acid case is now closed too, from a source of a different kind: Qi's
*Hydrometallurgy of Rare Earths* (Elsevier, 2018), an 815-page account of Chinese
industrial practice, obtained and split into its eight chapters. Its first
chapter gives stage-by-stage recoveries for the concentrated-sulfuric-acid
roasting route on bastnäsite: 96-98 % at water leaching, 98 % at double-sulfate
precipitation, 95-96 % at caustic conversion and about 95 % at the preferential
hydrochloric dissolution — roughly **86 % compounded** from calcine to chloride
liquor [@qi2018extraction]. Chapter 05 now carries those, flagged as a stage-wise
product rather than a measured plant figure, together with the point that the
~10 % of middle and heavy rare earths lost at the double-sulfate step is a
composition loss falling on the elements the flowsheet can least spare.

What remains open is the *beneficiation* recovery — ore to concentrate — at
Mountain Pass and Bayan Obo, which is a separate question and which the
chapter's own paragraph on the two chains still declines to answer.

## What the Qi monograph closed

Three further standing statements were retired by the same source, and the
chapters record what replaced them.

- **Chapter 03 said no source established how widely magnesium or calcium
  saponification is practised.** Both non-saponification and CaO/MgO
  saponification appear on the technology list the Chinese Ministry of
  Environmental Protection recommends for eliminating ammonium pollution in
  extraction-separation [@qi2018waste]. That is practice guidance, not an
  installed-capacity survey, and the chapter says so.
- **Chapter 03 attributed the ammonium effluent to saponification alone.** There
  is a second source: converting a dilute sulfate leachate to a chloride feed by
  precipitating with ammonium bicarbonate and redissolving in hydrochloric acid.
  The industry's answer has been non-saponified P507/P204 extraction stripped
  with HCl, which does the conversion without the ammonium [@qi2018waste].
- **Chapter 17 called cascade start-up "the least tested part of any of these
  models".** True of the English-language literature; the Chinese cascade-theory
  tradition treats the approach to steady state as a design variable. Starting
  under total reflux rather than conventionally cut the time to qualified product
  to about a sixtieth and a hundred-and-eightieth of the conventional figure in
  two worked examples, and to a tenth or less generally [@qi2018countercurrent].
  The chapter now carries that, with the consequence that a start-up model
  validated on one procedure is not validated on another.

Chapter 12 also gained the industrial benchmark for europium reduction that the
photochemical and electrochemical routes are competing against: a single
zinc-plus-barium coprecipitation lifts a feed from 0.2-0.3 % Eu₂O₃ in REO to a
20-25 % concentrate at 99 % europium recovery [@qi2018chemical].

Chapter 23, Environment, techno-economics and life cycle, had a second gap of the
same kind, opened and then mostly closed in the 2026 pass. The question was
whether producing rare earth oxide outside China is an environmental
improvement, which the chapter had been careful not to assert:
`zaimes2015environmental` is Bayan Obo alone and `wan2022lca` is Chinese ionic
clay alone. `zapp2022environmental` was flagged as the likeliest source to
close it, then **retrieved and read**, and it does: the review models four
pathways — Bayan Obo/Baotou, Mountain Pass, Mt Weld/Kuantan and Norra Kärr — on
one boundary from mine to metal refining, and reports both normalized totals and
absolute per-kilogram figures. Chapter 23 now carries that table and the ranking.
Reading it also **corrected two things the chapter had said on its authority**:
that the review reports no absolute figures (it does, per kg of neodymium rather
than per kg of REO), and a hotspot table that attributed human toxicity to
radionuclides and listed a water hotspot, neither of which the review supports.

What the study does *not* close is the part that matters most to the American
case, and the chapter now says so in those terms. The authors state that ²³²Th
emissions are not considered in most of the underlying studies, so radionuclide
management sits outside the boundary rather than inside it; no emissions in any
underlying study are measured at a plant, with regulatory discharge limits
standing in; and the modelling assumes exhaust gas scrubbing at every Western
plant but only at modern large Chinese ones, which is an assumed difference in
environmental standard rather than a chemical one. The study that would close
the remainder is the same four chains with radionuclide handling inside the
boundary and measured effluent data in place of permit limits.

## Cited for existence, with no number taken

A second and milder category, introduced with chapter 14, Kinetics and Mass
Transfer, and extended by the 2026 literature-gap pass. These are sources whose
abstracts are not exposed by any interface reachable from here — some are
pre-2000 Elsevier and ACS papers that predate structured abstracts in the
aggregators, others are recent papers behind publishers that block automated
access. The book cites them for what their titles establish (that a measurement
was made, of what, by what method) and quotes no value from any of them; the
prose says so at each point. Nothing in the text depends on their contents, so
none of these is a correctness risk in the way the table above is. They are
listed because reading them would let the chapters say more than they currently
do.

| Citation key | What the chapter would gain |
|----|----|
| `geist1999kinetics` | Measured rate constants for rare earth extraction into D2EHPA, and which step controls. **PDF retrieved, not yet read.** |
| `cossy1988oxygen` | Water-exchange rate constants across the Ln(III) aqua ions, and how much of the series ¹⁷O NMR could actually reach. **PDF retrieved, not yet read.** |
| `gabelman1999hollow` | Mass-transfer correlations for hollow-fibre contactors; currently cited only as the standard review. **PDF retrieved, not yet read.** |
| `tian2010kinetics` | Rate law and activation energy for ammonium sulfate leaching of weathered-crust ore. **PDF retrieved, not yet read.** |
| `he2016kinetics` | The same for column leaching, including the aluminium co-extraction behaviour. **PDF retrieved, not yet read.** |
| `duchanois2023prospects` | Which metals are worth recovering from wastewater and brine, and the techno-economic criteria that decide it. Cited in ch21 for existence only; @smith2024critical relies on it for that guidance and this book takes no number from it. |
| `leite2025creation` | What the Separation Archive for Elements actually contains — how many systems, which measurements, and in what form. Taylor \& Francis returns HTTP 403 and no aggregator carries more than the letter's opening line. Chapter 16 cites it only for the database's formal announcement. |
| `yu2026progress` | The state of pulsed-column development for reprocessing: throughputs, stage efficiencies and the pulse conditions that set them. Closed, with no abstract released anywhere. Chapter 03 cites it at title level only. |
