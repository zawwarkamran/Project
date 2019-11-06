import pandas as pd
from pandas.plotting import lag_plot
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.tsa.stattools as ts
sns.set_style('white')

data = pd.read_csv('merged.txt', sep=',')

# Time Series plot with all the equities
data.plot()
plt.tight_layout()
plt.ylabel('Price')
plt.show()

# Shows the individual time series for each equity
for item in data.columns:
    if item != 'date':
        plt.figure(dpi=160)
        data[item].plot()
        plt.title(item)
        plt.tight_layout()
        plt.ylabel('Price')
        plt.grid()
        plt.show()

# Shows the correlation between each equity
plt.figure(dpi=160)
sns.heatmap(data.corr(), cmap='coolwarm', annot=True)
plt.tight_layout()
plt.title('Heatmap showing correlation between equities')
plt.show()

sns.pairplot(data)
plt.tight_layout()
plt.show()
