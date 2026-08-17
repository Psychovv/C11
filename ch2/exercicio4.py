#parte 4
distancia = float(input('Digite a distancia em Km: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('Preco da passagem:', preco)
