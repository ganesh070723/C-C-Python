import turtle as t
import random
t.setup(width=800, height=600)
screen = t.Screen()
#israce=False
colors = ["red","Indianred","orange","green","purple","SkyBlue"]
turtles_list=[]
y = -150
for index in range(0,6):
    turtle = t.Turtle()
    turtle.color(colors[index])
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(-380,y)
    y+=50
    turtles_list.append(turtle)
user = t.textinput(title="MAKE A CHOICE",prompt="ChOoSe AnY OnE CoLoR")
israce=False
if user:
 israce=True

while israce:
    for a in turtles_list:
        if a.xcor() > 370:
            israce=False
            wincolor = a.pencolor()
            if user== wincolor:
                print(f"you've won!,the {wincolor} color turtle is the winner")
            else:
                print(f"you lose!,the {wincolor} color turtle is the winner")
          
        randomphase = random.randint(0,10)
        a.forward(randomphase)
    









screen.exitonclick()