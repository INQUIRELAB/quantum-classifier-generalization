# ---------------------------------------------------------------
#  Accuracy comparison for different minimization methods
#  --------------------------------------------------------------
#  1-Qubit Classifier
# ---------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

plt.rcParams["font.family"] = "Times New Roman"
# Set global font to bold
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'

# 1.  ==== YOUR DATA  ===========================================
patterns = ['Circle', 'Crown', 'Tricrown', 'Line',
            '2 Lines', 'Squares', 'Wavy_lines', '3 Circles', '6 Rectangles']

# Define different markers for each pattern
markers = ['o', 's', '^', 'v', 'D', 'P', 'X', '*', 'H']

# Accuracy data from Fig5.py
accuracy_data = {
    'Circle':      [96.82, 97.30, 96.82],
    'Crown':       [92.25, 91.40, 92.50],
    'Tricrown':    [88.55, 83.55, 89.27],
    'Line':        [97.17, 97.60, 96.92],
    '2 Lines':     [93.27, 91.95, 93.72],
    'Squares':     [91.12, 90.52, 91.35],
    'Wavy_lines':  [90.57, 90.17, 89.95],
    '3 Circles':   [82.30, 84.62, 87.10],
    '6 Rectangles':   [72.82, 74.27, 77.17],
}

# Prepare data for each optimizer
cobyla_acc = np.array([accuracy_data[pat][0] for pat in patterns])
nelder_acc = np.array([accuracy_data[pat][1] for pat in patterns])
slsqp_acc = np.array([accuracy_data[pat][2] for pat in patterns])

# colour palette with distinct hues (9 tasks → 9 colours)
cmap = get_cmap('tab10')
colors = [cmap(i % 10) for i in range(len(patterns))]

# Create single figure
fig, ax = plt.subplots(figsize=(8, 5))

# Plot lines for each pattern
x = np.array([0, 1, 2])  # Three points for three optimizers
optimizers = ['COBYLA', 'Nelder-Mead', 'SLSQP']

for idx, (pat, marker) in enumerate(zip(patterns, markers)):
    y = [accuracy_data[pat][i] for i in range(3)]
    ax.scatter(x, y,
               marker=marker,
               color=colors[idx],
               s=64,  # Make markers a bit larger (marker size in points^2)
               label=pat)

# Customize the plot
ax.set_xlim(-0.2, 2.2)
ax.set_ylim(70, 100)
ax.set_xticks(x)
ax.set_xticklabels(optimizers, fontweight='bold', fontsize=12)
ax.set_ylabel("Test accuracy (%)", fontweight='bold', fontsize=12)
#ax.set_title("1-Qubit Classifier Accuracy", fontweight='bold', pad=15, fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.grid(True, linestyle='--', alpha=0.3)
ax.spines[['top', 'right']].set_visible(False)

# Add legend
ax.legend(bbox_to_anchor=(1.04, 1), loc='upper left',
         borderaxespad=0.2, fontsize='small',
         title="Pattern", prop={'weight': 'bold'},
         title_fontproperties={'weight': 'bold'})

# Adjust layout and show plot
plt.tight_layout()
plt.savefig('Fig_5.png', dpi=300, bbox_inches='tight')
plt.show()
