class SquareIter:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = -1
            self.stop = args[0]
        elif len(args) == 2:
            self.start, self.stop = args[0] - 1, args[1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.stop:
            raise StopIteration
        self.start += 1
        return self.start ** 2


heir = SquareIter(10)
print(*(next(heir) for _ in range(5)))  # 0 1 4 9 16
print(list(heir))  # [25, 36, 49, 64, 81, 100]

try:
    print(heir.__next__())
except StopIteration:
    print("This is an iterator, you can iterate it over only once !")
# This is an iterator, you can iterate it over only once !

heir2 = SquareIter(1, 6)
print(tuple(heir2), list(heir2))  # (1, 4, 9, 16, 25, 36) []
