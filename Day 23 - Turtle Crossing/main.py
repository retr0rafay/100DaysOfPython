import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
scoreBoard = Scoreboard()
list_of_cars = cars.all_cars
screen.onkeypress(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()
    for car in list_of_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreBoard.game_over()
    if player.ycor() >= 280:
        player.goto(0, -280)
        scoreBoard.increase_level()
        cars.level_up_car()

screen.exitonclick()