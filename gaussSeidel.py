from numpy import zeros

def gaussseidel_opti(A, b, x0, eps, N):
    # A est la matrice
    # b est le vecteur second membre
    # x0 est la valeur initiale
    # eps est la précision
    # N est le nombre maximum d'itérations
    n = len(b)
    x = zeros(n)
    for k in range(N):
        for i in range(n):
            S = 0
            for j in range(n):
                if(j != i):
                    S += A[i][j] * x0[j]
            x[i] = (b[i] - S) / A[i][i]
        if(max(abs(x - x0)) < eps):
            return x
        x0 = x
    return x

from decompDMN import decompDMN

def gaussseidel(A, b, x0, eps, N):
    # A est la matrice
    # b est le vecteur second membre
    # x0 est la valeur initiale
    # eps est la précision
    # N est le nombre maximum d'itérations

    [DM, N] = decompDMN(A)

    n = len(b)
    x = zeros(n)
    x[0] = (b[0] - A[0][1] * x0[1] - A[0][2] * x0[2]) / A[0][0]
    for k in range(N):
        for i in range(1,n):
            S = 0
            for j in range(i+1,n):
                S += N[i][j] * x[j]
            x[i] = (b[i] - DM[i][i-1] * x[i] - S) / DM[i][i]
        if(max(abs(x - x0)) < eps):
            return x
        x0 = x
    return x