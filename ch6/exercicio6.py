import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfPaises = pd.read_csv('paises.csv', delimiter=',')
df_filtered = dfPaises[(dfPaises['Region'].str.strip() == 'LATIN AMER. & CARIB') | (dfPaises['Region'].str.strip() == 'WESTERN EUROPE')]
sns.boxplot(data=df_filtered, x='Region', y='GDP ($ per capita)')
plt.show()
