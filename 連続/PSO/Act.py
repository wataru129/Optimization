from math import sqrt


def activity(v, m, n):
    act = 0
    for i in range(m):
        tmp = 0
        for j in range(n):
            tmp=tmp + v[j, i]**2
        act = act + tmp
#    plot_gbest(k)=benchi_f(gbest)
    act = sqrt(act / (m * n))
    return act
