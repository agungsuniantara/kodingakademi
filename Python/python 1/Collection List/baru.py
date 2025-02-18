data = {"1" : "anjing", "2" : "mawar"}
data_copy = data.copy()

for key in data.keys():
    print(key)
    
for key, value in data_copy.items(): # looping = 5
    data.pop("1")