
f=10

def someFun():
    global f
    f=1
    print(f)

def main():
    print("Helo")
if __name__ == "__main__":
    main()
    someFun()
    print(f)