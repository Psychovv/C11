import numpy as np

arr = np.loadtxt('ch4/space.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)
st_missao = arr[:, 7]

ok = arr[st_missao == 'Success']
print((len(ok) / len(arr)) * 100)
