from numpy import zeros,array

def creemat(n):
    A = zeros((n, n))
    b = zeros(n)
    for i in range(n):
        A[i][i]=3
        if(i!=n-1):
            A[i+1][i]=1
            A[i][i+1]=1
        b[i]=1
    return [A, b]