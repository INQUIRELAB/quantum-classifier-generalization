import matplotlib.pyplot as plt
import numpy as np

# === Global Font Settings ===
plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.weight': 'bold',
    'axes.labelweight': 'bold',
    'axes.titleweight': 'bold',
})

# Labels and data
labels = np.array([
    "Circle", "Crown", "Tricrown", "Line", "2 Lines",
    "Squares", "Wavy_Lines", "3 Circles", "6 Rectangles"
])
quantum = np.array([93.9, 91.425, 91.600, 97.350, 95.225, 93.075, 92.150, 88.900, 82.850])
classical = np.array([60.17, 50.41, 56.98, 98.39, 63.49, 34.09, 60.64, 28.54, 3.51])

# Radar chart setup
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # close the circle

# Close the data loop
classical_plot = np.append(classical, classical[0])
quantum_plot = np.append(quantum, quantum[0])

# Create radar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot classical
ax.plot(angles, classical_plot, linewidth=2, linestyle='solid', label='Classical', color='red')
ax.fill(angles, classical_plot, alpha=0.25, color='red')

# Plot quantum
ax.plot(angles, quantum_plot, linewidth=2, linestyle='solid', label='Quantum', color='blue')
ax.fill(angles, quantum_plot, alpha=0.25, color='blue')

# Set axis labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)
for label in ax.get_xticklabels():
    label.set_fontweight('bold')

# Set y-ticks and limit
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'], color="gray", size=12, fontweight='bold')
ax.set_ylim(0, 100)

# Add title and legend
plt.title('Quantum vs Classical Classifier Accuracy', size=16, y=1.08, fontweight='bold')
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), prop={'weight': 'bold', 'family': 'Times New Roman'})

plt.tight_layout()
plt.savefig("Fig_9.png")
plt.show()
