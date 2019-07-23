import pandas as pd
import numpy as np
from sklearn import datasets

# create df with a date index
index = pd.date_range(start='01-May-2018', periods=5)
data = np.random.randn(5, 2)
columns = ['num1', 'num2']
date_df = pd.DataFrame(data=data, index=index, columns=columns)


# create df with labelled columns
rectangles = [
    {'height': 40, 'width': 10},
    {'height': 20, 'width': 9},
    {'height': 3.4, 'width': 4}
]
rectangles_df = pd.DataFrame(rectangles)


# create df of lists
# normal constructor tries to parse list as columns, so cant use it
data = [[1, 2, 3], [2, 3], [4]]
column = 'lists'
lists_df = pd.DataFrame.from_dict({column: data})


# create df from external library
iris = datasets.load_iris()
df_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_target = pd.DataFrame(data=iris.target, columns=['target'])


# create df with multiindex columns
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
            ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']
          ]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df_multi_col = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=index)


# create two dfs to outer join
df_pair1 = pd.DataFrame(data=np.random.randn(4, 2), index=[0, 1, 2, 3], columns=['A', 'B'])
df_pair1['source'] = 'pair1'
df_pair2 = pd.DataFrame(data=np.random.randn(4, 2), index=[2, 3, 4, 5], columns=['A', 'B'])
df_pair2['source'] = 'pair2'
df_join = pd.concat([df_pair1, df_pair2], axis='columns', keys=['first', 'second'])


