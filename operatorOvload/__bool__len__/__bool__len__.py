class WithBool:

    """
    If __bool__ method is not defined, then class uses __len__ method in bool operations,
    by counting length of any data that requested for review in __len__.

    If both methods are not defined, then class becomes True automatically

    Without __len__ method your class is not able being used by len(YourClassInstance)
    """

    def __init__(self, *args):
        self.data = list(args)

    def __bool__(self):
        return True if self.data else False

    def __len__(self):
        length = 0
        for item in self.data:
            length += 1
        return length


data, nodata = WithBool(1, 3, 2, 5), WithBool()
print(bool(data), bool(nodata))  # True False
print(len(data), len(nodata))  # 4 0
