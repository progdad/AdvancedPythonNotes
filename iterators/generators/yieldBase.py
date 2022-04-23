def gensquares(n):
    yield from (x ** 2 for x in range(n))


for i in gensquares(10):
    print(i)  # 0 1 4 9 16 25 ...


iteratorForSure = gensquares(10)
print(gensquares)  # <function gensquares at 0x7ff4f5cc3ee0>
print(iteratorForSure)  # <generator object gensquares at 0x7ff2ce0dec10>
print(iteratorForSure is iter(iteratorForSure))  # True

for _ in range(5):
    print(iteratorForSure.__next__())  # 0 1 4 9 16

print(list(iteratorForSure))  # [25, 36, 49, 64, 81]
