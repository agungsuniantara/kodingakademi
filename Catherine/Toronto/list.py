data = [10,20,30,40] # 0, 1, 2, 3

print(data[0])

for i in data:
    print(i)

print(data[1 : 3])
print(data[1:])
print(data[-4:-2])

data.append(10)
print(data)

data.insert(1, 100)
print(data)

del data[1]
print(data)

data.remove(20)
print(data)

store = data.pop(1)
print(store)

data2 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(data2[1][1])

for i in data2:
    for z in i:
        print(z)

print(len(data))
print(len(data2))

for i in range(10):
    print(i)

data3 = [2 * x for x in range(10)]
print(data3)