# Delegation is an implementation of a necessary object functionality
# by the use of the another object (a shift of the responsibility).

class Wrapper:
    def __init__(self, objct):
        self.wrapped = objct

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)  # That's exactly the delegation
