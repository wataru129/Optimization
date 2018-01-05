# -*- coding: utf-8 -*-
import numpy as np
#ベンチマーク問題(ZDT1)------------------------------------------------------------
def benchmark(temp_x,dimension):
    sample_x_value = np.zeros((temp_x.shape[0],2))
    for size_x in range(temp_x.shape[0]):
        sample_x_value[size_x, 0] = temp_x[size_x, 0] # f1(x)評価値
        multi_g = 1 + 9 / (dimension-1) * sum(temp_x[size_x,2:-1])
        multi_h = 1 - (temp_x[size_x,1] / multi_g) ** 0.5
        sample_x_value[size_x,1] = multi_g * multi_h # f2(x)評価値
        return sample_x_value
#-----------------------------------------------------------------------