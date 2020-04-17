#!/usr/bin/env python
# coding: utf-8

# In[6]:


from scipy import integrate
from numpy import log, linspace
import matplotlib.pyplot as plt
import numpy as np


# In[7]:


def Integrate(f,a,b):
    I,_=integrate.quad(f, a, b)
    return I


# In[8]:


def func(n):
    return 1/np.log(n)


# In[20]:


s = np.linspace(10,10**10,100)


# In[22]:


result = np.empty(100)


# In[23]:


for i, n in enumerate(s):
    int = Integrate(func, 2, n)
    result[i]=int


# In[40]:


from publib import set_style, fix_style
set_style('article')  

fig = plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.scatter(ns, result, label="Logarithmic integral, $L_i(n)$")

plt.title("Primes")
plt.xlabel("$n$")
plt.legend()

fix_style('article')
plt.show()


# In[ ]:




