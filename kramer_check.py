import numpy as np


def det(a1):
    a = np.array([[j for j in i] for i in a1])
    res = 1
    n = len(a)
    for i in range(n):
        j = max(list(range(i, n)))
        if i != j:
            a[i], a[j] = a[j].copy(), a[i].copy()
            res *= -1
        if a[i][i] == 0:
            return 0
        res *= a[i][i]
        for j in range(i+1, n):
            b = a[j][i] / a[i][i]
            a[j] = [a[j][k] - b*a[i][k] for k in range(n)]
    return res


def kramer(a, v):
    n = len(a)
    x = np.ones(n)
    deltas = np.ones(n)
    m = np.copy(a)
    a_t = a.transpose()
    delta = det(m)
    for i in range(n):
        m_t = a_t.copy()
        m_t[i] = np.copy(v)
        #deltas[i] = det(m_t)
        deltas[i] = np.linalg.det(m_t)
        x[i] = deltas[i] / delta + 0
        print(f"x[{i}] = {x[i] + 0}")
    return x


a = np.array([[2., 5.], [1., -10.]])
v = np.array([1., 3.])
M = np.copy(a)
print(det(M))

kramer(a, v)
