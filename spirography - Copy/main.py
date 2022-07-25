import turtle as t
import random
t.colormode(255)
def randomcolours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
circle = t.Turtle()
circle.pensize(3)
circle.speed("fastest")
def siprography(size_of_gap):
    for _ in range(round(360/size_of_gap)):
        circle.color(randomcolours())
        circle.circle(150)
        circle.setheading(circle.heading() + 10)

siprography(9)
# for _ in range(37):
#     circle.color(randomcolours())
#     circle.forward(15)
#     circle.right(10)

screen = t.Screen()
screen.exitonclick()