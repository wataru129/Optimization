#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:42:36 2017

@author: wataru
"""

import numpy as np
import scipy.io as spio
import bench
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)#show all data of array


f_number = 1
# Load initial point from Initialpoint.mat
if f_number == 1:
    initial = spio.loadmat("initial_solution_20bit.mat")
elif f_number == 2:
    initial = spio.loadmat("initial_solution_50bit.mat")
else:
    initial = spio.loadmat("initial_solution_100bit.mat")

def visualize_visit_order(graph):
    """Visualize traveling path for given visit order"""
    x_arr = graph[0, :]
    y_arr = graph[1, :]
    
    
    plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
    plt.rcParams['font.size'] = 20 #フォントサイズを設定
    plt.figure(figsize=(5,5), dpi=100)
    plt.plot(x_arr, y_arr, 'o-')
    plt.xlabel("TL", fontsize=20)
    plt.ylabel("f(x)", fontsize=20)
    plt.tick_params(labelsize=20)
    plt.subplots_adjust(left=0.2, bottom=0.2, right=0.9, top=0.9)
    plt.show()






p, w, weight_limit, bit = bench .bench(f_number)
w       = np.array(w)    #重量
p       = np.array(p)    #価値
w_t     = w.T            #計算のため転置
p_t     = p.T            #計算のため転置

S_max   = 50
G_max   = 10 * bit  # 反復回数
answer  = np.zeros([S_max])
one    = np.ones([1, bit])
# Start Local Search Algolithm
# Step0[Prepare]
graph       = np.zeros([2, bit])
N       = np.zeros([bit, bit])  #近傍
win_x   = np.zeros([bit])       #世代での暫定的な最良解
fw      = np.zeros([bit])         #重さの合計
fp      = np.zeros([bit])         #価値の合計
# Step1[Initial point]
x_all = initial['initial_solution']
hyouka=0
for k in range(bit):
    L=k+1
    T      = np.zeros([L])
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
                N[j, :] = x
                N[j,j]=N[j,j]-1
                N=np.absolute(N)
                for i in range(L):
                    if j==T[i]:
                        N[j, :] = one
                        count -= 1
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
                    T[l] = j
            x = win_x
            if win > zantei:      #解の更新
                zantei = win
 #step4[Add Tabulist]  
            if l == L - 1:
                l = 0
            else:
                l = l + 1
        answer[S] = zantei
        hyouka += count
        
    graph[:,k]=[L,np.average(answer)]
visualize_visit_order(graph)