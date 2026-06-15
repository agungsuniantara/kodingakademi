# dictionary function (copy, values, keys, items)

# copy
data = {
    "name" : "diva",
    "age" : 14,
    "address" : "denpasar"
}
data2 = data.copy()
data2["name"] = "william"

print(data)
print(data2)

# values
result_values = data.values()
print(result_values)

# keys
result_keys = data.keys()
print(result_keys)

# items
result_items = data.items()
print(result_items)

# dict_items([('name', 'diva'), ('age', 14), ('address', 'denpasar')])
for key, value in data.items(): #  ('age', 14)
    print(key)
    print(value)
    
score = {
    "Budi" : 85,
    "Siti" : 93
}

# 1. Update score ( Andrew : 90 )
# 2. show score siti has
# 3. use looping to show all of the name and score

