

from sklearn import datasets
import matplotlib.pyplot as plt

# import some data
iris = datasets.load_iris()

# create the datasets
x0 = iris.data[:, 0]
x1 = iris.data[:, 1]
y = iris.target

# calculate axes limits
x_min, x_max = x0.min() - .5, x0.max() + .5
y_min, y_max = x1.min() - .5, x1.max() + .5

# create one figure
plt.figure(1, figsize=(8, 6))

# create scatter plot; using a standard colormap
# points have a 'k'=black border
plt.scatter(x0, x1, c=y, cmap=plt.cm.Set1, edgecolor='k')

# label & size etc
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks()
plt.yticks()
plt.grid()

# save it to working directory; and show it
plt.savefig('test_scatter')
plt.show()
