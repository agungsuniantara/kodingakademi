matrix1 = [
    [4, 0],
    [2, 1],
]

print("matriks 1")
for list in matrix1:
    print(list)

print()

matrix2 = [
    [4, 1],
    [7, 5],
]

print("matriks 2")
for list in matrix2:
    print(list)

print()

# pertambahan matriks
for x in range(len(matrix1)): 
    for y in range(len(matrix2)):
        print("[",matrix1[x][y] + matrix2[x][y],"]", end='')
    print()

print()

# pengurangan matriks
for x in range(len(matrix1)): 
    for y in range(len(matrix2)):
        print("[",matrix1[x][y] - matrix2[x][y],"]", end='')
    print()