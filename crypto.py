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
btc = pd.read_csv('data/btcusdt_trade.csv')
'done'

# %%


def prepare(df):
    diff = df['price'] - df['price'].shift(periods=1)
    result = pd.DataFrame(df['time'])
    volume = diff * df['quantity']

    times = pd.DatetimeIndex(df['time']).round('10S')
    result['volume'] = volume.groupby([times]).sum()
    price = df['price'].groupby([times]).first()
    return result


prepare(btc)


# %%
