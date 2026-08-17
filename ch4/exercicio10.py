import numpy as np

arr = np.loadtxt('ch4/space.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)
comps = arr[:, 1]

nomes, counts = np.unique(comps, return_counts=True)
for item, total in zip(nomes, counts):
    print(item, total)
