import numpy as np
import copy

def det(a1):
    a=copy.copy(a1)
    res = 1
    n = len(a)
    for i in range(n):
        j = max(range(i,n), key=lambda k: abs(a[k][i]))
        if i != j:
            a[i],a[j] = a[j],a[i]
            res *= -1
        if a[i][i] == 0:
            return 0
        res *= a[i][i]
        for j in range(i+1,n):
            b = a[j][i] / a[i][i]
            a[j] = [a[j][k]-b*a[i][k] for k in range(n)]
    return res


def kramer(a, v):
    n=len(a)
    x=np.ones(n)
    deltas=np.ones(n)
    M = copy.copy(a)
    M_t = np.transpose(M)
    delta=det(M)
    
    for i in range(0,n):
        M_t[i]=copy.copy(v)
        deltas[i] = det(M_t)
        x[i]=deltas[i]/delta
        print("x[", i, "] =", x[i])
    return x

def relax():
    pass

#a = [(2,5),(1,-10)]
a = np.array([[2.,5.],[1.,-10.]])
v = [1.,3.]
M = copy.copy(a)
print(det(M))

kramer(a, v)
