# collections (list) : variable that can contain more than 1 value

data = ["cow", "fish", "apple"]
print(data)

# access list 

print(data[0])
print(data[1])
print(data[2])

for i in data:
    print(i)

print(len(data))
for i in range(len(data)):
    print(data[i])
    
# change list

data[0] = "shark"
print(data[0])

# add value to list

data = ["cow", "fish", "apple"]
data.append("bird") # append = adding value at the end
print(data)

data = ["cow", "fish", "apple"]
data.insert(1, "bird") # insert = adding value at index
print(data)

# delete value

data = ["cow", "fish", "apple"]
del data[1] # del = delete list with index
print(data)

data = ["cow", "fish", "apple"]
data.remove("apple") # remove = delete list with value
print(data)

# list operation

data1 = ["cow", "fish", "apple"]
data2 = ["cow", "fish", "apple"]
data3 = data1 + data2
print(data3)

# list mutidimension 

data = [["Coffe", "Milk"], ["Juice", "Pop ice"], ["Ice cream", "Ice tea"]]

print(data)
print(data[0])
print(data[0][0])

number = 1
for i in data:
    for z in i:
        print(f"{number}. {z}")
        number += 1

# assignment : 
        
data = ["1", "2"]
order = []

value = input("check : ")

if value not in data:
    print("you put it wrong")
else:
    print("you put it right")
    
my_order = input("please type what item ? ")
order.append(my_order)
    
print("your order : ")
for i in data:
    print(i)
price =  len(data) * 20000
actual = str(price)
print(f"order price : Rp {actual[0:2]}.{actual[2:]}")

# tuples = variable that can store more than 1 value, but it cannot be change.

data_tuples = ("koding", "python", "php")
print(data_tuples[0])

# data_tuples[0] = "hello" # error because tuples can not do item assignment
# print(data_tuples)

# data_tuples.append("hello") # tuples doesnt have append function

# unpacking (list / tuples)

one, two, three = data_tuples
print(one)

# dictionary = variable that can store key and value

biodata = {
    "name" : "agung",
    "age" : "20 years old",
    "hoby" : ["coding", "play"]
}

print(biodata)

biodata2 = dict(name="agung", 
                age="20", 
                hoby=["coding", "play"])

print(biodata2)

# access dictionary

print(biodata["name"])

for i in biodata:
    print("key : ", i)
    print("value : ", biodata[i])

# change dictionary 

biodata["name"] = "bryan"
print(biodata)

# delete dictionary del

biodata = {
    "name" : "agung",
    "age" : "20 years old",
    "hoby" : ["coding", "play"]
}

del biodata["age"] # del = delete dictionary with key
print(biodata)

# delete dictionary pop

biodata = {
    "name" : "agung",
    "age" : "20 years old",
    "hoby" : ["coding", "play"]
}

value_del = biodata.pop("name")
print(value_del)
print(biodata)

# adding dictionary

biodata = {
    "name" : "agung",
    "age" : "20 years old",
    "hoby" : ["coding", "play"]
}

biodata.update({"address" : "canggu", "food" : "free food"})
print(biodata)

# check data dictionary 

print(len(biodata))

# assignment

data = {
    "a" : input("input your name : ")
}

print("name : ", data["a"])

# function dictionary

biodata = {
    "name" : "agung",
    "age" : "20 years old",
    "hoby" : ["coding", "play"]
}

data_key = biodata.keys() # keys = function to get all of key dictionary
print(data_key)

data_value = biodata.values() # values = function to get all of value dictionary
print(data_value)

data_item = biodata.items() # items = function to make key and value seperate
print(data_item)

for key, value in biodata.items():
    if value % 2 == 0:
        print(key)
    




