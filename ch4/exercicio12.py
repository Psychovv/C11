import numpy as np

arr = np.loadtxt('ch4/space.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)
locs = arr[:, 2]

rus = [l for l in locs if 'Russia' in l]
print(len(rus))
