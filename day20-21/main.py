from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Move the snake
is_game_on = True
while is_game_on:
    screen.update() # update the move of all segment
    time.sleep(0.1)
    snake.move()

    #Phats hien va cham voi thuc an
    if snake.head.distance(food) < 15:
        print("Ăn")
        food.refresh()
        snake.extent()
        scoreboard.increase_score()
    #Phat hien va cham voi tuong'
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        # scoreboard.reset()
        snake.changeLocateonY()
        # snake.reset_snake()
    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # scoreboard.reset()
        snake.changeLocateonX()
        # snake.reset_snake()

    #Phat hien va cham voi duoi
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()