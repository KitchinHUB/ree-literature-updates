"""The four microchannel flow regimes named in ch. 9.

A schematic, not data. The four panels are the four regimes of the chapter's
"Flow Regimes and Configurations" section, in the order it lists them:
co-laminar, slug, micro-droplet, pore-throat. The numbers beside each panel are
that section's own: phase ratios 5:1 to 1:5 for co-laminar, mass transfer
efficiencies of 86.9-94.8% for slug and 92.9-97.4% for micro-droplet, and
50-250:1 phase ratios with 77% extraction at 500:1 and equilibrium within 30 s
for pore-throat. Nothing is drawn to scale; the channel is the same width in
every panel precisely so that the only thing changing down the figure is what
the two phases do inside it.

The figure has one job beyond naming the regimes, which is to make the
interfacial-area argument visible. The interface is drawn in a single colour in
all four panels, so the reader can see it go from one flat line (co-laminar,
where mass transfer is diffusion across a single plane) to the caps of a slug
train, to the perimeter of every drop in a dispersion. That ordering is why the
chapter's efficiency numbers rise down the list: same two phases, same channel,
more interface.

What sets the transitions is where the chapter is thinner than the drawing
would like. It states only the envelope -- all of this is laminar, Re < 2300 --
and cites the flow-regime maps of @dessimoz2010quantitative and
@kashid2007hydrodynamics for the definitions, without quoting a capillary
number or a transition velocity. So the first three panels are labelled with
the direction of the transition (increasing flow rate and shear, which is what
disperses one phase into the other) and no threshold is invented for it. The
fourth is deliberately set apart: pore-throat is a change of channel geometry,
not of flow rate, and the sequence would misread as a single flow-rate axis if
it were left in line with the others.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from matplotlib.patches import Rectangle, Ellipse, Polygon, FancyArrowPatch
import style

style.use()

FIG_W, FIG_H = 7.3, 5.0
fig = plt.figure(figsize=(FIG_W, FIG_H))
# The axes fills the figure so that data units have a known aspect: a drop that
# should look round has to be drawn CIRC times taller than it is wide.
ax = fig.add_axes([0, 0, 1, 1])
style.blank(ax)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
CIRC = FIG_W / FIG_H

X0, X1 = 2.05, 5.90          # channel extent
HH = 0.45                    # channel half-height
TX = 6.15                    # left edge of the annotation column
ROWS = (8.35, 6.25, 4.15, 2.05)

IFACE = style.ACCENT         # the liquid-liquid interface, in every panel


def tint(color, a):
    """A washed fill. Patch-level alpha would fade the interface edge too."""
    return to_rgba(color, a)


def channel_walls(y, x0=X0, x1=X1):
    ax.plot([x0, x1], [y + HH, y + HH], color=style.INK, lw=1.0, zorder=4)
    ax.plot([x0, x1], [y - HH, y - HH], color=style.INK, lw=1.0, zorder=4)


def flow_arrow(y):
    ax.add_patch(FancyArrowPatch((X0 - 0.62, y), (X0 - 0.14, y),
                                 arrowstyle="-|>", mutation_scale=8,
                                 color=style.MUTED, lw=0.9,
                                 shrinkA=0, shrinkB=0, zorder=3))


def label(y, name, lines):
    ax.text(X0, y + HH + 0.22, name, fontsize=9, color=style.INK,
            ha="left", va="bottom")
    ax.text(TX, y, lines, fontsize=7.4, color=style.MUTED, ha="left",
            va="center", linespacing=1.5)


# ------------------------------------------------- 1. co-laminar (parallel)
y = ROWS[0]
ax.add_patch(Rectangle((X0, y), X1 - X0, HH, fc=style.ORGANIC, alpha=0.16,
                       lw=0, zorder=1))
ax.add_patch(Rectangle((X0, y - HH), X1 - X0, HH, fc=style.AQUEOUS, alpha=0.16,
                       lw=0, zorder=1))
ax.plot([X0, X1], [y, y], color=IFACE, lw=1.8, zorder=5)
ax.text(X0 + 0.16, y + 0.22, "organic", fontsize=7, color=style.ORGANIC,
        ha="left", va="center", zorder=6)
ax.text(X0 + 0.16, y - 0.22, "aqueous", fontsize=7, color=style.AQUEOUS,
        ha="left", va="center", zorder=6)
channel_walls(y)
flow_arrow(y)
label(y, "Co-laminar (parallel) flow",
      "phase ratio 5:1 to 1:5\n"
      "one flat interface; transfer is\n"
      "diffusion across a single plane")

# ------------------------------------------------------------- 2. slug flow
y = ROWS[1]
BULGE = 0.17
edges = np.linspace(X0, X1, 7)


def cap(xb, n=60):
    ys = np.linspace(y - HH, y + HH, n)
    xs = xb + BULGE * np.cos(np.pi * (ys - y) / (2 * HH))
    return xs, ys


for i in range(len(edges) - 1):
    xa, xb = edges[i], edges[i + 1]
    xsa, ysa = cap(xa)
    xsb, ysb = cap(xb)
    if i == 0:
        xsa = np.full_like(ysa, X0)          # inlet face is flat
    if i == len(edges) - 2:
        xsb = np.full_like(ysb, X1)
    pts = np.concatenate([np.column_stack([xsa, ysa]),
                          np.column_stack([xsb, ysb])[::-1]])
    c = style.ORGANIC if i % 2 else style.AQUEOUS
    ax.add_patch(Polygon(pts, closed=True, fc=c, alpha=0.16, lw=0, zorder=1))

for xb in edges[1:-1]:
    xs, ys = cap(xb)
    ax.plot(xs, ys, color=IFACE, lw=1.6, zorder=5)

# One slug's internal circulation, drawn once rather than in every segment.
xc = 0.5 * (edges[1] + edges[2])
for s in (-1, 1):
    ax.add_patch(FancyArrowPatch((xc - 0.16, y + s * 0.20),
                                 (xc + 0.16, y + s * 0.20),
                                 connectionstyle=f"arc3,rad={-0.9 * s}",
                                 arrowstyle="-|>", mutation_scale=6,
                                 color=style.MUTED, lw=0.7, zorder=6))
channel_walls(y)
flow_arrow(y)
label(y, "Slug (segmented) flow",
      "86.9–94.8% mass transfer efficiency\n"
      "interface is the slug caps; internal\n"
      "circulation renews it from inside")

# --------------------------------------------------------- 3. micro-droplet
y = ROWS[2]
ax.add_patch(Rectangle((X0, y - HH), X1 - X0, 2 * HH, fc=style.AQUEOUS,
                       alpha=0.12, lw=0, zorder=1))
d = 0.24
xs = np.arange(X0 + 0.26, X1 - 0.15, 0.32)
for i, xd in enumerate(xs):
    yd = y + (0.20 if i % 2 else -0.20)
    ax.add_patch(Ellipse((xd, yd), d, d * CIRC, fc=tint(style.ORGANIC, 0.22),
                         ec=IFACE, lw=1.1, zorder=5))
channel_walls(y)
flow_arrow(y)
label(y, "Micro-droplet flow",
      "92.9–97.4% mass transfer efficiency\n"
      "large specific surface area; used\n"
      "for trace, high-selectivity REE")

# ------------------------------------------------------------ 4. pore-throat
y = ROWS[3]
xs = np.linspace(X0, X1, 400)
L = (X1 - X0) / 4.0
h = 0.45 - 0.20 * (1 + np.cos(2 * np.pi * (xs - X0 - L / 2) / L)) / 2
ax.fill_between(xs, y - h, y + h, color=style.AQUEOUS, alpha=0.12, lw=0,
                zorder=1)
ax.plot(xs, y + h, color=style.INK, lw=1.0, zorder=4)
ax.plot(xs, y - h, color=style.INK, lw=1.0, zorder=4)
for k in range(4):
    xd = X0 + L / 2 + k * L
    ax.add_patch(Ellipse((xd, y), 0.52, 0.52, fc=tint(style.ORGANIC, 0.22),
                         ec=IFACE, lw=1.2, zorder=5))
ax.annotate("throat", xy=(X0 + L, y - 0.28), xytext=(X0 + L, y - 0.72),
            fontsize=7, color=style.MUTED, ha="center", va="top",
            arrowprops=dict(arrowstyle="-", color=style.MUTED, lw=0.7,
                            shrinkA=1, shrinkB=1))
flow_arrow(y)
label(y, "Pore-throat microchannel",
      "phase ratio 50–250:1; 77% at 500:1\n"
      "capillary barriers hold drops back,\n"
      "reaching equilibrium within 30 s")

# ---------------------------------------------------------- the two margins
ax.add_patch(FancyArrowPatch((0.95, ROWS[0] + 0.55), (0.95, ROWS[2] - 0.55),
                             arrowstyle="-|>", mutation_scale=10,
                             color=style.MUTED, lw=1.0, shrinkA=0, shrinkB=0))
ax.text(0.72, (ROWS[0] + ROWS[2]) / 2,
        "increasing flow rate and shear",
        rotation="vertical", ha="right", va="center", fontsize=8,
        color=style.MUTED)
ax.text(0.95, ROWS[3], "geometry,\nnot flow rate",
        rotation="vertical", ha="center", va="center", fontsize=7.4,
        color=style.MUTED, linespacing=1.4)

ax.text(0.30, 9.62,
        "All four are laminar ($Re$ < 2300); the chapter names the regimes "
        "but quotes no transition threshold.",
        fontsize=8, color=style.MUTED, ha="left", va="center")
ax.text(0.30, 0.52,
        "The coloured line is the liquid–liquid interface. Same two phases, "
        "same channel:\nthe regime decides how much interface there is, and "
        "that is what mass transfer must cross.",
        fontsize=8, color=style.INK, ha="left", va="center", linespacing=1.5)

style.save(fig, "09-flow-regimes")
