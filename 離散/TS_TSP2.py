import numpy as np
import scipy.io as spio
import TSPbenchi
import matplotlib.pyplot as plt


f_number = 1
# Load initial point from Initialpoint.mat
if f_number == 1:
    initial = spio.loadmat("29.mat")
elif f_number == 2:
    initial = spio.loadmat("48.mat")
else:
    initial = spio.dloadmat("70.mat")

x, y,  number  = TSPbenchi .TSPbenchi(f_number)

city_xy=np.zeros([number,2])
city_xy[:, 0]=x
city_xy[:, 1]=y
initial_point_all = initial['initial_point']
one=np.ones([1,number])
zantei=np.zeros(50)
#order = list(np.random.permutation(29))

A=np.array([[0, 97, 205,139,86, 60, 220,65, 111,115,227,95, 82, 225,168,103,266,205,149,120,58, 257,152,52, 180,136,82, 34, 145],[
        0,0,129,103,71, 105,258,154,112,65, 204,150,87, 176,137,142,204,148,148,49, 41, 211,226,116,197,89, 153,124,74],[
        0,0,0,219,125,175,386,269,134,184,313,201,215,267,248,271,274,236,272,160,151,300,350,239,322,78, 276,220,60],[
        0,0,0,0,167,182,180,162,208,39, 102,227,60, 86, 34, 96, 129,69, 58, 60, 120,119,192,114,110,192,136,173,173],[
        0,0,0,0,0,51, 296,150,42, 131,268,88, 131,245,201,175,275,218,202,119,50, 281,238,131,244,51, 166,95, 69],[
        0,0,0,0,0,0,279,114,56, 150,278,46, 133,266,214,162,302,242,203,146,67, 300,205,111,238,98, 139,52, 120],[
        0,0,0,0,0,0,0,178,328,206,147,308,172,203,165,121,251,216,122,231,249,209,111,169,72, 338,144,237,331],[
        0,0,0,0,0,0,0,0,169,151,227,133,104,242,182,84, 290,230,146,165,121,270,91, 48, 158,200,39, 64, 210],[
        0,0,0,0,0,0,0,0,0,172,309,68, 169,286,242,208,315,259,240,160,90, 322,260,160,281,57, 192,107,90],[
        0,0,0,0,0,0,0,0,0,0,140,195,51, 117,72, 104,153,93, 88, 25, 85, 152,200,104,139,154,134,149,135],[
        0,0,0,0,0,0,0,0,0,0,0,320,146,64, 68, 143,106,88, 81, 159,219,63, 216,187,88, 293,191,258,272],[
        0,0,0,0,0,0,0,0,0,0,0,0,174,311,258,196,347,288,243,192,113,345,222,144,274,124,165,71, 153],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,144,86, 57, 189,128,71, 71, 82, 176,150,56, 114,168,83, 115,160],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,61, 165,51, 32, 105,127,201,36, 254,196,136,260,212,258,234],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,106,110,56, 49, 91, 153,91, 197,136,94, 225,151,201,205],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,215,159,64, 126,128,190,98, 53, 78, 218,48, 127,214],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,61, 155,157,235,47, 305,243,186,282,261,300,252],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,105,100,176,66, 253,183,146,231,203,239,204],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,113,152,127,150,106,52, 235,112,179,221],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,79, 163,220,119,164,135,152,153,114],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,236,201,90, 195,90, 127,84, 91],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,273,226,148,296,238,291,269],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,112,130,286,74, 155,291],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,130,178,38, 75, 180],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,281,120,205,270],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,213,145,36],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,94, 217],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,162],[
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

cost_matrix=A+A.T
    
    
def calculate_total(order, cost_matrix):
    idx_from = np.array(order)
    idx_to = np.array(order[1:] + [order[0]])
    result_arr = cost_matrix[idx_from, idx_to]

    return np.sum(result_arr)

def calculate_2opt_exchange_cost(order, i, j, cost_matrix):
    ###Calculate the difference of cost by applying given 2-opt exchange###
    number = len(order)
    a, b = order[i], order[(i + 1) % number]
    c, d = order[j], order[(j + 1) % number]

    cost_before = cost_matrix[a, b] + cost_matrix[c, d]
    cost_after = cost_matrix[a, c] + cost_matrix[b, d]
    return cost_after - cost_before

def apply_2opt_exchange(order, i, j):
    """Apply 2-opt exhanging on visit order"""
    tmp = order[i + 1: j + 1]
    tmp.reverse()
    order[i + 1: j + 1] = tmp

    return order

def improve_with_2opt(order, cost_matrix,count):
    """Check all 2-opt neighbors and improve the visit order"""
    number = len(order)
    cost_diff_best = 1000.0
    i_best, j_best = None, None

    for i in range(0, number - 2):
        for j in range(i + 2, number):
            if i == 0 and j == number - 1:
                continue
            cost_diff = calculate_2opt_exchange_cost(order, i, j, cost_matrix)
            count += 1
            for k in range(L):
                if np.allclose(np.array([i,j]),T[k,:]):
                    cost_diff=100000000000000
                    count -= 1
            if cost_diff < cost_diff_best:
                cost_diff_best = cost_diff
                i_best, j_best = i, j
    order_new = apply_2opt_exchange(order, i_best, j_best)
    T[l,:]=np.array([i_best, j_best])
    return order_new,count


def local_search(order, cost_matrix, improve_func,count):
    """Main procedure of local search"""
 #   cost_total = calculate_total_distance(order, cost_matrix)
    improved,count = improve_func(order, cost_matrix,count)
    order = improved

    return order,count

def visualize_visit_order(order, city_xy):
    """Visualize traveling path for given visit order"""
    route = np.array(order + [order[0]])  # add point of departure
    x_arr = city_xy[:, 0][route]
    y_arr = city_xy[:, 1][route]
    
    
    plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
    plt.rcParams['font.size'] = 20 #フォントサイズを設定
    plt.figure(figsize=(5,5), dpi=100)
    plt.plot(x_arr, y_arr, 'o-')
    plt.xlabel("x", fontsize=20)
    plt.ylabel("y", fontsize=20)
    plt.tick_params(labelsize=20)
    plt.subplots_adjust(left=0.2, bottom=0.2, right=0.9, top=0.9)
    plt.show()

L=5
S_max=50
G_max=50
T=np.zeros([L,2])
l=0
hyouka=0
for S in range(S_max):
    order   = initial_point_all[S, :]
    order = order-one
    order=list(order[0])
    order=np.array(order[:], dtype=np.int32)
    order=list(order)
    total_distance = calculate_total(order, cost_matrix)
   # print('初期解の総移動距離 = {}'.format(total_distance))
#    visualize_visit_order(order, city_xy)

# 近傍を計算
    count=0
    for G in range(G_max):
        improved,count = local_search(order, cost_matrix, improve_with_2opt,count)
        total_distance = calculate_total(improved, cost_matrix)
        if zantei[S] > total_distance:
            zantei[S]=total_distance
        l=l+1
        if l==L-1:
            l=0
        order=improved
#        if G==10:
#            visualize_visit_order(improved, city_xy)
    #print('近傍探索適用後の総移動距離 = {}'.format(total_distance))
    zantei[S]=total_distance
    hyouka += count
    
print(np.max(zantei))
print(np.min(zantei))
print(np.average(zantei))
print(np.std(zantei))
#visualize_visit_order(improved, city_xy)

#An=list([16,13,17,14,3,9,19,1,20,4,28,2,25,8,11,5,27,0,23,12,15,26,7,22,6,24,18,10,21])
#visualize_visit_order(An, city_xy)