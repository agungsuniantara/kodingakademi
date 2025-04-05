data = []
for i in range(10):
    a = int(input("masukan nilai : "))
    data.append(a)

def test(*a): # ([1, 2, 3, 4, 5, 6, 7, 8, 9, 1])
    z = 0
    print(a[0])
    for i in a[0]: # [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        z += i
    return z

hasil = test(data)

result = (lambda a: a / len(data))(hasil)