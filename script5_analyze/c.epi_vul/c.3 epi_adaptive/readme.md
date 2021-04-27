# Script No. 5.c.3: Analyzing and Visualizing the Relationship Between EPI vs. Lack of Adaptive Capacities
## A. Summary

This script uses `pandas`, `matplotlib.pyplot`, `seaborn`, and `statsmodels.api` modules of `Python`. The script is aimed at:

1. Analyzing the relationship between EPI and Lack of Adaptive Capacities through linear regression; and

2. Visualizing the relationship given the country's economic development status, economic region and qualitative risk level.

## B. Input Data

There is only one input data in this script ***combined_clean.csv***, which is the master file we generated in `script4_combine` folder. 

## C. Deliverables

1. Script named ***scatter_epi_adaptive.py***; and

2. Output files with names: ***scatter_epi_region.png***, ***scatter_epi_risk.png***, and ***scatter_epi_status.png***.

## D. Instructions

1. Read input file by assigning `plots_data` to the result of calling `pd.read_csv()` to `'combined_clean.csv'`.

2. Import `pandas` as `pd`, `matplotlib.pyplot`, `seaborn` as `sns`, and `statsmodels.api` as `sm`.

3. Let us test the correlation of EPI and Lack of Adaptive Capacities. Print a descritpive message, then call the `.corr()` function to the `['Lack of Adaptive Capacities']` column of `plots_data` with the argument `corr(plots_data['EPI.new']`, then round the result to 3 decimal places. This will show the correlation coefficient.

4. Define dependent variable by assigning `y` to to the `['Lack of Adaptive Capacities']` column of `plots_data`.

5. Define independent variable by assigning `x` to to the `['EPI.new']` column of `plots_data`.

6. Add constant to independent variable by assigning `x` to the result of calling `sm.add_constant(x)`.

7. Fit a linear regression model by assigning `model` to `sm.OLS(y, x).fit(cov_type='HC1')`

8. Print model summary by calling `.summary()` to `model`.

9. Save regression results as text file using the following syntax:

        `with open('ols_summary_epi_wri.txt', 'w') as fh:
            fh.write(model.summary().as_text())`

10. Now we will visualize the result of regression thru a scatter plot. Start by assigning `plots_data` to the result of calling 
`pd.read_csv()` with the input file `combined_clean.csv` as argument. Plot the correlation between EPI and Lack of Adaptive Capacities given their Economic Region.

    1. Start by assigning `fig, ax1` to `plt.subplots()`;

    2. Assign  `region_scatter` to the result of calling `sns.scatterplot()` using the following arguments: `x="EPI.new"`, `y="Lack of Adaptive Capacities"`,`hue='Economic Region'`, `data=plots_data`, `s=15`, and `palette="muted"`.

    3. Set grid color by calling `sns.set_style('darkgrid')`;

    4. Set the axes label by calling `.set()` to `region_scatter` using `xlabel='Environmental Performance Index'` and `ylabel='Lack of Adaptive Capacities'` as arguments.

    5. Set the title of the scatter to `"EPI vs. Lack of Adaptive Capacities per Economic Region"`, plot by calling `.set_title()` to `region_scatter`.

    6. Tighten figure by calling `fig.tight_layout()`; and

    7. Save the plot by calling `fig.savefig()` with`'scatter_region.png'` and `dpi=300` as arguments.

11. Plot the correlation between EPI and Lack of Adaptive Capacities given their Economic Development Status. Follow the steps from 9.1 to 9.7 except that, set `'Economic Development Status'` and save the figure as `'scatter_status.png'`.

12. Plot the correlation between EPI and Lack of Adaptive Capacities given their Risk Level. Follow the steps from 9.1 to 9.7 except that, set `'Risk Level'` and save the figure as `'scatter_risk.png'`.

## Code Credits

1. https://www.statology.org/simple-linear-regression-in-python/


