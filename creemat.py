from random import randint, random, randrange
from numpy import zeros

def creemat(n):
    A = zeros((n, n))
    b = zeros(n)
    x0 = zeros(n)
    for i in range(n):
        A[i][i]=3
        if(i!=n-1):
            A[i+1][i]=1
            A[i][i+1]=1
        b[i]=1
        x0[i]=randint(0,10)
    return [A, b, x0]