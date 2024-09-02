from turtle import Turtle, Screen
from PIL import Image
import random

# Open the image file
image1 = Image.open("mini project\dino3.gif")
image2 = Image.open("mini project\dino4.gif")

# Resize the image
resized_image1 = image1.resize((100, 100))  # Adjust the size as needed
resized_image2 = image2.resize((100, 100))  # Adjust the size as needed

# Save the resized image as a GIF
resized_image1.save("mini project\dino_resized1.gif")
resized_image2.save("mini project\dino_resized2.gif")

# Create a turtle screen
screen = Screen()

# Register the resized image as a turtle shape
screen.register_shape("mini project\dino_resized1.gif")
screen.register_shape("mini project\dino_resized2.gif")

# Create a turtle with the custom image shape
t1 = Turtle("mini project\dino_resized1.gif")
t2 = Turtle("mini project\dino_resized2.gif")

# Move the turtle 1
t1.penup()
t1.goto(-250, 200)

# Move the turtle 2
t2.penup()
t2.goto(-250, 100)

# speed
speed_t1 = random.randint(1, 10)
speed_t2 = random.randint(1, 10)

# loop untuk pergerakan
while True:
    t1.forward(speed_t1)
    t2.forward(speed_t2)
    
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

# Close the turtle graphics window when clicked
screen.exitonclick()
