import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import re
import statsmodels.formula.api as sm



#Indlæs datasæt. Husk at opdatere stien når du skifter mellem computere.
df = pd.read_excel(r"C:\Course-in-programming\Data analysis project 1\datasætudvidele21.xlsx")
print(df)

df.head()

#We see in the head that there is a lot of missing data for Aruba. If we delve deeper into the dataset we will find that this is also the case for many other countries in the 20th century. 
#Before handling this issue: Our dummy variables for different regions of the world are placed in year 2005. We want to relocate these variables


#We're focusing on the last 5 years of data. Most countries are covered and we don't have to constantly be aware that a financial crisis happened, even though the world was still in aftermath
#Dropping 1950-2010 due to inconsistent data on majority of the variables
indexNames = df[ (df['year'] >= 1950) & (df['year'] <= 2000) ].index   
reduced_df = df
reduced_df.drop(indexNames , inplace=True)

print(reduced_df)
print(type(reduced_df))

            
#Calculating means for 2010-2014
means = reduced_df.groupby('country')['rgdpe','popgr', 'csh_i', 'csh_g', 'pl_i', 'gdpgr', 'pri', 'sec', 'gdppc', 'tradeqog', 'CorruptionPerception', 'Political Corruption index', 'Control of Corruption', 'GovernmentEffectiveness', 'PoliticalStability', 'RuleofLaw', 'RegulatoryQuality','MENA','SSAF','LAC','WEOFF','EECA','SEAS'].mean()
means.head()

#Send to excel so I can verify that there was no screwups
means.to_excel("Wide_2010-2014.xlsx")

#Pairplot
sns.pairplot(means[['gdppc', 'popgr', 'csh_i', 'sec', 'pri', 'gdpgr']], dropna=True)
plt.show()

#Correlation Matrix
plt.title("Figure 2: Correlation of growth factors")
corr = means[['gdppc', 'popgr', 'csh_i', 'sec', 'pri', 'gdpgr']].corr()
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, annot=True, fmt='.2f')
plt.show()




#OLS
result_basic = sm.ols(formula="gdpgr ~ rgdpe + csh_g+ csh_i + pri+ sec + pl_i + popgr ", data=means).fit()
print(result_basic.summary())

result_investment = sm.ols(formula = "csh_i ~ rgdpe + sec + popgr + csh_g", data=means).fit()
print(result_investment.summary())





