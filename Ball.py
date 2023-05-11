from turtle import *
import random

UP_BOUND = 230
DOWN_BOUND = -230

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x = -1
        self.y = 1
        self.penup()
        self.shape("square")
        self.goto(0, 0)
        self.xcord = 0
        self.ycord = 0

    def ball_init(self):
        self.xcord = 0
        self.ycord = 0
        self.home()

    def move(self):

        self.xcord += (10 * self.x)
        self.ycord += (20 * self.y)
        self.goto(self.xcord, self.ycord)

    def detect_collision_with_paddle(self, first_paddle, second_paddle):
        if self.distance(first_paddle.paddle[0]) <= 15 or self.distance(first_paddle.paddle[1]) <= 10 or self.distance(
                first_paddle.paddle[2]) <= 10:
            self.x = - self.x
            self.y = random.choice([-1, 1])
        elif self.distance(second_paddle.paddle[0]) <= 15 or self.distance(
                second_paddle.paddle[1]) <= 10 or self.distance(second_paddle.paddle[2]) <= 10:
            self.x = - self.x
            self.y = random.choice([-1, 1])

    def detect_collision_with_bounds(self):
        if self.ycor() >= UP_BOUND:
            self.y = -1
        elif self.ycor() <= DOWN_BOUND:
            self.y = 1


