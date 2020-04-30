from scipy import integrate
from numpy import log, linspace
import matplotlib.pyplot as plt

def Integrate(f, a, b):
    I, _ = integrate.quad(f, a, b)
    return I

N = linspace(10, 10**10, 100) # Define n (could probably also have used np.logspace)
Li_n = lambda t: 1/log(t) # Define function
pi_n = [Integrate(Li_n, 2, n) for n in N]

pltstyle = "https://raw.githubusercontent.com/cako/mpl_grandbudapest/master/grandbudapest.mplstyle"

with plt.style.context(pltstyle):
    plt.plot(N, pi_n, label = '$Li(n) $')    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('$n\in [10, 10^{10}]$', fontsize = 16)
    plt.ylabel('$\pi(n)$', fontsize = 16)
    plt.title('Warmup 7', fontsize= 16)
    plt.legend(frameon = True, fontsize = 14)
    plt.figure(figsize=(10,5))
    plt.show()

