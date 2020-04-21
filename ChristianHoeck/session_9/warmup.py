from scipy import integrate
from numpy import log, linspace
import numpy as np
import matplotlib.pyplot as plt

def Integrate(f, a, b):
    I, _ = integrate.quad(f, a, b)
    return I

def f(t):
    return 1/log(t)

def Li(n):
    return Integrate(f,2,n)


def Li_vec(n):
    return np.vectorize(Li)(n)


lin = linspace(10,10**10,100)
results = Li_vec(lin)

plt.style.use('default')
plt.scatter(lin,results)
plt.legend(['Li'])
plt.xlabel('n')
plt.ylabel('Li(n)')