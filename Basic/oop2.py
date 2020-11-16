class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)

    class Laptop:
        def __init__(self, brand, ram):
            self.brand = brand
            self.ram = ram
        def show(self):
            print(self.brand, self.ram)


lap1 = Student.Laptop('hp', 8)

s1 = Student("Jitu", 10)
s2 = Student("Sloku", 5)



print(s1.lap.brand)