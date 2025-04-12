from turtle import Screen, Turtle
from src.paddles import Paddle
from src.ball import Ball

class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("🏓 PongMaster Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.color("white")
        self.writer.penup()

        self.left_player_name = ""
        self.right_player_name = ""

    def show_start_screen(self):
        self.writer.clear()
        self.writer.goto(0, 150)
        self.writer.write("🎮 Welcome to PongMaster 🎮", align="center", font=("Arial", 30, "bold"))

        self.writer.goto(0, 70)
        self.writer.write("Choose Difficulty:\nE - Easy  |  M - Medium  |  H - Hard", align="center", font=("Arial", 18, "normal"))

        self.writer.goto(0, -20)
        self.writer.write("Press E, M, or H to Start", align="center", font=("Arial", 16, "italic"))

        self.screen.listen()
        self.screen.onkey(lambda: self.start_game('easy'), "e")
        self.screen.onkey(lambda: self.start_game('medium'), "m")
        self.screen.onkey(lambda: self.start_game('hard'), "h")
        self.screen.mainloop()

    def start_game(self, mode):
        self._mode = mode
        speed_map = {"easy": 0.1, "medium": 0.07, "hard": 0.05}
        self.ball_speed = speed_map[mode]

        self.writer.clear()
        self.left_player_name = self.screen.textinput("Player 1", "Enter Left Player Name:") or "Player 1"
        self.right_player_name = self.screen.textinput("Player 2", "Enter Right Player Name:") or "Player 2"

        self.setup_game()
        self.run()

    def setup_game(self):
        self.paddle_left = Paddle(-350, 0, "cyan")
        self.paddle_right = Paddle(350, 0, "magenta")
        self.ball = Ball(self.ball_speed)
        self.score_left = 0
        self.score_right = 0

        self.writer.goto(0, 260)
        self.update_score()

        self.screen.listen()
        self.screen.onkeypress(self.paddle_left.move_up, "w")
        self.screen.onkeypress(self.paddle_left.move_down, "s")
        self.screen.onkeypress(self.paddle_right.move_up, "Up")
        self.screen.onkeypress(self.paddle_right.move_down, "Down")

    def update_score(self):
        self.writer.clear()
        self.writer.goto(0, 260)
        self.writer.write(f"{self.left_player_name}: {self.score_left}    {self.right_player_name}: {self.score_right}", align="center", font=("Arial", 18, "bold"))

    def run(self):
        while True:
            self.screen.update()
            self.ball.move()

            # Bounce on walls
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce_y()

            # Bounce on paddles
            if (self.ball.xcor() > 330 and self.ball.distance(self.paddle_right) < 50) or \
               (self.ball.xcor() < -330 and self.ball.distance(self.paddle_left) < 50):
                self.ball.bounce_x()

            # Missed
            if self.ball.xcor() > 380:
                self.score_left += 1
                self.update_score()
                self.ball.reset_position()

            if self.ball.xcor() < -380:
                self.score_right += 1
                self.update_score()
                self.ball.reset_position()
