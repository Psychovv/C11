import numpy as np

seq_asc = np.arange(0, 52, 2)
seq_desc = np.arange(100, 48, -2)

vetor_unido = np.concatenate((seq_asc, seq_desc))
vetor_final = np.sort(vetor_unido)

print("Arrays concatenados e ordenados:\n", vetor_final)
