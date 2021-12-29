from functools import reduce

lst = [i**2 for i in range(1, 1001)]
print(lst,  end='\n\n\n')

lst1 = list(map((lambda value: int( str(value)[::-1] )), lst ))  # It's a list where all the numbers from list lst are reversed: (625 > 526), (1024 > 4201)
print(lst1, end='\n\n\n')

lst2 = list(filter((lambda value: (value % 5 == 0) and (value % 9 == 0)), lst))  # This list contnains only numbers that are divided by 5 and 9 the same time
print(lst2, end='\n\n\n')

lst3 = reduce((lambda x, y: x+y), lst)  # And there is the sum of all the lst numbers multiplied by 2
print(lst3, end='\nThis is the end !!!\n')

superlambda = lambda x: (lambda y, z: str(y**z) * x)
child = superlambda(3)
print(child, type(child))
print(child(10, 2))
print(child(4, 4))
 
