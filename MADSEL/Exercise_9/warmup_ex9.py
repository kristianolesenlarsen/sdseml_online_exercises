from scipy import integrate
from numpy import log, linspace
import matplotlib.pyplot as plt

from publib import set_style, fix_style

def Integrate(f, a, b):
    I, _ = integrate.quad(f,a,b)
    return I

ft = lambda t: 1/log(t)
limits = list(linspace(10,10**10,100))
Li = []
n = []

for i in limits:
    temp = Integrate(ft,2,i)

    #Append results i times
    Li.append(temp)
    n.append(i)

#Creating figure
set_style('article') #before the first plot

plt.figure()
ax = plt.subplot()
ax.plot(n, Li,'o', label = 'Logarithmic integral')
plt.xlabel(r'$n \in [10,10^{10}]$')
plt.ylabel(r'$Li(n)=\int_{2}^n \frac{1}{\log \: t}dt$')
plt.title('A nice title')
plt.legend(loc='upper left')

fix_style('article')
plt.show()


