![](https://github.com/jsacoba/pai789_finalproject/blob/main/script6_mapping/joined_maps.png)

# Results and Analysis

## 1. Performance in environmental sustainability management is negatively correlated with the risk of natural disaster.

Results show that a country's performance in addressing environmental sustainability issues is associated with its risk of becoming a victim of an extreme natural event (disaster). Based from the OLS regression, EPI and WRI are negatively correlated with a correlation coefficient of -0.477. This suggests that on the average, a one-point increase in EPI is associated with a decrease in WRI by 0.1826 points. With a p-value close to zero, the coefficient of EPI is significant at 5% level [and even at 1% level]. Finally, the results show that around 22.8% of variation in WRI is explained by EPI. 

## 2. EPI has a stronger correlation with a country's risk vulnerability than its exposure.

Because WRI is a function of the inherent risk (exposure) brought by physical hazards given the geographic location of a country and its societal framework and structural characteristics (vulnerability), we extend our analysis to determine and dissect which of these WRI components is correlated with EPI.

![OLS Exposure and Vulnerability](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/to_RESULTS.MD/ols.pngg)
Figure 1. OLS Regression Results: EPI vs. Exposure and Vulnerability


The results show that EPI is negatively correlated to both exposure and vulnerability with EPI coefficients that are both significant at 5% level. Interestingly, OLS regression shows that EPI has a stronger correlation with vulnerability with r = -0.892 than that of exposure with r = -0.188. Although this does not support a causal relationship, the model seem to suggest that addressing environmental sustainability issues cannot do much on risk exposure since it is a function of inherent physical hazard brought by the geographical location of countries. 

![Combined Scatter Plots](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/to_RESULTS.MD/combined_scatter_region.png)
Figure No. 2. a.) WRI Distribution, b.) WRI per Economic Region, and c.) EPI vs. WRI per Economic Region

To support this analysis, first we take the case of countries that were rated with the same risk exposure index. Both the United States of America (Global West) and Afghanistan (Southern Asia) were rated 12.99 in terms of exposure but with vulnerability rating of 66.93 and 30.06, repectively, their WRI registered a large gap of 4.79. The same case holds true for Spain (Global West) and Pakistan (Southern Asia). Relative thereto, we also note the large disparity between their EPI scores. The United States has an EPI of 69.3 while Afghanistan was rated 25.5. Thus, nothwithstanding equal footing on risk exposure, we can conclude that better environmental management performance is associated with lower risk vulnerability, and lower disaster risk (WRI).

![Countries with Same Risk Exposure](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/points_ols.png)

Second, let us take the case of advanced economies or the G7 countries namely, Japan, Italy, United States of America, United Kingdom, Canada, Germany, and France with summative information shown below:

![](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/japan_highlight.png)


As observed from the table above, G7 countries performed well in environmental sustainability and management as evidenced by their high EPIs. Interestingly, while the 6 of them have on the average kept their WRI low, Japan did not. Dissecting the components of WRI would suggest that while Japan have maintained its risk vulnerability low, its being geographically located in Asia Pacific where most typhoons are formed and active volcanoes (destrcutive earthquakes) are located, it tallied the highest WRI of 38.67 among these major advanced economies.

![Japan Outlier](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/epi_wri_status.png)

## 3. Advanced economies performs better in addressing environmental sustainability issues, hence with lower risk of natural disaster.

Let us take another dimesnion of analysis by taking into account the economic development status of countries. The table below contains information about the ten poorest and and ten riches countries based on their GDP per capita in 2020.

![Rich and Poor Countries](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/points_rich.png)

It can be gleaned from the table above that richer countries have higher EPIs. This suggests that higher capacity to support environmental sustainability by investing in societal institutions, structures and management (coping and adaptive capacities), can potentially  lower vulnerability risk, hence a lower risk of natural disaster.