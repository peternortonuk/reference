import pandas as pd
from data import df_data, df_target, df_pair1, df_pair2

'''
https://stackoverflow.com/questions/40468069/merge-two-dataframes-by-index/40468090#40468090
https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

merge: inner join by default:
pd.merge(df1, df2, left_index=True, right_index=True)

join: left join by default:
df1.join(df2)

concat: outer join by default:
pd.concat([df1, df2], axis=1)
'''

# concatenate
df_join = pd.concat([df_pair1, df_pair2], axis='columns')  # concat horizontally
print('\n', df_join)

df_join = pd.concat([df_pair1, df_pair2], axis='rows')  # concat vertically
print('\n', df_join)

# keys means we get a column multiindex
df_join = pd.concat([df_pair1, df_pair2], axis='columns', keys=['first', 'second'])
print('\n', df_join)

import pdb; pdb.set_trace()