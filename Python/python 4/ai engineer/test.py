# dictionary function

# copy()

data = {"name": "Alice", "age": 30}
data_test = data
print(data_test)  # Output: {'name': 'Alice', 'age': 30}

data2 = {"name": "Alice", "age": 30}
data_copy = data2.copy()
print(data_copy)  # Output: {'name': 'Alice', 'age': 30}

data_test["name"] = "Bob"
print(data_test)  # Output: {'name': 'Bob', 'age': 30}
print(data)  # Output: {'name': 'Bob', 'age': 30}

data_copy["name"] = "Charlie"
print(data_copy)  # Output: {'name': 'Charlie', 'age': 30}
print(data2)  # Output: {'name': 'Alice', 'age': 30}

# fromkeys()

keys = ["name", "age", "city"]
animals = dict.fromkeys(keys, "unknown")
print(animals)  # Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

# get()

person = {"name": "Alice", "age": 30}
print(person.get("name"))  # Output: Alice
print(person.get("city", "Not Found"))  # Output: Not Found

# items()

person = {"name": "Alice", "age": 30}
items = person.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 30)])

for key, value in items:
    print(f"{key}: {value}")

# keys()

person = {"name": "Alice", "age": 30}
keys = person.keys()
print(keys)  # Output: dict_keys(['name', 'age'])

for i in keys:
    print(i)

# values()

person = {"name": "Alice", "age": 30}
values = person.values()
print(values)  # Output: dict_values(['Alice', 30])

for v in values:
    print(v)

# assignment

data = {
    "1" : "anggur",
    "2" : "apel",
    "3" : "jeruk"
}

for i in data.keys():
    if int(i) % 2 != 0:
        data[i] = "hewan"
        
kata = "aku"
data = []

for i in kata:
    if i == "a":
        data.append("i")
    else:
        data.append(i)

print(data)  # Output: ['i', 'k', 'u']
kata_sambung = "".join(data)
print(kata_sambung)  # Output: "iku"
