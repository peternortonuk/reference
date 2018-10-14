import pandas as pd
import numpy as np
from sklearn import datasets

# ===================================================================================
# concatenate and update

# import some data
iris = datasets.load_iris()

# create dataframe from numpy arrays
df_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_target = pd.DataFrame(data=iris.target, columns=['target'])

# concatenate
df = pd.concat([df_data, df_target], axis=1)

# create mask
mask = df['sepal length (cm)'] > 5.0

# update values as df.loc[rows, columns]
df.loc[mask, 'sepal width (cm)'] = 20

print(df.head())
print('===============')

# ===================================================================================
# slicing

# create df with a date index
index = pd.date_range(start='01-May-2018', periods=20)
data = np.random.randn(20, 2)
columns = ['num1', 'num2']
df = pd.DataFrame(data=data, index=index, columns=columns)

# a single date for comparison with the index
single_date = pd.to_datetime('05-May-2018')

# slice on index and single column
dfx = df.loc[single_date:, 'num1']
print(dfx.head())
print()

# slice on boolean and list of columns
mask = df['num1'] < 0
dfx = df.loc[mask, ['num2', 'num1']]
print(dfx.head())
print()

# chaining; but see warning below
dfx = df[mask]['num1']
print(dfx.head())
print()

# reversing order of chaining doesnt matter
dfx = df['num1'][mask]
print(dfx.head())
print('===============')

'''
note this warning about chaining:
http://pandas.pydata.org/pandas-docs/stable/indexing.html#why-does-assignment-fail-when-using-chained-indexing
'''

# ===================================================================================
# copying

df1 = pd.DataFrame(data=[0, 1, 2])

df2 = df1  # same df object id therefore same data
df3 = df2.copy(deep=False)  # new df object id but referenced to same data; changes are reflected
df4 = df3.copy(deep=True)  # new df object id and new data; changes are isolated; however check the object id of the data

print(id(df1), id(df2), id(df3), id(df4))
print()

# now change one value
df2.loc[0] = 99

# print the object ids of the values
print('df1\n', df1.applymap(id))
print('df2\n', df2.applymap(id))
print('df3\n', df3.applymap(id))
print('df4\n', df4.applymap(id))

# print the data
print('df1\n', df1)
print('df2\n', df2)
print('df3\n', df3)
print('df4\n', df4)
print()

'''
this is a bug apparently:
https://stackoverflow.com/questions/46327494/python-pandas-dataframe-copydeep-false-vs-copydeep-true-vs
if it was a true deep copy should have had new ids for the lists contained within it. As a result, when you modify a list inside df2, it affects the list inside df1 as well, because they are the same objects.
https://github.com/pandas-dev/pandas/issues/17406
'''



# ===================================================================================
# apply

# create df; normal constructor tries to parse list as columns
data = [[1, 2, 3], [2, 3], [4]]
column = 'lists'
df = pd.DataFrame.from_dict({column: data})
print(df)

# this is weird; it appends twice; append method returns None but does modify the df
dfx = df.applymap(lambda x: x.append(5))
print(dfx)  # returns None
print(df)  # modified df

# so instead do this
dfx = df.applymap(lambda x: x + [6])
print(dfx)

# this works fine
dfx = df.applymap(lambda x: len(x))
print(dfx)

# now combine with apply; which is an aggregate function
# apply function along column and broadcast to original shape
dfy = dfx.apply(np.sum, axis=0, result_type='broadcast')
print(dfy)


# ===================================================================================
# merge, join & concat

'''
https://stackoverflow.com/questions/40468069/merge-two-dataframes-by-index/40468090#40468090
Use merge, which is inner join by default:
pd.merge(df1, df2, left_index=True, right_index=True)

Or join, which is left join by default:
df1.join(df2)

Or concat, which is outer join by default:
pd.concat([df1, df2], axis=1)
'''





pass
