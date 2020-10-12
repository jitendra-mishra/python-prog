# Program to sort alphabetically the words form a string provided by the user
my_str = "Hello this Is an Example With cased letters"

word_list = my_str.split(" ")
word_list.sort()

for word in word_list:
    print(word)
