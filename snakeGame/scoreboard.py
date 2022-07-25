from turtle import Turtle,textinput
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)

        self.name = textinput(title="enter the player Name : ", prompt="NAME")
        self.update()
    def update(self):

       self.write(f"{self.name}'s SCORE : {self.count}", align="center", font=("Courier", 12, "normal"))
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Courier",24,"normal"))
    def co(self):
        self.count+=1
        self.clear()
        self.update()