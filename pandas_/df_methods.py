import pandas as pd
from pandas_.data import df_market_cap

'''
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
    df_market_cap.query(' `SECTOR` in @mylist ')
)

print()