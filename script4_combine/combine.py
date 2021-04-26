# Import pandas

import pandas as pd

# Open files.

wri = pd.read_csv('wri16to20_clean.csv')
epi = pd.read_csv('epi_clean.csv')
weo = pd.read_csv('weo_data_clean.csv')

# Print initial number of records.

print('\nNumber of Records (wri):', len(wri))
print('Number of Records (epi):', len(epi))
print('Number of Records (weo):', len(weo))

# Merge 'wri' and 'epi'.

indices = wri.merge(epi, on='iso3', how='inner', validate='1:1', indicator=True)

# Drop `"_merge"` from `index`.

indices = indices.drop("_merge", axis="columns")

# Rearrange "region" column's position (as third column). 

pos_region = "region"
third_col = indices.pop(pos_region)
indices.insert(2, pos_region, third_col)

# Merge 'indices' to 'weo'.

indices_econ = indices.merge(weo, on='iso3', how='inner', validate='1:1', indicator=True)

# Drop '"Country_y"' and '"_merge"' columns.

indices_econ = indices_econ.drop("Country_y", axis="columns")
indices_econ = indices_econ.drop("_merge", axis="columns")

# Print number of dropped records from joining the three data sets.

print('\nDropped Records:', len(epi)-len(indices_econ))
                                                                                
# Set index to 'iso'.

indices_econ.set_index('iso3', inplace = True)

# Save file.

indices_econ.to_csv('combined_clean.csv')



