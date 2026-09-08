---
title: Why Rare Earths Are Hard to Separate
---

(why-rare-earths-are-hard-to-separate)=
# Why Rare Earths Are Hard to Separate

Most separations in chemical engineering exploit a difference. Distillation
exploits volatility, crystallization exploits solubility, {index}`chromatography`
exploits affinity. Rare earth separation is hard because the seventeen elements
in question were built by nature to have as few differences as possible.

They share a +3 oxidation state. They share coordination preferences. Their
ionic radii decrease across the series by roughly 0.012 Å per element — La³⁺ at
1.032 Å down to Lu³⁺ at 0.861 Å in six-coordination [@shannon1976revised], about one percent of an
ionic radius per step, distributed evenly over fourteen steps. Any
chemical process that responds to that difference responds to it weakly, and a
process that responds weakly must be repeated many times. That single fact
explains the shape of the entire industry: a modern separation plant runs
hundreds of {index}`countercurrent <countercurrent cascade>` {index}`mixer-settler` stages not because any one stage is
inefficient, but because a per-stage {index}`separation factor` near 1.5 needs a hundred
stages to reach the 99.99% purity a magnet alloy demands.

Everything else in this book follows from that. The conventional answer —
{index}`solvent extraction`, [](#solvent-extraction-fundamentals) — accepts the weak
per-stage discrimination and compensates with staging, at a cost in solvent
inventory, capital, and waste. Every emerging technology in Part III is an
attempt to find a property that *does* differ sharply between neighbours:
coordination geometry that changes abruptly partway along the series
([](#precipitation-and-selective-crystallization)), a protein binding site evolved for one ion
([](#biological-and-biomimetic-separations)), a pore that admits one hydrated
radius and not the next ([](#membranes-mofs-and-emerging-approaches)). Each is a
bet that some threshold behaviour can be found where the underlying chemistry
offers only a gradient.

## Strategic Importance of Rare Earth Elements
Rare earth elements are essential components in:

- **Clean energy technologies**: Wind turbines, electric vehicles, solar panels
- **Electronics**: Smartphones, computers, displays
- **Defense systems**: Precision-guided weapons, stealth aircraft, submarines
- **Medical devices**: MRI machines, diagnostic equipment

The demand for REEs is expected to increase by a factor of up to 7 by 2040, driven primarily by the global energy transition [@fujita2022recycling].

## The Separation Challenge
The 17 rare earth elements (15 lanthanides plus {index}`scandium` and {index}`yttrium`) share remarkably similar chemical and physical properties, making their separation one of the most difficult problems in chemistry. Key challenges include:

- Similar ionic radii (\~0.012 Å per element, 0.171 Å in total from La³⁺ to Lu³⁺)
- Identical +3 oxidation state for most elements
- Similar complexation behavior with common ligands
- Requirement for extremely high purity (\>99.99%) for many applications

**A note on names.** Which seventeen elements are meant is not left to
convention. IUPAC's *Nomenclature of Inorganic Chemistry* approves
*lanthanoids* as the collective name for the fifteen elements lanthanum through
lutetium, and *rare earth metals* for scandium, yttrium and the lanthanoids
together — exactly the group this book is about [@connelly2005nomenclature].
The same recommendations prefer *lanthanoid* to the far more common
*lanthanide*, on the grounds that an *-ide* ending normally signals a negative
ion. This book uses *lanthanide* throughout, because that is what the
separations literature uses and nothing in the chemistry turns on the choice.
A short free summary of the recommendations is published as an IUPAC technical
report [@hartshorn2015brief], though that summary covers the nomenclature rules
rather than the collective element names, which are in the Red Book itself.

(supply-chain-concerns)=
## Supply Chain Concerns
China dominates the global rare earth supply chain, and it is worth being
precise about which part of it, because the concentration is not the same at
every step and the numbers in general circulation are not all traceable.

**Mining.** In 2025 China produced 270,000 t of a world total of 390,000 t of
rare-earth oxide equivalent — **69%** [@usgs2026mineral]. Burma added 22,000 t,
the United States 51,000 t, Australia 29,000 t.

**Separated product.** No agency publishes separation capacity by country, so
the sharpest available measure is where separated material actually comes from.
Over 2021–24 the United States imported **71%** of its rare-earth compounds and
metals from China, 13% from Malaysia, 5% from Japan, with Estonia next
[@usgs2026mineral] — and the Malaysian and Estonian plants run on concentrates
produced elsewhere, so those shares understate how much of the chain runs
through Chinese-separated feed. For the heavy elements the concentration is
sharper still: US net import reliance for heavy rare-earth compounds and metals
is **100%**, and of those imports terbium, holmium and lutetium are **100%**
from China, ytterbium 86% [@usgs2026mineral].

The figures usually quoted for the middle of the chain — around 90% of
separation capacity, and a similar share of magnet manufacturing — are probably
close to right, but this book could not trace either to a primary source during
its verification pass, so neither is asserted here. What can be verified is
above, and [](#the-industrial-landscape) sets out who actually operates separation
plants and at what published capacity.

**Export controls.** In April 2025 China tightened export controls on rare
earths, adding specific controls on alloys, compounds, metals and oxides of
samarium, gadolinium, terbium, dysprosium, lutetium, {index}`scandium` and
{index}`yttrium`. In October it expanded the controls to europium, holmium,
erbium, thulium and ytterbium; in November it suspended the October expansion
for one year, while the April controls remained in effect and general export
licences began to be issued to selected exporters [@usgs2026mineral].
