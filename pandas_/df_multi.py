from data import df_multi_col, df_join

# slice on multindex columns; simple on first level
print(df_multi_col)
multi_mask = 'bar', slice(None)
df = df_multi_col.T.loc[multi_mask].T
print(df)
import pdb; pdb.set_trace()


# doesnt work on second level; use cross-section instead
multi_mask = slice(None), 'two'  # this wont work
df = df_multi_col.T.xs('two', level='second')
print(df)
import pdb; pdb.set_trace()


# maybe loc doesnt work due to indexing so
df = df_multi_col.T
df.sort_index(inplace=True)
import pdb; pdb.set_trace()
# df = df.loc[multi_mask].T  # KeyError: 'two'


# filter result of outer join
# cross-section xs works well on a single row but not on multiple rows
print(df_join)
df = df_join.T.xs('A', level=1).T
print(df)
import pdb; pdb.set_trace()


# alternative for multiple selection
df = df_join.T.select(lambda x: x[1] in ['A', 'source'])
print(df)
import pdb; pdb.set_trace()


pass
