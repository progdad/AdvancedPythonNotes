# https://docs.python.org/3/howto/descriptor.html#simple-example-a-descriptor-that-returns-a-constant

class Descriptor:
    """
        Descriptor is an any object which defines the methods __get__(), __set__(), or __delete__().
        When a class attribute is a descriptor, its special binding behavior is triggered upon attribute lookup.
        Normally, using a.b to get, set or delete an attribute looks up the object named b in the class dictionary for a,
        but if b is a descriptor, the respective descriptor method gets called.
        TO USE THE DESCRIPTOR, IT MUST BE STORED AS A CLASS VARIABLE IN ANOTHER CLASS
    """

    def __get__(self, obj, objtype=None):
        return 10


class A:
    x = 5
    y = Descriptor()


d = Descriptor()
a = A()

print(d)  # <__main__.Ten object at 0x7fd949f79fa0>
print(a.y)  # 10

# In the a.x attribute lookup, the dot operator finds 'x': 5 in the class dictionary.
# In the a.y lookup, the dot operator finds a descriptor instance, recognized by its __get__ method.
# Calling that method returns 10.
