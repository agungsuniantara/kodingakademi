import turtle

kura = turtle.Turtle()
screen = turtle.Screen()
finish_line = turtle.Turtle()

screen.bgcolor("black")

kura.shape("turtle")
kura.color("green")
kura.shapesize(2)
kura.penup()

finish_line.penup()
finish_line.goto(200, 350)
finish_line.pendown()

finish_line.fillcolor("white")
finish_line.begin_fill()
finish_line.forward(150)
finish_line.right(90)
finish_line.forward(690)
finish_line.right(90)
finish_line.forward(150)
finish_line.end_fill()
finish_line.hideturtle()

menang = False

def move_up():
    kura.setheading(90)
    kura.forward(20)
    check_goal()

def move_left():
    kura.setheading(180)
    kura.forward(20)
    check_goal()
    
def move_right():
    kura.setheading(0)
    kura.forward(20)
    check_goal()

def move_down():
    kura.setheading(270)
    kura.forward(20)
    check_goal()

def check_goal():
    global menang
    if kura.xcor() > 200:
        menang = True
        kura.hideturtle()
        kura.color("black")
        kura.write("you win !")
        screen.onkey(None, "Up")
        screen.onkey(None, "Left")
        screen.onkey(None, "Right")
        screen.onkey(None, "Down")

screen.onkey(move_up, "Up")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_down, "Down")
screen.listen()

screen.mainloop()