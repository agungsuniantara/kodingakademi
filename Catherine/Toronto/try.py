a = 15
b = 4

print("Addition:", a + b)          # Output: 19
print("Subtraction:", a - b)       # Output: 11
print("Multiplication:", a * b)    # Output: 60
print("Division:", a / b)          # Output: 3.75
print("Floor Division:", a // b)   # Output: 3
print("Modulus:", a % b)           # Output: 3
print("Exponentiation:", a ** b)   # Output: 50625

is_sunny = True
is_raining = False

print(type(is_sunny))  # Output: <class 'bool'>
print(is_sunny and is_raining)  # Output: False

a = 10
b = 20

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: False
print(a < b)   # Output: True
print(a >= b)  # Output: False
print(a <= b)  # Output: True

# Multiplication vs. Addition
print(3 + 5 * 2)  # Output: 13 (multiplication first)

# Exponentiation vs. Division
print(2 ** 3 / 2)  # Output: 4.0 (exponentiation first)

print(0.1 + 0.2)  # Output: 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # Output: False


x = 5       # Integer
y = 2.5     # Float
result = x + y  # Python automatically converts 'x' to float
print(result)   # Output: 7.5
print(type(result))  # Output: <class 'float'>