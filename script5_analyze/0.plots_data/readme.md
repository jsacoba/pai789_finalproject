# Script No. 5.0: Building Data for Plotting

## A. Summary

This script uses `pandas` module of Python. The script is aimed at building a data frame to be used in creating density plots.

## B. Input Data

There is one input data in this script: `combined_clean.csv` which was generated from the `script4_combine` folder.

## C. Deliverables

1. A script named `plots_data.py`.

## D. Instructions

1. Import `pandas as pd`.

2. Assign `combine` to the result of reading the input file `'combined_clean.csv'` by calling `pd.read_csv`.

3. Sort values by `"WRI_2020"` column by calling `.sort()` to `combined` with arguments `by="WRI_2020"`, and `ascending=False`.

4. Build a dictionary for renaming the column names. Assign `col_names` to the following set of keys and values: `{'Country_x': 'Country', 'status': 'Economic Status', 'region': 'Economic Region','risk_desc_2020': 'Risk Description', 'EPI.new': 'Environmental Performance Index', 'WRI_2020': '2020', 'WRI_2019': '2019', 'WRI_2018': '2018', 'WRI_2017': '2017', 'WRI_2016': '2016'}`

5. Using the dictionary we built, rename the columns by calling `.rename()` to `combined` with aruments `columns = col_names`, and `inplace=True`.

6. Build data frame for plotting density plots. Assign `dist_data` to the result of calling `.iloc` to `combined` with the arguments: `[:,[0,1,2,3,28,4,10,11,12,13,14]]`. The selection will return the following columns: 'Country'(1), 'Economic Region' (2), 'Risk Description'(3), 'Economic Status'(28), 
'2020'(4), '2019'(10), '2018'(11), '2017'(12), '2016'(13), and 'Environmental Performance Index'(14).

7. Call `.to_csv` to plots_data with argument `'plots_data.csv'` as file name.