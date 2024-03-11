import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S.A Game")

image = "blank_states_img.gif"
screen.addshape(image)  #Python only support image with .gif
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_state = []
while len(guess_state) < 50:

    answer = screen.textinput(f"{len(guess_state)}/50 States Correct", "What's your guess").title()

    if answer in all_states:
        guess_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())



#Ham nay cho  phep hien thi toa do khi click vao man hinh
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# # 2 dong nay hoat dong nhu nhau
# turtle.mainloop()
screen.exitonclick()