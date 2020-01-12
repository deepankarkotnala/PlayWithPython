import turtle   # importing the turtle module

my_turtle = turtle.Turtle()

# Defining a function which creates a square based on the parameters "length" and "angle" passed to it
def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

# A loop for calling the square function 33 times. This will create an interesting pattern!
for i in range(33):
    square(200, 90)
    my_turtle.right(11)
