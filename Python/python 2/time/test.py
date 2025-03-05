import turtle 
import random 

turtle.Turtle()

angle = 0

while True:
    angka = random.randint(0, 100)
    if angka == 90:
        angle = angka
        break

for i in range(4):
    turtle.forward(100)
    turtle.forward(angle)
