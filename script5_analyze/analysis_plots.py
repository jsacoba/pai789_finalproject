import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read file.

plots_data = pd.read_csv('combined_clean.csv')


# ***A. Scatter Plot: World Risk Index per Economic Region.***

fig, ax1 = plt.subplots()
region =sns.scatterplot(x="2020", y="Economic Region", 
                         hue='Economic Region', data=plots_data, s=15, 
                         palette="muted")
sns.set_style('darkgrid')
region.set(xlabel='World Risk Index', ylabel='Economic Region')
region.set_title("World Risk Index per Economic Region")
fig.tight_layout()
fig.savefig('risk_region.png', dpi=300)

# ***B. Distribution Plot: World Risk Index per Economic Region.***

fig, ax1 = plt.subplots()
sns.set_style('darkgrid')
sns.kdeplot(data=plots_data, shade=True, ax=ax1, x="2020", 
            hue = "Economic Region")
ax1.axvline(linewidth=2, color='r', linestyle="dotted")
ax1.set_xlabel('World Risk Index')
fig.tight_layout()
fig.savefig('dist_wri_region.png', dpi=300)


# ***C. Scatter Plot: EPI vs. WRI per Economic Region.***


fig, ax1 = plt.subplots()
region =sns.scatterplot(x="EPI.new", y="2020", 
                         hue='Economic Region', data=plots_data, s=15, 
                         palette="muted")
sns.set_style('darkgrid')
region.set(xlabel='Environmental Performance Index', ylabel='World Risk Index')
region.set_title("EPI vs. WRI per Economic Region")
fig.tight_layout()
fig.savefig('epi_wri_region.png', dpi=300)


# ***C. Scatter Plot: EPI vs. WRI per Economic Development Status.***

fig, ax1 = plt.subplots()
region =sns.scatterplot(x="EPI.new", y="2020", 
                         hue='Economic Development Status', data=plots_data, s=15, 
                         palette="muted")
sns.set_style('darkgrid')
region.set(xlabel='Environmental Performance Index', ylabel='World Risk Index')
region.set_title("EPI vs. WRI per Economic Region")
fig.tight_layout()
fig.savefig('epi_wri_status.png', dpi=300)