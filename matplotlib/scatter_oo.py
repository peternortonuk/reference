'''
http://matplotlib.org/api/_as_gen/matplotlib.pyplot.colors.html

'''


from sklearn import datasets
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

# import some data
iris = datasets.load_iris()

# create the datasets
x0 = iris.data[:, 0]
x1 = iris.data[:, 1]
y = iris.target

# calculate axes limits
x_min, x_max = x0.min() - .5, x0.max() + .5
y_min, y_max = x1.min() - .5, x1.max() + .5

# calculate ticks; pyplot does this automatically
xticks = np.arange(x_min, x_max, 1)
yticks = np.arange(y_min, y_max, 0.5)

# create one figure
fig = Figure(figsize=(8, 6))
FigureCanvas(fig)

# create one subplot
# a 3-digit integer or three separate integers describing the position of the subplot.
# If the three integers are I, J, and K, the subplot is the Ith plot on a grid with J rows and K columns.
# returns: The axes of the subplot.
ax = fig.add_subplot(111)

# create scatter plot; using a standard colormap
# points have a 'k'=black border
ax.scatter(x0, x1, c=y, cmap='Set1', edgecolor='k')

# label & size etc
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.grid(True)

# save it to working directory
fig.savefig('test_scatter_oo')

# can't show it without using pyplot
# fig.show()

