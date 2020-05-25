#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


def simulate(n):
    x0 = np.random.uniform(0, 2/n) 
    y0 = np.random.uniform(0, 2/n) 
    x, y = [x0], [y0] 
    
    for _ in range(n-1): 
        x0 = x0 + np.random.uniform(0,2/n) 
        y0 = y0 + np.random.uniform(0,2/n) 
        x.append(x0 if x0 < 1 else 1) 
        y.append(y0 if y0 < 1 else 1)
    return x,y


# In[6]:


simulate(8)


# In[ ]:


def minimize(x,y)

    return(x_star)

