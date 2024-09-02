import turtle

turtle.Turtle()

turtle.bgcolor("black")
turtle.hideturtle()


def draw_star(xpos, ypos):
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.dot(20, "white")


draw_star(0, 0)
draw_star(40, 15)
draw_star(-70, 55)
draw_star(60, -65)
draw_star(-83, -90)

turtle.done()
