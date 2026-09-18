import pandas as pd

dfPaises = pd.read_csv('ch5/paises.csv', delimiter=';')
dfPaises['Country'] = dfPaises['Country'].str.strip()
dfPaises['Region'] = dfPaises['Region'].str.strip()

noCoast = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]
noCoast.to_csv('ch5/noCoast.csv', sep=';', index=False)
print(noCoast['Country'])
