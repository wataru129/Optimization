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

f_number = 2
# Load initial point from Initialpoint.mat
if f_number == 1:
    initial = spio.loadmat("initial_solution_20bit.mat")
elif f_number == 2:
    initial = spio.loadmat("initial_solution_50bit.mat")
else:
    initial = spio.loadmat("initial_solution_100bit.mat")

p, w, weight_limit, bit = bench .bench(f_number)
w       = np.array(w)
p       = np.array(p)
w_t     = w.T
p_t     = p.T

S_max   = 20
answer  = np.zeros([S_max])
# Start Genetic Algolithm
# Step0[Prepare]
for S in range(1):
    m       = 20
    G_max   = 20 * bit  # The max of generation
# Step1[Initial point]
    x_all = initial['initial_solution']
    r = np.random.randint(1, 1900)  # Make random
    x_i     = np.zeros([20, bit])
    for j in range(r,r + m):
        x_i[j-r, :]=x_all[j,:]
# Step2[crossover]
    x_a     = np.zeros([20, bit])
    x_b     = np.zeros([20, bit])
    m_a     = np.zeros([20, bit])
    m_b     = np.zeros([20, bit])
    al      = np.zeros([40, bit])
    s       = np.zeros([A, bit])
    win_x   = np.zeros([20, bit])
    fw      = np.zeros([m])
    fp      = np.zeros([m])
    zantei  = np.zeros([1, G_max])
    for G in range(G_max):
        zantei[0, G] = 0
        for j in range(m):
            r1 = np.random.randint(1, m, 2)  # Make random
            x_a[j, :] = x_i[r1[0], :]
            x_b[j, :] = x_i[r1[1], :]
            if np.random.rand() <= PC:
                n = np.random.randint(1, bit)
                for i in range(n, bit):
                    if np.random.rand() < CR or j == r1[0]:
                        x_a[j, i] = x_b[j, i]
                    else:
                        x_a[j, i] = x_a[j, i]
                    if np.random.rand() < CR or j == r1[1]:
                        x_b[j, i] = x_a[j, i]
                    else:
                        x_b[j, i] = x_b[j, i]
# Step3[mutation]
            for i in range(1, bit):
                if x_a[j, i] == 1:
                    if np.random.rand() < PM:
                        m_a[j, i] = 0
                    else:
                        m_a[j, i] = 1
                else:
                    if np.random.rand() < PM:
                        m_a[j, i] = 1
                    else:
                        m_a[j, i] = 0
                if x_b[j, i] == 1:
                    if np.random.rand() < PM:
                        m_b[j, i] = 0
                    else:
                        m_b[j, i] = 1
                else:
                    if np.random.rand() < PM:
                        m_b[j, i] = 1
                    else:
                        m_b[j, i] = 0
# step4[select]
        al = np.r_[m_a, m_b]
        win = np.zeros([1, 20])
        for j in range(m):
            r2 = np.random.randint(0, 2 * m, A)
            win_x[j, :] = s[0, :]
            for k in range(A):
                s[k, :] = al[r2[k], :]
                fw[j] = s[k, :].dot(w)
                fp[j] = s[k, :].dot(p_t)
                if fw[j] > weight_limit:
                    fp[j] = -fp[j]
                if fp[j] >= win[0, j]:
                    win[0, j] = fp[j]
                    win_x[j, :] = s[k, :]
            x_i[j, :] = win_x[j, :]
            if win[0, j] > zantei[0, G]:
                zantei[0, G] = win[0, j]
    answer[S] = np.max(zantei)
print(np.max(answer))
print(np.min(answer))
print(np.average(answer))
print(np.std(answer))