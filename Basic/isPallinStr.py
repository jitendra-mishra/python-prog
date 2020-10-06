# Check if string is pallindrome or not

my_str = "Hello"

def reverseString(str):
    l = len(str)
    temp_str = ""
    for i in range(l):
        temp_str += str[l-i-1]
    print(temp_str)
    return temp_str

print(my_str)
my_str = reverseString(my_str)
print(my_str)