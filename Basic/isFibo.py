import math


def isPerfectQuare(x):
    s = int(math.sqrt(x))
    return s * s == x


def isFibo(num):
    # 5*n*n+4 or 5*n*n-4 is a perfect square
    return isPerfectQuare(5 * num * num + 4) or isPerfectQuare(5 * num * num - 4)


for i in range(1, 11):
    if isFibo(i):
        print(i, "is a is a Fibo number")
    else:
        print(i, "is a is NOT a Fibo number")
