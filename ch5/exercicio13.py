import pandas as pd

dfPaises = pd.read_csv('ch5/paises.csv', delimiter=';')
dfPaises['Country'] = dfPaises['Country'].str.strip()
dfPaises['Region'] = dfPaises['Region'].str.strip()


def humanitarian_help(deathrate):
    return 'Balanced' if deathrate < 9 else 'Urgent'


dfPaises['Humanitarian Help'] = dfPaises['Deathrate'].apply(humanitarian_help)
print(dfPaises)
