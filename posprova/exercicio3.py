import numpy as np

colors = [
    {"color": "black", "type": "primary", "code": {"rgba": [255, 255, 255, 1], "hex": "#000"}},
    {"color": "green", "type": "secondary", "code": {"rgba": [0, 255, 0, 0.1], "hex": "#0F0"}},
    {"color": "yellow", "type": "primary", "code": {"rgba": [255, 255, 0, 0.7], "hex": "#FF0"}},
    {"color": "blue", "type": "primary", "code": {"rgba": [0, 0, 255, 1], "hex": "#00F"}},
]

print('a) Cores primarias:')
for c in colors:
    if c['type'] == 'primary':
        print(c['color'])

print('\nb) Hex com azul maximo (255):')
for c in colors:
    if c['code']['rgba'][2] == 255:
        print(c['code']['hex'])

pares = []
for c in colors:
    pares.extend([c['color'], c['code']['hex']])

arr_1d = np.array(pares)
print('\nc) Array 1-D:', arr_1d)

arr_2d = arr_1d.reshape(-1, 2)
print('\nd) Array 2-D:\n', arr_2d)

traducao = {
    'black': 'preto',
    'green': 'verde',
    'yellow': 'amarelo',
    'blue': 'azul',
}

arr_pt = np.array([[traducao[nome], hex_] for nome, hex_ in arr_2d])
print('\ne) Array 2-D em portugues:\n', arr_pt)
