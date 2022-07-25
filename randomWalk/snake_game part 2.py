import turtle as t
import time

screen = t.Screen()
screen.tracer(1)
POS=[(0,0),(-20,0),(-40,0)]
class Snake:
    
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.move()
    def create_snake(self):
       for a in POS:
          
          snake = t.Turtle("square")
          snake.color("white")
          snake .penup()
          snake.goto(a)
          self.segment.append(snake)
    def move(self):
            for snakenum in range(len(self.segment)-1,0,-1):
                  
                  newx = self.segment[snakenum-1].xcor()
                  newy = self.segment[snakenum-1].ycor()
                  self.segment[snakenum].goto(newx,newy)
            self.segment[0].forward(20)
                 

 
screen.bgcolor("black")

screen.title("Snake Game CG")
screen.setup(600,600)

snake = Snake()

snake.create_snake()

gameIsOn=True

while gameIsOn:
    screen.update()
    #time.sleep(0.1)
    snake.move()
    
   


screen.exitonclick()
