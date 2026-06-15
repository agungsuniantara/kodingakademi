# variable = place for storing data

fruit = "apple"
print(fruit)

# challange 1 : 
# 1. buat 3 variabel (nama, umur, alamat)
# 2. tampilkan 3 variabel tersebut

# data types (string, integer, float, boolean)
# string = text
# integer = whole number
# float = decimal number
# boolean = true / false

fruit = "banana"
number = 25
price = 19.99
is_available = False

print(type(fruit))
print(type(number))
print(type(price))
print(type(is_available))

price = int(price)
print(price)
print(type(price))

# challange 2 : 
# 1. buat 3 variabel dengan tipe data yang berbeda
# 2. tampilkan tipe data dari masing-masing variabel tersebut
# 3. ubah 3 variabel ke tipe data float / int / str, lalu tampilkan nilai dan tipe data barunya

# input & output 

fruit = input("insert fruit name: ") # input
print("the fruit you entered is " + fruit) # output

# challange 3 :
# 1. buat program yang meminta user memasukkan nama, umur, dan alamat
# 2. tampilkan data yang sudah dimasukkan user dengan format :
#    "nama saya ___, umur saya ___ tahun, dan saya tinggal di ___"

name = input("masukkan nama: ")
age = input("masukkan umur: ")
address = input("masukkan alamat: ")

print("nama saya " + name + ", umur saya " + age + " tahun, dan saya tinggal di " + address)

# operator (arithmetic, assignment, comparison, logical)
# arithmetic (+, -, *, /, %, //, **)
# assignment (=, +=, -=, *=, /=)
# comparison (==, !=, >, <, >=, <=)
# logical (and, or, not)

# arithmetic
x = 15
y = 4
print(x + y) # addition
print(x - y) # subtraction
print(x * y) # multiplication
print(x / y) # division
print(x % y) # modulus
print(x // y) # floor division
print(x ** y) # exponentiation

# assignment
z = 7
z += 3 # z = z + 3
print(z)
z *= 2 # z = z * 2
print(z)
z -= 5 # z = z - 5
print(z)
z /= 2 # z = z / 2
print(z)
z %= 4 # z = z % 4
print(z)

# comparison
m = 20
n = 10
print(m == n) # equal
print(m != n) # not equal
print(m > n)  # greater than
print(m < n)  # less than
print(m >= n) # greater than or equal to
print(m <= n) # less than or equal to

# logical
# and = both conditions must be true
# or = at least one condition must be true
# not = reverses the boolean value

m = 20
n = 10
print(m == n and m != n) # false and true = false
print(m == n or m != n)  # false or true = true 
print(not(m == n))       # not false = true

# challange 4 :
# 1. buat 2 variabel dengan nilai integer
# 2. lakukan operasi aritmatika pada kedua variabel tersebut (semua operasi)
# 3. lakukan operasi perbandingan pada kedua variabel tersebut (semua operasi)
# 4. lakukan operasi logika pada kedua variabel tersebut (minimal 3 operasi)

# conditional statement (if, elif, else)

age = int(input("masukkan umur Anda: "))

if age < 18:
    print("you are a minor.")
elif age >= 18 and age < 65:
    print("you are an adult.")
if age >= 65:
    print("you are a senior citizen.")
else:
    print("you are a senior citizen.")

# challange 5 : 
# 1. buat program yang meminta user memasukkan angka
# 2. jika angka tersebut lebih dari 0, tampilkan "angka positif"
# 3. jika angka tersebut kurang dari 0, tampilkan "angka negatif"
# 4. jika angka tersebut sama dengan 0, tampilkan "angka nol"



