data1d = [1, 2, 3] # 1D
data2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] # 2D
print(data1d[1])
print(data2d[0][1])

for i in data2d:
    print(i)
    for z in i:
        print(z)

