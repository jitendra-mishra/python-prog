class A:
    def show(self):
        print("A-show")

class B(A):
    def show(self):
        print("B-show")

a1 = B()
a1.show()