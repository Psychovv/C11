import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfPaises = pd.read_csv('paises.csv', delimiter=',')
sns.regplot(data=dfPaises, x='Literacy (%)', y='Infant mortality (per 1000 births)', line_kws={'color':'red'})
plt.show()
