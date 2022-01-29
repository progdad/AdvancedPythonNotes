class ForAPI:
    def __call__(self, *args, **kwargs):
        """
            Is used to handle any arguments called by class instances.
            Third by popularity magic method after __init__ constructor and __repr__, __str__
        """
        return 'Called: ', args, kwargs


callableCls = ForAPI()
print(callableCls('Arguments', 1, 2, 3, ddd=222, soup="Beautifulsoup"))
# ('Called: ', ('Arguments', 1, 2, 3), {'ddd': 222, 'soup': 'Beautifulsoup'})
