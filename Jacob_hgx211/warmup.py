class clock:
    def __init__(self, n = 24):
        self.n = n
        self.cycles = 0
        self.hour = 0

    def tick(self):
        if self.hour + 1 < self.n:
            self.hour = self.hour + 1
        else:
            self.hour = 0
            self.cycles = self.cycles + 1
        
    def __eq__(self, other):
        return self.hour == other.hour