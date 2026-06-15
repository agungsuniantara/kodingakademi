# Declaring variables
student_name = "Alice"
age = 20
height = 165.5

# Displaying values
print("Name:", student_name)
print("Age:", age)
print("Height:", height)

score = 100           # int
average = 95.5        # float
subject = "Math"      # str
passed = True         # bool

print(type(score))
print(type(average))
print(type(subject))
print(type(passed))

# Taking input from user
name = input("Enter your name: ")
print("Hello,", name)

str_num = "25"
float_num = 5.5

# Convert string to int
converted_int = int(str_num)

# Convert float to int
rounded_int = int(float_num)

print("Converted int:", converted_int)
print("Rounded int:", rounded_int)

x = 10
y = 3
print("Modulus (remainder):", x % y)
print("Exponentiation:", x ** y)

a = 5
b = 10
print("Is a equal to b?", a == b)
print("Is a less than b?", a < b)

is_sunny = True
is_warm = False
print("Sunny AND Warm:", is_sunny and is_warm)
print("Sunny OR Warm:", is_sunny or is_warm)

count = 5
count += 2  # Same as count = count + 2
print("New count:", count)

for i in range(3):
    print("Iteration:", i)
    
n = 1
while n <= 3:
    print("Count:", n)
    n += 1
    
temperature = 25

if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("It's a pleasant day.")
else:
    print("It's cold.")
    


