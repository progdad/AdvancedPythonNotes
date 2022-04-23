ls = [1, 4, 9, 16, 25]
iterator_ls = iter(ls)  # Can be iterated over only once as well
while True:
    try:
        print(iterator_ls.__next__())  # 1 4 9 16 25
    except StopIteration:
        break


# File object is an iterator
file = open("example.txt")
print(file.__next__())  # Something 1
print(file.__next__())  # Something 2


lst = [n**2 for n in range(5)]  # list is not an iterator and dict and tuple as well
print(lst is iter(lst))  # False


import os
allDocsDirs = os.walk("../")
print(allDocsDirs)  # <generator object _walk at 0x7fb5eaa0fc10>
print(allDocsDirs is iter(allDocsDirs))  # True
print(allDocsDirs.__next__())  # ('../', ['iters', 'generators'], [])
# Generators also can be opened by a "star"
print(*(dr[0] for dr in allDocsDirs))  # ../iters ../generators

while True:
    try:
        print(allDocsDirs.__next__())  # StopIteration ERROR
    except StopIteration:
        print("Only once !")
        break
