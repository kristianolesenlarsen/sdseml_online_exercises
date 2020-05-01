import numpy as np
import matplotlib.pyplot as plt

def TnFactory(n):
    if n == 0: return 1
    elif n == 1: return x
    else:
        return 2*x*TnFactory(n-1) - x*TnFactory(n-2)

x = np.linspace(-1,1,100)
for i in range(1,6):
    y = TnFactory(i)
    plt.plot(x,y, label='n = %i' %i)
    plt.legend()
    plt.show()
