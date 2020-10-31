from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from data import x, y


# create one figure
fig = Figure(figsize=(8, 6))
FigureCanvas(fig)
ax = fig.add_subplot(111)

# calculate and plot regression
fit = np.polyfit(x, y, deg=1)
ax.plot(x, fit[0] * x + fit[1], color='red')

# plot scatter data
ax.scatter(x, y)

fig.savefig('test_regression_oo')
pass