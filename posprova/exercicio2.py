import numpy as np

a = np.array(['Ana', 'Bruno', 'Carla', 'Diego'])
b = np.array(['Elena', 'Felipe', 'Gabi', 'Hugo'])

unido = np.concatenate((a, b))
print('Array concatenado:', unido)

mat = unido.reshape(2, 4)
print('Array 2-D:\n', mat)

ordenado = np.sort(mat.flatten())[::-1].reshape(2, 4)
print('Array 2-D em ordem decrescente:\n', ordenado)
