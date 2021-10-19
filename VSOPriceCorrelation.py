import pandas as pd
from pycoingecko import CoinGeckoAPI
from scipy.stats.stats import pearsonr
from matplotlib import pyplot as plt
import numpy as np


# calling the API directly instead of using requests and url
cg = CoinGeckoAPI()
vso_prices = cg.get_coin_market_chart_by_id(id='verso', vs_currency='usd', days=8)
hct_prices = cg.get_coin_market_chart_by_id(id='hurricaneswap-token', vs_currency='usd', days=8)
avax_prices = cg.get_coin_market_chart_by_id(id='avalanche-2', vs_currency='usd', days=8)

# create date and price dataframes for each token
df_vso = pd.DataFrame(vso_prices['prices'], columns=['Date', 'Price'])
df_hct = pd.DataFrame(hct_prices['prices'], columns=['Date', 'Price'])
df_avax = pd.DataFrame(avax_prices['prices'], columns=['Date', 'Price'])

# print(len(df_vso['Price']))
# print(len(df_hct['Price']))
# print(len(df_avax['Price']))

# convert 'Date' column from unix (in milliseconds) format to datetime format
df_vso['Date'] = pd.to_datetime(df_vso['Date'], unit='ms')
df_hct['Date'] = pd.to_datetime(df_hct['Date'], unit='ms')
df_avax['Date'] = pd.to_datetime(df_avax['Date'], unit='ms')

# print(df_vso.head())
# print(df_hct.head())
# print(df_avax.head())


corr = pearsonr(df_avax['Price'], df_hct['Price'])

print('Pearson correlation: ' + str(corr[0]))
print('At p-value: ' + str(corr[1]))


plt.plot(np.log(df_vso['Price']))
plt.plot(np.log(df_hct['Price']))
plt.plot(np.log(df_avax['Price']))
plt.show()