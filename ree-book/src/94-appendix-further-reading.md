---
title: "Appendix B: Further Reading"
---

(appendix-b-further-reading)=
# Appendix B: Further Reading

This book is a synthesis, and a synthesis is a poor substitute for the reviews
it was built on. What follows is a reading path: for each part of the book, the
one or two works to go to next, and why that one. Every entry is in
[](#bibliography) and every DOI in it has been checked
([](#appendix-a-source-provenance)).

Where a topic has a genuinely canonical review, it is named as such. Where it
does not — and several of the emerging technologies do not — that is said
plainly rather than papered over with the most recent paper available.

## Starting anywhere

Two general reviews cover the whole field at different depths.
@balaram2019rare is the broad one: occurrence, applications, analysis,
recycling, and environmental impact in a single article, and the best first
read for someone who has arrived from outside the field. @chen2021advances is
narrower and more useful once separation itself is the question, covering the
selective-separation technologies that Parts II and III of this book treat one
per chapter.

For the older literature — the chemistry that everything since rests on —
@nash1993basic remains the clearest statement of trivalent f-element separation
principles. @moyer2011overview is about spent nuclear fuel rather than about
rare earths, and is here for that reason: reprocessing is the neighbouring
field that trivalent-f-element separation shares its reagents, its stagewise
thinking, and much of its history with, and reading it shows how much of what
this book treats as rare earth practice arrived from there.

## Ore, beneficiation, and leaching

@jordens2013beneficiation is the reference review on beneficiating rare earth
minerals, and the right place to understand what a concentrate actually
contains before any chemistry starts. @sadri2017cracking covers cracking,
baking, and leaching of concentrates — the step this book treats in
[](#hydrometallurgical-leaching) — across the acid and alkaline routes.
For the two ore minerals specifically: @kim2025rare on bastnäsite, from
beneficiation through to metallurgy, and @kumari2015process on monazite,
including the thorium problem that dominates monazite flowsheets.

Ion-adsorption clays have their own literature because they have their own
chemistry. @moldoveanu2016overview is the overview, and @wu2023rare treats
adsorption and desorption on clay minerals at the level of mechanism.

## Solvent extraction

@xie2014critical is the critical review of rare earth solvent extraction and
the natural companion to [](#solvent-extraction-fundamentals).
@li2019development is the one to read after it: it traces the development of
the acidic phosphorus extractants — D2EHPA, PC88A, Cyanex 272 — as a historical
argument rather than a list, which is the best way to understand why the
industry settled where it did. @guo2026acidic is the recent addition, narrower
than @xie2014critical in that it takes acidic media as its subject, and broader
in that it puts mechanism and process control in the same frame.

For process modelling of the cascade rather than chemistry within it, the two
theses are better starting points than the papers drawn from them:
@lyon2016separation on a Pr/Nd flowsheet with PC88A, and @srivastava2021modeling
on designing a multi-component train when McCabe-Thiele no longer applies.

For ion exchange, which this book covers only in outline,
@elouardi2023progress is the recent survey.

## Pyrometallurgy and halogenation

@pomiro2021panoramic is the panoramic review of chlorination and
carbochlorination of light rare earth oxides, and the closest thing
[](#pyrometallurgical-and-halogenation-routes) has to a single source.
@zheng2019mechanism cover chlorination treatment of ores more generally.
For the electrowinning end, @liao2024research reviews fluoride molten-salt
electrolysis as practised industrially and @li2023extraction covers molten-salt
electrolysis for critical metals more broadly.

## Emerging separations

This is where the reading path thins, and it is worth saying why: several of
the technologies in Part III have no review because they have no field yet —
a handful of groups, a decade of papers, and no independent replication of the
headline results.

Membranes have one: @chen2018overview. Functionalized porous materials,
including the MOF work, have @oztug2024overview. For the ionic-liquid and
aqueous-biphasic systems of [](#coacervates-and-aqueous-biphasic-systems),
@neves2022liquid surveys the more environmentally acceptable liquid-liquid
systems. Microfluidic extraction is reviewed as a unit operation rather than as
a rare earth method, by @xu2017microfluidic and @wang2017microflow; the rare
earth application has to be read from the primary literature.

Bioleaching and biological separation are reviewed by @rasoulnia2020critical,
which is the critical one — it is specific about the process parameters that
determine whether a reported recovery means anything.

## Computation and high-throughput work

@augustine2024advancing is the anchor: the Los Alamos platform that couples
automated high-throughput extraction experiments to machine learning, and the
concrete instance of what [](#high-throughput-and-computational-methods)
describes. @gupta2025accelerating is the surrogate-model paper whose 6.1
kcal/mol error is weighed against the 1 kJ/mol selectivity signal in
[](#the-energy-scale-of-selectivity) — read them together, in that order.

## Machine learning

There is no review of machine learning for rare earth separations, because there
is not yet enough of it to review. The reading path is therefore assembled from
three directions.

For the method: @wigh2022review on how a molecule becomes a vector, which is
where most of the assumptions are buried, and @muratov2020qsar on the validation
discipline that fifty-five years of QSAR produced and that this field has not
yet inherited. @wang2020machine is the practical protocol paper for a chemist
running a first model.

For the field itself: @liu2022advancing is the one to read first — it trains on
measured distribution ratios and then synthesises and measures four of its own
predictions, which almost nothing else here does. @zahariev2024prediction is the
one to read second, because it reports the relative error on a selectivity task
alongside the absolute error, and the gap between the two is the whole argument
for whether any of this works ([](#machine-learning-in-rare-earth-separations)).
@zhang2026augmenting is the most ambitious current workflow, and reading it
carefully — noting where the human approval step sits and where the results stop
being measured — is a useful calibration exercise.

For the process side, which is further along: @dobbelaere2021machine on where
machine learning helps a chemical engineer and where it does not, and
@vogel2023learning and @stops2022flowsheet on flowsheet synthesis treated as a
learning problem. Neither has been applied to a rare earth cascade.

Against all of it: @thebelt2022maximizing on why chemical engineering data
defeats classical machine learning, @estay2023challenges for the same argument
from mineral processing, and @slack2020fooling for the demonstration that a
post-hoc explanation and a model's actual behaviour are separable things.

## Characterization

@balaram2019rare again, for the analytical sections; and @ali2023mineral for
the SEM-based mineral characterization that precedes any flowsheet decision.

## Recycling

@binnemans2013recycling is the paper that defined the field and is still the
one to read first; it is the source of the under-one-percent end-of-life
recycling rate that everything since has quoted. @yang2017ree is the critical
review specific to end-of-life NdFeB magnet scrap, and
@zhang2020hydrometallurgical treats the hydrometallurgical routes for the same
feed in more detail. @fujita2022recycling is the recent perspective.

## Environment, economics, and life cycle

@weber2012rare surveys production, processing, recycling, and the associated
environmental issues together, which is the right framing for
[](#environment-techno-economics-and-life-cycle). @browning2017life is the
inventory that chapter leans on hardest — it is the source of the carbon, water,
and energy figures for monazite — with @navarro2014life and
@zaimes2015environmental the two life-cycle studies behind its framing; @mugion2025systematic is the systematic review of that literature --
seventy-eight studies gathered under PRISMA, covering primary and secondary
production together -- and the fastest way to see the shape of the field and
where its attention has gone.

## Reference works

@connelly2005nomenclature — the IUPAC "Red Book" — is the authority on what the
group is called and which elements are in it; it is freely available and worth
having to hand for the lanthanoid/lanthanide question if nothing else.

@habashi1997handbook and @gupta2003chemical are the extractive-metallurgy
reference works. Neither is about rare earths specifically, and both are the
better for it: much of what makes rare earth processing hard is ordinary
hydrometallurgy operating with unusually poor selectivity.
