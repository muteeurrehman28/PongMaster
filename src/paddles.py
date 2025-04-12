import turtle

class Paddle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(x, y)
        self.speed(0)

    def move_up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)
