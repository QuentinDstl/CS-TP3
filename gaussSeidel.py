from numpy import zeros

def gaussseidel(A, b, x0, eps, N):
    # A est la matrice
    # b est le vecteur second membre
    # x0 est la valeur initiale
    # eps est la précision
    # N est le nombre maximum d'itérations
    n = len(b)
    x = zeros(n)
    for k in range(N):
        for i in range(n):
            s = 0
            for j in range(n):
                if(j != i):
                    s += A[i][j] * x0[j]
            x[i] = (b[i] - s) / A[i][i]
        if(max(abs(x - x0)) < eps):
            return x
        x0 = x
    return x