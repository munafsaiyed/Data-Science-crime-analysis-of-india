import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = pd.read_csv("project_file.csv")

sb.pairplot(df)
plt.savefig("pairplot")
plt.show()
