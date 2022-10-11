from decompDMN import decompDMN
from trianginf import trianginf
from creemat import creemat
from numpy import zeros,array,dot

[A,b,x0] = creemat(5)
print(A)
print(b)
print(x0)

def gaussseidel(A, b, x0, eps, Nb):
    # A est la matrice
    # b est le vecteur second membre
    # x0 est la valeur initiale
    # eps est la précision
    # N est le nombre maximum d'itérations

    [DM, N]= decompDMN(A)
    n = len(b)
    x = zeros(n)
    L = zeros(n)

    for k in range(Nb):
        L=dot(N,x0)+b
        x=trianginf(DM,L)
        if(max(abs(x - x0)) < eps):
            return x
        x0 = x
    return x

x=gaussseidel(A,b,x0, 0.001,100)
print(x)