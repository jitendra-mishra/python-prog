from functools import reduce

def is_even(n):
    return n%2
def update(n):
    return n*2
def add_all(a,b):
    return a+b
nums = [2,6,4,19,11,20,34,122]

evens = list(filter(lambda n: n%2 == 0, nums))
print(evens)
doubles = list(map(lambda n: n*2, evens))
print(doubles)

sum = reduce(lambda a,b: a+b,doubles)
print(sum)
