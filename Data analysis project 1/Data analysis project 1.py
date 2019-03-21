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

#Indlæs datasæt. Husk at opdatere stien når du skifter mellem computere.
df = pd.read_excel(r"https://github.com/Aloise3/Course-in-programming/blob/master/Data%20analysis%20project%201/datas%C3%A6tudvidele21.xlsx")
print(df)

#Dropper 1950-1958 pga datamangel
indexNames = df[ (df['year'] >= 1950) & (df['year'] <= 2010) ].index   
df.drop(indexNames , inplace=True)
pd.__version__
print(df)
print(type(df))

#Grouping
#data_by_year = df.groupby('country')
#print(type(data_by_year))

#data_by_year.groups

#for key, value in data_by_year: 
#    print('Groupname: ', key)
#    print(value)
#    print('-----------------------------------------------')

#Konverter til cross sectional data
table = pivot_table(df, index=['country',,'rgdpe','popgr', 'csh_i', 'csh_g', 'pl_i', \
'rdgpnapc', 'grna', 'gdpgro', 'ppidevgammel', 'pri', 'sec', 'etnony', 'gdpgr', 'gdppc', 'gdpgrwb', 'gdpwb90', 'gdppcwb05', 'tradeqog', 'MENA', 'SSAF', 'LAC', 'WEOFF', 'EECA', 'SEAS', \
'ppidevny', 'laam', 'safrica', 'CorruptionPerception', 'PoliticalCorruptionindex', 'ControlofCorruption', \
'GovernmentEffectiveness', 'PoliticalStability', 'RuleofLaw', 'RegulatoryQuality'], columns = ['year'])




#Dropper missing values
#dataset.dropna(inplace=True)




