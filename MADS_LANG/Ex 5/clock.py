# not done, but this is my best shot...
class Clock:
    def __init__(self, current = 0):
        self.current = current

    def generator(self):
        while True:
            yield self.current
            self.current += 1

    def tick(self):
        self.current = self.generator().__next__()
        print(self.current)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



clock1 = Clock()
clock1.tick()
