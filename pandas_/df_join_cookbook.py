'''
Merge, join, and concatenate
   https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

Merge
   https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#merge

Merge two dataframes by index
   https://stackoverflow.com/questions/40468069/merge-two-dataframes-by-index/40468090#40468090
'''

import pandas as pd
from data import df_data, df_target, df_pair1, df_pair2


# ===================================================================
'''
User guide: Merge, join, and concatenate
   https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#concatenating-objects
   
   A useful shortcut to concat() are the append() instance methods on Series and DataFrame. 
   These methods actually predated concat. They concatenate along axis=0, namely the index
'''

# ===================================================================
print('\n=========================================================\n'
      'Concatenating objects'
      '\n========\n')


df_join = pd.concat([df_pair1, df_pair2], axis='columns')  # concat horizontally
print('\n', df_join)

df_join = pd.concat([df_pair1, df_pair2], axis='rows')  # concat vertically
print('\n', df_join)

# keys means we get a column multiindex
df_join = pd.concat([df_pair1, df_pair2], axis='columns', keys=['first', 'second'])
print('\n', df_join)


# ===================================================================
print('\n=========================================================\n'
      'CONCATENATE'
      '\n========\n')
