![](https://github.com/jsacoba/pai789_finalproject/blob/main/aes-folder/joined_maps.png)


# Results and Analysis



## Data Distribution


## Results and Analysis

### 1. Is there a relationship between EPI and WRI? If there is, are they positively or negatively correlated?;

Yes. Based on the OLS Regression Results below, EPI and WRI are negatively correlated with a correlation coefficient of -0.477. This suggests that on the average, a 1 point increase in EPI is associated with a decrease in WRI by 0.1826 points. Moreover, the coefficient of EPI is significant at 97.5% confidence level. This means that a country's performance in addressing environmental sustainability issues is associated with its risk of becoming a victim of an extreme natural event (disaster). Finally, the results show that around 22.8% of variation in WRI is explained by the EPI. 

###  2. What does EPI tell about the exposure and vulnerability of countries to natural disasters?

Because WRI is a function of the inherent risk (exposure) brought by physical hazards given the geographic location of a country and its societal framework and structural characteristics (vulnerability), we extend our analysis to determine and dissect which of these WRI components is correlated with EPI.

![](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/a.epi_wri/ols_epi_expo_vul.png)

The results whow that EPI is negatively correlated to both exposure and vulnerability with EPI coefficients that are both significant at 5% level. Interestingly, regression shows that EPI has a stronger correlation with vulnerability with r = -0.892 than that of exposure with r = -0.188. Although this does not support a causal relationship, the model seem to suggest that addressing environmental sustainability issues cannot do much on the risk of exposure since it is a function of inherent risk brought by the geographical location of countries.

![](https://github.com/jsacoba/pai789_finalproject/blob/main/aes-folder/points_ols.png)

To support this analysis, first we take the case of countries that were rated with the same risk exposure index. Both the United States of America (Global West) and Afghanistan (Southern Asia) were rated 12.99 in terms of exposure but with vulnerability rating of 66.93 and 30.06, repectively, their WRI has a large gap of 4.79. The same case is through with Spain (Global West) and Pakistan (Southern Asia). Relative thereto, we also note the large disparity between their EPI scores. 

![](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/e.%20analysis_tables/risk_region.png)















3. What does the location and economic development status tell about their WRI and EPI?

