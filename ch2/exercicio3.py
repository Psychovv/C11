#parte 3
sexo = input('Digite o sexo (M/F): ')
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o sexo (M/F): ')
if sexo == 'M':
    print('Homem')
else:
    print('Mulher')
