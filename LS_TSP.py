import numpy as np
import scipy.io as spio
import TSPbenchi
np.set_printoptions(threshold=np.inf)#show all data of array


f_number = 1
# Load initial point from Initialpoint.mat
if f_number == 1:
    initial = spio.loadmat("initial_solution_29.mat")
elif f_number == 2:
    initial = spio.loadmat("initial_solution_48.mat")
else:
    initial = spio.dloadmat("initial_solution_70.mat")

x, y,  number  = TSPbenchi .TSPbenchi(f_number)

x      = np.array(x)    #重量
#y       = np.array(y)    #価値
#x_t     = x.T            #計算のため転置
#y_t     = y.T            #計算のため転置
#initial_point_all = initial['initial_solution']
#order   = initial_point_all[1, :,1]
order = list(np.random.permutation(number))

def cost_matlix(number,x):
    cost = np.zeros([number,number])
    for i in range (number):
        for j in range(number):
            cost[i][j]=x[i]-x[j]
    cost=np.absolute(cost)
    return cost

def calculate_total(order, cost):
    idx_from = np.array(order)
    idx_to = np.array(order[1:] + [order[0]])
    result_arr =cost[idx_from, idx_to]
    return np.sum(result_arr)

def calculate_2opt_exchange_cost(visit_order, i, j, cost):
    ###Calculate the difference of cost by applying given 2-opt exchange###
    number = len(visit_order)
    a, b = visit_order[i], visit_order[(i + 1) % number]
    c, d = visit_order[j], visit_order[(j + 1) % number]

    cost_before = cost[a, b] + cost[c, d]
    cost_after = cost[a, c] + cost[b, d]
    return cost_after - cost_before

def apply_2opt_exchange(visit_order, i, j):
    """Apply 2-opt exhanging on visit order"""

    tmp = visit_order[i + 1: j + 1]
    tmp.reverse()
    visit_order[i + 1: j + 1] = tmp

    return visit_order

def improve_with_2opt(visit_order, cost):
    """Check all 2-opt neighbors and improve the visit order"""
    number = len(visit_order)
    cost_diff_best = 0.0
    i_best, j_best = None, None

    for i in range(0, number - 2):
        for j in range(i + 2, number):
            if i == 0 and j == number - 1:
                continue

            cost_diff = calculate_2opt_exchange_cost(
                visit_order, i, j, cost)

            if cost_diff < cost_diff_best:
                cost_diff_best = cost_diff
                i_best, j_best = i, j

    if cost_diff_best < 0.0:
        visit_order_new = apply_2opt_exchange(visit_order, i_best, j_best)
        return visit_order_new
    else:
        return None


cost=cost_matlix(number,x)
result=calculate_total(order, cost)