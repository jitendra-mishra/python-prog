a = 40
b = a
c = [b]

print(a,b,c)

del a
print(b,c)
b = 100
print(b,c)
c [0] = -10
print(b,c)

__del__()