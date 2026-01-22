# ---------------------------------------------------------------
#  Slope-graph • Entanglement lift  (example: COBYLA optimiser)
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
            "2 Lines", "Squares", "Wavy_Lines", "3 Circles", "6 Rectangles"]

# Define markers for each pattern
markers = ['o', 's', '^', 'v', 'D', 'P', 'X', '*', 'H']

# Replace the two arrays below with *test-accuracy* (%) values
baseline_acc  = np.array([88.15, 70.12, 81.65, 95.62, 89.55, 98.57, 89.32, 81.97, 75.57])

entangled_acc = np.array([92.17, 74.12, 88.05, 97.75, 90.35, 96.55, 90.12, 85.20, 88.60])
# ===============================================================

# colour palette with distinct hues (9 tasks → 9 colours)
cmap   = get_cmap('tab10')
colors = [cmap(i % 10) for i in range(len(patterns))]

# Increase figure width for more spacing
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
ax.set_ylim(70, 100)                      # adjust to your range
ax.set_xticks([0.5, 2.5])  # New x-tick positions
ax.set_xticklabels(["2-Qubit", "2-Qubit + Ent"])
ax.set_ylabel("Test accuracy (%)")
#ax.set_title("Slope-graph – Entanglement lift (COBYLA)")

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
plt.savefig('Fig_6(a).png', dpi=300, bbox_inches='tight')
plt.show()
