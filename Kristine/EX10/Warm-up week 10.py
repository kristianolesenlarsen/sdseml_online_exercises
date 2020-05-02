#!/usr/bin/env python
# coding: utf-8

# ### Q1

# In[6]:


import numpy as np


# In[13]:


def Pyth(a,b,c,q):
    qa = q*a
    qb = q*b
    qc = q*c
    return(qa,qb,qc)


# In[14]:


def Prof(a,b,c):
    if a**2 + b**2 == c**2:
        return("TRUE")
    else:
        return("False")


# Example True

# In[18]:


Prof(3,4,5)


# In[19]:


Pyth(3,4,5,3)


# In[20]:


Prof(9,12,15)


# Example False

# In[21]:


Prof(1,2,3)


# In[22]:


Pyth(1,2,3,4)


# In[23]:


Prof(4,8,12)


# ### Q2

# Plot in a,b space all pythagorean triples with a,b < 10.000

# In[32]:


import math

A = []
B = []
C = []

def pythagorean_triplet(n):
  for b in range(n):
    for a in range(1, b):
        c = math.sqrt( a * a + b * b)
        if c % 1 == 0:
            A.append(a)
            B.append(b)
            C.append(c)
            print(a, b, int(c))
            


# In[35]:


pyth = pythagorean_triplet(10000)


# In[40]:


import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
plt.scatter(A, B)
plt.xlabel('a')
plt.ylabel('b')
plt.title('Pythagorean triplets with a,b < 10,000')
plt.show()


# In[ ]:




