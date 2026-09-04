"""Approach to equilibrium against contact time, and the kinetic window (ch. 9).

Panel (a) is the chapter's central quantitative claim drawn as a curve rather
than a table: the same first-order approach to equilibrium,

    E(t)/E_eq = 1 - exp(-k_L a * t),

evaluated with the two volumetric mass transfer coefficients the chapter's
Table 2 puts side by side. The microfluidic band is k_L a = 0.19-0.41 s^-1,
measured for slug flow in 269-400 um rectangular glass channels by Dessimoz
et al. (@dessimoz2008liquid); the conventional band is the 1e-3 to 1e-2 s^-1
order-of-magnitude figure the same table gives for a stirred contactor, which
carries no stated agitation condition and is therefore drawn as a wide band and
labelled as an order of magnitude, not a measurement.

Nothing in either band is data. The curves are the rate law; the *bands* are
the reported spread in k_L a. What makes the figure worth drawing is that the
two bands independently reproduce the two contact times the chapter quotes
from elsewhere: 0.19-0.41 s^-1 reaches 95% of equilibrium in 7-16 s, which
brackets the 3-60 s residence time of the flow-focusing droplet work
(@fernandezmaza2024high) and the "10-15 s" and "equilibrium within 30 s"
figures reported in the chapter; 1e-3 to 1e-2 s^-1 reaches 95% in 5-50 min,
which brackets the 10-25 min quoted for a mixer-settler. The two shaded
vertical windows are those quoted operating times, so the reader can check the
consistency by eye.

Panel (b) is the mechanism the chapter says bulk processing cannot use: if two
lanthanides share an equilibrium but not a rate, the separation exists only
before equilibrium. Both curves are the same first-order model; the faster one
uses the top of the measured microfluidic range, and the slower one is drawn a
factor of three slower. That 3x ratio is *illustrative* — the chapter names
Eu/La as a kinetically distinguished pair but gives no rate ratio for it, so
none is claimed here. The maximum of the gap is analytic,
t* = ln(k_f/k_s)/(k_f - k_s), and lands at 4 s, inside the microfluidic window
of panel (a), which is the whole argument for a contactor whose contact time is
settable to a fraction of a second.

No separation factor appears in this figure: the chapter attributes the same
Dy/La value to two different citation keys, and that has to be resolved before
the number can be drawn.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib.pyplot as plt
import style

style.use()

# Chapter Table 2, both columns.
KLA_MICRO = (0.19, 0.41)      # slug flow, 269-400 um channels, @dessimoz2008liquid
KLA_CONV = (1e-3, 1e-2)       # conventional contactor, order of magnitude only
T_MICRO = (3.0, 60.0)         # residence time, @fernandezmaza2024high
T_CONV = (600.0, 1500.0)      # 10-25 min mixer-settler

fig, (axa, axb) = plt.subplots(1, 2, figsize=(7.4, 3.5),
                               gridspec_kw=dict(width_ratios=[1.35, 1.0],
                                                wspace=0.30))

# ---------------------------------------------------------------- panel (a)
t = np.logspace(-2, 3.6, 900)


def approach(k):
    return 1.0 - np.exp(-k * t)


for band, color, alpha in ((KLA_CONV, style.MUTED, 0.16),
                           (KLA_MICRO, style.GOOD, 0.18)):
    lo, hi = approach(band[0]), approach(band[1])
    axa.fill_between(t, lo, hi, color=color, alpha=alpha, lw=0)
    axa.plot(t, lo, color=color, lw=1.0)
    axa.plot(t, hi, color=color, lw=1.0)

axa.axhline(0.95, color=style.MUTED, lw=0.7, ls=(0, (4, 3)), zorder=0)
axa.text(0.023, 0.965, "95% of equilibrium", color=style.MUTED, fontsize=7.5,
         ha="left", va="bottom")

axa.axvspan(*T_MICRO, color=style.ACCENT, alpha=0.10, lw=0)
axa.axvspan(*T_CONV, color=style.MUTED, alpha=0.12, lw=0)

axa.text(np.sqrt(T_MICRO[0] * T_MICRO[1]), 0.035,
         "3–60 s\nmicrofluidic\nresidence time", color=style.ACCENT,
         fontsize=7.5, ha="center", va="bottom", linespacing=1.35)
axa.text(np.sqrt(T_CONV[0] * T_CONV[1]), 0.035,
         "10–25 min\nmixer-settler", color=style.MUTED,
         fontsize=7.5, ha="center", va="bottom", linespacing=1.35)

axa.text(0.023, 0.83, "microfluidic slug flow\n$k_L a$ = 0.19–0.41 s$^{-1}$",
         color=style.GOOD, fontsize=8, ha="left", va="top", linespacing=1.4)
axa.text(0.023, 0.46,
         "conventional contactor\n$k_L a$ = 10$^{-3}$–10$^{-2}$ s$^{-1}$\n"
         "(order of magnitude,\nno agitation stated)",
         color=style.MUTED, fontsize=8, ha="left", va="top", linespacing=1.4)

axa.set_xscale("log")
axa.set_xlim(0.02, 4000)
axa.set_ylim(0, 1.06)
axa.set_xlabel("contact time (s)")
axa.set_ylabel("fraction of equilibrium extraction")
axa.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
axa.set_title("a   the same rate law, two contactors", loc="left",
              color=style.INK)

# ---------------------------------------------------------------- panel (b)
K_FAST = KLA_MICRO[1]
RATIO = 3.0
K_SLOW = K_FAST / RATIO
tb = np.linspace(0, 24, 600)
fast = 1.0 - np.exp(-K_FAST * tb)
slow = 1.0 - np.exp(-K_SLOW * tb)

t_star = np.log(RATIO) / (K_FAST - K_SLOW)
gap = np.exp(-K_SLOW * t_star) - np.exp(-K_FAST * t_star)

axb.fill_between(tb, slow, fast, color=style.ACCENT, alpha=0.14, lw=0)
axb.plot(tb, fast, color=style.INK, lw=1.6)
axb.plot(tb, slow, color=style.MUTED, lw=1.6, ls=(0, (5, 2.5)))

axb.plot([t_star, t_star], [1 - np.exp(-K_SLOW * t_star),
                            1 - np.exp(-K_FAST * t_star)],
         color=style.ACCENT, lw=1.2)
axb.plot([t_star], [1 - np.exp(-K_FAST * t_star)], marker="o", ms=3.5,
         color=style.ACCENT)
axb.plot([t_star], [1 - np.exp(-K_SLOW * t_star)], marker="o", ms=3.5,
         color=style.ACCENT)
axb.annotate(f"widest gap, {gap:.2f}\nat $t^*$ = {t_star:.0f} s",
             xy=(t_star + 0.05, 0.40), xytext=(t_star + 1.3, 0.28),
             color=style.ACCENT, fontsize=8, ha="left", va="center",
             linespacing=1.35,
             arrowprops=dict(arrowstyle="-", color=style.ACCENT, lw=0.8,
                             shrinkA=2, shrinkB=2))

axb.text(9.2, 0.985, "faster lanthanide", color=style.INK, fontsize=8,
         ha="left", va="bottom")
axb.text(15.0, 0.895, "slower lanthanide", color=style.MUTED, fontsize=8,
         ha="left", va="top")
axb.text(23.5, 0.06,
         "same equilibrium:\nthe gap closes if you wait",
         color=style.MUTED, fontsize=8, ha="right", va="bottom",
         linespacing=1.35)

axb.set_xlim(0, 24)
axb.set_ylim(0, 1.10)
axb.set_xlabel("contact time (s)")
axb.set_ylabel("fraction extracted")
axb.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
axb.set_title("b   selectivity only before equilibrium", loc="left",
              color=style.INK)

style.save(fig, "09-kinetics")
