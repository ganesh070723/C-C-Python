# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 01:20:12 2021

@author: ganes
"""

import turtle as t
from foodd import Food
from scoreboard import Score
import time
from snake_game import Snake
screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game CG")
screen.tracer(0)
snake = Snake()
score = Score()

food = Food()
snake.create_snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segment[0].distance(food) < 20:
        food.foodsup()
        snake.extent()
        score.co()
    if snake.segment[0].xcor() > 300 or snake.segment[0].xcor() < -300 or snake.segment[0].ycor() > 300 or snake.segment[0].ycor() < -300:
       score.gameover()
       game=False
    for segment in snake.segment[1:]:
       if snake.segment[0].distance(segment) < 10:
            score.gameover()
            game =False

screen.exitonclick()
