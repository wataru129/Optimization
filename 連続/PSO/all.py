# -*- coding: utf-8 -*-
import numpy as np
import region
import scipy.io as spio
from numpy import random
#import update
#from plot import plot
import sys
sys.path.append('C:\\Users\SYS2017B4-c.DESKTOP-1LG9001\Desktop\graduation research\graduate\Benchmark')

from Bench_continuous_function import benchi_f



initial=spio.loadmat("InitialPoints_300_100_100.mat")
initial_points = initial['IP']

# PSO-parameter---------------
w = 0.729
c1 = 1.4955
c2 = 1.4955
# --------------------------
# settig-parameter----------
count=0
T = 1   # Max of challenge
problem=1
n = 50   # dimension
m = 20   # The number of Particle
k_max = 50  # Max of reiteration
# ----------------------------------
test = np.zeros((n,m,k_max))
print('all')
for S in range(T):
    # Reset of initial value---------------------------
    r1, r2 = region.region(problem)   # Area of x
    x = r2 * initial_points[S,0:m, 0:n].T    # initial point r2=(|r1|     +     |r2|)/2
    v = 1  * initial_points[S,0:m, 0:n].T         # initial velocity
    pbest = x               # Best x in the diviual particle
    fpbest = np.zeros(m)
    gbest = pbest[:,0]
    fgbest = benchi_f(gbest,problem)
    for i in range(m):
        fpbest[i]=benchi_f(pbest[:, i],problem)
        if fpbest[i] < fgbest:
            gbest=pbest[:, i]
            fgbest=fpbest[i]
    # -----------------------------------------
    for k in range(k_max):
        for i in range(m):
            v[:, i] = w * v[:, i] + c1 * random.rand() * (pbest[:, i] - x[:, i]) + c2 * random.rand() * (gbest - x[:, i])
            x[:, i] = x[:, i] + v[:, i]
        temp_fpbest=np.zeros(m)
        for i in range(m):
            temp_fpbest[i]=benchi_f(x[:, i],problem)
            if temp_fpbest[i] < fpbest[i]:
                pbest[:, i] = x[:, i]
                fpbest[i] = temp_fpbest[i]
                if temp_fpbest[i] < fgbest :
                    gbest = x[:, i]
                    fgbest = temp_fpbest[i]
        test[:,:,k] = x
       