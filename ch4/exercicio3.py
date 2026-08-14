import numpy as np

grid = np.zeros((2, 2), dtype=int)

b_row, b_col = np.random.randint(0, 2, size=2)
grid[b_row, b_col] = 1

pontos = 0

for i in range(1, 4):
    print(f"\nTentativa {i}/3")
    l = int(input("Escolha a linha (0 ou 1): "))
    c = int(input("Escolha a coluna (0 ou 1): "))

    if grid[l, c] == 1:
        print("Perdeu!")
        break

    print("Continua..")
    pontos += 1

    if pontos == 3:
        print("Ganhou!")
