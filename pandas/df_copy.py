import pandas as pd
from data import date_df

df1 = date_df

df2 = df1  # same df object id therefore same data
df3 = df2.copy(deep=False)  # new df object id but referenced to same data; changes are reflected
df4 = df3.copy(deep=True)  # new df object id and new data; changes are isolated; however check the object id of the data

# print object ids of the dataframes
print(id(df1), id(df2), id(df3), id(df4), '\n')

# now change one value
df2.loc[0] = 99

print(id(df1), id(df2), id(df3), id(df4), '\n')


# print the object ids of the values
print('df1', df1.applymap(id), '\n')
print('df2', df2.applymap(id), '\n')
print('df3', df3.applymap(id), '\n')
print('df4', df4.applymap(id), '\n')

# print the data
print('df1', df1, '\n')
print('df2', df2, '\n')
print('df3', df3, '\n')
print('df4', df4, '\n')  # <-- this is the only one unchanged

'''
this is a bug apparently:
https://stackoverflow.com/questions/46327494/python-pandas-dataframe-copydeep-false-vs-copydeep-true-vs
if it was a true deep copy should have had new ids for the lists contained within it. As a result, when you modify a list inside df2, it affects the list inside df1 as well, because they are the same objects.
https://github.com/pandas-dev/pandas/issues/17406
'''
