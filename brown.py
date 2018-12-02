import numpy as np
import sympy
from sympy import *

def brown(a, b):
    e = 1e-3
    p_prev, q_prev = 1, 1
    xk, yk = a, b
    while(max(abs(p_prev), abs(q_prev)) >= e):
        xk_wave = xk - f(xk, yk)/diffs('f_x').evalf(subs={'x': xk, 'y': yk})
        
        qk = g(xk_wave, yk) * diffs('f_x').evalf(subs={'x': xk, 'y': yk}) / (
                 diffs('f_x').evalf(subs={'x': xk, 'y': yk}) * 
                 diffs('g_y').evalf(subs={'x': xk_wave, 'y': yk}) - 
                 diffs('f_y').evalf(subs={'x': xk, 'y': yk}) * 
                 diffs('g_x').evalf(subs={'x': xk_wave, 'y': yk}))
        
        pk = (f(xk, yk) - qk * diffs('f_y').evalf(subs={'x': xk, 'y': yk})) / (
                 diffs('f_x').evalf(subs={'x': xk, 'y': yk}))
        
        p_prev, q_prev = pk, qk
        xk = xk - pk
        yk = yk - qk
    print(xk, yk)

'''def f(x, y):
    return (x + y - 15.)

def g(x, y):
    return (x**2 + y**2 - 127.)

def diffs(d):
    x = Symbol('x')
    y = Symbol('y')
    dic = {
        'f_x': diff(x + y, x),
        'f_y': diff(x + y, y),
        'g_x': diff(x**2 + y**2, x),
        'g_y': diff(x**2 + y**2, y)}
    return(dic[d])'''

def f(x, y):
    return (x*y - 2*x - 11.)

def g(x, y):
    return (y**3 - x)

def diffs(d):
    x = Symbol('x')
    y = Symbol('y')
    dic = {
        'f_x': diff(x*y - 2*x, x),
        'f_y': diff(x*y - 2*x, y),
        'g_x': diff(y**3 - x, x),
        'g_y': diff(y**3 - x, y)}
    return(dic[d])

k = np.array([-8., -10.])
brown(k[0], k[1])

