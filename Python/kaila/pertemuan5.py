# matrix / multidimensi list

matrix1 = [["nasi goreng", "mie goreng"], ["jus alpukat", "jus tomat"]]

nomer = 1

for i in matrix1:
    for z in i:
        print(f"{nomer}. {z}")
        nomer += 1

data1 = [
    [2, 1],
    [3, 2]
]

data2 = [
    [3, 4],
    [5, 6]
]

print("addition : ")
# addition
for i in range(len(data1)):
    for z in range(len(data2[0])):
        hasil = data1[i][z] + data2[i][z]
        print(hasil)

print("subtraction : ")
# subtraction
for i in range(len(data1)):
    for z in range(len(data2[0])):
        hasil = data1[i][z] - data2[i][z]
        print(hasil)

data3 = []

for x in range(len(matrix1)):
    row = []
    for y in range(len(matrix1[0])):
        total = 0
        for z in range(len(matrix1)):
            total = total + (data1[x][z] * data2[z][y])
        row.append(total)
    data3.append(row)

print(data3)


