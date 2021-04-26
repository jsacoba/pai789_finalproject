# Import pandas as pd.

import pandas as pd

# Read input file.

combined = pd.read_csv('combined_clean.csv')

# Sort values by 'WorldRiskIndex' column.

combined = combined.sort_values(by="WRI_2020", ascending=False)

# Build a dictionary for renaming the column names.

col_names = {'Country_x': 'Country', 'status': 'Economic Status', 'region': 'Economic Region',
            'risk_desc_2020': 'Risk Description', 'WRI_2020': '2020', 'WRI_2019': 
            '2019', 'WRI_2018': '2018', 'WRI_2017': '2017', 'WRI_2016': '2016'}

# Rename the columns.

combined.rename(columns = col_names, inplace=True)

# Select data for plotting using their location. Select the columns 'iso3'(column 0), 
# 'Country'(1), 'Economic Region' (2), 'Risk Description'(3), 'Economic Status'(28), 
# '2020'(4), '2019'(10), '2018'(11), '2017'(12), '2016'(13), and 'Environmental 
# Performance Index'(14).

plots_data = combined.iloc[:,[0,1,2,3,28,4,5,6,7,8,9,10,11,12,13,14]]

# Set index to 'iso3'

plots_data.set_index('iso3', inplace = True)

# Save file.

plots_data.to_csv('plots_data.csv')





