import numpy as np
from scipy import integrate
from numpy import log, linspace
import matplotlib.pyplot as plt
style = "https://raw.githubusercontent.com/nicoguaro/matplotlib_styles/master/styles/neon.mplstyle"

def Integrate(f, a, b):
    I, _ = integrate.quad(f, a, b)
    return I

#function
y = lambda x: 1/log(x)
#100 numbers between 10 and 10**10
n = np.linspace(10, 10**10, num=100)
#Li(n) list
Li = [Integrate(y, 2, n2) for n2 in n]
#plot
with plt.style.context(style):
    fix, ax = plt.subplots(figsize = (8, 5))
    plt.plot(Li, n)
    plt.xlabel('Li(n) (primes under n)', fontsize = 20)
    plt.ylabel('n', fontsize = 15)