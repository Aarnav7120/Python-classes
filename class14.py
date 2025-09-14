"""Polygon
Outline:
Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?"""

"""import turtle 
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500.500)
polygon = turtle.Turtle()

num_sides = 6
side_length = 100
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)


turtle.done()"""

"""Star
Outline:
Write a program to draw a star using a turtle?"""

"""import turtle

turtle.Screen().bgcolor("Aqua")
board= turtle.Turtle()

board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.penup()
board.right(150)
board.forward(50)

board.pendown()
board.right(90) 
board.forward(100)

board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

turtle.done() """

"""Spiral pattern
Outline:
Write a program to draw a square inside a square?"""

"""import turtle
my_wn =turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        my_pen.fd(size + 1)
        my_pen.left(90)
        size = size -5
    size = size + 1"""

"""import turtle
colors = [
    "red", "purple", "blue", "green", "orange", "yellow"]

my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    my_pen.pencolor(colors[x % 6])
    my_pen.width(x/100 + 1)
    my_pen.width(x)
    my_pen.left(59)

turtle.done:"""

import turtle 
loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.exitonclick()