class ReprStr:
    """
    __repr__ is used to keep object name in the low-level of the program,
    when __str__ is used by print() and str(). So that __repr__ method is more preferable.
    Also, they both must return a string
    """

    #def __repr__(self):
    #    return "ReprStr from __repr__"

    def __str__(self):
        return "Hi, I'm __str__"


child = ReprStr()
print(child)  # Hi, I'm __str__

herewego = [ReprStr(), ReprStr()]

# There is why __repr__ is more preferable:
print(herewego)  # [ReprStr from __repr__, ReprStr from __repr__]
# If __repr__ was not defined in the class, it would return this >> <__main__.ReprStr object at 0x7fdd608152e0>

print(herewego[1])  # Hi, I'm __str__
