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
dataset = pd.read_excel(r"C:\Users\Mads Chrøis\Desktop\KU\Kandidat\Introduction to Programming and Numerical Analysis\Course-in-programming\Data analysis project 1\datasætudvidele21.xlsx")

#Dropper 1950-1958 pga datamangel
indexNames = dataset[ (dataset['year'] >= 1950) & (dataset['year'] <= 1958) ].index   
dataset.drop(indexNames , inplace=True)

#Konverter til cross sectional data
#dataset.pivot_table(index=['country'], columns = ['year','rgdpe','popgr', 'csh_i', 'csh_g', 'pl_i', \
#'rdgpnapc', 'grna', 'gdpgro', 'ppidevgammel', 'pri', 'sec', 'etnony', 'gdpgr', 'gdppc', 'gdpgrwb', 'gdpwb90', 'gdppcwb05', 'tradeqog', 'MENA', 'SSAF', 'LAC', 'WEOFF', 'EECA', 'SEAS', \
#'ppidevny', 'laam', 'safrica', 'CorruptionPerception', 'PoliticalCorruptionindex', 'ControlofCorruption', \
#'GovernmentEffectiveness', 'PoliticalStability', 'RuleofLaw', 'RegulatoryQuality'])



#Dropper missing values
#dataset.dropna(inplace=True)


print(dataset)

