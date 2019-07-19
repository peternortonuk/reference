# coding: utf-8

import numpy as np
from data import rectangles_df, lists_df

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
print(lists_df)

# this appends twice; append method returns None but does modify the df
dfx = lists_df.applymap(lambda x: x.append(5))
print(lists_df)  # modified df
print(dfx)  # returns None

# this appends once
dfx = lists_df.applymap(lambda x: x + [6])
print(lists_df)  # original unchanged
print(dfx)  # returns desired result

# this works fine
dfx = lists_df.applymap(lambda x: len(x))
print(dfx)

# now combine with apply; which is an aggregate function
# apply function along column and broadcast to original shape
dfy = dfx.apply(np.sum, axis=0)
print(dfy)
