"""One flowsheet for ch. 5, replacing the chapter's three ASCII drawings.

The chapter carried three separate ASCII flowsheets — Mountain Pass bastnäsite,
the Indian monazite sulfuric route, and the southern-China ion-adsorption clay
route. Drawn side by side on one grid they say something none of them said
alone, which is the reason for a single figure:

1.  The routes differ only in how the mineral is *cracked*. From the leach
    onward they converge on one liquor with one specification, and that
    specification is what the solvent extraction chapter takes as its input.
2.  The medium is the organising variable, so it is the only thing colour is
    used for: black for solids (ore, concentrate, calcine, hydroxide cake),
    purple for a sulfate liquor, blue for a chloride liquor. Read that way the
    figure makes the chapter's own argument visible — every route that leaches
    into sulfate has to precipitate the rare earths as a hydroxide or a double
    sulfate and redissolve that solid in HCl before it can feed a chloride
    circuit. Only the Mountain Pass route, which never leaves chloride, skips
    the step, and its long unbroken arrow across the conversion column is the
    point.
3.  The ion-adsorption lane is drawn as a long arrow across two empty columns,
    because the absence of beneficiation and of any decomposition step is the
    defining fact about those deposits, not an omission in the drawing.

A fourth branch is included that the ASCII drawings did not have: the Bayan Obo
concentrated-sulfuric bake, which the chapter sets out in prose immediately
after Mountain Pass precisely so the two can be compared. Putting it on the
same grid is what makes the chloride/sulfate contrast legible.

Every box, condition and side stream is taken from ch. 5 — Mountain Pass and
Bayan Obo from @gupta2004extractive, @castor2006rare and @kim2025rare; the
Indian monazite route and the caustic alternative from @gupta2004extractive,
@jha2016hydrometallurgical and @borai2016modified; the ion-adsorption route
from @chi2008weathered and @shi2022column; the purification pH windows and the
feed specification from @jha2016hydrometallurgical. No new source is used.

Where the chapter states a quantity two incompatible ways, this figure prints no
number rather than choosing one. That applies to the ore grade feeding flotation
(5-15 % REO as raw ore, 7-9 % at Mountain Pass, 10-30 % as "flotation feed"), to
the acid strength of the bastnäsite leach (4-8 M HCl in the HCl section, 2-6 M
in the summary table), to the lixiviant strength for the clays (2-3 % in one
place, 2-5 % in two others), and to every leach residence time (1-3 h, 2-4 h and
4-8 h are all given for steps the chapter treats as one). Temperatures, the
digestion acid and caustic strengths, and the purification pH windows are stated
consistently and are printed.

This is a schematic: unit operations and their order, not a mass balance, and
not to scale in any dimension.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import style

style.use()

# --- geometry -------------------------------------------------------------
# One drawing unit = 0.5 in, so the layout can be reasoned about in inches.
XW, YH = 21.8, 14.5
fig, ax = plt.subplots(figsize=(XW * 0.5, YH * 0.5))
style.blank(ax)
ax.set_xlim(0, XW)
ax.set_ylim(0, YH)

X1, X2, X3, X4 = 2.90, 6.00, 9.10, 12.20   # benefic., crack, leach, Th/medium
BUS1, X5, BUS2, X6 = 13.75, 15.70, 17.50, 19.70
W, WP, WF = 2.50, 2.80, 3.60               # standard, purification, feed

A1, A2 = 11.60, 9.30      # bastnäsite: chloride route, sulfuric route
B1, B2 = 6.90, 4.60       # monazite: sulfuric route, caustic route
CL = 1.90                 # ion-adsorption clay
ASPAN, BSPAN = (A1 + A2) / 2, (B1 + B2) / 2
MERGE, FEEDY = (A1 + A2 + B1 + B2) / 4, 5.00

SOLID, SULF, CHLOR = style.INK, style.ACCENT, style.AQUEOUS

LH, TH, PAD = 0.235, 0.30, 0.16   # body line, title line, box padding
FT, FB, FS = 6.8, 6.0, 6.2        # title, body, annotation font sizes

# --- primitives -----------------------------------------------------------


def node(xc, yc, title, lines=(), w=W):
    """A unit-operation box. Returns (left, right, bottom, top)."""
    h = 2 * PAD + TH + len(lines) * LH
    ax.add_patch(FancyBboxPatch((xc - w / 2, yc - h / 2), w, h,
                                boxstyle="round,pad=0.03",
                                fc=style.GROUND, ec=style.FAINT, lw=0.8,
                                zorder=4))
    ytop = yc + h / 2 - PAD
    ax.text(xc, ytop - TH / 2, title, fontsize=FT, color=style.INK,
            ha="center", va="center", zorder=5)
    y0 = ytop - TH - LH / 2
    for i, ln in enumerate(lines):
        ax.text(xc, y0 - i * LH, ln, fontsize=FB, color=style.MUTED,
                ha="center", va="center", zorder=5)
    return xc - w / 2, xc + w / 2, yc - h / 2, yc + h / 2


def head(x0, y0, x1, y1, color, lw=1.0):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                 mutation_scale=8, color=color, lw=lw,
                                 shrinkA=0, shrinkB=0, zorder=3))


def flow(x0, y0, x1, y1, color, xm=None, lw=1.0):
    """A stream: horizontal, then vertical, then an arrow into the target."""
    if abs(y1 - y0) < 1e-9:
        head(x0, y0, x1, y1, color, lw)
        return
    if xm is None:
        xm = (x0 + x1) / 2
    ax.plot([x0, xm, xm], [y0, y0, y1], color=color, lw=lw, zorder=3,
            solid_joinstyle="miter", solid_capstyle="butt")
    head(xm, y1, x1, y1, color, lw)


def side(xc, ybot, lines):
    """A waste or by-product stream leaving the bottom of a box."""
    head(xc, ybot, xc, ybot - 0.26, style.MUTED, lw=0.7)
    for i, ln in enumerate(lines):
        ax.text(xc, ybot - 0.42 - i * 0.26, ln, fontsize=5.9,
                color=style.MUTED, ha="center", va="center", style="italic")


def band(y0, y1, label):
    ax.add_patch(FancyBboxPatch((1.00, y0), 12.55, y1 - y0,
                                boxstyle="round,pad=0.02", fc="#f5f5f3",
                                ec="none", zorder=0))
    ax.text(0.48, (y0 + y1) / 2, label, fontsize=7.4, color=style.INK,
            ha="center", va="center", rotation="vertical")


# --- the three feedstocks -------------------------------------------------
band(8.20, 12.60, "bastnäsite ore")
band(3.45, 7.95, "monazite sand")
band(0.85, 3.15, "ion-adsorption clay")

for x, t in ((X1, "beneficiation"), (X2, "cracking"), (X3, "leaching"),
             (X4, "Th removal and\nmedium conversion"),
             (X5, "purification"), (X6, "separation feed")):
    ax.text(x, 13.05, t, fontsize=7.2, color=style.MUTED, ha="center",
            va="center", linespacing=1.35)

# --- bastnäsite -----------------------------------------------------------
_, br, bb, _ = node(X1, ASPAN, "Froth flotation",
                    ["rougher, cleaner,", "scavenger",
                     "→ ≈60 % REO conc."])
side(X1, bb, ["flotation tailings"])

# chloride route (Mountain Pass): never leaves chloride
al, ar, _, _ = node(X2, A1, "Oxidative roast",
                    ["after dilute HCl", "pre-leach of the",
                     "carbonate gangue", "air, ≈600 °C",
                     "Ce(III) → Ce(IV)"])
cl_, cr, cb, _ = node(X3, A1, "HCl leach", ["60-90 °C"])
side(X3, cb, ["cerium concentrate", "in the residue"])

# sulfuric route (Bayan Obo): leaches into sulfate, must convert
dl, dr, db, _ = node(X2, A2, "Sulfuric acid bake",
                     ["conc. H₂SO₄,", "400-600 °C"])
side(X2, db, ["HF and SiF₄ off-gas", "to scrubbing"])
el, er, _, _ = node(X3, A2, "Water leach", ["REE₂(SO₄)₃ dissolves"])
fl, fr, _, _ = node(X4, A2, "Medium conversion",
                    ["precipitate double", "sulfate or hydroxide",
                     "redissolve in HCl"])

flow(br, ASPAN, al, A1, SOLID, xm=(br + al) / 2)
flow(br, ASPAN, dl, A2, SOLID, xm=(br + al) / 2)
head(ar, A1, cl_, A1, SOLID)
head(dr, A2, el, A2, SOLID)
head(er, A2, fl, A2, SULF)

# --- monazite -------------------------------------------------------------
_, gr, gb, _ = node(X1, BSPAN, "Gravity + magnetic",
                    ["spirals, HIMS,", "electrostatic",
                     "→ monazite conc."])
side(X1, gb, ["ilmenite and zircon", "as co-products"])

hl, hr, _, _ = node(X2, B1, "Sulfuric digestion",
                    ["93-98 wt% H₂SO₄,", "200-250 °C"])
il, ir, _, _ = node(X3, B1, "Water leach",
                    ["REE and Th sulfates", "H₃PO₄ in the liquor"])
jl, jr, jb, _ = node(X4, B1, "Th removal",
                     ["primary amine from", "the sulfate liquor;",
                      "REE(OH)₃ at pH 8,", "redissolve in HCl"])
side(X4, jb, ["Th concentrate to", "licensed storage"])

kl, kr, _, _ = node(X2, B2, "Caustic digestion",
                    ["60-70 wt% NaOH,", "140-150 °C, 1 atm"])
ll, lr, lb, _ = node(X3, B2, "Water leach",
                     ["Na₃PO₄ dissolves;", "REE(OH)₃, Th(OH)₄",
                      "stay solid"])
side(X3, lb, ["Na₃PO₄ recovered", "for fertiliser"])
ml, mr, mb, _ = node(X4, B2, "Acid dissolution",
                     ["hydroxide cake in", "dilute HCl; Th(OH)₄",
                      "out at pH 4-5"])
side(X4, mb, ["Th(OH)₄ residue"])

flow(gr, BSPAN, hl, B1, SOLID, xm=(gr + hl) / 2)
flow(gr, BSPAN, kl, B2, SOLID, xm=(gr + hl) / 2)
head(hr, B1, il, B1, SOLID)
head(ir, B1, jl, B1, SULF)
head(kr, B2, ll, B2, SOLID)
head(lr, B2, ml, B2, SOLID)

# --- ion-adsorption clay: no beneficiation, no decomposition --------------
nl, nr, nb, _ = node(X3, CL, "Ion-exchange leach",
                     ["(NH₄)₂SO₄ or MgSO₄", "ambient, pH 4-6"])
side(X3, nb, ["residual NH₄⁺ on the ore → groundwater"])
ol, orr, _, _ = node(X4, CL, "P507 extraction",
                     ["PLS 200-1000 mg/L", "concentrated 10-50×,",
                      "stripped with HCl"])

head(1.65, CL, nl, CL, SOLID)
xa = (1.65 + nl) / 2
for dy, t in ((0.62, "0.05-0.3 % REO ore — no beneficiation,"),
              (0.36, "no roast, no digestion"),
              (-0.34, "leached in place through wells,"),
              (-0.60, "or heaped on a pad, for 20-100 days")):
    ax.text(xa, CL + dy, t, fontsize=FS, color=style.MUTED, ha="center",
            va="center")
head(nr, CL, ol, CL, SULF)

# --- convergence on one purified liquor -----------------------------------
pl, pr, pb, _ = node(X5, MERGE, "Impurity removal",
                     ["pH 3.5-4.5 → Fe(OH)₃", "pH 4.5-5.5 → Al(OH)₃",
                      "Ca as gypsum, PO₄³⁻", "as Ca₃(PO₄)₂"], w=WP)
side(X5, pb, ["Fe, Al, Ca and", "phosphate residues"])

ql, qr, _, _ = node(X6, FEEDY, "Feed to solvent extraction",
                    ["0.5-2.0 M total REE",
                     "chloride medium",
                     "(nitrate if HNO₃ used)",
                     "Fe < 100 ppm, Al < 500 ppm",
                     "Ca < 1000 ppm, Th < 10 ppm",
                     "PO₄³⁻ < 500 ppm, < 100 NTU"], w=WF)

for x0, y0 in ((cr, A1), (fr, A2), (jr, B1), (mr, B2)):
    flow(x0, y0, pl, MERGE, CHLOR, xm=BUS1)
ax.text((cr + BUS1) / 2, A1 + 0.40, "already chloride —",
        fontsize=FS, color=CHLOR, ha="center", va="center")
ax.text((cr + BUS1) / 2, A1 + 0.16, "no conversion step",
        fontsize=FS, color=CHLOR, ha="center", va="center")

flow(pr, MERGE, ql, FEEDY, CHLOR, xm=BUS2)
flow(orr, CL, ql, FEEDY, CHLOR, xm=BUS2)
ax.text((orr + BUS2) / 2, CL + 0.22, "Al, Fe and Ca minimal in the PLS",
        fontsize=FS, color=style.MUTED, ha="center", va="center")

# --- titles and legend ----------------------------------------------------
ax.text(0.20, 14.15,
        "Four ways to crack a rare earth mineral, one liquor to separate",
        fontsize=10.0, color=style.INK, ha="left", va="center")
ax.text(0.20, 13.72,
        "Schematic. Conditions are as this chapter states them; steps whose "
        "numbers the chapter gives inconsistently are left unlabelled.",
        fontsize=7.2, color=style.MUTED, ha="left", va="center")

# The legend sits under the feed box, the one large empty corner.
for y, c, lab in ((1.30, SOLID, "solid: ore, concentrate, calcine, cake"),
                  (0.95, SULF, "sulfate liquor"),
                  (0.60, CHLOR, "chloride liquor")):
    ax.plot([14.60, 15.15], [y, y], color=c, lw=1.4)
    ax.text(15.30, y, lab, fontsize=6.8, color=style.INK, ha="left",
            va="center")

ax.text(0.25, 0.30,
        "A sulfate route reaches a chloride feed only by going back through a "
        "solid: precipitate the rare earths, filter, redissolve in HCl.",
        fontsize=6.8, color=style.INK, ha="left", va="center")

style.save(fig, "05-flowsheet")
