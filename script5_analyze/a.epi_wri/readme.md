# Script No. 5.a: Analyzing and Visualizing the Relationship Between EPI vs. WRI

## A. Summary

This script uses `pandas`, `matplotlib.pyplot`, `seaborn`, and `statsmodels.api` modules of `Python`. The script is aimed at:

1. Analyzing the relationship between EPI and WRI through linear regression; and

2. Visualizing the relationship given the country's economic development status, economic region and qualitative risk level.

## B. Input Data

There is only one input data in this script ***combined_clean.csv***, which is the master file we generated in `script4_combine` folder. 

## C. Deliverables

1. Script named ***scatter_epi_wri.py***; and

2. Output files with names: ***scatter_epi_region.png***, ***scatter_epi_riskdesc.png***, and ***scatter_epi_status.png***.

## D. Instructions

1. Import `pandas` as `pd`, `matplotlib.pyplot`, `seaborn` as `sns`, and `statsmodels.api` as `sm`.

2. Let us test the correlation of EPI and WRI. Print a descritpive message, then call the `.corr()` function to the `['2020']` column of `plots_data` with the argument `corr(plots_data['EPI.new']`, then round the result to 3 decimal places. This will show the correlation coefficient.

3. Define dependent variable by assigning `y` to to the `['2020'` column of `plots_data`.

y = plots_data['2020']

4. Define independent variable by assigning `x` to to the `['EPI.new']` column of `plots_data`.

x = plots_data[['EPI.new']]

5. Add constant to independent variable by assigning `x` to the result of calling `sm.add_constant(x)`.

x = sm.add_constant(x)

6. Fit a linear regression model by assigning `model` to `sm.OLS(y, x).fit(cov_type='HC1')`

model = sm.OLS(y, x).fit(cov_type='HC1')

7. Print model summary by calling `.summary()` to `model`.

8. Save regression results as text file using the following syntax:

        `with open('ols_summary_epi_wri.txt', 'w') as fh:
            fh.write(model.summary().as_text())`

9. Now we will visualize the result of regression thru a scatter plot. Start by assigning `plots_data` to the result of calling `pd.read_csv()` with the input file `combined_clean.csv` as argument. Plot the correlation between EPI and WRI given their Economic Region.

    1. Start by assigning `fig, ax1` to `plt.subplots()`;

    2. Assign  `region_scatter` to the result of calling `sns.scatterplot()` using the following arguments: `x="EPI.new"`, `y="2020"`,`hue='Economic Region'`, `data=plots_data`, `s=15`, and `palette="muted"`.

    3. Set grid color by calling `sns.set_style('darkgrid')`;

    4. Set the axes label by calling `.set()` to `region_scatter` using `xlabel='Environmental Performace Index'` and `ylabel='World Risk Index'` as arguments.

    5. Set the title of the scatter to `"EPI vs. WRI per Economic Region"`, plot by calling `.set_title()` to `region_scatter`.

    6. Tighten figure by calling `fig.tight_layout()`; and

    7. Save the plot by calling `fig.savefig()` with`'scatter_region.png'` and `dpi=300` as arguments.

10. Plot the correlation between EPI and WRI given their Economic Development Status. Follow the steps from 9.1 to 9.7 except that, set `Economic Development Status'` and save the figure as `'scatter_status.png`.

11. Plot the correlation between EPI and WRI given their Risk Level. Follow the steps from 9.1 to 9.7 except that, set `Risk Level'` and save the figure as `'scatter_risk.png`.

## Code Credits

1. https://www.statology.org/simple-linear-regression-in-python/


