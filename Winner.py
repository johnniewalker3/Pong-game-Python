from turtle import *

FINISH = 3

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'normal')


class Winner(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.hideturtle()
        self.goto(0, 0)

    def checkWinner(self, score1, score2):
        if score1.player1 == FINISH:
            self.write(f"Winner is Player1", align=ALIGNMENT, font=FONT)
        elif score2.player2 == FINISH:
            self.write(f"Winner is Player2", align=ALIGNMENT, font=FONT)
