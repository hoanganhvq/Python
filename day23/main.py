import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard =  Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()
    #Detect with car
    for car in car_manager.cars:
        if car.distance(player) <= 20:
            scoreboard.game_over()
            game_is_on = False

    #Detect with line
    if player.is_at_finish_line():
        scoreboard.increse_level()
        player.reset()
        car_manager.level_up()


screen.exitonclick()