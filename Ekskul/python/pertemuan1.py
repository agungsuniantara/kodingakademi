# Declaring variables
name = "John"
age = 30
height = 175.5

# Displaying variable values
print("Name:", name)
print("Age:", age)
print("Height:", height)

# Basic data types

number = 10               # int
pi = 3.14                 # float
text = "Learning Python"  # str
is_true = True            # bool

print(type(number))       # Output: <class 'int'>
print(type(pi))           # Output: <class 'float'>
print(type(text))         # Output: <class 'str'>
print(type(is_true))       # Output: <class 'int'>

# Taking input from the user

name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")

print("personal data : ")
print("name = ", name)
print("age = ", age)
print("address = ", address)

# Converting float to int
num_float = 7.8
num_int = int(num_float) 
print("Integer value:", num_int)
print(type(num_int))   

# Converting int to float
num1 = 15
num_float = float(num1)
print("Float value:", num_float)  
print(type(num_float))  

# Converting int to string
num2 = 50
num_str = str(num2)
print("String value:", num2)  
print(type(num_str))  