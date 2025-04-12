from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.dx = 2  # Speed in the x direction
        self.dy = 2  # Speed in the y direction
        self.move_speed = speed

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def check_collision_with_wall(self):
        # If the ball hits the top or bottom wall, bounce
        if self.ycor() > 290 or self.ycor() < -290:
            self.bounce_y()

        # If the ball hits the left or right wall, bounce
        if self.xcor() > 290 or self.xcor() < -290:
            self.bounce_x()