
import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sb
#import squarify as sq
from collections import Counter
from matplotlib import cm as cm

df = pd.read_csv("project_file.csv")
#sb.pairplot(df)
country=df.groupby(['LoanAmount'])[['Gender']].sum()
#sb.distplot(country)
cor_df=df.corr()
sb.heatmap(cor_df,annot=True,linewidths=.5)
plt.xticks(rotation=60)
plt.yticks(rotation=360)
plt.show()
##C:\Users\Dell\AppData\Local\Programs\Python\Python37-32\Scripts
