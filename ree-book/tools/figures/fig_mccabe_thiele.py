"""The McCabe-Thiele construction chapter 3 describes but never drew.

The chapter gives the recipe -- plot the equilibrium curve, draw the operating
line, step off stages between them -- and then moves straight to the Kremser
equation, which is the same calculation done algebraically. Drawing it is worth
the page for one reason: the algebra assumes the equilibrium line is *straight*,
and the whole content of the graphical method is what happens when it is not.

Nothing here is measured. Every number is the chapter's own, propagated:

  * D = 10 and O/A = 1/3, so the extraction factor E = D(O/A) = 3.33 and the
    operating line has slope A/O = 3. These are the worked example's numbers.
  * A 30 vol% D2EHPA solution is about 0.9 M in monomer and three monomers are
    consumed per REE, so the organic saturates near 0.30 M REE. That is the
    chapter's own capacity argument, and it is what sets the plateau.
  * The feed is 0.05 M REE, which loads the organic to 0.15 M -- half of
    saturation, which is where the chapter says such a circuit is run.
  * The target is 99.9% recovery, x_out = 5e-5 M, the worked example's duty.

The equilibrium curve is a Langmuir form chosen to have the chapter's initial
slope (D = 10 as x -> 0) and the chapter's capacity (0.30 M). It is an
*illustration of curvature*, not an isotherm anybody measured; the caption says
so. What survives the choice of functional form is the shape of the conclusion,
not the digits: any saturating curve costs stages, and every saturating curve
has a phase ratio past which no number of stages is enough.

Three things are drawn that the Kremser equation cannot say:

1.  The straight line the algebra assumes, against the curve a loaded extractant
    actually follows. Six stages becomes seven.
2.  The pinch. Raise A/O far enough -- load the organic harder to save solvent --
    and the operating line touches the equilibrium curve at the feed end. At
    that phase ratio the driving force goes to zero and the stage count goes to
    infinity. The pinch is why the chapter says the ceiling on the phase ratio
    is the extractant rather than the hydraulics.
3.  Where the stages actually go. The staircase is not evenly spaced: most of
    the metal moves in the first two steps and the last four stages are spent
    on the final couple of percent, which is the shape of every recovery duty.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import style

style.use()

# ------------------------------------------------------------- the numbers
D = 10.0                 # distribution ratio at low loading, ch. 3
YMAX = 0.30              # M REE; 0.9 M monomer / 3 monomers per REE
XIN = 0.05               # M REE in the aqueous feed
XOUT = XIN / 1000.0      # 99.9% recovery, the worked example's duty
AO = 3.0                 # A/O = 1/(O/A) = 3, so E = D (O/A) = 3.33
K = D / YMAX             # Langmuir constant fixed by the initial slope


def y_eq(x):
    """Saturating equilibrium: slope D at the origin, plateau at YMAX."""
    return YMAX * K * x / (1.0 + K * x)


def x_eq(y):
    """Its inverse: the aqueous concentration in equilibrium with y."""
    return y / (D - y * K)


def operating(x, ao):
    return ao * (x - XOUT)


def stairs(ao, curved):
    """Step off stages from the concentrated end. Returns the corner points."""
    y = operating(XIN, ao)
    x = XIN
    pts = [(x, y)]
    n = 0
    while x > XOUT and n < 40:
        x = x_eq(y) if curved else y / D          # horizontal to equilibrium
        pts.append((x, y))
        n += 1
        y = operating(x, ao)                      # vertical to operating line
        pts.append((x, y))
    return pts, n


# The largest phase ratio the extractant allows: beyond it the operating line
# cuts the equilibrium curve and the cascade pinches at the feed end.
AO_PINCH = y_eq(XIN) / (XIN - XOUT)

pts_curved, n_curved = stairs(AO, curved=True)
pts_linear, n_linear = stairs(AO, curved=False)

# ------------------------------------------------------------------ drawing
fig, ax = plt.subplots(figsize=(6.9, 6.3))

XHI, YHI = XIN * 1.06, 0.312
xg = np.linspace(0, XHI, 400)
ax.plot(xg, y_eq(xg), color=style.INK, lw=1.8, zorder=4,
        label="equilibrium $y^*$ = f($x$): the organic saturates at 0.30 M")

# The straight line only says something near the origin, so it is drawn only
# where it is close enough to the curve to be a plausible approximation.
xl = xg[D * xg <= 0.195]
ax.plot(xl, D * xl, color=style.MUTED, lw=1.1, ls=(0, (4, 2.5)), zorder=3,
        label="the straight line Kremser assumes, $y^*$ = 10$x$")

# The operating line the worked example runs on.
ax.plot([XOUT, XIN], [0, operating(XIN, AO)], color=style.AQUEOUS, lw=1.8,
        zorder=4, label="operating line, slope A/O = 3 (the worked example)")

# The pinched operating line, and the point where it touches the curve.
ax.plot([XOUT, XIN], [0, operating(XIN, AO_PINCH)], color=style.ACCENT,
        lw=1.1, ls=(0, (1, 2)), zorder=4,
        label="A/O = %.2f: pinched against the curve" % AO_PINCH)
ax.plot([XIN], [y_eq(XIN)], marker="o", ms=5.5, mfc=style.GROUND,
        mec=style.ACCENT, mew=1.3, zorder=6)

# The staircase, stepped on the curve a loaded extractant actually follows.
ax.plot([p[0] for p in pts_curved], [p[1] for p in pts_curved],
        color=style.ORGANIC, lw=1.2, zorder=5)

ax.set_xlim(0, XHI)
ax.set_ylim(0, YHI)
ax.set_xlabel("$x$, REE in the aqueous phase  (mol/L)")
ax.set_ylabel("$y$, REE in the organic phase  (mol/L)")
ax.axhline(YMAX, color=style.FAINT, lw=0.8, zorder=0)
# The saturation line is left unlabelled: the legend already says what it is,
# and there is no room at the top of the panel that does not collide.

# Number the steps that are legible at this scale; the rest go in the inset.
for i in range(n_curved):
    xk, yk = pts_curved[2 * i + 1]
    if xk < XIN * 0.05:
        break
    ax.text(xk - XIN * 0.011, yk + YHI * 0.010, str(i + 1), fontsize=8.5,
            color=style.ORGANIC, ha="right", va="bottom")

ax.legend(loc="lower right", bbox_to_anchor=(1.005, -0.012), fontsize=7.6,
          handlelength=2.4, labelspacing=0.55)

# ------------------------------------------------------- what the ends mean
ax.annotate("feed end\n$x_\\mathrm{in}$ = 0.05 M in, organic\nleaves loaded to 0.15 M",
            xy=(XIN, operating(XIN, AO)), xytext=(XIN * 0.735, 0.098),
            fontsize=7.6, color=style.INK, ha="center", va="top",
            linespacing=1.4,
            arrowprops=dict(arrowstyle="-", color=style.MUTED, lw=0.7,
                            shrinkA=3, shrinkB=4))
ax.annotate("raffinate end\n$x_\\mathrm{out}$ = 5$\\times$10$^{-5}$ M,\n"
            "fresh organic in at $y$ = 0",
            xy=(XOUT, 0), xytext=(XIN * 0.185, 0.0045),
            fontsize=7.6, color=style.INK, ha="left", va="bottom",
            linespacing=1.4,
            arrowprops=dict(arrowstyle="-", color=style.MUTED, lw=0.7,
                            shrinkA=3, shrinkB=8))

ax.annotate("load the organic harder than this\n"
            "and the operating line meets the\n"
            "equilibrium curve: driving force\n"
            "zero at the feed end, and no number\n"
            "of stages is enough. The cap on the\n"
            "phase ratio is the extractant.",
            xy=(XIN, y_eq(XIN)), xytext=(XIN * 0.565, YHI * 0.975),
            fontsize=7.6, color=style.ACCENT, ha="left", va="top",
            linespacing=1.45,
            arrowprops=dict(arrowstyle="-", color=style.ACCENT, lw=0.7,
                            shrinkA=3, shrinkB=5))

# ------------------------------------------------------------------- inset
# The last four stages live in a corner 1/25 the width of the plot. Every
# recovery duty looks like this: the metal moves in the first two contacts and
# the rest of the train is spent on the tail.
XZ = XIN / 25
ins = ax.inset_axes([0.075, 0.605, 0.295, 0.315])
xi = np.linspace(0, XZ, 200)
ins.plot(xi, y_eq(xi), color=style.INK, lw=1.2)
ins.plot([XOUT, XZ], [0, operating(XZ, AO)], color=style.AQUEOUS, lw=1.2)
ins.plot([p[0] for p in pts_curved], [p[1] for p in pts_curved],
         color=style.ORGANIC, lw=1.0)
ins.set_xlim(0, XZ)
ins.set_ylim(0, y_eq(XZ) * 1.06)
ins.set_xticks([0, 0.001, 0.002])
ins.set_xticklabels(["0", "0.001", "0.002"], fontsize=6.5)
ins.set_yticks([0, 0.005, 0.010, 0.015])
ins.set_yticklabels(["0", "5", "10", "15"], fontsize=6.5)
ins.set_title("the tail, magnified 25$\\times$ ($y$ in mM):\n"
              "four stages to move the last two percent",
              fontsize=7.2, color=style.MUTED, pad=3, linespacing=1.35)
for i in range(n_curved):
    xk, yk = pts_curved[2 * i + 1]
    if xk > XZ * 0.94:
        continue
    ins.text(xk, yk + y_eq(XZ) * 0.030, str(i + 1), fontsize=6.8,
             color=style.ORGANIC, ha="center", va="bottom")
ax.indicate_inset_zoom(ins, edgecolor=style.FAINT, lw=0.7, alpha=1.0)

ax.set_title("%d stages stepped off on the real curve; the straight line the "
             "Kremser equation assumes says %d" % (n_curved, n_linear),
             loc="left", color=style.INK, fontsize=9.5)

style.save(fig, "03-mccabe-thiele")

print(f"  A/O = {AO}: {n_curved} stages on the saturating curve, "
      f"{n_linear} on the straight line")
print(f"  pinch at A/O = {AO_PINCH:.3f} (y_out = {y_eq(XIN):.4f} M)")
