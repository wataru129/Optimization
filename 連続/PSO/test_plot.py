import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def benchi_f(x):
    n=int(x.shape[0]) #xの次元
    out=0
    for i in range(n):
        out = out + x[i]**2
    return out


x = np.arange(-5,5,0.01)
y = np.arange(-5,5,0.01)    
#X = np.c_[x, y].T
X = np.meshgrid(x,y)
Z=np.zeros(1000)
for i in range(1000):
    Z[i] = benchi_f(X[:,i])
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X[0,:],X[1,:],Z)
plt.show()