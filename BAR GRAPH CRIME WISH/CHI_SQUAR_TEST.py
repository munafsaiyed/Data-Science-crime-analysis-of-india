import numpy as np
import pandas as pd
import scipy.stats 

df = pd.DataFrame.from_csv('writeData.csv')
####edf.head()
##print(df)
edf=df.iloc[[0,1,2,3],df.columns.get_indexer(['rape'])]
edf1=df.iloc[[0,1,2,3],df.columns.get_indexer(['robbery'])]
edf2=df.iloc[[0,1,2,3],df.columns.get_indexer(['murder'])]
print("edf rape : \n",edf)
print("edf1 robbery : \n",edf1)
print("edf2 murder : \n",edf2)
observed=df
print(observed)
expected=scipy.stats.contingency.expected_freq(observed)
print(expected)
dof = observed.size - sum(observed.shape) + observed.ndim - 1
print(dof)
test=scipy.stats.chisquare(f_obs=observed,f_exp=expected,ddof=3)
print(test)
##Male_ratios=edf/len(edf1)
##print(Male_ratios)
##expected=Male_ratios*len(edf2)
##print(expected)
##chi_square_stat=71172.61240967
##print(chi_square_stat)
##crit=scipy.stats.chi2.ppf(q=0.95,df=3)
##print(crit)
##p_value=1-scipy.stats.chi2.cdf(x=chi_square_stat,df=3)
##print(p_value)
##test=scipy.stats.chisquare(f_obs=observed,f_exp=expected,)
##print("chi %0.4f p_value %0.4f " %test)

