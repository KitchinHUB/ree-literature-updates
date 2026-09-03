---
title: From Ore to Feed Solution
---

(from-ore-to-feed-solution)=
# From Ore to Feed Solution

A solvent extraction circuit does not start from an ore. It starts from an
aqueous solution of a particular acid, at a particular pH, carrying a particular
set of impurities — and almost everything that circuit can achieve is fixed
before the first contactor by decisions made upstream. This short chapter covers
that upstream span: which minerals rare earths actually come in, how each is
dissolved, and what the resulting liquor has to look like before extraction can
begin.

Two decisions made here echo through the rest of the book. The first is the
choice of acid: hydrochloric gives a chloride liquor that suits the acidic
organophosphorus extractants, nitric gives a nitrate liquor that suits TBP, and
the two are not freely interchangeable downstream. The second is impurity
removal — iron, aluminium, calcium, thorium, and phosphate all interfere with
extraction, and each part-per-million left in the feed is paid for later.

[](#hydrometallurgical-leaching) treats the leaching step itself in full
industrial detail. What follows here is the condensed version needed to make
sense of [](#solvent-extraction-fundamentals).

## Primary REE Minerals
Rare-earth elements do not occur as native metals but are found in oxide or phosphate minerals cite:jha2016review,xie2014critical. The most important industrial sources are:

1.  **Bastnasite** (REE·FCO₃): Carbonate-fluoride mineral
    - Primary source in US (Mountain Pass, CA) and China (Bayan Obo)
    - Enriched in light REEs: La, Ce, Pr, Nd
    - Typical composition: 60-70% REO (rare earth oxides)
2.  **Monazite** ((REE,Th)PO₄): Phosphate mineral
    - Contains thorium (radioactive, complicates processing)
    - Enriched in middle REEs and heavy REEs
    - Typical composition: 50-70% REO, 0-12% ThO₂
3.  **Xenotime** (YPO₄): Yttrium phosphate
    - Primary source of heavy REEs: Y, Dy, Er, Yb
    - Typical composition: 50-67% Y₂O₃ + heavy REO
4.  **Ion-adsorption clays** (Southern China)
    - REEs weakly bound to clay surfaces as exchangeable ions
    - Can be leached with dilute electrolytes (NH₄)₂SO₄
    - Enriched in heavy REEs (Dy, Tb, Y)
    - Recent work by cite:han2024efficient focuses on this feedstock

## Dissolution and Feed Solution Preparation
### Chloride Solutions
**Preparation**: REE concentrates are roasted and dissolved in hydrochloric acid cite:xie2014critical:

    REE₂O₃ + 6 HCl → 2 REECl₃ + 3 H₂O

**Advantages**:

- Faster dissolution kinetics than nitrate
- Higher REE concentration possible (1-2 M)
- Lower viscosity than nitrate solutions
- Preferred for D2EHPA and PC88A extractants

**Challenges**:

- Corrosive to equipment (requires specialized metallurgy)
- Chloride can interfere with some extractants
- Environmental concerns with HCl vapor

**Typical composition** cite:agarwal2020comparative:

- REE concentration: 0.5-2.0 M (total mixed REEs)
- Free HCl: 0.01-1.0 M (pH 0-2)
- Impurities: Fe³⁺, Ca²⁺, Al³⁺, thorium (if from monazite)

### Nitrate Solutions
**Preparation**: REE carbonates or hydroxides dissolved in nitric acid cite:matveev2018solvent:

    REE₂O₃ + 6 HNO₃ → 2 REE(NO₃)₃ + 3 H₂O

**Advantages**:

- Less corrosive than chloride (316L stainless steel compatible)
- Better for TBP and some neutral extractants
- Salting-out effect with Ca(NO₃)₂ or Al(NO₃)₃ enhances extraction

**Challenges**:

- Lower maximum REE concentration (viscosity limits)
- Nitrate co-extraction can occur with some extractants
- Decomposition risk at high temperatures

**Typical composition** cite:matveev2018solvent,tanaka2021revaluating:

- REE concentration: 0.2-1.0 M
- Free HNO₃: 0.1-3.0 M
- Salting agent: 0-3 M Ca(NO₃)₂ or NaNO₃

### Sulfate Solutions (Ion-Adsorption Ores)
**Preparation**: Direct leaching of clay ores with ammonium sulfate cite:han2024efficient:

    Clay-REE³⁺ + (NH₄)₂SO₄ → REE₂(SO₄)₃ + NH₄⁺-Clay

**Advantages**:

- Mild leaching conditions (ambient temperature)
- Low environmental impact
- Selective for surface-bound REEs

**Challenges**:

- Lower REE concentration in leachate
- Sulfate can precipitate with some extractants
- Requires different extractant chemistry

## Feed Solution Purification
Before solvent extraction, feed solutions require purification cite:jha2016review:

1.  **Removal of bulk impurities**:
    - Fe³⁺ removal: pH adjustment to precipitate Fe(OH)₃ (pH 3-4)
    - Ca²⁺, Al³⁺: Precipitation or ion exchange
    - Radioactive elements (Th, U): Pre-extraction or precipitation
2.  **pH adjustment**:
    - Adjust to extraction pH (typically 0.5-4.0)
    - Buffer if needed (acetate, citrate buffers)
3.  **Concentration adjustment**:
    - Evaporation to increase REE concentration
    - Dilution if too concentrated
    - Target: 0.1-1.0 M total REE
