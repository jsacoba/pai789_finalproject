import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read input file.

analyze = pd.read_csv('combined_clean.csv')

analyze['dup'] = analyze.Exposure.duplicated(keep=False) & analyze.Exposure.notna()

dup_risk = analyze[analyze['dup'] == True]

dup_risk.to_csv('same_exposure.csv')

advanced = analyze[analyze['Economic Development Status'] == 'Major Advanced Economy']

rich = analyze.nlargest(10, ['GDP'])

poor = analyze.nsmallest(10, ['GDP'])

extremes = pd.concat([rich, poor], axis = 0)

fig, ax1 = plt.subplots()
region_scatter =sns.scatterplot(x="2020", y="Economic Region", 
                         hue='Economic Region', data=analyze, s=15, 
                         palette="muted")
sns.set_style('darkgrid')
region_scatter.set(xlabel='World Risk Index', ylabel='Economic Region')
region_scatter.set_title("Economic Region vs. World Risk Index")
fig.tight_layout()
fig.savefig('scatter_region.png', dpi=300)
                   