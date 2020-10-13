# Programs related to functions in Python

#Function returning multiple values - possible in python
def fun1(a, b):
    print(a)
    print(b)
    return a, b

x, y = fun1(10,20)
print(x, y)

#Function with default values
def fun_default(name, age=18):
    print(name)
    print(age)
    age = age-5
    print(age)
fun_default('jitu')

#Function with value passed as keywords
def fun_key(name, age=50):
    print("name=", name)
    age = age-5
    print("age=", age)
fun_key(name='hitu',age=40)

#Variable number of arguments in a function
def fun_var(*num):
    print(len(num))
    
fun_var(10,20,'jitu',4.5)

#keyword with variable number of arguments
def fun_keyword_var(name, **data):
    print("name=", name)
    for i, j in data.items():
        print(i, j)
    print(data)

fun_keyword_var('jitu', age=22, city='blore', mob=94835)

