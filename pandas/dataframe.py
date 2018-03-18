
import pandas as pd
from sklearn import datasets

# import some data
iris = datasets.load_iris()

# create dataframe from numpy arrays
df_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_target = pd.DataFrame(data=iris.target, columns=['target'])
df = pd.concat([df_data, df_target], axis=1)
print df.head()

# create mask
mask = df['sepal length (cm)'] > 5.0

# update values as df.loc[rows, columns]
df.loc[mask, 'sepal width (cm)'] = 20

print df.head()

pass