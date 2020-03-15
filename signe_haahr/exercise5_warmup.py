class Clock:
    def __init__(self, hour = 0, n = 24):
        self.hr = hour
        self.n = n
    
    def __str__(self):
        return f"Number of hours elapsed: {self.hr}"
    
    def __eq__(self, other):
        if isinstance(other, Clock):
            if other.hr == self.hr:
                return True
            
            else:
                return False
    
    def tick(self):
        if self.hr == self.n:
            self.hr = 0 
        
        elif self.hr < self.n:
            self.hr += 1  
    
        return self.hr