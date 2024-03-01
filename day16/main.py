# from turtle import Turtle, Screen
# screen = Screen()
# vy = Turtle()
# # Tao doi tuong ne
# print(vy)
# vy.shape("turtle")
# vy.color("coral")
# vy.forward(500)
# print(screen.canvheight)
# screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
table.align["Pokemon"] = "l"
table.align["Type"] = "l"

print(table)