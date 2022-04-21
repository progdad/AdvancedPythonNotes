from abc import ABC, abstractmethod


# Abstract class is a class that contains one and more abstract methods.
# Abstract method is a method that's been defined but not implemented.
# Abstract class cannot be instanced, it must be a class that's going to be inherited,
# and all its methods are going to be implemented in a class that's going to inherit an abstract class,
# and only then you can create an instance of a class.
# Python has no built-in support for abstract classes, for this goal you need to use "abc" module from PyPi


class Figure(ABC):
    # This is a general method that draws a figure, that's used by all the classes of figures
    def draw(self):
        print("Here's supposed to be a code to draw a chess figure")

    # The abstract method that must be implemented in all the heir clas
    @abstractmethod
    def move(self):
        pass


class Queen(Figure):
    def move(self):
        print("Moved Queen to e2e4")


queen = Queen()
queen.draw()  # Here's supposed to be a code to draw a chess figure
queen.move()  # Moved Queen to e2e4

try:
    absClassHeir = Figure()
except TypeError as typeErr:
    print(typeErr)  # Can't instantiate abstract class Figure with abstract method move


# The example was taken from http://pythonicway.com/education/python-oop-themes/33-python-abstract-class
