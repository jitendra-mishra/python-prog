# Program to find the factorial of a number

#Case-1 - Using recursive call
def factorial(num):
    assert num >= 0, "Invalid number"
    return 1 if (num==1 or num==0) else num*factorial(num-1)
x = 6
print("Factorial of {0} is {1}".format(x, factorial(x)))

#Case-2 - Using loop
def factorial1(num):
    assert num >= 0, "Invalid number"
    if(num==1 or num==0):
        return 1
    else:
        fact=1
        while num!=1:
            fact = fact*num
            num-=1
        return fact
y = 3
print("Factorial of {0} is {1}".format(y, factorial1(y)))

#case-3
def fact3(num):
    fact = 1
    if num < 0:
        print("Invalid number")
    elif num == 0:
        return fact
    else:
        for i in range(1, num+1):
            fact = fact * i
    return fact

print(fact3(4))
