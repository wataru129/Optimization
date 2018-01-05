from numpy import random
import numpy as np
import sys
sys.path.append('C:\\Users\SYS2017B4-c.DESKTOP-1LG9001\Desktop\graduation research\graduate\Benchmark')
from Bench_continuous_function import benchi_f


def update_x_v(x, v, pbest, gbest, m, n, c1, c2, w):
    for i in range(m):
        for j in range(n):
            v[j, i]= w * v[j, i]  \
                + c1 * random.rand() * (pbest[j, i] - x[j, i]) \
                + c2 * random.rand() * (gbest[j] - x[j, i])
            x[j, i] = x[j, i] + v[j, i]
    return x, v


def update_p_gbest(x, m, pbest, gbest, fpbest, fgbest,problem):
    temp_fpbest=np.zeros(m)
    for i in range(m):
        temp_fpbest[i]=benchi_f(x[:, i],problem)
        if temp_fpbest[i] < fpbest[i]:
            pbest[:, i] = x[:, i]
            fpbest[i] = temp_fpbest[i]
            if temp_fpbest[i] < fgbest :
                gbest = x[:, i]
                fgbest = temp_fpbest[i]
    return pbest, gbest, fpbest, fgbest
