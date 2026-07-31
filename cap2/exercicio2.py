#parte 2
numero = int(input('Digite o numero: '))
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
for c in range(inicio, fim+1):
    print(numero, 'x', c, '=', numero*c)
