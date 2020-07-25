'''
https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#compare-with-sql-join


'''

import pandas as pd
import numpy as np
from data import tips

'''
Use the DataFrame.assign() method to append a new column:
'''

# ===================================================================
print('\n=========================================================\n'
      'SELECT'
      '\n========\n')

x = tips.assign(tip_rate=tips['tip'] / tips['total_bill']).head(5)
print(x)


# ===================================================================
print('\n=========================================================\n'
      'WHERE'
      '\n========\n')

# multiple conditions
# and
x = tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5.00)]
print(x)

# or
x = tips[(tips['size'] >= 5) | (tips['total_bill'] > 45)]
print(x)


# ===================================================================
print('\n=========================================================\n'
      'GROUP BY'
      '\n========\n')

x = tips.groupby('sex').size()
print(x)

# applies the method to each column
x = tips.groupby('sex').count()
print(x)

x = tips.groupby('day').agg({'tip': np.mean, 'day': np.size})
print(x)


# ===================================================================
'''
JOINs can be performed with join() or merge(). By default, join() will join the DataFrames on their indices. 
Each method has parameters allowing you to specify the type of join to perform (LEFT, RIGHT, INNER, FULL) 
or the columns to join on (column names or indices).

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html
'''

print('\n=========================================================\n'
      'JOIN'
      '\n========\n')


df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': np.random.randn(4)})
df2 = pd.DataFrame({'key': ['B', 'D', 'D', 'E'], 'value': np.random.randn(4)})

# key is a column here; not an index
x = pd.merge(df1, df2,
             on='key'  # join dfs using this common column name
             )
print(x)


# now set the key as an index
indexed_df2 = df2.set_index('key')
x = pd.merge(df1, indexed_df2,
             left_on='key',  # join the left df on this column
             right_index=True,  # join the right df using its index
             how='inner',  # this is actually the default
             )
print(x)


# ===================================================================
'''
UNION ALL can be performed using concat().

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
'''

print('\n=========================================================\n'
      'UNION'
      '\n========\n')

x = pd.concat([df1, df2],
              axis='rows',  # concat vertically
              ).drop_duplicates()
print(x)


print('\n=========================================================\n'
      'Pandas equivalents for some SQL analytic and aggregate functions'
      '\n========\n')

x = tips.assign(tip_rate=tips['tip'] / tips['total_bill'])\
      .query('tip_rate < 0.14')\
      .sort_values('tip_rate', ascending=False)
print(x)

pass