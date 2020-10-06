
def sum(num):
    if(num==1):
        return 1
    else:
        return (num+sum(num-1))

num = 5

print(sum(num))

