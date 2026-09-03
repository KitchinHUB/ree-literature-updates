"""The five-step extraction thermodynamic cycle (ch. 13).

This replaces the ASCII drawing in the chapter. Two things have to survive the
redraw, because both are load-bearing:

1.  The three protons appear explicitly at the top-right corner and leave at
    the bottom-right one. The version of the cycle that omits them is short by
    roughly +4,000 kJ/mol of gas-phase deprotonation, and that is the chapter's
    first named failure mode.
2.  The two largest terms have opposite signs and nearly cancel. The figure
    prints them at the same size so the reader can see that the answer is a
    small residual of large numbers, not a large term with corrections.

Numbers are the La + D2EHPA column of the chapter's table: dehydration from
Marcus 1991, proton hydration from Tissandier 1998, the two solvation terms
estimated from implicit solvation.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import style

style.use()

fig, ax = plt.subplots(figsize=(6.4, 4.0))
style.blank(ax)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7.2)

TOP, BOT = 5.60, 1.55
LX, RX = 2.35, 7.75


def corner(x, y, text, color):
    ax.text(x, y, text, ha="center", va="center", fontsize=9, color=color,
            bbox=dict(boxstyle="round,pad=0.34", fc=style.GROUND,
                      ec=style.FAINT, lw=0.8), zorder=4)


def arrow(x0, y0, x1, y1, color, lw=1.1):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                 mutation_scale=11, color=color, lw=lw,
                                 shrinkA=0, shrinkB=0, zorder=3))


# The gas-phase band, drawn so the reader sees the reference state as a place.
ax.add_patch(FancyBboxPatch((0.35, TOP - 0.68), 9.3, 1.36,
                            boxstyle="round,pad=0.02", fc="#f5f5f3",
                            ec="none", zorder=0))
ax.text(0.62, TOP, "gas phase",
        fontsize=8, color=style.MUTED, ha="center", va="center",
        rotation="vertical")

corner(LX, TOP, r"REE$^{3+}$(g) + 3 HL(g)", style.INK)
corner(RX, TOP, r"REEL$_3$(g) + 3 H$^+$(g)", style.INK)
corner(LX, BOT, r"REE$^{3+}$(aq) + 3 HL(org)", style.INK)
corner(RX, BOT, r"REEL$_3$(org) + 3 H$^+$(aq)", style.INK)

# Up the left side: two separate desolvations, drawn separately because they
# are estimated separately.
arrow(LX - 1.05, BOT + 0.42, LX - 1.05, TOP - 0.42, style.AQUEOUS)
ax.text(LX - 1.22, (TOP + BOT) / 2, r"$\Delta G_1$  dehydrate REE$^{3+}$",
        rotation="vertical", ha="right", va="center", fontsize=8,
        color=style.AQUEOUS)
ax.text(LX - 0.90, (TOP + BOT) / 2, "+3145", rotation="vertical",
        ha="left", va="center", fontsize=9, color=style.AQUEOUS)

arrow(LX + 1.05, BOT + 0.42, LX + 1.05, TOP - 0.42, style.ORGANIC)
ax.text(LX + 0.90, (TOP + BOT) / 2, r"$\Delta G_4$  desolvate 3 HL",
        rotation="vertical", ha="right", va="center", fontsize=8,
        color=style.ORGANIC)
ax.text(LX + 1.22, (TOP + BOT) / 2, "+200", rotation="vertical",
        ha="left", va="center", fontsize=9, color=style.ORGANIC)

# Down the right side.
arrow(RX - 1.05, TOP - 0.42, RX - 1.05, BOT + 0.42, style.ORGANIC)
ax.text(RX - 1.22, (TOP + BOT) / 2, r"$\Delta G_3$  solvate REEL$_3$",
        rotation="vertical", ha="right", va="center", fontsize=8,
        color=style.ORGANIC)
ax.text(RX - 0.90, (TOP + BOT) / 2, "$-$120", rotation="vertical",
        ha="left", va="center", fontsize=9, color=style.ORGANIC)

arrow(RX + 1.05, TOP - 0.42, RX + 1.05, BOT + 0.42, style.AQUEOUS)
ax.text(RX + 0.90, (TOP + BOT) / 2, r"$\Delta G^{\circ}_5$  hydrate 3 H$^+$",
        rotation="vertical", ha="right", va="center", fontsize=8,
        color=style.AQUEOUS)
ax.text(RX + 1.22, (TOP + BOT) / 2, "$-$3312", rotation="vertical",
        ha="left", va="center", fontsize=9, color=style.AQUEOUS)

# Across the top: the one term that has to be computed.
arrow(LX + 1.95, TOP, RX - 1.95, TOP, style.ACCENT, lw=1.3)
ax.text((LX + RX) / 2, TOP + 0.52,
        r"$\Delta G_2$  complexation $+$ 3 deprotonation",
        ha="center", va="bottom", fontsize=8.5, color=style.ACCENT)
ax.text((LX + RX) / 2, TOP + 0.20,
        "computed (DFT or surrogate)", ha="center", va="bottom", fontsize=8,
        color=style.ACCENT)

# Across the bottom: the thing an experiment actually returns.
arrow(LX + 2.05, BOT, RX - 2.05, BOT, style.INK, lw=1.3)
ax.text((LX + RX) / 2, BOT + 0.22, "net extraction", ha="center",
        va="bottom", fontsize=8.5, color=style.INK)
ax.text((LX + RX) / 2, BOT - 0.40,
        r"$\Delta G^{\circ} = -87 + \Delta G_2$   (what $\log K_{ex}$ measures)",
        ha="center", va="top", fontsize=8, color=style.MUTED)

# The point of the whole diagram.
ax.text(5.0, 0.02,
        "The two largest terms, $+3145$ and $-3312$ kJ/mol, cancel to within "
        "5%.\nThe answer is their residual, so $\\Delta G_2$ must be right to "
        "about 1% of its own parts.",
        ha="center", va="bottom", fontsize=8, color=style.INK)

ax.text(0.35, 6.95, "Charge is $+3$ on both sides at every corner; the three "
                   "protons are not optional bookkeeping.",
        fontsize=8, color=style.MUTED, ha="left", va="center")

style.save(fig, "13-thermo-cycle")
