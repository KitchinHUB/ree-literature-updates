"""log D against pH for a cation-exchange extractant (ch. 3).

Everything drawn here follows from the mass-action expression in ch. 13,

    log D = log K_ex + 3 log[(HL)_2]_org + 3 pH,

so the lines are the equation, not fitted data. The figure has to carry two
facts at once: the slope is +3, and the horizontal offset between neighbours
is Delta pH_1/2 = (log beta) / 3, which for beta = 1.5 is 0.06 pH units. At
full scale that offset is invisible, which is itself the point, so the inset
zooms on it rather than exaggerating it in the main panel.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
import style

style.use()

BETA = 1.5           # a representative adjacent-pair separation factor
LOG_KEX_A = -1.8     # placed so that D = 1 falls in the middle of the panel
DIMER = -1.0         # log[(HL)2] in the organic phase

pH = np.linspace(0.0, 2.4, 500)
logD_A = LOG_KEX_A + 3 * DIMER + 3 * pH
logD_B = logD_A + np.log10(BETA)

# pH_1/2 for each element: where log D = 0.
ph_A = (0.0 - LOG_KEX_A - 3 * DIMER) / 3
ph_B = (0.0 - LOG_KEX_A - np.log10(BETA) - 3 * DIMER) / 3

fig, ax = plt.subplots(figsize=(5.4, 3.6))


def draw_lines(a, lw=1.6):
    a.plot(pH, logD_A, color=style.AQUEOUS, lw=lw, label="lighter neighbour")
    a.plot(pH, logD_B, color=style.ORGANIC, lw=lw, label="heavier neighbour")


draw_lines(ax)
ax.axhline(0.0, color=style.MUTED, lw=0.8, ls=(0, (4, 3)), zorder=0)
ax.text(0.05, 0.08, "$D = 1$", color=style.MUTED, fontsize=8)

# Slope triangle, drawn to scale on the lighter neighbour's line: one pH unit
# of the horizontal leg buys three decades of the vertical one.
xa, xb = 1.00, 2.00
ya = LOG_KEX_A + 3 * DIMER + 3 * xa
yb = ya + 3.0
ax.plot([xa, xb, xb], [ya, ya, yb], color=style.MUTED, lw=0.9, zorder=1)
ax.text((xa + xb) / 2, ya - 0.22, "1 pH unit", color=style.MUTED,
        fontsize=8, ha="center", va="top")
ax.text(xb + 0.07, (ya + yb) / 2, "3 decades in $D$", color=style.MUTED,
        fontsize=8, ha="center", va="center", rotation="vertical")

# The gap the whole industry is built on, at true scale in an inset.
pad_x, pad_y = 0.075, 0.30
zx0, zx1 = ph_B - pad_x, ph_A + pad_x
axi = ax.inset_axes([0.055, 0.07, 0.40, 0.36],
                    xlim=(zx0, zx1), ylim=(-pad_y, pad_y),
                    xticks=[], yticks=[])
draw_lines(axi, lw=1.3)
axi.axhline(0.0, color=style.MUTED, lw=0.7, ls=(0, (4, 3)), zorder=0)
for x, c in ((ph_A, style.AQUEOUS), (ph_B, style.ORGANIC)):
    axi.plot([x], [0.0], marker="o", ms=4.5, color=c, zorder=5)
    axi.plot([x, x], [-pad_y, 0.0], color=c, lw=0.7, ls=(0, (2, 2)), zorder=1)
axi.annotate("", xy=(ph_A, -0.17), xytext=(ph_B, -0.17),
             arrowprops=dict(arrowstyle="<|-|>", color=style.ACCENT, lw=1.0,
                             shrinkA=0, shrinkB=0, mutation_scale=8))
axi.text((ph_A + ph_B) / 2, -0.13, "0.06", color=style.ACCENT, fontsize=8,
         ha="center", va="bottom")
axi.set_title(r"$\Delta \mathrm{pH}_{1/2} = (\log \beta)/3$",
              fontsize=8, color=style.INK, pad=3)
for s in axi.spines.values():
    s.set_visible(True)
    s.set_color(style.FAINT)
axi.set_facecolor(style.GROUND)

ind = ax.indicate_inset_zoom(axi, edgecolor=style.FAINT, alpha=1.0, lw=0.8)
for ln in ind.connectors:
    ln.set(color=style.FAINT, lw=0.7)

ax.set_xlabel("equilibrium aqueous pH")
ax.set_ylabel(r"$\log D$")
ax.set_xlim(0.0, 2.4)
ax.set_ylim(-2.4, 2.4)
ax.legend(loc="upper left", frameon=False, fontsize=8)
ax.set_title(r"A separation factor of 1.5 is a 0.06 pH-unit gap",
             loc="left", color=style.INK)

style.save(fig, "03-logd-vs-ph")
