musicas = []

while True:
    nome = input('Nome da musica: ')
    ano = int(input('Ano da musica: '))
    musicas.append({'nome': nome, 'ano': ano})

    cont = input('Cadastrar outra? (s/n): ')
    if cont.lower() != 's':
        break

print('Quantidade cadastrada:', len(musicas))

ano_mais_antigo = min(m['ano'] for m in musicas)
antigas = [m for m in musicas if m['ano'] == ano_mais_antigo]

print('Musica(s) do ano mais antigo:')
for m in antigas:
    print(m)
