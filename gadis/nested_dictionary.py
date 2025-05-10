nama = {
    "nama1" : "agung",
    "nama2" : "wahyu"
}

data = {
    "data1" : [1,2,3,4,5],
    "data2" : nama,
    "data3" : {
        "barang1" : "sabun",
        "barang2" : "sikat gigi"
    }
}

print(data["data1"])
print(data["data1"][1])

print(data["data2"])
print(data["data2"]["nama1"])

print(data["data3"])
print(data["data3"]["barang1"])

data_list = [1,1,1,1]
data_tuple = (1,1,1,1)
data_set = {1,1,1,1}

print(data_list)
print(data_tuple)
print(data_set)

