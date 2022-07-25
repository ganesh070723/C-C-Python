import time
from turtle import Turtle, Screen
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("CG's Game")
screen.tracer(0)
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
class Snake:
    
    def __init__(self):
        
        self.segment=[]
        self.create_snake()
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)
            
    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            new_x = self.segment[seg_num-1].xcor()
            new_y = self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.segment[0].forward(20 )


snake = Snake()

game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()