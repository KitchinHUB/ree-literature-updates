# FIXPLAN G29 — figure for ch. 11 (lanmodulin EF-hand)

## What was drawn

`tools/figures/fig_lanm_efhand.py` → `figures/11-lanm-efhand.svg`, wired into
`src/11-biological-biomimetic.md` as `fig-lanm-efhand` at the end of the
*Structural Basis of Selectivity* section (directly after the "Critical Proline
Residues" paragraph, before *Metal-Sensitive Dimerization*), and referred to from
a new paragraph as `[](#fig-lanm-efhand)`.

Three panels:

- **A — canonical Ca²⁺ EF-hand.** Helix–loop–helix scaffold, 12-residue binding
  loop, seven oxygen donors around Ca²⁺.
- **B — lanmodulin EF-hand.** Same scaffold, ten oxygen donors around Ln³⁺,
  Ln–O 2.5–2.7 Å, with the proline marked on the loop and labelled with the
  Pro→Ala result.
- **C — both selectivities on one affinity axis** (−log₁₀ K_d, so tighter is
  up). The ~10⁸ Ln³⁺/Ca²⁺ preference is eight units of the axis; the whole
  lanthanide series sits in a flat 0.4–10 pM band; the ~5× light-over-heavy
  preference is drawn *to scale* as a 0.7-log dashed tilt inside/below that
  band, where it is visibly smaller than the band's own width; and the panel
  states in text that the best adjacent-pair separation factor from any protein
  system is 1.4 (Nd/Pr) to 3.0 (Ce/La).

Panel C is the answer to the correctness constraint: it is impossible to read
the figure as "the site distinguishes neighbouring rare earths", because the
group gap and the intra-group tilt are on the same axis and differ by more than
seven orders of magnitude. The prose paragraph and the caption both say so
explicitly. The ~5× figure is attributed on the figure to the prototypal
Mex-LanM, and the 1.4–3.0 figures are attributed to "any protein system"
(they are LanD's, not lanmodulin's — the chapter is careful about that, and the
figure does not claim them for LanM).

## Where each structural detail came from

| Detail on the figure | Source |
| --- | --- |
| Four EF-hands, adjacent ones fused | chapter §Structural Basis of Selectivity → `cook2019structural` |
| Ln³⁺ coordination number 10 | same |
| Ln–O 2.5–2.7 Å | same (chapter says "La³⁺-ligand distances: 2.5-2.7 Å") |
| Donor types: Asp/Glu carboxylate (bidentate), Asn side chain (monodentate), backbone C=O | same |
| One proline per EF-hand; Pro→Ala restores the Ca²⁺ response | chapter §Critical Proline Residues → `cotruvo2018lanmodulin` |
| K_d = 0.4–10 pM for every Ln³⁺ and Y³⁺; Ca²⁺ response only near millimolar; ~10⁸ | chapter binding-properties table → `cotruvo2018lanmodulin` |
| ~5× light over heavy, whole series, Mex-LanM | chapter → `mattocks2023enhanced` |
| Adjacent-pair SF 1.4 (Nd/Pr) to 3.0 (Ce/La) | chapter → `larrinaga2024modulating` |
| Canonical Ca²⁺ EF-hand: helix–loop–helix, 12-residue loop, donors at loop positions 1, 3, 5, 7, 9, 12, bidentate carboxylate at 12, one water, CN 7 | **Gifford, Walsh & Vogel 2007** — see below |

## New reference needed (do not merge silently — this is the one ask)

`review/bib-additions/fig11.bib` contains a single entry,
`gifford2007structures` (Biochem. J. **405**, 199–221, 2007,
doi:10.1042/BJ20070255). DOI verified against the CrossRef REST API with the
required User-Agent; CrossRef returned the matching title, the three authors
(Gifford, Walsh, Vogel), the journal, volume 405, issue 2, pages 199–221, 2007.

It is needed because **nothing in the chapter and nothing currently in
`references.bib` states the canonical Ca²⁺ EF-hand's loop length, its
coordinating loop positions, or its coordination number of 7** — and that
contrast (7 vs 10) is the visual core of panels A/B. `references.bib` does have
`anon2001hand` ("EF-hand Calcium-Binding Proteins"), but it is an
author-less stub with a `10.1201/...` DOI that does not match the journal it
names, so I did not rely on it.

**Suggested follow-up for the orchestrator:** once `gifford2007structures` is
merged into `references.bib`, add `[@gifford2007structures]` to the figure
caption after "the canonical seven around Ca²⁺". I deliberately did **not**
put that key in the caption now, because an unresolvable citation key would
break or dirty the build, and I was told not to edit `references.bib` or run
the build.

## What I could not verify, and how the figure handles it

- **The composition of lanmodulin's ten donors.** The chapter names the three
  donor *types* but never says how many of each make up CN 10, and I found no
  statement of the breakdown in any source already cited. Rather than invent a
  plausible "3 bidentate + 2 monodentate + 2 carbonyl = 10", panel B draws ten
  undifferentiated oxygen donors and says on the panel itself: "the types of
  donor are known, how many of each is not drawn". The caption repeats it.
- **Geometry.** Neither panel is a structure. Donors are spaced evenly on a
  circle so the reader counts 7 against 10; the caption states in the first
  sentence of the (A, B) description that these are schematics, not crystal
  structures, and that the positions are not real geometry.
- **Residue identities and numbers.** No residue is named beyond what the
  chapter names (Asp/Glu, Asn, Pro), and no residue *numbers* are given for
  lanmodulin. Panel A's loop positions (1, 3, 5, 7, 9, 12) are positions within
  the canonical EF-hand loop, from Gifford 2007, not residue numbers in any
  particular protein. The chapter's "D9" engineering result was deliberately
  left off the figure: the chapter does not say whether D9 is the loop position
  or a sequence position, so drawing it would have been a guess.
- **Ca–O distances** are not stated anywhere in the chapter, so panel A carries
  no bond length; only panel B does, where the chapter supplies one.

## Proofing

Proofed visually via `FIG_PROOF=/tmp/figproof python3
tools/figures/fig_lanm_efhand.py` and inspecting
`/tmp/figproof/11-lanm-efhand.png` across four iterations. Fixed on the way:
the Pro annotation overlapping the loop label and the loop arc, the italic
inter-panel captions overlapping the coordination spheres, the panel-C series
annotation running outside the axes on the right, and the calcium label falling
below the axes into the tick labels. Final state: nothing overlaps, no text
falls outside an axes, and the smallest type is 6.5 pt on a 6.9 × 6.3 in figure.

## Files touched

- `tools/figures/fig_lanm_efhand.py` (new)
- `figures/11-lanm-efhand.svg` (generated)
- `src/11-biological-biomimetic.md` (one new paragraph + one figure directive)
- `review/bib-additions/fig11.bib` (new)
- `review/agent-reports/fig11.md` (this file)

Nothing else was edited; the build was not run and nothing was committed.
