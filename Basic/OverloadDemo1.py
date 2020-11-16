#Overloading __add__() method and __str__() method
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return '(%d,%d)' %(self.a, self.b)
    def __add__(self, other):
        return A(self.a + other.a, self.b + other.b)

o1 = A(2,5)
o2 = A(1,6)
o3 = o1+o2
print(o3)