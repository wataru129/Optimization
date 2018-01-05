# -*- coding: utf-8 -*-
import numpy as np
"""
make pubolec
"""
import math
"""
数学module
"""
global countfx




def mofunc(problem, x, r):
    """
     多目的用ベンチマーク問題集　連続関数編
     引数
         FUNnum : 問題番号
         r : 目的数
     戻り値
        fx : 目的関数値ベクトル
        gx : パレートフロンティアからの距離
    """
    [m, n] = x.shape
    gx = np.zeros(m, 1)
    fx = np.zeros(m, r)
    print(problem)
    print(x)
    print(r)
#    if problem == 1:
    for i in range(m):
         fx[i, 1] = x[i, 1]
         gx = (1 + 9 * sum(x[i, 2:-1]) / (n - 1))
         fx[i, 2] = gx * (1 - math.sqrt(x[i, 1] / (gx)))
         countfx += 1
    return fx
#    elif problem == 2:
 #       for i in range(m):
  #         gx = (1 + 9 * sum(x[i, 2:-1]) / (n - 1))
   #         fx[i, 2] = gx * (1 - (x[i, 1] / (gx))**2)
   #         countfx += 1
   #         return fx
   # else:
   #     k=0
   #     return k
            
y=np.ones((2,2)
mofunc(1, y, 1)