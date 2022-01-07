class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]


ohmy = StepperIndex()
ohmy.data = "Spam"

for item in ohmy:
    print(item, end=' ')  # S p a m

print('p' in ohmy)  # True

a, b, c, d = ohmy
print(a, c, d)  # S a m

print(list(map(str.upper, ohmy)))  # ['S', 'P', 'A', 'M']
