from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("My Snack Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #Detect with food
    if snake.head.distance(food) <= 15:
        food.random_location()
        snake.extent()
        scoreboard.increase_score()

    #Detect with line
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
       snake.reset()

    #Detect with tail
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) <= 15:
            is_game_on = False
            scoreboard.game_over()







screen.exitonclick()