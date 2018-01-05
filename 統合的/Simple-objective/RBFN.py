# -*- coding: utf-8 -*-
import numpy as np
import math
import scipy.io as spio
from numpy.linalg import inv



def hyouka(x,dimension):
    answer=0
    for i in range(dimension-1):
           answer = answer+(100*((x[i]**2-x[i+1])**2)+(1-x[i])**2)
    return answer




#init------------------------------------------------------------------------
sample_kazu = 300
dimension = 2
y_teacher_value=np.zeros(sample_kazu)  
H=np.zeros((sample_kazu,sample_kazu))   #H行列の初期化
sample_value=np.zeros(sample_kazu)
d_max=0                                 #サンプル点間の最大距離の初期化
sample_kyori=np.zeros((sample_kazu,sample_kazu)) #サンプル点間の各距離の行列の初期化
#----------------------------------------------------------------------- 

#create initial point--------------------------------
initial=spio.loadmat("InitialPoints_300_100_100.mat")
initial_points = initial['IP']
x = 5 * initial_points[0:sample_kazu, 0:dimension,0].T 
seikiten = 5 * initial_points[0:sample_kazu, 0:dimension,0].T 
for i in range(sample_kazu):
    sample_value[i] = hyouka(x[:,i],dimension)
#------------------------------------------------------

######################パラメータ設定開始########################
sample_value_max=max(sample_value)
for h in range(sample_kazu):
    y_teacher_value[h]=sample_value[h]-sample_value_max
#####################パラメータ設定の終了###################

#############　サンプル点間最大距離の計算開始　##############
for j in range(sample_kazu-1):
    for j1 in range(j+1,sample_kazu):
        sample_kyori[j,j1]=sum(np.square(seikiten[:,j]-seikiten[:,j1]))
d_max=math.sqrt(np.amax(sample_kyori))                             #サンプル点間の最大距離
#############　サンプル点間最大距離の計算終了　##############

#############　基底関数半径ｒの計算開始　##############
r=d_max/(np.sqrt(sample_kazu*dimension)**(1/dimension))
if r==0:
    r=0.5
#############　基底関数半径ｒの計算終了　##############

#############　基底関数計算開始　##############
for j in range(sample_kazu):
    for j1 in range(sample_kazu):
        H[j,j1]= sum(np.square(seikiten[:,j]-seikiten[:,j1]))
        H[j,j1]= math.exp(-H[j,j1]/(np.square(r)))
###############　基底関数計算終了　##############

###############　ωの計算開始　##############
ramda_element = math.pow(10,-2)                                        #ラムダの設定
ramda = ramda_element *np.eye(sample_kazu,sample_kazu)                     #ラムダの行列
A= H.T * H + ramda
omega = inv(A) * H.T * y_teacher_value                                            #重み値ωの設定
###############　ωの計算終了　##############

###############　出力関数O(x)　##############
out=np.zeros(sample_kazu);
for i in range(dimension):
    for k1 in range(sample_kazu):
        out[i]=out[i]+omega[k1,1]*math.exp(- sum((x[:,i]-seikiten[:,k1])**2) / (r**2));
###############　出力関数O(x)　##############
