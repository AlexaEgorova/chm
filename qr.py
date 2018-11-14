import numpy as np
import math as m
    
def norm(x):
    #евклидова норма
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
    return Q, A

def ufind(cln):
    v = cln / (cln[0] + np.copysign(norm(cln), cln[0]))
    v[0] = 1
    U = np.eye(cln.shape[0])
    U -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return U

def backsub(A, b):
    n = len(A)
    for i in range(0, n):
        if A[i][i] == 0:
            print("Вырожденная матрица!")
        else:
            x = np.zeros(n)
            for k in range(n):
                if A[k, k] != 1:
                    A[k, :] *= 1 / A[k, k]
                    b[k] *= A[k, k]
                for row in range(k + 1, n):
                    A[row, :] -= A[k, :] * A[row, k]
                    b[row] -= b[k] * A[row, k]
                for j in range(n-1, 0, -1):
                    for i in range(j-1, -1, -1):
                        if A[i][j]:
                            A[i, :] -= A[j, :] * A[i][j]
                            b[i] -= b[j] * A[i][j]
            print(A)
            print(b)

    
A = np.array([
    [12., -51.,   4.],
    [ 6., 167., -68.],
    [-4.,  24., -41.]])

b = np.array([10, 20, 30])

A = np.array([
    [12., -51.,   4.],
    [ 6., 167., -68.],
    [-4.,  24., -41.]])

b = np.array([10, 20, 30])


backsub(A, b)

#print(np.linalg.qr(A))
#print(np.linalg.solve(A, b))

qr(A) 

 
