# 1. Import modules.

import pandas as pd

# 2. Read 'epi2020.csv' file.

epi_raw = pd.read_csv('epi20_raw.csv')

# 3. Count and print initial number of observations.

initial = len(epi_raw)
print('\nInitial number of records:', initial)

# 4. Select specific columns to be used in the analysis. Build a list called 'select' 
# containing  the following column names: 'iso', 'region', 'EPI.new', 'HLT.new', 
# 'AIR.new', 'H2O.new','HMT.new', 'WMG.new', 'ECO.new', 'BDH.new','ECS.new', 
# 'FSH.new', 'CCH.new', 'APE.new', 'AGR.new', and 'WRS.new'.

select = ['iso', 'region', 'EPI.new', 'HLT.new', 'AIR.new', 'H2O.new',
                              'HMT.new', 'WMG.new', 'ECO.new', 'BDH.new', 
                              'ECS.new', 'FSH.new', 'CCH.new', 'APE.new', 
                              'AGR.new', 'WRS.new']

# 5. Assign 'code' to the result of reading 'epi2020_indicators.csv' file. Then, print 'code'.

code = pd.read_csv('epi2020_indicators.csv')
print(code)

# 6. Build new data frame using selected columns.

epi_clean = epi_raw.loc[:181, select]

# 7. Rename 'iso' column to 'iso3' and 'region' colum to 'Economic Region'.

epi_clean.rename(columns={"iso": 'iso3', 'region': 'Economic Region'}, inplace=True)

# 8. Count and print number of filtered observations.

filtered = len(epi_clean)
print('\nFiltered number of records:', filtered)

# 9. Set 'iso3 as index.

epi_clean.set_index('iso3', inplace = True)

# 10. Save filtered data as 'epi_clean.csv'.

epi_clean.to_csv('epi_clean.csv')








