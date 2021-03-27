from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = -10
        self.y_move = 20

    def move(self):
        x_coor = self.xcor() + self.x_move
        y_coor = self.ycor() + self.y_move
        self.goto(x_coor, y_coor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def out_of_bounds(self):
        self.goto(0, 0)
        self.bounce_x()