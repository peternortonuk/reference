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
from pair_plot_function import scatterplot_matrix

# import some data
iris = datasets.load_iris()

# create one figure
scatterplot_matrix(data, names=[], **kwargs)

# save it to working directory
fig.savefig('test_pairplot')

# can't show it without using pyplot
# fig.show()

