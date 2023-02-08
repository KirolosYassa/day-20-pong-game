from env import *


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()

        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_back(self):
        self.x_move *= -1

    def reset_position(self):
        self.ball_speed = SPEED
        self.goto(0, 0)
        self.bounce_back()

