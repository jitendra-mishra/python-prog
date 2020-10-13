# pass list to a function and returns number of even and odd numbers
def getOddEven(my_lst):
    even = odd = 0
    l = []
    print("Empty list", l)
    for i in my_lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd



lst = [2, 5, 3, 9, 10, 6, 19, 20, 11, 99]
print(getOddEven(lst))
