#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Create class
class Clock():
    
    def __init__(self, time=0, hours = 24, cycle = 0):
        self.time = time
        self.hours = hours
        self.cycle = cycle
    
    def tick(self):
        self.time += 1
        self.cycle += 1
        if self.time >= self.hours:
            self.time = 0
        
    def __eq__(self, other):
        return self.time == other

# create two instances with different hours
clock1 = Clock(3)
clock2 = Clock(2)

# test __eq__ (not equal)
print(clock1 == clock2)

# make equal
clock2.tick()

# test __eq__ (equal)
print(clock1 == clock2)

# does the cycle work? create clock with three hours
clock3 = Clock(hours=3)

print(clock3.cycle)
print(clock3.time)

i = 0
while i != 4:
    clock3.tick()
    i += 1
    
print(clock3.cycle)
print(clock3.time)

