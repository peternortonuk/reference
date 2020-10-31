from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from data import groups_of_data

'''
control order of plots
'''

fig = Figure(figsize=(8, 6))
FigureCanvas(fig)

ax1 = fig.add_subplot(121)
ax1.boxplot(groups_of_data)

ax1 = fig.add_subplot(122)
groups_of_data = sorted(groups_of_data, key=lambda x: np.average(x))
ax1.boxplot(groups_of_data)

fig.savefig('test_boxplot2_oo')

