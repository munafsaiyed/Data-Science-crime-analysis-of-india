import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = pd.read_csv("project_file.csv")
cor_df=df.corr()
plt.xticks(rotation=60)
plt.yticks(rotation=360)
sb.heatmap(cor_df,annot=True,linewidths=.5)
plt.show()


