# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:46:40 2017

@author: SYS2017B4-c
"""
import numpy as np
import math

def evaluation(sample_point_fill,W,teacher_num,r,temp_x,func_num,dimension,sample_x):
    out= np.zeros((temp_x.shape[0],func_num))
    for func in range(func_num):
        for size_x in range(temp_x.shape[0]):
            reserve=0
            for sample_num in range(sample_point_fill):
                for dim in range(dimension):
                    reserve = reserve + ( temp_x[size_x,dim] - sample_x[teacher_num[sample_num]-1,dim] )**2 
                out[size_x,func] = out[size_x,func] + W[func,sample_num]*math.exp( (-1) * ( reserve / (r**2) ) )
                reserve=0
    return out