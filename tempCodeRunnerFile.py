import turtle
import random

# ──────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ──────────────────────────────────────────────────────────────────────────────
WIN_WIDTH, WIN_HEIGHT = 800, 600
BASE_BALL_SPEED = 4
MAX_BALL_SPEED = 15
FRAME_DELAY = 20  # milliseconds

# ──────────────────────────────────────────────────────────────────────────────
# CLASSES
# ──────────────────────────────────────────────────────────────────────────────

class Paddle(turtle.Turtle):
    def __init__(self, x_pos):
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)

    def move_up(self):
        if self.ycor() < WIN_HEIGHT//2 - 40:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -WIN_HEIGHT//2 + 40:
            self.sety(self.ycor() - 20)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("yellow")
        self.penup()
        self.reset()

    def reset(self):
        self.goto(0, 0)
        self.dx = BASE_BALL_SPEED * random.choice((1, -1))
        self.dy = BASE_BALL_SPEED * random.choice((1, -1))

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        # reverse X and slightly increase speed, cap at MAX_BALL_SPEED
        new_speed = min(abs(self.dx) * 1.02, MAX_BALL_SPEED)
        self.dx = -new_speed if self.dx > 0 else new_speed

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, WIN_HEIGHT//2 - 40)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Left: {self.left_score}    Right: {self.right_score}",
                   align="center", font=("Courier", 24, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update()

    def right_point(self):
        self.right_score += 1
        self.update()

# ──────────────────────────────────────────────────────────────────────────────
# GAME SETUP & LOOP
# ──────────────────────────────────────────────────────────────────────────────

class PongMaster:
    def __init__(self):
        # screen
        self.wn = turtle.Screen()
        self.wn.title("🏓 PongMaster")
        self.wn.bgcolor("black")
        self.wn.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
        self.wn.tracer(0)

        self.draw_border()

        # game objects
        self.left_paddle = Paddle(-WIN_WIDTH//2 + 40)
        self.right_paddle = Paddle(WIN_WIDTH//2 - 40)
        self.ball = Ball()
        self.scoreboard = Scoreboard()

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

        # paddle collisions
        if (self.ball.xcor() > WIN_WIDTH//2 - 60 and
            abs(self.ball.ycor() - self.right_paddle.ycor()) < 50):
            self.ball.setx(WIN_WIDTH//2 - 60)
            self.ball.bounce_x()

        if (self.ball.xcor() < -WIN_WIDTH//2 + 60 and
            abs(self.ball.ycor() - self.left_paddle.ycor()) < 50):
            self.ball.setx(-WIN_WIDTH//2 + 60)
            self.ball.bounce_x()

        # scoring: bounce off side wall
        if abs(self.ball.xcor()) > WIN_WIDTH//2 - 10:
            if self.ball.xcor() > 0:
                self.scoreboard.left_point()
            else:
                self.scoreboard.right_point()

            self.ball.bounce_x()

            # check win
            if self.scoreboard.left_score == 10:
                return self.end_game("Left")
            if self.scoreboard.right_score == 10:
                return self.end_game("Right")

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

if __name__ == "__main__":
    PongMaster()
