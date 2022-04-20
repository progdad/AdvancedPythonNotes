class StepperIndex:
    def __init__(self):
        self.data = "Spam"

    def __getitem__(self, i):
        return self.data[i]


ohmy = StepperIndex()

for item in ohmy:
    print(item, end=' ')  # S p a m

print('p' in ohmy)  # True

a, b, c, d = ohmy
print(a, c, d)  # S a m

print(list(map(str.upper, ohmy)))  # ['S', 'P', 'A', 'M']
