from abc import ABC, abstractmethod


# You can see the whole example here >> https://docs.python.org/3/howto/descriptor.html#practical-application


class Validator(ABC):

    # Read about abstract classes and methods in "NotesAdvancedPython/abstractClass/chess.py" file

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class String(Validator):

    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Expected {value!r} to be an str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f'Expected {value!r} to be no smaller than {self.minsize!r}'
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f'Expected {value!r} to be no bigger than {self.maxsize!r}'
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(
                f'Expected {self.predicate} to be True for {value!r}'
            )


class Component:
    name = String(minsize=3, maxsize=10, predicate=str.isupper)

    def __init__(self, name):
        self.name = name


comp = Component('Widget')
# ValueError: Expected <method 'isupper' of 'str' objects> to be True for 'Widget'
