'''
The Pyplot API
https://matplotlib.org/api/pyplot_summary.html#the-pyplot-api

Colors in Matplotlib
https://matplotlib.org/api/pyplot_summary.html#colors-in-matplotlib
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# create the dataset
x0 = np.arange(-5, 5, 0.25)
x1 = np.arange(-5, 5, 0.25)
x0, x1 = np.meshgrid(x0, x1)
y = x0 + (x1*5)

# calculate axes limits
x_min, x_max = x0.min() - .5, x0.max() + .5
y_min, y_max = x1.min() - .5, x1.max() + .5

# create figure
fig2d = plt.figure(1, figsize=(8, 6))
ax2d = fig2d.add_subplot(111)

fig3d = plt.figure(1, figsize=(8, 6))
ax3d = fig3d.add_subplot(111, projection='3d')

# create scatter plot
scatter2d = ax2d.scatter(x0, y, cmap=plt.cm.Set1, edgecolor='k')
scatter3d = ax3d.scatter(x0, x1, y, cmap=plt.cm.Set1, edgecolor='k')

# show it
plt.show()
