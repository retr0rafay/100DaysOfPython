from turtle import Turtle, Screen
from playerpaddle import PlayerPaddle
from opponentpaddle import OpponentPaddle
from ball import Ball
import random
import time

screen = Screen()
screen.setup(800, 800)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

player_paddle = PlayerPaddle()
opponent_paddle = OpponentPaddle()
ball = Ball()
screen.onkey(player_paddle.up, "Up")
screen.onkey(player_paddle.down, "Down")
# Create the divider between players
y_position = 380

while y_position > -450:
    screen.update()
    line = Turtle()
    line.shape('square')
    line.color('white')
    line.shapesize(stretch_wid=0.3, stretch_len=0.8)
    line.penup()
    line.right(90)
    line.sety(y_position)
    y_position -= 40

screen.tracer(1)
game_on = True

while game_on:
    screen.update()
    ball.move()

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    if ball.distance(player_paddle) < 30:
        ball.bounce_x()

    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.out_of_bounds()

screen.exitonclick()
