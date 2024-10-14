from turtle import Turtle

starting_positions=[(0,0),(-15,0),(-30,0)]

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()


    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
            self.segments[0].forward(20)

    def add_segment(self,position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.speed("fastest")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def up(self):
        if self.segments[0].heading() !=270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() !=90:
           self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)