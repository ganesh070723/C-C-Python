import turtle
from turtle import Turtle
from random import randint
def randc():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    col = (r, g, b)
    return col;
class Food(Turtle):


    def __init__(self):
        super().__init__()
        turtle.colormode(255)
        self.shape("circle")
        self.penup()
        self.speed(10)
        self.shapesize(0.5, 0.5)
        self.foodsup()

    def foodsup(self):
        self.color(randc())

        randx = randint(-280, 280)
        randy = randint(-280, 280)
        self.goto(randx, randy)


