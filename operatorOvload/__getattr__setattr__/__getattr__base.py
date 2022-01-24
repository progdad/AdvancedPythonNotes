class Nothing:
    age = 30

    def __getattr__(self, attrname):
        """
            __getattr__ is not called when attribute is somewhere in class tree.
            It calls out only when there is no such attribute name in the tree
        """
        if attrname == "age":
            return "In this case, code will never be here"
        elif attrname == "python":
            return "developer"
        raise AttributeError(f"no such attribute: {attrname}")


noth = Nothing()
print(noth.age, noth.python)
print(noth.err)
