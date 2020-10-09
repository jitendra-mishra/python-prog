# Program to sort alphabetically the words form a string provided by the user
my_str = "Hello this Is an Example With cased letters"

words = my_str.split(" ")
words.sort()

for w in words:
    print(w)