class A:
    def __init__(self):
        print("A class constructor")
class B:
    def __init__(self):
        print("B class constructor")
class C(A, B):
    def __init__(self):
        print("C class constructor")
class D:
    def __init__(self):
        print("D class constructor")

def main():
    cobj = C()
    print(isinstance(cobj, D))

if __name__ == '__main__':
    main()