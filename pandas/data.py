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

