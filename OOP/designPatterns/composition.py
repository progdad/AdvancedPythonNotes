# Composition or AGGREGATION is an implementation of objects
# within the other object to make this object completed from separated parts.
# Say the way simpler, composition is used to collect ONE completed object from several separated ones.

# Do not confuse composition with inheritance.
# Inheritance involves belonging to some base object,
# when composition is the formation of a whole object from separated parts


class Heart:
    pass


class Brain:
    pass


class Human:
    def __init__(self):
        self.heart = Heart()
        self.brain = Brain()

        # And there we can use the attributes methods and behaviour
