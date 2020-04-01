#!/usr/bin/env python
# coding: utf-8

# In[19]:


def add(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print(sum)


# In[25]:


def custom_hello(**name_greeting_pair):
    print(" and ".join(f"{greeting} {name}" for name, greeting in name_greeting_pair.items()))


# In[28]:


if __name__ == '__main__':
    custom_hello(Kristian='Hello',upload = 'sorry about forgetting to')
    print(f'How many times sorry?')
    add(120,130,150)

