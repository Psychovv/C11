import numpy as np

np.random.seed(10)

m = np.random.randint(1, 51, size=(4, 4))
print("Matriz 4x4:\n", m)

cols_mean = m.mean(axis=0)
rows_mean = m.mean(axis=1)

print("\nMédia das colunas:", cols_mean)
print("Média das linhas:", rows_mean)

print("\nMaior média encontrada nas colunas:", cols_mean.max())
print("Maior média encontrada nas linhas:", rows_mean.max())

vals, counts = np.unique(m, return_counts=True)

print("\nQuantidade de aparições de cada número:")
for v, cnt in zip(vals, counts):
    print(f"Número {v}: {cnt} vez(es)")

duplicados = vals[counts == 2]
print("\nNúmeros que aparecem exatamente 2 vezes na matriz:", duplicados)
