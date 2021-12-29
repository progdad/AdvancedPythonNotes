lst = [n**2 for n in range(5)]
print(lst is iter(lst))  # Can't use __next__() method to list

dct = {n: n**2 for n in range(5)}
print(dct is iter(dct))  # The same thing with dict, it is not iterator


# But file object is the iterator
with open("exmpl.txt", "w") as f:
    for n in range(10):
        f.write(f"Something {n + 1}\n")


file = open("exmpl.txt")
print(file.__next__())
print(file.__next__())

