import turtle

# Inisialisasi objek Turtle
turtle.Turtle()

# Maju sejauh 100 satuan
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)


def move(size, angle):
    turtle.forward(size)
    turtle.right(angle)

move(100, 90)
move(100, 90)
move(100, 90)
move(100, 90)

for x in range(4):
    move(100, 90)

# Menutup jendela Turtle saat selesai
turtle.done()
