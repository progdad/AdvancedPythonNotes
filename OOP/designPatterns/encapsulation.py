# Encapsulation is the OOP design pattern that is used to encapsulate object behaviour(its methods and attributes),
# and this is the convenient approach because it hides object realisation(that makes object interface much simpler),
# and makes name conflicts impossible to happen(if to use private variables, not protected)


# Protected variables can be accessed only within the package, when Private - only within the class


class C1:
    def set_c1(self):
        self.__X = 88  # This is the private attribute that can be accessed only within the C1 class

    def print_c1(self):
        print(self.__X)


class C2:
    def set_c2(self):
        self.__X = 99  # This is the private attribute as well, that can be accessed only within the C2 class

    def print_c2(self):
        print(self.__X)


class C3(C1, C2):
    pass


inst = C3()
inst.set_c1()
inst.set_c2()

inst.print_c1()  # 88
inst.print_c2()  # 99

# Actually private objects can be accessed by the syntax => <instanceName>._<className>__<privateVariableName>
print(inst.__dict__)  # {'_C1__X': 88, '_C2__X': 99}
print(inst._C1__X)  # 88
inst._C1__X = 10  # And you may set private attributes
inst.print_c1()  # 10
