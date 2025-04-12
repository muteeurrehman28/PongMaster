import turtle
from src.paddles import Paddle
from src.ball import Ball

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Pong Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

        self.left_paddle = Paddle(-350, 0)
        self.right_paddle = Paddle(350, 0)
        self.ball = Ball()
        
        # Score variables
        self.left_score = 0
        self.right_score = 0

        # Score display
        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 260)
        self.score_display.write(f"Left: {self.left_score}  Right: {self.right_score}", align="center", font=("Courier", 24, "normal"))

    def run(self):
        self.screen.listen()
        self.screen.onkey(self.left_paddle.move_up, "w")
        self.screen.onkey(self.left_paddle.move_down, "s")
        self.screen.onkey(self.right_paddle.move_up, "Up")
        self.screen.onkey(self.right_paddle.move_down, "Down")

        while True:
            self.screen.update()

            # Move the ball
            self.ball.move()

            # Ball paddle collision
            self.ball.check_collision(self.left_paddle, self.right_paddle)

            # Check if ball is out of bounds
            if self.ball.xcor() > 390:
                self.ball.reset_position()
                self.left_score += 1
                self.update_score()

            if self.ball.xcor() < -390:
                self.ball.reset_position()
                self.right_score += 1
                self.update_score()

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"Left: {self.left_score}  Right: {self.right_score}", align="center", font=("Courier", 24, "normal"))
