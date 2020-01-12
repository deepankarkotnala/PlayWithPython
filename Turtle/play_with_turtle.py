import turtle

my_turtle = turtle.Turtle()

def square(length, angle):
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)

for i in range(33):
    square(200, 90)
    my_turtle.right(11)
