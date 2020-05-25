# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import minimize_scalar

# %% [markdown]
# Q1

# %%
def simulate(n): 
    x0 = np.random.uniform(0,2/n)
    y0 = np.random.uniform(0,2/n)

    x,y = [x0],[y0]

    for _ in range(n-1):
        x0 = x0 + np.random.uniform(0,2/n)
        y0 = y0 + np.random.uniform(0,2/n)
        x.append(x0 if x0 < 1 else 1)
        y.append(y0 if y0 < 1 else 1)
    return x,y


# %%
x,y = simulate(5)
print(x,y)

# %% [markdown]
# Q2

# %%
def minimize(x,y):
    """
    This function returns the x0 and y0 within the sequence(x,y) that minimizes the sum of distance between 0 to y and y to 1 respectively. 
    
    ---
    Arguments
    x0: float
    - intersection point
    
    x,y: lists
    - sequence of increasing floats
    
    ---
    Returns
    x0_star,y0_star: floats
    
    """
    
    x    = np.array(x)
    y    = np.array(y)
    obj  = lambda x0: np.sum(y[x<x0])+np.sum(1-y[x>=x0])
    res  = minimize_scalar(obj, bounds=(0,1),method='bounded')
    x0_star = x[x>=res.x][0]
    y0_star = y[x>=res.x][0]
    return x0_star,y0_star


# %%
minimize(x,y)


# %%
n_list = np.arange(10,1000,10)
y_star_list = []

for n in n_list:
    x,y = simulate(n=n)
    x0_star,y0_star = minimize(x,y)
    y_star_list.append(y0_star)


# %%
fig,ax = plt.subplots()
ax.plot(n_list,y_star_list)
plt.xlabel('n')
plt.ylabel('$y_k*$')
plt.title('Convergence of $y_k^*$')

# %% [markdown]
# $y_k^*$ seems to converge towards 0.5, which is the midpoint of the interval, given it's a uniform distribution that's as expected.
