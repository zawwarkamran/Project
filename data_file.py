import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from functools import reduce
# We can pull technical indicators as well from alpha_vantage using alpha_vantage.technicalindicators

# The equities we want
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']
# Your key here
key = 'TUFG6CJ46YJKR38I'
# Chose your output format, or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')

# The TimeSeries function returns a tuple, where the first item in the tuple is the pandas data frame with the
# historical data. Right now we are getting the 'compact' historical data, this basically means the last 100 days of
# data, if we set outputsize to 'full' we can get all of the data alpha_vantage has.
# aapl_data is a pandas dataframe, aapl_meta_data is a dict
# aapl_data, aapl_meta_data = ts.get_daily(symbol='AAPL', outputsize='full')
stocks = {}
for equity in tickers:
    stocks[equity] = ts.get_intraday(outputsize='full', symbol=equity)[0]

# We want to keep the close prices only so the following chunk of code makes one pandas dataframe with just the closing
# prices of all of the equities with their name. We can reset the index once we call merged.txt and set index to date to
# create a time series plot, although tbh this is not needed.
data_lst = []
for key, item in stocks.items():
    for name in item.columns:
        if name != '4. close':
            item = item.drop(name, axis=1)
    data_lst.append(item.rename(columns={'4. close': key}).reset_index())
df_merged = reduce(lambda left, right: pd.merge(left, right, on=['date'], how='outer'), data_lst).fillna(0)
df_merged.to_csv('merged.txt', sep=',', na_rep='.', index=False)
