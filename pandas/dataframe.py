import pandas as pd
import numpy as np
from sklearn import datasets

# ===================================================================================
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

# ===================================================================================
# create my own data; but with an index
index = pd.date_range(start='01-May-2018', periods=20)
data = np.random.randn(20, 2)
columns = ['num1', 'num2']
df = pd.DataFrame(data=data, index=index, columns=columns)

# a single date for comparison with the index
single_date = pd.to_datetime('05-May-2018')

# slice on index and column
dfx = df.loc[single_date:, 'num1']
print(dfx.head())

# slice on boolean and set values
mask = df['num1'] < 0
dfx = df.loc[mask, 'num1']
print(dfx.head())

# dont need to use loc but then have to chain
dfx = df[mask]['num1']
print(dfx.head())

pass
