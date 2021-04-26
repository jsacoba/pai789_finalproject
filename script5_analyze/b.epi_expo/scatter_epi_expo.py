# Import modules.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Read input file.

plots_data = pd.read_csv('plots_data.csv')

# Testing Correlation between EPI and Exposure.

# Print correlation coefficient.

print('\nCorrelation Coefficient (EPI vs. Exposure):', round(plots_data['Exposure'].corr(plots_data['EPI.new']), 3))

# Define dependent variable.

y = plots_data['Exposure']

# Define independent variable

x = plots_data[['EPI.new']]

# Add constant to independent variable.

x = sm.add_constant(x)

# Fit linear regression model.

model = sm.OLS(y, x).fit(cov_type='HC1')

# Print model summary.

print(model.summary())

# Save regression results.

with open('ols_summary_epi_expo.txt', 'w') as fh:
          fh.write(model.summary().as_text())


# Visualize data.

# a. Correlation between EPI and Exposure per Economic Region.

fig, ax1 = plt.subplots()
region_scatter =sns.scatterplot(x="EPI.new", y="Exposure", 
                         hue='Economic Region', data=plots_data, s=15, 
                         palette="muted")
sns.set_style('darkgrid')
region_scatter.set(xlabel='Environmental Performace Index', ylabel='Exposure')
region_scatter.set_title("EPI vs. Exposure per Economic Region")
fig.tight_layout()
fig.savefig('scatter_region.png', dpi=300)

# b. Correlation between EPI and Exposure per Economic Status.

fig, ax1 = plt.subplots()
status_scatter =sns.scatterplot(x="EPI.new", y="Exposure", 
                         hue='Economic Status', data=plots_data, s=15,
                         palette="muted")
sns.set_style('darkgrid')
status_scatter.set(xlabel='Environmental Performace Index', ylabel='Exposure')
status_scatter.set_title("EPI vs. Exposure per Economic Status")
fig.tight_layout()
fig.savefig('scatter_status.png', dpi=300)

# c. Correlation between EPI and Exposure per Risk Description.

fig, ax1 = plt.subplots()
status_scatter =sns.scatterplot(x="EPI.new", y="Exposure", 
                         hue='Risk Description', data=plots_data, s=15,
                         palette="muted")
sns.set_style('darkgrid')
status_scatter.set(xlabel='Environmental Performace Index', ylabel='Exposure')
status_scatter.set_title("EPI vs. Exposure per Risk Type")
fig.tight_layout()
fig.savefig('scatter_risktype.png', dpi=300)


# Code credits:
    
# https://www.statology.org/simple-linear-regression-in-python/


