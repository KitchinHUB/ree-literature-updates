"""The coacervate phase window and the loop it is supposed to buy (ch. 8).

The chapter makes exactly one topological claim about the phase diagram, and
this figure draws that claim and nothing more:

    "Phase diagrams for coacervate systems typically show a two-phase region at
    intermediate ionic strengths, bounded by a single-phase region at very low
    salt (kinetically trapped precipitates) and at high salt (electrostatic
    screening suppresses coacervation)."  [sing2020progress, ch. 8]

So salt is the vertical axis, total polymer the horizontal one, tie lines are
horizontal (both coexisting phases sit at the same ionic strength), and the
two-phase dome closes at a critical salt concentration above which the charges
are screened and there is nothing to separate. That much is standard for
complex coacervation [wang2014polyelectrolyte, sing2020progress].

**The binodal here is schematic.** The chapter reports no measured binodal for
any REE-relevant system, so drawing one with numbers on it would be an
invention. Both axes therefore carry direction arrows and no tick values. What
is taken from the chapter is the *topology*: that the two-phase region exists,
that it is bounded above by a critical salt concentration, that it is bounded
below by a regime where the complex is a kinetically trapped precipitate rather
than a liquid, and that the metal partitions into the dense phase. The curve
shape (an asymmetric mean-field dome, dilute branch hugging the axis) is drawn
for illustration.

Panel (b) is the operating loop, and it is the reason the chapter cares: the
whole claim of coacervate extraction is that both phases are water, so the loop
replaces the kerosene diluent while leaving the extraction chemistry to
ligands. The strip step is the chapter's stimuli-responsive section - salt,
temperature (cloud point, LCST) or pH all move the system out of the dome
[love2020reversible; favrerguillon2004cloud; kumar2023comprehensive]. The two
caveats printed under it are the chapter's own: lower metal loading than an
organic extractant, and polymer recovery as a cost line.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import style

style.use()

# ---------------------------------------------------------------- binodal
# Schematic, not fitted. Salt is scaled so the critical point sits at 1.0;
# the exponents give the usual asymmetric dome with the dilute branch pressed
# against the axis. No number here is a measurement, which is why no axis
# carries tick values.
S_C = 1.00           # critical salt concentration (top of the dome)
S_PPT = 0.12         # below this the complex is a trapped solid, not a liquid
PHI_CR = 0.26        # polymer concentration at the critical point

s = np.linspace(S_PPT, S_C, 400)
u = 1.0 - s / S_C
phi_dil = PHI_CR * (1.0 - 0.93 * u ** 0.55)
phi_coa = PHI_CR * (1.0 + 2.20 * u ** 0.62)


def branches(sv):
    uv = 1.0 - sv / S_C
    return (PHI_CR * (1.0 - 0.93 * uv ** 0.55),
            PHI_CR * (1.0 + 2.20 * uv ** 0.62))


fig = plt.figure(figsize=(7.6, 4.0))
gs = fig.add_gridspec(1, 2, width_ratios=[1.18, 1.0], wspace=0.16)
axA = fig.add_subplot(gs[0, 0])
axB = fig.add_subplot(gs[0, 1])

# ------------------------------------------------------------- panel (a)
XMAX, YMAX = 1.12, 1.42
axA.set_xlim(0, XMAX)
axA.set_ylim(0, YMAX)
axA.set_xticks([])
axA.set_yticks([])
for sp in ("top", "right"):
    axA.spines[sp].set_visible(False)

# The low-salt strip, where the chapter says you get a precipitate instead.
axA.axhspan(0, S_PPT, color="#f0f0ee", zorder=0)
axA.text(XMAX - 0.02, S_PPT / 2,
         "very low salt: kinetically trapped precipitate",
         ha="right", va="center", fontsize=7.5, color=style.MUTED, zorder=2)

# The two-phase region.
axA.fill_betweenx(s, phi_dil, phi_coa, color=style.ACCENT, alpha=0.09,
                  lw=0, zorder=1)
axA.plot(phi_dil, s, color=style.ACCENT, lw=1.5, zorder=3)
axA.plot(phi_coa, s, color=style.ACCENT, lw=1.5, zorder=3)
axA.plot([PHI_CR], [S_C], marker="o", ms=4.5, mfc=style.GROUND,
         mec=style.ACCENT, mew=1.2, zorder=5)
axA.text(PHI_CR + 0.035, S_C + 0.01, "critical point", fontsize=7.5,
         color=style.ACCENT, ha="left", va="bottom")

axA.text(0.325, 0.72, "two phases", fontsize=8.5, color=style.ACCENT,
         ha="center", va="center")
axA.text(0.02, 1.40, "one phase:\nsalt screens the charges",
         fontsize=7.5, color=style.MUTED, ha="left", va="top")

# The operating tie line: both coexisting phases at one ionic strength.
S_OP = 0.45
d_op, c_op = branches(S_OP)
axA.plot([d_op, c_op], [S_OP, S_OP], color=style.INK, lw=0.9,
         ls=(0, (4, 3)), zorder=4)
axA.plot([d_op], [S_OP], marker="o", ms=6, color=style.AQUEOUS, zorder=6)
axA.plot([c_op], [S_OP], marker="o", ms=8, color=style.ACCENT, zorder=6)
axA.text(d_op + 0.02, S_OP - 0.03, "supernatant\ndilute, REE-poor",
         fontsize=7.5, color=style.AQUEOUS, ha="left", va="top")
axA.text(c_op + 0.03, S_OP - 0.03, "coacervate\ndense, REE-rich",
         fontsize=7.5, color=style.ACCENT, ha="left", va="top")
axA.annotate("", xy=(c_op - 0.03, S_OP + 0.050),
             xytext=(d_op + 0.03, S_OP + 0.050),
             arrowprops=dict(arrowstyle="-|>", color=style.INK, lw=0.9,
                             shrinkA=0, shrinkB=0, mutation_scale=9))
axA.text((d_op + c_op) / 2, S_OP + 0.080, "REE follows the dense phase",
         fontsize=7.5, color=style.INK, ha="center", va="bottom")

# Strip: raise the salt (or the temperature, or drop the pH) and the dense
# phase walks straight out of the dome.
axA.add_patch(FancyArrowPatch((c_op, S_OP + 0.04), (c_op, 1.05),
                              arrowstyle="-|>", mutation_scale=11,
                              color=style.GOOD, lw=1.3, shrinkA=0, shrinkB=0,
                              zorder=6))
axA.text(c_op + 0.035, 0.80, "add salt,\nheat past the\ncloud point,\n"
                             "or drop pH",
         fontsize=7.5, color=style.GOOD, ha="left", va="center")
axA.text(c_op, 1.08, "REE released", fontsize=7.5, color=style.GOOD,
         ha="center", va="bottom")

axA.set_xlabel("total polymer concentration $\\longrightarrow$")
axA.set_ylabel("salt concentration $\\longrightarrow$")
axA.set_title("(a)  salt sets the window (schematic)", loc="left",
              color=style.INK, fontsize=9.5)

# ------------------------------------------------------------- panel (b)
style.blank(axB)
axB.set_xlim(0, 10)
axB.set_ylim(0, 8.8)

BX = 5.75
ROWS = (8.05, 6.30, 4.55, 2.80)


def station(y, text, color):
    axB.text(BX, y, text, ha="center", va="center", fontsize=8,
             color=style.INK, linespacing=1.35,
             bbox=dict(boxstyle="round,pad=0.42", fc=style.GROUND,
                       ec=color, lw=1.0), zorder=4)


def down(y0, y1, color=style.INK):
    axB.add_patch(FancyArrowPatch((BX, y0), (BX, y1), arrowstyle="-|>",
                                  mutation_scale=10, color=color, lw=1.0,
                                  shrinkA=0, shrinkB=0, zorder=3))


station(ROWS[0], "1   mix polycation + polyanion\ninto the leach liquor",
        style.FAINT)
station(ROWS[1], "2   coacervate droplets form\nREE partitions into them",
        style.ACCENT)
station(ROWS[2], "3   settle: dense phase out,\nspent supernatant discarded",
        style.FAINT)
station(ROWS[3], "4   strip: leave the dome,\nREE into a small liquor",
        style.GOOD)

down(ROWS[0] - 0.58, ROWS[1] + 0.58)
down(ROWS[1] - 0.58, ROWS[2] + 0.58)
down(ROWS[2] - 0.58, ROWS[3] + 0.58, style.GOOD)
axB.text(BX + 0.25, (ROWS[1] + ROWS[2]) / 2,
         "tie line in (a)", fontsize=7.5, color=style.MUTED,
         ha="left", va="center")
axB.text(BX + 0.25, (ROWS[2] + ROWS[3]) / 2,
         "arrow up in (a)", fontsize=7.5, color=style.GOOD,
         ha="left", va="center")

# The return leg: this is the claim the whole approach rests on.
axB.plot([BX - 3.05, 0.85], [ROWS[3], ROWS[3]], color=style.GOOD, lw=1.0,
         zorder=2)
axB.plot([0.85, 0.85], [ROWS[3], ROWS[0]], color=style.GOOD, lw=1.0, zorder=2)
axB.add_patch(FancyArrowPatch((0.85, ROWS[0]), (BX - 3.05, ROWS[0]),
                              arrowstyle="-|>", mutation_scale=10,
                              color=style.GOOD, lw=1.0, shrinkA=0, shrinkB=0,
                              zorder=2))
axB.text(1.20, (ROWS[0] + ROWS[3]) / 2, "polymer desalted and returned",
         rotation="vertical", ha="left", va="center", fontsize=7.5,
         color=style.GOOD)

axB.text(0.0, 1.20,
         "Every stream here is water. The loop replaces\n"
         "the kerosene diluent, not the chemistry.",
         fontsize=8, color=style.INK, ha="left", va="bottom")
axB.text(0.0, 0.10,
         "Costs the chapter names: lower metal loading\n"
         "than an organic extractant, and polymer recovery.",
         fontsize=7.5, color=style.MUTED, ha="left", va="bottom")

axB.set_title("(b)  load, split, strip, return", loc="left", color=style.INK,
              fontsize=9.5)

style.save(fig, "08-coacervate-phase-diagram")
