# Warmp up session 5
# CLOCK
# Implement a class Clock that mimick a n-hour clock.
# Assume that all clocks start at hour 0. Implement a .tick() the clock forward one hour.
# the clock should also store the number of cycles it has run through since intitialization.

# I did not have time to figure in detail, sorry

#__eq__method
class Clock:

def __init__(self, the_hr, the_min, the_sec):
self.hr = the_hr
self.min = the_min
self.sec = the_sec

def __str__(self):
return “{0:02d}:{1:02d}:{2:02d}”.format(self.hr, self.min, self.sec)

def tick(self):
self.sec += 1
if self.sec == 60:
self.sec = 0
self.min += 1

if self.min == 60:
self.min = 0
self.hr += 1

if self.hr == 24:
self.hr = 0

test.py
