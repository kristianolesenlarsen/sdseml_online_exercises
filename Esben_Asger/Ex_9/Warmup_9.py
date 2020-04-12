# Warmup 7(9)
from scipy import integrate
import numpy as np
from numpy import log, linspace
import matplotlib.pyplot as plt

#Intergration function
def Integrate(f, a, b):
    I, _ = integrate.quad(f, a, b)
    return I

#define function to integrate
func = lambda t: 1/log(t)
# 100 number between 10^1 and 10^10
n_list = np.logspace(1, 10, num=100)
#Calc Li(n)
li_n = [Integrate(func, 2, n) for n in n_list]

#plot
plt.style.use('/Users/Esben/.matplotlib/stylelib/science.mplstyle')
fig, ax = plt.subplots(figsize = (10,7))
plt.plot(n_list, li_n)
plt.xlabel('primes under n', fontsize = 20)
plt.ylabel('n', fontsize = 20)
plt.yscale('log')
plt.xscale('log')
plt.show()