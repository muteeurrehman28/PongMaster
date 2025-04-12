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

        # Ball bouncing off top and bottom
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1

        if self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1

    def check_collision(self, left_paddle, right_paddle):
        if (self.xcor() > 340 and self.xcor() < 350) and (self.ycor() < right_paddle.ycor() + 50 and self.ycor() > right_paddle.ycor() - 50):
            self.setx(340)
            self.dx *= -1

        if (self.xcor() < -340 and self.xcor() > -350) and (self.ycor() < left_paddle.ycor() + 50 and self.ycor() > left_paddle.ycor() - 50):
            self.setx(-340)
            self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.dx *= -1
