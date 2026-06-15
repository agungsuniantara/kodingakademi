# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing the first item (Index 0)
print("First fruit:", fruits[0])

# Adding an item
fruits.append("orange")

# Removing an item
fruits.remove("banana")

print("Updated list:", fruits)

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "course": "Computer Science"
}

# Accessing a value
print("Student Name:", student["name"])

# Modifying a value
student["age"] = 21

# Adding a new key-value pair
student["grade"] = "A"

print("Updated Student Data:", student)

# Defining a function
def greet():
    print("Hello! Welcome to Python.")

# Calling the function
greet()

def greet_person(name):
    print("Hello, " + name)

greet_person("Alice")
greet_person("Bob")

def multiply_numbers(x, y):
    return x * y

result = multiply_numbers(5, 3)
print("The result is:", result)