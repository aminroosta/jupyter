# %% imports
import matplotlib.pyplot as plt
import pandas as pd
from os import system

# %% functions


def download_data(table, since="2021-04-19T06:40:00"):
    url = f'http://192.53.118.48/binance_{table}?time=gt.{since}'
    system(f'curl -H "Accept: text/csv" \'{url}\' > data/{table}.csv')


# %% download data as csv files
download_data('btcusdt_trade')
download_data('ltcusdt_trade')
download_data('ltcbtc_trade')

download_data('btcusdt_orderbook')
download_data('ltcusdt_orderbook')
download_data('ltcbtc_orderbook')
'done'
# %% load csv files
btc = pd.read_csv('data/btcusdt_trade.csv', index_col=0, parse_dates=True)
btc.dtypes
# btc['price'].hist(bins=20, figsize=(10, 10))
btc['quantity'].plot(figsize=(7, 7))
plt.show()
btc['price'].plot(figsize=(7, 7))
plt.show()

# %%
times = pd.DatetimeIndex(btc.time)
grouped = btc.groupby([times.hour, times.minute])
grouped.agg(lambda x: x['price'] * x['quantity'])
