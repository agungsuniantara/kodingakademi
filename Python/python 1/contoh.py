import turtle

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)

heart = turtle.Turtle()
heart.speed(2)

heart.color('red')
heart.begin_fill()

heart.left(140)
heart.forward(180)
heart.circle(-90, 200)

heart.left(120)
heart.circle(-90, 200)
heart.forward(180)

heart.end_fill()
heart.hideturtle()

# Menulis teks "Happy Valentine's Day"
heart.penup()
heart.goto(0, -70)
heart.color('red')
heart.write("Happy Valentine's Day", align="center", font=("Arial", 24, "bold"))
heart.hideturtle()

heart.penup()
heart.goto(0, -110)
heart.color('orange')
heart.write("By Koding Akademi", align="center", font=("Arial", 18, "bold"))

turtle.done()
