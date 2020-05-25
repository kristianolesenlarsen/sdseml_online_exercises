import numpy as np

# Function for simulating sequence
def simulate(n):
    # Since no initial was stated I use zero
    x = [0]
    y = [0]

    for i in range(n):
        x_new = min(x[i] + np.random.uniform(0,2/n),1)
        y_new = min(y[i] + np.random.uniform(0,2/n),1)
        x.append(x_new)
        y.append(y_new)
    return [np.array(x),np.array(y)]

# Inner function for divided sum
def divsum(seq,x0):
    greater_lst = (seq[0] > x0)
    less_lst = ~(seq[0] > x0)
    divsum =  np.inner(seq[1],less_lst) + np.inner(np.subtract(1,seq[1]),greater_lst)
    return divsum

# Outer function that finds minimum
def minimize(seq):
    divsum_lst = [divsum(seq,x) for x in seq[0]]
    min_index = np.argmin(divsum_lst)
    return [seq[0][min_index], seq[1][min_index]]

# Simulate and find min over range
n = np.arange(10,1000,10)
min_lst = [minimize(simulate(i))[1] for i in n]

import matplotlib.pyplot as plt

plt.plot(n,min_lst)

# We see that y_k converges 0.5. This makes sense since as  the theoretic mean of the distriubtion for y, the mean miniminzes the sum of dinstances, both aboslute and squared when in 1d.