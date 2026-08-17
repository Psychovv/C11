import numpy as np

arr = np.loadtxt('ch4/space.csv', delimiter=';', dtype=str, encoding='utf-8', skiprows=1)
st_foguete = arr[:, 5]

ret = arr[st_foguete == 'StatusRetired']
print((len(ret) / len(arr)) * 100)
