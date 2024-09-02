import turtle
import random

turtle.speed(0)

turtle.Turtle()
turtle.Screen()

turtle.bgcolor("black")
turtle.hideturtle()

def draw_star(xpos, ypos):
    turtle.penup()
    size = random.randrange(5, 20)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.dot(size, "white")

width = turtle.window_width()
height = turtle.window_height()

for x in range(100):
    xpos = random.randrange(round(-width / 2), round(width / 2))
    ypos = random.randrange(round(-height / 2), round(height / 2))
    draw_star(xpos, ypos)

turtle.done()
