import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(1)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.15
        self.dy = -0.15

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def check_bounce(self):
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1
        elif self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1
