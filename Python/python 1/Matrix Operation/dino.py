matrix1 = [
    [1,2],
    [3,4]
]

matrix2 = [
    [10,20],
    [30,40]
]

det = (matrix2[0][0] * matrix2[1][1]) + (matrix2[0][1] * matrix2[1][0])

for i in range(len(matrix1)): 
    for z in range(len(matrix1)): 
        print(matrix1[i][z] + matrix2[i][z], end = " ")
    print(" ")
    
matrix3 = []

for i in range(len(matrix1)):  # i = 0
    row = [] # [30]
    for z in range(len(matrix1)): # z = 1
        total = 0
        for c in range(len(matrix1)): # c = 0
            hasil = matrix1[i][z] * matrix2[z][c]
            total += hasil
        row.append(total)
    matrix3.append(row)

print(matrix3)
    
        