import turtle as t
POS=[(0,0),(-20,0),(-40,0)]
class Snake:
    
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.move()
    def create_snake(self):
       for a in pos:
          snake = t.Turtle("square")
          snake.color("white")
          snake .penup()
          snake.goto(a)
          self.segment.append(snake)
    def move(self):
       for snakenum in range(len(self.segment)-1,0,-1):
                  newx = segment[snakenum-1].xcor()
                  newy = segment[snakenum-1].ycor()
                  segment[snakenum].goto(newx,newy)

        self.segment[0].forward(20)
        self.segment[0].left(90)                                
