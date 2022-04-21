# https://docs.python.org/3/howto/descriptor.html#managed-attributes


class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        print(f'Accessing age giving {value}')
        return value

    def __set__(self, obj, value):
        print(f'Updating age to {value}')
        obj._age = value


class Person:

    age = LoggedAgeAccess()

    def __init__(self, name, age):
        self.name = name
        self.age = age                  # Calls __set__()

    def birthday(self):
        self.age += 1                   # Calls both __get__() and __set__()
        # That's clear better when you replace self.age += 1 to this:
        # age = self.age
        # self.age = age + 1


hero = Person("Zelensky", 44)  # INFO:root:Updating age to 44

print(hero.__dict__)  # {'name': 'Zelensky', '_age': '44'}
print(hero.age)  # 44
hero.birthday()
print(hero.name, hero.age)  # Zelensky 45

# The full OUTPUT is:
    # INFO:root:Updating age to 44
    # {'name': 'Zelensky', '_age': 44}
    # INFO:root:Accessing age giving 44
    # 44
    # INFO:root:Accessing age giving 44
    # INFO:root:Updating age to 45
    # INFO:root:Accessing age giving 45
    # Zelensky 45


# One major issue with this example is that the private name _age is hardwired in the LoggedAgeAccess class.
# That means that each instance can only have one logged attribute and that its name is unchangeable.
# In the "4_customize_names.py" file the issue will be solved.
