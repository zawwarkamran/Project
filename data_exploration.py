import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

data = pd.read_csv('merged.txt', sep=',')
data.set_index('date', inplace=True)

# Time Series plot with all the equities
data.plot()
plt.ylabel('Price')
plt.show()

# Shows the individual time series for each equity
for item in data.columns:
    data[item].plot()
    plt.title(item)
    plt.tight_layout()
    plt.ylabel('Price')
    plt.grid()
    plt.show()

# Shows the correlation between each equity
sns.heatmap(data.corr(), cmap='coolwarm', annot=True)
plt.show()

sns.pairplot(data)
plt.show()
