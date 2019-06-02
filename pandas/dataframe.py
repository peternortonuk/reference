import pandas as pd
import numpy as np
from sklearn import datasets


# ===================================================================================
# slicing

print('=== slicing ===\n')

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

print('===============\n')

# ===================================================================================
# copying

print('=== copying ===')

df1 = pd.DataFrame(data=[0, 1, 2])

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

print('===============\n')

# ===================================================================================
'''
apply: apply a function along an axis of the Dataframe
applymap: apply a function to a Dataframe elementwise
map: works elementwise on a Series.

axis : {0 or ‘index’, 1 or ‘columns’}, default 0
   0: apply function to each column.
   1: apply function to each row ie one row at a time
'''

# ===============
# apply

print('=== apply ===\n')

rectangles = [
    {'height': 40, 'width': 10},
    {'height': 20, 'width': 9},
    {'height': 3.4, 'width': 4}
]
rectangles_df = pd.DataFrame(rectangles)


def calculate_area(row):
    return row['height'] * row['width']


# calculate area by multiplying elements along a row
x = rectangles_df.apply(calculate_area, axis=1)
print(x)

# add up all the heights along a column
x = rectangles_df.apply(np.sum, axis=0)
print(x)

print('===============')


# ===============
# applymap

'''
applymap calls func twice on the first column/row to decide whether it can take a fast or slow code path. 
This can lead to unexpected behavior if func has side-effects, as they will take effect twice for the first column/row.
'''

print('=== applymap ===\n')

# create df; normal constructor tries to parse list as columns, so cant use it
data = [[1, 2, 3], [2, 3], [4]]
column = 'lists'
df = pd.DataFrame.from_dict({column: data})
print(df)

# this appends twice; append method returns None but does modify the df
dfx = df.applymap(lambda x: x.append(5))
print(df)  # modified df
print(dfx)  # returns None

# this appends once
dfx = df.applymap(lambda x: x + [6])
print(df)  # original unchanged
print(dfx)  # returns desired result

# this works fine
dfx = df.applymap(lambda x: len(x))
print(dfx)

# now combine with apply; which is an aggregate function
# apply function along column and broadcast to original shape
dfy = dfx.apply(np.sum, axis=0)
print(dfy)

print('===============')

# ===================================================================================
# merge, join & concat

'''
https://stackoverflow.com/questions/40468069/merge-two-dataframes-by-index/40468090#40468090

merge: inner join by default:
pd.merge(df1, df2, left_index=True, right_index=True)

join: left join by default:
df1.join(df2)


concat: outer join by default:
pd.concat([df1, df2], axis=1)
'''

print('=== concatenate ===\n')

# import some data
iris = datasets.load_iris()

# create dataframe
df_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_target = pd.DataFrame(data=iris.target, columns=['target'])

# concatenate
df = pd.concat([df_data, df_target], axis=1)
print(df.head())

print('===============')

# ===================================================================================


pass
