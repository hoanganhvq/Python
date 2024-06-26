import random
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER !", align=ALIGNMENT, font=FONT)

