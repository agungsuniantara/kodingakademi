import turtle 
import random

t1 = turtle.Turtle()

angka = 0
while True:
    angka = random.randrange(1, 100)
    if angka == 90:
        break

t1.forward(angka)

turtle.done()