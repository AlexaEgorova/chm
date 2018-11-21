import numpy as np
import math as m

def norm(x):
    return m.sqrt(sum([x_i**2 for x_i in x]))

def qr(A):
    n = len(A)
    Q = np.eye(n)
    for i in range(0, n-1):
        U = np.eye(n)
        U[i:, i:] = ufind(A[i:, i])
        Q = np.dot(Q, U)
        A = np.dot(U, A)
    return Q, A

def ufind(cln):
    v = cln / (cln[0] + np.copysign(norm(cln), cln[0]))
    v[0] = 1
    U = np.eye(cln.shape[0])
    U -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return U

def vectors(Z):
    a = Z.copy()
    x = (a + a.transpose()).copy()
    pq = np.eye(Z.shape[0])
    for i in range(30):
        q, r = qr(x)
        pq = np.dot(pq, q)
        x = np.dot(r, q)
    x = np.around(x, decimals=5)
    return q, x, pq

F = np.array([
    [52., 30., 49., 28.],
    [30., 50., 8., 44.],
    [49., 8., 46., 16.],
    [28., 44., 16., 22.]])

B = np.array([[-2., 1.], [1., -1.]])

Q, x, Ux = vectors(F)
print("X:\n", x/2)
print("Ux:\n", Ux)   

print("qr_lin\n", np.linalg.qr(F))
print("eig_lin\n", np.linalg.eig(F), "\n")

Q, R = qr(F)

print("Q:\n", Q)
print("R:\n", R)
