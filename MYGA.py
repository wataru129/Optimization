from numpy.random import *
import numpy as np
from scipy.io import loadmat
import scipy.io as spio
from numpy import linalg as la
import bench
np.set_printoptions(threshold=np.inf)

f_number = 1
initial = spio.loadmat("initial_solution_20bit.mat")   #Load initial point from Initialpoint.mat
p, w, weight_limit, m = bench.bench(f_number)
w = np.array(w)
p = np.array(p)
w_t = w.T
p_t = p.T
#Step0[Prepare]#
CR = 0.5     #The probability of crossover
MU = 0.5     #The probability of mutation
G_max = 100     #The max of generation
A = 10         #The number of battle
#####Step1[Initial point]#############
x_i = initial['initial_solution']
#####Step2[crossover]#############
x_a = np.zeros([20, 20])
x_b = np.zeros([20, 20])
c_a = np.zeros([20, 20])
c_b = np.zeros([20, 20])
m_a = np.zeros([20, 20])
m_b = np.zeros([20, 20])
al = np.zeros([40, 20])
s = np.zeros([A, 20])
fw = np.zeros([A])
fp = np.zeros([A])

for G in range(G_max):
    for j in range(m):
        r = np.random.randint(1, m, 2)  # Select random 2 Parents
        x_a[j, :] = x_i[r[0], :]
        x_b[j, :] = x_i[r[1], :]
        for i in range(m):
            rr=rand()
            if rr < CR or j == r[0]:
                c_a[j, i] = x_b[j, i]
            else:
                c_a[j, i] = x_a[j, i]
            if rr < CR or j == r[1]:
                c_b[j, i] = x_a[j, i]
            else:
                c_b[j, i] = x_b[j, i]
#####Step3[mutation]#############
            rr = rand()
            if c_a[j, i] == 1:
                if rr < MU:
                    m_a[j, i] = 0
                else:
                    m_a[j, i] = 1
            else:
                if rr < MU:
                    m_a[j, i] = 1
                else:
                    m_a[j, i] = 0
            if c_b[j, i] == 1:
                if rr < MU:
                    m_b[j, i] = 0
                else:
                    m_b[j, i] = 1
            else:
                if rr < MU:
                    m_b[j, i] = 1
                else:
                    m_b[j, i] = 0
#######step4[select]#########
    al = np.r_[m_a, m_b]
    for j in range(m):
        r = np.random.randint(0 ,2*m, A)  # Select random 2 Parents
        win = 0
        win_x = s[0, :]
        for k in range(A):
            s[k,:]=al[r[k],:]
            fw[k] = s[k,:].dot(w_t)
            fp[k] = s[k,:].dot(p_t)
            if fw[k] > weight_limit:
                fp[k] = 0
            if fp[k] >= win:
                win=fp[k]
                win_x=s[k,:]
        x_i[j, :]=win_x
        print(fp)


f1 = x_i[3,:].dot(w_t)
f2 = x_i[3,:].dot(p_t)
print(f1)
print(f2)
print(fp)