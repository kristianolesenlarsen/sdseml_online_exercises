import time

class clock():
    def __init__(self, type, hour):
        self.type = type
        self.hour = hour
    def tick(self):
        self.hour = self.hour + 1
    def display(self):
        return self.hour%self.type
    def reset(self):
        self.hour = 0
    def cycle(self):
        return self.hour // self.type

clocks = clock(24,0), clock(12,0)

def time_test(h):
    clocks[0].reset()
    clocks[1].reset()
    for i in range(h):
        clocks[0].tick()
        clocks[1].tick()
        print ('time', clocks[0].display(), ': 00', clocks[1].display(), ': 00')
        print ('cycles',clocks[0].cycle(), clocks[1].cycle())
        time.sleep(0.5)
time_test(48)
