class Iters:

    """
    This class do the same as 'Iters' class from __contains__iter__next.py
    But it is much shorter and also more readable than the code from the file mentioned above
    """

    def __init__(self, value):
        self.data = value

    def __getitem__(self, value):
        return self.data[value]

    def __iter__(self):
        for item in self.data:
            yield item

    def __contains__(self, value):
        return value in self.data
