import numpy as np

def relax(a, v):
    e = 0.001 
    n = len(a)
    b = np.ones((n, n))
    c = np.ones(n)
    count = 1
    #_______________________
    #приведение к необходимому виду
    for i in range(0, n):
        for j in range(0, n):
            b[i][j] = - a[i][j]/a[i][i]
        c[i] = v[i]/a[i][i] 
    print("c:\n", c)
    z = np.ones((n, n)) #матрица для вычислений
    z1 = np.zeros((n, n)) #нижняя треугольная
    z2 = np.zeros((n, n)) #верхняя треугольная 
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                z[i][j] = 0
            else:
                z[i][j] = b[i][j]
        for j in range(0, i):
            z1[i][j] = z[i][j]
        for j in range(i+1, n):
            z2[i][j] = z[i][j]
    print("z:\n", z)
    print("z1:\n", z1)
    print("z2:\n", z2)
    #_______________________
    #матричные равномерные нормы
    summs = np.zeros(n)
    summs1 = np.zeros(n)
    summs2 = np.zeros(n)
    for i in range(0, n):
        for j in range(0, n):
            summs[i] += abs(z[i][j])
            summs1[i] += abs(z1[i][j])
            summs2[i] += abs(z2[i][j])
    summ = max(summs)
    summ1 = max(summs1) 
    summ2 = max(summs2) 
    print("summ:\n", summ)
    #________________________
    #начальное приближение 
    x = np.zeros(n)
    x.shape = (n, 1)
    '''for i in range(0, n):
        x[i] = c[i]'''
    print("x:\n", x)
    #________________________
    #поиск i-ого приближения (до заданной точности)
    if summ < 1:
        crit = 1
        while crit > (e*(1-summ)/summ2):
            crits = np.zeros(n)
            x_k = np.zeros(n)
            x_k.shape = (n, 1)
            
            for i in range(0, n):
                for j in range(0, n):
                    x_k[i] += z1[i][j] * x_k[j] + z2[i][j] * x[j][count-1]
                x_k[i] += c[i]

            crit = max(crits)
            print("x(", count, "):\n", x_k)
            x = np.hstack((x, x_k))
            #критерий остановки
            for i in range(n):
                crits[i] = x[i][len(x[0])-1] - x[i][len(x[0])-2]
            crit = max(crits)
            print("crit:\n", crit)
            count += 1
    else:
        print("Метод расходится")
    return(x)
    


a = np.array([[6.25, -1., 0.5], [-1., 5., 2.12], [0.5, 2.12, 3.6]])
v = np.array([7.5, -8.68, -0.24])
w = 1.5

relax(a, v)
