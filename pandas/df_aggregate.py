import pandas as pd
from data import df_market_cap

'''
calculate a percentage of group totals

https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#grouping
https://stackoverflow.com/questions/39442064/merging-with-more-than-one-level-overlap-not-allowed
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transform.html

originally tried dataframe merge operation but it couldnt cope with different
indexes
'''

# join with an aggregate; use transform to maintain shape of original df
df = df_market_cap

sector_cols = ['EFFECTIVE DATE', 'CAP', 'SECTOR']
cap_cols = sector_cols[:1]
measure_name = 'INDEX WEIGHT'

# source data structure is unchanged but groupby defines multi-index
df_detail = df.groupby(sector_cols)[measure_name].sum().to_frame()

# transform function maintains original shape
totals = df_detail.groupby(cap_cols)[measure_name].transform(pd.Series.sum)
df_totals = totals.to_frame()

print(df_detail / df_totals)
import pdb; pdb.set_trace()
pass

