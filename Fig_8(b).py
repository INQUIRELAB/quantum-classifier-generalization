# ---------------------------------------------------------------
#  NELDER-MEAD –  error vs generalisation gap   (shape-coded points)
# ---------------------------------------------------------------
#
#  • pure matplotlib (no seaborn)
#  • distinct marker shape per pattern
#  • colour   = generalisation gap
#  • shape    = pattern identity  →  legend outside plot
#
# ---------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['font.size'] = 12

# 1.  ==== DATA  =================================================
patterns = ["Circle",
            "Crown",
            "Tricrown",
            "Line",
            "2 Lines",
            "Squares",
            "Wavy",
            "3 Circles",
            "6 Squares"]

# Converting accuracies to errors (error = 1 - accuracy/100)
train_err = np.array([0.08325, 0.19925, 0.17100, 0.03275,
                      0.07675, 0.02300, 0.10825, 0.17250, 0.26800])
test_err = np.array([0.07050, 0.09275, 0.15600, 0.03600,
                     0.08825, 0.02675, 0.08700, 0.13400, 0.10950])

gap = test_err - train_err          # generalisation gap
print(gap)
# One unique marker for each pattern
markers = ['o', 's', '^', 'v', 'D', 'P', 'X', '*', 'H']

# Create custom colormap matching the reference image
colors = ['#000080',  # Dark blue
          '#0000FF',  # Blue
          '#00FFFF',  # Cyan
          '#00FF00',  # Green
          '#FFFF00',  # Yellow
          '#FF8C00',  # Orange
          '#FF0000',  # Red
          '#FF1493']  # Deep pink

custom_cmap = LinearSegmentedColormap.from_list('custom', colors)

# 2.  ==== PLOT  =================================================
fig, ax = plt.subplots(figsize=(7, 4))

# draw each point individually so it gets its own shape
for i, pat in enumerate(patterns):
    sc = ax.scatter(train_err[i],
                    test_err[i],
                    c=gap[i],
                    cmap=custom_cmap,  # Use custom colormap
                    vmin=-0.02,  # Updated range for Nelder-Mead data
                    vmax=0.03,  # Updated range for Nelder-Mead data
                    marker=markers[i],
                    s=90,
                    edgecolors='k',
                    label=pat)

# reference diagonal (ideal train = test)
ax.plot([0, max(train_err)*1.1],
        [0, max(test_err)*1.1],
        linestyle='--',
        linewidth=1.5,
        color='#E69F00')

# axis labels & title
ax.set_xlabel('Train error', fontweight='bold', fontsize=12)
ax.set_ylabel('Test error', fontweight='bold', fontsize=12)

# colour-bar for the gap
cbar = plt.colorbar(sc, ax=ax, label='Generalization Gap', pad=0.02)
cbar.set_label('Generalization Gap', fontweight='bold', fontsize=12)

# neat limits & grid
ax.set_xlim(0, max(train_err)*1.1)
ax.set_ylim(0, max(test_err)*1.1)
ax.grid(alpha=0.3, linestyle=':')

# Make tick labels bold
ax.tick_params(axis='both', which='major', labelsize=12)
for tick in ax.get_xticklabels():
    tick.set_fontweight('bold')
for tick in ax.get_yticklabels():
    tick.set_fontweight('bold')
    
# Make colorbar ticks bold
cbar.ax.tick_params(labelsize=12)
for tick in cbar.ax.get_yticklabels():
    tick.set_fontweight('bold')

# legend outside the plot area, closer to colorbar
ax.legend(title='Pattern',
          bbox_to_anchor=(1.25, 1), loc='upper left',
          borderaxespad=0.2, fontsize=12,
          title_fontproperties={'weight': 'bold', 'size': 12},
          prop={'weight': 'bold', 'size': 12})

# Make colorbar label and ticks bold
cbar.ax.tick_params(labelsize=12)
cbar.ax.set_ylabel('Generalization Gap', fontweight='bold', fontsize=12)
for tick in cbar.ax.get_yticklabels():
    tick.set_fontweight('bold')

plt.tight_layout()
plt.savefig('Fig_8(b).png', dpi=300, bbox_inches='tight', pad_inches=0.2)
plt.show() 