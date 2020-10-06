# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

rows = len(X)
cols = len(Y[0])

for i in range(rows):
    for j in range(cols):
        for k in range(len(Y)):
            result[i][j] = result[i][j] + (X[i][k] * Y[k][j])

for r in result:
   print(r)