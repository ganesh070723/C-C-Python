import turtle as t
import time
pos=[(0,0),(-20,0),(-40,0)]
t.bgcolor("black")
screen = t.Screen()
snake_move=[]
screen.tracer(0)
for a in pos:
   snake = t.Turtle("square")
   snake.color("white")
   snake .penup()
   snake.goto(a)
   snake_move.append(snake)
gameIsOn=True

while gameIsOn:
    screen.update()
    time.sleep(0.1)
    for snakenum in range(len(snake_move)-1,0,-1):
      newx = snake_move[snakenum-1].xcor()
      newy = snake_move[snakenum-1].ycor()
      snake_move[snakenum].goto(newx,newy)
    snake_move[0].forward(20)
    snake_move[0].left(90)

screen.title("Snake Game CG")
screen.setup(500,500)
screen.exitonclick()