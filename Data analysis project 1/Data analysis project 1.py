import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import re
sns.set_style("darkgrid")
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
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
means = df.groupby('country')['rgdpe','popgr', 'csh_i', 'csh_g', 'pl_i', 'gdpgro', 'pri', 'sec', 'etnony', 'gdpgr', 'gdppc', 'gdpgrwb', 'gdpwb90', 'gdppcwb05', 'tradeqog', 'CorruptionPerception', 'Political Corruption index', 'Control of Corruption', 'GovernmentEffectiveness', 'PoliticalStability', 'RuleofLaw', 'RegulatoryQuality'].mean()
print(means)
#Send to excel so I can verify that there was no screwups
means.to_excel("Wide_2010-2014.xlsx")

#Correlation Matrix
def plot_corr(means,size=1000):
    corr = means.corr()
    fig, ax = plt.subplots(figsize=(size, size/10))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns);
    plt.yticks(range(len(corr.columns)), corr.columns);
    plt.matshow(means.corr())
    plt.show()
plot_corr(means)
#Correlation matrix for excel
corr = means.corr('gdpgr', 'popgr', 'csh_i' )
corr.style.background_gradient(cmap='coolwarm').set_precision(2)
plt.matshow(means.corr())
plt.show()
print(corr)
corr.to_excel("Correlation Matrix")
#MAKE SCATTER PLOTS


#OLS

result_basic = sm.ols(formula="gdpgr ~ rgdpe + csh_g+ csh_i + pri+ sec + pl_i + popgr ", data=means).fit()
print(result_basic.summary())

result_investment = sm.ols(formula = "csh_i ~ rgdpe + sec + popgr + csh_g", data=means).fit()
print(result_investment.summary())





