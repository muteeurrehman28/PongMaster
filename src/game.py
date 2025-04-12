from src.ball import Ball  # Correct the import path for Ball class
from src.paddles import Paddle
import turtle

# Constants for ball speeds based on difficulty
EASY_SPEED = 0.1
MEDIUM_SPEED = 0.2
HARD_SPEED = 0.3

class Game:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("PongMaster Game")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)  # Turn off automatic screen updates

        self.paddle_left = Paddle(-350, 0)
        self.paddle_right = Paddle(350, 0)
        self.ball = Ball()

    def show_menu(self):
        # Create the menu text and options
        menu_text = turtle.Turtle()
        menu_text.hideturtle()
        menu_text.color("white")
        menu_text.penup()
        menu_text.goto(0, 100)
        menu_text.write("PongMaster Game", align="center", font=("Courier", 24, "normal"))

        menu_text.goto(0, 50)
        menu_text.write("Select Difficulty", align="center", font=("Courier", 18, "normal"))

        menu_text.goto(0, 0)
        menu_text.write("1: Easy", align="center", font=("Courier", 14, "normal"))

        menu_text.goto(0, -30)
        menu_text.write("2: Medium", align="center", font=("Courier", 14, "normal"))

        menu_text.goto(0, -60)
        menu_text.write("3: Hard", align="center", font=("Courier", 14, "normal"))

        self.window.update()  # Update the window after writing text

        # Wait for user selection (1, 2, or 3 for difficulty)
        difficulty = None
        while difficulty is None:
            difficulty = self.window.textinput("Select Difficulty", "Enter 1 for Easy, 2 for Medium, or 3 for Hard:")
            if difficulty == "1":
                self.ball.dx = EASY_SPEED
                self.ball.dy = EASY_SPEED
            elif difficulty == "2":
                self.ball.dx = MEDIUM_SPEED
                self.ball.dy = MEDIUM_SPEED
            elif difficulty == "3":
                self.ball.dx = HARD_SPEED
                self.ball.dy = HARD_SPEED
            else:
                difficulty = None  # Invalid input, ask again

        # Start the game once difficulty is chosen
        self.run()

    def run(self):
        while True:
            self.window.update()  # Update the screen manually to avoid auto-refresh

            self.ball.move()
            self.paddle_left.move()
            self.paddle_right.move()

            # Check for collisions with top and bottom borders
            if self.ball.ycor() > 290:
                self.ball.dy = -abs(self.ball.dy)
            elif self.ball.ycor() < -290:
                self.ball.dy = abs(self.ball.dy)

            # Check for ball out of bounds (left or right)
            if self.ball.xcor() > 390:
                self.ball.goto(0, 0)  # Reset to the center
                self.ball.dx = -self.ball.dx  # Reverse ball direction
            elif self.ball.xcor() < -390:
                self.ball.goto(0, 0)  # Reset to the center
                self.ball.dx = -self.ball.dx  # Reverse ball direction
