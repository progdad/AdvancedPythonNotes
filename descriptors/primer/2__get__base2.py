# https://docs.python.org/3/howto/descriptor.html#dynamic-lookups

import os


class DirectorySize:
    def __get__(self, obj, objtype=None):
        print(obj, '_____', objtype)  # Instance of directory, self.dirname="../../" _____ <class '__main__.Directory'>
        return len(os.listdir(obj.dirname))


class Directory:
    size = DirectorySize()

    def __init__(self, dirname):
        self.dirname = dirname

    def __repr__(self):
        return f"Instance of directory, self.dirname=\"{self.dirname}\""


dir1 = Directory("../../")
dir2 = Directory("../../operatorsOverload")
print(dir1.size)  # 5
print(dir2.size)  # 10

# Besides showing how descriptors can run computations,
# this example also reveals the purpose of the parameters to __get__().
# The "self" parameter is "size", an instance of "DirectorySize" class.
# The "obj" parameter is either dir1 or dir2, an instance of Directory.
# It is the obj parameter that lets the __get__() method learn the target directory.
# The objtype parameter is the class Directory.
