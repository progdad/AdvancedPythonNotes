# https://docs.python.org/3/howto/descriptor.html#customized-names


# In this example, the Person class has two descriptor instances, name and age.
# When the Person class is defined, it makes a callback to __set_name__() in LoggedAccess
# so that the field names can be recorded, giving each descriptor its own public_name and private_name


class LoggedAccess:

    def __set_name__(self, owner, name):
        """
            Optionally, descriptors can have a __set_name__() method.
            This is only used in cases where a descriptor needs to know
            either the class where it was created
            or the name of class variable it was assigned to
        """
        print(f"Setting public_name={name} to {owner}")
        self.public_name = name
        print(f"Setting private_name=_{name} to {owner}")
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        print(f'Accessing {self.public_name} giving {value}')
        return value

    def __set__(self, obj, value):
        print(f'Updating {self.public_name} to {value}')
        setattr(obj, self.private_name, value)


class Person:
    name = LoggedAccess()  # First descriptor instance
    age = LoggedAccess()  # Second descriptor instance

    def __init__(self, name, age):
        self.name = name  # Calls the first descriptor
        self.age = age  # Calls the second descriptor

    def birthday(self):
        self.age += 1


dima = Person("Dima", 11)

print(dima.__dict__)  # {'_name': 'Dima', '_age': 11}
print(dima.age)  # 11
dima.birthday()
print(dima.name, dima.age)  # Dima 12


# The OUTPUT:
    # Setting public_name=name to <class '__main__.Person'>
    # Setting private_name=_name to <class '__main__.Person'>
    # Setting public_name=age to <class '__main__.Person'>
    # Setting private_name=_age to <class '__main__.Person'>
    # Updating name to Dima
    # Updating age to 11
    # {'_name': 'Dima', '_age': 11}
    # Accessing age giving 11
    # 11
    # Accessing age giving 11
    # Updating age to 12
    # Accessing name giving Dima
    # Accessing age giving 12
    # Dima 12
