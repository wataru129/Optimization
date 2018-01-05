import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def benchi_f(x):
    n=int(x.shape[0]) #xの次元
    out=0
    if problem == 1: #対象2
        for i in range(n):
            out = out + x[i]**2
    return out

def plot():
    x = np.arange(-5,5,0.25)
    y = np.arange(-5,5,0.25)    
    
    X = np.c_[x, y]
    print(X.shape)
    #X = np.meshgrid(X)
    print(X.shape)
    Z = benchi_f(X)

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(X[:,0],X[:,1],Z)
    plt.show()
plot()