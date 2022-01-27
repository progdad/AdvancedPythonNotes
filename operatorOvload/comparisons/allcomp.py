class AllCompMethods:
    def __init__(self, string):
        self.string = string

    def __eq__(self, other):
        return "__eq__", self.string == other

    def __ne__(self, other):
        return "__ne__", self.string != other

    def __gt__(self, other):
        return "__gt__", self.string > other

    def __lt__(self, other):
        return "__lt__", self.string < other

    def __ge__(self, item):
        return "__ge__", self.string >= item

    def __le__(self, other):
        return "__le__", self.string <= other


inst = AllCompMethods("something")
print(inst == "something")  # ('__eq__', True)
print(inst != "someone")  # ('__ne__', True)
print(inst > "python")  # ('__gt__', True)
print(inst < "good")  # ('__lt__', False)
print(inst >= "somethinnn")  # ('__ge__', False)
print(inst <= "somethin")  # ('__le__', False)
