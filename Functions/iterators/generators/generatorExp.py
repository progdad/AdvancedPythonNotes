genexp = (tpl for tpl in enumerate(num ** 2 for num in range(100)))

print(genexp)  # <generator object <genexpr> at 0x7fba649ad890>
print(genexp is iter(genexp))  # True

for _ in range(55):
    print(genexp.__next__())
print("\nSeparator :)\n")

# Let's see from where items of genexp are printed
while True:
    try:
        print(genexp.__next__())
    except StopIteration:
        break

# Generator expression can be iterated over only once.
print(list(genexp))  # []
