import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

def simulate(n):
    """
    Returns a uniform sequence of x,y 
    
    Args:
    n (int): Length of sequence
    
    Returns:
    x (array): array of x sequence
    y (array): array of y sequence
    """
    
    x0 = np.random.uniform(0, 2/n) 
    y0 = np.random.uniform(0, 2/n) 
    x, y = [x0], [y0] 
    
    for _ in range(n-1): 
        x0 = x0 + np.random.uniform(0,2/n) 
        y0 = y0 + np.random.uniform(0,2/n) 
        x.append(x0 if x0 < 1 else 1) 
        y.append(y0 if y0 < 1 else 1)
        
    return np.array(x),np.array(y)

def minimize(x,y):
    """
    Estimates the minimum of sequence 
    
    Args:
    x (array): array of x sequence
    y (array): array of y sequence
    
    Returns:
    x_star (float): the x0 that minimizes the sequence
    y_star (float): the y0 that minimizes the sequence
    
    """
    #objective function
    obj = lambda x0: np.sum(y[x<x0[0]])+np.sum(1-y[x>=x0[0]]) 
    
    #initial guess and bounds
    guess = [0.5]
    bounds = ((0,1),)
    
    #calling optimizer
    result = optimize.minimize(obj,x0=guess,method='L-BFGS-B',bounds=bounds)
    
    #unpacking results
    x_star = x[x>=result.x][0]
    y_star = y[x>=result.x][0]
    return x_star,y_star

n_sim = np.arange(10,1000,10)
y_star = np.empty(np.shape(n_sim))
for i, n in enumerate(n_sim):
    x,y = simulate(n=n)
    x_star,y_star[i] = minimize(x,y)

#plotting y_star as a function of n
fig = plt.figure(figsize=(13,9))
ax = fig.add_subplot(1,1,1)
ax.plot(n_sim,y_star)
ax.set_ylabel('$y^{\star}_k$')
ax.set_xlabel('$n$')
xlim = ax.get_xlim()
ax.hlines(np.mean(y_star), xlim[0], xlim[1],color="r") #plots the mean of y_star