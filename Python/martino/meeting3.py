# function = blue print that can be reused 
# 3 type of function : 
# - function void (function that the result is not returned)
# - function parameter (function that has input)
# - function return (function that returns a value)
# - function inside function (function that has function inside)
# - function recursion = function that calls itself

def greet(): # function void
    print("hello world")
    
def greet_name(name): # function parameter
    print("hello ", name)
    
def add(a, b): # function return
    return a + b

def rectangle_2d(length, width):
    result = length * width
    return result

def rectangle_3d(length, width, height):
    result = rectangle_2d(length, width) * height
    return result

greet() # call function void
greet_name("John") # call function parameter
print(add(10, 5))
result = add(5, 3) # call function return
print("result : ", result)

print("2D rectangle area : ", rectangle_2d(10, 5))
print("3D rectangle area : ", rectangle_3d(20, 6, 10))

# function python (global) = variable that can be accessed anywhere

number = 0 

def increment():
    global number
    number += 1
    print(number)

increment()

# function recursion 

def factorial(n): # n = 4
    if n == 0:
        return 1
    else:
        print("n :", n)
        return n * factorial(n - 1) # 5 * 4 * 3 * 2 * 1 

print("factorial 5 : ", factorial(5))


# example 

def add(a, b):
    return a + b

while True:
    print("choose menu :")
    print("1. add")
    
    choose = input("choose menu : ")
    if choose == "1":
        num1 = int(input("input first number : "))
        num2 = int(input("input second number : "))
        result = add(num1, num2)
        print("result : ", result)
    
    condition = input("do you want to continue ? (y/n) 😀")
    if condition == "n":
        break
    
# function python args = parameter that can accept many arguments

def sample_function(*a):
    print(a)
    for i in a:
        print(i)
    
sample_function(1, 2, 3, 4, 5)

# function python kwargs = parameter that can accept many key and value

def sample_function2(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")

sample_function2(name="agung", age=20, hoby="coding")

# function python lambda = anonymous function / function without name

double = (lambda x: x * 2)(5)
print("double of 5 is", double)

# OOP (Object Oriented Programming) = programming that based on object and class

# class 1
class Car:
    name = "civic"
    color = "red"
    year = 2020
    
    def drive(self):
        print("the car is driving")
    
    def stop(self):
        print("the car is stopping")

my_car = Car()
print("car name :", my_car.name)
my_car.drive()

# class 2 (constructor) = special function that is called when the class is instantiated
class Car:
    def __init__(self, a, b, c):
        self.name = a
        self.color = b
        self.year = c

    def drive(self):
        print(f"the {self.name} is driving")

    def stop(self):
        print(f"the {self.name} is stopping")

my_car1 = Car("civic", "red", 2020)
print("car name :", my_car1.name)
my_car1.drive()

my_car2 = Car("fortuner", "black", 2020)
print("car name :", my_car2.name)
my_car2.drive()

# class 3 (inheritance) = class that can inherit another class

class Vehicle:
    def __init__(self, a, b):
        self.color = a
        self.year = b

    def drive(self):
        print("the car is driving")

    def stop(self):
        print("the car is stopping")
        
class Car(Vehicle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.name = c
    
    def name(self):
        print("car name :", self.name)
        
car1 = Car("red", 2020, "civic")
print("car color :", car1.color)
car1.drive()

# file operation = read, write, append
# r = read, w = write, a = append

# file txt
# operation read
file = open("data.txt", "r") 
content = file.read() # read = read all content
print(content)
file.close()

with open("data.txt", "r") as f: # with = automatically close file
    data = f.read()
    print(data)

# operation write
with open("data2.txt", "w") as f:
    f.write("Hello world\n")
    f.write("This is a test file\n")
    
# operation append
with open("data2.txt", "a") as f:
    f.write("New line\n")
    
# file csv 

import csv

with open("data.csv", "w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(["Kolom1", "Kolom2"])
    writer.writerow(["A", "B"])
    
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        
# file json

import json

data = {
    "nama": "Andi",
    "umur": 20
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data.json", "r") as f:
    data = json.load(f)
    for key, value in data.items():
        print(f"{key} : {value}")










    