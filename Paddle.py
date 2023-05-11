from turtle import Turtle

Y = 20


class Paddle():
    def __init__(self, x):
        self.paddle = []
        self.paddle.append(Turtle())
        self.paddle[0].penup()
        self.paddle[0].shape("square")
        self.paddle[0].goto(x, Y)
        self.paddle[0].setheading(90)
        self.create_blocks()

    def create_blocks(self):
        self.paddle.append(Turtle())
        self.paddle[1].penup()
        self.paddle[1].shape("square")
        self.paddle[1].setheading(90)
        self.paddle[1].goto(self.paddle[0].xcor(), Y - 20)

        self.paddle.append(Turtle())
        self.paddle[2].penup()
        self.paddle[2].shape("square")
        self.paddle[2].setheading(90)
        self.paddle[2].goto(self.paddle[0].xcor(), Y - 2 * 20)

    def moveUp(self):
        if self.paddle[0].ycor() <= 220:
            for i in range(len(self.paddle) - 1, 0, -1):
                self.paddle[i].setheading(90)
                self.paddle[i].goto(self.paddle[i - 1].pos())
            self.paddle[0].setheading(90)
            self.paddle[0].forward(20)

    def moveDown(self):
        if self.paddle[2].ycor() >= -220:
            for i in range(0, len(self.paddle) - 1):
                self.paddle[i].setheading(270)
                self.paddle[i].goto(self.paddle[i + 1].pos())
            self.paddle[2].setheading(270)
            self.paddle[2].forward(20)
