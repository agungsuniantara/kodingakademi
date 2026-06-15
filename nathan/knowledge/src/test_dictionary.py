data = {
    "1" : "ayam",
    "2" : "tikus"
}

backup = data.copy()

for key, value in backup.items():
    if int(key) % 2 != 0:
        data[key] = "hewan"

print(data)