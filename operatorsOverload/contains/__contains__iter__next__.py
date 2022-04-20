class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, value):
        return self.data[value]

    def __iter__(self):
        self.ix = 0
        return self

    def __next__(self):
        if self.ix == len(self.data):
            raise StopIteration

        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, value):
        return value in self.data


if __name__ == '__main__':
    iters = Iters([1, 2, 3, 4, 5])
    print(3 in iters)  # True
    for i in iters:
        print(i, (i + 2) in iters, end=', ')  # 1 True, 2 True, 3 True, 4 False, 5 False,

    print()
    print([i ** 2 for i in iters])  # [1, 4, 9, 16, 25]
    print(list(map(bin, iters)))  # ['0b1', '0b10', '0b11', '0b100', '0b101']
    iters2 = iter(iters)
    while True:
        try:
            print(next(iters2), end=', ')  # 1, 2, 3, 4, 5,
        except StopIteration:
            break
