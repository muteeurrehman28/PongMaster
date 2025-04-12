import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.2
        self.dy = 0.2
        self.speed = 2  # Default ball speed

    def move(self):
        self.setx(self.xcor() + self.dx * self.speed)
        self.sety(self.ycor() + self.dy * self.speed)

        # Ball boundary collision
        if self.ycor() > 290:
            self.dy *= -1
        if self.ycor() < -290:
            self.dy *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.dy *= -1
        self.dx *= -1
