# Import 'pandas' module.

import pandas as pd

# Read input file.

analyze = pd.read_csv('combined_clean.csv')

# ***A. Extracting countries with the same Risk Exposure Index.***

# Create column 'dup' in 'analyze' to select duplicates in 'Exposure' column.

analyze['dup'] = analyze.Exposure.duplicated(keep=False) & analyze.Exposure.notna()

# Create new data frame for the selected countries with the same risk exposure.

same_exposure = analyze[analyze['dup'] == True]

# Save results.

same_exposure.to_csv('same_exposure.csv')


# ***B. Extracting major advanced economies.***

# Create new data frame for the major advanced economies.

advanced = analyze[analyze['Economic Development Status'] == 'Major Advanced Economy']

# Save results.

advanced.to_csv('advanced.csv')


# ***C. Select top 10 riches and top 10 poorest countries based on GDP.***

rich = analyze.nlargest(10, ['GDP'])
poor = analyze.nsmallest(10, ['GDP'])

# Concatenate data for the selected rich and poor countries.

extremes = pd.concat([rich, poor], axis = 0)

# Save results.

extremes.to_csv('extremes.csv')
