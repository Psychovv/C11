import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_iris = sns.load_dataset('iris')
ds_setosa = ds_iris[ds_iris['species'] == 'setosa']
corr = ds_setosa.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, fmt='.2f')
plt.show()
