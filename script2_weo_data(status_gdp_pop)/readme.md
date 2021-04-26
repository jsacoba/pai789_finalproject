# Script No. 2: Cleaning and Joining Data on Development Status, GDP and Population from the IMF Website

## A. Summary

This script uses `pandas` module of Python. The script is aimed at:

1. Cleaning the data set containing information on Development Status, Gross Domestic Product (GDP) per capita and Population of countries; and

2. Join the cleaned data sets.

## B. Input Data

There are various input files in this script:

1. World Economic Outlook data sets from the IMF webiste (3 files): `status_raw.csv`, `gdp_raw.csv`, and `pop_raw.csv`. The `status_raw.csv` file contains information on the economic status of countries. They are classified as : `Major Advanced Economy` which are the G7 countries,`Advanced Economy`, and `Emerging Market and Developing Economy`.

2. The mapping file `mapping_wri_clean.csv`  generated under `script1-wri_data`.

## C. Deliverables

1. A script called `join_weo_clean.py`; and

2. A joined file called `weo_data_clean.csv`.

## D. Instructions

1. Import `pandas` module as pd.

2. Read input files by calling `pd.read_csv` function.

3. Read the population and GDP as `float` by calling the `.str.replace(',','').astype(float)` from the `gdp_raw` and `pop_raw`.

4. Assign `gdp_clean` and `pop_clean` to the result of selecting the `ISO` and `2020` columns from `gdp_raw` and `pop_raw` using the `.iloc` function to  `gdp_raw` and `pop_raw` with arguments as follows:

    `gdp_clean = gdp_raw.loc[:194,['ISO', '2020']]`

    `pop_clean = pop_raw.loc[:192,['ISO', '2020']]`

5. Rename the `"ISO"` and `"2020"` columns from `gdp_raw` and `pop_raw` by calling `.rename` from the each data frames with argument: `(columns = {'ISO': 'iso3', '2020': 'GDP20'}, inplace = True)`.

6. Set `index` to `iso3` for `devstat_raw`, `gdp_clean`, and `pop_clean`.

7. Assign `weo_data_clean` to the result of joining the 3 data sets above using the `mapping` file. Use the `.join` call with arguments `on="iso3"` and `how='inner'`.

8. Set `iso3` as index on `weo_data_clean`.

9. Saved joined file as `weo_data_clean.csv`.


