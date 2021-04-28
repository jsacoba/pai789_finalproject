import pandas as pd

# Read input file.

analyze = pd.read_csv('combined_clean.csv')

analyze['dup'] = analyze.Exposure.duplicated(keep=False) & analyze.Exposure.notna()

dup_risk = analyze[analyze['dup'] == True]

dup_risk.to_csv('same_exposure.csv')

advanced = analyze[analyze['Economic Development Status'] == 'Major Advanced Economy']

rich = analyze.nlargest(10, ['GDP'])

poor = analyze.nsmallest(10, ['GDP'])

extremes = pd.concat([rich, poor], axis = 0)
                   