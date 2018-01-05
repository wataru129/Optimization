#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:42:36 2017

@author: wataru
"""

import numpy as np
import scipy.io as spio
import bench
np.set_printoptions(threshold=np.inf)#show all data of array


f_number = 3
# Load initial point from Initialpoint.mat
if f_number == 1:
    initial = spio.loadmat("initial_solution_20bit.mat")
elif f_number == 2:
    initial = spio.loadmat("initial_solution_50bit.mat")
else:
    initial = spio.loadmat("initial_solution_100bit.mat")

p, w, weight_limit, bit = bench .bench(f_number)
w       = np.array(w)    #重量
p       = np.array(p)    #価値
w_t     = w.T            #計算のため転置
p_t     = p.T            #計算のため転置

S_max   = 50
G_max   = 10 * bit  # 反復回数
answer  = np.zeros([S_max])
L       = 5
one    = np.ones([1, bit])
# Start Local Search Algolithm
# Step0[Prepare]
T      = np.zeros([L])
N       = np.zeros([bit, bit])  #近傍
win_x   = np.zeros([bit])       #世代での暫定的な最良解
fw      = np.zeros([bit])         #重さの合計
fp      = np.zeros([bit])         #価値の合計
# Step1[Initial point]
x_all = initial['initial_solution']
hyouka=0
for S in range(S_max):
    count=0
    x     = x_all[S, :]
    zantei = 0
    l = 0 #タブーリストの長さ調整パラメータ
    for G in range(G_max):
        win     = np.zeros([1])
# step2[Make neighborhood]
        tmp = x #近傍生成のための解
        for j in range(bit):
            kai=0            
            N[j, :] = x
            N[j,j]=N[j,j]-1
            N=np.absolute(N)
            kai = N[j, :].dot(p_t)
            for i in range(L):
                if kai == T[i]:
 #                   print(kai)
                    N[j, :] = one
                    count -= 1
                    break
# step3[Find best answer]
#        for j in range(bit): #願望条件の中での最良解を見つける処理
            fw[j] = N[j, :].dot(w)
            fp[j] = N[j, :].dot(p_t)
            count += 1
            if fw[j] > weight_limit:
                fp[j] = -fp[j]
            if fp[j] >= win:
                win = fp[j]
                win_x = N[j, :]
        x = win_x
        if win > zantei:      #解の更新
            zantei = win
 #step4[Add Tabulist]  
        T[l] = win
        if l == L - 1:
            l = 0
        else:
            l = l + 1
    answer[S] = zantei
    hyouka += count
print(np.max(answer))
print(np.min(answer))
print(np.average(answer))
print(np.std(answer))
print(hyouka/50)