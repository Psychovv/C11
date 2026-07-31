#parte 5
numero = int(input('Digite um numero entre 1000 e 9999: '))
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10
print('Unidade:', unidade)
print('Dezena:', dezena)
print('Centena:', centena)
print('Milhar:', milhar)
