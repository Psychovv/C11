import numpy as np

arr = np.loadtxt('ch4/space.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)
valores = arr[:, 6].astype(float)

filtrados = valores[valores > 0]
print(np.mean(filtrados))
