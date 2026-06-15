# variabel = container that can store value

name = "agung"
print("name : ", name)

# data type ( string (keep with word), boolean (true/false), int (storing number), null (empty), float (decimal number) )

print("name : ", name)
print("data type : ", type(name))

is_true = True
print("value : ", is_true)
print("data type : ", type(is_true))

# change data type 

number = 10.0
change = int(number)
print(change)

# input / output

# input_name = input("your name : ")
# print(input_name)

# operator (arithmatic)

add = 10 + 10
minus = 100 - 10
times = 100 * 10
divide = 100 / 10
remainder = 5 % 2 == 0
power = 2 ** 2

# operator (comparison)

test1 = add == minus 
print(test1)

test2 = add > minus 
print(test2)

# operator (logic)

# and = if one condition is false the output will be false
# or = if one condition is true the output will be true
# not = if condition is true it will be false

number1 = 10
number2 = 20
number3 = 30

logic1 = (number1 > number2) and (number2 < number3) # false and true = false
print(logic1)

logic2 = (number1 > number2) or (number2 < number3) # false or true = true
print(logic2)

logic3 = not(number1 > number2) and (number2 < number3) # true and true = true
print(logic3)

# conditional statement

username = input("username : ")
password = input("password : ")

if (username == "admin") and (password == "admin123"):
    print("hello admin")
elif (username == "user") and (password == "user123"):
    print("hello user")
elif (username == "member") and (password == "member123"):
    print("hello member")
else:
    print("account not found")

if False:
    print("hello admin")
elif True:
    print("hello user")
else:
    print("account not found")

# assignment

# make decision grade (A, B, C, D):
# condition1 : 0 - 50 (D)
# condition2 : 51 - 70 (C)
# condition3 : 71 - 90 (B)
# condition4 : 91 - 100 (A)
# condition5 : if all wrong it will have an output ("grade is not correct")

# assignment 2

# make a decision between odd and even

# looping (for and while)
# for loop = already know how many times it will be looping
# while loop = looping when condition is true, it will stop if condition is false.

# for loops

for i in range(3):
    print(i)

print("\n")
for i in range(1, 4): # (start, stop)
    print(i)

print("\n")
for i in range(1, 6, 2): # (start, stop, step)
    print(i)

# while loops

stop = 5
i = 0

while i <= 5:
    print(i)
    i += 1 # i = i + 1
    
while True:
    answer = input("you want to ask again ? ")
    if answer == "no":
        break
    
# loops inside loops

for i in range(3): # i = 0
    print("outside loops : ", i)
    for z in range(3):
        print("inside loops : ", z)
        
# assignment 
# 1. do 10 looping and make output, example : 1,2.. 10
# 2. make variable score = 0, end_score = 10, using while loops, everytime do looping score + 1
# if score == end_score, while loops stop.
# 3. make a 

for i in range(3): # i = 0
    for z in range(3): # z = 0
        if z <= i:
            print("*", end=" ")
    print("")


        













