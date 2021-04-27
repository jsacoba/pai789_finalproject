# Import modules.

import pandas as pd
import numpy as np

# Read the 'wri' files using 'pd.read_csv'.

wri_raw20 = pd.read_csv('wri2020_raw.csv', encoding='cp1252')
wri_raw19 = pd.read_csv('wri2019_raw.csv', encoding='cp1252')
wri_raw18 = pd.read_csv('wri2018_raw.csv', encoding='cp1252')
wri_raw17 = pd.read_csv('wri2017_raw.csv', encoding='cp1252')
wri_raw16 = pd.read_csv('wri2016_raw.csv', encoding='cp1252')

# Drop some columns.

wri20 = wri_raw20.drop(["Rank"], axis = "columns")
wri19 = wri_raw19.drop(["Rank", "Exposure", "Vulnerability", "Susceptibility", 
                       "Lack of Coping Capacities", "Lack of Adaptive Capacities"], axis = "columns")
wri18 = wri_raw18.drop(["Rank", "Exposure", "Vulnerability", "Susceptibility", 
                      "Lack of Coping Capacities", "Lack of Adaptive Capacities"], axis = "columns")
wri17 = wri_raw17.drop(["Rank", "Exposure", "Vulnerability", "Susceptibility", 
                        "Lack of Coping Capacities", "Lack of Adaptive Capacities"], axis = "columns")
wri16 = wri_raw16.drop(["Rank", "Exposure", "Vulnerability", "Susceptibility", 
                      "Lack of Coping Capacities", "Lack of Adaptive Capacities"], axis = "columns")

# Read mapping files.

map_alpha16 = pd.read_csv('iso16_map.csv', encoding='cp1252')
map_alpha17 = pd.read_csv('iso17_map.csv', encoding='cp1252')
map_alpha18 = pd.read_csv('iso18_map.csv', encoding='cp1252')
map_alpha19 = pd.read_csv('iso19_map.csv', encoding='cp1252')
map_alpha20 = pd.read_csv('iso20_map.csv', encoding='cp1252')

# Map the ISO 3 letter alpha code to each 'wri' file to standardize ID for 
# joining the World Risk Index data from 2016 to 2020. 

wri20 = wri20.merge(map_alpha20, on='Country', how='left')
wri19 = wri19.merge(map_alpha19, on='Country', how='left')
wri18 = wri18.merge(map_alpha18, on='Country', how='left')
wri17 = wri17.merge(map_alpha17, on='Country', how='left')
wri16 = wri16.merge(map_alpha16, on='Country', how='left')

# Rename 'WorldRiskIndex' column.

wri20.rename(columns={'WorldRiskIndex' : '2020'}, inplace=True)
wri19.rename(columns={'WorldRiskIndex' : '2019'}, inplace=True)
wri18.rename(columns={'WorldRiskIndex' : '2018'}, inplace=True)
wri17.rename(columns={'WorldRiskIndex' : '2017'}, inplace=True)
wri16.rename(columns={'WorldRiskIndex' : '2016'}, inplace=True)

# Set the column 'iso3' as index.

wri20.set_index('iso3', inplace=True)
wri19.set_index('iso3', inplace=True)
wri18.set_index('iso3', inplace=True)
wri17.set_index('iso3', inplace=True)
wri16.set_index('iso3', inplace=True)

# Drop the 'Country' column for 2016-2019 data. 

wri19.drop(['Country'], inplace = True, axis=1)
wri18.drop(['Country'], inplace = True, axis=1)
wri17.drop(['Country'], inplace = True, axis=1)
wri16.drop(['Country'], inplace = True, axis=1)

# Count number of countries in the 2020 WRI Report.

count_20 = len(wri20)
print('\nNumber of Countries in the 2020 WRI Report:', count_20)

# Join the data from 2020 to 2016 for countries with complete records only for 5 years.

wri16_to_20 = wri20.join(wri19, how='inner').join(wri18, how='inner').join(wri17, how='inner').join(wri16, how='inner')

# Count number of countries with complete records.

count_final = len(wri16_to_20)
print('\nNumber of Countries with Complete Records (2016-2020):', count_final)
print('\nNumber of Records Dropped:', count_20 - count_final, '\n')

# Set conditions for risk description numerical scale.
          
conditions = [
    (wri16_to_20['2020'] >= 0.31) & (wri16_to_20['2020'] <= 3.29),
    (wri16_to_20['2020'] >= 3.30) & (wri16_to_20['2020'] <= 5.67),
    (wri16_to_20['2020'] >= 5.68) & (wri16_to_20['2020'] <= 7.58),
    (wri16_to_20['2020'] >= 7.59) & (wri16_to_20['2020'] <= 10.75),
    (wri16_to_20['2020'] >= 10.76) & (wri16_to_20['2020'] <= 49.74)
    ]

# Set descriptive values for each numerical scale.

values = ['Very Low', 'Low', 'Medium', 'High', 'Very High']

# Assign risk description to the 'WRI' of each countires.

wri16_to_20['Risk Level'] = np.select(conditions, values)

# Rearrange columns.

wri16_to_20 = wri16_to_20[wri16_to_20.columns[[0,11,1,2,3,4,5,6,7,8,9,10]]]

# Double check for missing values/records.

na_values = wri16_to_20[wri16_to_20.isna().any(axis=1)]
print(na_values)

# Create final mapping file.

mapping_wri = wri16_to_20.iloc[:, 0:1] 

# Save cleaned data sets.

wri16_to_20.to_csv('wri16to20_clean.csv')
mapping_wri.to_csv('mapping_wri_clean.csv')

