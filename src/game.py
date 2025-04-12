import turtle
from paddles import Paddle
from src.ball import Ball

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Pong Master")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

        self.paddle_left = Paddle(-350, 0)
        self.paddle_right = Paddle(350, 0)
        self.ball = Ball()

        # Difficulty settings
        self.difficulty = "normal"  # Default difficulty

        self.screen.listen()
        self.screen.onkey(self.paddle_left.move_up, "w")
        self.screen.onkey(self.paddle_left.move_down, "s")
        self.screen.onkey(self.paddle_right.move_up, "Up")
        self.screen.onkey(self.paddle_right.move_down, "Down")

    def show_menu(self):
        # This is where you can display a simple text menu
        print("Welcome to Pong Master!")
        print("Choose difficulty: Easy, Normal, Hard")

        self.difficulty = input("Enter difficulty: ").lower()

        if self.difficulty == "easy":
            self.ball.speed = 1
        elif self.difficulty == "normal":
            self.ball.speed = 2
        elif self.difficulty == "hard":
            self.ball.speed = 3
        else:
            print("Invalid choice, defaulting to normal")
            self.difficulty = "normal"
            self.ball.speed = 2

        self.run()

    def run(self):
        while True:
            self.screen.update()
            self.ball.move()

            # Move paddles based on user input
            if self.paddle_left.ycor() < 250:
                self.paddle_left.move_up()
            if self.paddle_left.ycor() > -240:
                self.paddle_left.move_down()

            if self.paddle_right.ycor() < 250:
                self.paddle_right.move_up()
            if self.paddle_right.ycor() > -240:
                self.paddle_right.move_down()

            # Ball-paddle collision detection
            if self.ball.xcor() > 340 and self.ball.xcor() < 350 and (self.ball.ycor() < self.paddle_right.ycor() + 50 and self.ball.ycor() > self.paddle_right.ycor() - 50):
                self.ball.dx *= -1

            if self.ball.xcor() < -340 and self.ball.xcor() > -350 and (self.ball.ycor() < self.paddle_left.ycor() + 50 and self.ball.ycor() > self.paddle_left.ycor() - 50):
                self.ball.dx *= -1

            # Ball out of bounds
            if self.ball.xcor() > 390:
                self.ball.reset_position()
            if self.ball.xcor() < -390:
                self.ball.reset_position()

            # Adding delay to the game loop for a smoother experience
            turtle.delay(10)
