import numpy as np

mat = np.zeros((3, 5))

r, c = mat.shape
qtd_elem = mat.size

print(f"Linhas: {r} | Colunas: {c}")
print(f"Total de elementos: {qtd_elem}")

paridade = "PAR" if qtd_elem % 2 == 0 else "ÍMPAR"
print(f"Esta matriz pode se tornar um vetor unidimensional com um número {paridade} de elementos.")
