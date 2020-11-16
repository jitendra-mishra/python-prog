class Employee:
    'Class name for all employees'
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def displayEmployee(self):
        print("Name=%s, Salary=%d" %(self.name, self.salary))

emp1 = Employee("AAA", 100)
emp1.displayEmployee()
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )

print("emp1.name=", getattr(emp1, "name"))
setattr(emp1, "sex", "male")
print(emp1.sex)
if hasattr(emp1, "salary1"):
    print("Has salary")
else:
    print("Salary doesn't exist")
delattr(emp1, "name")
emp1.displayEmployee()
