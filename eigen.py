import numpy as np
import math as m

def norm(x):
    return m.sqrt(sum([x_i**2 for x_i in x]))


def qr(A):
    n = len(A)
    Q = np.eye(n)
    Ux = np.eye(n)
    for i in range(0, n-1):
        U = np.eye(n)
        U[i:, i:] = ufind(A[i:, i])
        Q = np.dot(Q, U)
        Ux = np.dot(Ux, Q)
        print(Ux is Q)
        A = np.dot(U, A)
    #print("Q:\n", Q)
    '''for i in range(0, n):
        for j in range(0, n):
            A[i][j] = round(A[i][j], 8)'''
    #print("A:\n", A)
    return Q, A, Ux


def ufind(cln):
    v = cln / (cln[0] + np.copysign(norm(cln), cln[0]))
    v[0] = 1
    U = np.eye(cln.shape[0])
    U -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return U


def check_diagonal(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                continue
            else:
                if abs(arr[i][j]) > 1e-3:
                    return False
    return True


'''def qr_factorization(arr):
    temp = arr
    i = 0
    while True:
        q, r = qr(temp)
        temp = np.dot(r, q)
        if check_diagonal(temp):
            break
        i += 1
    return temp'''

A = np.array([
    [2.,-1., 3.],
    [1., 0., 5.],
    [0., 1., 6]])

B = np.array([[-2., 1.], [1., -1.]])

eigens = np.diag(np.dot(R, Q))
veigens = np.eye(2, len(eigens))
z = B.copy()
for i in range(0, len(eigens)):
    z[i][i] -= eigens[i]
print("z:\n", z)    

print("eigens\n", eigens)
print("qr_lin\n", np.linalg.qr(B))
print("eig_lin\n", np.linalg.eig(B), "\n")
#print("fac", qr_factorization(B), "\n")
Q, R, Ux = qr(B)
print("Q:\n", Q)
print("R:\n", R)
print("Ux:\n", Ux)
