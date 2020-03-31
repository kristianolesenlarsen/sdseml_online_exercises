class Clock:
    def __init__(self, n):
        self.n = n
        self.hours = 0
        self.cycles = 0

    # the tick method adds one hours and if the clock completes one full cycle, it adds 1 to cycle
    def tick(self):
        self.hours += 1
        self.cycles = self.hours // self.n
    # the __eq__ dunder method is specifying when two instances are 'equal', i.e. when (objecta == objectb) is True.
    # in this case we define two instances to be equal, when the amount of hours in each instance are the same, and when
    # the other instance is actually and instance.

    def __eq__(self, other):
        if isinstance(other, Clock):
            if other.hours == self.hours:
                return True
        return False

