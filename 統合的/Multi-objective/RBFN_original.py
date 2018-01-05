# -*- coding: utf-8 -*-
import numpy as np
#from matplotlib import pyplot
import math

global dimension,current_sample_point


#応答局面生成##############################################################
def RBFN(sample_x_value,current_sample_point,func_num,sample_x,dimension):
#RBFNのパラメータ---------
    lamda = 1.0 + 10 **(-2)
#---------------------
    sample_point_fill = current_sample_point
    teacher_num = np.arange(1,current_sample_point+1)
    teacher_data = np.zeros((func_num,current_sample_point)).T
    for func in range(func_num):
        max_data = max(sample_x_value[func,:])
        teacher_data[func,:] = sample_x_value[func,:] - max_data

#サンプル点間最大距離------------------------------------------------------
    compute_dmax=np.zeros((sample_point_fill,sample_point_fill))
    for p in range(sample_point_fill-1):
        for t in range(p+1,sample_point_fill-1):
            compute_dmax[p,t] = sum( ( sample_x[teacher_num[p],:]-sample_x[teacher_num[t],:] )**2 )
            compute_dmax[t,p] = compute_dmax[p,t]
    d_max = math.sqrt(compute_dmax.max())
    r=d_max/(math.sqrt(dimension-1)*(sample_point_fill**(1/(dimension-1))) )
#-----------------------------------------------------------------------

    if r == 0:
        r = 0.2
    H=np.zeros((sample_point_fill,sample_point_fill)) # H行列
    L=np.zeros((sample_point_fill,sample_point_fill)) # Λ行列
    for i in range(sample_point_fill):
        for j in range(sample_point_fill):
            for k in range(dimension):
                H[i,j] = H[i,j] + ( sample_x[i,k] - sample_x[j,k] )**2 
            H[i,j] = math.exp( (-1) * ( H[i,j] / (r**2) ) )
    L = lamda * np.eye(sample_point_fill)
    W = np.empty([0,100])
    for func in range(func_num):
        A = H.T * H + L
        A = np.linalg.inv(A)
        W_f=A * (H.T) * (teacher_data[:,func])
        W = np.r_[W , W_f]
    return sample_point_fill,W,teacher_num,r
##############################################################################
