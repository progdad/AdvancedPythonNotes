ls = [1, 4, 9, 16, 25]
iterator_ls = iter(ls)  # Can be iterated over only once as well
while True:
    try:
        print(iterator_ls.__next__())
    except StopIteration:
        break


# File object is an iterator
file = open("example.txt")
print(file.__next__())
print(file.__next__())


lst = [n**2 for n in range(5)]  # list is not iterator as dict and tuple;
print(lst is iter(lst))  # False
