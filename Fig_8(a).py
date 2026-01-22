# ---------------------------------------------------------------
#  CO B Y L A –  error vs generalisation gap   (shape-coded points)
# ---------------------------------------------------------------
#
#  • pure matplotlib (no seaborn)
#  • distinct marker shape per pattern
#  • colour   = generalisation gap
#  • shape    = pattern identity  →  legend outside plot
#
#  Replace the arrays below with your real numbers and rerun.
# ---------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['font.size'] = 12
# 1.  ==== DATA  =================================================
patterns = ["Circle",
            "Crown",
            "Tricrown",
            "Line",
            "2 Lines",
            "Squares",
            "Wavy_Lines",
            "3 Circles",
            "6 Rectangles"]

#  (Put your measured errors here)
train_err = np.array([0.14527358, 0.14130376, 0.06754714, 0.09642499,
                      0.12559708, 0.03961308, 0.04605944, 0.07136096, 0.0768812])
test_err  = np.array([0.16328215, 0.12714461, 0.06879348, 0.1063123,
                      0.11789481, 0.0512426, 0.05830045, 0.09711928, 0.06828279])

gap = test_err - train_err          # generalisation gap

# One unique marker for each pattern (≥ 10? recycle or add more)
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
                    vmin=-0.02,  # Match the range from the reference image
                    vmax=0.03,   # Match the range from the reference image
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
#ax.set_title('COBYLA – error vs generalisation gap', fontweight='bold', fontsize=12)

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

# Create custom legend handles with empty markers
legend_handles = []
for i, pat in enumerate(patterns):
    handle = Line2D([0], [0], 
                   marker=markers[i], 
                   color='white',  # Line color (not visible since linestyle='None')
                   markerfacecolor='none',  # Empty interior
                   markeredgecolor='black',  # Black edges
                   markeredgewidth=1.5,  # Edge thickness
                   markersize=8,  # Marker size
                   linestyle='None',  # No line
                   label=pat)
    legend_handles.append(handle)

# legend outside the plot area, with increased distance from colorbar
ax.legend(handles=legend_handles,
          title='Pattern',
          bbox_to_anchor=(1.35, 1), loc='upper left',
          borderaxespad=0.3, fontsize=12,
          title_fontproperties={'weight': 'bold', 'size': 12},
          prop={'weight': 'bold', 'size': 12})

# Make colorbar label and ticks bold
cbar.ax.tick_params(labelsize=12)
cbar.ax.set_ylabel('Generalization Gap', fontweight='bold', fontsize=12)
for tick in cbar.ax.get_yticklabels():
    tick.set_fontweight('bold')

plt.tight_layout()
plt.savefig('Fig_8(a).png', dpi=300, bbox_inches='tight', pad_inches=0.2)
plt.show()

