from turtle import Turtle

UP = 90
DOWN = 270


class PlayerPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.right(90)
        self.setx(-380)

    def up(self):
        self.bk(30)
        self.speed('fastest')

    def down(self):
        self.setheading(270)
        self.forward(30)
        self.speed('fastest')
