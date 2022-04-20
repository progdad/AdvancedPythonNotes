# https://pythontutor.com/visualize.html#code=class%20Iters1%3A%0A%20%20%20%20%22%22%22%0A%20%20%20%20There%20are%20three%20methods%20in%20the%20class%20responsible%20for%20checking%20IN%20condition%0A%20%20%20%20It%20works%20with%20next%20priority%3A%0A%20%20%20%20%20%201.%20__contains__%0A%20%20%20%20%20%202.%20__iter__%0A%20%20%20%20%20%203.%20__getitem__%0A%20%20%20%20%22%22%22%0A%0A%20%20%20%20def%20__init__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20self.data%20%3D%20value%0A%0A%20%20%20%20def%20__getitem__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20return%20self.data%5Bvalue%5D%0A%0A%20%20%20%20def%20__iter__%28self%29%3A%0A%20%20%20%20%20%20%20%20for%20item%20in%20self.data%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20yield%20item%0A%0A%20%20%20%20def%20__contains__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20return%20value%20in%20self.data%0A%0A%0Aclass%20Iters2%3A%0A%0A%20%20%20%20def%20__init__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20self.data%20%3D%20value%0A%0A%20%20%20%20def%20__getitem__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20return%20self.data%5Bvalue%5D%0A%0A%20%20%20%20def%20__iter__%28self%29%3A%0A%20%20%20%20%20%20%20%20for%20item%20in%20self.data%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20yield%20item%0A%0A%20%20%20%20%23%20def%20__contains__%28self,%20value%29%3A%0A%20%20%20%20%23%20%20%20%20%20return%20value%20in%20self.data%0A%0A%0Aclass%20Iters3%3A%0A%0A%20%20%20%20def%20__init__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20self.data%20%3D%20value%0A%0A%20%20%20%20def%20__getitem__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20return%20self.data%5Bvalue%5D%0A%0A%20%20%20%20%23%20def%20__iter__%28self%29%3A%0A%20%20%20%20%23%20%20%20%20%20for%20item%20in%20self.data%3A%0A%20%20%20%20%23%20%20%20%20%20%20%20%20%20yield%20item%0A%0A%20%20%20%20%23%20def%20__contains__%28self,%20value%29%3A%0A%20%20%20%20%23%20%20%20%20%20return%20value%20in%20self.data%0A%0A%0Aif%20__name__%20%3D%3D%20'__main__'%3A%0A%20%20%20%20for%20cls%20in%20range%281,%204%29%3A%0A%20%20%20%20%20%20%20%20%23%20It%20will%20be%20the%20same%20output%20for%20all%20the%20classes%0A%20%20%20%20%20%20%20%20iters%20%3D%20eval%28f'Iters%7Bcls%7D%28%5B1,%202,%203,%204,%205%5D%29'%29%0A%20%20%20%20%20%20%20%20print%283%20in%20iters%29%20%20%23%20True%0A%20%20%20%20%20%20%20%20for%20i%20in%20iters%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28i,%20%28i%20%2B%202%29%20in%20iters,%20end%3D',%20'%29%20%20%23%201%20True,%202%20True,%203%20True,%204%20False,%205%20False,%0A%0A%20%20%20%20%20%20%20%20print%28%29%0A%20%20%20%20%20%20%20%20print%28%5Bi%20**%202%20for%20i%20in%20iters%5D%29%20%20%23%20%5B1,%204,%209,%2016,%2025%5D%0A%20%20%20%20%20%20%20%20print%28list%28map%28bin,%20iters%29%29%29%20%20%23%20%5B'0b1',%20'0b10',%20'0b11',%20'0b100',%20'0b101'%5D%0A%20%20%20%20%20%20%20%20iters2%20%3D%20iter%28iters%29%0A%20%20%20%20%20%20%20%20while%20True%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28next%28iters2%29,%20end%3D',%20'%29%20%20%23%201,%202,%203,%204,%205,%0A%20%20%20%20%20%20%20%20%20%20%20%20except%20StopIteration%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%0A%0A%20%20%20%20%20%20%20%20print%28%22%5CnEnd%20of%20the%20class%20output%3B%20%5Cn%5Cn%22%29%0A&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

class Iters1:
    """
    There are three methods in the class responsible for checking IN condition
    It works with next priority:
      1. __contains__
      2. __iter__
      3. __getitem__
    """

    def __init__(self, value):
        self.data = value

    def __getitem__(self, value):
        return self.data[value]

    def __iter__(self):
        for item in self.data:
            yield item

    def __contains__(self, value):
        return value in self.data


class Iters2:

    def __init__(self, value):
        self.data = value

    def __getitem__(self, value):
        return self.data[value]

    def __iter__(self):
        for item in self.data:
            yield item

    # def __contains__(self, value):
    #     return value in self.data


class Iters3:

    def __init__(self, value):
        self.data = value

    def __getitem__(self, value):
        return self.data[value]

    # def __iter__(self):
    #     for item in self.data:
    #         yield item

    # def __contains__(self, value):
    #     return value in self.data


if __name__ == '__main__':
    for cls in range(1, 4):
        # It will be the same output for all the classes
        iters = eval(f'Iters{cls}([1, 2, 3, 4, 5])')
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

        print("\nEnd of the class output; \n\n")
