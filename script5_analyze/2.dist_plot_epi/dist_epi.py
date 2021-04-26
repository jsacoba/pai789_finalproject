# Import modules as needed.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read input file.

plots_data = pd.read_csv('plots_data.csv')

# Plot a 'Environmental Performance Index' density plot, using hue = 'Economic Status'.

fig, ax1 = plt.subplots()
sns.set_style('darkgrid')
sns.kdeplot(data=plots_data, shade=True, ax=ax1, x="EPI.new", hue = "Economic Status")
ax1.axvline(linewidth=2, color='r', linestyle="dotted")
ax1.set_xlabel('Environmental Performance Index')
fig.tight_layout()
fig.savefig('dist_epi_status.png', dpi=300)

# Plot a 'Environmental Performance Index' density plot, using hue = 'Economic Region'.

fig, ax1 = plt.subplots()
sns.set_style('darkgrid')
sns.kdeplot(data=plots_data, shade=True, ax=ax1, x="EPI.new", hue = "Economic Region")
ax1.axvline(linewidth=2, color='r', linestyle="dotted")
ax1.set_xlabel('Environmental Performance Index')
fig.tight_layout()
fig.savefig('dist_epi_region.png', dpi=300)

# Plot a 'Environmental Performance Index' density plot, using hue = 'Risk Description'.

fig, ax1 = plt.subplots()
sns.set_style('darkgrid')
sns.kdeplot(data=plots_data, shade=True, ax=ax1, x="EPI.new", hue = "Risk Description")
ax1.axvline(linewidth=2, color='r', linestyle="dotted")
ax1.set_xlabel('Environmental Performance Index')
fig.tight_layout()
fig.savefig('dist_epi_riskdesc.png', dpi=300)




