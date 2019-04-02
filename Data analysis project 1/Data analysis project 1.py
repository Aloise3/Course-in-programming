import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import re
import statsmodels.formula.api as sm



#Indlæs datasæt. Husk at opdatere stien når du skifter mellem computere.
df = pd.read_excel(r"C:\Course-in-programming\Data analysis project 1\datasætudvidele21.xlsx")

df.head()

#We see in the head that there is a lot of missing data for Aruba. If we delve deeper into the dataset we will find that this is also the case for many other countries in the 20th century. 
#Before handling this issue: Our dummy variables for different regions of the world are placed in year 2005. We want to relocate these variables


#We're focusing on the last 5 years of data. Most countries are covered and we don't have to constantly be aware that a financial crisis happened, even though the world was still in aftermath
#Dropping 1950-2010 due to inconsistent data on majority of the variables
indexNames = df[ (df['year'] >= 1950) & (df['year'] <= 2009) ].index   
reduced_df = df
reduced_df.drop(indexNames , inplace=True)

print(reduced_df)

#Renaming the variables
reduced_df.rename(columns={'gdppc':'GDPPerCapita'}, inplace=True)
reduced_df.rename(columns={'csh_i':'Investment'}, inplace=True)
reduced_df.rename(columns={'popgr':'PopulationGrowth'}, inplace=True)
reduced_df.rename(columns={'csh_g':'GovernmentExpenditure'}, inplace=True)
reduced_df.rename(columns={'gdpgr':'GDPGrowth'}, inplace=True)
reduced_df.rename(columns={'tradeqog':'Trade'}, inplace=True)
reduced_df.rename(columns={'pl_i':'PPI'}, inplace=True)
#Calculating means for 2010-2014
means = reduced_df.groupby('country')['GDPPerCapita', 'PopulationGrowth', 'Investment', 'GovernmentExpenditure', 'PPI', 'GDPGrowth', 'pri', 'sec', 'Trade', 'GovernmentEffectiveness', 'PoliticalStability'].mean()
#Dropping countries with empty variables
means = means.dropna(axis=0)
means.head()

#Send to excel so I can verify that there was no screwups
means.to_excel("2010-2014.xlsx")

#Adding empty column to reshape PoliticalStability into a dummy
#The scale goes from -2.5 to 2.5 by definition. 
bins_pol = [-2.5, 0.5,  2.5]
group_names_pol = [0, 1]
means['PolStabInd'] = pd.cut(means['PoliticalStability'], bins_pol, labels=group_names_pol)
print(means)
sns.jointplot(x="PoliticalStability", y="Investment", data=means)
plt.show()
sns.jointplot(x="PoliticalStability", y="sec", data=means)
plt.show()
sns.jointplot(x="GovernmentEffectiveness", y="Investment", data=means)
plt.show()
sns.jointplot(x="GovernmentEffectiveness", y="sec", data=means)
plt.show()
#Scatter
plt.scatter('Investment', 'PopulationGrowth', data = means)
plt.show()

#Pairplot
sns.pairplot(means[['PopulationGrowth', 'Investment', 'sec', 'GDPGrowth']], dropna=True)
plt.show()

#Correlation Matrix
plt.title("Figure 2: Correlation of growth factors")
corr = means[['GDPPerCapita', 'PopulationGrowth', 'Investment', 'sec', 'pri', 'GDPGrowth', 'PoliticalStability']].corr()
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, annot=True, fmt='.2f')
plt.show()

#OLS
result_basic = sm.ols(formula="GDPGrowth ~ GovernmentExpenditure + Investment + sec ", data=means).fit()
print(result_basic.summary())

result_basic = sm.ols(formula="GDPGrowth ~  Investment + sec + PoliticalStability + GovernmentExpenditure", data=means).fit()
print(result_basic.summary())

#Dropping Oil countries
means_without_oil = means.drop(['Algeria', 'Indonesia', 'Iran', 'Iraq', 'Kuwait', 'Venezuela', 'Ecuador', 'Congo, D.R.'])
#Gabon, Nigeria, Oman and Saudi Arabia are already dropped
#OLS
result_basic_without_oil = sm.ols(formula="GDPGrowth ~  Investment + sec + PoliticalStability + GovernmentExpenditure", data=means_without_oil).fit()
print(result_basic_without_oil.summary())

result_basic_without_oil = sm.ols(formula="GDPGrowth ~  Investment + sec + PoliticalStability + GovernmentExpenditure", data=means_without_oil).fit()
print(result_basic_without_oil.summary())