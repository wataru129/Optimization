# -*- coding: utf-8 -*-
import numpy as np
# 初期化#######################################################################
def init(current_sample_point,dimension,upper_limit,lower_limit,sample_x):
# 初期サンプル点の生成-----------------------------------------------------
    for i in range(current_sample_point):
        for j in range(dimension):            
             sample_x[i,j] = (upper_limit[j]-lower_limit[j])*np.random.rand()+lower_limit[j]
#-----------------------------------------------------------------------
    return sample_x
######################################################################################