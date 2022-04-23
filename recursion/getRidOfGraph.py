def indepth(lst, another):
    for x in lst:
        if not isinstance(x, list):
            another.append(x)
        else:
            indepth(x, another)


LST = []
indepth([[[[[1], 2], 3], 4], 5, [6, [7, 8], [9, 10, [11, 12]]]], LST)
print(LST)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
