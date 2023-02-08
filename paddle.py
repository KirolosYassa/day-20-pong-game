from env import *


class Paddle(Turtle):

    def __init__(self, player):
        self.steps = 20
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if player == 0:
            self.goto(x=PADDLE_POSITION_LEFT, y=0)
            return
        self.goto(x=PADDLE_POSITION_RIGHT, y=0)

    def up(self):
        new_y = self.ycor() + self.steps
        self.sety(y=new_y)

    def down(self):
        new_y = self.ycor() - self.steps
        self.sety(y=new_y)

    def increase_speed(self):
        self.steps = self.steps + 10

    def reset_speed(self):
        self.steps = STEPS
