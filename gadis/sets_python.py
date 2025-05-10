data_list = [1,2,3,4,5] # list
data_tuple = (1,2,3,4,5) # tuple 
data_set = {1,2,3,4,5} # set

data_list[0] = 10
# data_tuple[0] = 10 | error tidak dapat diubah
# data_set[0] = 10 | error tidak dapat diubah
 
print(data_list[0])
print(data_tuple[0])
# print(data_set[0]) | error tidak bisa diakses index 

# add (menambah data)

data_set = {1,2,3,4,5}

data_set.add(6) 
print(data_set)

# update (menggabungkan data)

data_set = {1,2,3,4,5}
data_set2 = {6,7,8,9}
data_set.update(data_set2)
print(data_set)

# union (duplikat data yang digabungkan)

data_set = {1,2,3,4,5}
data_set2 = {6,7,8,9}
data_baru = data_set.union(data_set2)
print(data_baru)

# intersection (menampilkan nilai yang sama)

data_set = {1,2,3,4,5}
data_set2 = {4,5,6,7,8,9}
inter = data_set.intersection(data_set2)
print(inter)

# difference (menampilkan nilai yang tidak sama)

data_set = {1,2,3,4,5}
data_set2 = {4,5,6,7,8,9}
diff = data_set.difference(data_set2)
print(diff)

# clear (menghapus semua data)

data_set = {1,2,3,4,5}
data_set.clear()
print(data_set)

# remove (menghapus data sesuai dengan valuenya)

data_set = {"a", "b", "c"}
data_set.remove("b")
print(data_set)

# pop (menghapus data pertama namun data hapus bisa disimpan)

data_set = {"a", "b", "c"}
data = data_set.pop() 
print(data_set)
print(data)

# copy (duplikat data)

data_set = {"a", "b", "c"}
data = data_set.copy() 
print(data)


