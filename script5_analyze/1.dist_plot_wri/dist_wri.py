# Import modules as needed.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read input file.

plots_data = pd.read_csv('combined_clean.csv')

# Plot a 'World Risk Index' density plot, using hue = 'Economic Status'.

fig, ax1 = plt.subplots()
sns.set_style('darkgrid')
sns.kdeplot(data=plots_data, shade=True, ax=ax1, x="2020", hue = "Economic Development Status")
ax1.axvline(linewidth=2, color='r', linestyle="dotted")
ax1.set_xlabel('World Risk Index')
fig.tight_layout()
fig.savefig('dist_wri_status.png', dpi=300)

# Plot a 'World Risk Index' density plot, using hue = 'Economic Region'.

fig, ax1 = plt.subplots()
sns.set_style('darkgrid')
sns.kdeplot(data=plots_data, shade=True, ax=ax1, x="2020", hue = "Economic Region")
ax1.axvline(linewidth=2, color='r', linestyle="dotted")
ax1.set_xlabel('World Risk Index')
fig.tight_layout()
fig.savefig('dist_wri_region.png', dpi=300)

# Plot a World Risk Index density plot, using hue = 'Risk Level'.

fig, ax1 = plt.subplots()
sns.set_style('darkgrid')
sns.kdeplot(data=plots_data, shade=True, ax=ax1, x="2020", hue = "Risk Level")
plots_data
ax1.axvline(linewidth=2, color='r', linestyle="dotted")
ax1.set_xlabel('World Risk Index')
fig.tight_layout()
fig.savefig('dist_wri_risk.png', dpi=300)




