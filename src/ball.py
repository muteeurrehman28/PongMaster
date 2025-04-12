import turtle

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.dx = 3
        self.dy = 3

    def move(self):
        x = self.ball.xcor() + self.dx
        y = self.ball.ycor() + self.dy
        self.ball.setx(x)
        self.ball.sety(y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.ball.goto(0, 0)
        self.dx *= -1

    def xcor(self):
        return self.ball.xcor()

    def ycor(self):
        return self.ball.ycor()

    def distance(self, paddle):
        return self.ball.distance(paddle)
