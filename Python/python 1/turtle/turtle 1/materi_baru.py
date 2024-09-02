import turtle

# Inisialisasi objek Turtle
turtle.Turtle()

diameter = 40
pop_diameter = 100


def draw_balloon():
    turtle.color("red")
    turtle.dot(diameter)


def inflate_balloon():
    global diameter
    diameter = diameter + 10
    draw_balloon()

    if diameter >= pop_diameter:
        turtle.clear()
        diameter = 40
        turtle.write("POP!")


draw_balloon()
turtle.onkey(inflate_balloon, "Up")
turtle.listen()

# Menutup jendela Turtle saat selesai
turtle.done()
