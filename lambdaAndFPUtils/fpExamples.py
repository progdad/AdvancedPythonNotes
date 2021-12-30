from functools import reduce

lst = [i**2 for i in range(1, 21)]
print(lst)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

lst1 = list(map((lambda value: int(str(value)[::-1])), lst))
print(lst1)  # [1, 4, 9, 61, 52, 63, 94, 46, 18, 1, 121, 441, 961, 691, 522, 652, 982, 423, 163, 4]

lst2 = list(filter((lambda value: (value % 5 == 0) or (value % 9 == 0)), lst))
print(lst2)  # [9, 25, 36, 81, 100, 144, 225, 324, 400]

sumitems = reduce((lambda x, y: x + y), lst)
print(sumitems)  # 2870

superlam = lambda x: (lambda y, z: str(y**z) * x)
child = superlam(3)
print(child)  # <function <lambda>.<locals>.<lambda> at 0x7f1bbb633f70>
print(child(4, 4))  # 256256256
