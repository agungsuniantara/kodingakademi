data = {1 : "mawar", 2 : "sapi", 3 : "anggrek"}

for key, value in data.copy().items():
    if value == "mawar" or value == "anggrek":
        del data[key]

print(data)