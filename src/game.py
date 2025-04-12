import turtle
from src.paddles import Paddle
from src.ball import Ball

class Game:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("PongMaster")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        self.difficulty = "medium"
        self.ball_speed = 0.05

        self.paddle_left = Paddle(-350, 0)
        self.paddle_right = Paddle(350, 0)
        self.ball = Ball()

        self.score_left = 0
        self.score_right = 0

        self.score_writer = turtle.Turtle()
        self.score_writer.speed(0)
        self.score_writer.color("white")
        self.score_writer.penup()
        self.score_writer.hideturtle()
        self.score_writer.goto(0, 260)
        self.update_score()

        self.window.listen()
        self.window.onkeypress(self.paddle_left.move_up, "w")
        self.window.onkeypress(self.paddle_left.move_down, "s")
        self.window.onkeypress(self.paddle_right.move_up, "Up")
        self.window.onkeypress(self.paddle_right.move_down, "Down")

    def update_score(self):
        self.score_writer.clear()
        self.score_writer.write(f"Player A: {self.score_left}  Player B: {self.score_right}",
                                align="center", font=("Courier", 20, "normal"))

    def show_menu(self):
        menu_writer = turtle.Turtle()
        menu_writer.color("white")
        menu_writer.penup()
        menu_writer.hideturtle()
        menu_writer.goto(0, 100)
        menu_writer.write("Select Difficulty:\n1 - Easy\n2 - Medium\n3 - Hard",
                          align="center", font=("Courier", 18, "bold"))

        self.window.onkey(lambda: self.set_difficulty("easy"), "1")
        self.window.onkey(lambda: self.set_difficulty("medium"), "2")
        self.window.onkey(lambda: self.set_difficulty("hard"), "3")

        self.window.mainloop()

    def set_difficulty(self, level):
        self.difficulty = level
        if level == "easy":
            self.ball_speed = 0.09
        elif level == "medium":
            self.ball_speed = 0.05
        elif level == "hard":
            self.ball_speed = 0.03

        self.window.clearscreen()
        self.__init__()
        self.run()

    def run(self):
        while True:
            self.window.update()
            self.ball.move()

            if self.ball.xcor() > 340 and self.ball.distance(self.paddle_right.paddle) < 50:
                self.ball.bounce_x()
            if self.ball.xcor() < -340 and self.ball.distance(self.paddle_left.paddle) < 50:
                self.ball.bounce_x()

            if self.ball.ycor() > 290 or self.ball.ycor() < -290:
                self.ball.bounce_y()

            if self.ball.xcor() > 390:
                self.score_left += 1
                self.update_score()
                self.ball.reset_position()

            if self.ball.xcor() < -390:
                self.score_right += 1
                self.update_score()
                self.ball.reset_position()

            turtle.delay(int(self.ball_speed * 1000))
