# Inheritance is the pattern, that gives an ability to an object to use methods and attributes
# of the inherited class(AttrDisplay), without redefining them in the base class(TopTest, Subtest).

# Inheritance is necessary when some object behaviour may belong to any other object, parent object.
# For example class "Human" can be inherited by a class "Programmer",
# as well as "Dog" can be inherited from "Animal".


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
