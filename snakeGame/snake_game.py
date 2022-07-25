import turtle as t

POS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_FORWARD = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for a in POS:
          self.add_new(a)
    def add_new(self,a):

            snake = t.Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(a)
            self.segment.append(snake)
    def extent(self):
        self.add_new(self.segment[-1].position())

    def move(self):

        for snakenum in range(len(self.segment) - 1, 0, -1):
            newx = self.segment[snakenum - 1].xcor()
            newy = self.segment[snakenum - 1].ycor()
            self.segment[snakenum].goto(newx, newy)
        self.segment[0].forward(MOVE_FORWARD)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)







