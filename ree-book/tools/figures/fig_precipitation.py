"""Hydroxide precipitation pH across the lanthanide series (ch. 10).

The chapter's own numbers set the terms of this figure, and the honest thing to
do is draw exactly what they support and nothing more.

*   The chapter's "Industrial pH Thresholds" table gives **three** ranges for
    the rare earths and no per-element values: light REE 6.8-7.5, heavy REE
    7.0-8.0, Y 6.5-7.5. There is no series of fourteen precipitation pH values
    to plot, so none is plotted. The bands are drawn as bands, flat across the
    elements they cover, because that is the resolution of the data. Drawing a
    smooth curve through them would invent fourteen numbers the chapter does
    not have, and the shape of that curve would then be doing the arguing.
*   The three ranges all contain pH 7.0-7.5, and the chapter's own process
    tolerance is +/-0.2 pH units — a 0.4-unit window, wider than the 0.35-unit
    offset between the two group midpoints. That is the whole argument for why
    one precipitation step is a group split: it is not that the separation is
    difficult, it is that the target ranges overlap by more than the process
    can hold. The inset makes that overlap the subject.
*   The exception is cerium, and it is drawn as a discontinuity rather than a
    trend: Ce(3+) -> Ce(4+) (E = 1.74 V) and Ce(OH)4 comes out at pH 3-5,
    roughly three pH units below where its neighbours come out, against the
    0.35 units the entire lanthanide contraction is worth. Oxidation state is a
    threshold; radius is a gradient. That contrast is the chapter's thesis and
    it is the one thing in the figure that must be visible at a glance.

Every number is from ch. 10: the three REE ranges and the impurity window
(Fe 2.5-3.5, Th 3.5-4.5, Al 4.0-5.0, U 4.0-5.5) from the pH-threshold table;
pH 3-5 and 80-95 % Ce with < 5 % other-REE loss from the H2O2 performance
table; E = 1.74 V from the cerium half-reaction; +/-0.2 pH control from the
process-parameter list; "above pH 9.5 all REE hydroxides have similar low
solubility" from the solubility-trends list. The 0.03 pH per neighbour figure
is labelled in the panel as implied rather than measured, because it is 0.35
divided by fourteen steps and nothing more.

Y is placed between Ho and Er. The chapter says only that Y "behaves as HREE";
the position is by six-coordinate ionic radius, Y(3+) 0.900 A against Ho(3+)
0.901 and Er(3+) 0.890 [@shannon1976revised], the same source ch. 1 uses for
the contraction. Pm is drawn muted: it has no place in any real feed, and the
group band covers it only nominally.

No solubility product is plotted. The chapter tabulates saturation indices for
lanthanum alone (La-oxalate and La-hydroxide at pH 7 and 8) and gives no Ksp
for the series, so there is no traceable basis for computed solubility curves
and none are drawn.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import style

style.use()

# --- the chapter's numbers -------------------------------------------------
LREE = (6.8, 7.5)      # "Light REEs", pH-threshold table
HREE = (7.0, 8.0)      # "Heavy REEs"
YTTRIUM = (6.5, 7.5)   # "Y ... behaves as HREE"
CE_IV = (3.0, 5.0)     # Ce(OH)4 window, H2O2 method
NO_SELECTIVITY = 9.5   # above this, all REE hydroxides are similarly insoluble
CONTROL = 0.2          # pH control precision, +/- units

ELEMENTS = ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu",
            "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]
X = {e: i for i, e in enumerate(ELEMENTS)}
X_Y = 10.5             # Y by ionic radius, between Ho and Er
LIGHT = (X["La"] - 0.45, X["Eu"] + 0.45)   # book convention: La-Eu light,
HEAVY = (X["Gd"] - 0.45, X["Lu"] + 0.45)   # Gd-Lu (+Y) heavy

fig, ax = plt.subplots(figsize=(6.6, 4.5))
X0, X1 = -1.0, 15.2
Y0, Y1 = 2.55, 11.0
ax.set_xlim(X0, X1)
ax.set_ylim(Y0, Y1)


def band(xspan, yspan, color, alpha=0.20):
    ax.add_patch(Rectangle((xspan[0], yspan[0]), xspan[1] - xspan[0],
                           yspan[1] - yspan[0], fc=color, alpha=alpha,
                           ec="none", zorder=1))
    for y in yspan:
        ax.plot(xspan, [y, y], color=color, lw=1.1, zorder=2)


band(LIGHT, LREE, style.AQUEOUS)
band(HEAVY, HREE, style.ORGANIC)
ax.text(2.6, sum(LREE) / 2, "light REE   6.8$-$7.5", ha="center", va="center",
        fontsize=8, color=style.AQUEOUS, zorder=4)
ax.text(12.9, 7.28, "heavy REE   7.0$-$8.0", ha="center", va="center",
        fontsize=8, color=style.ORGANIC, zorder=4)

# Yttrium: one value, at the radius it actually has.
ax.plot([X_Y, X_Y], YTTRIUM, color=style.INK, lw=1.4, zorder=5,
        solid_capstyle="butt")
for y in YTTRIUM:
    ax.plot([X_Y - 0.16, X_Y + 0.16], [y, y], color=style.INK, lw=1.4, zorder=5)
ax.text(X_Y, YTTRIUM[1] + 0.09, "Y", ha="center", va="bottom", fontsize=8,
        color=style.INK, zorder=5)

# The one place the series is not a gradient.
xc = X["Ce"]
band((xc - 0.5, xc + 0.5), CE_IV, style.ACCENT, alpha=0.22)
ax.annotate("", xy=(xc, CE_IV[1] + 0.12), xytext=(xc, LREE[0] - 0.12),
            arrowprops=dict(arrowstyle="-|>", color=style.ACCENT, lw=1.3,
                            shrinkA=0, shrinkB=0, mutation_scale=11))
ax.text(xc, sum(CE_IV) / 2, "Ce(IV)\n3$-$5", ha="center", va="center",
        fontsize=8, color=style.ACCENT, zorder=4)

ax.text(1.75, 6.45,
        "Ce$^{3+}\\rightarrow$Ce$^{4+}$ ($E^{\\circ}$ = 1.74 V), then "
        "Ce(OH)$_4$ at pH 3$-$5:\n80$-$95 % of the cerium, other REE losses "
        "under 5 %.",
        ha="left", va="top", fontsize=8, color=style.ACCENT)
ax.text(1.75, 5.72,
        "Oxidation state is a threshold;\n"
        "radius is a gradient. Fe, Th, Al\n"
        "and U come out over this same\n"
        "2.5$-$5.5 window, so cerium is last.",
        ha="left", va="top", fontsize=7.5, color=style.MUTED)

# Where the handle runs out altogether.
ax.plot([X0, X1], [NO_SELECTIVITY] * 2, color=style.MUTED, lw=0.8,
        ls=(0, (4, 3)), zorder=1)
ax.text(X1 - 0.15, NO_SELECTIVITY + 0.10,
        "above pH 9.5 every REE hydroxide is similarly insoluble",
        ha="right", va="bottom", fontsize=7.5, color=style.MUTED)

ax.text(X0 + 0.15, Y1 - 0.10,
        "The chapter reports two group ranges and one value for Y. There are "
        "no per-element\nprecipitation pH values, so none are drawn: the bands "
        "are flat because the data is.",
        ha="left", va="top", fontsize=8, color=style.MUTED)

# --- the inset: the ranges laid on the pH axis they share ------------------
axi = ax.inset_axes([0.545, 0.055, 0.435, 0.255],
                    xlim=(6.32, 8.18), ylim=(0.0, 4.6), yticks=[])
axi.axvspan(7.0, 7.5, color=style.FAINT, zorder=0)
for (lo, hi), yb, color, lw in ((LREE, 3.55, style.AQUEOUS, 0.42),
                                (HREE, 2.75, style.ORGANIC, 0.42),
                                (YTTRIUM, 1.95, style.INK, 0.42)):
    axi.add_patch(Rectangle((lo, yb), hi - lo, lw, fc=color, alpha=0.55,
                            ec=color, lw=0.9, zorder=3))
axi.add_patch(Rectangle((7.2 - CONTROL, 0.72), 2 * CONTROL, 0.42,
                        fc=style.GROUND, ec=style.MUTED, lw=0.9,
                        hatch="////", zorder=3))
axi.text(7.47, 0.93, "$\\pm$0.2 pH control", ha="left", va="center",
         fontsize=7, color=style.MUTED)
axi.set_title("all three ranges contain pH 7.0$-$7.5", fontsize=8,
              color=style.INK, pad=3)
axi.set_xticks([6.5, 7.0, 7.5, 8.0])
axi.tick_params(labelsize=7)
for s in axi.spines.values():
    s.set_visible(True)
    s.set_color(style.FAINT)
axi.set_facecolor(style.GROUND)

ax.text(X0 + 0.15, 9.28,
        "The two group midpoints are 0.35 pH apart, over fourteen steps: about "
        "0.03 pH per neighbour,\nimplied and never measured — and the whole "
        "0.35 is narrower than the 0.4-unit control window.",
        ha="left", va="top", fontsize=8, color=style.INK)

ax.set_xticks(range(len(ELEMENTS)))
ax.set_xticklabels(ELEMENTS)
for lbl, e in zip(ax.get_xticklabels(), ELEMENTS):
    if e == "Pm":
        lbl.set_color(style.FAINT)
ax.set_yticks([3, 4, 5, 6, 7, 8, 9, 10])
ax.set_ylabel("pH at which the hydroxide precipitates")
ax.set_title("A single hydroxide step splits groups; only cerium leaves the trend",
             loc="left", color=style.INK)

style.save(fig, "10-precipitation-ph")
