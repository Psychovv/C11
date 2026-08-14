import numpy as np

a = np.ones(8)
b = np.random.randint(0, 10, size=8)

c = a + b
print(c)

total = np.sum(c)
print(f"Soma total: {total}")

shape_final = (4, 2) if total >= 40 else (2, 4)
mat_res = c.reshape(shape_final)

print("Matriz reshape:\n", mat_res)
