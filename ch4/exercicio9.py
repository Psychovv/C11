import numpy as np

arr = np.loadtxt('ch4/space.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

spx = arr[arr[:, 1] == 'SpaceX']
custos_spx = spx[:, 6].astype(float)
pos = np.argmax(custos_spx)

print(spx[pos, 4], custos_spx[pos])
