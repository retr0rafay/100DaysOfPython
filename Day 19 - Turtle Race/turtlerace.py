from turtle import Turtle, Screen
import random

leonardo = Turtle()
donatello = Turtle()
michelangelo = Turtle()
raphael = Turtle()

# Set turtle colors
leonardo.color("blue")
donatello.color("purple")
michelangelo.color("orange")
raphael.color("red")

# Set turtle shape
leonardo.shape("turtle")
donatello.shape("turtle")
michelangelo.shape("turtle")
raphael.shape("turtle")

ninja_turtles = [leonardo, donatello, michelangelo, raphael]

screen = Screen()
screen.setup(width=500, height=400)
# Ask user for winner choice
user_answer = screen.textinput(prompt="Who do you think will win the race?", title="Make Your Choice")
y_position = 0

# Starting positions
for turtle in ninja_turtles:
    turtle.penup()
    turtle.goto(-200, y_position)
    y_position += 40

race = True
# Run the race
while race:
    for turtle in ninja_turtles:
        turtle.forward(random.randrange(10, 25))
        if turtle.xcor() >= 250:
            if user_answer == turtle.pencolor():
                print(f'You win. The {turtle.pencolor()} turtle won the race.')
                race = False
                break
            else:
                print(f'You lose. The {turtle.pencolor()} turtle won the race.')
                race = False
                break
                
screen.exitonclick()
