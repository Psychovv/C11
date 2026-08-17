qtd = int(input('Quantas pessoas: '))
grupo = []

for _ in range(qtd):
    n = input('Nome: ')
    i = int(input('Idade: '))
    s = input('Sexo (M/F): ')
    grupo.append({'nome': n, 'idade': i, 'sexo': s})

total_idades = sum(item['idade'] for item in grupo)
jovens_fem = sum(1 for item in grupo if item['sexo'] == 'F' and item['idade'] < 20)

print('Media de idade:', total_idades / qtd)
print('Mulheres com menos de 20 anos:', jovens_fem)
