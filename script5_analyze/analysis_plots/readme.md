
![Visual](https://github.com/jsacoba/pai789_finalproject/blob/main/aes-folder/visual.png)
Photo credits: `www.google.com`

# Script No. 5.3: Density and Scatter Plots

## A. Summary

This script uses `pandas`, `matplotlib.pyplot`, and `seaborn` modules of `Python`. The script is aimed at analyzing and visualizing the WRI data distribution of countries thru density plots and the relationship of EPI and WRI thru scatter plots.

## B. Input Data

There is only one input data in this script, which is the master file ***'combined_clean.csv'*** we generated in `script4_combine` folder. 

## C. Deliverables

1. Script named ***analysis_plot.py***; and

2. Output file with name ***dist_wri_region.png***, ***risk_region.png***, ***epi_wri_region.png***, and ***epi_wri_status.png***.

## D. Instructions

1. Import `pandas` as `pd`, `matplotlib.pyplot` as `plt` and import `numpy` as `np`.

2. Assign `plots_data` to the result of calling `pd.read_csv()` with the input file name `'combined_clean.csv'` as argument.

3. Plot a 'World Risk Index' density plot grouped by `'Economic Region'`.

    1. Start by assigning `fig, ax1` to `plt.subplots()`;

    2. Set grid color by calling `sns.set_style('darkgrid')`;

    3. Call kernel density estimate (KDE) plot as `sns.kdeplot()` with arguments `data=plots_data`, `shade=True`, `ax=ax1`, `x="2020"`, and `hue = "Economic Region'`;

    4. Plot a vertical red dotted line at x =0. Do it by calling `ax1.axvline()` with arguments `linewidth=2`, `color='r'`, and `linestyle="dotted")`;

    5. Set x-axis label to `"World Risk Index"`;

    6. Tighten figure by calling `fig.tight_layout()`; and

    7. Save the plot by calling `fig.savefig()` with`'dist_wri_region.png'` and `dpi=300` as arguments.

4. Now we will visualize the distribution of WRI of countries thru scatter plot. Start by assigning `fig, ax1` to `plt.subplots()`. 

5. Assign  `region` to the result of calling `sns.scatterplot()` using the following arguments: `x="2020"`, `y="Economic Region"`,`hue='Economic Region'`, `data=plots_data`, `s=15`, and `palette="muted"`.

6. Set grid color by calling `sns.set_style('darkgrid')`.

7. Set the axes label by calling `.set()` to `region` using `xlabel='World Risk Index'` and `ylabel='Economic Region'` as arguments.

8. Set the title of the scatter to `"World Risk Index per Economic Region"`, plot by calling `.set_title()` to `region`.

9. Tighten figure by calling `fig.tight_layout()`; and

10. Save the plot by calling `fig.savefig()` with `'risk_region.png'` and `dpi=300` as arguments.

11. Let us also create a scatter plot to visualize the relationship between `EPI` and `World Riesk Index`. Start by assigning `fig, ax1` to `plt.subplots()`.

12. Assign  `region` to the result of calling `sns.scatterplot()` using the following arguments: `x="EPI.new"`, `y="2020"`,`hue='Economic Region'`, `data=plots_data`, `s=15`, and `palette="muted"`.

13. Set grid color by calling `sns.set_style('darkgrid')`.

14. Set the axes label by calling `.set()` to `region` using `xlabel='Environmental Performance Index'` and `ylabel='World Risk Index'` as arguments.

15. Set the title of the scatter to `"EPI vs. WRI per Economic Region"`, plot by calling `.set_title()` to `region`.

16. Tighten figure by calling `fig.tight_layout()`; and

17. Save the plot by calling `fig.savefig()` with `'scatter_region.png'` and `dpi=300` as arguments.

11. Now we will create the same scatter plot, but with `hue=Economic Development Status`. Follow the same steps from 11 to 17, except that use `hue=Economic Development Status` and set the title of the scatter to `"EPI vs. WRI per Economic Development Status"`. Save the figure as `'scatter_status.png'`