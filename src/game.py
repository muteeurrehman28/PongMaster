import turtle
from src.paddles import Paddle
from src.ball import Ball
from src.scoreboard import Scoreboard

# CONSTANTS
WIN_WIDTH, WIN_HEIGHT = 800, 600
MAX_BALL_SPEED = 15
FRAME_DELAY = 20  # milliseconds

class PongMaster:
    def __init__(self):
        # screen
        self.wn = turtle.Screen()
        self.wn.title("🏓 PongMaster")
        self.wn.bgcolor("black")
        self.wn.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
        self.wn.tracer(0)

        self.draw_border()
        self.speed, self.left_name, self.right_name = self.get_player_info()

        # game objects
        self.left_paddle = Paddle(-WIN_WIDTH//2 + 40, self.left_name)
        self.right_paddle = Paddle(WIN_WIDTH//2 - 40, self.right_name)
        self.ball = Ball(self.speed)
        self.scoreboard = Scoreboard(self.left_name, self.right_name)

        # controls
        self.paused = False
        self.wn.listen()
        self.wn.onkeypress(self.left_paddle.move_up, "w")
        self.wn.onkeypress(self.left_paddle.move_down, "s")
        self.wn.onkeypress(self.right_paddle.move_up, "Up")
        self.wn.onkeypress(self.right_paddle.move_down, "Down")
        self.wn.onkeypress(self.toggle_pause, "p")
        self.wn.onkeypress(self.toggle_pause, "r")

        # start loop
        self.game_loop()
        self.wn.mainloop()

    def draw_border(self):
        border = turtle.Turtle()
        border.hideturtle()
        border.color("white")
        border.penup()
        border.goto(-WIN_WIDTH//2, WIN_HEIGHT//2)
        border.pendown()
        for _ in range(4):
            border.forward(WIN_WIDTH if _ % 2 == 0 else WIN_HEIGHT)
            border.right(90)

    def get_player_info(self):
        diff = self.wn.textinput("Difficulty", "Choose: Easy / Medium / Hard").lower()
        if diff == "easy":
            speed = 4
        elif diff == "hard":
            speed = 8
        else:
            speed = 6  # medium default

        left_name = self.wn.textinput("Player 1", "Enter name for Player 1:") or "Left"
        right_name = self.wn.textinput("Player 2", "Enter name for Player 2:") or "Right"
        return speed, left_name, right_name

    def toggle_pause(self):
        self.paused = not self.paused
        if not self.paused:
            self.game_loop()

    def game_loop(self):
        if self.paused:
            return

        self.ball.move()

        # wall bounce
        if abs(self.ball.ycor()) > WIN_HEIGHT//2 - 20:
            self.ball.bounce_y()

        # Improved Paddle Collisions
        # Right paddle
        if (self.ball.xcor() > WIN_WIDTH//2 - 60 and
            abs(self.ball.ycor() - self.right_paddle.ycor()) < 50):
            self.ball.setx(WIN_WIDTH//2 - 60)      # push out
            self.ball.bounce_x()

        # Left paddle
        if (self.ball.xcor() < -WIN_WIDTH//2 + 60 and
            abs(self.ball.ycor() - self.left_paddle.ycor()) < 50):
            self.ball.setx(-WIN_WIDTH//2 + 60)     # push out
            self.ball.bounce_x()

        # scoring: bounce off side wall
        if abs(self.ball.xcor()) > WIN_WIDTH//2 - 10:
            if self.ball.xcor() > 0:
                self.scoreboard.left_point()
            else:
                self.scoreboard.right_point()

            # bounce instead of reset
            self.ball.bounce_x()

            # check win
            if self.scoreboard.left_score == 10:
                return self.end_game(self.left_name)
            if self.scoreboard.right_score == 10:
                return self.end_game(self.right_name)

        self.wn.update()
        self.wn.ontimer(self.game_loop, FRAME_DELAY)

    def end_game(self, winner):
        self.wn.clear()
        self.wn.bgcolor("black")
        msg = turtle.Turtle()
        msg.color("white")
        msg.hideturtle()
        msg.write(f"{winner} wins! 🎉", align="center", font=("Courier", 36, "bold"))
        msg.goto(0, -50)
        msg.write("Click to play again or close window to quit", align="center", font=("Courier", 16, "normal"))
        self.wn.exitonclick()
        self.__init__()  # restart cleanly
