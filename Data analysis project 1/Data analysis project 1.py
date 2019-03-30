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

#Dropper 1950-1958 pga datamangel
indexNames = df[ (df['year'] >= 1950) & (df['year'] <= 2009) ].index   
df.drop(indexNames , inplace=True)
pd.__version__
print(df)
print(type(df))
#Dropping irrelevant variables
df.drop(columns=['MENA','SSAF',	'LAC','WEOFF','EECA','SEAS','ppidevny', 'ppidevgammel',	'laam',	'safrica'])



#Long to wide. Not needed as I found out I could take a mean as listed below.
            #df_wide = df.pivot('country', 'year')
            #print(df_wide)
            
#Calculating means for 2010-2014
means = df.groupby('country')['rgdpe','popgr', 'csh_i', 'csh_g', 'pl_i', 'gdpgr', 'pri', 'sec', 'gdpgr', 'gdppc', 'tradeqog', 'CorruptionPerception', 'Political Corruption index', 'Control of Corruption', 'GovernmentEffectiveness', 'PoliticalStability', 'RuleofLaw', 'RegulatoryQuality'].mean()
print(means)
#Send to excel so I can verify that there was no screwups
means.to_excel("Wide_2010-2014.xlsx")


#MAKE SCATTER PLOTS
sns.pairplot(means[['rgdpe', 'popgr', 'csh_i', 'sec', 'gdpgr']])
plt.show()

#Correlation Matrix
corr = means[['rgdpe', 'popgr', 'csh_i', 'sec', 'pri', 'gdpgr']].corr()
#corr.style.background_gradient(cmap='coolwarm').set_precision(2)
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, annot=True, fmt='.2f')
#sns.heatmap(corr, vmin=corr.values.min(), vmax=1, square=True, linewidths=0.1, annot=True, annot_kws={"size":8}, fmt='.2f')
plt.show()

#OLS
result_basic = sm.ols(formula="gdpgr ~ rgdpe + csh_g+ csh_i + pri+ sec + pl_i + popgr ", data=means).fit()
print(result_basic.summary())

result_investment = sm.ols(formula = "csh_i ~ rgdpe + sec + popgr + csh_g", data=means).fit()
print(result_investment.summary())





