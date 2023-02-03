import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)

    def move(self, y_direction=True):
        new_x = self.xcor() + 6
        if y_direction:
            new_y = self.ycor() + 6
        else:
            new_y = self.ycor() - 6
        self.goto(x=new_x, y=new_y)
