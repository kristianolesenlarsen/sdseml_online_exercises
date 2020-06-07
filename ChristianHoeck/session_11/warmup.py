import numpy as np
import matplotlib.pyplot as plt

def chebyshev(x,n):
    if n==0:
        return 1
    if n==1:
         return x
    else:
         return 2*x*chebyshev(x,n-1) - chebyshev(x,n-2) 

def chebyshev_fac(n):
    return lambda x: chebyshev(x, n)


for n in range(1,6):
    t = chebyshev_fac(n)
    v = [t(x) for x in np.arange(-1,1,0.01)]
    plt.plot(np.arange(-1,1,0.01), v)