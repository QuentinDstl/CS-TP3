from decompDMN import decompDMN
from trianginf import trianginf
from creemat import creemat
from numpy import zeros,array

[A,b] = creemat(5)
print(A)
print(b)

# def gaussseidel(A, b, x0, eps, Nb):
#     # A est la matrice
#     # b est le vecteur second membre
#     # x0 est la valeur initiale
#     # eps est la précision
#     # N est le nombre maximum d'itérations

#     [DM, N]= decompDMN(A)
#     n = len(b)
#     x = zeros(n)
#     L = zeros(n)

#     for k in range(Nb):
#         for i in range(0,n):
#             S = 0
#             for j in range(i+1,n):
#                 S += N[i][j] * x0[j]
#             L[i]=S+b[i]
#         x=trianginf(DM,L)
#         print(x)
#         if(max(abs(x - x0)) < eps):
#             return x
#         x0 = x
#     return x

# x=gaussseidel(array([[1,1,-1],[2,-1,1],[-1,2,2]]), array([-2, 5, 1]),array([0, 0, 0]), 0.5,2)
# print(x)

# x=gaussseidel(array([[1,1,-1],[2,-1,1],[-1,2,2]]), array([-2, 5, 1]),array([0, 0, 0]), 0.5,2)
# print(x)

