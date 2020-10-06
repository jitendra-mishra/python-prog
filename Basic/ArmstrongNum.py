#A positive integer is called an Armstrong number of order n if# we should get the same number
#abcd... = an + bn + cn + dn + ...

num = 407

"""
get the number of digits
"""
temp = num
c = 0
while temp != 0:
    temp = temp//10
    c = c+1

def isArmstrong(num):
    temp = num
    sum = 0
    while temp != 0:
        rem = temp % 10;
        sum = sum + pow(rem, c)
        temp = temp//10
        print("Rem={0}, sum={1} temp={2}".format(rem, sum, temp))
    return (sum == num)

print(isArmstrong(num))