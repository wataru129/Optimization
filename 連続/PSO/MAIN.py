# -*- coding: utf-8 -*-
import numpy as np
import region
import scipy.io as spio
import update
#from plot import plot
import sys
import all
sys.path.append('C:\\Users\SYS2017B4-c.DESKTOP-1LG9001\Desktop\graduation research\graduate\Benchmark')

from Bench_continuous_function import benchi_f


initial=spio.loadmat("InitialPoints_300_100_100.mat")
IP = initial['IP']

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
k_max = 100  # Max of reiteration
# ----------------------------------


for S in range(T):
    print("START")
    # Reset of initial value---------------------------
    r1, r2 = region.region(problem)   # Area of x
    x = r2 * IP[0:m, 0:n, S].T    # initial point r2=(|r1|     +     |r2|)/2
    v = IP[0:m, 0:n, S].T         # initial velocity
    pbest = x               # Best x in the diviual particle
    fpbest=np.zeros(m)
    gbest=pbest[:,0]
    fgbest = benchi_f(gbest,problem)
    for i in range(m):
        fpbest[i]=benchi_f(pbest[:, i],problem)
        if fpbest[i] < fgbest:
            gbest=pbest[:, i]
            fgbest=fpbest[i]
    # -----------------------------------------
    for k in range(k_max):
        x, v = update.update_x_v(x, v, pbest, gbest, m, n, c1, c2, w)
        pbest, gbest, fpbest, fgbest \
            = update.update_p_gbest(x, m, pbest, gbest, fpbest, fgbest,problem)
        #print(x[:,0])
        #print(fpbest[0])
#plot()
all