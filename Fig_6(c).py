# ---------------------------------------------------------------
#  Slope-graph • Entanglement lift  (example: SLSQP optimiser)
#  --------------------------------------------------------------
#  x-axis has two categorical positions:
#      0  →  2-Qubit   (no entanglement)
#      1  →  2-Qubit + Entanglement
#
#  Each classification pattern is a line; upward = accuracy gain
# ---------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'

# 1.  ==== YOUR DATA  ===========================================
patterns = ["Circle", "Crown", "Tricrown", "Line",
            "2 Lines", "Squares", "Wavy_Lines", "3 Circles", "6 Squares"]

# Define markers for each pattern
markers = ['o', 's', '^', 'v', 'D', 'P', 'X', '*', 'H']

# Data from Fig 8_SLSQP.py (reordered to match pattern order)
baseline_acc = np.array([91.000, 91.925, 88.900, 96.200, 
                        93.600, 99.775, 92.925, 88.900, 73.950])

entangled_acc = np.array([94.925, 90.625, 89.775, 96.850, 
                         94.175, 99.650, 92.300, 84.900, 86.775])

# ===============================================================

# colour palette with distinct hues (9 tasks → 9 colours)
cmap = get_cmap('tab10')
colors = [cmap(i % 10) for i in range(len(patterns))]

# Create figure
fig, ax = plt.subplots(figsize=(6, 3))

for idx, (pat, marker) in enumerate(zip(patterns, markers)):
    # Plot points at 0.5 and 2.5 instead of 0 and 1 for more spacing
    ax.scatter([0.5, 2.5],
               [baseline_acc[idx], entangled_acc[idx]],
               marker=marker,
               color=colors[idx],
               s=64,  # Make markers a bit larger (marker size in points^2)
               label=pat)

# axes cosmetics
ax.set_xlim(0, 3)  # Adjusted x-limits for new point positions
ax.set_ylim(70, 101)                      # adjust to your range
ax.set_xticks([0.5, 2.5])  # New x-tick positions
ax.set_xticklabels(["2-Qubit", "2-Qubit + Ent"])
ax.set_ylabel("Test accuracy (%)")
#ax.set_title("Slope-graph – Entanglement lift (SLSQP)")

# light vertical guide lines
ax.axvline(0.5, color='grey', alpha=0.2)  # Adjusted guideline positions
ax.axvline(2.5, color='grey', alpha=0.2)

# optional legend outside plot
ax.legend(bbox_to_anchor=(1.04, 1),
         loc='upper left',
         borderaxespad=0.2,
         fontsize='small',
         title="Pattern")

ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('Fig_6(c).png', dpi=300, bbox_inches='tight')
plt.show() 