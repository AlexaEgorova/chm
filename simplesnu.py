import numpy as np
import sympy
from sympy import *
import matplotlib.pyplot as plt
import pandas as pd

def simplesnu(a, b, c):
    data = [[a, b, c]]
    for i in range(1, 10):
        x_prev, y_prev, z_prev = data[i-1][0], data[i-1][1], data[i-1][2]
        xk = fi1(x_prev, y_prev, z_prev)
        yk = fi2(x_prev, y_prev, z_prev)
        zk = fi3(x_prev, y_prev, z_prev)
        data.append([xk, yk, zk])
        
        
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    print(df)
    plt.subplot(1, 3, 1)
    plt.plot(df['x'], df['y'], marker = 'o')
    plt.subplot(1, 3, 2)
    plt.plot(df['y'], df['z'], marker = 'o')
    plt.subplot(1, 3, 3)
    plt.plot(df['x'], df['z'], marker = 'o')
    return(df)


def fi1(x, y, z):
    return ((1/18)*x**3 + (1/18)*y**3 + (1/9)*z + 3)

def fi2(x, y, z):
    return ((1/18)*x**3 - (1/18)*y**3 + (1/6)*z + 2)

def fi3(x, y, z):
    return((1/6)*x**2 - (1/3)*y + (1/20)*z)

k = np.array([-5, -3, 5])
simplesnu(k[0], k[1], k[2])
