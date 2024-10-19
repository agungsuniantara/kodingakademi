print("range 1 parameter : ")
for i in range(2):
    print(i)

print("range 2 parameter : ")
for i in range(1, 6): # start, stop
    print(i)

print("range 3 parameter : ")
for i in range(1, 6, 2): # start, stop, step
    print(i)

begin = 1 # 10
end = 10

while begin < end: # looping that will be doing loop if condition is true
    begin += 1

# assignment :

# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ......
# 9 x 9 = 82

# answer :

print("result : ")

for i in range(1, 10) : # i = 2
    for z in range(1, 10): # z = 2
        print(f"{i} * {z} = {i * z}") # 2 * 2 = 4

print("star 1 : ")

for i in range(5): # i = 4
    for z in range(5): # z = 0
        print("*", end = "")
    print("")

print("star 2 : ")

for i in range(5):
    for z in range(5):
        if i >= z:
            print("*", end = "")
    print("")

# list 1 dimension

data = [10,20,30]

# index
print(data[0], data[1], data[2])
data[0] = 89
print(data)

# append
data.append(80)
print(data)

# insert
data.insert(1, 100)
print(data)

# del
del data[4]
print(data)

# remove
data.remove(100)
print(data)

# join (string)
kata = "".join(str(data))
print(kata)

# split
kata = "hey halo maybe"
data_split = kata.split()
print(data_split)

# list multidimension

data = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# index
print(data[0])
print(data[0][1])

# append
data[0].append(100)
print(data)

# using for in list

data = [10,20,30]

for i in data:
    print(i)

for i in range(len(data)):
    print(data[i])

# using for in multidimension list:

data = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

for i in data:
    for z in i:
        print(z)

for i in range(len(data)):
    for z in range(len(data[i])): # i = row, z = column
        print(data[i][z])








