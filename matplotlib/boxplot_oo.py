'''
The Object-Oriented API
https://matplotlib.org/api/pyplot_summary.html#the-object-oriented-api

Colors in Matplotlib
http://matplotlib.org/api/_as_gen/matplotlib.pyplot.colors.html
'''


from sklearn import datasets
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

# import some data
iris = datasets.load_iris()

# create one figure
fig = Figure(figsize=(8, 6))
FigureCanvas(fig)

# create one subplot
# a 3-digit integer or three separate integers describing the position of the subplot.
# If the three integers are I, J, and K, the subplot is the Ith plot on a grid with J rows and K columns.
# returns: The axes of the subplot.
ax = fig.add_subplot(111)

# create boxplot
ax.boxplot(iris.data)

# label & size etc
ax.set_xticklabels(iris.feature_names)
ax.set_ylabel('cm')
ax.grid(False)

# save it to working directory
fig.savefig('test_boxplot_oo')

# can't show it without using pyplot
# fig.show()

