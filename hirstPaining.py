from turtle import Turtle, Screen
import random

raphael_ninja_turtle = Turtle()
Screen().colormode(255)
list_of_colors = [(245, 243, 238), (248, 241, 244), (237, 240, 246), (201, 164, 112), (238, 246, 241), (152, 75, 49),
                  (221, 201, 138), (171, 153, 42), (56, 95, 126), (139, 31, 19), (134, 163, 184), (197, 93, 73),
                  (48, 121, 88), (98, 75, 77), (142, 178, 148), (75, 41, 33), (165, 145, 156), (15, 99, 71),
                  (234, 175, 164), (54, 45, 47), (32, 61, 77), (145, 21, 25), (21, 83, 89), (182, 205, 175),
                  (85, 147, 127), (44, 66, 87), (178, 94, 98), (222, 177, 184), (8, 68, 51), (108, 127, 151)]

x_position = -300
raphael_ninja_turtle.penup()
raphael_ninja_turtle.setx(x_position)
raphael_ninja_turtle.sety(-30)
for row in range(10):
    for color in range(10):
        raphael_ninja_turtle.dot(20, random.choice(list_of_colors))
        raphael_ninja_turtle.penup()
        if color == 9:
            break
        else:
            raphael_ninja_turtle.forward(50)
    raphael_ninja_turtle.left(90)
    raphael_ninja_turtle.forward(50)
    raphael_ninja_turtle.setx(x_position)
    raphael_ninja_turtle.right(90)

screen = Screen()
screen.screensize(1000, 1000)
screen.exitonclick()
