angka1 = int(input("masukan angka1 : "))
angka2 = int(input("masukan angka2 : "))

def addition():
    global angka1
    global angka2 
    result = angka1 + angka2 
    print(result)

while True:
    print("choose menu : ")
    print("1. addition")
    print("2. multiply")
    print("3. division")
    print("4. subtraction")
    
    menu = int(input("menu : "))
    if menu == 1:
        addition()
    
    