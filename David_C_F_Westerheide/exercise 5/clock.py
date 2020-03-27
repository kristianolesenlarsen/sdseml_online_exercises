class Clock:

    def __init__(self, cycles, h, max_h):
        self.cycles= cycles
        self.h = h
        self.max_h = max_h

    def tick(self):
        if (self.h == self.max_h):
            self.cycles += 1
            self.h = 0
        else:
            self.h += 1
        print(self.cycles)
        print(self.h)
        print(self.max_h)

    def __eq__(self, second):
        hours1 = self.max_h*self.cycles+self.h
        hours2 = second.max_h*second.cycles+second.h
        print(hours1)
        print(hours2)
        if (hours1 == hours2):
            return True 
        else:
            return False 
   
#Tests
A=Clock(cycles=0,h=22,max_h=24)
A.tick()
A.tick()
A.tick()

B=Clock(cycles=1,h=10,max_h=12)
B.tick()
B.tick()
B.tick()

C=Clock(cycles=3,h=10,max_h=24)
C.tick()
C.tick()
C.tick()

print(A==B)
print(A==C)        