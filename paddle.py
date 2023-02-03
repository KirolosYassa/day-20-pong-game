from turtle import Turtle
import time
WIDTH = 800
HEIGHT = 600
PADDLE_POSITION_RIGHT = WIDTH/2 - 30
PADDLE_POSITION_LEFT = -WIDTH/2 + 30
SPEED = 0.05
STEPS = 20


class Paddle(Turtle):

    def __init__(self, player):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if player == 0:
            self.goto(x=PADDLE_POSITION_LEFT, y=0)
            return
        self.goto(x=PADDLE_POSITION_RIGHT, y=0)

    def up(self):
        new_y = self.ycor() + STEPS
        self.sety(y=new_y)

    def down(self):
        new_y = self.ycor() - STEPS
        self.sety(y=new_y)
