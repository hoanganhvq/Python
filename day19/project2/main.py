import random
from turtle import Turtle, Screen
colors = ["red", "green", "orange","yellow", "blue", "purple"]
y = [-100,-60,-20,20,60,100]
is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning = turtle.pencolor()
            if winning.lower() == user_bet.lower():
                print(f"You win, the {winning} turtle is the winner! ")
            else:
                print(f"You lose, the {winning} turtle is the winner")
        rand = random.randint(0,10)
        turtle.forward(rand)


screen.exitonclick() #it keep the screen which is not exit