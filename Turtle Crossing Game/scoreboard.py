from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", align= "left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align= "left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align= "center", font=FONT)

    def win(self):
        self.clear()
        self.goto(0,0)
        self.write(f"YOU WIN", align= "center", font=FONT)
