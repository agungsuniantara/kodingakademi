import turtle 

t = turtle.Turtle()

t.fillcolor("yellow")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.goto(-100, 100)
t.pendown()
t.forward(100)

turtle.done()