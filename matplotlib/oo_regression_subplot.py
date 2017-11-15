import pandas as pd
import numpy as np
from sklearn import datasets
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# import some data
iris = datasets.load_iris()

# create dataframe from numpy arrays
df_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_target = pd.DataFrame(data=iris.target, columns=['target'])
df = pd.concat([df_data, df_target], axis=1)

# create one figure
fig = Figure(figsize=(8, 6))
FigureCanvas(fig)

# find all unique values of target
levels = df.groupby(['target']).all().index

axes = {}
for i, target in enumerate(levels):
    # create a new subplot
    axes[i] = fig.add_subplot(1, 3, i+1)
    # select the data
    mask = df['target'] == target
    x, y = df[mask]['petal length (cm)'], df[mask]['petal width (cm)']
    # add scatter to the axes
    axes[i].scatter(x, y, edgecolor='k')
    # fit and plot regression
    fit = np.polyfit(x, y, deg=1)
    axes[i].plot(x, fit[0] * x + fit[1])
    # labelling
    axes[i].set_title(iris.target_names[i])

fig.savefig('test_regression_subplot')

pass