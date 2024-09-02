import turtle
import random

turtle.Turtle()

turtle.hideturtle()

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
skor = turtle.Turtle()

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

# data structure

x = {}

# loop untuk pergerakan
while True:
    t1.forward(speed_turtle1)
    t2.forward(speed_turtle2)
    t3.forward(speed_turtle3)
    t4.forward(speed_turtle4)
    t5.forward(speed_turtle5)

    if t1.xcor() >= 230:
        t1.hideturtle()
        x.update({"t1" : t1.xcor(), "t2" : t2.xcor(), "t3" : t3.xcor(), "t4" : t4.xcor(), "t5" : t5.xcor()})
        break

    elif t2.xcor() >= 230:
        t2.hideturtle()
        x.update({"t1" : t1.xcor(), "t2" : t2.xcor(), "t3" : t3.xcor(), "t4" : t4.xcor(), "t5" : t5.xcor()})
        break

    elif t3.xcor() >= 230:
        t3.hideturtle()
        x.update({"t1" : t1.xcor(), "t2" : t2.xcor(), "t3" : t3.xcor(), "t4" : t4.xcor(), "t5" : t5.xcor()})
        break

    elif t4.xcor() >= 230:
        t4.hideturtle()
        x.update({"t1" : t1.xcor(), "t2" : t2.xcor(), "t3" : t3.xcor(), "t4" : t4.xcor(), "t5" : t5.xcor()})
        break

    elif t5.xcor() >= 230:
        t5.hideturtle()
        x.update({"t1" : t1.xcor(), "t2" : t2.xcor(), "t3" : t3.xcor(), "t4" : t4.xcor(), "t5" : t5.xcor()})
        break

# show ranking

sorted_data = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))

posisi_x = -280
rank = 1

for key, value in sorted_data.items():
    skor.hideturtle()
    skor.penup()
    skor.goto(posisi_x, 250)
    skor.pendown()
    skor.color("white")
    skor.write(f"Rank {rank} : {key}", font=(20))
    posisi_x += 115
    rank += 1

turtle.done()
