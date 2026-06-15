# function parameter (args & kwargs)
# args = parameter yang bisa menyimpan lebih dari satu nilai.
# kwargs = parameter yang bisa menyimpan nilai dictionary.

def test(*a): # * = args
    print(a)
    for i in a:
        print(i)

def test2(**a): # ** = kwargs
    print(a)
    for key, value in a.items():
        print(key)
        print(value)

def calculate(*a):
    total = sum(a)
    n = len(a)
    return total, n

test(10,20,30,40)
test2(name = "agung", alamat = "denpasar")

total, jumlah = calculate(10,20,30,40)
result = (lambda a,b : a / b)(total, jumlah)
print(result)
    