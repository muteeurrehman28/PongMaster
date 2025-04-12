import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.1  # Default speed, will be overridden by the menu selection
        self.dy = 0.1  # Default speed, will be overridden by the menu selection

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
