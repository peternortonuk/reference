# coding: utf-8

import pandas as pd
import numpy as np


# create df with a date index
index = pd.date_range(start='01-May-2018', periods=5)
data = np.random.randn(5, 2)
columns = ['num1', 'num2']
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df, '\n')

# a single date for comparison with the index
single_date = pd.to_datetime('05-May-2018')

# slice on index and single column
dfx = df.loc[single_date:, 'num1']
print(dfx, '\n')

# slice on boolean and list of columns; see change in column order
mask = df['num1'] < 0
dfx = df.loc[mask, ['num2', 'num1']]
print(dfx, '\n')

# chaining; but see warning below
dfx = df[mask]['num1']
print(dfx, '\n')

# reversing order of chaining doesnt matter
dfx = df['num1'][mask]
print(dfx, '\n')

# compare setting values with these two approaches
df[mask]['num1'] = 999  # SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
df.loc[mask, 'num1'] = 999  # happy joy

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

df[df['num1']>-1]
df.where(df['num1'] > -1)

# but where gives more options
dfx = df.where(df['num1'] > 1, other=999)
print(dfx, '\n')

