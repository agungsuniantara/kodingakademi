import turtle

kura = turtle.Turtle()
screen = turtle.Screen()

kura.speed(0)
move_distance = 20
screen.bgcolor("#ffeb86")

kura.penup()
kura.goto(100, 300)
kura.pendown()

kura.color("blue")

kura.begin_fill()
kura.goto(400, 300)
kura.goto(400, -300)
kura.goto(100, -300)
kura.goto(100, 300)
kura.end_fill()

kura.penup()
kura.goto(-200, 0)
kura.shape("turtle")
kura.shapesize(2)
kura.color("green")

menang = False


def move_up():
    global menang
    if not menang:
        kura.setheading(90)
        kura.forward(move_distance)
        check_goal()


def move_down():
    global menang
    if not menang:
        kura.setheading(270)
        kura.forward(move_distance)
        check_goal()


def move_left():
    global menang
    if not menang:
        kura.setheading(180)
        kura.forward(move_distance)
        check_goal()


def move_right():
    global menang
    if not menang:
        kura.setheading(0)
        kura.forward(move_distance)
        check_goal()


def check_goal():
    global menang
    if kura.xcor() > 100:
        menang = True
        kura.hideturtle()
        kura.color("white")
        kura.write("you win !")


screen.onkey(move_up, "Up")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_down, "Down")
screen.listen()

screen.mainloop()
