# program to remove punctuation from a string

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, he said ---and went."

temp = ""
for c in my_str:
    if c not in punctuations:
        temp += c

print(temp)
