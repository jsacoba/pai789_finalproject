# Import Pandas module.

import pandas as pd

# Read files by calling pd.read_csv function.

devstat_raw = pd.read_csv('status_raw.csv', encoding='cp1252')
gdp_raw = pd.read_csv('gdp_raw.csv', encoding='cp1252')
pop_raw = pd.read_csv('pop_raw.csv', encoding='cp1252')

# For 'gdp_raw' and 'pop_raw', read figures as float in the '"2020"' column.

gdp_raw['2020'] = gdp_raw['2020'].str.replace(',','').astype(float)
pop_raw['2020'] = pop_raw['2020'].str.replace(',','').astype(float)

# Select relevant columns (2020 population and GDP) from 'gdp_raw' and 'pop_raw'.

gdp_clean = gdp_raw.loc[:194,['ISO', '2020']]
pop_clean = pop_raw.loc[:192,['ISO', '2020']]

# Rename 'ISO' columns to 'iso3' from 'gdp_raw' and 'pop_raw'.

gdp_clean.rename(columns = {'ISO': 'iso3', '2020': 'GDP'}, inplace = True)
pop_clean.rename(columns = {'ISO': 'iso3','2020': 'Population'}, inplace = True)
devstat_raw.rename(columns = {'status': 'Status'}, inplace = True)

# Join the 3 data sets above using the 'mapping' file.

weo_data_clean = pd.merge(devstat_raw, gdp_clean).merge(pop_clean, on = 'iso3', how='inner')

# Set 'iso3' as index.

weo_data_clean.set_index('iso3', inplace=True)

# Saved joined file.

weo_data_clean = weo_data_clean.to_csv('weo_data_clean.csv')






