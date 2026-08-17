nome_aluno = input('Digite o nome do aluno: ')
nota_final = float(input('Digite a media do aluno: '))

registro = {'nome': nome_aluno, 'media': nota_final}
registro['situacao'] = 'AP' if nota_final >= 50 else 'RP'

print(registro)
