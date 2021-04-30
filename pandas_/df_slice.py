# coding: utf-8
import pandas as pd
from data import df_short_dates


# df with a date index
print(df_short_dates, '\n')

# a single date for comparison with the index
single_date = pd.to_datetime('05-May-2018')

# slice on index and single column
dfx = df_short_dates.loc[single_date:, 'A']
print(dfx, '\n')

# slice on boolean and list of columns; see change in column order
mask = df_short_dates['A'] < 0
dfx = df_short_dates.loc[mask, ['B', 'A']]
print(dfx, '\n')

# chaining; but see warning below
dfx = df_short_dates[mask]['A']
print(dfx, '\n')

# reversing order of chaining doesnt matter
dfx = df_short_dates['A'][mask]
print(dfx, '\n')

# compare setting values with these two approaches
df_short_dates[mask]['A'] = 999  # SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
df_short_dates.loc[mask, 'A'] = 999  # happy joy

'''
note this warning about chaining:
http://pandas.pydata.org/pandas-docs/stable/indexing.html#why-does-assignment-fail-when-using-chained-indexing
http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
'''

'''
where method
https://pandas.pydata.org/pandas-docs/stable/indexing.html#the-where-method-and-masking
Selecting values from a DataFrame with a boolean criterion now also preserves input data shape.
where is used under the hood as the implementation
'''

df_short_dates[df_short_dates['A'] > -1]
df_short_dates.where(df_short_dates['A'] > -1)

# but where gives more options
dfx = df_short_dates.where(df_short_dates['A'] > 1, other=999)
print(dfx, '\n')

