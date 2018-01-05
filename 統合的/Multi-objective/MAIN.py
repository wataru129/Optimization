# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:48:12 2017
This is my Intergreation Optimization
@author: SYS2017B4-c
"""
import init , zdt1, RBFN_original,evaluation
import numpy as np

#統合的最適化パラメータ設定################################################
func_num = 2                     # 目的関数の数
dimension = 2                    # 次元
upper_limit=np.ones(dimension)   # 実行可能領域の上限
lower_limit=np.zeros(dimension)  # 実行可能領域の下限
initial_sample_points   =100         # 初期サンプル点数
#初期化----------------------------------------------------------------------
sample_x = np.zeros((initial_sample_points,dimension)) # サンプル点決定変数配列
sample_ｆx = np.array([])                      # サンプル点評価値配列
decison_values    = np.array([])                     # 決定変数配列
real_decison_values = np.array([])                  # 実関数の評価値配列
fitting_counter = 1                                  # 応答曲面フィッティング回数初期化
current_sample_point = initial_sample_points           # 初期サンプル点数を代入
#---------------------------------------------------------------------------

#初期点作成
sample_x = init.init(current_sample_point,dimension,upper_limit,lower_limit,sample_x)
temp_x = sample_x          # 評価値呼び出し用決定変数
#評価値呼び出し
sample_x_value = zdt1.benchmark(temp_x,dimension)
#応答局面作成
sample_point_fill,W,teacher_num,r = RBFN_original.RBFN(sample_x_value,current_sample_point,func_num,sample_x,dimension)
#応答局面の評価値呼び出し
out = evaluation.evaluation(sample_point_fill,W,teacher_num,r,temp_x,func_num,dimension,sample_x)





#x = temp_x
#y = out
#pyplot.plot(x, y)  # "r"はredの省略
