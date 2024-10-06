data = {
    1 : "Ayam",
    2 : "Sapi",
    3 : "Mawar"
}

for key, value in data.items():
    if key % 2 != 0:
        data[key] = "Hewan"

print(data)