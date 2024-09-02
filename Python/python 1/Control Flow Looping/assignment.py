# assignment 1
print("assignment 1")
no = 0
for n in range(10):
    no += 1
    print(no)

print()

# assignment 2
print("assignment 2")
score = 0
end_score = 10
for n in range(end_score):
    score += 1
    print(score)
    if score == end_score:
        print("berhenti")

print()

# assignment 3
print("assignment 3")
kolom = int(input("masukkan nilai : "))
baris = 5

for i in range(kolom):
    for j in range(baris):
        print("*", end=" ")
    print()

print()

# assignment 4
print("assignment 4")
kolom = 5
baris = 1

for i in range(kolom):
    for j in range(baris): 
        print("*", end=" ") 
    baris += 1 
    print() 

print()

print("note penggunaan end dan print()")
print("Welcome to", end = ' ')
print("Koding akademi", end= ' ')
print()
print("Welcome to")
print("Koding akademi")