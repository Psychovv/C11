import pandas as pd

dfPaises = pd.read_csv('ch5/paises.csv', delimiter=';')
dfPaises['Country'] = dfPaises['Country'].str.strip()
dfPaises['Region'] = dfPaises['Region'].str.strip()

print(dfPaises.groupby('Region')['Literacy (%)'].mean())
