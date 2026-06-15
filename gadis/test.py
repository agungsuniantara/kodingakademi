# Soal 1 

# buat program untuk membedakan angka genap & ganjil. 
# buat program untuk menambahkan 5 bilangan inputan.

# 3 collections : list, tuples, dictionaries.

# list = variabel that store different value, you can change & delete.
# tuples = same like list but it cant delete / change.
# dictionary = variabel that can store key : value.

data = (10, 20, 30, 40)
print(data[0])

data2 = (
    (10, 20, 30),
    (40, 50, 60)
)
print(data2[0][0])

nama, alamat, age = "diva", "denpasar", "20 tahun"
print(nama)
print(alamat)
print(age)
print(nama + alamat + age)

data = (10, 20, 30, 40, 50)

for i in data: # i = 20
    print(i)
    
# dictionary 

# create dictionary

data = {"name" : ["diva", "william"], "address" : "denpasar"}
print(data["address"])
print(data["name"][0])

# change dictionary

data["address"] = "tabanan"
print(data["address"])
data["name"][0] = "agung"

# looping

for i in data:
    print(data[i])

# assignment

data = {
    "name" : input("insert your name : ")
}


