class Student:
    school = 'UCE'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def get_classinfo():
        print("This is Student class")


s1 = Student(23, 11, 56)
s2 = Student(24, 67, 89)

print(s1.average())
print(s2.average())

print(Student.get_school())
Student.get_classinfo()
