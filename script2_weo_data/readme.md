![WEO](https://github.com/jsacoba/pai789_finalproject/blob/main/aes-folder/WEO.PNG)

# Script No. 2: Cleaning and Joining Data on Development Status, GDP and Population from the IMF Website

## A. Summary

This script uses `pandas` module of Python. The script is aimed at:

1. Cleaning the data set containing information on Development Status, Gross Domestic Product (GDP) per capita and Population of countries; and

2. Join the cleaned data sets.

## B. Input Data

There are various input files in this script:

1. World Economic Outlook data sets from the IMF webiste `https://www.imf.org/en/Publications/WEO/weo-database/2020/October/select-country-group` (3 files): ***status_raw.csv***, ***gdp_raw.csv***, and ***pop_raw.csv***. When downloading the GDP file, select records for **all countries** and select **Gross domestic product per capita, constant prices** for **2020**  and select **ISO Alpha-3 Code** in the field selector. In a separate download under the same website, extract **population** from the selector for **2016 to 2020 and** select **ISO Alpha-3 Code**.

The ***status_raw.csv*** is a self-created file that contains information about the economic status of countries based from the same website above. Countries are classified as : ***Major Advanced Economy***, which are the G7 countries, ***Advanced Economy***, and ***Emerging Market and Developing Economy***.

2. The mapping file ***mapping_wri_clean.csv***  generated under the ***script1-wri_data*** folder in this repository.

## C. Deliverables

1. A script called ***join_weo_clean.py***; and

2. A joined file called ***weo_data_clean.csv*** that contains the following columns: `iso3`, `Country`, `Status`, `GDP` for 2020, and `Population` from 2016 to 2020. After joining the input files, the output file contains 193 countries.

## D. Instructions

1. Import `pandas` module as `pd`.

2. Read input files by calling `pd.read_csv()` function. Assign the reading of the files to the following names: `devstat_raw` for reading `'status_raw.csv'`; `gdp_raw` for reading `'gdp_raw.csv'`; and `pop_raw` for reading `'pop_raw.csv'`. In addition to the file name as argument, add `encoding = 'cp1252'`. Finally, assign `mapping` for reading `'mapping_wri_clean.csv'` ***without*** the need to put the `encoding = 'cp1252'` argument on it.

3. Read the population and GDP as `float` by calling `.str.replace(',','').astype(float)` from the `['2020']` column of `gdp_raw` and `pop_raw`.

4. Assign `gdp_clean` and `pop_clean` to the result of selecting the `ISO` and `2020` columns from both `gdp_raw` and `pop_raw` using the `.iloc()` function to  `gdp_raw` and `pop_raw` with arguments as follows:

    `gdp_clean = gdp_raw.loc[:194,['ISO', '2020']]`

    `pop_clean = pop_raw.loc[:192,['ISO', '2020']]`

    The `194` and `192` in the arguments pertain to the rows where the last records that we need are located.

5. Rename the `"ISO"` and `"2020"` columns from `gdp_raw` and `pop_raw` by calling `.rename()` from the each data frames using the following arguments: 1.) for `gdp_raw`, use `(columns = {'ISO': 'iso3', '2020': 'GDP'}, inplace = True)`; and 2.) for `pop_raw`, use the argument `(columns = {'ISO': 'iso3', '2020': 'Population'}, inplace = True)`. Finally, rename the `status` column of `devstat_raw`. Use the argument `(columns = {'status': 'Status'}, inplace = True)`.

6. Assign `weo_data_clean` to the result of joining the 3 data sets above using the `.merge()` call with arguments `on="iso3"` and `how='inner'`. Start calling `pd.merge()` with arguments `devstat_raw` and `gdp_clean`. Finally, call `.merge()` at the end of the first join, with arguments `on="iso3"` and `how='inner'`. 

7. Set the index to `iso3` by calling `.set_index()` to `weo_data_clean`, with additional argument `inplace=True`.

8. Saved joined file as `weo_data_clean.csv` by calling `.to_csv()` to `weo_data_clean`.


