def f1():
    print("A")
    return None


def f2():
    print("B")
    return "B"


def f3():
    print("UNREACHABLE")
    return "C"


checkpoints = [f1, f2, f3]

result = next(filter(None, (chp() for chp in checkpoints)), None)
if result:
    print(f"Result {result}")  # Result B

# That's how it works:
# filter() is an iterator(it has __next__ and __iter__ magic methods), so we can use it with next() built-in function.
# filter() takes a genexp(generator expression) as an iterable object for the second parameter,
# so next() calls filter() next item, and this is None object that returns f1 function.
# This is not valid item so filter() doesn't take this object.
# Then next() calls filter() again and only here f2 function is called and returns True object. <result == "B">
# That's all, for better understanding read about generator expressions.
# ** Generator does not create all its items in the time when generator is initialized.
# ** Generator returns by one element in a time, when it's called.
# ...
# Parameters Explanation:
# next() takes a sequence as a first parameter, it is required parameter,
# and the second one is an optional parameter where you set a default value,
# that's going to be returned if all elements in an iterator were already returned.
# ...
# filter() takes a function as a first parameter,
# and this function filters elements that are coming from iterable object,
# that's the second filter() parameter.
# In case with None, as a first parameter, filter() takes only "True" objects from an iterable.
