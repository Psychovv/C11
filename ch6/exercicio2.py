import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_titanic = sns.load_dataset('titanic')
sns.histplot(data=ds_titanic, x='age', hue='sex', kde=True)
plt.show()
