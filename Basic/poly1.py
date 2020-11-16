class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        return Student(self.m1+other.m1, self.m2+other.m2)
    def show(self):
        print("m1=", self.m1, "m2=", self.m2)
    def __gt__(self, other):
        return True if((self.m1+self.m2) > (other.m1+other.m2)) else False
    def __str__(self):
        return '{} {}'.format (self.m1, self.m2)



s1 = Student(60,20)
s2 = Student(50,10)

s3 = s1+s2
s3.show()
if (s1 > s2):
    s1.show()
else:
    s2.show()

print(s3)