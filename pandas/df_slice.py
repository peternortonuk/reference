# coding: utf-8
import pandas as pd
from data import date_df


# df with a date index
print(date_df, '\n')

# a single date for comparison with the index
single_date = pd.to_datetime('05-May-2018')

# slice on index and single column
dfx = date_df.loc[single_date:, 'num1']
print(dfx, '\n')

# slice on boolean and list of columns; see change in column order
mask = date_df['num1'] < 0
dfx = date_df.loc[mask, ['num2', 'num1']]
print(dfx, '\n')

# chaining; but see warning below
dfx = date_df[mask]['num1']
print(dfx, '\n')

# reversing order of chaining doesnt matter
dfx = date_df['num1'][mask]
print(dfx, '\n')

# compare setting values with these two approaches
date_df[mask]['num1'] = 999  # SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
date_df.loc[mask, 'num1'] = 999  # happy joy

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

date_df[date_df['num1'] > -1]
date_df.where(date_df['num1'] > -1)

# but where gives more options
dfx = date_df.where(date_df['num1'] > 1, other=999)
print(dfx, '\n')

