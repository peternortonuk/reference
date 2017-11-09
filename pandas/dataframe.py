
import pandas as pd
from sklearn import datasets

# import some data
iris = datasets.load_iris()

# create dataframe from numpy arrays
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print df.head()

# create mask
mask = df['sepal length (cm)'] > 5.0

# update values as df.loc[rows, columns]
df.loc[mask, 'sepal width (cm)'] = 20

print df.head()

pass