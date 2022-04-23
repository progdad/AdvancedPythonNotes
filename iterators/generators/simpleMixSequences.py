# First method
def scramble(seq):
    yield from (seq[x:] + seq[:x] for x in range(len(seq)))


print(list(scramble("something")))  # ['something', 'omethings', 'methingso', 'ethingsom', 'thingsome', 'hingsomet', 'ingsometh', 'ngsomethi', 'gsomethin']
###


# Second method
string = "spam"
genexp = (string[i:] + string[:i] for i in range(len(string)))
print(list(genexp))  # ['spam', 'pams', 'amsp', 'mspa']
# ###


# Third method
func = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print(func)  # <function <lambda> at 0x7fd297266f70>
print(func("str"))  # <generator object <lambda>.<locals>.<genexpr> at 0x7fd2972ae9e0>

gen = func((1, 2, 3, 4, 5))
print(gen.__next__())  # (1, 2, 3, 4, 5)
print(gen.__next__())  # (2, 3, 4, 5, 1)
print(list(gen))  # [(3, 4, 5, 1, 2), (4, 5, 1, 2, 3), (5, 1, 2, 3, 4)]
###
