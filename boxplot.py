import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv('project_file.csv')
boxprops = dict(linestyle='-', linewidth=4, color='blue')
medianprops = dict(linestyle='-', linewidth=4, color='red')
plt.boxplot([df['murder'],df["rape"],df["robbery"]],
                showfliers=False, showmeans=True,
                boxprops=boxprops,
                medianprops=medianprops)
plt.title("BoxPlot")
plt.xticks([1, 2, 3], ['Murder', 'Rape', 'Robbery'])
plt.xlabel("Types Of Crimes")
plt.ylabel("Crimes Count Under IPC")
plt.show()

