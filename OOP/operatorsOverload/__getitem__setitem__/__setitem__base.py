class IndexerAndSetter:
    def __init__(self, *args):
        self.data = list(args)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __index__(self):
        """
        __index__ is absolutely not related with indexing,
        it just adds the possibility to use IndexerAndSetter as an index in list indexing.
        """

        return 255


child = IndexerAndSetter(1, 3, 4, 5, 7)

# __setitem__
child[4] = 10
print(child.data)  # [1, 3, 4, 5, 10]

# __index__
print([i*2 for i in range(1000)][child])  # 510
