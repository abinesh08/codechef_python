X=[[1,2,3],
   [4,6,6],
   [7,8,9]]
Y=[[1,2,3],
   [4,6,6],
   [7,8,9]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(Y)): #if we put X or Y will get same result
    for j in range(len(Y[0])):
        result[i][j]= X[i][j] +  Y[i][j]
for r in result:
    print(r)