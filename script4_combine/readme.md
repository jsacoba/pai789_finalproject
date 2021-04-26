# Script No. 4: Combining Data Sets: WRI, EPI and economic data from IMF the website.

## A. Summary

This script uses `pandas` module of `Python`. The script is aimed at joining data sets containing information on WRI, EPI and economic data of countries from the IMF website.

## B. Input Data

There are three input files in this script:

1. ***wri16to20_clean.csv*** which contains information about World Risk Index of 170 countries from 2016 to 2020.

2. ***epi_clean.csv*** which contains information about Environmental Perfromance Index of 180 countries in 2020.

3. ***weo_data_clean.csv*** which contains economic data of 193 countries in 2020.

## C. Deliverables

1. A script called ***combine.py***; and

2. A cleaned file called ***combined_clean.csv*** with records of 166 countries. This will serve as the final master file in the analysis.

## D. Instructions

1. Import `pandas` as `pd`.

2. Assign the names `wri`, `epi` and `weo` to the result of calling `pd.read_csv()` to the input files.

3. Print initial number of records by calling `len()` to each file. Use short message description of printed results.

4. Assign `indices` to the result of merging `epi` onto `wri`. Use the arguments:` on='iso3'`, `how='inner'`,`validate='1:1'`, and `indicator=True`.

5. Drop `"_merge"` from `indices` by calling `.drop` from `indices`, with the argument `axis="columns"`.

6. Rearrange `"region"` column's position (as third column). Start by assigning `pos_region` to the string `"region"`. Then, assign `third_col` to the result of calling `.pop()` to `indices` with `pos_region` as argument. This will return a series which basically selects the `region` column of the data set. Finally, call `.insert()` to `indices` with arguments `2`, `pos_region`, and `third_col`.

7. Merge `indices` and `weo`. Assign `indices_econ` to the result of merging `weo` onto `indices`. As in step number (4), use the arguments:` on='iso3'`, `how='inner'`,`validate='1:1'`, and `indicator=True`.

8. Drop the `"_merge"` column by calling `.drop()` from `indices_econ`. Add `axis="columns"` as argument.

9. Print number of dropped records from joining the three data sets. Since the `'epi'` data has the largest initial number of records, we will use that as benchmark on how much data was filtered out to the end. To do that, print with a short message on the result of subtracting `len(indices_econ)` from `len(epi)`. If all goes well, it should return 14 records dropped in all.

10. Set index to `'iso3'` by calling `set_index()` to `indices_econ`, with arguments `"iso3"`, `inplace = True`

11. Save file as `'combined_clean.csv'` by calling `.to_csv()` to `indices_econ`.



