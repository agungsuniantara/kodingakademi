from turtle import Turtle, Screen
from PIL import Image

# Create a turtle screen
screen = Screen()

# Register the image as a turtle shape
screen.register_shape("mini project\dinosaur2.gif")

# Create a turtle with the custom image shape
my_turtle = Turtle("mini project\dinosaur2.gif")

# Move the turtle
my_turtle.forward(100)

# Close the turtle graphics window when clicked
screen.exitonclick()
