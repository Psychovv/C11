import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_titanic = sns.load_dataset('titanic')
sns.boxplot(data=ds_titanic, x='class', y='age', hue='sex')
plt.show()
