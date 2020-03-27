

class Clock:

    def __init__(self, hours):
        self.hours = hours
        self.cycles = 0
        self.time = 0

    def tick(self):
        self.time += 1
        if self.time == self.hours:
        	self.time = 0
        	self.cycles += 1

    def __eq__(self, other):
    	return (self.time + self.hours*self.cycles) == (other.time + other.hours*other.cycles)


# Example
clock1 = Clock(4)
clock2 = Clock(2)

clock1.tick()
clock1.tick()
clock1.tick()

clock2.tick()
clock2.tick()
print(clock1 == clock2)
clock2.tick()
print(clock1 == clock2)