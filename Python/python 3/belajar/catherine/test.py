dict = {
    "a" : 1
}
a = input("masukan key : ")
b = input("masukan value : ")

if a.isdigit():
    a = int(a)
    
if b.isdigit():
    b = int(b)
    
dict.update({a : b})
print(dict)

a = input("masukan angka : ")
list = []
if a.isdigit():
    list.append(int(a))
else:
    list.append(a)

print(list)