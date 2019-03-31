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

#Dropping 1950-2010 due to inconsistent data
indexNames = df[ (df['year'] >= 1950) & (df['year'] <= 2009) ].index   
reduced_df = df
reduced_df.drop(indexNames , inplace=True)

print(reduced_df)
print(type(reduced_df))
#Dropping irrelevant variables
reduced_df.drop(columns=['MENA','SSAF',	'LAC','WEOFF','EECA','SEAS','ppidevny', 'ppidevgammel',	'laam',	'safrica'])

#Long to wide. Not needed as I found out I could take a mean as listed below.
            #df_wide = df.pivot('country', 'year')
            #print(df_wide)
            
#Calculating means for 2010-2014
means = reduced_df.groupby('country')['rgdpe','popgr', 'csh_i', 'csh_g', 'pl_i', 'gdpgr', 'pri', 'sec', 'gdppc', 'tradeqog', 'CorruptionPerception', 'Political Corruption index', 'Control of Corruption', 'GovernmentEffectiveness', 'PoliticalStability', 'RuleofLaw', 'RegulatoryQuality'].mean()
print(means)
#Send to excel so I can verify that there was no screwups
means.to_excel("Wide_2010-2014.xlsx")


#MAKE SCATTER PLOTS
g1 = means['csh_i']
g2 = means['popgr']
g3 = means['gdpgr']

plot_data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("Real GDP", "Population growth", "GDP growth")
 
fig = plt.figure()
ax = fig.add_subplot(10, 10, 10, axisbg="1.0")
 
for plot_data, color, group in zip(plot_data, colors, groups):
        x, y = plot_data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
 
plt.title('Scatter')
plt.legend(loc=2)
plt.show()


#Pairplot
#sns.pairplot(means[['rgdpe', 'popgr', 'csh_i', 'sec', 'gdpgr']], dropna=True)
#plt.show()
sns.pairplot(means[['popgr', 'csh_i', 'gdpgr']], dropna=True)
plt.show()

#Correlation Matrix
plt.title("Figure 2: Correlation of growth factors")
corr = means[['rgdpe', 'popgr', 'csh_i', 'sec', 'pri', 'gdpgr']].corr()
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, annot=True, fmt='.2f')
plt.show()


#OLS
result_basic = sm.ols(formula="gdpgr ~ rgdpe + csh_g+ csh_i + pri+ sec + pl_i + popgr ", data=means).fit()
print(result_basic.summary())

result_investment = sm.ols(formula = "csh_i ~ rgdpe + sec + popgr + csh_g", data=means).fit()
print(result_investment.summary())





