# Script No. 5.2: Analyzing and Visualizing the EPI Distribution

## A. Summary

This script uses `pandas`, `matplotlib.pyplot`, and `seaborn` modules of `Python`. The script is aimed at:

1. Analyzing the data distribution of the EPI of countries; and

2. Visualizing the the distribution through a Density Plot by economic development status, economic region and qualitative risk rating.

## B. Input Data

There is only one input data in this script, which is the master file we generated in `script4_combine` folder. 

## C. Deliverables

1. Script named ***dist_epi.py***; and

2. Output file with name ***dist_epi_region.png***, ***dist_epi_riskdesc.png***, and ***dist_epi_status.png***.

## D. Instructions

1. Import `pandas` as `pd`, `matplotlib.pyplot` as `plt` and import `numpy` as `np`.

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
