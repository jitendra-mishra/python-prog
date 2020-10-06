arr1 = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
arr2 = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
print(arr1)
row = len(arr1)
col = len(arr1[0])
print("row=",row,",col=",col)
for i in range(row):
    for j in range(col):
        result[i][j] = arr1[i][j] + arr2[i][j]

for i in range(row):
    for j in range(col):
        print(result[i][j], end=" ")
    print()

