# import colorgram
# color = colorgram.extract("hirst.jpg", 30)
# rgb_c=[]
# for colors in color:
#   r = colors.rgb.r
#   g = colors.rgb.g
#   b = colors.rgb.b
#   new_col=(r,g,b)
#   rgb_c.append(new_col)
# print(rgb_c)
import random
import turtle as t
t.colormode(255)
dott = t.Turtle()
dott.speed("fastest")

c = [ (41, 104, 174), (234, 205, 114), (228, 151, 85), (189, 46, 74), (231, 118, 144), (115, 90, 46), (110, 107, 189), (216, 60, 77), (114, 186, 136), (122, 176, 212), (52, 178, 110), (204, 16, 40), (115, 171, 36), (223, 57, 47), (31, 58, 117), (154, 223, 195), (182, 168, 223), (23, 142, 107), (29, 164, 172), (85, 35, 37), (39, 45, 84), (229, 169, 182), (232, 174, 161), (81, 39, 38), (151, 206, 223), (92, 43, 42)]
dott.penup()
dott.hideturtle()
dott.setheading(225)
dott.forward(300)
dott.setheading(0)
num=100
for a in range(1,num+1):
    dott.hideturtle()
    dott.penup()
    dott.dot(20, random.choice(c))
    dott.forward(50)
    if a % 10 == 0:
        dott.setheading(90)
        dott.forward(50)
        dott.setheading(180)
        dott.forward(500)
        dott.setheading(0)
    dott.pendown()


    # for b in range(10):
    #     dott.penup()
    #
    #     dott.forward(50)
    #     dott.pendown()
    #     dott.dot(20, random.choice(c))
    #     dott.color(random.choice(c))





screen = t.Screen()
screen.exitonclick()