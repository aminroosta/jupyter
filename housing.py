#%% download the housing.csv file
from os import system
remote = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/'
url = remote + 'datasets/housing/housing.csv'
system(f'curl {url} > housing.csv')
#%%
import pandas as pd
import matplotlib.pyplot as plt
housing = pd.read_csv('housing.csv')
housing.hist()
housing.describe()