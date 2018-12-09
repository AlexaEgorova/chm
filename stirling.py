import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import pandas as pd
import math

def mnk(x, y):
    n = len(x)
    A = np.zeros((n, n))
    g = np.zeros(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                A[i][j] += ort(i, x[k]) * ort(j, x[k])
            g[i] += ort(i, x[j]) * y[j]
    B = np.linalg.inv(A)
    c = np.dot(B, g)
    return c

def stirling(x, y, a):
    h = 0.01
    n = len(x)
    A = np.array([y[0], a[1]*h, a[2]*(h**2), a[3]*(h**3), a[4]*(h**4)])
    deltas = np.array([1, A[1]+A[3], 2*A[2]+2*A[4], 6*A[3], 24*A[4]])
    ans = np.array([y[0], deltas[1], deltas[2]/2, deltas[3]/6, deltas[4]/24])
    return ans
        
def ort(deg, x):
    return x**deg
        
x = [0., 1., 2., 4., 5.]
y = [2.1, 2.4, 2.6, 2.8, 3]

c = mnk(x, y)

f = []
for i in x:
    f.append((i+1)**(1/2) + 1)
    
orts = []
for i in range(len(x)):
    if i == 0: 
        orts.append('1')
    else:
        orts.append('x^%i' % i)

ts = ['1', 't', 't**2', 't*(t-1)*(t+1)', '(t**2)*(t-1)*(t+1)']
s = stirling(x, y, c)

for i in range(len(x)):
    print(s[i], '*', ts[i], '+')

plt.plot(x, y)
plt.plot(f)
plt.show()
df = pd.DataFrame(x, columns=['x'])
df.insert(1, 'y', y)
df.insert(2, 'c', c[::-1])
df.insert(3, 'fi', orts[::-1])
df
