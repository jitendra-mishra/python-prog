# print sting which is passed as a list which has length more than 5 letters
def my_fun(my_list):
    for s in my_list:
        if len(s) > 5:
            print(s)

lst = ['Jitu','Jitendra', 'Mita', 'Madhu', 'Samruddhi', 'Sambhrant']
my_fun(lst)