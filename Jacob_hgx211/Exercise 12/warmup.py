import numpy as np
import matplotlib.pyplot as plt

# QUESTION 1
# Function for simulating sequence of length n
def simulate(n):
    seq = [(0,0)] # I assume we initialize in (0,0)
    for i in range(n-1):
        dx,dy = np.random.uniform(0,2/n),np.random.uniform(0,2/n)
        x,y = seq[i][0] + dx, seq[i][1] + dy
        if x > 1: x = 1
        if y > 1: y = 1
        seq.append((x,y))
    return seq


# QUESTION 2
# Function for calculating divided sum of sequence
def divided_sum(seq,x0):
    dsum = 0
    for i in seq:
        if i[0] < x0:
            dsum += i[1]
        else:
            dsum += 1-i[1]
    return dsum

# Function for minimizing divided sum of sequence
def minimize(seq):
    xs = list(set([i[0] for i in seq]))
    dsums = [divided_sum(seq,x) for x in xs]
    min_idx = dsums.index(min(dsums))
    x_min = xs[min_idx]
    y_min = [i[1] for i in seq if i[0] == x_min][0]
    return x_min, y_min


# QUESTION 3
ns = np.arange(10,1000,10)
results = [(n,minimize(simulate(n))[0]) for n in ns]

plt.style.use('science')    
plt.figure(figsize=(5,4),dpi=120)
plt.scatter(ns,[i[1] for i in results])
plt.xlabel('$n$')
plt.ylabel('$y_k*$')
plt.savefig('fig.png')

# COMMENT: y appears to converge to 0.5. This makes sense: Looking at the graph
#          in the exercise slide, it makes sense that the sum is on average
#          minimized for x = 0.5 and thus y = 0.5, since the bars on the left
#          and right sides are then the smallest. As n grows larger, the
#          randomness (variance) is minimized, such the values of y narrow in
#          around y = 0.5. I note that the sum will on average always be
#          minimized for y = 0.5, no matter the n. The only difference is that
#          the variance becomes smaller as n grows.