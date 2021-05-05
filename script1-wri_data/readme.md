![2020 World Risk Report Image](https://github.com/jsacoba/pai789_finalproject/blob/main/aes-folder/World%20Risk%20Report.PNG)

# Script No. 1: Joining Data from the World Risk Index (WRI) Report (2016 to 2020)

## A. Summary

This script uses `pandas` and `numpy` modules of `Python`. The script is aimed at:

1. Creating a master file by joining rankings of countries that were consistently included in the WRI Report from 2016 to 2020; and

2. Creating a mapping file to be used in joining the master file to other data sourced from other open repositories.

## B. Input Data

There are various input data in this script:

1. WRI files (5 files): ***wri2016_raw.csv***, ***wri2017_raw.csv***, ***wri2018_raw.csv***, ***wri2019_raw.csv*** and ***wri2020_raw.csv***. These were extracted from the ***'Appendix'*** portion of the ***WorldRiskIndex*** reports from 2016 to 2020 which come in `.pdf` format. The reports can be downloaded from `https://weltrisikobericht.de/english/`. Each report contains different number of countries ranked:

      ***wri2016_raw.csv*** - 171 countries

      ***wri2017_raw.csv*** - 171 countries

      ***wri2018_raw.csv*** - 172 countries

      ***wri2019_raw.csv*** - 180 countries

      ***wri2020_raw.csv*** - 181 countries

2. Mapping files (5 files): ***iso16_map.csv***, ***iso17_map.csv***, ***iso18_map.csv***, ***iso19_map.csv*** and ***iso20_map.csv***. There were inconsistencies in naming the countries in the WRI reports from 2016 to 2020. Mapping files were created to facilitate joining rankings of countries that have been included in the ***WorldRiskIndex*** Report for five years. The mapping files contain the countries ***'as named'*** in each report year, and the 3-letter ***ISO code*** for each country.

## C. Deliverables

1. A script named ***join_wri16to20.py***;

2. Output file with name ***wri16to20_clean.csv*** that consolidates WRIs for five years. To reiterate, take note that the WRI reports contain different number of countries. This output file contains WRIs for countries that have been consistently included in the report for five years. After joining the input files, the output file contains 170 countries; and

3. Based from the consolidated records, a mapping file called ***mapping_wri_clean.csv*** is made to serve as master file in joining ***wri16to20_clean.csv*** with other variables from other data sets.

## D. Instructions

1. Import `pandas` as `pd` and import `numpy` as `np`.

2. Read the input files with file format ***wriyear_raw*** (e. g. `wri2020_raw.csv`) by calling `pd.read_csv()` to each of the file and assign the following names to each read files: `wri_raw16`, `wri_raw17`, `wri_raw18`, `wri_raw19` and `wri_raw20`, respectively.

3. Drop some columns in each data frame. 

   1. Start by dropping the `Rank` column in  `wri_raw20` by calling `.drop()` using the arguments `"Rank"` and `axis = "columns"`.

   2. Then, for `wri_raw16`, `wri_raw17`, `wri_raw18`, and `wri_raw19` data frames,  drop the `"Rank"`, `"Exposure"`, `"Vulnerability"`, `"Susceptibility"`, `"Lack of  Coping Capacities"`, and `"Lack of Adaptive Capacities"`. This means that we only want to retain the WRI for each year, and the `Vulnerability`, `Susceptibility`, `Lack of Coping Capacities`, and `Lack of Adaptive Capacities`columns for the year 2020 data.
   
4. Read the input files with file format ***isoyear_map*** (e. g. `iso20_map.csv`) by calling `pd.read_csv` to each file. As in  number (2) use the following variable names: `map_alpha16`, `map_alpha17`, `map_alpha18  `, `map_alpha19` and. `map_alpha20`, respectively. 

   The `Country` column of the mapping files are identical to the `Country`  column of the `wri` files. The  3-letter `iso` codes serve  two purposes. First, this will facilitate joining the data sets to for the countries that were named differently in the reports, and second, dropping out countries that have not been consistently included in the report in the last five years. 
   
5. Map the 3-letter `iso` code to each `wri` file to standardize `key` for  joining the WRI data from 2016 to 2020. Do it by calling `.merge()` function to each joins and assign each joins to a file name of format `wriyear`. For example:

      `wri20 = wri20.merge(map_alpha20, on='Country', how='left')`
          
6. Rename the `WorldRiskIndex` column in each `wri` data set by calling `.rename()` function in each file with arguments `columns= {"WorldRiskIndex" : "2020"}`, and `inplace=True`. Do this in every `wri` file.

7. In each `wri` file, set the `iso3` column as `index`  by calling `.set_index()` in the file with the arguments `"iso3"` and `inplace=True`.

8. Drop the `Country` column for the 2016 to 2019 `wri` files by calling `.drop()` in each of the file with the arguments `["Country"]`, `inplace = True`, and `axis=1`.

9. To keep track of how much data will be filtered, we will count the number of initial records. Start by assigning `count_20` to the result of calling `len(wri20)`. Then print `count_20` with a description. If all goes well, the count should be 181. This means that the 2020 WRI Report ranked 181 countries.

10. Now let us join the data sets. Using `.join()`, start with joining `wri20` to `wri19`, then to  `wri18`, `wri17`and finally `wri16` using `how="inner"` in the argument for each join. Assign the join call to `wri16_to_20`. We used the `wri20` file first to rule that it is the master file. This means that the countries with complete records for 5 years that were ranked from 2016 up to 2020 are the only ones retained. For clarity, do it like this:

      `wri16_to_20 = wri20.join(wri19, how="inner").join(wri18, how="inner").join(...2016)`
        
11. To keep track how much data have been filtered out, count the number of countries  with complete records. Start by assigning `count_final` to `len(wri16_to_20)`. Print the result with description. Then, print a message describing the  result of subtracting `count_final` from `count_20`. If all goes well, countries with complete records should be 170, thus with dropped records of 11.

12. Now let us assign risk description for each WRI in 2020. Start by setting the conditions for risk description scale from the WRI Report. Build a list called `conditions` containing arguments for range of values. Set up as follows:

      `[(wri16_to_20["2020"] >= 0.31) & (wri16_to_20["2020"] <= 3.29),`

      `(wri16_to_20["2020"] >= 3.30) & (wri16_to_20["2020"] <= 5.67),`

      `(wri16_to_20["2020"] >= 5.68) & (wri16_to_20["2020"] <= 7.58),`

      `(wri16_to_20["2020"] >= 7.59) & (wri16_to_20["2020"] <= 10.75),`
      
      `(wri16_to_20["2020"] >= 10.76) & (wri16_to_20["2020"] <= 49.74)]`
      
13. Then, build a list of qualitative description of the risk range of values. Set `'values'` to a list of string: `"Very Low"`, `"Low"`, `"Medium"`, `"High"`, `"Very High"`.

14. Assign risk description to the WRI of each countries by adding a new column called `"Risk Description"` in `wri16_to_20` by calling `np.select()` with arguments `conditions` and `values`.

15. Now let us rearrange the columns. Do it by assigning `wri16_to_20` to the result of calling the `columns` of `wri16_to_20` with a list of the column locations that  we need to retain. Use the argument `[0,11,1,2,3,4,5,6,7,8,9,10]`.

16. Double check for missing values or records. Start by assigning `na_values` to the  result of calling `.isna().any()` to `wri16_to_20`. That is:

      `na_values = wri16_to_20[wri16_to_20.isna().any(axis=1)]`
      
17. Then print `na_values`. If all goes well, it should return an empty data frame. 

18. Now let us create a final mapping file. This will serve as master mapping file for all succeeding merging or joining of information from other data sets. Start building the mapping file by assigning `mapping_wri` to  the result of calling `.iloc()` to `wri16_to_20` with argument `:, 0:1`. This will select the 3-letter `iso` code and `Country` column of the cleaned data `wri16_to_20`.

19. Save cleaned data sets. Save the cleaned WRI data set by calling `.to_csv()` to `wri16_to_20`. Use the filename `wri16to20_clean.csv`. Then save the mapping  file by calling `.to_csv()` to `mapping_wri` and use the filename `mapping_wri_clean.csv`. he data cleaned data set contains the following columns:

      `iso3`            - refers to the UN 3-letter alpha code for countries.

      `Country`         - country name as reported in the 2020 World Risk Index report.

      `Risk Level`      - descriptive value of the 2020 WRI of each countries.

      `2020`            - 2020 World Risk Index. WRI is equal to Exposure times Vulnerability.

      `Exposure`        - 2020 Exposure Risk Index.

      `Vulnerability`   - 2020 Vulnerability Risk Index. It is the mean of scores in `Susceptibility`, `Lack of Coping Capacities` and  `Lack of Adaptive Capacities`.

      It also contains the WRI for `2019`, `2018`,`2017` and `2016`.
