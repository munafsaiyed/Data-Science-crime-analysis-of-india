# library & dataset

import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv('project_file11.csv')
 
# Make boxplot for one group only
grp=[df["murder"],df["rape"],df["robbery"]]
#plt.boxplot(df["murder"])

plt.boxplot(grp)
plt.title("BoxPlot")
#plt.legend(["a","b","c","d","e","f","g"])
plt.xticks([1, 2, 3], ['Murder', 'Rape', 'Robbery'])
plt.xlabel("Types Of Crimes")
plt.ylabel("Crimes Count Under IPC")
plt.show()
