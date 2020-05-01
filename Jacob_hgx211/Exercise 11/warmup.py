import matplotlib.pyplot as plt
from numpy import linspace

# Function
def TnFactory(n):
    if n == 0:
        def Tn(x):
            return 1
    elif n == 1:
        def Tn(x):
            return x
    elif n > 1:
        def Tn(x):
            return 2*x*TnFactory(n-1)(x) - TnFactory(n-2)(x)
    return Tn



# BONUS
x_start, x_end = -1, 1 # x-axis range
pols = 5               # Number of polynomials to plot

# pip install git+https://github.com/garrettj403/SciencePlots.git
x = linspace(x_start,x_end,200)       
plt.style.use('science')   
plt.figure(figsize=(5,4),dpi=400)
for i in range(1,pols+1):
    plt.plot(x, TnFactory(i)(x), label='$T_{}(x)$'.format(i))
plt.xlabel('$x$')
plt.ylabel('$T_n(x)$')
plt.title('First 5 Chebyshev polynomials, $T_n(x)$', fontsize=16)
plt.xlim([x_start,x_end])
plt.ylim([x_start,x_end])
plt.legend(loc='lower right', frameon=True)
plt.savefig('fig.png')