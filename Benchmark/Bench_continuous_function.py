import math


def benchi_f(x,problem):
#ベンチマーク問題
    n=int(x.shape[0]) #xの次元
    out=0
    if problem == 1: #対象2
        for i in range(n):
            out = out + x[i]**2
    elif problem == 2: #対象2
        for i in range(n-1):
           out=out+(100*((x[i]**2-x[i+1])**2)+(1-x[i])**2)
    elif problem == 3: #対象3
        for i in range(n):
            out=out+(x[i]**4-16*x[i]**2+5*x[i])
    elif problem == 4: #対象4
       for i in range(n):
           out=out+(x[i]**2-10*math.cos(2*math.pi*x[i])+10)
    elif problem == 5: #対象5
       for i in range(n):
           tmp=0
           for j in range(i):
               tmp=tmp+x[j]
           out=out+tmp**2
    return out


