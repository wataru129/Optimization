from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt

from deap import benchmarks
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5.12, 5.12, 0.1)
Y = np.arange(-5.12, 5.12, 0.1)
X, Y = np.meshgrid(X, Y)
Z = [[benchmarks.rastrigin((x, y))[0] for x, y in zip(xx, yy)] for xx, yy in zip(X, Y)]
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.show()