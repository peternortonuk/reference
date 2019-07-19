import pandas as pd
from data import df_data, df_target

'''
https://stackoverflow.com/questions/40468069/merge-two-dataframes-by-index/40468090#40468090

merge: inner join by default:
pd.merge(df1, df2, left_index=True, right_index=True)

join: left join by default:
df1.join(df2)

concat: outer join by default:
pd.concat([df1, df2], axis=1)
'''

# concatenate
df = pd.concat([df_data, df_target], axis=1)
print(df.head())

