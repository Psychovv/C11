import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfPaises = pd.read_csv('paises.csv', delimiter=',')
corr_paises = dfPaises[['GDP ($ per capita)', 'Literacy (%)', 'Infant mortality (per 1000 births)', 'Phones (per 1000)']].corr()
sns.heatmap(corr_paises, annot=True, fmt='.2f')
plt.show()
