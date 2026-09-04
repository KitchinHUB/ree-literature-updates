"""Where things come out of an acidic rare earth liquor, by pH (ch. 10).

This figure was rebuilt in September 2026. The version it replaces plotted
precipitation pH against the lanthanide series using three group bands -- light
REE 6.8-7.5, heavy REE 7.0-8.0, Y 6.5-7.5 -- together with E = 1.74 V for the
cerium couple, 80-95 % cerium recovery, and a +/-0.2 pH control window. When
chapter 10 was rewritten every one of those numbers was deleted: none could be
traced to a primary source. Drawing them to scale on a labelled axis asserted
them more strongly than the prose ever had, so the figure had to go with them.

What is drawn now is only what survived sourcing, and the subject changes as a
result. There are no per-element precipitation pH values in the sourced
literature, so there is no series to plot and the lanthanide x-axis is gone.
The honest picture is one-dimensional: a single pH axis, with each species
marked in the window where the sources put it.

*   Fe(3+) is removed over pH 2.0-3.0 and is essentially complete by 3.5;
    Al(3+) over 3.5-4.5; Th(4+) about 95 % removed at 3.6 with MgCO3 and H2O2
    [@zhang2018rare; @li2025iron].
*   Rare earth hydroxides are thermodynamically favourable over pH 7.0-10.0 --
    one band for the whole series [@zhang2018rare]. That single band is the
    argument the old figure was trying to make with three overlapping ones, and
    it makes it better: if the entire series precipitates in one window, a
    hydroxide step returns a group, not an element.
*   Cerium is the exception, and the sourced window is pH 1.0-4.0, where
    Elizalde and co-workers studied oxidative Ce(IV) precipitation at 25, 45
    and 65 C [@elizalde2019oxidative]. Note where that window sits: on top of
    iron, aluminium and thorium. That overlap is why the industrial sequence
    oxidises cerium only after the impurities are gone, and it is visible here
    in a way it was not before.
*   The band between them is the result worth the figure. Treating a natural
    coal-refuse leachate, Zhang and Honaker recovered more than 80 % of the
    rare earths over pH 4.85-6.11, far below where hydroxides can form
    [@zhang2018rare]. They are not precipitating there: they are adsorbing onto
    the iron and aluminium hydroxysulfate solids that are. The old figure had
    no way to show this, and it is the one place where the thermodynamic
    picture and the plant disagree.

Nothing is interpolated, no solubility product is plotted, and no number
appears here that is not in the chapter with a citation attached.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import style

style.use()

# --- sourced windows, all from the chapter's cited table --------------------
FE = (2.0, 3.5)          # removed 2.0-3.0, essentially complete by 3.5
AL = (3.5, 4.5)
TH = 3.6                 # ~95 % with MgCO3 + H2O2, a point not a band
CE_IV = (1.0, 4.0)       # oxidative Ce(IV), the studied range
REE_OH = (7.0, 10.0)     # thermodynamically favourable, whole series
ADSORB = (4.85, 6.11)    # >80 % REE recovered, by adsorption not precipitation

fig, ax = plt.subplots(figsize=(7.0, 4.6))
ax.set_xlim(0.4, 11.2)
ax.set_ylim(0.0, 6.05)

ROW = {"ce": 4.85, "fe": 3.62, "al": 2.85, "ads": 1.75, "ree": 0.60}
H = 0.40


def bar(xspan, y, color, label, alpha=0.22, lw=1.0, note=None):
    """A window on the pH axis, labelled above its own left edge."""
    ax.add_patch(Rectangle((xspan[0], y), xspan[1] - xspan[0], H,
                           fc=color, alpha=alpha, ec=color, lw=lw, zorder=3))
    ax.text(xspan[0], y + H + 0.10, label, ha="left", va="bottom",
            fontsize=8, color=color, zorder=4)
    if note:
        ax.text(xspan[0], y - 0.12, note, ha="left", va="top",
                fontsize=7.5, color=style.MUTED, zorder=4)


# Cerium, and the overlap that sets the industrial order.
bar(CE_IV, ROW["ce"], style.ACCENT, "Ce(IV), oxidative   1.0$-$4.0")

# The impurities that must leave first.
bar(FE, ROW["fe"], style.AQUEOUS, "Fe$^{3+}$   2.0$-$3.5")
bar(AL, ROW["al"], style.AQUEOUS, "Al$^{3+}$   3.5$-$4.5")
ax.plot([TH, TH], [ROW["al"] - 0.30, ROW["al"] - 0.02], color=style.GOOD,
        lw=1.6, zorder=5, solid_capstyle="butt")
ax.text(TH + 0.10, ROW["al"] - 0.32, "Th$^{4+}$  3.6", ha="left", va="top",
        fontsize=7.5, color=style.GOOD, zorder=5)

# The band where the plant disagrees with the thermodynamics.
ax.add_patch(Rectangle((ADSORB[0], ROW["ads"]), ADSORB[1] - ADSORB[0], H,
                       fc=style.GROUND, ec=style.INK, lw=1.0, zorder=3,
                       hatch="////"))
ax.text(ADSORB[0], ROW["ads"] + H + 0.10,
        "> 80 % of the rare earths   4.85$-$6.11", ha="left", va="bottom",
        fontsize=8, color=style.INK, zorder=4)
ax.text(ADSORB[0], ROW["ads"] - 0.12,
        "adsorbed on Fe/Al hydroxysulfate, not precipitated",
        ha="left", va="top", fontsize=7.5, color=style.MUTED, zorder=4)

# The whole series, in one band.
bar(REE_OH, ROW["ree"], style.ORGANIC,
    "every rare earth hydroxide   7.0$-$10.0", alpha=0.20)

# The gap that makes staged precipitation work.
ax.annotate("", xy=(4.5, 5.68), xytext=(7.0, 5.68),
            arrowprops=dict(arrowstyle="<|-|>", color=style.MUTED, lw=0.9,
                            shrinkA=0, shrinkB=0, mutation_scale=9))
ax.text(5.75, 5.76, "the gap staged precipitation lives in", ha="center",
        va="bottom", fontsize=7.5, color=style.MUTED)

ax.text(0.55, 5.76,
        "Cerium's window sits on top of the impurities:\nit is oxidised last, "
        "not first.",
        ha="left", va="bottom", fontsize=8, color=style.INK)

for x in (4.5, 7.0):
    ax.plot([x, x], [0.30, 5.58], color=style.FAINT, lw=0.8,
            ls=(0, (4, 3)), zorder=1)

ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.set_xticks(range(1, 12))
ax.set_xlabel("pH")
ax.set_title("One hydroxide window holds the whole series; only cerium leaves it",
             loc="left", color=style.INK, pad=26)

style.save(fig, "10-precipitation-ph")
