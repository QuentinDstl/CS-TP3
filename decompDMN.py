from numpy import zeros

# decompostion A = DM - N
# DM est la matrice diagonale
# N est la matrice triangulaire strictement supérieure
def decompDMN(A):
    n = len(A)
    DM = zeros((n, n))
    N = zeros((n, n))
    for i in range(n):
        for j in range(n):
            if(j <= i):
                DM[i][j] = A[i][j]
            else:
                N[i][j] = -A[i][j]
    return [DM, N]