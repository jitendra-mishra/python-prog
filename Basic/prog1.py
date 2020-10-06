# add 2 numbers
num1 = 10
num2 = 20
sum = num1 + num2
print("Sum=", sum)
print("Sum of {0} and {1} = {2}".format(num1, num2, sum))

# add 2 number provided as input
num1 = input("Enter number 1:")
num2 = input("Enter number 2:")
sum = float(num1) + float(num2)
print("Sum of {0} and {1} is equal to {2}".format(num1, num2, sum))

## assgin value to multiple variable
x , y, z = 1,3,5
print(x)
print(y)
print(z)
x = y = z = 10

x = "outer"
def myfun():
    global p
    p = 'hello'
    x = "inner"
    print('I am', x)
myfun()
print("I am {0}".format(p))