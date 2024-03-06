from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        # Create 3 white segment in begining
        for position in STARTING_POSITION:
            self.add_segment(position)
    def changeLocateonX(self):
        new_y = self.head.ycor() * -1
        self.head.goto(self.head.xcor(), new_y)

    def changeLocateonY(self):
        new_x = self.head.xcor() * -1
        self.head.goto(new_x, self.head.ycor())
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,100)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extent(self):
        #add a new segment to the snack
        self.add_segment(self.segments[-1].position()) # get the positon (x,y) of the last element in position


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, - 1):  # Nạp đè lên nhau, thì cục 3 se d qua 2
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)