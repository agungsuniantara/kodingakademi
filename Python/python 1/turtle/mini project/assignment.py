import turtle
import random

turtle.Turtle()

turtle.bgcolor("green")
turtle.color("black")
turtle.pensize(40)

# line 1
turtle.penup()
turtle.goto(-250, 200)
turtle.pendown()
turtle.goto(250, 200)

# line 2
turtle.penup()
turtle.goto(-250, 100)
turtle.pendown()
turtle.goto(250, 100)

# line 3
turtle.penup()
turtle.goto(-250, 00)
turtle.pendown()
turtle.goto(250, 00)

# line 4
turtle.penup()
turtle.goto(-250, -100)
turtle.pendown()
turtle.goto(250, -100)

# line 5
turtle.penup()
turtle.goto(-250, -200)
turtle.pendown()
turtle.goto(250, -200)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()

# turtle 1
t1.penup()
t1.goto(-250, 200)
t1.shape("turtle")
t1.color("red")

# turtle 2
t2.penup()
t2.goto(-250, 100)
t2.shape("turtle")
t2.color("yellow")

# turtle 3
t3.penup()
t3.goto(-250, 00)
t3.shape("turtle")
t3.color("green")

# turtle 4
t4.penup()
t4.goto(-250, -100)
t4.shape("turtle")
t4.color("blue")

# turtle 5
t5.penup()
t5.goto(-250, -200)
t5.shape("turtle")
t5.color("orange")

# speed
speed_turtle1 = random.randint(1, 5)
speed_turtle2 = random.randint(1, 5)
speed_turtle3 = random.randint(1, 5)
speed_turtle4 = random.randint(1, 5)
speed_turtle5 = random.randint(1, 5)

# loop untuk pergerakan
while True:
    t1.forward(speed_turtle1)
    t2.forward(speed_turtle2)
    t3.forward(speed_turtle3)
    t4.forward(speed_turtle4)
    t5.forward(speed_turtle5)

    if t1.xcor() >= 230:
        t1.hideturtle()
        t1.penup()
        t1.goto(0, 0)
        t1.pendown()
        t1.write("Turtle 1 Wins!", font=(20))
        break

    elif t2.xcor() >= 230:
        t2.hideturtle()
        t2.penup()
        t2.goto(0, 0)
        t2.pendown()
        t2.write("Turtle 2 Wins!", font=(20))
        break

    elif t3.xcor() >= 230:
        t3.hideturtle()
        t3.penup()
        t3.goto(0, 0)
        t3.pendown()
        t3.write("Turtle 3 Wins!",font=(20))
        break

    elif t4.xcor() >= 230:
        t4.hideturtle()
        t4.penup()
        t4.goto(0, 0)
        t4.pendown()
        t4.write("Turtle 4 Wins!", font=(20))
        break

    elif t5.xcor() >= 230:
        t5.hideturtle()
        t5.penup()
        t5.goto(0, 0)
        t5.pendown()
        t5.write("Turtle 5 Wins!", font=(20))
        break

turtle.done()


