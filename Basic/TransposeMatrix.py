arr = [[1,2,3],
        [4,5,6],
        [7,8,9]]

##Transpose should be
#[1,4,7]
#[2,5,8]
#[3,6,9]
def printArray():
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=" ")
        print()

rows = len(arr)
cols = len(arr[0])

print("Original Matrix:: ")
printArray()

for i in range(rows):
    for j in range(cols):
        if i == j or i > j:
            continue
        else:
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp
print("After Transpose Matrix:: ")
printArray()
