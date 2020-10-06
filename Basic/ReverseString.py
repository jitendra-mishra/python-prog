# Program to reverse a string
my_str = "BangalorE"

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


# method-4 using slice syntax
def reverseString4(str):
    return str[::-1]


# method-5 using join and reversed method
def reverseString5(str):
    return "".join(reversed(str))



print("Original str=", my_str)
my_str = reverseString5(my_str)
print("Reversed str=", my_str)


