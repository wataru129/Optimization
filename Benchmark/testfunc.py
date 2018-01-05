# -*- coding: utf-8 -*-

import numpy as np
import math

#x =np.ones((1,5))
x = np.arange(1)
#x=np.reshape(x,(6,2))
print(x.shape)
r = 2
[m, n] = x.shape
gx = np.zeros((m, 1))
fx = np.zeros((m, r))
print(m)
print(n)
print(fx)

for i in range(m):
    fx[i, 0] = x[i, 0]
    gx = (1 + 9 * sum(x[i, 1:-1]) / (n - 1))
    fx[i, 1] = gx * (1 - math.sqrt(x[i, 0] / (gx)))
  #  countfx += 1

print(fx)