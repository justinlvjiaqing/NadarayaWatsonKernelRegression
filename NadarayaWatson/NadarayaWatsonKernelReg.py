import numpy as np

def Kernel(w):
    # This code uses a quartic (biweight) kernel function as an example
    y = 15/16*(1-w**2)**2*(np.abs(w)<1)
    return y


def KernelEst(w,h,U,Y):
    Sk = Kernel((w-U)/h).sum() 
    if np.abs(Sk) <0.000001:
        g = 0
    else:
        Sy = (Y*Kernel((w-U)/h)).sum()
        g = Sy/Sk
    return g