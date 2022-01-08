class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    itr = iter(skipper)
    print(next(itr), next(itr), next(itr))  # a c e
    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')  # aa ac ae ca cc ce ea ec ee
