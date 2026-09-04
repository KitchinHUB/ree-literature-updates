"""The fractional extraction cascade, and the stage count it implies (ch. 3).

This replaces the ASCII drawing in ch. 3. Four things have to survive the
redraw, because the chapter's argument rests on all of them:

1.  The two phases run counter to each other, and the drawing has to get the
    directions right. The raffinate leaves the left end and the loaded organic
    leaves the right end, so the organic runs left to right and the aqueous
    runs right to left. (The ASCII version drew both arrows the other way,
    which contradicted its own end labels.)
2.  The feed enters partway along. That is the whole difference between a
    recovery cascade and a fractional one: everything on the raffinate side of
    the feed point is the extraction section, everything on the loaded-organic
    side is the scrub section.
3.  The scrub liquor is a split of the cascade's own strip product, drawn as a
    return loop and labelled as the reflux. A scrub drawn as "dilute acid in"
    would make the section look like impurity washing, which is a different and
    much smaller operation.
4.  Two curved arrows say what each section does: in the extraction section the
    more-extractable element is pulled into the organic; in the scrub section
    the co-extracted less-extractable element is displaced back off the
    extractant into the aqueous and carried toward the feed. That return is why
    a cascade can be pure at *both* ends rather than one.

The lower panel is the reason the upper one is so long. It is the chapter's
Fenske bound,

    N_min = ln[ (x_P/(1-x_P)) * ((1-x_R)/x_R) ] / ln(beta),

drawn rather than evaluated: at total reflux each equilibrium stage multiplies
the ratio of the two elements by beta, so on a logit axis the composition
profile is a straight line of slope log(beta) and the stage count is read off
as a length. Nothing here is measured. The chapter's own numbers set the
endpoints (99.99% at both ends) and the two separation factors -- beta = 1.5
for an adjacent pair, beta = 3.0 for a pair two apart -- and the curves
reproduce the chapter's 45 and 17 stages. The feed stage falls where the
profile passes 50/50, which for an equimolar binary feed is the middle of the
train, which is where the upper panel puts it.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import style

style.use()

# ---------------------------------------------------------------- the numbers
XP, XR = 0.9999, 0.0001          # ch. 3's purity specification, both ends
BETAS = (1.5, 3.0)               # adjacent pair; pair two apart


def fenske(beta):
    return np.log((XP / (1 - XP)) * ((1 - XR) / XR)) / np.log(beta)


# 45.4 and 16.8; the chapter quotes 45 and 17.
N15 = int(round(fenske(BETAS[0])))
N30 = int(round(fenske(BETAS[1])))

# The feed goes where the profile crosses 50/50, which for an equimolar binary
# feed is 23.7 stages up from the raffinate end: stage 24.
FEED = int(np.ceil(1 + np.log((1 - XR) / XR) / np.log(BETAS[0])))

X0, X1 = -3.6, 50.5                      # horizontal extent, shared by panels
LEFT, RIGHT = 1.0, float(N15)            # the cascade spans stages 1..45

fig, (axs, axp) = plt.subplots(
    2, 1, figsize=(6.9, 7.5),
    gridspec_kw=dict(height_ratios=[1.10, 1.0], hspace=0.28))

# =========================================================== upper: schematic
style.blank(axs)
axs.set_xlim(X0, X1)
axs.set_ylim(0.85, 12.0)

ORG_Y, AQ_Y = 8.35, 6.45
TOP, BOT = 9.20, 5.60


def route(pts, color, lw=1.1, zorder=3):
    """Polyline with an arrowhead on the final segment."""
    axs.plot([p[0] for p in pts], [p[1] for p in pts], color=color, lw=lw,
             solid_capstyle="round", solid_joinstyle="round", zorder=zorder)
    axs.add_patch(FancyArrowPatch(pts[-2], pts[-1], arrowstyle="-|>",
                                  mutation_scale=10, color=color, lw=lw,
                                  shrinkA=0, shrinkB=0, zorder=zorder))


# The cascade body: one frame, one divider at the feed stage.
axs.add_patch(FancyBboxPatch((LEFT, BOT), RIGHT - LEFT, TOP - BOT,
                             boxstyle="round,pad=0.02", fc="#f7f7f5",
                             ec=style.FAINT, lw=0.8, zorder=0))
axs.plot([FEED, FEED], [BOT, TOP], color=style.FAINT, lw=0.8, zorder=1)

# The two counterflowing phases. Direction is the load-bearing detail.
axs.plot([LEFT, RIGHT], [ORG_Y, ORG_Y], color=style.ORGANIC, lw=1.8, zorder=2)
for x in (7, 17, 28, 40):
    axs.add_patch(FancyArrowPatch((x - 1.3, ORG_Y), (x, ORG_Y),
                                  arrowstyle="-|>", mutation_scale=11,
                                  color=style.ORGANIC, lw=1.8, shrinkA=0,
                                  shrinkB=0, zorder=2))
axs.plot([LEFT, RIGHT], [AQ_Y, AQ_Y], color=style.AQUEOUS, lw=1.8, zorder=2)
for x in (4, 15, 26, 37):
    axs.add_patch(FancyArrowPatch((x + 1.3, AQ_Y), (x, AQ_Y),
                                  arrowstyle="-|>", mutation_scale=11,
                                  color=style.AQUEOUS, lw=1.8, shrinkA=0,
                                  shrinkB=0, zorder=2))
axs.text(RIGHT - 0.6, ORG_Y + 0.16, "organic", fontsize=8,
         color=style.ORGANIC, ha="right", va="bottom")
axs.text(RIGHT - 0.6, AQ_Y - 0.18, "aqueous", fontsize=8,
         color=style.AQUEOUS, ha="right", va="top")

# Section labels.
axs.text((LEFT + FEED) / 2, TOP + 0.22,
         "EXTRACTION SECTION   stages 1-%d" % (FEED - 1),
         fontsize=8.5, color=style.INK, ha="center", va="bottom")
axs.text((FEED + RIGHT) / 2, TOP + 0.22,
         "SCRUB SECTION   stages %d-%d" % (FEED, N15),
         fontsize=8.5, color=style.INK, ha="center", va="bottom")

# What each section does, drawn between the bands.
MID = (ORG_Y + AQ_Y) / 2
axs.add_patch(FancyArrowPatch((10.5, AQ_Y + 0.10), (13.5, ORG_Y - 0.10),
                              connectionstyle="arc3,rad=-0.32",
                              arrowstyle="-|>", mutation_scale=9,
                              color=style.ACCENT, lw=1.0, shrinkA=0, shrinkB=0,
                              zorder=4))
axs.text(9.9, MID, "heavy REE\nextracted", fontsize=7.6, color=style.ACCENT,
         ha="right", va="center", linespacing=1.35)
axs.add_patch(FancyArrowPatch((32.0, ORG_Y - 0.10), (29.0, AQ_Y + 0.10),
                              connectionstyle="arc3,rad=-0.32",
                              arrowstyle="-|>", mutation_scale=9,
                              color=style.ACCENT, lw=1.0, shrinkA=0, shrinkB=0,
                              zorder=4))
axs.text(32.6, MID, "light REE returned\ntoward the feed", fontsize=7.6,
         color=style.ACCENT, ha="left", va="center", linespacing=1.35)

# Feed, joining the aqueous stream at the section boundary.
route([(FEED, 10.20), (FEED, AQ_Y + 0.20)], style.AQUEOUS, lw=1.3, zorder=5)
axs.text(FEED + 0.8, 11.35, "FEED", fontsize=9, color=style.INK,
         ha="left", va="center")
axs.text(FEED + 0.8, 10.75, "light + heavy REE", fontsize=7.8,
         color=style.MUTED, ha="left", va="center")

# Raffinate: the aqueous leaves the left end.
route([(LEFT, AQ_Y), (-3.0, AQ_Y), (-3.0, 10.30)], style.AQUEOUS, lw=1.3)
axs.text(-3.4, 11.35, "RAFFINATE", fontsize=9, color=style.INK,
         ha="left", va="center")
axs.text(-3.4, 10.75, "less-extractable (light) REE, e.g. La", fontsize=7.8,
         color=style.MUTED, ha="left", va="center")

# Fresh / stripped organic enters at the left end.
route([(-2.3, ORG_Y), (LEFT, ORG_Y)], style.ORGANIC, lw=1.3)
axs.text(-3.5, ORG_Y + 0.12, "stripped\norganic in", fontsize=7.8,
         color=style.ORGANIC, ha="left", va="bottom", linespacing=1.35)

# Loaded organic leaves the right end and goes to the strip section.
route([(RIGHT, ORG_Y), (48.6, ORG_Y), (48.6, 3.20), (41.7, 3.20)],
      style.ORGANIC, lw=1.3)
axs.text(49.4, 5.9, "loaded organic", fontsize=7.8, color=style.ORGANIC,
         ha="center", va="center", rotation="vertical")

axs.add_patch(FancyBboxPatch((27.6, 2.35), 14.0, 1.70,
                             boxstyle="round,pad=0.02", fc=style.GROUND,
                             ec=style.FAINT, lw=0.8, zorder=2))
axs.text(34.6, 3.62, "STRIP SECTION", fontsize=8.5, color=style.INK,
         ha="center", va="center", zorder=3)
axs.text(34.6, 2.90, "strong acid; extractant\nregenerated and recycled",
         fontsize=7.6, color=style.MUTED, ha="center", va="center",
         linespacing=1.35, zorder=3)

# The strip liquor splits: part is product, part returns as the scrub.
axs.plot([27.6, 25.0], [3.20, 3.20], color=style.AQUEOUS, lw=1.3, zorder=3)
axs.plot([25.0], [3.20], marker="o", ms=3.6, color=style.AQUEOUS, zorder=4)
route([(25.0, 3.20), (25.0, 1.50), (16.0, 1.50)], style.AQUEOUS, lw=1.3)
axs.text(15.4, 1.72, "PRODUCT", fontsize=9, color=style.INK,
         ha="right", va="center")
axs.text(15.4, 1.18, "more-extractable (heavy) REE, e.g. Pr + Nd",
         fontsize=7.8, color=style.MUTED, ha="right", va="center")

route([(25.0, 3.20), (25.0, 4.85), (46.9, 4.85), (46.9, AQ_Y),
       (RIGHT + 0.05, AQ_Y)], style.AQUEOUS, lw=1.3)
axs.text(32.0, 4.98, "scrub = part of the strip product: the reflux",
         fontsize=7.8, color=style.AQUEOUS, ha="center", va="bottom")

# ============================================================ lower: profile
curves = {}
for beta, n in ((BETAS[0], N15), (BETAS[1], N30)):
    k = np.arange(1, n + 1)
    ratio = (XR / (1 - XR)) * beta ** (k - 1)
    curves[beta] = (k, ratio / (1 + ratio))

k15, y15 = curves[BETAS[0]]
k30, y30 = curves[BETAS[1]]

axp.set_xlim(X0, X1)
axp.set_yscale("logit")
axp.set_ylim(2.0e-5, 1 - 2.0e-5)

for lvl in (XR, XP):
    axp.axhline(lvl, color=style.FAINT, lw=0.8, zorder=0)
axp.axvline(FEED, color=style.FAINT, lw=0.8, zorder=0)

axp.plot(k30, y30, color=style.MUTED, lw=1.3, ls=(0, (4, 2.5)), zorder=3,
         marker="o", ms=2.6, mfc=style.MUTED, mec="none")
axp.plot(k15, y15, color=style.INK, lw=1.5, zorder=4,
         marker="o", ms=2.6, mfc=style.INK, mec="none")
axp.plot([FEED], [y15[FEED - 1]], marker="o", ms=6.5, mfc=style.GROUND,
         mec=style.INK, mew=1.2, zorder=5)

ytr = axp.get_yaxis_transform()          # x in axes fraction, y in data
axp.text(0.012, XP, "99.99% pure at the extract end", fontsize=7.8,
         color=style.MUTED, ha="left", va="bottom", transform=ytr)
axp.text(0.012, XR, "0.01% left at the raffinate end", fontsize=7.8,
         color=style.MUTED, ha="left", va="top", transform=ytr)

axp.text(0.90, 0.945, r"$\beta = 1.5$, an adjacent pair:  %d stages" % N15,
         fontsize=8.5, color=style.INK, ha="right", va="center",
         transform=axp.transAxes)
axp.text(0.345, 0.855, r"$\beta = 3.0$, a pair two apart:  %d" % N30,
         fontsize=8.5, color=style.MUTED, ha="right", va="center",
         transform=axp.transAxes)

axp.annotate("feed stage %d: the profile\ncrosses 50/50 here" % FEED,
             xy=(FEED, y15[FEED - 1]), xycoords="data",
             xytext=(0.545, 0.34), textcoords="axes fraction",
             fontsize=7.8, color=style.INK, ha="left", va="center",
             linespacing=1.35,
             arrowprops=dict(arrowstyle="-", color=style.MUTED, lw=0.7,
                             shrinkA=2, shrinkB=5))

# The slope is the whole content of the panel, so label it on the line itself.
fig.canvas.draw()
p0 = axp.transData.transform((k15[27], y15[27]))
p1 = axp.transData.transform((k15[33], y15[33]))
angle = np.degrees(np.arctan2(p1[1] - p0[1], p1[0] - p0[0]))
odds = y15[25] / (1 - y15[25]) * 3.4   # sit the label just above the line
axp.text(k15[25], odds / (1 + odds),
         r"each stage multiplies the heavy:light ratio by $\beta$",
         fontsize=7.8, color=style.MUTED, ha="center", va="center",
         rotation=angle, rotation_mode="anchor")

axp.set_xticks([1, 10, 20, 30, 40, N15])
axp.set_xlabel("stage   (raffinate end  $\\rightarrow$  extract end)")
axp.set_ylabel("mole fraction of the\nmore-extractable element")
axp.set_title(r"Fenske: $N_{\min} = \ln[\,(x_P/(1-x_P))\,((1-x_R)/x_R)\,]\,"
              r"/\,\ln \beta$,  drawn not measured",
              loc="left", color=style.INK, fontsize=9)

style.save(fig, "03-cascade")
