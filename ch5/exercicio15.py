import pandas as pd

dfPaises = pd.read_csv('ch5/paises.csv', delimiter=';')


def reduzir_mortalidade(valor):
    return valor * 0.85


original = dfPaises['Infant mortality (per 1000 births)']
reduzida = original.apply(reduzir_mortalidade).rename('Infant mortality -15%')
print(pd.concat([original, reduzida], axis=1))
