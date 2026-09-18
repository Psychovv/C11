import pandas as pd

dfPaises = pd.read_csv('ch5/paises.csv', delimiter=';')
dfPaises = dfPaises.drop('Coastline (coast/area ratio)', axis=1)
dfPaises.to_csv('ch5/paises_sem_coastline.csv', sep=';', index=False)
