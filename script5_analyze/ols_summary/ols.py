# 1. Import modules

import pandas as pd
import statsmodels.api as sm

# 2. Read input file.

analyze = pd.read_csv('combined_clean.csv')

# A. Test the Correlation: WRI and EPI.

# 3. Generate and print correlation coefficient (rounded to three decimal places).

print('\Correlation Coefficient, r (WRI vs. EPI):', 
      round(analyze['2020'].corr(analyze['EPI.new']), 3))
print('\Correlation Coefficient, r (Exposure vs. EPI):', 
      round(analyze['Exposure'].corr(analyze['EPI.new']), 3))
print('\Correlation Coefficient, r (Vulnerability vs. EPI):', 
      round(analyze['Vulnerability'].corr(analyze['EPI.new']), 3), '\n')

# A. Regress WRI and EPI.

# 4. Define dependent variable.

y = analyze['2020']

# 5. Define independent variable

x = analyze[['EPI.new']]

# 6. Add constant to independent variable.

x = sm.add_constant(x)

# 7. Fit linear regression model.

model = sm.OLS(y, x).fit(cov_type='HC1')

# 8. Print model summary.

print(model.summary())

# 9. Save regression results.

with open('ols_summary_epi_wri.txt', 'w') as fh:
          fh.write(model.summary().as_text())
          
# B. Regress Exposure and EPI. (10)
y = analyze['Exposure']

# Define independent variable

x = analyze[['EPI.new']]

# Add constant to independent variable.

x = sm.add_constant(x)

# Fit linear regression model.

model = sm.OLS(y, x).fit(cov_type='HC1')

# Print model summary.

print(model.summary())

# Save regression results.

with open('ols_summary_epi_exposure.txt', 'w') as fh:
          fh.write(model.summary().as_text())

# C. Regress Vulnerability and EPI. (11)

y = analyze['Vulnerability']

# Define independent variable

x = analyze[['EPI.new']]

# Add constant to independent variable.

x = sm.add_constant(x)

# Fit linear regression model.

model = sm.OLS(y, x).fit(cov_type='HC1')

# Print model summary.

print(model.summary())

# Save regression results.

with open('ols_summary_epi_vulnerability.txt', 'w') as fh:
          fh.write(model.summary().as_text())




