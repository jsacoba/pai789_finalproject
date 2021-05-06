
![](https://github.com/jsacoba/pai789_finalproject/blob/main/aes-folder/joined_maps.png)

# Linking Disaster Risk and Environmental Sustainability
## Background

### The World Risk Index

In 2020, the Bündnis Entwicklung Hilft, in collaboration with Ruhr University Bochum – Institute for International Law of Peace and Armed Conflict (IFHV), ranked 181 countries according to their risk of becoming the victim of a disaster resulting from an extreme natural event. Topping the list is the Pacific island of Vanuatu with a World Risk Index (WRI) of 49.79, while the Greatest Middle East country Qatar has the lowest risk of 0.31.

![](https://github.com/jsacoba/pai789_finalproject/blob/main/script1-wri_data/wri_components.PNG)
Figure 1. World Risk Index Components, ***The 2020 WorldRiskIndex Report***

As defined by the report, the WRI is the interaction of a country's risk exposure and vulnerability. Exposure pertains to the risk faced by various entities such as communities, resources, infrastructure, production, goods, services or ecosystems to physical hazards such as earthquakes, storms, floods, droughts, tsunamis and sea-level rise (Welle, Torsten & Birkmann, Joern, 2015).  On the other hand, vulnerability refers to the mean of the following three sub-components:

1.	Susceptibility. This pertains to societal framework conditions and structural characteristics that indicates the likelihood of suffering from harm in an extreme natural event.

2.	Coping. This pertains to various societal capacities to minimize negative impacts of natural hazards and climate change through direct action and the resources available.

3.	Adaptation. These include measures and strategies dealing with and attempting to address the negative impacts of natural hazards and climate change in the future. Adaptation, unlike coping, is understood as a long-term process that also includes structural changes.

### The Environmental Performance Index

The 2020 Environmental Performance Index (EPI) report ranked 180 countries according to their performance in addressing sustainability issues and environmental challenges that they face. It includes 32 performance metrics under 11 issue categories. The interaction of these indicator variables are summed up in two main EPI components: environmental health and ecosystem vitality. The report puts: **"These indicators provide a gauge at a national scale of how close countries are to established environmental policy targets. The EPI offers a scorecard that highlights leaders and laggards in environmental performance and provides practical guidance for countries that aspire to move toward a sustainable future."**

![](https://github.com/jsacoba/pai789_finalproject/blob/main/script3_epi_data/epi_components.PNG)
Figure 2. Environmental Performance Index Components, ***The 2020 EPI Report***

Among the countries included in the report, Denmark was ranked first with an EPI of 82.5 while Liberia ranked last with an EPI of 22.6.

## Objectives

This analysis seeks to provide data-driven analysis of the relationship between countries' environmental sustainability performance and natural disaster risk. Specifically, this analysis is aimed at answering the following questions:

1. Is there a relationship between EPI and WRI? If there is, are they positively or negatively correlated?;

2. What does EPI tell about the exposure and vulnerability of countries to natural disasters?; and

3. What does the location and economic development status a country tell about its WRI and EPI?

## Data Handling and Processing

This project used `Python` and `QGIS 3.18` in data cleaning, processing, and visualization. For the detailed `Python` codes and `QGIS` instructions, refer to each of the numbered folders in the main branch of this repository.

## Results and Analysis

### 1. Performance in environmental sustainability management is negatively correlated with the risk of natural disaster.

The results show that a country's performance in addressing environmental sustainability issues is associated with its risk of becoming a victim of an extreme natural event (disaster). Linear regression suggests that EPI and WRI are negatively correlated with a correlation coefficient of -0.477. This suggests that on the average, a one-point increase in EPI is associated with a decrease in WRI by 0.1826 points. With a p-value close to zero, the coefficient of EPI is significant at 5% level [and even at 1% level]. Finally, the results show that around 22.8% of variation in WRI is explained by EPI.

![corr EPI vs WRI](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/to_RESULTS.MD/EPI%20vs%20WRI%20corr.PNG)

### 2. EPI has a stronger correlation with a country's risk vulnerability than its exposure.

Because WRI is a function of the inherent risk (exposure) brought by physical hazards given the geographic location of a country and its societal framework and structural characteristics (vulnerability), we extend our analysis to determine and dissect which of these WRI components is correlated with EPI.

![OLS Exposure and Vulnerability](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/to_RESULTS.MD/ols.png)
Figure 3. OLS Regression Results: EPI vs. Exposure and Vulnerability

The results show that EPI is negatively correlated to both exposure and vulnerability with EPI coefficients that are both significant at 5% level. Interestingly, OLS regression shows that EPI has a stronger correlation with vulnerability with r = -0.892 than that of exposure with r = -0.188. Although this does not support a causal relationship, the model seem to suggest that addressing environmental sustainability issues cannot do much on risk exposure since it is a function of inherent physical hazard brought by the geographical location of countries. 

![Combined Scatter Plots](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/to_RESULTS.MD/combined_scatter_region.png)
Figure 4. a and b) WRI per Ecoomic Region, and c.) EPI vs. WRI per Economic Region

To support this analysis, first we take the case of countries that were rated with the same risk exposure index. Both the United States of America (Global West) and Afghanistan (Southern Asia) were rated 12.99 in terms of exposure but with vulnerability rating of 66.93 and 30.06, repectively, their WRI registered a large gap of 4.79. The same case holds true for Spain (Global West) and Pakistan (Southern Asia). Relative thereto, we also note the large disparity between their EPI scores. The United States has an EPI of 69.3 while Afghanistan was rated 25.5. Thus, nothwithstanding equal footing on risk exposure, we can conclude that better environmental management performance is associated with lower risk vulnerability, and lower disaster risk (WRI).

![Countries with Same Risk Exposure](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/to_RESULTS.MD/points_ols.png)
Table 1. Countries with Same Exposure Risk Index

Second, let us take the case of advanced economies or the G7 countries namely, Japan, Italy, United States of America, United Kingdom, Canada, Germany, and France with summative information shown below:

![G7 Countries](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/to_RESULTS.MD/japan_highlight.png)
Table 2. Major Advanced Economies

As observed from the table above, G7 countries performed well in environmental sustainability and management as evidenced by their high EPIs. Interestingly, while the 6 of them have on the average kept their WRI low, Japan did not. Dissecting the components of WRI would suggest that while Japan have maintained its risk vulnerability low, its being geographically located in Asia Pacific where most typhoons are formed and active volcanoes (destructive earthquakes) are located, it tallied the highest WRI of 38.67 among these major advanced economies.

![Japan Outlier](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/to_RESULTS.MD/japan_scatter.png)
Figure 5. EPI vs. WRI per Economic Region

### 3. Advanced economies perform better in addressing environmental sustainability issues, hence with lower risk of natural disaster.

Let us take another dimesnion of analysis by taking into account the economic development status of countries. The table below contains information about the ten poorest and and ten riches countries based on their GDP per capita in 2020.

![Rich and Poor Countries](https://github.com/jsacoba/pai789_finalproject/blob/main/script5_analyze/to_RESULTS.MD/points_rich.png)
Table 3. Top 10 Poorest and Richest Countries According to GDP per capita

It can be gleaned from the table above that richer countries have higher EPIs. This suggests that higher capacity to support environmental sustainability by investing in societal institutions, structures and management (coping and adaptive capacities), can potentially  lower vulnerability risk, hence a lower risk of natural disaster. 

We can also run an analysis that counters this relationship as it could also be the case that countries with less exposure risk [hence, lowe WRI], makes them better off economically. Hence, they have better ability to address environmental sustainability issues that further lowers their risk of disaster.

## Policy Significance

The result of this analysis backs up the call and need for countries around the world to strive in scaling up environmental sustainability management in order to lessen the adverse impact of natural disasters. 

## References

1. World Risk Report 2020. Bündnis Entwicklung Hilft, Ruhr University Bochum – Institute for International Law of Peace and Conflict 2020. 

2. Welle, Torsten & Birkmann, Joern. (2015). The World Risk Index – An Approach to Assess Risk and Vulnerability on a Global Scale. Journal of Extreme Events. Volume 2. 10.1142/S2345737615500025. 

3. Wendling, Z. A., Emerson, J. W., de Sherbinin, A., Esty, D. C., et al. (2020). 2020 Environmental Performance Index. New Haven, CT: Yale Center for Environmental Law & Policy. epi.yale.edu