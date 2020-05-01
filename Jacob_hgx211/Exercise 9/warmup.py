# Imports
from scipy import integrate
from numpy import log, linspace
import matplotlib.pyplot as plt

# Function for integrating
def Integrate(f,a,b):
    '''
    Returns the definite integral of f from a to b
    '''
    return integrate.quad(f,a,b)[0]

# Define function
f = lambda t: 1/log(t)

# Values for x-axis and y-axis in graph
x = linspace(10,10**10,10)
y = [Integrate(f,2,n) for n in x]

# Make figure
plt.style.use('science') # pip install git+https://github.com/garrettj403/SciencePlots.git
plt.plot(x,y)
plt.savefig('fig.pdf')