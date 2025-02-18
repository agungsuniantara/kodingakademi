import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.pencolor("blue")
t1.fillcolor("green")
t1.begin_fill()
t1.forward(100)
t1.right(90)
t1.forward(100)
t1.end_fill()

t2.pencolor("blue")
t2.fillcolor("green")
t2.begin_fill()
t2.forward(100)
t2.right(90)
t2.forward(100)
t2.end_fill()

turtle.done()