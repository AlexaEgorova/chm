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
    #print("Q:\n", Q)
    for i in range(0, n):
        for j in range(0, n):
            A[i][j] = round(A[i][j], 5)
    #print("A:\n", A)
    #print("QA\n", np.dot(Q, A))
    return Q, A


def ufind(cln):
    v = cln / (cln[0] + np.copysign(norm(cln), cln[0]))
    v[0] = 1
    U = np.eye(cln.shape[0])
    U -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return U

def backsub(A, b):
    A1 = A.copy()
    n = len(A1)
    x = np.zeros(n)
    x[n-1] = b[n-1] / A1[n-1][n-1]
    for k in range(n-2, -1, -1):
        sum = b[k]
        for j in range(n-1, k, -1):
            sum -= A1[k][j] * x[j]
        x[k] = sum / A1[k][k]
    print(x)
    return x
            

A = np.array([
    [12., -51.,   4.],
    [ 6., 167., -68.],
    [-4.,  24., -41]])
b = np.array([10., 20., 30.])

print("npqr", np.linalg.qr(A))
Q, R = qr(A)
print("Q:\n", Q)
print("R:\n", R)
print("QR:\n", np.dot(Q, R))
print("Qb:\n", np.dot(Q, b))
print("npsolve", np.linalg.solve(A, b))
backsub(R, np.dot(Q.transpose(), b));
