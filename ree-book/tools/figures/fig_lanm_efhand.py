"""The lanmodulin EF-hand against the canonical calcium EF-hand (ch. 11).

The chapter's central claim about lanmodulin is that one number, ~10^8, belongs
to Ln/non-Ln selectivity and must never be read as Ln/Ln selectivity. A figure
of the binding site can very easily undo that, because a drawing of a snug
coordination pocket *looks* like an argument that the pocket picks elements.
It does not, and the figure is laid out so that it cannot be read that way:

*   Panels A and B put the two sites side by side. They share a fold, and they
    differ in the two respects the chapter names -- the size of the first
    coordination sphere (7 donors for Ca(II), 10 for Ln(III) in LanM) and the
    proline that sits in every LanM EF-hand loop and blocks the calcium
    response. That contrast is a charge-and-radius story, i.e. rare earth
    versus calcium, and it stops there.
*   Panel C is where the honesty lives. Affinity is plotted as -log Kd, so the
    ~10^8 preference for the rare earths over calcium is literally eight units
    of the same axis on which the entire lanthanide series is flat to within
    the band's own width. The ~5x light-over-heavy tilt is drawn to scale
    inside the band (0.7 log units), where it is visibly smaller than the
    spread of the reported Kd values -- which is the point.

Provenance of every drawn detail:

*   LanM site: four EF-hand motifs, adjacent pairs fused, La(III) coordination
    number 10, Ln-O 2.5-2.7 A, donors = Asn side chains (monodentate),
    Asp/Glu carboxylates (bidentate) and backbone carbonyls; a critical proline
    in each EF-hand whose mutation to alanine restores the calcium response.
    All from the chapter's "Structural Basis of Selectivity" section, sourced
    there to Cook et al. 2019 (cook2019structural) and Cotruvo et al. 2018.
    The chapter does NOT say how many donors of each type make up the ten, so
    the ten donor positions here are drawn undifferentiated and the panel says
    so. Inventing a 3-bidentate-plus-2-monodentate-plus-2-carbonyl breakdown
    would be fabricating a structure.
*   Canonical Ca(II) EF-hand: 12-residue loop, donors at loop positions
    1, 3, 5, 7, 9 and 12, bidentate carboxylate at 12, one water, coordination
    number 7. From Gifford, Walsh and Vogel, Biochem. J. 405, 199 (2007) --
    NOT yet in references.bib; the entry is filed in
    review/bib-additions/fig11.bib for the orchestrator to merge.
*   Panel C numbers: Kd 0.4-10 pM for every Ln(III) and Y(III), and a calcium
    response only near millimolar, from the chapter's binding-properties table
    (cotruvo2018lanmodulin); ~5x light-over-heavy for the prototypal
    Mex-LanM from mattocks2023enhanced; the 1.4-3.0 band for the best
    adjacent-pair separation factor from any protein system is the chapter's
    own summary of larrinaga2024modulating.

Nothing here is a crystal structure. The donor positions are spaced evenly
around a circle because the count is the message; the real geometry is not.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, PathPatch
from matplotlib.path import Path
import style

style.use()

CA = style.AQUEOUS
LN = style.ACCENT


# ---------------------------------------------------------------- schematics

def bezier(p0, p1, p2, p3, t):
    """Point on a cubic Bezier, used to hang the Pro marker on the loop."""
    t = np.asarray(t)[..., None] if np.ndim(t) else t
    return ((1 - t) ** 3 * np.asarray(p0) + 3 * (1 - t) ** 2 * t * np.asarray(p1)
            + 3 * (1 - t) * t ** 2 * np.asarray(p2) + t ** 3 * np.asarray(p3))


def helix_loop_helix(ax, loop_label, pro=False):
    """The shared scaffold: two helices and the metal-binding loop between."""
    for x0 in (0.75, 6.35):
        ax.add_patch(FancyBboxPatch((x0, 8.42), 2.9, 0.46,
                                    boxstyle="round,pad=0.06",
                                    fc="#efefec", ec=style.MUTED, lw=0.7,
                                    zorder=2))
    ax.text(2.20, 8.65, "helix", ha="center", va="center", fontsize=7.5,
            color=style.MUTED, zorder=3)
    ax.text(7.80, 8.65, "helix", ha="center", va="center", fontsize=7.5,
            color=style.MUTED, zorder=3)

    p0, p1, p2, p3 = (3.65, 8.65), (4.45, 7.15), (5.55, 7.15), (6.35, 8.65)
    ts = np.linspace(0, 1, 60)
    pts = np.array([bezier(p0, p1, p2, p3, t) for t in ts])
    ax.add_patch(PathPatch(Path(pts), fc="none", ec=style.MUTED, lw=1.3,
                           zorder=2))
    if loop_label:
        ax.text(5.0, 7.30, loop_label, ha="center", va="top", fontsize=7.5,
                color=style.MUTED)

    if pro:
        px, py = bezier(p0, p1, p2, p3, 0.24)
        ax.plot([px], [py], marker="o", ms=5.0, color=LN, zorder=4)
        ax.annotate("Pro", xy=(px, py), xytext=(3.45, 7.92), fontsize=8,
                    color=LN, ha="right", va="center",
                    arrowprops=dict(arrowstyle="-", color=LN, lw=0.8,
                                    shrinkA=3, shrinkB=4))
        ax.text(5.0, 7.30, "one Pro per loop; Pro$\\rightarrow$Ala restores "
                           "the Ca$^{2+}$ response",
                ha="center", va="top", fontsize=7.5, color=LN)


def sphere(ax, n, ion, color, cx=5.0, cy=4.45, r_ion=0.60, r_don=1.95):
    """n oxygen donors, evenly spaced, drawn around one ion."""
    ang = np.linspace(90, 450, n, endpoint=False)
    for a in np.radians(ang):
        dx, dy = cx + r_don * np.cos(a), cy + r_don * np.sin(a)
        ax.plot([cx + r_ion * np.cos(a), dx - 0.21 * np.cos(a)],
                [cy + r_ion * np.sin(a), dy - 0.21 * np.sin(a)],
                color=style.MUTED, lw=0.7, zorder=1)
        ax.add_patch(Circle((dx, dy), 0.25, fc=style.GROUND, ec=style.INK,
                            lw=0.9, zorder=3))
        ax.text(dx, dy, "O", ha="center", va="center", fontsize=6.5,
                color=style.INK, zorder=4)
    ax.add_patch(Circle((cx, cy), r_ion, fc=color, ec="none", zorder=3))
    ax.text(cx, cy, ion, ha="center", va="center", fontsize=8.5,
            color=style.GROUND, zorder=4)


def block(ax, lines, y0=2.15, dy=0.42, x=0.35):
    for i, (txt, col, size) in enumerate(lines):
        ax.text(x, y0 - i * dy, txt, ha="left", va="top", fontsize=size,
                color=col)


fig = plt.figure(figsize=(6.9, 6.3))
gs = fig.add_gridspec(2, 2, height_ratios=[1.30, 1.0], hspace=0.16,
                      wspace=0.10)

axA = fig.add_subplot(gs[0, 0])
axB = fig.add_subplot(gs[0, 1])
for ax in (axA, axB):
    style.blank(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")

axA.set_title("A   canonical Ca$^{2+}$ EF-hand", loc="left", fontsize=9.5,
              color=style.INK, pad=6)
helix_loop_helix(axA, "12-residue binding loop")
sphere(axA, 7, "Ca$^{2+}$", CA)
block(axA, [
    ("coordination number 7", style.INK, 8.5),
    ("donors: side-chain O at loop positions 1, 3, 5;", style.MUTED, 7.5),
    ("backbone C=O at 7; one H$_2$O; a bidentate", style.MUTED, 7.5),
    ("carboxylate at 12", style.MUTED, 7.5),
])

axB.set_title("B   lanmodulin EF-hand", loc="left", fontsize=9.5,
              color=style.INK, pad=6)
helix_loop_helix(axB, "", pro=True)
sphere(axB, 10, "Ln$^{3+}$", LN)
block(axB, [
    ("coordination number 10,  Ln$-$O 2.5$-$2.7 Å", style.INK, 8.5),
    ("donors: Asp/Glu carboxylate O (bidentate),", style.MUTED, 7.5),
    ("Asn side-chain O (monodentate), backbone C=O", style.MUTED, 7.5),
    ("four EF-hands, adjacent ones fused; the types of", style.MUTED, 7.5),
    ("donor are known, how many of each is not drawn", style.MUTED, 7.5),
])


# ------------------------------------------------------------------ panel C

axC = fig.add_subplot(gs[1, :])

SERIES = ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho",
          "Er", "Tm", "Yb", "Lu"]
xs = np.arange(len(SERIES))
X_CA = 18.0

# Kd = 0.4-10 pM  ->  -log10 Kd = 12.4 down to 11.0.
axC.fill_between([-0.55, 14.55], 11.0, 12.4, color=LN, alpha=0.16, lw=0)
axC.plot([-0.55, 14.55], [12.4, 12.4], color=LN, lw=0.9)
axC.plot([-0.55, 14.55], [11.0, 11.0], color=LN, lw=0.9)
axC.text(7.0, 12.52, "$K_\\mathrm{d}$ = 0.4$-$10 pM for every Ln$^{3+}$ "
                     "and Y$^{3+}$",
         ha="center", va="bottom", fontsize=8, color=LN)

# The intra-series preference, drawn to scale and inside the band, because it
# is a tilt within these affinities and not a separate, weaker set of them:
# 5x is 0.7 log units, half the height of the band that contains it.
axC.plot([0, 14], [12.05, 11.35], color=LN, lw=1.2, ls=(0, (4, 3)))
axC.annotate("$\\approx$5$\\times$ light over heavy, whole series (Mex-LanM):\n"
             "the tilt is half the width of the band that contains it",
             xy=(11.0, 11.50), xytext=(7.0, 10.15), fontsize=8, color=LN,
             ha="center", va="top",
             arrowprops=dict(arrowstyle="-", color=LN, lw=0.7,
                             shrinkA=4, shrinkB=2))
axC.text(7.0, 8.05, "best adjacent-pair separation factor from any protein\n"
                    "system: 1.4 (Nd/Pr) to 3.0 (Ce/La)",
         ha="center", va="top", fontsize=8, color=style.MUTED)

# Calcium: a response only near millimolar.
axC.plot([X_CA - 0.75, X_CA + 0.75], [3.0, 3.0], color=CA, lw=3.0,
         solid_capstyle="butt")
axC.text(X_CA, 3.30, "response only\nnear millimolar", ha="center",
         va="bottom", fontsize=7.5, color=CA)

axC.add_patch(FancyArrowPatch((16.2, 3.1), (16.2, 11.6), arrowstyle="<|-|>",
                              mutation_scale=10, color=style.INK, lw=1.1,
                              shrinkA=0, shrinkB=0))
axC.text(16.55, 8.4, "$\\approx$10$^{8}$\nLn$^{3+}$ over Ca$^{2+}$\n"
                     "(the group selectivity)",
         ha="left", va="center", fontsize=8, color=style.INK)

axC.axvline(15.35, color=style.FAINT, lw=0.8)
axC.set_xticks(list(xs) + [X_CA])
axC.set_xticklabels(SERIES + ["Ca$^{2+}$"], fontsize=7.5)
axC.get_xticklabels()[-1].set_color(CA)
axC.set_xlim(-1.1, 19.8)
axC.set_ylim(1.9, 13.2)
axC.set_yticks([3, 5, 7, 9, 11, 13])
axC.set_ylabel("affinity,  $-\\log_{10} K_\\mathrm{d}$\n"
               "(12 = 1 pM,  3 = 1 mM)", fontsize=8)
axC.set_title("C   eight decades separate the group from calcium; across the "
              "series the site is flat", loc="left", fontsize=9.5,
              color=style.INK, pad=6)

style.save(fig, "11-lanm-efhand")
