list1=[1,2,3,4,5]
def data1(b):
    return b**2
print(list(map(data1,list1)))

#

def addition(n):
    return n

numbers = (2, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

#reduce
from functools import reduce
def addition1(a,b):
    return a+3*b

reduce(addition1,numbers)
reduce(lambda a,b:a+3*b,numbers)