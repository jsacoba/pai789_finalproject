# Script No. 5.1: Data Analysis

## A. Summary

This script uses `pandas` module of `Python`. The script is aimed at extracting data from the master file ***combined_clean.csv*** file for the analysis.

## B. Input Data

There is only one input data in this script, which is the master file ***combined_clean.csv*** we generated in `script4_combine` folder. 

## C. Deliverables

1. Script named ***analysis_data.py***; and

2. Output files with names ***advanced.csv***, ***extremes.csv***, and ***same_exposure.csv***. The column names are similar to those in the master file. The ***advanced.csv*** file contains information about the G7 countries; ***extremes.csv*** contains the top 10 (richest) and bottom 10 (poorest) countries in terms of GDP per capita, and; ***same_exposure.csv*** contains a list of countries with same Exposure Index for 2020. 

## D. Instructions

1. Import `pandas` as `pd`.

2. Read input file by assigning `analyze` to the result of calling `pd.to_csv()` on `'combined_clean.csv'`.

3. Now extract countries with the same Risk Exposure Index. Start by creating a column named `'dup'` in `analyze` that is equal to the result of calling `.duplicated()` to the `Exposure` column of `analyze` with arguments `(keep=False) & analyze.Exposure.notna()`. That is:

    `analyze['dup'] = analyze.Exposure.duplicated(keep=False) & analyze.Exposure.notna()`

4. Create a new data frame for the selected countries. Assign `same_exposure` to the result of calling the `dup` column of analyze and use the argument `== True`. That is:

    `same_exposure = analyze[analyze['dup'] == True]`

5. Save the new data frame by calling `.to_csv()` to `same_exposure`. Use the file name `same_exposure.csv`.

6. Now we create new data frame for the major advanced economies. Redo step number 4, except that use the `'Economic Development Status'` of `analyze` and use the argument `== 'Major Advanced Economy'`.

7. Save the new data frame by calling `.to_csv()` to `advanced`. Use the file name `advanced.csv`.

8. Now we select the top 10 richest countries based on their GDP per capita. Start by assigning `rich` to the result of calling `.nlargest` method of `analyze` with arguments `10` and `['GDP']`.

9. Then, we select the top 10 poorest countries based on their GDP per capita. Start by assigning `poor` to the result of calling `.nsmallest` method of `analyze` with arguments `10` and `['GDP']`.

10. Concatenate `rich` and `poor` by assigning `extremes` to the result of calling `pd.concat()` with arguments `[rich, poor]` and `axis = 0`.

11. Save the new data frame by calling `.to_csv` to `extremes`. Use the file name `extremes.csv`.
