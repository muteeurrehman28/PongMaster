import turtle
from src.paddles import Paddle
from src.ball import Ball

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("PongMaster")
        self.screen.bgcolor("#1e1e2e")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

        self.score_left = 0
        self.score_right = 0

        self.paddle_left = Paddle(-350, 0, "#ff6f61")   # Coral
        self.paddle_right = Paddle(350, 0, "#6c5ce7")   # Purple
        self.ball = Ball("#00cec9")  # Cyan

        self.screen.listen()
        self.screen.onkeypress(self.paddle_left.move_up, "w")
        self.screen.onkeypress(self.paddle_left.move_down, "s")
        self.screen.onkeypress(self.paddle_right.move_up, "Up")
        self.screen.onkeypress(self.paddle_right.move_down, "Down")

        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("#fdcb6e")  # Yellow
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(0, 260)

    def show_menu(self):
        writer = turtle.Turtle()
        writer.color("#fab1a0")
        writer.penup()
        writer.hideturtle()
        writer.goto(0, 50)
        writer.write("Select Difficulty:\n1. Easy   2. Medium   3. Hard", align="center", font=("Courier", 24, "bold"))

        self.difficulty = None
        self.screen.onkeypress(lambda: self.set_difficulty(1), "1")
        self.screen.onkeypress(lambda: self.set_difficulty(2), "2")
        self.screen.onkeypress(lambda: self.set_difficulty(3), "3")

        while self.difficulty is None:
            self.screen.update()

        writer.clear()
        self.run()

    def set_difficulty(self, level):
        self.ball.dx = 0.175 if level == 1 else (0.225 if level == 2 else 0.275)
        self.ball.dy = 0.175 if level == 1 else (0.225 if level == 2 else 0.275)
        self.difficulty = level

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"{self.score_left}  :  {self.score_right}", align="center", font=("Courier", 28, "bold"))

    def run(self):
        self.update_score()

        while True:
            self.screen.update()
            self.ball.move()

            if self.ball.ycor() > 290 or self.ball.ycor() < -290:
                self.ball.bounce_y()

            if self.ball.xcor() > 390:
                self.ball.reset_position()
                self.score_left += 1
                self.update_score()

            if self.ball.xcor() < -390:
                self.ball.reset_position()
                self.score_right += 1
                self.update_score()

            if (340 < self.ball.xcor() < 350 and self.ball.distance(self.paddle_right) < 50) or \
               (-350 < self.ball.xcor() < -340 and self.ball.distance(self.paddle_left) < 50):
                self.ball.bounce_x()
