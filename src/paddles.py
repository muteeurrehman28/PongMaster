import turtle

class Paddle(turtle.Turtle):
    def __init__(self, x_pos, name):
        super().__init__(shape="square")
        self.name = name
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)

    def move_up(self):
        if self.ycor() < 600//2 - 40:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -600//2 + 40:
            self.sety(self.ycor() - 20)
