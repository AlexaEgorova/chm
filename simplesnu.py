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
    plt.subplot(3, 1, 1)
    plt.plot(df['x'], df['y'], marker = 'o')
    plt.subplot(3, 1, 2)
    plt.plot(df['y'], df['z'], marker = 'o')
    plt.subplot(3, 1, 3)
    plt.plot(df['x'], df['z'], marker = 'o')
    return(df)


def fi1(x, y, z):
    return (x**3 + y**2 + 7*z**4 - 1)

def fi2(x, y, z):
    return (x + 2*z)

def fi3(x, y, z):
    return((x - y - 8*z)**4)

k = np.array([-0.99, -0.99, 0.0001])
simplesnu(*k)
