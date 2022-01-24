class Access:
    age = 30

    def __setattr__(self, key, value):
        if key == "age":
            self.__dict__[key] = value


acc = Access()
acc.age = 100