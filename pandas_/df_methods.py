import pandas as pd
from pandas_.data import df_market_cap, df_random

'''
api reference
https://pandas.pydata.org/docs/reference/frame.html


query method
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html
'''

print(
    # unquoted string is parsed as a column name
    # quoted string is a value
    df_market_cap.query(' SECTOR == "B" ')
)

print(
    # column name with spaces needs backtick
    df_market_cap.query(' `INDEX WEIGHT` == .3')
)


mylist = ['A', 'B', 'C']
print(
    # variable is identified by @ symbol
    df_market_cap.query(' SECTOR in @mylist ')
)


'''
isin method
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html
'''

print(
    df_market_cap['SECTOR'].isin(mylist)
)



'''
where method
Replace values where the condition is FALSE.
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html

mask method
Replace values where the condition is TRUE.
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html
'''

print(
    # if else replace with NaN
    df_market_cap.where(df_market_cap['INDEX WEIGHT'] > 0.3)
)


print(
    # if else replace with a value
    df_market_cap.where(df_market_cap['INDEX WEIGHT'] > 0.3, -999)
)


print(
    # if then
    df_market_cap.mask(df_market_cap['INDEX WEIGHT'] > 0.3, -999)
)

'''
idxmin/max method
Return index of first occurrence of minimum over requested axis.
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html
'''

print(
    df_random,
    '\n\n',
    df_random.idxmin(axis='index')
)

pass