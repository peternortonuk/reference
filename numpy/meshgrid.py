# ========================================================================
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html
#
# generate a full set of co-ordinates

import numpy as np
import matplotlib.pyplot as plt

nx, ny = (5, 2)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)

print('breakpoint')

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
h = plt.contourf(x,y,z)

print('breakpoint')
