class Commuter1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other, end='; ')
        return self.val + other

    def __radd__(self, other):
        print('radd', self.val, other, end='; ')
        return other + self.val


x = Commuter1(100)
y = Commuter1(101)

print(x + 1)  # add 100 1; 101
print(10 + y)  # radd 101 10; 111
print(x + y)  # add 100 <__main__.Commuter1 object at 0x7fd28040bb50>; radd 101 100; 201
