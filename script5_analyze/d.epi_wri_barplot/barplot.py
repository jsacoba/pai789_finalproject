import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

barplot = pd.read_csv('plots_data.csv')
bot = barplot.nsmallest(10, ['2020'])

bot = pd.melt(bot, id_vars=['iso3'], value_vars=['2020','EPI.new'], var_name='Indices')
fig,ax = plt.subplots()
sns.set_color_codes("pastel")
sns.barplot(x="iso3", y="value", data=bot, palette='pastel')
#%%


sns.set_color_codes("pastel")
sns.barplot(x="2020", y="Country", data=top, label="Budget 2019")

sns.despine(left=True, bottom=True)

plt.tight_layout()
plt.show()
#%%

top = barplot.nlargest(10, ['2020'])
ends_wri = pd.concat([bot, top]).sort_index()


#%%


plt.figure(figsize=(100,100))
plt.xticks(rotation=90)
sns.set(style="darkgrid")

fig,ax = plt.subplots()
sns.set_color_codes("pastel")
sns.barplot(x=["Country"], y="Country", data=ends_wri, palette='pastel')
#%%

#ax = sns.barplot(x="budget2018", y="ministere", data=budget, label="Total")
sns.set_color_codes("pastel")
sns.barplot(x="2020", y="Country", data=barplot, label="Budget 2019")

sns.despine(left=True, bottom=True)

plt.tight_layout()
plt.show()




#%%

top = barplot.sort_values(by=['2020']).head(10)
#%%
top = [barplot['2020'].sort_values('2020')['Country'].head(10)
#%%
nlargest = barplot.groupby('2020')['EPI.new'].nlargest(2).reset_index()['level_1'].values
nsmallest = barplot.groupby('2020')['EPI.new'].nsmallest(2).reset_index()['level_1'].values

result = pd.concat([barplot.iloc[nlargest], barplot.iloc[nsmallest]]).sort_index()
print(result)
#%%
plt.figure(figsize=(100,100))


bar_panel = pd.melt(barplot , id_vars=['Country'], value_vars=['2020','EPI.new'], var_name='Indices')

plt.figure(figsize=(50,100))
plt.xticks(rotation=90)
sns.set(style="darkgrid")

fig,ax = plt.subplots()
sns.set_color_codes("pastel")
sns.barplot(x="Country", y="value", hue="Indices", data=bar_panel, palette='pastel')
#%%

#ax = sns.barplot(x="budget2018", y="ministere", data=budget, label="Total")
sns.set_color_codes("pastel")
sns.barplot(x="2020", y="Country", data=barplot, label="Budget 2019")

sns.despine(left=True, bottom=True)

plt.tight_layout()
plt.show()

