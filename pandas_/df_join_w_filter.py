import pandas as pd
from pandas.testing import assert_frame_equal
import numpy as np
from data import df_prices, df_expiry

'''
Join with a criteria based on the values
   https://stackoverflow.com/questions/15581829/how-to-perform-an-inner-or-outer-join-of-dataframes-with-pandas-on-non-simplisti

Using searchsorted to merge based on values inside a range
   https://stackoverflow.com/questions/25125626/pandas-merge-with-logic/2512764
   https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.Index.searchsorted.html
'''


df_prices_copy = df_prices.copy()
df_expiry_copy = df_expiry.copy()

# ===================================================================
print('\n=========================================================\n'
      'Iterate method'
      '\n========\n')
# iterate method (slow and bad); but at least its right

df_prices = df_prices_copy.copy()
df_result = pd.DataFrame()
for row in df_expiry.itertuples():
    mask = (row.expiry_start <= df_prices.index) & (df_prices.index <= row.expiry_end)
    df_prices.loc[mask, 'expiry_start'] = row.expiry_start
    df_prices.loc[mask, 'expiry_end'] = row.expiry_end
    df_result = pd.concat([df_result, df_prices.loc[mask]], axis='rows')
print(df_result)


# ===================================================================
print('\n=========================================================\n'
      'Cartesian join then filter'
      '\n========\n')

df_prices = df_prices_copy.copy()

# move index to column to support filtering later
df_prices.reset_index(inplace=True)

# add dummy columns to support join
df_expiry['key'] = 0
df_prices['key'] = 0

df_result2 = df_prices.merge(df_expiry, how='outer', on='key')\
    .drop('key', axis=1)\
    .query('expiry_start <= price_index and price_index <= expiry_end')

df_result2.set_index('price_index', drop=True, inplace=True)
print(df_result2)

assert_frame_equal(df_result, df_result2)

# ===================================================================
print('\n=========================================================\n'
      'Index searchsorted method'
      '\n========\n')

df_prices = df_prices_copy.copy()
df_expiry = df_expiry_copy.copy()

# create expiry index from the start/end column data
expiry_start_idx = pd.DatetimeIndex(df_expiry['expiry_start'])
expiry_end_idx = pd.DatetimeIndex(df_expiry['expiry_end']) + pd.DateOffset(days=1)

# create new index showing index location of where the price date fits in the expiry index
#    left: the index of the first suitable location found is given
#    right: return the last such index
start_idx = expiry_start_idx.searchsorted(df_prices.index, side='right') - 1
end_idx = expiry_end_idx.searchsorted(df_prices.index, side='right')

# insert the new index where start and end match
df_prices['idx'] = np.where(start_idx == end_idx, end_idx, np.nan)

# remove the contract date index and reset to an integer (to match our new expiry index)
df_expiry.reset_index(inplace=True)

# join on new index; then drop
df_result3 = pd.merge(df_prices, df_expiry, left_on=['idx'], right_index=True)\
    .drop(['idx', 'expiry_index'], axis='columns')
print(df_result3)

assert_frame_equal(df_result, df_result3)
pass
