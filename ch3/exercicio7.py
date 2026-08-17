lista_receita = {'farinha', 'ovo', 'acucar', 'leite', 'fermento'}
despensa_p1 = {'farinha', 'ovo'}
despensa_p2 = {'acucar', 'leite'}

estoque_total = despensa_p1.union(despensa_p2)
pendencias = lista_receita.difference(estoque_total)

print(pendencias)
