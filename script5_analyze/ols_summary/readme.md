# ***Script No. 5.1: Analyzing and Visualizing the WRI Distribution***

## A. Summary

This script uses `pandas`,  and `statsmodels.api` modules of `Python`. The script is aimed at generating OLS regression results for various dependent and independent variables from the master file.

## B. Input Data

There is only one input data in this script, which is the master file ***combine_clean.csv*** we generated in `script4_combine` folder. 

## C. Deliverables

1. Script named ***ols.py***; and

2. Output file with name ***ols_summary_epi_exposure.txt***, ***ols_summary_epi_vulnerability.txt***, and ***ols_summary_epi_wri.txt***.

## D. Instructions

1. Import `pandas` as `pd`, and `statsmodels.api` as `sm`.

2. Read the input file by assigning `analyze` to the result of calling `pd.read_csv()` with the file `'combined_clean.csv'`.

3. Let us test the correlation of EPI and WRI. Print a descritpive message, then call the `.corr()` function to the `['2020']` column of `analyze` with the argument `corr(plots_data['EPI.new']`, then round the result to 3 decimal places. This will show the correlation coefficient.

4. Then, test the correlation of EPI and Exposure. Print a descritpive message, then call the `.corr()` function to the `['Exposure']` column of `analyze` with the argument `corr(plots_data['EPI.new']`, then round the result to 3 decimal places. 

5. Finally, test the correlation of EPI and Vulnerability. Print a descritpive message, then call the `.corr()` function to the `['Vulnerability']` column of `analyze` with the argument `corr(plots_data['EPI.new']`, then round the result to 3 decimal places. 


6. Now we regress WRI and EPI. Start by defining the dependent variable by assigning `y` to to the `['2020']` column of `analyze`.

7. Then define independent variable by assigning `x` to to the `['EPI.new']` column of `analyze`.

8. Add constant to independent variable by assigning `x` to the result of calling `sm.add_constant(x)`.

9. Fit a linear regression model by assigning `model` to `sm.OLS(y, x).fit(cov_type='HC1')`

10. Print model summary by calling `.summary()` to `model`.

11. Save regression results as text file using the following syntax:

        `with open('ols_summary_epi_wri.txt', 'w') as fh:
            fh.write(model.summary().as_text())`

12. Do the same steps from 6 to 11 to regress `EPI` and `Exposure`. Be sure to use the correct variable `Exposure` in place of the `2020` column of `analyze`. Save the regression results as text file as `ols_summary_epi_exposure.txt`.

13. As in number 12, do the same to regress `EPI.new` and ` Vulnerability`. Be sure to use the correct variable `Vulnerability` in place of the `2020` column of `analyze`. Save the regression results as text file as `ols_summary_epi_vulnerability.txt`.