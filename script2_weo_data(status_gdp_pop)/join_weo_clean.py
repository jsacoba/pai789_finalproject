# Import Pandas module.

import pandas as pd


# Read files by calling pd.read_csv function.

devstat_raw = pd.read_csv('status_raw.csv', encoding='cp1252')
gdp_raw = pd.read_csv('gdp_raw.csv', encoding='cp1252')
pop_raw = pd.read_csv('pop_raw.csv', dtype = str, encoding='cp1252')
mapping = pd.read_csv('mapping_wri_clean.csv')

# For 'gdp_raw' and 'pop_raw', read figures as float in the '"2020"' column.

gdp_raw['2020'] = gdp_raw['2020'].str.replace(',','').astype(float)
pop_raw['2020'] = pop_raw['2020'].str.replace(',','').astype(float)

# Select relevant columns from 'gdp_raw' and 'pop_raw'.

gdp_clean = gdp_raw.loc[:194,['ISO', '2020']]
pop_clean = pop_raw.loc[:192,['ISO', '2020']]

# Rename columns from 'gdp_raw' and 'pop_raw'.

gdp_clean.rename(columns = {'ISO': 'iso3', '2020': 'GDP20'}, inplace = True)
pop_clean.rename(columns = {'ISO': 'iso3', '2020': 'pop2020'}, inplace = True)

# Set 'iso3' as index.

devstat_raw.set_index('iso3', inplace=True)
pop_clean.set_index('iso3', inplace=True)
gdp_clean.set_index('iso3', inplace=True)

# Join the 3 data sets above using the 'mapping' file.

weo_data_clean = mapping.join(devstat_raw, on = 'iso3', how='inner').join(gdp_clean, on = 'iso3', how='inner').join(pop_clean, on = 'iso3', how='inner')

# Set 'iso3' as index.

weo_data_clean.set_index('iso3', inplace=True)

# Saved joined file.

weo_data_clean = weo_data_clean.to_csv('weo_data_clean.csv')






