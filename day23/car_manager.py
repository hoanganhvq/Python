from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        ran = random.randint(1,6)
        if ran == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250,250)
            new_car.goto(300, new_y)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT