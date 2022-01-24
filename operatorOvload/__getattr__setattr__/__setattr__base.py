class Avanger:
    def __init__(self, age=27):
        self.age = age

    def __setattr__(self, key, value):

        """
        __setattr__ always takes over the role of adding new variables in class.
        You have to use <self.__dict__[key]> to add new variable.

        :param key: in <acc.age = 10> age is key
        :param value: in <acc.age = 10> 10 is value
        """

        if key in ["age", "name", "surname", "gender", "resp"]:
            self.__dict__[key] = value
        else:
            raise PermissionError(f"no permissions to add '{key}' attribute")


blackwidow = Avanger()
blackwidow.name, blackwidow.surname = "Natasha", "Romanoff"
blackwidow.gender = "Woman"
print(blackwidow.__dict__)

blackwidow.status = "Dead :("
