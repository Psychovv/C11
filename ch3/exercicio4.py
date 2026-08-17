cadastro = []

for _ in range(3):
    n = input('Digite o nome: ')
    p = float(input('Digite o peso: '))
    cadastro.append({'nome': n, 'peso': p})

pesado = max(cadastro, key=lambda item: item['peso'])
leve = min(cadastro, key=lambda item: item['peso'])

print('Mais pesada:', pesado['nome'])
print('Mais leve:', leve['nome'])
