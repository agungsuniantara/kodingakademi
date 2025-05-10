data = [1,2,3,4,5] # list 1 dimensi (1D) 
multi = [[1,2,3], [4,5,6]] # list 2 dimensi (2D)

print(data[0])
print(multi[0])
print(multi[0][0])
print(multi[1][2])

multi[0][1] = 100
print(multi)

data = [10,20,30,40,50]
a = data # pass by reference

a[0] = 100

print(a)
print(data)

# copy 

data = [10,20,30,40,50]
a = data.copy()

a[0] = 100

print(a)
print(data)

# deepcopy

from copy import deepcopy

multi = [[1,2,3],[4,5,6],10]
data_copy = deepcopy(multi)

data_copy[0][0] = 10

print(data_copy)
print(multi)

# copy = duplikat data 1D namun ketika data copy diubah, data yang dicopy tidak ikut berubah.
# deepcopy = duplikat data 2D namun ketika data copy diubah, data yang dicopy tidak ikut berubah.