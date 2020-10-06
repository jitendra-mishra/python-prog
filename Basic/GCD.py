# method-1
def gcd1(a, b):
    gcd = 0
    for i in range(1, a+1):
        if (a%i == 0 and b%i == 0):
            gcd = i
    return gcd

print(gcd1(98,56))

#method-2 using while loop
def gcd2(a, b):
    while b != 0:
        temp = b
        b = a%b
        a = temp
    return a
print(gcd2(10,70))

#method using recursion
def gcd3(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd3(a-b, b)
    if b > a:
        return gcd3(a, b-a)

print(gcd3(98,56))

# best mehod using recursion
def gcd4(a, b):
    if b == 0:
        return a
    return gcd4(b, a%b)

print(gcd4(54,24))


