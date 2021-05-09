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
df_short_dates = df_pair1.copy(deep=True)

# create df with labelled columns
rectangles = [
    {'height': 40, 'width': 10},
    {'height': 20, 'width': 9},
    {'height': 3.4, 'width': 4}
]
df_rectangles = pd.DataFrame(rectangles)


# create a small square of data
data = np.random.random_sample(size=(3, 4))
columns = ['a', 'b', 'c', 'd']
df_random = pd.DataFrame(data=data, columns=columns)


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

# create long df of dates
days = 1000
df_long_dates = pd.DataFrame(data=np.random.randn(days, 1), index=pd.date_range(start='01-Jan-2018', periods=days), columns=['price'])


# market cap data
df_market_cap = pd.DataFrame([
        [0, 'Large', 'A', .1, 'a'],
        [0, 'Large', 'B', .2, 'b'],
        [0, 'Large', 'C', .1, 'c'],
        [0, 'Large', 'D', .3, 'd'],
        [0, 'Large', 'E', .1, 'e'],
        [0, 'Large', 'F', .4, 'f'],
        [0, 'Large', 'G', .1, 'g'],
        [0, 'Small', 'A', .2, 'h'],
        [0, 'Small', 'B', .3, 'i'],
        [0, 'Small', 'C', .4, 'j'],
        [0, 'Small', 'D', .5, 'k'],
        [0, 'Small', 'E', .1, 'l'],
        [0, 'Small', 'F', .2, 'm'],
        [0, 'Small', 'G', .1, 'n'],
        [1, 'Large', 'A', .1, 'a'],
        [1, 'Large', 'B', .2, 'b'],
        [1, 'Large', 'C', .1, 'c'],
        [1, 'Large', 'D', .3, 'd'],
        [1, 'Large', 'E', .1, 'e'],
        [1, 'Large', 'F', .4, 'f'],
        [1, 'Large', 'G', .1, 'g'],
        [1, 'Small', 'A', .2, 'h'],
        [1, 'Small', 'B', .3, 'i'],
        [1, 'Small', 'C', .4, 'j'],
        [1, 'Small', 'D', .5, 'k'],
        [1, 'Small', 'E', .1, 'l'],
        [1, 'Small', 'F', .2, 'm'],
        [1, 'Small', 'G', .1, 'n'],
    ], columns=['EFFECTIVE DATE', 'CAP', 'SECTOR', 'INDEX WEIGHT', 'ID'])


'''
https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html
'''
url = ('https://raw.github.com/pandas-dev'
       '/pandas/master/pandas/tests/io/data/csv/tips.csv')
tips = pd.read_csv(url)

# =========================================================================
# a pair of dataframes for comparison

# index is the date of the price observation
length = 300
index = pd.date_range('01-Jan-2018', freq='D', periods=length, name='price_index')
data = np.random.randn(length)
columns = ['price']
df_prices = pd.DataFrame(data=data, index=index, columns=columns)


# index is the contract month that has expiry dates in the columns
length = 5
index = pd.date_range('01-Jan-2018', freq='MS', periods=length, name='expiry_index')
data_dict = {
    'expiry_start': pd.date_range('01-Dec-2017', freq='MS', periods=length),
    'expiry_end': pd.date_range('01-Dec-2017', freq='M', periods=length),
    }
df_expiry = pd.DataFrame(data=data_dict, index=index)

# =========================================================================
