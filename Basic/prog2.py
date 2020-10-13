def person(name, **data):
    for i,j in data.items():
        print(i,j)
        print(data.get(i))
    print(data)

person('navin', age=25,city='blore',mob=98567)

