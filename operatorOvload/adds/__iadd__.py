class Commuter:
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):
        """
            addition assignment operator handler
        """
        self.val += other
        return self


x = Commuter(100)
x += 1
x += 15
