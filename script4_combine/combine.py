# 1. Import pandas

import pandas as pd

# 2. Open files.

wri = pd.read_csv('wri16to20_clean.csv')
epi = pd.read_csv('epi_clean.csv')
weo = pd.read_csv('weo_data_clean.csv')

# 3. Print initial number of records.

print('\nNumber of Records (wri):', len(wri))
print('Number of Records (epi):', len(epi))
print('Number of Records (weo):', len(weo))

# 4. Merge 'wri' and 'epi'.

indices = wri.merge(epi, on='iso3', how='inner', validate='1:1', indicator=True)

# 5. Drop `"_merge"` from `index`.

indices = indices.drop("_merge", axis="columns")

# 6. Rearrange "Economic Region" column's position (as third column). 

pos_region = "Economic Region"
third_col = indices.pop(pos_region)
indices.insert(2, pos_region, third_col)

# 7. Merge 'indices' to 'weo' data.

indices_econ = indices.merge(weo, on='iso3', how='inner', validate='1:1', indicator=True)

# 8. Drop '"_merge"' columns.

indices_econ = indices_econ.drop("_merge", axis="columns")

# 9. Print number of dropped records from joining the three data sets.

print('\nDropped Records:', len(epi)-len(indices_econ))
                                                                                
# 10. Set index to 'iso3'.

indices_econ.set_index('iso3', inplace = True)

# 11. Save file.

indices_econ.to_csv('combined_clean.csv')



