import pandas as pd

dfPaises = pd.read_csv('ch5/paises.csv', delimiter=';')
dfPaises['Country'] = dfPaises['Country'].str.strip()
dfPaises['Region'] = dfPaises['Region'].str.strip()

idx = dfPaises['Population'].idxmax()
print(dfPaises.loc[idx, ['Country', 'Region']])
