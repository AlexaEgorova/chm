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
    print(c[::-1])
    return c
    
        
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
print(orts)

plt.plot(x, y)
plt.plot(f)
plt.show()
df = pd.DataFrame(x, columns=['x'])
df.insert(1, 'y', y)
df.insert(2, 'c', c[::-1])
df.insert(3, 'fi', orts[::-1])
df
