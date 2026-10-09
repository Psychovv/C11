import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfSpace = pd.read_csv('space.csv', delimiter=',')
dfSpace['Cost'] = pd.to_numeric(dfSpace['Cost'].astype(str).str.replace(',', ''), errors='coerce')
dfSpace = dfSpace[dfSpace['Cost'] > 0]
sns.boxplot(data=dfSpace, x='StatusRocket', y='Cost')
plt.show()
