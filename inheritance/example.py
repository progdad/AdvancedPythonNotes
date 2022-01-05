class Person:
    # Марк Лутц. Изучаем Python, глава 28
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self. job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return f'[Person: {self.name}, {self.pay}]'


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            yield person


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaises(.10)
    for employee in development.showAll():
        print(employee)

    # [Person: Bob Smith, 0]
    # [Person: Sue Jones, 110000]
    # [Person: Tom Jones, 60000]
