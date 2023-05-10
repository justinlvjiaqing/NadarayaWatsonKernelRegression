import numpy as np

def Hammerstein(n,input_std, nonlinear_fun, linear_fun, noise_std):
    n1 = n+len(linear_fun)
    U = np.random.normal(loc=0,scale=input_std,size=(n1,1))
    V = nonlinear_fun(U)
    V1 = V
    W = np.zeros([n1,1])
    for i in range(len(linear_fun)):
        W = V1[:n1]*linear_fun[i]+W
        V1 = np.insert(V1,0,0,axis=0)
    Z = np.random.normal(loc=0,scale=noise_std,size=(n1,1))
    Y = W+Z
    U = U[len(linear_fun):]
    Y = Y[len(linear_fun):]
    return U,Y