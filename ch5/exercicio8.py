import numpy as np
import pandas as pd

np.random.seed(10)
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)

slicing = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print(slicing)
print(slicing.sum(axis=1))
print(slicing.sum(axis=0))
