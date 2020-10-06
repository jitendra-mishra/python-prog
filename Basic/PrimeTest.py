num = 91

def isprime(num):
    if num == 1 or num == 2:
        return True
    found = True
    for x in range(2, num//2+1):
        if (num%x == 0):
            found = False
            break
    return found

def isprime2(num):
    if num == 1 or num == 2:
        return True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

for x in range (1,100):
    print("Number is ", x, " and prime=", isprime(x))