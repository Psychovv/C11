estoque = []

for _ in range(3):
    item = input('Nome do produto: ')
    val = float(input('Preco: '))
    unid = int(input('Quantidade em estoque: '))
    estoque.append({'nome': item, 'preco': val, 'quantidade': unid})

for p in estoque:
    subtotal = p['preco'] * p['quantidade']
    print(p['nome'], subtotal)
