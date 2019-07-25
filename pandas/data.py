import pandas as pd
import numpy as np
from sklearn import datasets


# create two dfs to outer join
days = 5
df_pair1 = pd.DataFrame(data=np.random.randn(days, 2), index=pd.date_range(start='01-May-2018', periods=days), columns=['A', 'B'])
df_pair1['source'] = 'pair1'
df_pair2 = pd.DataFrame(data=np.random.randn(days, 2), index=pd.date_range(start='03-May-2018', periods=days), columns=['A', 'B'])
df_pair2['source'] = 'pair2'
df_join = pd.concat([df_pair1, df_pair2], axis='columns', keys=['first', 'second'])


# when only one of the pair is required
date_df = df_pair1.copy(deep=True)

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

