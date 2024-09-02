x = "hello"

print(isinstance(x, int))  
print(isinstance(x, str))   

data = [10, "Hello", 3.14]

for item in data:
    if isinstance(item, (int, float)):
        print(f"{item} adalah angka")
    else:
        print(f"{item} bukan angka")