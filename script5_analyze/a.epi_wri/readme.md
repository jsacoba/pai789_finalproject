# Script No. 5.a: Analyzing and Visualizing the EPI vs. WRI

## A. Summary

This script uses `pandas`, `matplotlib.pyplot`, `seaborn`, and `statsmodels.api` modules of `Python`. The script is aimed at:

1. Analyzing the relationship between EPI and WRI through regression; and

2. Visualizing the relationship given the country's by economic development status, economic region and qualitative risk rating.

## B. Input Data

There is only one input data in this script, which is the master file we generated in `script4_combine` folder. 

## C. Deliverables

1. Script named ***scatter_epi_wri.py***; and

2. Output file with name ***scatter_epi_region.png***, ***scatter_epi_riskdesc.png***, and ***scatter_epi_status.png***.

## D. Instructions

1. Import `pandas` as `pd`, `matplotlib.pyplot`, `seaborn` as `sns`, and `statsmodels.api` as `sm`.

2. Let us test the correlation of EPI and WRI by running a regression.

    a. Print a descritpive correlation message, then call `.corr()` to the `['2020']` column of `plots_data` with the argument 
    `corr(plots_data['EPI.new']`, then round the result to 3 decimal places. This will show the correlation coefficient.

# Define dependent variable.

y = plots_data['2020']

# Define independent variable

x = plots_data[['EPI.new']]

# Add constant to independent variable.

x = sm.add_constant(x)

# Fit linear regression model.

model = sm.OLS(y, x).fit(cov_type='HC1')

# Print model summary.

print(model.summary())

# Save regression results.

with open('ols_summary_epi_wri.txt', 'w') as fh:
          fh.write(model.summary().as_text())


2. Assign `plots_data` to the result of calling `pd.read_csv()` with the input file name as argument.

3. Plot a 'Environemntal Performance Index' density plot grouped by `'Economic Development Status'`.

    1. Start by assigning `fig, ax1` to `plt.subplots()`;

    2. Set grid color by calling `sns.set_style('darkgrid')`;

    3. Call kernel density estimate (KDE) plot as `sns.kdeplot()` with arguments `data=plots_data`, `shade=True`, `ax=ax1`, `"EPI.new"`, and `hue = "Economic Development Status"`;

    4. Plot a vertical red dotted line at x =0. Do it by calling `ax1.axvline()` with arguments `linewidth=2`, `color='r'`, and `linestyle="dotted")`;

    5. Set x-axis label to `"Environemntal Performance Index"`;

    6. Tighten figure by calling `fig.tight_layout()`; and

    7. Save the plot by calling `fig.savefig()` with`'dist_epi_status.png'` and `dpi=300` as arguments.

4. Plot a 'World Risk Index' density plot grouped by `'Economic Region'`. Follow the steps from 3.1 to 3.7 except that, set `hue='Economic Region'` and save the figure as `'dist_epi_region.png`.

5. Plot a 'World Risk Index' density plot grouped by `'Risk Description'`. Follow the steps from 3.1 to 3.7 except that, set `hue='Risk Description'` and save the figure as `'dist_epi_riskdesc.png`.
