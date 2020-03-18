import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("project_file.csv")
#Rape
country=df.groupby(['murder'])[['rape']].sum()
sb.distplot(country, color="r")
plt.title("Rape")
plt.show()

#Robbery
country=df.groupby(['murder'])[['robbery']].sum()
sb.distplot(country, color="y")
plt.title("Robbery")
plt.show()
