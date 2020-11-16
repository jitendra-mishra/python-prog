from functools import reduce

# example of using lamda
def sum(a, b):
    return a+b

multi = lambda a,b: a*b
add = lambda a,b: a+b
print(add(10,20))

def is_even(n):
    return n%2 == 0

lst=[2,5,6,9,10,11]
evens = list(filter(is_even, lst))
evens1 = list(filter(lambda n: n%2 == 0, lst))
print(evens1)
def update(n):
    return n*2

doubles = list(map(update, evens1))
doubles1 = list(map(lambda n: n*2, evens1))
print(doubles1)

def add_all(a,b):
    return a+b

sum = reduce(lambda a,b: a+b , doubles1)
print(sum)