# %% imports
import pandas as pd
from os import system

# %% functions


def download_data(table, since="2021-04-19T06:40:00"):
    url = f'http://192.53.118.48/binance_{table}?time=gt.{since}'
    system(f'curl -H "Accept: text/csv" \'{url}\' > {table}.csv')


# %% download data as csv files
download_data('btcusdt_trade')
download_data('ltcusdt_trade')
download_data('ltcbtc_trade')

download_data('btcusdt_orderbook')
download_data('ltcusdt_orderbook')
download_data('ltcbtc_orderbook')
'done'
# %% load csv files
download_data_as_csv_files()
btc = pd.read_csv('btcusdt_trade.csv')

# %%
