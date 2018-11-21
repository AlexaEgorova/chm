import numpy as np
import math as m

def norm(x):
    return m.sqrt(sum([x_i**2 for x_i in x]))

def simple(a, b, x0=None): 
    e = 1e-3
    if len(a) != len(a[0]) or len(a) != len(b): 
        return None 
    x = x0 
    if x0 is None: 
        x = b.copy() 
    r = b - np.dot(a, x) 
    while norm(r) > e: 
        x += r 
        r = (b - np.dot(a, x)) / np.diag(a)
    print(x)
    return x
    

a = np.array([[8., 0., -12.], [0., 51., 12.], [-12., 12., 24.]])
v = np.array([58., -41., 88.])

simple(a, v)
