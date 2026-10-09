import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_mpg = sns.load_dataset('mpg')
sns.regplot(data=ds_mpg, x='horsepower', y='mpg')
plt.show()
