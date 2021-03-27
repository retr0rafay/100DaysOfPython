from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = list()
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle('square')
            car.penup()
            car.shapesize(stretch_wid=2, stretch_len=1)
            car.tiltangle(90)
            car.setheading(0)
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.setposition(300, random_y)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.back(self.car_speed)

    def level_up_car(self):
        self.car_speed += MOVE_INCREMENT
