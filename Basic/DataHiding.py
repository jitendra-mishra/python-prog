# data hiding.. restrict access of a class attribute outside of class
class A:
    __count = 0
    def count(self):
        self.__count += 1
        print("count=", self.__count)

o1 = A()
o1.count()
o1.count()
print(o1._A__count)