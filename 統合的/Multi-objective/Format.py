# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 22:28:11 2017

@author: SYS2017B4-c
"""
import numpy as np
from matplotlib import pyplot

global dimension,current_sample_point

###############################
func_num = 2                     # 目的関数の数
dimension = 2                    # 次元
upper_limit=np.ones(dimension)   # 実行可能領域の上限
lower_limit=np.zeros(dimension)  # 実行可能領域の下限
init_sample_point   =100         # 初期サンプル点数
################################

# 初期化


sample_x = np.zeros((init_sample_point,dimension)) # サンプル点決定変数配列
sample_x_value = np.array([])                      # サンプル点評価値配列
real_archive    = np.array([])                     # 決定変数配列
real_archive_value = np.array([])                  # 実関数の評価値配列
fitting_count = 1                                  # 応答曲面フィッティング回数初期化
current_sample_point = init_sample_point           # 初期サンプル点数

# 初期サンプル点の生成-----------------------------------------------------
for i in range(current_sample_point):
    for j in range(dimension):
             #sample_x(i,j) = (upper_limit(1,j)-lower_limit(1,j))*sample_RANDOM_X(i,j,run)+lower_limit(1,j);
             sample_x[i,j] = (upper_limit[j]-lower_limit[j])*np.random.rand()+lower_limit[j]
#-----------------------------------------------------------------------
temp_x = sample_x        # 評価値呼び出し用決定変数
#function_call             # 評価値呼び出し

pyplot.scatter(sample_x[:,0],sample_x[:,1])
pyplot.show()