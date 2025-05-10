import random 
import turtle

# Inisialisasi objek Turtle
turtle.Turtle()

forward = 0
right = 0

while True:
    angka1 = random.randint(0, 100)
    angka2 = random.randint(0, 100)
    if angka1 == 100 and angka2 == 90:
        forward = angka1
        right = angka2
        break

for i in range(4):
    turtle.forward(forward)
    turtle.right(right)

# Menutup jendela Turtle saat selesai
turtle.done()