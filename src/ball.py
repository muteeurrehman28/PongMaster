import turtle
import random

class Ball(turtle.Turtle):
    def __init__(self, base_speed):
        super().__init__(shape="circle")
        self.color("yellow")
        self.penup()
        self.base_speed = base_speed
        self.reset()

    def reset(self):
        self.goto(0, 0)
        self.dx = self.base_speed * random.choice((1, -1))
        self.dy = self.base_speed * random.choice((1, -1))

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        new_speed = min(abs(self.dx) * 1.02, 15)
        self.dx = -new_speed if self.dx > 0 else new_speed
