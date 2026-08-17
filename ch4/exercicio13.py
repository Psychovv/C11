import numpy as np

arr = np.loadtxt('ch4/space.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)

custos = arr[:, 6].astype(float)
max_idx = np.argmax(custos)

print(arr[max_idx, 1], custos[max_idx])
