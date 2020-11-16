class Parent():
    'I am the parent'
    parentAttr = 100
    def __init__(self):
        print("calling parent constructor")
    def parentMethod(self):
        print("parent method called")
    def setAttr(self, attr):
        Parent.parentAttr = attr
    def getAttr(self):
        return Parent.parentAttr
    def printParentAttr(self):
        print("Parent attr = ", Parent.parentAttr)

# child class inheriting parent class
class Child(Parent):
    def __init__(self):
        print("calling child constructor")
    def childMethod(self):
        print("child method called")

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
print(c.getAttr())
