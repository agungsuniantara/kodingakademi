data_list = [1,2,3,4,5] # list
data_tuple = (1,2,3,4,5) # tuple 

data_list[0] = 10  # list[] data dapat diubah
# data_tuple[0] = 20 | error ! tuple() data tidak dapat diubah

print(data_list[0]) # list[] bisa akses index
print(data_tuple[0]) # tuple bisa akses index

# count 

data_tuple = (2,2,2,5,5,5)
count = data_tuple.count(2)

print(count)

# index

data_tuple = (2,2,2,5,5,5)
index = data_tuple.index(5)

print(index)
