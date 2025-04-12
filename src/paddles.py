import turtle

class Paddle:
    def __init__(self, x, y):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)

    def move_up(self):
        y = self.paddle.ycor()
        if y < 250:
            self.paddle.sety(y + 15)

    def move_down(self):
        y = self.paddle.ycor()
        if y > -250:
            self.paddle.sety(y - 15)
