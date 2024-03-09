from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():
    def __init__(self):
        self.segment =[]
        self.createsnake()
        self.head = self.segment[0]

    def createsnake(self):
        for position in STARTING_POSITION:
            self.add(position)

    def add(self,position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segment.append(new_segment)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.createsnake()


    def extent(self):
        self.add(self.segment[-1].position())
    def move(self):
       for seg_num in range(len(self.segment)- 1, 0, -1):
           new_x = self.segment[seg_num - 1].xcor()
           new_y = self.segment[seg_num - 1].ycor()
           self.segment[seg_num].goto(new_x,new_y)
       self.head.forward(MOVE_DISTANCE)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)