![EPI](https://github.com/jsacoba/pai789_finalproject/blob/main/aes-folder/EPI.PNG)
Photo credits: `https://epi.yale.edu/downloads`

# Script No. 3: Cleaning and Processing Data: Environmental Performance Index (EPI) of Countries

## A. Summary

This script uses `pandas` module of `Python`. The script is aimed at cleaning the data set containing information on the Environmental Performance Index of 180 countries included in the 2020 report.

## B. Input Data

There is only one input file in this script:

1. The `epi20_raw.csv` file that is downloaded from `https://epi.yale.edu/downloads`. It is a large data set containing the EPI of 180 countries.

## C. Deliverables

1. A script called `epi.py`; and

2. A cleaned file called `epi_clean.csv` with records of 180 countries.

## D. Instructions

1. Import `pandas` module as `pd`.

2. Assign `epi_raw` to the result of reading `'epi_clean.csv'` using  `pd.read_csv()` call.

3. To keep track of data loss in filtering records, count and print initial number of observations by assigning `initial` to the result of calling `len()` to `epi_raw`. Then print the result with a description.

4. Select specific columns to be used in the analysis. Build a list called  `select` containing  the following column names: `'iso'`, `'region'`, `'EPI.new'`, `'HLT.new'`, `'AIR.new'`, `'H2O.new'`,`'HMT.new'`, `'WMG.new'`, `'ECO.new'`, `'BDH.new'`,`'ECS.new'`, `'FSH.new'`, `'CCH.new'`, `'APE.new'`, `AGR.new'`, and `'WRS.new'`.

5. EPI is basically a function of Environemntal Health and Ecosystem Vitality policy objectives. Each objectives have sub-issue categories. There are more sub-categories, but we will keep our analysis on the upper layer of classification. There are more sub-categories (indicators) for each Issue Category, but we will keep our analysis on the upper layer of indicator variables. To obtain understanding on these variables, assign `code` to the result of reading `'epi2020_indicators.csv'` file. Then, print `code`. It will print a table describing all indicator variables in the original EPI data set.

6. Build new data frame using the selected columns by assigning `epi_clean` to the result of calling `.loc()` to `epi_raw` using the arguments `[:181, select]`. :181 pertains to the number of row where the last record is located and reads from the first row in the data frame.

7. Rename `iso` to `iso3` to standardize join key in the next scripts. Use the `.rename()` call to `epi_clean` with aruments `columns={"iso":"iso3"}` and, `inplace=True`.

8. Count and print number of filtered observations. Assign `filtered` to the result of calling `len()` on `epi_clean`. Print `filtered` with appropriate description.

9. Set `'iso3'` as index by calling `set_index()` to `epi_clean` using `'iso3'` and `inplace = True` as arguments.

10. Save `epi_clean` as `'epi_clean.csv'` by calling `.to_csv()` to `epi_clean`. The output file contains the columns: `iso3`, `Economic Region` and `EPI` indicator variables described as follows:

![EPI indicators](https://github.com/jsacoba/pai789_finalproject/blob/main/script3_epi_data/epi_indicators.png)