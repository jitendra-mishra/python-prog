from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def abc(self):
        print('abc')
    def process(self):
        print("process -Laptop")

#c1 = Computer()
com1 = Laptop()
com1.abc()



