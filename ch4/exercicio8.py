import numpy as np

arr = np.loadtxt('ch4/space.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)
locs = arr[:, 2]

us_launches = [loc for loc in locs if 'USA' in loc]
print(len(us_launches))
