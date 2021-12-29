def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot
    
print(sumtree([[[[ [1], 2], 3], 4], 5]))
