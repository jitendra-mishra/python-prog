num = 5
def fibo(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)

print(fibo(9))

#Fibo using another way
number = 4
f0 = 0
f1 = 1
if number <= 0:
    print("Wrong argument")
if number == 1:
    print(f0, end=" ")
elif number == 2:
    print(f0, end=" ")
    print(f1, end=" ")
else:
    print(f0, end=" ")
    print(f1, end=" ")
    for i in range(2, number):
        sum = f0 + f1
        f0 = f1
        f1 = sum
        print(f1,  end=" ")

print()
print()
#fibonacci series
def fibo3(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

fibo3(4)