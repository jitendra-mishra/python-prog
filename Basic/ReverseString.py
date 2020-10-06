# Program to reverse a string
my_str = "Jitendra"

#method1 using loop
def reversedString(str):
    l = len(str)
    temp_str = ""
    for i in range(l):
        temp_str+=str[l-i-1]
    return temp_str

#method 2 better way
def reverseString2(str):
    temp_str = ""
    for c in str:
        temp_str = c + temp_str
    return temp_str

#method3 - using recursion
def reverseString3(str):
    if str == "":
        return ""
    return reverseString3(str[1:]) + str[0]

print("Original str=", my_str)
my_str = reverseString3(my_str)
print("Reversed str=", my_str)
