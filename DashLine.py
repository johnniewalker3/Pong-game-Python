from turtle import *


class DashLine(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(0, -230)
        self.left(90)
        self.draw_line()

    def draw_line(self):
        self.pensize(6)
        for _ in range(24):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
