data = {
    1 : "Ayam",
    2 : "Sapi",
    3 : "Kambing", 
    4 : "Mawar",
    5 : "Lily"
}

data_copy = data.copy()

for i in data.copy():
    if i == 4 or i == 5:
        data.pop(i)

for i in data_copy:
    if i % 2 != 0:
        data_copy[i] = "hewan"

print(data_copy)