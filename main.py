from turtle import *
from DashLine import DashLine
from ScoreBoard import ScorePlayer1
from ScoreBoard import ScorePlayer2
from Paddle import Paddle
from Ball import Ball
from Winner import *
import time

LEFT_BOUND = -240
RIGHT_BOUND = 240

screen = Screen()
screen.setup(500, 500)
screen.tracer(0)

court = DashLine()
score1 = ScorePlayer1()
score2 = ScorePlayer2()
ball = Ball()
winner = Winner()

first_paddle = Paddle(-230)
second_paddle = Paddle(230)

screen.listen()
# for first paddle
screen.onkey(fun=first_paddle.moveUp, key='w')
screen.onkey(fun=first_paddle.moveDown, key='s')

# for second paddle
screen.onkey(fun=second_paddle.moveUp, key='Up')
screen.onkey(fun=second_paddle.moveDown, key='Down')

while True:
    screen.update()
    time.sleep(0.15)
    ball.move()
    ball.detect_collision_with_paddle(first_paddle, second_paddle)
    ball.detect_collision_with_bounds()
    ball_pos = ball.pos()
    if ball_pos[0] <= LEFT_BOUND:
        score2.incr_score()
        ball.ball_init()
    elif ball_pos[0] >= RIGHT_BOUND:
        score1.incr_score()
        ball.ball_init()
    if score1.player1 == FINISH or score2.player2 == FINISH:
        winner.checkWinner(score1, score2)
        break


screen.exitonclick()
