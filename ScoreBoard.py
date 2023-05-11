from turtle import *

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class ScorePlayer1(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.left(90)
        self.goto(-65, 220)
        self.color('black')
        self.player1 = 0
        self.update_score()

    def update_score(self):
        self.write(f"{self.player1}", font=FONT)

    def incr_score(self):
        self.clear()
        self.player1 += 1
        self.update_score()


class ScorePlayer2(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.left(90)
        self.goto(50, 220)
        self.color('black')
        self.player2 = 0
        self.update_score()

    def update_score(self):
        self.write(f"{self.player2}", font=FONT)

    def incr_score(self):
        self.clear()
        self.player2 += 1
        self.update_score()
