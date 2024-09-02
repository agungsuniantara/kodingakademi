import turtle

# Inisialisasi objek Turtle
turtle.Turtle()

def move(size, angle):
    turtle.forward(size)
    turtle.left(angle)

for x in range(9):
	move(80, 40)

# Menutup jendela Turtle saat selesai
turtle.done()
