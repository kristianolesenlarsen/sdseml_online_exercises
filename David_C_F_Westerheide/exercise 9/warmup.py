from scipy import integrate
from numpy import log, linspace
import matplotlib.pyplot as plt
plt.style.use('grandbudapest')

def Integrate(f, a, b):
    I, _ = integrate.quad(f, a, b)
    return I

Li = lambda x: 1/log(x)
N = linspace(10,10**10, 100)

pi_n = []
for n in N:
        pi_n.append(Integrate(Li, 2, n))


fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(N, pi_n, label='Li(n)')
ax.set_title('A Warm-up', fontsize=10, fontstyle='italic')
ax.set_ylabel('Number of Primes')
ax.set_xlabel('n')
ax.legend(loc='upper left', frameon=False)
fig.suptitle('Approximation of the Number of Primes')
plt.show()


