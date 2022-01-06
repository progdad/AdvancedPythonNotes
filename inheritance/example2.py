class AttrDisplay:

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{key} = {getattr(self, key)}')
        return ', '.join(attrs)

    def __repr__(self):
        return f'{self.__class__.__name__}: [{self.gatherAttrs()}]'


if __name__ == '__main__':

    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2


    class SubTest(TopTest):
        pass


    X, Y = TopTest(), SubTest()
    print(X)  # TopTest: [attr1 = 0, attr2 = 1]
    print(Y)  # SubTest: [attr1 = 2, attr2 = 3]
