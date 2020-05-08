#!/usr/bin/env python
# coding: utf-8

# In[38]:


import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace

def TnFactory(n,x):
    if n == 0:
         return 1
    elif n == 1:
        return x
    elif n > 1:
        return 2*x*TnFactory(n-1)(x) - TnFactory(n-2)(x)
    


# In[39]:


TnFactory(0,1)


# In[40]:


TnFactory(3,1)


# In[41]:


TnFactory(2,4)


# How do i get a functioning x? :)
