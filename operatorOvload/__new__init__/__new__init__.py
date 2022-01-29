class Person:
    def __new__(cls, name, age):
        """
        This method is called to create a new instance. It is built-in static method in any class,
        so there is usually no need to define __new__ method in a simple class like this one.

        If __new__ returns None, then init won't be called
        """
        print('__new__ is called')
        return super().__new__(cls)  # object.__new__() receives only one parameter

    def __init__(self, name, age):
        print('__init__ is called')
        self.name = name
        self.age = age


tom = Person('Tom', 24)
annie = Person("Anna", 19)

# The output:
#      __new__ is called
#      __init__ is called
#      __new__ is called
#      __init__ is called
