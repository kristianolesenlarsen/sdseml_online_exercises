from scipy import integrate
from numpy import log, linspace
import matplotlib.pyplot as plt

#Intergration function
def Integrate(f, a, b):
    I, _ = integrate.quad(f, a, b)
    return I

#define function to integrate
func = lambda t: 1/log(t)
# 100 number between 10^1 and 10^10
N = linspace(1, 10, num=100)

pi_n = []
for n in N:
        pi_n.append(Integrate(func, 2, n))

plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(N, pi_n, label='Li(n)')
ax.set_ylabel('Number of Primes')
ax.set_xlabel('n')
ax.legend(loc='upper left', frameon=False)
fig.suptitle('Approximation of the Number of Primes')
plt.show()