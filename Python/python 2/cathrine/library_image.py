import numpy as np
from PIL import Image

def do_something(left, right):
    left_array = np.array(left.resize(right.size))
    right_array = np.array(right)

    left_array[:, :, 0] = right_array[:, :, 0]
    return Image.fromarray(left_array)

def do_stuff(a, b, c):
    a = b + c
    c = a + b
    return a

a = 145
one = 20
two = 25
one = do_stuff(a, one, two)

# Load pictures
pic1 = Image.open("pisang.jpg")
pic2 = Image.open("curby.jpg")

result_image = do_something(pic1, pic2)

# Save or display the result_image as needed
result_image.save("result.jpg")
result_image.show()

number = 10.5

test = round(number)

print(test)