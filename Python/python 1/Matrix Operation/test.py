a = [
    [1,2],
    [3,4]
]

b = [
    [5,6],
    [7,8]
]

for i in range(0, len(a)): # i = 1
    print(a[i])
    for z in range(0, len(a[0])):
        print(a[i][z])