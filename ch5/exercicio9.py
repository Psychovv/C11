import pandas as pd

dfPaises = pd.read_csv('ch5/paises.csv', delimiter=';')
dfPaises['Country'] = dfPaises['Country'].str.strip()
dfPaises['Region'] = dfPaises['Region'].str.strip()

oceania = dfPaises[dfPaises['Region'].str.contains('OCEANIA')]
print(oceania['Country'])
print(len(oceania))
